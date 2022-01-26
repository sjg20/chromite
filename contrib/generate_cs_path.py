# Copyright 2022 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Use with an IDE to copy a link to the current file/line to your clipboard.

Currently only works locally and if using X11.

IDE integration instructions. Please add your IDE if it's not listed, or update
the instructions if they're vague or out of date!

For Intellij:
Create a new External Tool (Settings > Tools > External Tools).
Tool Settings:
  Program: ~/chromiumos/chromite/contrib/generate_cs_path
  Arguments: $FilePath$ -l $LineNumber$

For VSCode:
Create a custom task (code.visualstudio.com/docs/editor/tasks#_custom-tasks)
with the command:
  ~/chromiumos/chromite/contrib/generate_cs_path ${file} -l ${lineNumber}
"""

import os
from pathlib import Path

from chromite.lib import commandline
from chromite.lib import constants
from chromite.lib import cros_build_lib
from chromite.lib import git

# HEAD is the ref for the codesearch repo, not the project itself.
_PUBLIC_CS_BASE = (
    'https://source.chromium.org/chromiumos/chromiumos/codesearch/+/HEAD:')


def GetParser():
  """Build the argument parser."""
  parser = commandline.ArgumentParser(description=__doc__)

  parser.add_argument('-l', '--line', type=int, help='Line number.')

  parser.add_argument(
      '--open',
      action='store_true',
      default=False,
      help='Open the link in a browser rather than copying it to the clipboard.'
  )

  parser.add_argument('path', type='path', help='Path to a file.')

  return parser


def _ParseArguments(argv):
  """Parse and validate arguments."""
  parser = GetParser()
  opts = parser.parse_args(argv)

  opts.path = Path(opts.path).relative_to(constants.SOURCE_ROOT)

  opts.Freeze()
  return opts


def main(argv):
  opts = _ParseArguments(argv)

  checkout = git.ManifestCheckout.Cached(opts.path)

  checkout_path = None
  for checkout_path in checkout.checkouts_by_path:
    try:
      relative_path = opts.path.relative_to(checkout_path)
    except ValueError:
      continue
    else:
      break
  else:
    cros_build_lib.Die('No project found for %s.', opts.path)

  line = f';l={opts.line}' if opts.line else ''

  cs_str = f'{_PUBLIC_CS_BASE}{checkout_path}/{relative_path}{line}'

  if opts.open:
    cmd = ['xdg-open', cs_str]
    os.execvp(cmd[0], cmd)
  else:
    cros_build_lib.run(['xclip', '-selection', 'clipboard'], input=cs_str)
