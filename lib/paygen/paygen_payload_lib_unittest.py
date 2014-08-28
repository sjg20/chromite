#!/usr/bin/python
# Copyright (c) 2013 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test Utils library."""

import mox
import os
import shutil
import tempfile

import fixup_path
fixup_path.FixupPath()

from chromite.lib import cros_build_lib
from chromite.lib import cros_test_lib
from chromite.lib import osutils

from chromite.lib.paygen import download_cache
from chromite.lib.paygen import gspaths
from chromite.lib.paygen import paygen_payload_lib
from chromite.lib.paygen import signer_payloads_client
from chromite.lib.paygen import urilib


# We access a lot of protected members during testing.
# pylint: disable-msg=W0212


class PaygenPayloadLibTest(mox.MoxTestBase):
  """PaygenPayloadLib tests base class."""

  def __init__(self, test_case_names):
    mox.MoxTestBase.__init__(self, test_case_names)
    self.tempdir = ''

    self.old_image = gspaths.Image(
        channel='dev-channel',
        board='x86-alex',
        version='1620.0.0',
        key='mp-v3',
        uri=('gs://chromeos-releases-test/dev-channel/x86-alex/1620.0.0/'
             'chromeos_1620.0.0_x86-alex_recovery_dev-channel_mp-v3.bin'))

    self.new_image = gspaths.Image(
        channel='dev-channel',
        board='x86-alex',
        version='4171.0.0',
        key='mp-v3',
        uri=('gs://chromeos-releases-test/dev-channel/x86-alex/4171.0.0/'
             'chromeos_4171.0.0_x86-alex_recovery_dev-channel_mp-v3.bin'))

    self.new_nplusone_image = gspaths.Image(
        channel='dev-channel',
        board='x86-alex',
        version='4171.0.0',
        key='mp-v3',
        image_channel='nplusone-channel',
        image_version='4171.0.1',
        uri=('gs://chromeos-releases-test/dev-channel/x86-alex/4171.0.0/'
             'chromeos_4171.0.1_x86-alex_recovery_nplusone-channel_mp-v3.bin'))

    self.full_payload = gspaths.Payload(tgt_image=self.old_image,
                                        src_image=None,
                                        uri='gs://full_old_foo/boo')

    self.delta_payload = gspaths.Payload(tgt_image=self.new_image,
                                         src_image=self.old_image,
                                         uri='gs://delta_new_old/boo')

    self.nplusone_payload = gspaths.Payload(tgt_image=self.new_nplusone_image,
                                            src_image=self.new_image,
                                            uri='gs://delta_npo_new/boo')

  @classmethod
  def setUpClass(cls):
    cls.cache_dir = tempfile.mkdtemp(prefix='crostools-unittest-cache')
    cls.cache = download_cache.DownloadCache(cls.cache_dir)

  @classmethod
  def tearDownClass(cls):
    cls.cache = None
    shutil.rmtree(cls.cache_dir)


