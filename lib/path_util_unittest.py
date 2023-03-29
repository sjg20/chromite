# Copyright 2015 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test the path_util module."""

import itertools
import os
from pathlib import Path
import tempfile
from unittest import mock

from chromite.api.gen.chromiumos import common_pb2
from chromite.lib import constants
from chromite.lib import cros_test_lib
from chromite.lib import git
from chromite.lib import osutils
from chromite.lib import partial_mock
from chromite.lib import path_util


FAKE_SOURCE_PATH = "/path/to/source/tree"
FAKE_OUT_PATH = FAKE_SOURCE_PATH / constants.DEFAULT_OUT_DIR
FAKE_REPO_PATH = "/path/to/repo"
CUSTOM_SOURCE_PATH = "/custom/source/path"
CUSTOM_CHROOT_PATH = "/custom/chroot/path"
CUSTOM_OUT_PATH = Path("/custom/out/path")


class DetermineCheckoutTest(cros_test_lib.MockTempDirTestCase):
    """Verify functionality for figuring out what checkout we're in."""

    def setUp(self):
        self.rc_mock = cros_test_lib.RunCommandMock()
        self.StartPatcher(self.rc_mock)
        self.rc_mock.SetDefaultCmdResult()

    def RunTest(
        self, dir_struct, cwd, expected_root, expected_type, expected_src
    ):
        """Run a test with specific parameters and expected results."""
        cros_test_lib.CreateOnDiskHierarchy(self.tempdir, dir_struct)
        cwd = os.path.join(self.tempdir, cwd)
        checkout_info = path_util.DetermineCheckout(cwd)
        full_root = expected_root
        if expected_root is not None:
            full_root = os.path.join(self.tempdir, expected_root)
        full_src = expected_src
        if expected_src is not None:
            full_src = os.path.join(self.tempdir, expected_src)

        self.assertEqual(checkout_info.root, full_root)
        self.assertEqual(checkout_info.type, expected_type)
        self.assertEqual(checkout_info.chrome_src_dir, full_src)

    def testGclientRepo(self):
        """Recognizes a GClient repo checkout."""
        dir_struct = [
            "a/.gclient",
            "a/b/.repo/",
            "a/b/c/.gclient",
            "a/b/c/d/somefile",
        ]
        self.RunTest(
            dir_struct,
            "a/b/c",
            "a/b/c",
            path_util.CHECKOUT_TYPE_GCLIENT,
            "a/b/c/src",
        )
        self.RunTest(
            dir_struct,
            "a/b/c/d",
            "a/b/c",
            path_util.CHECKOUT_TYPE_GCLIENT,
            "a/b/c/src",
        )
        self.RunTest(
            dir_struct, "a/b", "a/b", path_util.CHECKOUT_TYPE_REPO, None
        )
        self.RunTest(
            dir_struct, "a", "a", path_util.CHECKOUT_TYPE_GCLIENT, "a/src"
        )

    def testGitUnderGclient(self):
        """Recognizes a chrome git checkout by gclient."""
        self.rc_mock.AddCmdResult(
            partial_mock.In("config"), stdout=constants.CHROMIUM_GOB_URL
        )
        dir_struct = [
            "a/.gclient",
            "a/src/.git/",
        ]
        self.RunTest(
            dir_struct, "a/src", "a", path_util.CHECKOUT_TYPE_GCLIENT, "a/src"
        )

    def testGitUnderRepo(self):
        """Recognizes a chrome git checkout by repo."""
        self.rc_mock.AddCmdResult(
            partial_mock.In("config"), stdout=constants.CHROMIUM_GOB_URL
        )
        dir_struct = [
            "a/.repo/",
            "a/b/.git/",
        ]
        self.RunTest(dir_struct, "a/b", "a", path_util.CHECKOUT_TYPE_REPO, None)

    def testBadGit1(self):
        """.git is not a directory."""
        self.RunTest(
            ["a/.git"], "a", None, path_util.CHECKOUT_TYPE_UNKNOWN, None
        )

    def testBadGit2(self):
        """'git config' returns nothing."""
        self.RunTest(
            ["a/.repo/", "a/b/.git/"],
            "a/b",
            "a",
            path_util.CHECKOUT_TYPE_REPO,
            None,
        )

    def testBadGit3(self):
        """'git config' returns error."""
        self.rc_mock.AddCmdResult(partial_mock.In("config"), returncode=5)
        self.RunTest(
            ["a/.git/"], "a", None, path_util.CHECKOUT_TYPE_UNKNOWN, None
        )


