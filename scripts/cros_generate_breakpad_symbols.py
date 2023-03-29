# Copyright 2013 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Generate minidump symbols for use by the Crash server.

Note: This should be run inside the chroot.

This produces files in the breakpad format required by minidump_stackwalk and
the crash server to dump stack information.

Basically it scans all the split .debug files in /build/$BOARD/usr/lib/debug/
and converts them over using the `dump_syms` programs.  Those plain text .sym
files are then stored in /build/$BOARD/usr/lib/debug/breakpad/.

If you want to actually upload things, see upload_symbols.py.
"""

import collections
import ctypes
import enum
import logging
import multiprocessing
import multiprocessing.sharedctypes
import os
import re
from typing import Optional

from chromite.cbuildbot import cbuildbot_alerts
from chromite.lib import build_target_lib
from chromite.lib import commandline
from chromite.lib import cros_build_lib
from chromite.lib import osutils
from chromite.lib import parallel
from chromite.lib import signals
from chromite.utils import file_util


# Elf files that don't exist but have a split .debug file installed.
ALLOWED_DEBUG_ONLY_FILES = {
    "boot/vmlinux",
}

# Allowlist of elf files that we know we can't symbolize in the normal way, but
# which we don't have an automatic way to detect.
EXPECTED_POOR_SYMBOLIZATION_FILES = ALLOWED_DEBUG_ONLY_FILES | {
    # Git binaries are downloaded as binary blobs already stripped.
    "usr/bin/git",
    "usr/bin/git-receive-pack",
    "usr/bin/git-upload-archive",
    "usr/bin/git-upload-pack",
    # Prebuild Android binary
    "build/rootfs/opt/google/vms/android/etc/bin/XkbToKcmConverter",
    # Pulled from
    # https://skia.googlesource.com/buildbot/+/refs/heads/main/gold-client/, no
    # need to resymbolize.
    "usr/bin/goldctl",
    # TODO(b/273620044): The following 44 binaries are from
    # app-benchmarks/lmbench; they hardcode some compiler options which prevent
    # us from generating STACK records. Fix the package.
    "usr/bin/lat_unix",
    "usr/bin/lat_select",
    "usr/bin/line.lmbench",
    "usr/bin/lat_rpc",
    "usr/bin/hello",
    "usr/bin/lmhttp",
    "usr/bin/lat_syscall",
    "usr/bin/par_mem",
    "usr/bin/lat_http",
    "usr/bin/lat_proc",
    "usr/bin/stream.lmbench",
    "usr/bin/enough",
    "usr/bin/lat_mem_rd",
    "usr/bin/mhz",
    "usr/bin/lat_fs",
    "usr/bin/lat_sem",
    "usr/bin/lmdd",
    "usr/bin/lat_fcntl",
    "usr/bin/lat_pipe",
    "usr/bin/lat_mmap",
    "usr/bin/bw_file_rd",
    "usr/bin/bw_unix",
    "usr/bin/lat_tcp",
    "usr/bin/flushdisk",
    "usr/bin/bw_pipe",
    "usr/bin/msleep",
    "usr/bin/bw_mmap_rd",
    "usr/bin/bw_tcp",
    "usr/bin/lat_ops",
    "usr/bin/loop_o",
    "usr/bin/bw_mem",
    "usr/bin/lat_pagefault",
    "usr/bin/lat_connect",
    "usr/bin/timing_o",
    "usr/bin/lat_ctx",
    "usr/bin/tlb",
    "usr/bin/lat_fifo",
    "usr/bin/disk",
    "usr/bin/lat_unix_connect",
    "usr/bin/par_ops",
    "usr/bin/lat_sig",
    "usr/bin/lat_udp",
    "usr/bin/lat_ops",
    "usr/bin/memsize",
    # This is complete for --board=eve and --board=kevin
    # TODO(b/241470012): Complete for other boards.
}

# Allowlist of patterns for ELF files that symbolize (dump_syms exits with
# success) but don't pass symbol file validation. Note that ELFs listed in
# EXPECTED_POOR_SYMBOLIZATION_FILES do not have their symbol files validated and
# do not need to be repeated here.
ALLOWLIST_NO_SYMBOL_FILE_VALIDATION = {
    # Built in a weird way, see comments at top of
    # https://source.chromium.org/chromium/chromium/src/+/main:native_client/src/trusted/service_runtime/linux/nacl_bootstrap.x
    "opt/google/chrome/nacl_helper_bootstrap",
    # TODO(b/273543528): Investigate why this doesn't have stack records on
    # kevin builds.
    "build/rootfs/dlc-scaled/screen-ai/package/root/libchromescreenai.so",
}
# Same but patterns not exact paths.
ALLOWLIST_NO_SYMBOL_FILE_VALIDATION_RE = tuple(
    re.compile(x)
    for x in (
        # Only has code if use.camera_feature_effects. Otherwise will have no
        # STACK records.
        r"usr/lib[^/]*/libcros_ml_core\.so",
        # Prebuilt closed-source library.
        r"usr/lib[^/]*/python[0-9]\.[0-9]/site-packages/.*/x_ignore_nofocus.so",
        # b/273577373: Rarely used, and only by few programs that do
        # non-standard encoding conversions
        r"lib[^/]*/libnss_files\.so\.[0-9.]+",
        r"lib[^/]*/libnss_dns\.so\.[0-9.]+",
        r"usr/lib[^/]*/gconv/libISOIR165\.so",
        r"usr/lib[^/]*/gconv/libGB\.so",
        r"usr/lib[^/]*/gconv/libKSC\.so",
        r"usr/lib[^/]*/gconv/libCNS\.so",
        r"usr/lib[^/]*/gconv/libJISX0213\.so",
        r"usr/lib[^/]*/gconv/libJIS\.so",
        # TODO(b/273579075): Figure out why libcares.so is not getting STACK
        # records on kevin.
        r"usr/lib[^/]*/libcares\.so[0-9.]*",
        # libevent-2.1.so.7.0.1 does not have executable code and thus no
        # STACK records. See libevent-2.1.12-libevent-shrink.patch.
        r"usr/lib[^/]*/libevent-[0-9.]+\.so[0-9.]*",
        # TODO(b/273599604): Figure out why libdcerpc-samr.so.0.0.1 is not
        # getting STACK records on kevin.
        r"usr/lib[^/]*/libdcerpc-samr\.so[0-9.]*",
        # TODO(b/272613635): Figure out why these libabsl shared libraries are
        # not getting STACK records.
        r"usr/lib[^/]*/libabsl_bad_variant_access\.so\.[0-9.]+",
        r"usr/lib[^/]*/libabsl_random_internal_platform\.so\.[0-9.]+",
        r"usr/lib[^/]*/libabsl_flags\.so\.[0-9.]+",
        r"usr/lib[^/]*/libabsl_bad_any_cast_impl\.so\.[0-9.]+",
        r"usr/lib[^/]*/libabsl_bad_optional_access\.so\.[0-9.]+",
        # TODO(b/273607289): Figure out why libgrpc++_error_details.so.1.43.0 is
        # not getting STACK records on kevin.
        r"usr/lib[^/]*/libgrpc\+\+_error_details\.so\.[0-9.]+",
    )
)

SymbolHeader = collections.namedtuple(
    "SymbolHeader",
    (
        "cpu",
        "id",
        "name",
        "os",
    ),
)


class SymbolGenerationResult(enum.Enum):
    """Result of running dump_syms

    Return value of _DumpAllowingBasicFallback() and _DumpExpectingSymbols().
    """

    SUCCESS = 1
    UNEXPECTED_FAILURE = 2
    EXPECTED_FAILURE = 3


class ExpectedFiles(enum.Enum):
    """The files always expect to see dump_syms run on.

    We do extra validation on a few, semi-randomly chosen files. If we do not
    create symbol files for these ELFs, something is very wrong.
    """

    ASH_CHROME = enum.auto()
    LIBC = enum.auto()
    CRASH_REPORTER = enum.auto()
    LIBMETRICS = enum.auto()


ALL_EXPECTED_FILES = frozenset(
    (
        ExpectedFiles.ASH_CHROME,
        ExpectedFiles.LIBC,
        ExpectedFiles.CRASH_REPORTER,
        ExpectedFiles.LIBMETRICS,
    )
)


class SymbolFileLineCounts:
    """Counts of the various types of lines in a .sym file"""

    LINE_NUMBER_REGEX = re.compile(r"^([0-9a-f]+)")

    def __init__(self, sym_file: str, elf_file: str):
        # https://chromium.googlesource.com/breakpad/breakpad/+/HEAD/docs/symbol_files.md
        # explains what these line types are.
        self.module_lines = 0
        self.file_lines = 0
        self.inline_origin_lines = 0
        self.func_lines = 0
        self.inline_lines = 0
        self.line_number_lines = 0
        self.public_lines = 0
        self.stack_lines = 0
        # Not listed in the documentation but still present.
        self.info_lines = 0

        with open(sym_file, mode="r", encoding="utf-8") as f:
            for line in f:
                words = line.split()
                expected_words_max = None
                if not words:
                    raise ValueError(
                        f"{elf_file}: symbol file has unexpected blank line"
                    )

                line_type = words[0]
                if line_type == "MODULE":
                    self.module_lines += 1
                    expected_words_min = 5
                    expected_words_max = 5
                elif line_type == "FILE":
                    self.file_lines += 1
                    expected_words_min = 3
                    # No max, filenames can have spaces.
                elif line_type == "INLINE_ORIGIN":
                    self.inline_origin_lines += 1
                    expected_words_min = 3
                    # No max, function parameter lists can have spaces.
                elif line_type == "FUNC":
                    self.func_lines += 1
                    expected_words_min = 5
                    # No max, function parameter lists can have spaces.
                elif line_type == "INLINE":
                    self.inline_lines += 1
                    expected_words_min = 5
                    # No max, INLINE can have multiple address pairs.
                elif SymbolFileLineCounts.LINE_NUMBER_REGEX.match(line_type):
                    self.line_number_lines += 1
                    expected_words_min = 4
                    expected_words_max = 4
                    line_type = "line number"
                elif line_type == "PUBLIC":
                    self.public_lines += 1
                    expected_words_min = 4
                    if os.path.basename(elf_file).startswith("libc.so"):
                        # TODO(b/251003272): libc.so sometimes produces PUBLIC
                        # records with no symbol name. This is an error but is
                        # not affecting our ability to decode stacks.
                        expected_words_min = 3
                    # No max, function parameter lists can have spaces.
                elif line_type == "STACK":
                    self.stack_lines += 1
                    expected_words_min = 5
                    # No max, expressions can be complex.
                elif line_type == "INFO":
                    self.info_lines += 1
                    # Not documented, so unclear what the min & max are
                    expected_words_min = None
                else:
                    raise ValueError(
                        f"{elf_file}: symbol file has unknown line type "
                        f"{line_type}"
                    )

                if expected_words_max is not None:
                    if not (
                        expected_words_min <= len(words) <= expected_words_max
                    ):
                        raise ValueError(
                            f"{elf_file}: symbol file has {line_type} line "
                            f"with {len(words)} words (expected "
                            f"{expected_words_min} - {expected_words_max})"
                        )
                elif expected_words_min is not None:
                    if len(words) < expected_words_min:
                        raise ValueError(
                            f"{elf_file}: symbol file has {line_type} line "
                            f"with {len(words)} words (expected "
                            f"{expected_words_min} or more)"
                        )


def ValidateSymbolFile(
    sym_file: str,
    elf_file: str,
    sysroot: Optional[str],
    found_files: Optional[multiprocessing.managers.ListProxy],
) -> bool:
    """Checks that the given sym_file has enough info for us to get good stacks.

    Validates that the given sym_file has enough information for us to get
    good error reports -- enough STACK records to unwind the stack and enough
    FUNC or PUBLIC records to turn the function addresses into human-readable
    names.

    Args:
        sym_file: The complete path to the breakpad symbol file to validate
        elf_file: The complete path to the elf file which was the source of the
            symbol file.
        sysroot: If not None, the root of the build directory ('/build/eve', for
            instance).
        found_files: A multiprocessing.managers.ListProxy list containing
            ExpectedFiles, representing which of the "should always be present"
            files have been processed.

    Returns:
        True if the symbol file passes validation.
    """
    if sysroot is not None:
        relative_path = os.path.relpath(elf_file, sysroot)
    else:
        relative_path = os.path.relpath(elf_file, "/")

    if relative_path in ALLOWLIST_NO_SYMBOL_FILE_VALIDATION:
        return True
    for regex in ALLOWLIST_NO_SYMBOL_FILE_VALIDATION_RE:
        if regex.match(relative_path):
            return True

    counts = SymbolFileLineCounts(sym_file, elf_file)

    errors = False
    if counts.stack_lines == 0:
        # Use the elf_file in error messages; sym_file is still a temporary
        # file with a meaningless-to-humans name right now.
        logging.warning("%s: Symbol file has no STACK records", elf_file)
        errors = True
    if counts.module_lines != 1:
        logging.warning(
            "%s: Symbol file has %d MODULE lines", elf_file, counts.module_lines
        )
        errors = True
    # Many shared object files have only PUBLIC functions. In theory,
    # executables should always have at least one FUNC (main) and some line
    # numbers, but for reasons I'm unclear on, C-based executables often just
    # have PUBLIC records. dump_syms does not support line numbers after
    # PUBLIC records, only FUNC records, so such executables will also have
    # no line numbers.
    if counts.public_lines == 0 and counts.func_lines == 0:
        logging.warning(
            "%s: Symbol file has no FUNC or PUBLIC records", elf_file
        )
        errors = True
    # However, if we get a FUNC record, we do want line numbers for it.
    if counts.func_lines > 0 and counts.line_number_lines == 0:
        logging.warning(
            "%s: Symbol file has FUNC records but no line numbers", elf_file
        )
        errors = True

    if counts.line_number_lines > 0 and counts.file_lines == 0:
        logging.warning(
            "%s: Symbol file has line number records but no FILE records",
            elf_file,
        )
        errors = True
    if counts.inline_lines > 0 and counts.file_lines == 0:
        logging.warning(
            "%s: Symbol file has INLINE records but no FILE records", elf_file
        )
        errors = True

    if counts.inline_lines > 0 and counts.inline_origin_lines == 0:
        logging.warning(
            "%s: Symbol file has INLINE records but no INLINE_ORIGIN records",
            elf_file,
        )
        errors = True

    def _AddFoundFile(files, found):
        """Add another file to the list of expected files we've found."""
        if files is not None:
            files.append(found)

    # Extra validation for a few ELF files which are special. Either these are
    # unusually important to the system (chrome binary, which is where a large
    # fraction of our crashes occur, and libc.so, which is in every stack), or
    # they are some hand-chosen ELF files which stand in for "normal" platform2
    # binaries. Not all ELF files would pass the extra validation, so we can't
    # run these checks on every ELF, but we want to make sure we don't end up
    # with, say, a chrome build or a platform2 build with just one or two FUNC
    # records on every binary.
    if relative_path == "opt/google/chrome/chrome":
        _AddFoundFile(found_files, ExpectedFiles.ASH_CHROME)
        if counts.func_lines < 100000:
            logging.warning(
                "chrome should have at least 100,000 FUNC records, found %d",
                counts.func_lines,
            )
            errors = True
        if counts.stack_lines < 1000000:
            logging.warning(
                "chrome should have at least 1,000,000 STACK records, found %d",
                counts.stack_lines,
            )
            errors = True
        if counts.line_number_lines < 1000000:
            logging.warning(
                "chrome should have at least 1,000,000 line number records, "
                "found %d",
                counts.line_number_lines,
            )
            errors = True
    # Lacros symbol files are not generated as part of the ChromeOS build and
    # can't be validated here.
    # TODO(b/273836486): Add similar logic to the code that generates Lacros
    # symbols.
    elif os.path.basename(relative_path).startswith("libc.so"):
        _AddFoundFile(found_files, ExpectedFiles.LIBC)
        if counts.public_lines < 100:
            logging.warning(
                "%s should have at least 100 PUBLIC records, found %d",
                elf_file,
                counts.public_lines,
            )
            errors = True
        if counts.stack_lines < 10000:
            logging.warning(
                "%s should have at least 10000 STACK records, found %d",
                elf_file,
                counts.stack_lines,
            )
            errors = True
    elif relative_path == "sbin/crash_reporter":
        # Representative platform2 executable.
        _AddFoundFile(found_files, ExpectedFiles.CRASH_REPORTER)
        if counts.stack_lines < 1000:
            logging.warning(
                "crash_reporter should have at least 1000 STACK records, "
                "found %d",
                counts.stack_lines,
            )
            errors = True
        if counts.func_lines < 1000:
            logging.warning(
                "crash_reporter should have at least 1000 FUNC records, "
                "found %d",
                counts.func_lines,
            )
            errors = True
        if counts.line_number_lines < 10000:
            logging.warning(
                "crash_reporter should have at least 10,000 line number "
                "records, found %d",
                counts.line_number_lines,
            )
            errors = True
    elif os.path.basename(relative_path) == "libmetrics.so":
        # Representative platform2 shared library.
        _AddFoundFile(found_files, ExpectedFiles.LIBMETRICS)
        if counts.func_lines < 100:
            logging.warning(
                "libmetrics should have at least 100 FUNC records, found %d",
                counts.func_lines,
            )
            errors = True
        if counts.public_lines == 0:
            logging.warning(
                "libmetrics should have at least 1 PUBLIC record, found %d",
                counts.public_lines,
            )
            errors = True
        if counts.stack_lines < 1000:
            logging.warning(
                "libmetrics should have at least 1000 STACK records, found %d",
                counts.stack_lines,
            )
            errors = True
        if counts.line_number_lines < 5000:
            logging.warning(
                "libmetrics should have at least 5000 line number records, "
                "found %d",
                counts.line_number_lines,
            )
            errors = True

    return not errors


