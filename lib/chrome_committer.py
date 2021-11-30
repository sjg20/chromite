# Copyright 2018 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Commits files to the chromium git repository."""

import logging
import os

from chromite.lib import commandline
from chromite.lib import constants
from chromite.lib import cros_build_lib
from chromite.lib import git
from chromite.lib import osutils


class CommitError(Exception):
  """Raised if the commit failed."""


class ChromeCommitter(object):
  """Committer object responsible for committing a git change."""

  def __init__(self, user_email, workdir, dryrun=False, cq=False):
    logging.info('user_email=%s, checkout_dir=%s', user_email, workdir)
    self.author = user_email
    self._checkout_dir = workdir
    self._git_committer_args = ['-c', 'user.email=%s' % user_email,
                                '-c', 'user.name=%s' % user_email]
    self._commit_msg = ''
    self._dryrun = dryrun
    self._cq = cq
    assert not (dryrun and cq), "Can't CQ+1 and CQ+2 simultaneously."

  def __del__(self):
    self.Cleanup()

  def FullPath(self, file_path):
    """Returns the full path in the source tree given a relative path.

    Args:
      file_path: Path of file.

    Returns:
      Full path rooted in source checkout.
    """
    if os.path.isabs(file_path):
      return file_path
    return os.path.join(self._checkout_dir, file_path)

  def Checkout(self, sparse_checkout):
    """Checks out chrome into tmp checkout dir.

    Args:
      sparse_checkout: List of file paths to fetch.
    """
    assert isinstance(sparse_checkout, list)
    sparse_checkout += ['codereview.settings', 'WATCHLISTS']
    git.ShallowFetch(self._checkout_dir, constants.CHROMIUM_GOB_URL,
                     sparse_checkout=sparse_checkout)
    git.CreateBranch(self._checkout_dir, 'auto-commit-branch')

  def Commit(self, file_paths, commit_msg):
    """Commits files listed in |file_paths|.

    Args:
      file_paths: List of files to commit.
      commit_msg: Message to use in commit.
    """
    assert file_paths and isinstance(file_paths, list)
    # Make paths absolute and ensure they exist.
    for i, file_path in enumerate(file_paths):
      if not os.path.isabs(file_path):
        file_paths[i] = self.FullPath(file_path)
      if not os.path.exists(file_paths[i]):
        raise CommitError('Invalid path: %s' % file_paths[i])

    self._commit_msg = 'Automated Commit: ' + commit_msg
    try:
      for file_path in file_paths:
        git.AddPath(file_path)
      commit_args = ['commit', '-m', self._commit_msg]
      git.RunGit(self._checkout_dir, self._git_committer_args + commit_args,
                 print_cmd=True, stderr=True, capture_output=False)
    except cros_build_lib.RunCommandError as e:
      raise CommitError('Could not create git commit: %r' % e)

  def Upload(self, publish=True):
    """Uploads the change to gerrit.

    Args:
      publish: If True, will publish the CL after uploading and notify the
          reviewers. Stays in WIP mode otherwise.
    """
    logging.info('Uploading commit.')

    try:
      # Run 'git cl upload' with --bypass-hooks to skip running scripts that are
      # not part of the shallow checkout, -f to skip editing the CL message,
      upload_args = self._git_committer_args + [
          'cl', 'upload', '-v', '-m', self._commit_msg, '--bypass-hooks', '-f',
          '--reviewers', constants.CHROME_GARDENER_REVIEW_EMAIL,
          '--set-bot-commit']
      if publish:
        # Marks CL as ready.
        upload_args += ['--send-mail']
      if self._cq:
        upload_args += ['--use-commit-queue']
      elif self._dryrun:
        upload_args += ['--dry-run']
      git.RunGit(self._checkout_dir, upload_args, print_cmd=True,
                 stderr=True, capture_output=False)
    except cros_build_lib.RunCommandError as e:
      # Log the change for debugging.
      git.RunGit(self._checkout_dir, ['--no-pager', 'log', '--pretty=full'],
                 capture_output=False)
      raise CommitError('Could not submit: %r' % e)

    logging.info('Submitted to CQ.')

  def Cleanup(self):
    """Remove chrome checkout."""
    osutils.RmDir(self._checkout_dir, ignore_missing=True)

  @staticmethod
  def GetParser():
    """Returns parser for ChromeCommitter.

    Returns:
      Parser for ChromeCommitter.
    """
    # We need to use the account used by the builder to upload git CLs when
    # generating CLs.
    default_git_account = None
    if cros_build_lib.HostIsCIBuilder(golo_only=True):
      default_git_account = 'chromeos-commit-bot@chromium.org'
    elif cros_build_lib.HostIsCIBuilder(gce_only=True):
      default_git_account = '3su6n15k.default@developer.gserviceaccount.com'

    parser = commandline.ArgumentParser(usage=__doc__, add_help=False)
    parser.add_argument('--dryrun', action='store_true', default=False,
                        help="Don't commit changes or send out emails.")
    parser.add_argument('--user_email', required=False,
                        default=default_git_account,
                        help='Email address to use when comitting changes.')
    parser.add_argument('--workdir',
                        default=os.path.join(os.getcwd(), 'chrome_src'),
                        help=('Path to a checkout of the chrome src. '
                              'Defaults to PWD/chrome_src'))
    return parser