class FindCacheDirTest(cros_test_lib.MockTempDirTestCase):
    """Test cache dir specification and finding functionality."""

    def setUp(self):
        dir_struct = [
            "repo/.repo/",
            "repo/manifest/",
            "gclient/.gclient",
        ]
        cros_test_lib.CreateOnDiskHierarchy(self.tempdir, dir_struct)
        self.repo_root = os.path.join(self.tempdir, "repo")
        self.gclient_root = os.path.join(self.tempdir, "gclient")
        self.nocheckout_root = os.path.join(self.tempdir, "nothing")

        self.rc_mock = self.StartPatcher(cros_test_lib.RunCommandMock())
        self.cwd_mock = self.PatchObject(os, "getcwd")

    def testRepoRoot(self):
        """Test when we are inside a repo checkout."""
        self.cwd_mock.return_value = self.repo_root
        self.assertEqual(
            path_util.FindCacheDir(),
            os.path.join(self.repo_root, path_util.GENERAL_CACHE_DIR),
        )

    def testGclientRoot(self):
        """Test when we are inside a gclient checkout."""
        self.cwd_mock.return_value = self.gclient_root
        self.assertEqual(
            path_util.FindCacheDir(),
            os.path.join(
                self.gclient_root, "src", "build", path_util.CHROME_CACHE_DIR
            ),
        )

    def testTempdir(self):
        """Test when we are not in any checkout."""
        self.cwd_mock.return_value = self.nocheckout_root
        self.assertStartsWith(
            path_util.FindCacheDir(), os.path.join(tempfile.gettempdir(), "")
        )