class PaygenPayloadLibBasicTest(PaygenPayloadLibTest):
  """PaygenPayloadLib basic (and quick) testing."""

  def _GetStdGenerator(self, work_dir=None, payload=None, sign=True,
                       au_generator_uri_override=None):
    """Helper function to create a standardized PayloadGenerator."""
    if payload is None:
      payload = self.full_payload

    if work_dir is None:
      work_dir = self.tempdir

    return paygen_payload_lib._PaygenPayload(
        payload=payload,
        cache=self.cache,
        work_dir=work_dir,
        sign=sign,
        verify=False,
        au_generator_uri_override=au_generator_uri_override)

  def testWorkingDirNames(self):
    """Make sure that some of the files we create have the expected names."""
    gen = self._GetStdGenerator(work_dir='/foo')

    self.assertEqual(gen.generator_dir, '/foo/au-generator')
    self.assertEqual(gen.src_image_file, '/foo/src_image.bin')
    self.assertEqual(gen.tgt_image_file, '/foo/tgt_image.bin')
    self.assertEqual(gen.payload_file, '/foo/delta.bin')
    self.assertEqual(gen.delta_log_file, '/foo/delta.log')

    # Siged image specific values.
    self.assertEqual(gen.signed_payload_file, '/foo/delta.bin.signed')
    self.assertEqual(gen.metadata_signature_file,
                     '/foo/delta.bin.signed.metadata-signature')

  def testUriManipulators(self):
    """Validate _MetadataUri."""
    gen = self._GetStdGenerator(work_dir='/foo')

    self.assertEqual(gen._MetadataUri('/foo/bar'),
                     '/foo/bar.metadata-signature')
    self.assertEqual(gen._MetadataUri('gs://foo/bar'),
                     'gs://foo/bar.metadata-signature')

    self.assertEqual(gen._DeltaLogsUri('/foo/bar'),
                     '/foo/bar.log')
    self.assertEqual(gen._DeltaLogsUri('gs://foo/bar'),
                     'gs://foo/bar.log')

  @osutils.TempDirDecorator
  def testGeneratorUri(self):
    """Validate that we can correctly decide which au-generator.zip to use."""

    default_uri = paygen_payload_lib._PaygenPayload.MINIMUM_GENERATOR_URI

    future_uri = ('gs://chromeos-releases/dev-channel/x86-alex/100000.0.0/'
                  'au-generator.zip')

    past_image = gspaths.Image(
        channel='dev-channel',
        board='x86-alex',
        version='1.0.0',
        key='mp-v3',
        uri=('gs://past_image/boo'))

    future_image = gspaths.Image(
        channel='dev-channel',
        board='x86-alex',
        version='100000.0.0',
        key='mp-v3',
        uri=('gs://future_image/boo'))

    past_full_payload = gspaths.Payload(tgt_image=past_image,
                                        src_image=None,
                                        uri='gs://past_full/boo')

    future_full_payload = gspaths.Payload(tgt_image=future_image,
                                          src_image=None,
                                          uri='gs://future_full/boo')

    past_delta_payload = gspaths.Payload(tgt_image=future_image,
                                         src_image=past_image,
                                         uri='gs://past_delta/boo')

    future_delta_payload = gspaths.Payload(tgt_image=future_image,
                                           src_image=future_image,
                                           uri='gs://future_delta/boo')

    # default_uri because it's a Full.
    gen = self._GetStdGenerator(payload=past_full_payload)
    self.assertEqual(gen._GeneratorUri(), default_uri)

    # default_uri because it's a Full.
    gen = self._GetStdGenerator(payload=future_full_payload)
    self.assertEqual(gen._GeneratorUri(), default_uri)

    # default_uri because it's from an old version.
    gen = self._GetStdGenerator(payload=past_delta_payload)
    self.assertEqual(gen._GeneratorUri(), default_uri)

    # future_uri because it's from an new version.
    gen = self._GetStdGenerator(payload=future_delta_payload)
    self.assertEqual(gen._GeneratorUri(), future_uri)

    # Ensure the the debug argument to override our standard logic works.
    override = 'file://au-foo.zip'
    gen = self._GetStdGenerator(payload=past_full_payload,
                                au_generator_uri_override=override)
    self.assertEqual(gen._GeneratorUri(), override)

    gen = self._GetStdGenerator(payload=future_delta_payload,
                                au_generator_uri_override=override)
    self.assertEqual(gen._GeneratorUri(), override)


  @osutils.TempDirDecorator
  def testPrepareGenerator(self):
    """Validate that we can download an unzip a generator artifact."""
    gen = self._GetStdGenerator()
    gen._PrepareGenerator()

    # Ensure that the expected executables in the au-generator are available.
    expected = os.path.join(gen.generator_dir, 'convert_recovery_to_ssd.sh')
    self.assertTrue(os.path.exists(expected))

    expected = os.path.join(gen.generator_dir, 'cros_generate_update_payload')
    self.assertTrue(os.path.exists(expected))

    expected = os.path.join(gen.generator_dir, 'delta_generator')
    self.assertTrue(os.path.exists(expected))

  def testRunGeneratorCmd(self):
    """Test the specialized command to run programs from au-generate.zip."""
    test_cmd = ['cmd', 'bar', 'jo nes']
    expected_cmd = ['/foo/au-generator/cmd', 'bar', 'jo nes']
    original_environ = os.environ.copy()
    gen = self._GetStdGenerator(work_dir='/foo')

    self.mox.StubOutWithMock(cros_build_lib, 'RunCommand')

    mock_result = cros_build_lib.CommandResult()
    mock_result.output = 'foo output'

    # Set up the test replay script.
    cros_build_lib.RunCommand(
        expected_cmd, cwd='/foo/au-generator',
        redirect_stdout=True,
        combine_stdout_stderr=True,
        error_code_ok=True,
        extra_env=mox.IgnoreArg()).AndReturn(mock_result)

    # Run the test verification.
    self.mox.ReplayAll()
    self.assertEqual(gen._RunGeneratorCmd(test_cmd),
                     'foo output')

    # Demonstrate that the PATH was restored.
    self.assertEqual(os.environ, original_environ)

  def testBuildArg(self):
    """Make sure the function semantics is satisfied."""
    gen = self._GetStdGenerator(work_dir='/work')
    test_dict = {'foo': 'bar'}

    # Value present.
    self.assertEqual(gen._BuildArg('--foo', test_dict, 'foo'),
                     ['--foo', 'bar'])
    self.assertEqual(gen._BuildArg(None, test_dict, 'foo'),
                     ['bar'])

    # Value present, default has no impact.
    self.assertEqual(gen._BuildArg('--foo', test_dict, 'foo', default='baz'),
                     ['--foo', 'bar'])

    # Value missing, default kicking in.
    self.assertEqual(gen._BuildArg('--foo2', test_dict, 'foo2', default='baz'),
                     ['--foo2', 'baz'])

  def _DoPrepareImageTest(self, image_type):
    """Test _PrepareImage via mox."""
    download_uri = 'gs://bucket/foo/image.bin'
    image_file = '/work/image.bin'
    test_work_dir = tempfile.gettempdir()  # for testing purposes
    gen = self._GetStdGenerator(work_dir=test_work_dir)

    if image_type == 'Image':
      image_obj = gspaths.Image(
          channel='dev-channel',
          board='x86-alex',
          version='4171.0.0',
          key='mp-v3',
          uri=download_uri)
      test_extract_file = None
      test_is_recovery = True
    elif image_type == 'UnsignedImageArchive':
      image_obj = gspaths.UnsignedImageArchive(
          channel='dev-channel',
          board='x86-alex',
          version='4171.0.0',
          image_type='test',
          uri=download_uri)
      test_extract_file = paygen_payload_lib._PaygenPayload.TEST_IMAGE_NAME
      test_is_recovery = False
    else:
      raise ValueError('invalid image type descriptor (%s)' % image_type)

    # Stub out and record the expected function calls.
    self.mox.StubOutWithMock(download_cache.DownloadCache,
                             'GetFileCopy')
    if test_extract_file:
      download_file = mox.IsA(str)
    else:
      download_file = image_file
    self.cache.GetFileCopy(download_uri, download_file)

    if test_extract_file:
      self.mox.StubOutWithMock(cros_build_lib, 'RunCommand')
      cros_build_lib.RunCommand(['tar', '-xJf', download_file,
                                 test_extract_file], cwd=test_work_dir)
      self.mox.StubOutWithMock(shutil, 'move')
      shutil.move(os.path.join(test_work_dir, test_extract_file), image_file)

    if test_is_recovery:
      self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                               '_RunGeneratorCmd')
      gen._RunGeneratorCmd(['convert_recovery_to_ssd.sh',
                            image_file, '--force',
                            '--cgpt=%s/au-generator/cgpt' % test_work_dir])

    # Run the test.
    self.mox.ReplayAll()
    gen._PrepareImage(image_obj, image_file)

  def testPrepareImageNormal(self):
    """Test preparing a normal image."""
    self._DoPrepareImageTest('Image')

  def testPrepareImageTest(self):
    """Test preparing a test image."""
    self._DoPrepareImageTest('UnsignedImageArchive')

  def testGenerateUnsignedPayloadFull(self):
    """Test _GenerateUnsignedPayload with full payload."""
    gen = self._GetStdGenerator(payload=self.full_payload, work_dir='/work')

    # Stub out the required functions.
    self.mox.StubOutWithMock(gen, '_RunGeneratorCmd')
    self.mox.StubOutWithMock(gen, '_StoreDeltaLog')

    # Record the expected function calls.
    cmd = ['cros_generate_update_payload',
           '--outside_chroot',
           '--output', gen.payload_file,
           '--image', gen.tgt_image_file,
           '--channel', 'dev-channel',
           '--board', 'x86-alex',
           '--version', '1620.0.0',
           '--key', 'mp-v3',
           '--build_channel', 'dev-channel',
           '--build_version', '1620.0.0',
           ]
    gen._RunGeneratorCmd(cmd).AndReturn('log contents')
    gen._StoreDeltaLog('log contents')

    # Run the test.
    self.mox.ReplayAll()
    gen._GenerateUnsignedPayload()

  def testGenerateUnsignedPayloadDelta(self):
    """Test _GenerateUnsignedPayload with delta payload."""
    gen = self._GetStdGenerator(payload=self.delta_payload, work_dir='/work')

    # Stub out the required functions.
    self.mox.StubOutWithMock(gen, '_RunGeneratorCmd')
    self.mox.StubOutWithMock(gen, '_StoreDeltaLog')

    # Record the expected function calls.
    cmd = ['cros_generate_update_payload',
           '--outside_chroot',
           '--output', gen.payload_file,
           '--image', gen.tgt_image_file,
           '--channel', 'dev-channel',
           '--board', 'x86-alex',
           '--version', '4171.0.0',
           '--key', 'mp-v3',
           '--build_channel', 'dev-channel',
           '--build_version', '4171.0.0',
           '--src_image', gen.src_image_file,
           '--src_channel', 'dev-channel',
           '--src_board', 'x86-alex',
           '--src_version', '1620.0.0',
           '--src_key', 'mp-v3',
           '--src_build_channel', 'dev-channel',
           '--src_build_version', '1620.0.0',
           ]
    gen._RunGeneratorCmd(cmd).AndReturn('log contents')
    gen._StoreDeltaLog('log contents')

    # Run the test.
    self.mox.ReplayAll()
    gen._GenerateUnsignedPayload()

  @osutils.TempDirDecorator
  def testGenPayloadHashes(self):
    """Test _GenPayloadHash via mox."""
    gen = self._GetStdGenerator()

    # Stub out the required functions.
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_RunGeneratorCmd')

    # Record the expected function calls.
    cmd = ['delta_generator',
           '-in_file', gen.payload_file,
           '-out_hash_file', mox.IsA(str),
           '-signature_size', '256']
    gen._RunGeneratorCmd(cmd)

    # Run the test.
    self.mox.ReplayAll()
    self.assertEqual(gen._GenPayloadHash(), '')

  @osutils.TempDirDecorator
  def testGenMetadataHashes(self):
    """Test _GenPayloadHash via mox."""
    gen = self._GetStdGenerator()

    # Stub out the required functions.
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_RunGeneratorCmd')

    # Record the expected function calls.
    cmd = ['delta_generator',
           '-in_file', gen.payload_file,
           '-out_metadata_hash_file', mox.IsA(str),
           '-signature_size', '256']
    gen._RunGeneratorCmd(cmd)

    # Run the test.
    self.mox.ReplayAll()
    self.assertEqual(gen._GenMetadataHash(), '')

  def testSignHashes(self):
    """Test _SignHashes via mox."""
    hashes = ('foo', 'bar')
    signatures = (('0'*256,), ('1'*256,))

    gen = self._GetStdGenerator(work_dir='/work')

    # Stub out the required functions.
    self.mox.StubOutWithMock(
        signer_payloads_client.SignerPayloadsClientGoogleStorage,
        'GetHashSignatures')

    gen.signer.GetHashSignatures(
        hashes,
        keysets=gen.PAYLOAD_SIGNATURE_KEYSETS).AndReturn(signatures)

    # Run the test.
    self.mox.ReplayAll()
    self.assertEqual(gen._SignHashes(hashes),
                     signatures)

  @osutils.TempDirDecorator
  def testInsertPayloadSignatures(self):
    """Test inserting payload signatures."""
    gen = self._GetStdGenerator(payload=self.delta_payload)
    payload_signatures = ('0'*256,)

    # Stub out the required functions.
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_RunGeneratorCmd')

    # Record the expected function calls.
    cmd = ['delta_generator',
           '-in_file', gen.payload_file,
           '-signature_file', mox.IsA(str),
           '-out_file', gen.signed_payload_file]
    gen._RunGeneratorCmd(cmd)

    # Run the test.
    self.mox.ReplayAll()
    gen._InsertPayloadSignatures(payload_signatures)

  @osutils.TempDirDecorator
  def testStoreMetadataSignatures(self):
    """Test how we store metadata signatures."""
    gen = self._GetStdGenerator(payload=self.delta_payload)
    metadata_signatures = ('1'*256,)
    encoded_metadata_signature = (
        'MTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMT'
        'ExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEx'
        'MTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMT'
        'ExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEx'
        'MTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMT'
        'ExMTExMTExMQ==')

    gen._StoreMetadataSignatures(metadata_signatures)

    with file(gen.metadata_signature_file, 'rb') as f:
      self.assertEqual(f.read(), encoded_metadata_signature)

  def testSignPayload(self):
    """Test the overall payload signature process via mox."""
    payload_hash = 'payload_hash'
    metadata_hash = 'metadata_hash'
    payload_sigs = ('payload_sig',)
    metadata_sigs = ('metadata_sig',)

    gen = self._GetStdGenerator(payload=self.delta_payload, work_dir='/work')

    # Set up stubs.
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_GenPayloadHash')
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_GenMetadataHash')
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_SignHashes')
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_InsertPayloadSignatures')
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_StoreMetadataSignatures')

    # Record expected calls.
    gen._GenPayloadHash().AndReturn(payload_hash)
    gen._GenMetadataHash().AndReturn(metadata_hash)
    gen._SignHashes([payload_hash, metadata_hash]).AndReturn(
        (payload_sigs,metadata_sigs))
    gen._InsertPayloadSignatures(payload_sigs)
    gen._StoreMetadataSignatures(metadata_sigs)

    # Run the test.
    self.mox.ReplayAll()
    gen._SignPayload()

  def testCreateSignedDelta(self):
    """Test the overall payload generation process via mox."""
    payload = self.delta_payload
    gen = self._GetStdGenerator(payload=payload, work_dir='/work')

    # Set up stubs.
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_PrepareGenerator')
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_PrepareImage')
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_GenerateUnsignedPayload')
    self.mox.StubOutWithMock(paygen_payload_lib._PaygenPayload,
                             '_SignPayload')

    # Record expected calls.
    gen._PrepareGenerator()
    gen._PrepareImage(payload.tgt_image, gen.tgt_image_file)
    gen._PrepareImage(payload.src_image, gen.src_image_file)
    gen._GenerateUnsignedPayload()
    gen._SignPayload()

    # Run the test.
    self.mox.ReplayAll()
    gen._Create()

  def testUploadResults(self):
    """Test the overall payload generation process via mox."""
    gen_sign = self._GetStdGenerator(work_dir='/work', sign=True)
    gen_nosign = self._GetStdGenerator(work_dir='/work', sign=False)

    # Set up stubs.
    self.mox.StubOutWithMock(urilib, 'Copy')
    self.mox.StubOutWithMock(urilib, 'ListFiles')

    # Record signed calls.
    urilib.Copy('/work/delta.bin.signed',
                'gs://full_old_foo/boo')
    urilib.Copy('/work/delta.bin.signed.metadata-signature',
                'gs://full_old_foo/boo.metadata-signature')
    urilib.Copy('/work/delta.log',
                'gs://full_old_foo/boo.log')

    # Record unsigned calls.
    urilib.Copy('/work/delta.bin',
                'gs://full_old_foo/boo')
    urilib.Copy('/work/delta.log',
                'gs://full_old_foo/boo.log')

    # Run the test.
    self.mox.ReplayAll()
    gen_sign._UploadResults()
    gen_nosign._UploadResults()

  def testDefaultPayloadUri(self):
    """Test paygen_payload_lib.DefaultPayloadUri."""

    # Test a Full Payload
    result = paygen_payload_lib.DefaultPayloadUri(self.full_payload,
                                                  random_str='abc123')
    self.assertEqual(
        result,
        'gs://chromeos-releases/dev-channel/x86-alex/1620.0.0/payloads/'
        'chromeos_1620.0.0_x86-alex_dev-channel_full_mp-v3.bin-abc123.signed')

    # Test a Delta Payload
    result = paygen_payload_lib.DefaultPayloadUri(self.delta_payload,
                                                  random_str='abc123')
    self.assertEqual(
        result,
        'gs://chromeos-releases/dev-channel/x86-alex/4171.0.0/payloads/'
        'chromeos_1620.0.0-4171.0.0_x86-alex_dev-channel_delta_mp-v3.bin-'
        'abc123.signed')

    # Test an N Plus One Delta Payload
    result = paygen_payload_lib.DefaultPayloadUri(self.nplusone_payload,
                                                  random_str='abc123')
    self.assertEqual(
        result,
        'gs://chromeos-releases/dev-channel/x86-alex/4171.0.0/payloads/'
        'chromeos_4171.0.0-4171.0.1_x86-alex_nplusone-channel_delta_mp-v3.bin-'
        'abc123.signed')

    # Test changing channel, board, and keys
    src_image = gspaths.Image(
        channel='dev-channel',
        board='x86-alex',
        version='3588.0.0',
        key='premp')
    tgt_image = gspaths.Image(
        channel='stable-channel',
        board='x86-alex-he',
        version='3590.0.0',
        key='mp-v3')
    payload = gspaths.Payload(src_image=src_image, tgt_image=tgt_image)

    result = paygen_payload_lib.DefaultPayloadUri(payload,
                                                  random_str='abc123')
    self.assertEqual(
        result,
        'gs://chromeos-releases/stable-channel/x86-alex-he/3590.0.0/payloads/'
        'chromeos_3588.0.0-3590.0.0_x86-alex-he_stable-channel_delta_mp-v3.bin-'
        'abc123.signed')

  def testFillInPayloadUri(self):
    """Test filling in the payload URI of a gspaths.Payload object."""
    # Assert that it doesn't change if already present.
    pre_uri = self.full_payload.uri
    paygen_payload_lib.FillInPayloadUri(self.full_payload,
                                        random_str='abc123')
    self.assertEqual(self.full_payload.uri,
                     pre_uri)

    # Test that it does change if not present.
    payload = gspaths.Payload(tgt_image=self.old_image)
    paygen_payload_lib.FillInPayloadUri(payload,
                                        random_str='abc123')
    self.assertEqual(
        payload.uri,
        'gs://chromeos-releases/dev-channel/x86-alex/1620.0.0/payloads/'
        'chromeos_1620.0.0_x86-alex_dev-channel_full_mp-v3.bin-abc123.signed')

  def testFindExistingPayloads(self):
    """Test finding already existing payloads."""
    self.mox.StubOutWithMock(urilib, 'ListFiles')

    # Set up the test replay script.
    urilib.ListFiles('gs://chromeos-releases/dev-channel/x86-alex/1620.0.0/'
                     'payloads/chromeos_1620.0.0_x86-alex_dev-channel_full_'
                     'mp-v3.bin-*.signed').AndReturn(['foo_result'])

    # Run the test verification.
    self.mox.ReplayAll()

    self.assertEqual(
        paygen_payload_lib.FindExistingPayloads(self.full_payload),
        ['foo_result'])


  def testFindCacheDir(self):
    """Test calculating the location of the cache directory."""
    # Test default dir in /tmp.
    result = paygen_payload_lib.FindCacheDir()
    self.assertEqual(result, '/usr/local/google/payloads')

    # Test in specified dir.
    result = paygen_payload_lib.FindCacheDir('/foo')
    self.assertEqual(result, '/foo/cache')


