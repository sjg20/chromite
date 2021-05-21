# Copyright 2016 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""CLI for running Chrome OS tests from lib/cros_test.py."""

import sys

from chromite.lib import cros_test


assert sys.version_info >= (3, 6), 'This module requires Python 3.6+'


def main(argv):
  opts = cros_test.ParseCommandLine(argv)
  opts.Freeze()
  return cros_test.CrOSTest(opts).Run()