def _ExpectGoodSymbols(elf_file, sysroot):
    """Determines if we expect dump_syms to create good symbols.

    We know that certain types of files never generate good symbols. Distinguish
    those from the majority of elf files which should generate good symbols.

    Args:
        elf_file: The complete path to the file which we will pass to dump_syms
        sysroot: If not None, the root of the build directory ('/build/eve', for
            instance)

    Returns:
        True if the elf file should generate good symbols, False if not.
    """
    # .ko files (kernel object files) never produce good symbols.
    if elf_file.endswith(".ko"):
        return False

    # dump_syms doesn't understand Golang executables.
    result = cros_build_lib.run(
        ["/usr/bin/file", elf_file], print_cmd=False, stdout=True
    )
    if b"Go BuildID" in result.stdout:
        return False

    if sysroot is not None:
        relative_path = os.path.relpath(elf_file, sysroot)
    else:
        relative_path = os.path.relpath(elf_file, "/")

    if relative_path in EXPECTED_POOR_SYMBOLIZATION_FILES:
        return False

    # Binaries in /usr/local are not actually shipped to end-users, so we
    # don't care if they get good symbols -- we should never get crash reports
    # for them anyways.
    if relative_path.startswith("usr/local"):
        return False

    return True


def ReadSymsHeader(sym_file, name_for_errors):
    """Parse the header of the symbol file

    The first line of the syms file will read like:
      MODULE Linux arm F4F6FA6CCBDEF455039C8DE869C8A2F40 blkid

    https://code.google.com/p/google-breakpad/wiki/SymbolFiles

    Args:
      sym_file: The symbol file to parse
      name_for_errors: A name for error strings. Can be the name of the elf file
          that generated the symbol file, or the name of the symbol file if the
          symbol file has already been moved to a meaningful location.

    Returns:
      A SymbolHeader object

    Raises:
      ValueError if the first line of |sym_file| is invalid
    """
    with file_util.Open(sym_file, "rb") as f:
        header = f.readline().decode("utf-8").split()

    if len(header) != 5 or header[0] != "MODULE":
        raise ValueError(
            f"header of sym file from {name_for_errors} is invalid"
        )

    return SymbolHeader(
        os=header[1], cpu=header[2], id=header[3], name=header[4]
    )


