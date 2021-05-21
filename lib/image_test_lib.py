# Copyright 2014 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Functions related to image tests."""

import os
import sys
import unittest

from chromite.lib import cros_logging as logging
from chromite.lib import perf_uploader


assert sys.version_info >= (3, 6), 'This module requires Python 3.6+'


# File extension for file containing performance values.
PERF_EXTENSION = '.perf'
# Symlinks to mounted partitions.
ROOT_A = 'dir-ROOT-A'
STATEFUL = 'dir-STATE'


def IsPerfFile(file_name):
  """Return True if |file_name| may contain perf values."""
  return file_name.endswith(PERF_EXTENSION)


class _BoardAndDirectoryMixin(object):
  """A mixin to hold image test's specific info."""

  _board = None
  _result_dir = None

  def SetBoard(self, board):
    self._board = board

  def SetResultDir(self, result_dir):
    self._result_dir = result_dir


class ImageTestCase(unittest.TestCase, _BoardAndDirectoryMixin):
  """Subclass unittest.TestCase to provide utility methods for image tests.

  Tests MUST use prefix "Test" (e.g.: TestLinkage, TestDiskSpace), not "test"
  prefix, in order to be picked up by the test runner.

  Tests are run inside chroot. Tests are run as root. DO NOT modify any mounted
  partitions.

  The current working directory is set up so that "ROOT_A", and "STATEFUL"
  constants refer to the mounted partitions. The partitions are mounted
  readonly.

    current working directory
      + ROOT_A
        + /
          + bin
          + etc
          + usr
          ...
      + STATEFUL
        + var_overlay
        ...
  """

  def _GeneratePerfFileName(self):
    """Return a perf file name for this test.

    The file name is formatted as:

      image_test.<test_class><PERF_EXTENSION>

    e.g.:

      image_test.DiskSpaceTest.perf
    """
    test_name = 'image_test.%s' % self.__class__.__name__
    file_name = '%s%s' % (test_name, PERF_EXTENSION)
    file_name = os.path.join(self._result_dir, file_name)
    return file_name

  @staticmethod
  def GetTestName(file_name):
    """Return the test name from a perf |file_name|.

    Args:
      file_name: A path to the perf file as generated by _GeneratePerfFileName.

    Returns:
      The qualified test name part of the file name.
    """
    file_name = os.path.basename(file_name)
    pos = file_name.rindex('.')
    return file_name[:pos]

  def OutputPerfValue(self, description, value, units,
                      higher_is_better=True, graph=None):
    """Record a perf value.

    If graph name is not provided, the test method name will be used as the
    graph name.

    Args:
      description: A string description of the value such as "partition-0". A
        special description "ref" is taken as the reference.
      value: A float value.
      units: A string describing the unit of measurement such as "KB", "meter".
      higher_is_better: A boolean indicating if higher value means better
        performance.
      graph: A string name of the graph this value will be plotted on. If not
        provided, the graph name will take the test method name.
    """
    if not self._result_dir:
      logging.warning('Result directory is not set. Ignore OutputPerfValue.')
      return
    if graph is None:
      graph = self._testMethodName
    file_name = self._GeneratePerfFileName()
    perf_uploader.OutputPerfValue(file_name, description, value, units,
                                  higher_is_better, graph)


class ImageTestSuite(unittest.TestSuite, _BoardAndDirectoryMixin):
  """Wrap around unittest.TestSuite to pass more info to the actual tests."""

  def run(self, result, debug=False):
    for t in self._tests:
      t.SetResultDir(self._result_dir)
      t.SetBoard(self._board)
    return super(ImageTestSuite, self).run(result)


class ImageTestRunner(unittest.TextTestRunner, _BoardAndDirectoryMixin):
  """Wrap around unittest.TextTestRunner to pass more info down the chain."""

  def run(self, test):
    test.SetResultDir(self._result_dir)
    test.SetBoard(self._board)
    return super(ImageTestRunner, self).run(test)