class TestPathResolver(cros_test_lib.MockTestCase):
    """Tests of ChrootPathResolver class."""

    def setUp(self):
        self.PatchObject(constants, "SOURCE_ROOT", new=FAKE_SOURCE_PATH)
        self.PatchObject(constants, "DEFAULT_OUT_PATH", new=FAKE_OUT_PATH)
        self.PatchObject(
            path_util, "GetCacheDir", return_value="/path/to/cache"
        )
        self.PatchObject(
            path_util.ChrootPathResolver,
            "_GetCachePath",
            return_value="/path/to/cache",
        )
        self.PatchObject(
            git,
            "FindRepoDir",
            return_value=os.path.join(FAKE_REPO_PATH, ".fake_repo"),
        )
        self.chroot_path = None
        self.out_path = None

    def FakeCwd(self, base_path):
        return os.path.join(base_path, "somewhere/in/there")

    def SetChrootPath(self, source_path, chroot_path=None, out_path=None):
        """Set and fake the chroot path."""
        self.chroot_path = chroot_path or os.path.join(
            source_path, constants.DEFAULT_CHROOT_DIR
        )
        self.out_path = out_path or (source_path / constants.DEFAULT_OUT_DIR)

    @mock.patch(
        "chromite.lib.cros_build_lib.IsInsideChroot", return_value=False
    )
    def testSourcePathInChrootInbound(self, _):
        """Test regular behavior if chroot_path is inside source_path."""

        self.SetChrootPath(constants.SOURCE_ROOT)
        resolver = path_util.ChrootPathResolver(
            source_from_path_repo=False,
            chroot_path=self.chroot_path,
            out_path=self.out_path,
        )

        self.assertEqual(
            os.path.join(self.chroot_path, "some/file"),
            resolver.FromChroot(os.path.join("/some/file")),
        )

        self.assertEqual(
            os.path.join("/other/file"),
            resolver.ToChroot(os.path.join(self.chroot_path, "other/file")),
        )

    @mock.patch("chromite.lib.cros_build_lib.IsInsideChroot", return_value=True)
    def testInsideChroot(self, _):
        """Tests {To,From}Chroot() call from inside the chroot."""
        self.SetChrootPath(constants.SOURCE_ROOT)
        resolver = path_util.ChrootPathResolver()

        self.assertEqual(
            os.path.realpath("some/path"), resolver.ToChroot("some/path")
        )
        self.assertEqual(
            os.path.realpath("/some/path"), resolver.ToChroot("/some/path")
        )
        self.assertEqual(
            os.path.realpath("some/path"), resolver.FromChroot("some/path")
        )
        self.assertEqual(
            os.path.realpath("/some/path"), resolver.FromChroot("/some/path")
        )

    @mock.patch(
        "chromite.lib.cros_build_lib.IsInsideChroot", return_value=False
    )
    def testOutsideChrootInbound(self, _):
        """Tests ToChroot() calls from outside the chroot."""
        for source_path, source_from_path_repo in itertools.product(
            (None, CUSTOM_SOURCE_PATH), (False, True)
        ):
            if source_from_path_repo:
                actual_source_path = FAKE_REPO_PATH
            else:
                actual_source_path = source_path or constants.SOURCE_ROOT

            fake_cwd = self.FakeCwd(actual_source_path)
            self.PatchObject(os, "getcwd", return_value=fake_cwd)
            self.SetChrootPath(actual_source_path)
            resolver = path_util.ChrootPathResolver(
                source_path=source_path,
                source_from_path_repo=source_from_path_repo,
            )
            self.PatchObject(resolver, "_ReadChrootLink", return_value=None)
            source_rel_cwd = os.path.relpath(fake_cwd, actual_source_path)

            # Case: path inside the chroot space.
            self.assertEqual(
                "/some/path",
                resolver.ToChroot(os.path.join(self.chroot_path, "some/path")),
            )

            # Case: the cache directory.
            self.assertEqual(
                constants.CHROOT_CACHE_ROOT,
                resolver.ToChroot(path_util.GetCacheDir()),
            )

            # Case: path inside the cache directory.
            self.assertEqual(
                os.path.join(constants.CHROOT_CACHE_ROOT, "some/path"),
                resolver.ToChroot(
                    os.path.join(path_util.GetCacheDir(), "some/path")
                ),
            )

            # Case: absolute path inside the source tree.
            if source_from_path_repo:
                self.assertEqual(
                    os.path.join(constants.CHROOT_SOURCE_ROOT, "some/path"),
                    resolver.ToChroot(
                        os.path.join(FAKE_REPO_PATH, "some/path")
                    ),
                )
            else:
                self.assertEqual(
                    os.path.join(constants.CHROOT_SOURCE_ROOT, "some/path"),
                    resolver.ToChroot(
                        os.path.join(actual_source_path, "some/path")
                    ),
                )

            # Case: relative path inside the source tree.
            if source_from_path_repo:
                self.assertEqual(
                    os.path.join(
                        constants.CHROOT_SOURCE_ROOT,
                        source_rel_cwd,
                        "some/path",
                    ),
                    resolver.ToChroot("some/path"),
                )
            else:
                self.assertEqual(
                    os.path.join(
                        constants.CHROOT_SOURCE_ROOT,
                        source_rel_cwd,
                        "some/path",
                    ),
                    resolver.ToChroot("some/path"),
                )

            # Case: unreachable, path with improper source root prefix.
            with self.assertRaises(ValueError):
                resolver.ToChroot(
                    os.path.join(actual_source_path + "-foo", "some/path")
                )

            # Case: unreachable (random).
            with self.assertRaises(ValueError):
                resolver.ToChroot("/some/path")

    @mock.patch(
        "chromite.lib.cros_build_lib.IsInsideChroot", return_value=False
    )
    def testOutsideCustomChrootInbound(self, _):
        """Tests ToChroot() calls from outside a custom chroot."""

        self.SetChrootPath(
            constants.SOURCE_ROOT, CUSTOM_CHROOT_PATH, out_path=CUSTOM_OUT_PATH
        )
        resolver = path_util.ChrootPathResolver(
            chroot_path=CUSTOM_CHROOT_PATH, out_path=CUSTOM_OUT_PATH
        )

        # Case: path inside the chroot space.
        self.assertEqual(
            "/some/path",
            resolver.ToChroot(os.path.join(self.chroot_path, "some/path")),
        )

        # Case: path from source root
        self.assertEqual(
            os.path.join(constants.CHROOT_SOURCE_ROOT, "some/path"),
            resolver.ToChroot(os.path.join(constants.SOURCE_ROOT, "some/path")),
        )

        # Case: not mapped to chroot
        with self.assertRaises(ValueError):
            resolver.ToChroot("/random/file")

    @mock.patch(
        "chromite.lib.cros_build_lib.IsInsideChroot", return_value=False
    )
    def testOutsideChrootOutbound(self, _):
        """Tests FromChroot() calls from outside the chroot."""
        self.PatchObject(
            os, "getcwd", return_value=self.FakeCwd(FAKE_SOURCE_PATH)
        )

        self.SetChrootPath(constants.SOURCE_ROOT)
        resolver = path_util.ChrootPathResolver()
        # These two patches are only necessary or have any affect on the test when
        # the test is run inside of a symlinked chroot. The _ReadChrootLink patch
        # ensures it runs as if it is not in a symlinked chroot. The realpath
        # patch is necessary to make it actually behave as if that's the case.
        # In both instances the effective return value are as if it was not in a
        # symlinked chroot.
        # TODO(saklein) Rewrite these tests so this isn't necessary.
        self.PatchObject(resolver, "_ReadChrootLink", return_value=None)
        self.PatchObject(os.path, "realpath", side_effect=lambda x: x)

        # Case: source root path.
        self.assertEqual(
            os.path.join(constants.SOURCE_ROOT, "some/path"),
            resolver.FromChroot(
                os.path.join(constants.CHROOT_SOURCE_ROOT, "some/path")
            ),
        )

        # Case: cyclic source/chroot sub-path elimination.
        self.assertEqual(
            os.path.join(constants.SOURCE_ROOT, "some/path"),
            resolver.FromChroot(
                os.path.join(
                    constants.CHROOT_SOURCE_ROOT,
                    constants.DEFAULT_CHROOT_DIR,
                    constants.CHROOT_SOURCE_ROOT.lstrip(os.path.sep),
                    constants.DEFAULT_CHROOT_DIR,
                    constants.CHROOT_SOURCE_ROOT.lstrip(os.path.sep),
                    "some/path",
                )
            ),
        )

        # Case: the cache directory.
        self.assertEqual(
            path_util.GetCacheDir(),
            resolver.FromChroot(constants.CHROOT_CACHE_ROOT),
        )

        # Case: path inside the cache directory.
        self.assertEqual(
            os.path.join(path_util.GetCacheDir(), "some/path"),
            resolver.FromChroot(
                os.path.join(constants.CHROOT_CACHE_ROOT, "some/path")
            ),
        )

        # Case: non-rooted chroot paths.
        self.assertEqual(
            os.path.join(self.chroot_path, "some/path"),
            resolver.FromChroot("/some/path"),
        )

    @mock.patch(
        "chromite.lib.cros_build_lib.IsInsideChroot", return_value=False
    )
    def testOutsideCustomChrootOutbound(self, _):
        """Tests FromChroot() calls from outside the chroot."""
        self.PatchObject(
            os, "getcwd", return_value=self.FakeCwd(FAKE_SOURCE_PATH)
        )

        self.SetChrootPath(
            constants.SOURCE_ROOT,
            chroot_path=CUSTOM_CHROOT_PATH,
            out_path=CUSTOM_OUT_PATH,
        )
        resolver = path_util.ChrootPathResolver(
            chroot_path=CUSTOM_CHROOT_PATH, out_path=CUSTOM_OUT_PATH
        )
        # These two patches are only necessary or have any affect on the test when
        # the test is run inside of a symlinked chroot. The _ReadChrootLink patch
        # ensures it runs as if it is not in a symlinked chroot. The realpath
        # patch is necessary to make it actually behave as if that's the case.
        # In both instances the effective return value are as if it was not in a
        # symlinked chroot.
        # TODO(saklein) Rewrite these tests so this isn't necessary.
        self.PatchObject(resolver, "_ReadChrootLink", return_value=None)
        self.PatchObject(os.path, "realpath", side_effect=lambda x: x)

        # Case: source root path.
        self.assertEqual(
            os.path.join(constants.SOURCE_ROOT, "some/path"),
            resolver.FromChroot(
                os.path.join(constants.CHROOT_SOURCE_ROOT, "some/path")
            ),
        )

        # Case: cyclic source/chroot sub-path
        self.assertEqual(
            os.path.join(
                constants.SOURCE_ROOT,
                constants.DEFAULT_CHROOT_DIR,
                constants.CHROOT_SOURCE_ROOT.lstrip(os.path.sep),
                constants.DEFAULT_CHROOT_DIR,
                constants.CHROOT_SOURCE_ROOT.lstrip(os.path.sep),
                "some/path",
            ),
            resolver.FromChroot(
                os.path.join(
                    constants.CHROOT_SOURCE_ROOT,
                    constants.DEFAULT_CHROOT_DIR,
                    constants.CHROOT_SOURCE_ROOT.lstrip(os.path.sep),
                    constants.DEFAULT_CHROOT_DIR,
                    constants.CHROOT_SOURCE_ROOT.lstrip(os.path.sep),
                    "some/path",
                )
            ),
        )

        # Case: path inside the cache directory.
        self.assertEqual(
            os.path.join(path_util.GetCacheDir(), "some/path"),
            resolver.FromChroot(
                os.path.join(constants.CHROOT_CACHE_ROOT, "some/path")
            ),
        )

        # Case: non-rooted chroot paths.
        self.assertEqual(
            os.path.join(self.chroot_path, "some/path"),
            resolver.FromChroot("/some/path"),
        )

    @mock.patch(
        "chromite.lib.cros_build_lib.IsInsideChroot", return_value=False
    )
    def testSymlinkedChroot(self, _):
        self.SetChrootPath(constants.SOURCE_ROOT)
        resolver = path_util.ChrootPathResolver()
        self.PatchObject(
            resolver, "_ReadChrootLink", return_value="/another/path"
        )

        # Should still resolve paths from the chroot to the default location.
        self.assertEqual(
            os.path.join(
                constants.SOURCE_ROOT, constants.DEFAULT_CHROOT_DIR, "some/path"
            ),
            resolver.FromChroot("/some/path"),
        )

        # Should be able to handle translating the linked location to a chroot path.
        self.assertEqual(
            "/some/path", resolver.ToChroot("/another/path/some/path")
        )