def GenerateBreakpadSymbol(
    elf_file,
    debug_file=None,
    breakpad_dir=None,
    strip_cfi=False,
    sysroot=None,
    num_errors=None,
    found_files=None,
    dump_syms_cmd="dump_syms",
):
    """Generate the symbols for |elf_file| using |debug_file|

    Args:
      elf_file: The file to dump symbols for
      debug_file: Split debug file to use for symbol information
      breakpad_dir: The dir to store the output symbol file in
      strip_cfi: Do not generate CFI data
      sysroot: Path to the sysroot with the elf_file under it
      num_errors: An object to update with the error count (needs a .value member)
      found_files: A multiprocessing.managers.ListProxy list containing
          ExpectedFiles, representing which of the "should always be present"
          files have been processed.
      dump_syms_cmd: Command to use for dumping symbols.

    Returns:
      The name of symbol file written out on success, or the failure count.
    """
    assert breakpad_dir
    if num_errors is None:
        num_errors = ctypes.c_int()
    debug_file_only = not os.path.exists(elf_file)

    cmd_base = [dump_syms_cmd, "-v"]
    if strip_cfi:
        cmd_base += ["-c"]
    # Some files will not be readable by non-root (e.g. set*id /bin/su).
    needs_sudo = not os.access(elf_file, os.R_OK)

    def _DumpIt(cmd_args):
        if needs_sudo:
            run_command = cros_build_lib.sudo_run
        else:
            run_command = cros_build_lib.run
        return run_command(
            cmd_base + cmd_args,
            stderr=True,
            stdout=temp.name,
            check=False,
            debug_level=logging.DEBUG,
        )

    def _CrashCheck(result, file_or_files, msg):
        if result.returncode:
            cbuildbot_alerts.PrintBuildbotStepWarnings()
            if result.returncode < 0:
                logging.warning(
                    "dump_syms %s crashed with %s; %s",
                    file_or_files,
                    signals.StrSignal(-result.returncode),
                    msg,
                )
            else:
                logging.warning(
                    "dump_syms %s returned %d; %s",
                    file_or_files,
                    result.returncode,
                    msg,
                )
            logging.warning("output:\n%s", result.stderr.decode("utf-8"))

    def _DumpAllowingBasicFallback():
        """Dump symbols for an ELF when we do NOT expect to get good symbols.

        Returns:
            A SymbolGenerationResult
        """
        if debug_file:
            # Try to dump the symbols using the debug file like normal.
            if debug_file_only:
                cmd_args = [debug_file]
                file_or_files = debug_file
            else:
                cmd_args = [elf_file, os.path.dirname(debug_file)]
                file_or_files = [elf_file, debug_file]

            result = _DumpIt(cmd_args)

            if result.returncode:
                # Sometimes dump_syms can crash because there's too much info.
                # Try dumping and stripping the extended stuff out.  At least
                # this way we'll get the extended symbols.
                #  https://crbug.com/266064
                _CrashCheck(result, file_or_files, "retrying w/out CFI")
                cmd_args = ["-c", "-r"] + cmd_args
                result = _DumpIt(cmd_args)
                _CrashCheck(result, file_or_files, "retrying w/out debug")

            if not result.returncode:
                return SymbolGenerationResult.SUCCESS

        # If that didn't work (no debug, or dump_syms still failed), try
        # dumping just the file itself directly.
        result = _DumpIt([elf_file])
        if result.returncode:
            # A lot of files (like kernel files) contain no debug information,
            # do not consider such occurrences as errors.
            cbuildbot_alerts.PrintBuildbotStepWarnings()
            if b"file contains no debugging information" in result.stderr:
                logging.warning("dump_syms failed; giving up entirely.")
                logging.warning("No symbols found for %s", elf_file)
                return SymbolGenerationResult.EXPECTED_FAILURE
            else:
                _CrashCheck(result, elf_file, "counting as failure")
                return SymbolGenerationResult.UNEXPECTED_FAILURE

        return SymbolGenerationResult.SUCCESS

    def _DumpExpectingSymbols():
        """Dump symbols for an ELF when we expect to get good symbols.

        Returns:
            A SymbolGenerationResult. We never expect failure, so the result
            will always be SUCCESS or UNEXPECTED_FAILURE.
        """
        if not debug_file:
            logging.warning("%s must have debug file", elf_file)
            return SymbolGenerationResult.UNEXPECTED_FAILURE

        cmd_args = [elf_file, os.path.dirname(debug_file)]
        result = _DumpIt(cmd_args)
        if result.returncode:
            _CrashCheck(result, [elf_file, debug_file], "unexpected failure")
            return SymbolGenerationResult.UNEXPECTED_FAILURE

        # TODO(b/270240549): Remove try/except, allow exceptions to just
        # fail the script. The try/except is just here until we are sure this
        # will not break the build.
        try:
            if not ValidateSymbolFile(
                temp.name, elf_file, sysroot, found_files
            ):
                logging.warning("%s: symbol file failed validation", elf_file)
                return SymbolGenerationResult.UNEXPECTED_FAILURE
        except ValueError as e:
            logging.warning(
                "%s: symbol file failed validation due to exception %s",
                elf_file,
                e,
            )
            return SymbolGenerationResult.UNEXPECTED_FAILURE

        return SymbolGenerationResult.SUCCESS

    osutils.SafeMakedirs(breakpad_dir)
    with cros_build_lib.UnbufferedNamedTemporaryFile(
        dir=breakpad_dir, delete=False
    ) as temp:
        if _ExpectGoodSymbols(elf_file, sysroot):
            result = _DumpExpectingSymbols()
            # Until the EXPECTED_POOR_SYMBOLIZATION_FILES allowlist is
            # completely set up for all boards, don't fail the build if
            # _ExpectGoodSymbols is wrong.
            # TODO(b/241470012): Remove the call to _DumpAllowingBasicFallback()
            # and just error out if _DumpExpectingSymbols fails.
            if result == SymbolGenerationResult.UNEXPECTED_FAILURE:
                result = _DumpAllowingBasicFallback()
        else:
            result = _DumpAllowingBasicFallback()

        if result == SymbolGenerationResult.UNEXPECTED_FAILURE:
            num_errors.value += 1
            os.unlink(temp.name)
            return num_errors.value

        if result == SymbolGenerationResult.EXPECTED_FAILURE:
            os.unlink(temp.name)
            return 0

        # Move the dumped symbol file to the right place:
        # /build/$BOARD/usr/lib/debug/breakpad/<module-name>/<id>/<module-name>.sym
        header = ReadSymsHeader(temp, elf_file)
        logging.info("Dumped %s as %s : %s", elf_file, header.name, header.id)
        sym_file = os.path.join(
            breakpad_dir, header.name, header.id, header.name + ".sym"
        )
        osutils.SafeMakedirs(os.path.dirname(sym_file))
        os.rename(temp.name, sym_file)
        os.chmod(sym_file, 0o644)

    return sym_file


