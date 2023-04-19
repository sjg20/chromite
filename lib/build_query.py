# Copyright 2023 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Python API for `cros query`."""

from __future__ import annotations

import abc
import functools
import logging
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
    Type,
)

from chromite.lib import constants
from chromite.lib import portage_util
from chromite.lib.parser import package_info
from chromite.utils.parser import make_defaults
from chromite.utils.parser import portage_profile_conf


# We use docstrings in this file frequently for property documentation, which
# doesn't follow the traditional format of leaving the second line blank used
# with traditional functions/methods.
# pylint: disable=docstring-second-line-blank


class QueryTarget(abc.ABC):
    """Abstract base class for all query targets."""

    @classmethod
    @abc.abstractmethod
    def find_all(
        cls,
        board: Optional[str] = None,
        overlays: str = constants.BOTH_OVERLAYS,
    ) -> Iterator[QueryTarget]:
        """Find all instances of this target.

        Args:
            board: Limit results to only those relevant to a named
                board.
            overlays: Limit overlays to the specified type.

        Yields:
            Instances of this class.
        """

    def tree(self) -> Iterator[QueryTarget]:
        """Yield any relevant children for the tree-view from the CLI."""
        yield from ()


class Overlay(QueryTarget):
    """An overlay, e.g., src/third_party/chromiumos-overlay."""

    def __init__(self, path):
        self.path = Path(path)

    @classmethod
    def find_all(cls, board=None, overlays=constants.BOTH_OVERLAYS):
        for overlay_path in portage_util.FindOverlays(overlays, board=board):
            yield cls(overlay_path)

    def tree(self):
        yield from self.ebuilds
        yield from self.profiles

    @functools.cached_property
    def name(self) -> str:
        """The repo-name in metadata/layout.conf."""
        return portage_util.GetOverlayName(self.path)

    @property
    def is_private(self) -> bool:
        """True if the overlay appears to be private, false otherwise."""
        return self.name.endswith("-private")

    @property
    def board_name(self) -> str:
        """If this overlay is a top-level overlay for a board, the name of that
        board.  Otherwise, this is None.
        """
        if not self.path.name.startswith("overlay-"):
            return None
        if self.is_private:
            board_name, _, _ = self.name.rpartition("-")
            return board_name
        return self.name

    @property
    def profiles_dir(self) -> Path:
        """The profiles directory for this overlay."""
        return self.path / "profiles"

    @property
    def metadata_dir(self) -> Path:
        """The metadata directory for this overlay."""
        return self.path / "metadata"

    @property
    def md5_cache_dir(self) -> Path:
        """The md5-cache directory for this overlay."""
        return self.metadata_dir / "md5-cache"

    @functools.cached_property
    def profiles(self) -> List[Profile]:
        """A list of all profiles defined in this overlay."""
        if not self.profiles_dir.is_dir():
            return []

        def _scan_profiles(path):
            is_profile = False
            for ent in path.iterdir():
                if ent.is_dir():
                    yield from _scan_profiles(ent)
                elif ent.is_file():
                    if ent.name in (
                        "parent",
                        "eapi",
                        "deprecated",
                        "make.defaults",
                        "packages",
                        "packages.build",
                        "packages.mask",
                        "package.provided",
                        "package.use",
                        "use.mask",
                        "use.force",
                        "use.stable.mask",
                        "use.stable.force",
                        "package.use.mask",
                        "package.use.force",
                        "package.use.stable.mask",
                        "package.use",
                    ):
                        is_profile = True
            if is_profile:
                yield Profile(
                    str(path.relative_to(self.profiles_dir)), path, self
                )

        return list(_scan_profiles(self.profiles_dir))

    def get_profile(self, name: str) -> Optional[Profile]:
        """Get a specific profile by name.

        Args:
            name: The name of the profile (e.g., "base").

        Returns:
            The Profile object with this name, or None if this profile does not
            exist.
        """
        profile_dir = self.path / "profiles" / name
        if profile_dir.is_dir():
            return Profile(name, profile_dir, self)
        return None

    @functools.cached_property
    def ebuilds(self) -> List[Ebuild]:
        """A list of all ebuilds in this overlay."""
        for ebuild_path in self.path.glob("*/*/*.ebuild"):
            yield Ebuild(ebuild_file=ebuild_path, overlay=self)

    def __repr__(self):
        return str(self.path)

    def __eq__(self, other):
        return self.path == other.path