def test_normalize_paths_to_source_root_collapsing_sub_paths():
    """Test normalize removes sub paths."""
    actual_paths = path_util.normalize_paths_to_source_root(
        [
            os.path.join(constants.SOURCE_ROOT, "foo"),
            os.path.join(constants.SOURCE_ROOT, "ab", "cd"),
            os.path.join(constants.SOURCE_ROOT, "foo", "bar"),
        ]
    )
    expected_paths = {"ab/cd", "foo"}
    assert set(actual_paths) == expected_paths

    actual_paths = path_util.normalize_paths_to_source_root(
        [
            os.path.join(constants.SOURCE_ROOT, "foo", "bar"),
            os.path.join(constants.SOURCE_ROOT, "ab", "cd"),
            os.path.join(constants.SOURCE_ROOT, "foo", "bar", ".."),
            os.path.join(constants.SOURCE_ROOT, "ab", "cde"),
        ]
    )
    expected_paths = {"ab/cd", "ab/cde", "foo"}
    assert set(actual_paths) == expected_paths


def test_normalize_paths_to_source_root_formatting_directory_paths(tmp_path):
    """Test normalize correctly handles /path/to/file and /path/to/dir/."""
    foo_dir = tmp_path / "foo"
    foo_dir.mkdir()
    bar_baz_dir = tmp_path / "bar" / "baz"
    bar_baz_dir.mkdir(parents=True)
    ab_dir = tmp_path / "ab"
    ab_dir.mkdir()
    ab_cd_file = ab_dir / "cd"

    osutils.WriteFile(ab_cd_file, "alphabet")

    expected_paths = [
        str(ab_cd_file.relative_to(tmp_path)),
        str(bar_baz_dir.relative_to(tmp_path)),
        str(foo_dir.relative_to(tmp_path)),
    ]

    actual_paths = path_util.normalize_paths_to_source_root(
        [
            str(foo_dir) + "/",
            str(ab_cd_file),
            str(bar_baz_dir) + "/",
        ],
        source_root=str(tmp_path),
    )
    assert actual_paths == expected_paths