def GenerateBreakpadSymbols(
    board,
    breakpad_dir=None,
    strip_cfi=False,
    generate_count=None,
    sysroot=None,
    num_processes=None,
    clean_breakpad=False,
    exclude_dirs=(),
    file_list=None,
):
    """Generate symbols for this board.

    If |file_list| is None, symbols are generated for all executables, otherwise
    only for the files included in |file_list|.

    TODO(build):
    This should be merged with buildbot_commands.GenerateBreakpadSymbols()
    once we rewrite cros_generate_breakpad_symbols in python.

    Args:
      board: The board whose symbols we wish to generate
      breakpad_dir: The full path to the breakpad directory where symbols live
      strip_cfi: Do not generate CFI data
      generate_count: If set, only generate this many symbols (meant for testing)
      sysroot: The root where to find the corresponding ELFs
      num_processes: Number of jobs to run in parallel
      clean_breakpad: Should we `rm -rf` the breakpad output dir first; note: we
        do not do any locking, so do not run more than one in parallel when True
      exclude_dirs: List of dirs (relative to |sysroot|) to not search
      file_list: Only generate symbols for files in this list. Each file must be a
        full path (including |sysroot| prefix).
        TODO(build): Support paths w/o |sysroot|.

    Returns:
      The number of errors that were encountered.
    """
    if sysroot is None:
        sysroot = build_target_lib.get_default_sysroot_path(board)
    if breakpad_dir is None:
        breakpad_dir = FindBreakpadDir(board, sysroot=sysroot)
    if clean_breakpad:
        logging.info("cleaning out %s first", breakpad_dir)
        osutils.RmDir(breakpad_dir, ignore_missing=True, sudo=True)
    # Make sure non-root can write out symbols as needed.
    osutils.SafeMakedirs(breakpad_dir, sudo=True)
    if not os.access(breakpad_dir, os.W_OK):
        cros_build_lib.sudo_run(["chown", "-R", str(os.getuid()), breakpad_dir])
    debug_dir = FindDebugDir(board, sysroot=sysroot)
    exclude_paths = [os.path.join(debug_dir, x) for x in exclude_dirs]
    if file_list is None:
        file_list = []
    file_filter = dict.fromkeys([os.path.normpath(x) for x in file_list], False)

    logging.info("generating breakpad symbols using %s", debug_dir)

    # Let's locate all the debug_files and elfs first along with the debug file
    # sizes.  This way we can start processing the largest files first in parallel
    # with the small ones.
    # If |file_list| was given, ignore all other files.
    targets = []
    for root, dirs, files in os.walk(debug_dir):
        if root in exclude_paths:
            logging.info("Skipping excluded dir %s", root)
            del dirs[:]
            continue

        for debug_file in files:
            debug_file = os.path.join(root, debug_file)
            # Turn /build/$BOARD/usr/lib/debug/sbin/foo.debug into
            # /build/$BOARD/sbin/foo.
            elf_file = os.path.join(
                sysroot, debug_file[len(debug_dir) + 1 : -6]
            )

            if file_filter:
                if elf_file in file_filter:
                    file_filter[elf_file] = True
                elif debug_file in file_filter:
                    file_filter[debug_file] = True
                else:
                    continue

            # Filter out files based on common issues with the debug file.
            if not debug_file.endswith(".debug"):
                continue

            elif os.path.islink(debug_file):
                # The build-id stuff is common enough to filter out by default.
                if "/.build-id/" in debug_file:
                    msg = logging.debug
                else:
                    msg = logging.warning
                msg("Skipping symbolic link %s", debug_file)
                continue

            # Filter out files based on common issues with the elf file.
            elf_path = os.path.relpath(elf_file, sysroot)
            debug_only = elf_path in ALLOWED_DEBUG_ONLY_FILES
            if not os.path.exists(elf_file) and not debug_only:
                # Sometimes we filter out programs from /usr/bin but leave behind
                # the .debug file.
                logging.warning("Skipping missing %s", elf_file)
                continue

            targets.append((os.path.getsize(debug_file), elf_file, debug_file))

    with multiprocessing.Manager() as mp_manager:
        bg_errors = parallel.WrapMultiprocessing(multiprocessing.Value, "i")
        found_files = parallel.WrapMultiprocessing(mp_manager.list)
        if file_filter:
            files_not_found = [
                x for x, found in file_filter.items() if not found
            ]
            bg_errors.value += len(files_not_found)
            if files_not_found:
                logging.error(
                    "Failed to find requested files: %s", files_not_found
                )

        # Now start generating symbols for the discovered elfs.
        with parallel.BackgroundTaskRunner(
            GenerateBreakpadSymbol,
            breakpad_dir=breakpad_dir,
            strip_cfi=strip_cfi,
            num_errors=bg_errors,
            processes=num_processes,
            sysroot=sysroot,
            found_files=found_files,
        ) as queue:
            for _, elf_file, debug_file in sorted(targets, reverse=True):
                if generate_count == 0:
                    break

                queue.put([elf_file, debug_file])
                if generate_count is not None:
                    generate_count -= 1
                    if generate_count == 0:
                        break

        missing = ALL_EXPECTED_FILES - frozenset(found_files)
        if missing and not file_filter and generate_count is None:
            logging.warning(
                "Not all expected files were processed successfully, "
                "missing %s",
                missing,
            )
            # TODO(b/270240549): Increment bg_errors.value here once we check
            # that this isn't going to fail any current builds.

    return bg_errors.value