@functools.lru_cache(maxsize=None)
def _get_all_overlays_by_name() -> Dict[Overlay]:
    """Get all overlays, in a dictionary by name.

    Returns:
        A dictionary mapping overlay names to the Overlay objects.
    """
    overlays = {}
    for overlay in Overlay.find_all():
        overlays[overlay.name] = overlay
    return overlays


class Profile(QueryTarget):
    """A portage profile, e.g., chromiumos:base."""

    _obj_cache = {}

    def __new__(cls, _name: str, path: Path, _overlay: Overlay):
        # Caching the construction of profiles prevents a re-parse of
        # make.defaults when a profile is inherited multiple times,
        # which provides a significant speed-up during many queries.
        if path not in cls._obj_cache:
            cls._obj_cache[path] = super().__new__(cls)
        return cls._obj_cache[path]

    def __init__(self, name: str, path: Path, overlay: Overlay):
        self.name = name
        self.path = path
        self.overlay = overlay

    @classmethod
    def find_all(cls, board=None, overlays=constants.BOTH_OVERLAYS):
        for overlay in Overlay.find_all(board=board, overlays=overlays):
            yield from overlay.profiles

    @functools.cached_property
    def make_defaults_vars(self) -> Dict[str, str]:
        """A dictionary of the raw make.defaults variables."""
        make_defaults_path = self.path / "make.defaults"
        if make_defaults_path.is_file():
            contents = make_defaults_path.read_text(encoding="utf-8")
            return make_defaults.parse(contents)
        return {}

    def resolve_var(self, var: str, default: Optional[str] = None) -> Any:
        """Resolve a variable for this profile, similar to how Portage would.

        Note: this function resolves variables non-incrementally.  For
        incremental variables (e.g., USE, USE_EXPAND, etc), use
        resolve_var_incremental.

        Args:
            var: The variable to resolve.
            default: What to return if the variable is not set.

        Returns:
            The resolved variable.
        """
        if var in self.make_defaults_vars:
            return self.make_defaults_vars[var]
        for profile in reversed(self.parents):
            result = profile.resolve_var(var)
            if result is not None:
                return result
        return default

    def resolve_var_incremental(self, var: str) -> Set[str]:
        """Resolve a variable incrementally, similar to how Portage would.

        This will traverse the profiles depth-first, adding tokens which are not
        prefixed with a dash, and removing those which are.

        Args:
            var: The variable to resolve.

        Returns:
            The resolved variable, as a set of the tokens.
        """
        result = set()

        def _rec(profile):
            tokens = profile.make_defaults_vars.get(var, "").split()
            if "-*" not in tokens:
                for parent in profile.parents:
                    _rec(parent)
            for token in tokens:
                if not token:
                    # Variable was unset, empty, or just whitespace.
                    continue
                if token == "-*":
                    result.clear()
                elif token.startswith("-"):
                    result.discard(token[1:])
                else:
                    result.add(token)

        _rec(self)
        return result

    @property
    def arch(self) -> str:
        """The machine architecture of this profile."""
        return self.resolve_var("ARCH")

    def _use_flag_changes(self) -> Tuple[Set[str], Set[str]]:
        """Compute the USE flags changed by this profile.

        Returns:
            A 2-tuple: the set of flags set, and the flags unset.
        """
        flags_set = set()
        flags_unset = set()

        def _process_flag(flag, prefix=""):
            flag_set = True
            if not flag:
                return
            if flag.startswith("-"):
                flag = flag[1:]
                flag_set = False
            flag = prefix + flag
            if flag_set:
                flags_unset.discard(flag)
                flags_set.add(flag)
            else:
                flags_unset.add(flag)
                flags_set.discard(flag)

        for flag in self.make_defaults_vars.get("USE", "").split():
            _process_flag(flag)

        use_expand = self.resolve_var_incremental("USE_EXPAND")
        for var in use_expand:
            for val in self.make_defaults_vars.get(var.upper(), "").split():
                _process_flag(val, prefix=f"{var.lower()}_")

        if "ARCH" in self.make_defaults_vars:
            flags_set.add(self.make_defaults_vars["ARCH"])

        return flags_set, flags_unset

    @property
    def use_flags_set(self) -> Set[str]:
        """A set of what USE flags this profile enables."""
        flags_set, _ = self._use_flag_changes()
        return flags_set

    @property
    def use_flags_unset(self) -> Set[str]:
        """A set of what USE flags this profile disables."""
        _, flags_unset = self._use_flag_changes()
        return flags_unset

    @property
    def use_flags(self) -> Set[str]:
        """A set of the fully-resolved USE flags for this profile."""
        use_flags = set(self.resolve_var_incremental("USE"))
        use_expand = self.resolve_var_incremental("USE_EXPAND")
        for var in use_expand:
            expansions = self.resolve_var_incremental(var.upper())
            for val in expansions:
                use_flags.add(f"{var.lower()}_{val}")

        # The architecture becomes a USE flag.
        use_flags.add(self.arch)

        return use_flags

    @functools.cached_property
    def parents(self) -> List[Profile]:
        """A list of the immediate parent profiles of this profile."""
        parent_file = self.path / "parent"
        if not parent_file.is_file():
            return []

        parents = []
        parent_file_contents = parent_file.read_text(encoding="utf-8")
        for tokens in portage_profile_conf.parse(parent_file_contents):
            if len(tokens) != 1:
                logging.warning(
                    "Profile %r has invalid parent configuration: %r",
                    self,
                    tokens,
                )
                continue
            if ":" in tokens[0]:
                repo_name, _, profile_name = tokens[0].partition(":")
                overlays = _get_all_overlays_by_name()
                overlay = overlays.get(repo_name)
                if not overlay:
                    logging.warning(
                        "Profile %r has parent %r, but %r isn't an overlay.",
                        self,
                        tokens[0],
                        repo_name,
                    )
                    continue
                profile = overlay.get_profile(profile_name)
            else:
                path = (self.path / Path(tokens[0])).resolve()
                path = path.relative_to(self.overlay.profiles_dir)
                profile = self.overlay.get_profile(path)
            if not profile:
                continue
            parents.append(profile)
        return parents

    def tree(self):
        yield from self.parents

    def __repr__(self):
        return f"{self.overlay.name}:{self.name}"


