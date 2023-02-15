# Copyright 2012 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for the binpkg.py module."""

import os
import tempfile
from typing import List, Optional

from chromite.lib import binpkg
from chromite.lib import build_target_lib
from chromite.lib import cros_test_lib
from chromite.lib import gs_unittest
from chromite.lib import osutils
from chromite.lib import sysroot_lib


PACKAGES_CONTENT = """USE: test

CPV: chromeos-base/shill-0.0.1-r1

CPV: chromeos-base/test-0.0.1-r1
DEBUG_SYMBOLS: yes
"""


class FetchTarballsTest(cros_test_lib.MockTempDirTestCase):
    """Tests for GSContext that go over the network."""

    def testFetchFakePackages(self):
        """Pretend to fetch binary packages."""
        gs_mock = self.StartPatcher(gs_unittest.GSContextMock())
        gs_mock.SetDefaultCmdResult()
        uri = "gs://foo/bar"
        packages_uri = f"{uri}/Packages"
        packages_file = """URI: gs://foo

CPV: boo/baz
PATH boo/baz.tbz2
"""
        gs_mock.AddCmdResult(["cat", packages_uri], stdout=packages_file)

        binpkg.FetchTarballs([uri], self.tempdir)

    @cros_test_lib.pytestmark_network_test
    def testFetchRealPackages(self):
        """Actually fetch a real binhost from the network."""
        uri = "gs://chromeos-prebuilt/board/lumpy/paladin-R37-5905.0.0-rc2/packages"
        binpkg.FetchTarballs([uri], self.tempdir)


class DebugSymbolsTest(cros_test_lib.TempDirTestCase):
    """Tests for the debug symbols handling in binpkg."""

    def testDebugSymbolsDetected(self):
        """When generating the Packages file, DEBUG_SYMBOLS is updated."""
        osutils.WriteFile(
            os.path.join(
                self.tempdir, "chromeos-base/shill-0.0.1-r1.debug.tbz2"
            ),
            "hello",
            makedirs=True,
        )
        osutils.WriteFile(
            os.path.join(self.tempdir, "Packages"), PACKAGES_CONTENT
        )

        index = binpkg.GrabLocalPackageIndex(self.tempdir)
        self.assertEqual(
            index.packages[0]["CPV"], "chromeos-base/shill-0.0.1-r1"
        )
        self.assertEqual(index.packages[0].get("DEBUG_SYMBOLS"), "yes")
        self.assertFalse("DEBUG_SYMBOLS" in index.packages[1])


class PackageIndexTest(cros_test_lib.TempDirTestCase):
    """Package index tests."""

    def testReadWrite(self):
        """Sanity check that the read and write method work properly."""
        packages1 = os.path.join(self.tempdir, "Packages1")
        packages2 = os.path.join(self.tempdir, "Packages2")

        # Set some data.
        pkg_index = binpkg.PackageIndex()
        pkg_index.header["A"] = "B"
        pkg_index.packages = [
            {
                "CPV": "foo/bar",
                "KEY": "value",
            },
            {
                "CPV": "cat/pkg",
                "KEY": "also_value",
            },
        ]

        # Write the package index files using each writing method.
        pkg_index.modified = True
        pkg_index.WriteFile(packages1)
        with open(packages2, "w", encoding="utf-8") as f:
            pkg_index.Write(f)
        tmpf = pkg_index.WriteToNamedTemporaryFile()

        # Make sure the files are the same.
        fc1 = osutils.ReadFile(packages1)
        fc2 = osutils.ReadFile(packages2)
        fc3 = tmpf.read()
        self.assertEqual(fc1, fc2)
        self.assertEqual(fc1, fc3)

        # Make sure it parses out the same data we wrote.
        with open(packages1, encoding="utf-8") as f:
            read_index = binpkg.PackageIndex()
            read_index.Read(f)

        self.assertDictEqual(pkg_index.header, read_index.header)
        self.assertCountEqual(pkg_index.packages, read_index.packages)


