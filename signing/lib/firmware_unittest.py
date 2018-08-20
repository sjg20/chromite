# -*- coding: utf-8 -*-
# Copyright 2018 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Tests Firmware related signing"""

from __future__ import print_function

import os

from chromite.lib import cros_test_lib
from chromite.lib import osutils
from chromite.signing.lib import firmware
from chromite.signing.lib import keys
from chromite.signing.lib import keys_unittest
from chromite.signing.lib import signer_unittest


class TestBiosSigner(cros_test_lib.RunCommandTestCase,
                     cros_test_lib.TempDirTestCase):
  """Test BiosSigner."""

  def testGetCmdArgs(self):
    bs = firmware.BiosSigner()
    ks = signer_unittest.KeysetFromSigner(bs, self.tempdir)

    self.assertListEqual(bs.GetFutilityArgs(ks, 'foo', 'bar'),
                         ['sign',
                          '--type', 'bios',
                          '--signprivate', ks.keys['firmware'].private,
                          '--keyblock', ks.keyblocks['firmware'].filename,
                          '--kernelkey', ks.keys['kernel'].public,
                          '--version', str(bs.version),
                          '--devsign', ks.keys['firmware'].private,
                          '--devkeyblock', ks.keyblocks['firmware'].filename,
                          'foo', 'bar'])

  def testGetCmdArgsWithDevKeys(self):
    bs = firmware.BiosSigner()
    ks = signer_unittest.KeysetFromSigner(bs, self.tempdir)

    # Add 'dev_firmware' keys and keyblock
    ks.AddKey(keys.KeyPair('dev_firmware', keydir=self.tempdir))
    keys_unittest.CreateDummyPrivateKey(ks.GetKey('dev_firmware'))

    ks.AddKeyblock(ks.keys['dev_firmware'].CreateKeyblock())
    keys_unittest.CreateDummyKeyblock(ks.GetKeyblock('dev_firmware'))

    self.assertListEqual(bs.GetFutilityArgs(ks, 'foo', 'bar'),
                         ['sign',
                          '--type', 'bios',
                          '--signprivate', ks.keys['firmware'].private,
                          '--keyblock', ks.keyblocks['firmware'].filename,
                          '--kernelkey', ks.keys['kernel'].public,
                          '--version', str(bs.version),
                          '--devsign', ks.keys['dev_firmware'].private,
                          '--devkeyblock',
                          ks.keyblocks['dev_firmware'].filename,
                          'foo', 'bar'])

  def testGetCmdArgsWithSig(self):
    loem_dir = os.path.join(self.tempdir, 'loem')
    loem_id = 'loem1'
    bs = firmware.BiosSigner(sig_dir=loem_dir, sig_id=loem_id)
    ks = signer_unittest.KeysetFromSigner(bs, self.tempdir)

    self.assertListEqual(bs.GetFutilityArgs(ks, 'foo', 'bar'),
                         ['sign',
                          '--type', 'bios',
                          '--signprivate', ks.keys['firmware'].private,
                          '--keyblock', ks.keyblocks['firmware'].filename,
                          '--kernelkey', ks.keys['kernel'].public,
                          '--version', str(bs.version),
                          '--devsign', ks.keys['firmware'].private,
                          '--devkeyblock', ks.keyblocks['firmware'].filename,
                          '--loemdir', loem_dir,
                          '--loemid', loem_id,
                          'foo', 'bar'])


class TestECSigner(cros_test_lib.RunCommandTestCase,
                   cros_test_lib.TempDirTestCase):
  """Test ECSigner."""

  def testGetCmdArgs(self):
    ecs = firmware.ECSigner()
    ks = signer_unittest.KeysetFromSigner(ecs, self.tempdir)

    self.assertListEqual(ecs.GetFutilityArgs(ks, 'foo', 'bar'),
                         ['sign',
                          '--type', 'rwsig',
                          '--prikey', ks.keys['ec'].private,
                          'foo', 'bar'])


class ShellballTest(cros_test_lib.RunCommandTestCase,
                    cros_test_lib.TempDirTestCase):
  """Verify that shellball is being called with correct arguments."""

  def setUp(self):
    """Setup simple Shellball instance for mock testing."""
    self.sb1name = os.path.join(self.tempdir, 'fooball')
    osutils.Touch(self.sb1name)
    self.sb1 = firmware.Shellball(self.sb1name)

  def testExtractCall(self):
    """Test arguments for image extract."""
    out_dir = 'bar'
    expected_args = ['--sb_extract', out_dir]

    self.sb1.Extract(out_dir)
    self.assertCommandContains(expected_args)

  def testRepackCall(self):
    """Test arguments for image repack."""
    from_dir = 'bar'
    expected_args = ['--sb_repack', from_dir]

    self.sb1.Repack(from_dir)
    self.assertCommandContains(expected_args)

  def testContextManager(self):
    with self.sb1 as sb_dir:
      self.assertExists(sb_dir)
      self.assertCommandContains(['--sb_extract'])
    self.assertCommandContains(['--sb_repack'])
