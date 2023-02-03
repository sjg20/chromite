# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test the python module."""

import pytest

from chromite.format.formatters import python


# pylint: disable=protected-access


# None means input is already formatted to avoid having to repeat.
@pytest.mark.parametrize(
    "data,exp",
    (
        ("", None),
        ("#", ""),
        ("\n#\n", ""),
        ("#\n#!/\n#\n", "#!/\n"),
        ("#!/\n\n# foo\n", "#!/\n# foo\n"),
        ('# foo\n#\n"""."""\n', '# foo\n\n"""."""\n'),
    ),
)
def test_check_custom_format(data, exp):
    """Verify inputs match expected outputs."""
    if exp is None:
        exp = data
    assert exp == python._custom_format_data(data)
