# Copyright 2015 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Store and manage Mob* Monitor checkfiles."""

from __future__ import print_function

import cherrypy
import collections
import imp
import inspect
import os
import time

from cherrypy.process import plugins
from chromite.lib import cros_logging as logging


HCEXECUTION_IN_PROGRESS = 0
HCEXECUTION_COMPLETED = 1

HCSTATUS_HEALTHY = 0

IN_PROGRESS_DESCRIPTION = 'Health check is currently executing.'
NULL_DESCRIPTION = ''
EMPTY_ACTIONS = []
HEALTHCHECK_STATUS = collections.namedtuple('healthcheck_status',
                                            ['name', 'health', 'description',
                                             'actions'])

HEALTH_CHECK_METHODS = ['Check', 'Diagnose']

CHECK_INTERVAL_DEFAULT_SEC = 30
HEALTH_CHECK_DEFAULT_ATTRIBUTES = {'CHECK_INTERVAL': CHECK_INTERVAL_DEFAULT_SEC}

CHECKFILE_DIR = '/etc/mobmonitor/checkfiles/'
CHECKFILE_ENDING = '_check.py'

SERVICE_STATUS = collections.namedtuple('service_status',
                                        ['service', 'health', 'healthchecks'])


class CollectionError(Exception):
  """Raise when an error occurs during checkfile collection."""


def MapHealthcheckStatusToDict(hcstatus):
  """Map a manager.HEALTHCHECK_STATUS named tuple to a dictionary.

  Args:
    hcstatus: A HEALTHCHECK_STATUS object.

  Returns:
    A dictionary version of the HEALTHCHECK_STATUS object.
  """
  return {'name': hcstatus.name, 'health': hcstatus.health,
          'description': hcstatus.description,
          'actions': [a.__name__ for a in hcstatus.actions]}


def MapServiceStatusToDict(status):
  """Map a manager.SERVICE_STATUS named tuple to a dictionary.

  Args:
    status: A SERVICE_STATUS object.

  Returns:
    A dictionary version of the SERVICE_STATUS object.
  """
  hcstatuses = [
      MapHealthcheckStatusToDict(hcstatus) for hcstatus in status.healthchecks]
  return {'service': status.service, 'health': status.health,
          'healthchecks': hcstatuses}


def isHealthcheckHealthy(hcstatus):
  """Test if a health check is perfectly healthy.

  Args:
    hcstatus: A HEALTHCHECK_STATUS named tuple.

  Returns:
    True if the hcstatus is perfectly healthy, False otherwise.
  """
  if not isinstance(hcstatus, HEALTHCHECK_STATUS):
    return False
  return hcstatus.health and not (hcstatus.description or hcstatus.actions)


def isServiceHealthy(status):
  """Test if a service is perfectly healthy.

  Args:
    status: A SERVICE_STATUS named tuple.

  Returns:
    True if the status is perfectly healthy, False otherwise.
  """
  if not isinstance(status, SERVICE_STATUS):
    return False
  return status.health and not status.healthchecks


def DetermineHealthcheckStatus(hcname, healthcheck):
  """Determine the healthcheck status.

  Args:
    hcname: A string. The name of the health check.
    healthcheck: A healthcheck object.

  Returns:
    A HEALTHCHECK_STATUS named tuple.
  """
  try:
    # Run the health check condition.
    result = healthcheck.Check()

    # Determine the healthcheck's status.
    health = result >= HCSTATUS_HEALTHY

    if result == HCSTATUS_HEALTHY:
      return HEALTHCHECK_STATUS(hcname, health, NULL_DESCRIPTION,
                                EMPTY_ACTIONS)

    description, actions = healthcheck.Diagnose(result)
    return HEALTHCHECK_STATUS(hcname, health, description, actions)

  except Exception as e:
    # Checkfiles may contain all kinds of errors! We do not want the
    # Mob* Monitor to fail, so catch generic exceptions.
    logging.error('Failed to execute health check %s: %s', hcname, e)
    return HEALTHCHECK_STATUS(hcname, False,
                              'Failed to execute the health check.'
                              ' Please review the health check file.',
                              EMPTY_ACTIONS)


def IsHealthCheck(obj):
  """A sanity check to see if a class implements the health check interface.

  Args:
    obj: A Python object.

  Returns:
    True if obj has 'check' and 'diagnose' functions.
    False otherwise.
  """
  return all(callable(getattr(obj, m, None)) for m in HEALTH_CHECK_METHODS)


