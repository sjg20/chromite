# -*- coding: utf-8 -*-
# Copyright (c) 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Configuration options for various cbuildbot tests."""

from __future__ import print_function

from chromite.lib import config_lib
from chromite.lib import constants

from chromite.config import chromeos_config_boards as config_boards

vmtest_boards = frozenset([
    # Full VMTest support on ChromeOS is currently limited to devices derived
    # from betty & co.
    'amd64-generic', # Has kernel 4.4, used with public Chromium.
    'betty',         # amd64 Chrome OS VM board with 32 bit arm/x86 ARC++ ABI.
    'betty-arc64',   # Chrome OS VM board with 64 bit x86_64 ARC++ ABI.
    'betty-arcnext', # Like betty but with the next version of ARC++.
    'novato',        # Like betty but with GMSCore but not the Play Store
    'novato-arc64',  # 64 bit x86_64 ARC++ ABI
]) | config_boards.lakitu_boards  # All lakitu boards have VM support.

def getInfoVMTest():
  suites = [
      'vmtest-informational4'
  ]
  ret = []
  for suite in suites:
    ret.append(config_lib.VMTestConfig(
        constants.VM_SUITE_TEST_TYPE,
        test_suite=suite,
        warn_only=True,
        timeout=12 * 60 * 60))
  return ret