class PackageIndexInfoTest(cros_test_lib.TestCase):
    """Package index info tests."""

    def _make_instance(self, sha, number, board, profile_name, location):
        """Return a binpkg.PackageIndexInfo instance."""
        return binpkg.PackageIndexInfo(
            snapshot_sha=sha,
            snapshot_number=number,
            build_target=build_target_lib.BuildTarget(name=board)
            if board
            else None,
            profile=sysroot_lib.Profile(name=profile_name)
            if profile_name
            else None,
            location=location,
        )

    def testEquality(self):
        """Test that equality checks work."""
        info = self._make_instance("SHA5", 5, "target", "profile", "LOCATION")
        self.assertEqual(
            info,
            self._make_instance("SHA5", 5, "target", "profile", "LOCATION"),
        )
        self.assertNotEqual(
            info,
            self._make_instance("XXXX", 5, "target", "profile", "LOCATION"),
        )
        self.assertNotEqual(
            info,
            self._make_instance("SHA5", 6, "target", "profile", "LOCATION"),
        )
        self.assertNotEqual(
            info,
            self._make_instance("SHA5", 5, "xxxxxx", "profile", "LOCATION"),
        )
        self.assertNotEqual(
            info,
            self._make_instance("SHA5", 5, "target", "xxxxxxx", "LOCATION"),
        )
        self.assertNotEqual(
            info,
            self._make_instance("SHA5", 5, "target", "profile", "XXXXXXXX"),
        )


class TestUpdateFile(cros_test_lib.TempDirTestCase):
    """Tests for the UpdateKeyInLocalFile function."""

    def setUp(self):
        self.contents_str = [
            "# comment that should be skipped",
            'PKGDIR="/var/lib/portage/pkgs"',
            'PORTAGE_BINHOST="http://no.thanks.com"',
            "portage portage-20100310.tar.bz2",
            'COMPILE_FLAGS="some_value=some_other"',
        ]
        self.version_file = os.path.join(self.tempdir, "version")
        osutils.WriteFile(self.version_file, "\n".join(self.contents_str))

    def _read_version_file(
        self, version_file: Optional[str] = None
    ) -> List[str]:
        """Read the contents of self.version_file and return as a list."""
        if not version_file:
            version_file = self.version_file

        with open(version_file, encoding="utf-8") as version_fh:
            return [line.strip() for line in version_fh.readlines()]

    def _verify_key_pair(self, key: str, val: str):
        file_contents = self._read_version_file()

        # Make sure 'key' entry is only found once.
        entry_found = False

        # Ensure value is wrapped on quotes.
        if '"' not in val:
            val = '"%s"' % val

        # Inspect file contents.
        for entry in file_contents:
            if "=" not in entry:
                continue
            file_key, file_val = entry.split("=", maxsplit=1)
            if file_key == key:
                if val == file_val:
                    if entry_found:
                        self.fail(f"Variable {file_key} appears twice")
                    else:
                        entry_found = True

        if not entry_found:
            self.fail('Could not find "%s=%s" in version file' % (key, val))

    def testAddVariableThatDoesNotExist(self):
        """Add in a new variable that was no present in the file."""
        key = "PORTAGE_BINHOST"
        value = "1234567"
        binpkg.UpdateKeyInLocalFile(self.version_file, value)
        print(self.version_file)
        self._read_version_file()
        self._verify_key_pair(key, value)
        print(self.version_file)

    def testUpdateVariable(self):
        """Test updating a variable that already exists."""
        binhost_key, binhost_val = self.contents_str[2].split("=")
        if binhost_key != "PORTAGE_BINHOST":
            self.fail(
                "unexpected test input: expected PORTAGE_BINHOST at line[2]"
            )
        self._verify_key_pair(binhost_key, binhost_val)

        # Confirm that unrelated variable 'PKGDIR' does not change.
        pkgdir_key, pkgdir_val = self.contents_str[1].split("=")
        if pkgdir_key != "PKGDIR":
            self.fail("unexpected test input: expected PKGDIR at line[1]")
        self._verify_key_pair(pkgdir_key, pkgdir_val)

        binhost_new_val = "test_update"
        binpkg.UpdateKeyInLocalFile(self.version_file, binhost_new_val)
        self._verify_key_pair(binhost_key, binhost_new_val)
        self._verify_key_pair(pkgdir_key, pkgdir_val)

        binhost_new_val = "test_update2"
        binpkg.UpdateKeyInLocalFile(self.version_file, binhost_new_val)
        self._verify_key_pair(binhost_key, binhost_new_val)
        self._verify_key_pair(pkgdir_key, pkgdir_val)

    def testUpdateNonExistentFile(self):
        """Test that we can write key/values in files that don't exist yet."""
        key = "PORTAGE_BINHOST"
        value = "1234567"
        non_existent_file = tempfile.mktemp()
        try:
            binpkg.UpdateKeyInLocalFile(non_existent_file, value)
            file_contents = self._read_version_file(non_existent_file)
            self.assertEqual(file_contents, ['%s="%s"' % (key, value)])
        finally:
            if os.path.exists(non_existent_file):
                os.remove(non_existent_file)
