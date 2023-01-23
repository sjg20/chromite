# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Provides utility for formatting XML files.

Not all XML files are formatted the same unfortunately.
"""

import os
from typing import Optional, Union
from xml.etree import ElementTree

from chromite.format.formatters import repo_manifest
from chromite.format.formatters import whitespace


def Data(
    data: str,
    # pylint: disable=unused-argument
    path: Optional[Union[str, os.PathLike]] = None,
) -> str:
    """Format XML |data|.

    Args:
        data: The file content to lint.
        path: The file name for diagnostics/configs/etc...

    Returns:
        Formatted data.
    """
    root = ElementTree.fromstring(data)
    if root.tag == "manifest":
        data = repo_manifest.Data(data)
    else:
        data = whitespace.Data(data)
    return data
