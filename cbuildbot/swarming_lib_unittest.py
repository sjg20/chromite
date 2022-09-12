# Copyright 2018 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unit tests for swarming_lib module."""

from chromite.cbuildbot import swarming_lib
from chromite.lib import cros_test_lib


class SwarmingLibTest(cros_test_lib.RunCommandTestCase):
    """Unit test of swarming_lib module."""

    def testEnv(self):
        """Validate that 'SWARMING_TASK_ID' is removed from swarming cmds."""
        swarming_lib.RunSwarmingCommand(["cmd"], "test-server")
        swarming_lib.RunSwarmingCommand(
            ["cmd"], "test-server", env={"SWARMING_TASK_ID": "foo"}
        )

        for _, kwargs in self.rc.call_args_list:
            self.assertIn("env", kwargs)
            self.assertNotIn("SWARMING_TASK_ID", kwargs["env"])