class HWTestList(object):
  """Container for methods to generate HWTest lists."""

  def __init__(self, ge_build_config):
    """Helper class for creating hwtests.

    Args:
      ge_build_config: Dictionary containing the decoded GE configuration file.
    """
    self.is_release_branch = ge_build_config[
        config_lib.CONFIG_TEMPLATE_RELEASE_BRANCH]

  def DefaultList(self, **kwargs):
    """Returns a default list of HWTestConfigs for a build.

    Args:
      *kwargs: overrides for the configs
    """
    installer_kwargs = kwargs.copy()
    # Force au suite to run first.
    installer_kwargs['priority'] = constants.HWTEST_CQ_PRIORITY

    async_kwargs = kwargs.copy()
    async_kwargs['priority'] = constants.HWTEST_POST_BUILD_PRIORITY
    async_kwargs['async'] = True
    async_kwargs['suite_min_duts'] = 1
    async_kwargs['timeout'] = config_lib.HWTestConfig.ASYNC_HW_TEST_TIMEOUT

    if self.is_release_branch:
      bvt_inline_kwargs = async_kwargs
    else:
      bvt_inline_kwargs = kwargs.copy()
      bvt_inline_kwargs['timeout'] = (
          config_lib.HWTestConfig.SHARED_HW_TEST_TIMEOUT)

    # BVT + INSTALLER suite.
    return [
        config_lib.HWTestConfig(constants.HWTEST_BVT_SUITE,
                                **bvt_inline_kwargs),
        config_lib.HWTestConfig(constants.HWTEST_ARC_COMMIT_SUITE,
                                **bvt_inline_kwargs),
        self.TastConfig(constants.HWTEST_TAST_CQ_SUITE, **bvt_inline_kwargs),
        config_lib.HWTestConfig(constants.HWTEST_INSTALLER_SUITE,
                                blocking=True, **installer_kwargs),
        config_lib.HWTestConfig(constants.HWTEST_COMMIT_SUITE,
                                **async_kwargs),
        config_lib.HWTestConfig(constants.HWTEST_CANARY_SUITE,
                                **async_kwargs),
    ]

  def DefaultListCanary(self, **kwargs):
    """Returns a default list of config_lib.HWTestConfig's for a canary build.

    Args:
      *kwargs: overrides for the configs
    """
    # Set minimum_duts default to 4, which means that lab will check the
    # number of available duts to meet the minimum requirement before creating
    # the suite job for canary builds.
    kwargs.setdefault('minimum_duts', 4)
    kwargs.setdefault('file_bugs', True)
    return self.DefaultList(**kwargs)

  def AFDOList(self, **kwargs):
    """Returns a default list of HWTestConfigs for a AFDO build.

    For more details on AFDO:
    - https://gcc.gnu.org/wiki/AutoFDO
    - https://sites.google.com/a/google.com/chromeos-toolchain-team-home2
      -> 11. AFDO PROFILE-GUIDED OPTIMIZATIONS

    Args:
      *kwargs: overrides for the configs
    """
    afdo_dict = dict(pool=constants.HWTEST_SUITES_POOL,
                     timeout=120 * 60, async=True, retry=False,
                     max_retries=None)
    afdo_dict.update(kwargs)
    return [config_lib.HWTestConfig('perf_v2', **afdo_dict)]

  def DefaultListNonCanary(self, **kwargs):
    """Return a default list of HWTestConfigs for a non-canary build.

    Optional arguments may be overridden in `kwargs`, except that
    the `blocking` setting cannot be provided.
    """
    # N.B.  The ordering here is coupled with the column order of
    # entries in _paladin_hwtest_assignments, below.  If you change the
    # ordering here you must also change the ordering there.
    return [
        config_lib.HWTestConfig(
            constants.HWTEST_PROVISION_SUITE,
            blocking=True,
            suite_args={'num_required': 1},
            **kwargs),
        config_lib.HWTestConfig(constants.HWTEST_BVT_SUITE,
                                **kwargs),
        config_lib.HWTestConfig(constants.HWTEST_COMMIT_SUITE,
                                **kwargs),
        config_lib.HWTestConfig(constants.HWTEST_ARC_COMMIT_SUITE,
                                **kwargs)]

  def DefaultListCQ(self, **kwargs):
    """Return a default list of HWTestConfigs for a CQ build.

    Optional arguments may be overridden in `kwargs`, except that
    the `blocking` setting cannot be provided.
    """
    default_dict = dict(pool=constants.HWTEST_PALADIN_POOL,
                        timeout=config_lib.HWTestConfig.PALADIN_HW_TEST_TIMEOUT,
                        file_bugs=False, priority=constants.HWTEST_CQ_PRIORITY,
                        minimum_duts=4)
    # Allows kwargs overrides to default_dict for cq.
    default_dict.update(kwargs)
    suite_list = self.DefaultListNonCanary(**default_dict)
    suite_list.append(self.TastConfig(constants.HWTEST_TAST_CQ_SUITE,
                                      **default_dict))
    return suite_list

  def DefaultListPFQ(self, **kwargs):
    """Return a default list of HWTestConfigs for a Chrome PFQ build.

    Optional arguments may be overridden in `kwargs`, except that
    the `blocking` setting cannot be provided.
    """
    default_dict = dict(pool=constants.HWTEST_PFQ_POOL, file_bugs=True,
                        priority=constants.HWTEST_PFQ_PRIORITY,
                        minimum_duts=4)
    # Allows kwargs overrides to default_dict for pfq.
    default_dict.update(kwargs)
    suite_list = self.DefaultListNonCanary(**default_dict)
    suite_list.append(self.TastConfig(constants.HWTEST_TAST_CHROME_PFQ_SUITE,
                                      **default_dict))
    return suite_list

  def DefaultListChromePFQInformational(self, **kwargs):
    """Return a default list of HWTestConfigs for an inform. Chrome PFQ build.

    Optional arguments may be overridden in `kwargs`, except that
    the `blocking` setting cannot be provided.
    """
    # The informational PFQ does not honor to retry jobs. This reduces
    # hwtest times and shows flakes clearer.
    default_dict = dict(pool=constants.HWTEST_PFQ_POOL, file_bugs=True,
                        priority=constants.HWTEST_PFQ_PRIORITY,
                        retry=False, max_retries=None, minimum_duts=1)
    # Allows kwargs overrides to default_dict for pfq.
    default_dict.update(kwargs)
    suite_list = self.DefaultListNonCanary(**default_dict)
    suite_list.append(config_lib.HWTestConfig(
        constants.HWTEST_CHROME_INFORMATIONAL, warn_only=True, **default_dict))
    suite_list.append(self.TastConfig(constants.HWTEST_TAST_CHROME_PFQ_SUITE,
                                      **default_dict))
    return suite_list

  def SharedPoolPFQ(self, **kwargs):
    """Return a list of HWTestConfigs for Chrome PFQ which uses a shared pool.

    The returned suites will run in pool:critical by default, which is
    shared with other types of builders (canaries, cq). The first suite in the
    list is a blocking sanity suite that verifies the build will not break dut.
    """
    sanity_dict = dict(pool=constants.HWTEST_MACH_POOL,
                       file_bugs=True, priority=constants.HWTEST_PFQ_PRIORITY)
    sanity_dict.update(kwargs)
    sanity_dict.update(dict(minimum_duts=1, suite_min_duts=1,
                            blocking=True))
    default_dict = dict(pool=constants.HWTEST_MACH_POOL,
                        suite_min_duts=3)
    default_dict.update(kwargs)
    suite_list = [config_lib.HWTestConfig(constants.HWTEST_SANITY_SUITE,
                                          **sanity_dict)]
    suite_list.extend(self.DefaultListPFQ(**default_dict))
    return suite_list

  def DefaultListAndroidPFQ(self, **kwargs):
    """Return a default list of HWTestConfig's for an ARC PFQ build.

    Optional arguments may be overridden in `kwargs`, except that
    the `blocking` setting cannot be provided.
    """
    default_dict = dict(file_bugs=True,
                        timeout=config_lib.HWTestConfig.ASYNC_HW_TEST_TIMEOUT,
                        priority=constants.HWTEST_PFQ_PRIORITY, minimum_duts=3)
    # Allows kwargs overrides to default_dict for pfq.
    default_dict.update(kwargs)

    return [
        config_lib.HWTestConfig(constants.HWTEST_ARC_COMMIT_SUITE,
                                pool=constants.HWTEST_MACH_POOL,
                                **default_dict),
        self.TastConfig(constants.HWTEST_TAST_ANDROID_PFQ_SUITE,
                        pool=constants.HWTEST_MACH_POOL, **default_dict),
    ]

  def SharedPoolAndroidPFQ(self, **kwargs):
    """Return a list of HWTestConfigs for ARC PFQ which uses a shared pool.

    The returned suites will run in pool:critical by default, which is
    shared with other types of builders (canaries, cq). The first suite in the
    list is a blocking sanity suite that verifies the build will not break dut.
    """
    sanity_dict = dict(pool=constants.HWTEST_MACH_POOL,
                       file_bugs=True, priority=constants.HWTEST_PFQ_PRIORITY)
    sanity_dict.update(kwargs)
    sanity_dict.update(dict(minimum_duts=1, suite_min_duts=1,
                            blocking=True))
    default_dict = dict(suite_min_duts=3)
    default_dict.update(kwargs)
    suite_list = [config_lib.HWTestConfig(constants.HWTEST_SANITY_SUITE,
                                          **sanity_dict)]
    suite_list.extend(self.DefaultListAndroidPFQ(**default_dict))
    return suite_list

  def SharedPoolCQ(self, **kwargs):
    """Return a list of HWTestConfigs for CQ which uses a shared pool.

    The returned suites will run in pool:critical by default, which is
    shared with other types of builder (canaries, pfq). The first suite in the
    list is a blocking sanity suite that verifies the build will not break dut.
    """
    sanity_dict = dict(pool=constants.HWTEST_MACH_POOL,
                       timeout=config_lib.HWTestConfig.SHARED_HW_TEST_TIMEOUT,
                       file_bugs=False, priority=constants.HWTEST_CQ_PRIORITY)
    sanity_dict.update(kwargs)
    sanity_dict.update(dict(minimum_duts=1, suite_min_duts=1,
                            blocking=True))
    default_dict = dict(pool=constants.HWTEST_MACH_POOL,
                        suite_min_duts=10)
    default_dict.update(kwargs)
    suite_list = [config_lib.HWTestConfig(constants.HWTEST_SANITY_SUITE,
                                          **sanity_dict)]
    suite_list.extend(self.DefaultListCQ(**default_dict))
    return suite_list

  def SharedPoolCanary(self, **kwargs):
    """Return a list of HWTestConfigs for Canary which uses a shared pool.

    The returned suites will run in pool:critical by default, which is
    shared with CQs. The first suite in the list is a blocking sanity suite
    that verifies the build will not break dut.
    """
    sanity_dict = dict(pool=constants.HWTEST_MACH_POOL, file_bugs=True)
    sanity_dict.update(kwargs)
    sanity_dict.update(dict(minimum_duts=1, suite_min_duts=1,
                            blocking=True))
    default_dict = dict(pool=constants.HWTEST_MACH_POOL,
                        suite_min_duts=6)
    default_dict.update(kwargs)
    suite_list = [config_lib.HWTestConfig(constants.HWTEST_SANITY_SUITE,
                                          **sanity_dict)]
    suite_list.extend(self.DefaultListCanary(**default_dict))
    return suite_list

  def AFDORecordTest(self, **kwargs):
    default_dict = dict(pool=constants.HWTEST_MACH_POOL,
                        warn_only=True, file_bugs=True,
                        timeout=constants.AFDO_GENERATE_TIMEOUT,
                        priority=constants.HWTEST_PFQ_PRIORITY)
    # Allows kwargs overrides to default_dict for cq.
    default_dict.update(kwargs)
    return config_lib.HWTestConfig(constants.HWTEST_AFDO_SUITE, **default_dict)

  def WiFiCellPoolPreCQ(self, **kwargs):
    """Return a list of HWTestConfigs which run wifi tests.

    This should be used by the ChromeOS WiFi team to ensure changes pass the
    wifi tests as a pre-cq sanity check.
    """
    default_dict = dict(pool=constants.HWTEST_WIFICELL_PRE_CQ_POOL,
                        file_bugs=False,
                        priority=constants.HWTEST_DEFAULT_PRIORITY,
                        retry=False, max_retries=None, minimum_duts=1)
    default_dict.update(kwargs)
    suite_list = [config_lib.HWTestConfig(constants.WIFICELL_PRE_CQ,
                                          **default_dict)]
    return suite_list

  def BluestreakPoolPreCQ(self, **kwargs):
    """Return a list of HWTestConfigs which run bluestreak tests.

    This should be used by the ChromeOS MRHW team to ensure changes pass the
    CFM tests as a pre-cq sanity check.
    """
    default_dict = dict(pool=constants.HWTEST_BLUESTREAK_PRE_CQ_POOL,
                        file_bugs=False,
                        priority=constants.HWTEST_DEFAULT_PRIORITY,
                        retry=False, max_retries=None, minimum_duts=1)
    default_dict.update(kwargs)
    suite_list = [config_lib.HWTestConfig(constants.BLUESTREAK_PRE_CQ,
                                          **default_dict)]
    return suite_list

  def ToolchainTestFull(self, machine_pool, **kwargs):
    """Return full set of HWTESTConfigs to run toolchain correctness tests."""
    default_dict = dict(pool=machine_pool, async=False,
                        file_bugs=False,
                        priority=constants.HWTEST_DEFAULT_PRIORITY)
    default_dict.update(kwargs)
    return [config_lib.HWTestConfig(constants.HWTEST_BVT_SUITE,
                                    **default_dict),
            config_lib.HWTestConfig(constants.HWTEST_COMMIT_SUITE,
                                    **default_dict),
            self.TastConfig(constants.HWTEST_TAST_CQ_SUITE,
                            **default_dict),
            config_lib.HWTestConfig('security',
                                    **default_dict),
            config_lib.HWTestConfig('kernel_daily_regression',
                                    **default_dict),
            config_lib.HWTestConfig('kernel_daily_benchmarks',
                                    **default_dict)]

  def ToolchainTestMedium(self, machine_pool, **kwargs):
    """Return list of HWTESTConfigs to run toolchain LLVM correctness tests.

    Since the kernel is not built with LLVM, it makes no sense for the
    toolchain to run kernel tests on LLVM builds.
    """
    default_dict = dict(pool=machine_pool, async=False,
                        file_bugs=False,
                        priority=constants.HWTEST_DEFAULT_PRIORITY)
    default_dict.update(kwargs)
    return [config_lib.HWTestConfig(constants.HWTEST_BVT_SUITE,
                                    **default_dict),
            config_lib.HWTestConfig(constants.HWTEST_COMMIT_SUITE,
                                    **default_dict),
            self.TastConfig(constants.HWTEST_TAST_CQ_SUITE,
                            **default_dict),
            config_lib.HWTestConfig('security',
                                    **default_dict)]

  # pylint: disable=unused-argument
  def CtsGtsQualTests(self, **kwargs):
    """Return a list of HWTestConfigs for CTS, GTS tests."""
    cts_config = dict(
        pool=constants.HWTEST_CTS_POOL,
        timeout=config_lib.HWTestConfig.CTS_QUAL_HW_TEST_TIMEOUT,
        priority=constants.HWTEST_CTS_PRIORITY,
        async=True,
        enable_skylab=False)
    cts_config.update(kwargs)

    gts_config = dict(
        pool=constants.HWTEST_GTS_POOL,
        timeout=config_lib.HWTestConfig.GTS_QUAL_HW_TEST_TIMEOUT,
        priority=constants.HWTEST_GTS_PRIORITY,
        async=True,
        enable_skylab=False)
    gts_config.update(kwargs)

    return [config_lib.HWTestConfig(constants.HWTEST_CTS_QUAL_SUITE,
                                    **cts_config),
            config_lib.HWTestConfig(constants.HWTEST_GTS_QUAL_SUITE,
                                    **gts_config)]

  def TastConfig(self, suite_name, **kwargs):
    """Return an HWTestConfig that runs the provided Tast test suite.

    Args:
      suite_name: String suite name, e.g. constants.HWTEST_TAST_CQ_SUITE.
      kwargs: Dict containing additional keyword args to use when constructing
              the HWTestConfig.

    Returns:
      HWTestConfig object for running the suite.
    """
    kwargs = kwargs.copy()

    # Tast test suites run at most three jobs (for system, Chrome, and Android
    # tests) and have short timeouts, so request at most 1 DUT (while retaining
    # passed-in requests for 0 DUTs).
    if kwargs.get('minimum_duts', 0):
      kwargs['minimum_duts'] = 1
    if kwargs.get('suite_min_duts', 0):
      kwargs['suite_min_duts'] = 1

    return config_lib.HWTestConfig(suite_name, **kwargs)

TRADITIONAL_VM_TESTS_SUPPORTED = [
    config_lib.VMTestConfig(constants.VM_SUITE_TEST_TYPE,
                            test_suite='smoke',
                            use_ctest=False),
    config_lib.VMTestConfig(constants.SIMPLE_AU_TEST_TYPE),
    config_lib.VMTestConfig(constants.CROS_VM_TEST_TYPE)]