class Ebuild(QueryTarget):
    """An ebuild, fully qualified by ebuild file.

    Note: This implementation relies on the md5-cache files, which are updated
    by a builder every 30 minutes.  Thus, if you've made changes locally, they
    may not be reflected in the query immediately.  Run egencache in the overlay
    to regenerate these cache files manually, should you require it.
    """

    def __init__(self, ebuild_file: Path, overlay: Overlay):
        self.ebuild_file = ebuild_file
        self.overlay = overlay

    @classmethod
    def find_all(cls, board=None, overlays=constants.BOTH_OVERLAYS):
        for overlay in Overlay.find_all(board=board, overlays=overlays):
            yield from overlay.ebuilds

    @functools.cached_property
    def package_info(self) -> package_info.PackageInfo:
        """The PackageInfo for this ebuild."""
        return package_info.parse(self.ebuild_file)

    @property
    def md5_cache_file(self) -> Path:
        """The path to the md5-cache file for this ebuild."""
        return self.overlay.md5_cache_dir / self.package_info.cpvr

    @functools.cached_property
    def vars(self) -> Dict[str, str]:
        """The raw variables from the md5-cache file."""
        if not self.md5_cache_file.is_file():
            return {}

        result = {}
        with open(self.md5_cache_file, encoding="utf-8") as f:
            for line in f:
                key, _, value = line.partition("=")
                result[key] = value.rstrip("\n")
        return result

    @property
    def eapi(self) -> int:
        """The EAPI for the package."""
        return int(self.vars.get("EAPI", 0))

    @property
    def iuse(self) -> Set[str]:
        """A set of the flags in IUSE."""
        iuse = self.vars.get("IUSE")
        if not iuse:
            return set()
        result = set()
        for var in iuse.split(" "):
            if var.startswith("-"):
                continue
            if var.startswith("+"):
                var = var[1:]
            result.add(var)
        return result

    @property
    def iuse_default(self) -> Set[str]:
        """A set of the flags enabled by default in IUSE."""
        iuse = self.vars.get("IUSE", "")
        result = set()
        for var in iuse.split(" "):
            if var.startswith("+"):
                var = var[1:]
                result.add(var)
        return result

    @property
    def eclasses(self) -> List[str]:
        """A list of the eclasses inherited by this package and its eclasses."""
        eclasses = self.vars.get("_eclasses_")
        if not eclasses:
            return []
        return eclasses.split("\t")[::2]

    @property
    def keywords(self) -> List[str]:
        """The KEYWORDS of this package."""
        keywords = self.vars.get("KEYWORDS")
        if not keywords:
            return []
        return keywords.split()

    def __repr__(self):
        return f"{self.package_info.cpvr}::{self.overlay.name}"

    def __eq__(self, other):
        return self.ebuild_file == other.ebuild_file


