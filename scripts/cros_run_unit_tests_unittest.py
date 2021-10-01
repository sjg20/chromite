# Copyright 2018 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unit tests for cros_run_unit_tests.py."""

from chromite.lib import cros_test_lib
from chromite.scripts import cros_run_unit_tests


pytestmark = cros_test_lib.pytestmark_inside_only


class DetermineBoardPackagesTest(cros_test_lib.TestCase):
  """Tests that package determination returns a non-empty set"""

  def testNonEmptyPackageSet(self):
    """Asserts that the deps of a known package are non-empty"""
    self.assertTrue(cros_run_unit_tests.determine_packages(
        '/', ('virtual/implicit-system',)))
