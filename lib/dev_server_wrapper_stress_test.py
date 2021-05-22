# Copyright (c) 2013 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Stress test for dev_server_wrapper.

Test script runs a long time stressing the ability to start and stop the
dev_server_wrapper. Even very rare hangs will cause significant build flake.
"""

import sys

from chromite.lib import cros_logging as logging
from chromite.lib import dev_server_wrapper


assert sys.version_info >= (3, 6), 'This module requires Python 3.6+'


_ITERATIONS = 10000


def main(_argv):
  logging.getLogger().setLevel(logging.DEBUG)
  for i in range(_ITERATIONS):
    print('Iteration {}'.format(i))
    wrapper = dev_server_wrapper.DevServerWrapper()
    print('Starting')
    wrapper.Start()
    print('Stopping')
    wrapper.Stop()