def test_expand_directories_in_git(tmp_path):
    """Test ExpandDirectories when given a dir in a git repo."""
    files_in_dir = [Path("foo.txt"), Path("bar.txt")]

    with mock.patch("chromite.lib.git.FindGitTopLevel", return_value=tmp_path):
        with mock.patch(
            "chromite.lib.git.LsFiles", return_value=files_in_dir
        ) as ls_files:
            result = set(path_util.ExpandDirectories([tmp_path]))

    assert result == set(files_in_dir)
    ls_files.assert_called_once_with(files=[tmp_path], untracked=True)


def test_expand_directories_not_git(tmp_path):
    """Test ExpandDirectories when given a dir outside a git repo."""
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    files_in_dir = [tmp_path / "foo.txt", subdir / "bar.txt"]
    for f in files_in_dir:
        osutils.Touch(f)

    with mock.patch("chromite.lib.git.FindGitTopLevel", return_value=None):
        result = set(path_util.ExpandDirectories([tmp_path]))

    assert result == set(files_in_dir)


def test_expand_directories_file(tmp_path):
    """Test ExpandDirectories when given a regular file."""
    file_path = tmp_path / "foo.txt"
    osutils.Touch(file_path)

    result = list(path_util.ExpandDirectories([file_path]))

    assert result == [file_path]