def FindDebugDir(board, sysroot=None):
    """Given a |board|, return the path to the split debug dir for it"""
    if sysroot is None:
        sysroot = build_target_lib.get_default_sysroot_path(board)
    return os.path.join(sysroot, "usr", "lib", "debug")


def FindBreakpadDir(board, sysroot=None):
    """Given a |board|, return the path to the breakpad dir for it"""
    return os.path.join(FindDebugDir(board, sysroot=sysroot), "breakpad")


def main(argv):
    parser = commandline.ArgumentParser(description=__doc__)

    parser.add_argument(
        "--board", default=None, help="board to generate symbols for"
    )
    parser.add_argument(
        "--breakpad_root",
        type="path",
        default=None,
        help="root output directory for breakpad symbols",
    )
    parser.add_argument(
        "--sysroot",
        type="path",
        default=None,
        help="root input directory for files",
    )
    parser.add_argument(
        "--exclude-dir",
        type=str,
        action="append",
        default=[],
        help="directory (relative to |board| root) to not search",
    )
    parser.add_argument(
        "--generate-count",
        type=int,
        default=None,
        help="only generate # number of symbols",
    )
    parser.add_argument(
        "--noclean",
        dest="clean",
        action="store_false",
        default=True,
        help="do not clean out breakpad dir before running",
    )
    parser.add_argument(
        "--jobs", type=int, default=None, help="limit number of parallel jobs"
    )
    parser.add_argument(
        "--strip_cfi",
        action="store_true",
        default=False,
        help="do not generate CFI data (pass -c to dump_syms)",
    )
    parser.add_argument(
        "file_list",
        nargs="*",
        default=None,
        help="generate symbols for only these files "
        "(e.g. /build/$BOARD/usr/bin/foo)",
    )

    opts = parser.parse_args(argv)
    opts.Freeze()

    if opts.board is None and opts.sysroot is None:
        cros_build_lib.Die("--board or --sysroot is required")

    ret = GenerateBreakpadSymbols(
        opts.board,
        breakpad_dir=opts.breakpad_root,
        strip_cfi=opts.strip_cfi,
        generate_count=opts.generate_count,
        sysroot=opts.sysroot,
        num_processes=opts.jobs,
        clean_breakpad=opts.clean,
        exclude_dirs=opts.exclude_dir,
        file_list=opts.file_list,
    )
    if ret:
        logging.error("encountered %i problem(s)", ret)
        # Since exit(status) gets masked, clamp it to 1 so we don't inadvertently
        # return 0 in case we are a multiple of the mask.
        ret = 1

    return ret
