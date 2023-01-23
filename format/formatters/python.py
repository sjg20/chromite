# Copyright 2022 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Python formatter."""

import os
from pathlib import Path
from typing import Optional, Union

from chromite.lib import constants
from chromite.lib import cros_build_lib
from chromite.lib import git


def _find_pyproject_toml(
    path: Optional[Union[str, os.PathLike]] = None
) -> Path:
    """Locate pyproject.toml to use with |path|."""
    if path:
        project_root = git.FindGitTopLevel(path)
        for dir_path in Path(path).resolve().parents:
            config_path = dir_path / "pyproject.toml"
            try:
                if "[tool.black]" in config_path.read_text(encoding="utf-8"):
                    return config_path
            except FileNotFoundError:
                pass

            if dir_path == project_root:
                break

    return Path(constants.CHROMITE_DIR) / "pyproject.toml"


def Data(
    data: str,
    path: Optional[Union[str, os.PathLike]] = None,
) -> str:
    """Format python |data|.

    Args:
        data: The file content to lint.
        path: The file name for diagnostics/configs/etc...

    Returns:
        Formatted data.
    """
    # We run through isort first to enforce module sorting order, then run that
    # result through black. We can't run isort independently (or after black)
    # because it has some known edge cases where it formats in black-incompatible
    # ways. See b/235526476 for details.
    result = cros_build_lib.run(
        [
            Path(constants.CHROMITE_SCRIPTS_DIR) / "isort",
            "--settings-file",
            Path(constants.CHROMITE_DIR) / ".isort.cfg",
            "-",
            "-d",
        ],
        capture_output=True,
        input=data,
        encoding="utf-8",
    )

    result = cros_build_lib.run(
        [
            Path(constants.CHROMITE_SCRIPTS_DIR) / "black",
            f"--config={_find_pyproject_toml(path)}",
            "-",
        ],
        input=result.stdout,
        capture_output=True,
        encoding="utf-8",
    )

    return result.stdout