class PaygenPayloadLibEndToEndTest(PaygenPayloadLibTest):
  """PaygenPayloadLib end-to-end testing."""

  def _EndToEndIntegrationTest(self, tgt_image, src_image, sign):
    """Helper test function for validating end to end payload generation."""
    output_uri = os.path.join(self.tempdir, 'expected_payload_out')
    output_metadata_uri = output_uri + '.metadata-signature'

    payload = gspaths.Payload(tgt_image=tgt_image,
                              src_image=src_image,
                              uri=output_uri)

    paygen_payload_lib.CreateAndUploadPayload(
        payload=payload,
        cache=self.cache,
        work_dir=self.tempdir,
        sign=sign)

    self.assertTrue(os.path.exists(output_uri))
    self.assertEqual(os.path.exists(output_metadata_uri), sign)

  @cros_test_lib.NetworkTest()
  @osutils.TempDirDecorator
  def testEndToEndIntegrationFull(self):
    """Integration test to generate a full payload for old_image."""
    self._EndToEndIntegrationTest(self.old_image, None, sign=True)

  @cros_test_lib.NetworkTest()
  @osutils.TempDirDecorator
  def testEndToEndIntegrationDelta(self):
    """Integration test to generate a delta payload for new_image -> NPO."""
    self._EndToEndIntegrationTest(self.new_nplusone_image,
                                  self.new_image,
                                  sign=False)


if __name__ == '__main__':
  cros_test_lib.main()
