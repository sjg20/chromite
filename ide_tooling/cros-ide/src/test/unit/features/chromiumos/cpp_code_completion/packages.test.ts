// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as assert from 'assert';
import * as path from 'path';
import {Packages} from '../../../../../features/chromiumos/cpp_code_completion/packages';
import * as services from '../../../../../services';
import * as testing from '../../../../testing';

describe('Packages', () => {
  const tempDir = testing.tempDir();

  it('returns package information using hard-coded mapping', async () => {
    await testing.buildFakeChroot(tempDir.path);

    const packages = new Packages(
      services.chromiumos.ChrootService.maybeCreate(tempDir.path, false)!
    );
    // A file should exists in the filepath to get its absolute path.
    await testing.putFiles(tempDir.path, {
      'src/platform2/cros-disks/foo.cc': 'x',
      'src/platform2/unknown_dir/foo.cc': 'x',
    });

    assert.deepStrictEqual(
      await packages.fromFilepath(
        path.join(tempDir.path, 'src/platform2/cros-disks/foo.cc')
      ),
      {
        sourceDir: 'src/platform2/cros-disks',
        atom: 'chromeos-base/cros-disks',
      },
      'success'
    );

    assert.deepStrictEqual(
      await packages.fromFilepath(
        path.join(tempDir.path, 'src/platform2/unknown_dir/foo.cc')
      ),
      null,
      'unknown'
    );

    assert.deepStrictEqual(
      await packages.fromFilepath(path.join(tempDir.path, 'not_exist')),
      null,
      'not exist'
    );
  });

  it('returns package information', async () => {
    await testing.buildFakeChroot(tempDir.path);

    const packages = new Packages(
      services.chromiumos.ChrootService.maybeCreate(tempDir.path, false)!,
      true
    );
    // A file should exists in the filepath to get its absolute path.
    await testing.putFiles(tempDir.path, {
      'src/platform2/foo/foo.cc': 'x',
      'src/third_party/chromiumos-overlay/chromeos-base/foo/foo-9999.ebuild': `inherit platform
PLATFORM_SUBDIR="foo"
`,
      'src/platform2/unknown_dir/foo.cc': 'x',
    });

    assert.deepStrictEqual(
      await packages.fromFilepath(
        path.join(tempDir.path, 'src/platform2/foo/foo.cc')
      ),
      {
        sourceDir: 'src/platform2/foo',
        atom: 'chromeos-base/foo',
      },
      'success'
    );

    assert.deepStrictEqual(
      await packages.fromFilepath(
        path.join(tempDir.path, 'src/platform2/unknown_dir/foo.cc')
      ),
      null,
      'unknown'
    );

    assert.deepStrictEqual(
      await packages.fromFilepath(path.join(tempDir.path, 'not_exist')),
      null,
      'not exist'
    );
  });
});