class Board(QueryTarget):
    """A board, as in what would be passed to setup_board."""

    def __init__(
        self,
        name: str,
        private_overlay: Optional[Overlay] = None,
        public_overlay: Optional[Overlay] = None,
    ):
        self.name = name
        self.private_overlay = private_overlay
        self.public_overlay = public_overlay

    @classmethod
    def find_all(cls, board=None, overlays=constants.BOTH_OVERLAYS):
        boards = {}

        for overlay in Overlay.find_all(board=board, overlays=overlays):
            board_name = overlay.board_name
            if not board_name:
                continue
            if board_name not in boards:
                boards[board_name] = Board(board_name)
            if overlay.is_private:
                boards[board_name].private_overlay = overlay
            else:
                boards[board_name].public_overlay = overlay

        yield from boards.values()

    @property
    def top_level_overlay(self) -> Optional[Overlay]:
        """The top-level overlay for this board."""
        return self.private_overlay or self.public_overlay

    @property
    def top_level_profile(self) -> Optional[Profile]:
        """The top-level profile for this board."""
        if self.top_level_overlay:
            return self.top_level_overlay.get_profile("base")
        return None

    def tree(self):
        if self.top_level_profile:
            yield self.top_level_profile

    @property
    def use_flags(self) -> Set[str]:
        """The fully-evaluated USE flags for this board."""
        result = {f"board_use_{self.name}"}
        if self.top_level_profile:
            result.update(self.top_level_profile.use_flags)
        return result

    @property
    def arch(self) -> str:
        """The machine architecture of this board."""
        return self.top_level_profile.arch

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name


class Query:
    """The Python-level interface for cros query.

    For example:

        board = Query(Board).filter(lambda board: board.name == "volteer").one()
    """

    def __init__(
        self,
        target: Type[QueryTarget],
        board: Optional[str] = None,
        overlays: str = constants.BOTH_OVERLAYS,
    ):
        self._filters = []
        self._iter = target.find_all(board=board, overlays=overlays)
        self._consumed = False

    def filter(self, func: Callable[[QueryTarget], bool]) -> Query:
        """Add a filter to the results."""
        if self._consumed:
            raise RuntimeError("Filters cannot be added after consumption.")
        self._filters.append(func)
        return self

    def __iter__(self) -> Iterator[QueryTarget]:
        """Iterate through all results."""
        if self._consumed:
            raise RuntimeError("Query iterator has already been consumed.")
        self._consumed = True
        for result in self._iter:
            if all(x(result) for x in self._filters):
                yield result

    def one(self) -> QueryTarget:
        """Assert there is exactly one result and return it."""
        iterator = iter(self)
        result = next(iterator)
        try:
            next(iterator)
        except StopIteration:
            return result
        raise ValueError("Query returned multiple results.")

    def one_or_none(self) -> Optional[QueryTarget]:
        """Return the result if there's exactly one, or None if zero."""
        try:
            return self.one()
        except StopIteration:
            return None

    def all(self) -> List[QueryTarget]:
        """Return all results in a list."""
        return list(self)
