# Copyright 2016 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Bootstrap for cbuildbot.

This script is intended to checkout chromite on the branch specified by -b or
--branch (as normally accepted by cbuildbot), and then invoke cbuildbot. Most
arguments are not parsed, only passed along. If a branch is not specified, this
script will use 'master'.

Among other things, this allows us to invoke build configs that exist on a given
branch, but not on TOT.
"""

from __future__ import print_function

import functools
import os

from chromite.cbuildbot import repository
from chromite.cbuildbot.stages import sync_stages
from chromite.lib import config_lib
from chromite.lib import cros_build_lib
from chromite.lib import cros_logging as logging
from chromite.lib import osutils
from chromite.scripts import cbuildbot


# This number should be incremented when we change the layout of the buildroot
# in a non-backwards compatible way. This wipes all buildroots.
BUILDROOT_BUILDROOT_LAYOUT = 1


def StageDecorator(functor):
  """A Decorator that adds buildbot stage tags around a method.

  It uses the method name as the stage name, and assumes failure on exception.
  """
  @functools.wraps(functor)
  def wrapped_functor(*args, **kwargs):
    try:
      logging.PrintBuildbotStepName(functor.__name__)
      return functor(*args, **kwargs)
    except Exception:
      logging.PrintBuildbotStepFailure()
      raise

  return wrapped_functor


def PreParseArguments(argv):
  """Extract the branch name from cbuildbot command line arguments.

  Ignores all arguments, other than the branch name.

  Args:
    argv: The command line arguments to parse.

  Returns:
    Branch as a string ('master' if nothing is specified).
  """
  parser = cbuildbot.CreateParser()
  options, args = cbuildbot.ParseCommandLine(parser, argv)

  # This option isn't required for cbuildbot, but is for us.
  if not options.buildroot:
    cros_build_lib.Die('--buildroot is a required option.')

  # Save off the build targets, in a mirror of cbuildbot code.
  options.build_targets = args
  options.Freeze()

  return options


def GetBuildrootState(buildroot):
  state_file = os.path.join(buildroot, '.cbuildbot_launch_state')

  try:
    state = osutils.ReadFile(state_file)
    buildroot_layout, branchname = state.split()
    buildroot_layout = int(buildroot_layout)
    return buildroot_layout, branchname
  except (IOError, ValueError):
    # If we are unable to either read or parse the state file, we get here.
    return 0, ''


def SetBuildrootState(branchname, buildroot):
  assert branchname
  state_file = os.path.join(buildroot, '.cbuildbot_launch_state')
  new_state = '%d %s' % (BUILDROOT_BUILDROOT_LAYOUT, branchname)
  osutils.WriteFile(state_file, new_state)


@StageDecorator
def CleanBuildroot(branchname, buildroot):
  """Some kinds of branch transitions break builds.

  This method tries to detect cases where that can happen, and clobber what's
  needed to succeed. However, the clobbers are costly, and should be avoided
  if necessary.

  Args:
    branchname: Name of branch to checkout.
    buildroot: Directory with old buildroot to clean as needed.
  """
  old_buildroot_layout, old_branch = GetBuildrootState(buildroot)

  if old_buildroot_layout != BUILDROOT_BUILDROOT_LAYOUT:
    logging.PrintBuildbotStepText('Unknown layout: Wiping buildroot.')
    osutils.RmDir(buildroot, ignore_missing=True, sudo=True)

  elif old_branch != branchname:
    logging.PrintBuildbotStepText('Branch change: Cleaning buildroot.')
    logging.info('Unmatched branch: %s -> %s', old_branch, branchname)

    logging.info('Remove Chroot.')
    osutils.RmDir(os.path.join(buildroot, 'chroot'),
                  ignore_missing=True, sudo=True)

    logging.info('Remove Chrome checkout.')
    osutils.RmDir(os.path.join(buildroot, '.cache', 'distfiles'),
                  ignore_missing=True, sudo=True)

  # Ensure buildroot exists.
  osutils.SafeMakedirs(buildroot)
  SetBuildrootState(branchname, buildroot)


@StageDecorator
def InitialCheckout(branchname, buildroot, git_cache_dir):
  """Preliminary ChromeOS checkout.

  Perform a complete checkout of ChromeOS on the specified branch. This does NOT
  match what the build needs, but ensures the buildroot both has a 'hot'
  checkout, and is close enough that the branched cbuildbot can successfully get
  the right checkout.

  This checks out full ChromeOS, even if a ChromiumOS build is going to be
  performed. This is because we have no knowledge of the build config to be
  used.

  Args:
    branchname: Name of branch to checkout.
    buildroot: Directory to checkout into.
    git_cache_dir: Directory to use for git cache. None to not use it.
  """
  logging.PrintBuildbotStepText('Branch: %s' % branchname)
  logging.info('Bootstrap script starting initial sync on branch: %s',
               branchname)

  site_config = config_lib.GetConfig()
  manifest_url = site_config.params['MANIFEST_INT_URL']

  repo = repository.RepoRepository(manifest_url, buildroot,
                                   branch=branchname,
                                   git_cache_dir=git_cache_dir)
  repo.Sync()


@StageDecorator
def RunCbuildbot(options):
  """Start cbuildbot in specified directory with all arguments.

  Args:
    options: Parse command line options.

  Returns:
    Return code of cbuildbot as an integer.
  """
  logging.info('Bootstrap cbuildbot in: %s', options.buildroot)
  cbuildbot_path = os.path.join(
      options.buildroot, 'chromite', 'bin', 'cbuildbot')

  cmd = sync_stages.BootstrapStage.FilterArgsForTargetCbuildbot(
      options.buildroot, cbuildbot_path, options)

  cros_build_lib.RunCommand(cmd, cwd=options.buildroot)


def ConfigureGlobalEnvironment():
  """Setup process wide environmental changes."""
  # Set umask to 022 so files created by buildbot are readable.
  os.umask(0o22)


def main(argv):
  """main method of script.

  Args:
    argv: All command line arguments to pass as list of strings.

  Returns:
    Return code of cbuildbot as an integer.
  """
  logging.EnableBuildbotMarkers()
  ConfigureGlobalEnvironment()

  options = PreParseArguments(argv)

  branchname = options.branch or 'master'
  buildroot = options.buildroot
  git_cache_dir = options.git_cache_dir

  # Sometimes, we have to cleanup things that can break cbuildbot, especially
  # on the branch.
  CleanBuildroot(branchname, buildroot)

  # Get a checkout close enough the branched cbuildbot can handle it.
  InitialCheckout(branchname, buildroot, git_cache_dir)

  # Run cbuildbot inside the full ChromeOS checkout, on the specified branch.
  try:
    RunCbuildbot(options)
  except cros_build_lib.RunCommandError as e:
    return e.result.returncode