class ProtoPathToPathlibPathTest(cros_test_lib.TestCase):
    """Verify functionality for ProtoPathToPathlibPath."""

    chroot = common_pb2.Chroot(path="/path/to/chroot")

    @staticmethod
    def createProtoPath(path: str, inside: bool) -> common_pb2.Path:
        """Helper function to create a common_pb2.Path."""
        location = (
            common_pb2.Path.Location.INSIDE
            if inside
            else common_pb2.Path.Location.OUTSIDE
        )
        return common_pb2.Path(path=path, location=location)

    def testRelativeInside(self):
        """Verify that passing in a relative path inside the chroot fails"""
        proto_path = self.createProtoPath(path="usr/bin", inside=True)
        with self.assertRaises(ValueError):
            path_util.ProtoPathToPathlibPath(proto_path, chroot=self.chroot)

    def testRelativeOutside(self):
        """Verify that passing in a relative path outside the chroot fails"""
        proto_path = self.createProtoPath(path="usr/bin", inside=False)
        with self.assertRaises(ValueError):
            path_util.ProtoPathToPathlibPath(proto_path, chroot=self.chroot)

    def testInsideWithChroot(self):
        """Verify that we can convert an inside path with a chroot."""
        proto_path = self.createProtoPath(path="/usr/bin", inside=True)
        pathlib_path = path_util.ProtoPathToPathlibPath(
            proto_path, chroot=self.chroot
        )
        self.assertEqual(pathlib_path, Path("/path/to/chroot/usr/bin"))

    def testOutsideWithChroot(self):
        """Verify that we can convert an outside path with a chroot."""
        proto_path = self.createProtoPath(path="/usr/bin", inside=False)
        pathlib_path = path_util.ProtoPathToPathlibPath(
            proto_path, chroot=self.chroot
        )
        self.assertEqual(pathlib_path, Path("/usr/bin"))

    def testInsideWithoutChroot(self):
        """Verify that we cannot convert an inside path without a chroot."""
        proto_path = self.createProtoPath(path="/usr/bin", inside=True)
        with self.assertRaises(ValueError):
            path_util.ProtoPathToPathlibPath(proto_path)

    def testOutsideWithoutChroot(self):
        """Verify that we can convert an outside path without a chroot."""
        proto_path = self.createProtoPath(path="/usr/bin", inside=False)
        pathlib_path = path_util.ProtoPathToPathlibPath(proto_path)
        self.assertEqual(pathlib_path, Path("/usr/bin"))