def ApplyHealthCheckAttributes(obj):
  """Set default values for health check attributes.

  Args:
    obj: A Python object.

  Returns:
    The same object with default attribute values set if they were not
    already defined.
  """
  for attr, default in HEALTH_CHECK_DEFAULT_ATTRIBUTES.iteritems():
    if not hasattr(obj, attr):
      setattr(obj, attr, default)

  return obj


def ImportFile(service, modulepath):
  """Import and collect health checks from the given module.

  Args:
    service: The name of the service this check module belongs to and
      for which the objects to import belong to.
    modulepath: The path of the module to import.

  Returns:
    A tuple containing the healthchecks defined in the module and the
    time of the module's last modification.

  Raises:
    SyntaxError may be raised by imp.load_source if the python file
      specified by modulepath has errors.
  """
  # Name and load the module from the module path. If service is 'testservice'
  # and the module path is '/path/to/checkdir/testservice/test_check.py',
  # the module name becomes 'testservice.test_check'.
  objects = []
  modname = '%s.%s' % (service,
                       os.path.basename(os.path.splitext(modulepath)[0]))
  module = imp.load_source(modname, modulepath)

  for name in dir(module):
    obj = getattr(module, name)
    if inspect.isclass(obj) and IsHealthCheck(obj):
      objects.append(ApplyHealthCheckAttributes(obj()))

  return objects, os.path.getmtime(modulepath)


class CheckFileManager(object):
  """Manage the health checks that are associated with each service."""

  def __init__(self, interval_sec=3, checkdir=CHECKFILE_DIR):
    if not os.path.exists(checkdir):
      raise CollectionError('Check directory does not exist: %s' % checkdir)

    self.interval_sec = interval_sec
    self.checkdir = checkdir
    self.monitor = None

    # service_checks is a dict of the following form:
    #
    #   {service_name: {hcname: (mtime, healthcheck)}}
    #
    # service_name: A string and is the name of the service.
    # hcname: A string and is the name of the health check.
    # mtime: The epoch time of the last modification of the check file.
    # healthcheck: The health check object.
    self.service_checks = {}

    # service_check_results is a dict of the following form:
    #
    #   {service_name: {hcname: (execution_status, exec_time,
    #                            healthcheck_status)}}
    #
    # service_name: As above.
    # hcname: As above.
    # execution_status: An integer. This will be one of the HCEXECUTION
    #   variables defined at the top of the file.
    # exec_time: The time of last execution.
    # healthcheck_status: A HEALTHCHECK_STATUS named tuple.
    self.service_check_results = {}

    # service_states is dict of the following form:
    #
    #   {service_name: service_status}
    #
    # service_name: As above.
    # service_status: A SERVICE_STATUS named tuple.
    self.service_states = {}

  def Update(self, service, objects, mtime):
    """Update the healthcheck objects for each service.

    Args:
      service: The service that the healthcheck corresponds to.
      objects: A list of healthcheck objects.
      mtime: The time of last modification of the healthcheck module.
    """
    for obj in objects:
      name = obj.__class__.__name__
      self.service_checks.setdefault(service, {})

      stored_mtime, _ = self.service_checks[service].get(name, (None, None))
      if stored_mtime is None or mtime > stored_mtime:
        self.service_checks[service][name] = (mtime, obj)
        logging.info('Updated healthcheck "%s" for service "%s" at time "%s"',
                     name, service, mtime)

  def Execute(self, force=False):
    """Execute all health checks and collect healthcheck status information.

    Args:
      force: Ignore the health check interval and execute the health checks.
    """
    for service, healthchecks in self.service_checks.iteritems():
      # Set default result dictionary if this is a new service.
      self.service_check_results.setdefault(service, {})

      for hcname, (_mtime, healthcheck) in healthchecks.iteritems():
        # Update if the record is stale or non-existent.
        etime = time.time()
        _, exec_time, status = self.service_check_results[service].get(
            hcname, (None, None, None))

        if exec_time is None or force or (
            etime > healthcheck.CHECK_INTERVAL + exec_time):
          # Record the execution status.
          status = HEALTHCHECK_STATUS(hcname, True, IN_PROGRESS_DESCRIPTION,
                                      EMPTY_ACTIONS)
          self.service_check_results[service][hcname] = (
              HCEXECUTION_IN_PROGRESS, etime, status)

          # TODO (msartori): Implement crbug.com/501959.
          #   This bug deals with handling slow health checks.

          status = DetermineHealthcheckStatus(hcname, healthcheck)

          # Update the execution and healthcheck status.
          self.service_check_results[service][hcname] = (
              HCEXECUTION_COMPLETED, etime, status)

  def ConsolidateServiceStates(self):
    """Consolidate health check results and determine service health states."""
    for service, results in self.service_check_results.iteritems():
      self.service_states.setdefault(service, {})

      quasi_or_unhealthy_checks = []
      for (_exec_status, _exec_stime, hcstatus) in results.itervalues():
        if not isHealthcheckHealthy(hcstatus):
          quasi_or_unhealthy_checks.append(hcstatus)

      health = all([hc.health for hc in quasi_or_unhealthy_checks])

      self.service_states[service] = SERVICE_STATUS(service, health,
                                                    quasi_or_unhealthy_checks)

  def CollectionExecutionCallback(self):
    """Callback for cherrypy Monitor. Collect checkfiles from the checkdir."""
    # Find all service check file packages.
    _, service_dirs, _ = next(os.walk(self.checkdir))
    for service_name in service_dirs:
      service_package = os.path.join(self.checkdir, service_name)

      # Import the package.
      try:
        file_, path, desc = imp.find_module(service_name, [self.checkdir])
        imp.load_module(service_name, file_, path, desc)
      except Exception as e:
        logging.warning('Failed to import package %s: %s', service_name, e)
        continue

      # Collect all of the service's health checks.
      for file_ in os.listdir(service_package):
        filepath = os.path.join(service_package, file_)
        if os.path.isfile(filepath) and file_.endswith(CHECKFILE_ENDING):
          try:
            healthchecks, mtime = ImportFile(service_name, filepath)
            self.Update(service_name, healthchecks, mtime)
          except Exception as e:
            logging.warning('Failed to import module %s.%s: %s',
                            service_name, file_[:-3], e)

    self.Execute()
    self.ConsolidateServiceStates()

  def StartCollectionExecution(self):
    # The Monitor frequency is mis-named. It's the time between
    # each callback execution.
    self.monitor = plugins.Monitor(cherrypy.engine,
                                   self.CollectionExecutionCallback,
                                   frequency=self.interval_sec)
    self.monitor.subscribe()

  def GetServiceList(self):
    """Return a list of the monitored services.

    Returns:
      A list of the services for which we have checks defined.
    """
    return self.service_states.keys()

  def GetStatus(self, service):
    """Query the current health state of the service.

    Args:
      service: The name of service that we are querying the health state of.

    Returns:
      A SERVICE_STATUS named tuple which has the following fields:
        service: A string. The service name.
        health: A boolean. True if all checks passed, False if not.
        healthchecks: A list of failed or quasi-healthy checks for the service.
          Each member of the list is a HEALTHCHECK_STATUS and details the
          appropriate repair actions for that particular health check.

      If service is not specified, a list of all service states is returned.
    """
    if not service:
      return self.service_states.values()

    return self.service_states.get(service, SERVICE_STATUS(service, False, []))

  def RepairService(self, service, action):
    """Execute the repair action on the specified service.

    Args:
      service: The name of the service to be repaired.
      action: The name of the action to execute.

    Returns:
      The same return value of GetStatus(service).
    """
    # No repair occurs if the service is not specified or is perfectly healthy.
    status = self.service_states.get(service, None)
    if status is None:
      return SERVICE_STATUS(service, False, [])
    elif isServiceHealthy(status):
      return self.GetStatus(service)

    # Check that at least one unhealthy/quasi-healthy check specifies this
    # repair actions. Actions are assumed to be service-centric at this point.
    repair_func = None
    for hc in status.healthchecks:
      for action_func in hc.actions:
        if action == action_func.__name__:
          repair_func = action_func
          break

    # TODO (msartori): Implement crbug.com/503373
    if repair_func is not None:
      repair_func()

      # Update the service status and return.
      # While actions are 'service-centric' from the perspective of the monitor,
      # actions may have system-wide effect, so we must re-check all services.
      self.Execute(force=True)
      self.ConsolidateServiceStates()

    return self.GetStatus(service)
