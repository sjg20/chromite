// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import {Chroot} from '../../common/common_util';
import {cleanState} from './clean_state';

export async function putFiles(dir: string, files: {[name: string]: string}) {
  for (const [name, content] of Object.entries(files)) {
    const filePath = path.join(dir, name);
    await fs.promises.mkdir(path.dirname(filePath), {recursive: true});
    await fs.promises.writeFile(path.join(dir, name), content);
  }
}

/**
 * Returns a state with the path to a temporary directory, installing an
 * afterEach hook to remove the directory.
 */
export function tempDir(): {path: string} {
  const state = cleanState(async () => {
    return {
      path: await fs.promises.mkdtemp(os.tmpdir() + '/'),
    };
  });
  afterEach(() => fs.promises.rm(state.path, {recursive: true}));
  return state;
}

/**
 * Builds fake chroot environment under tempDir, and returns the path to the
 * fake chroot (`${tempDir}/chroot`).
 */
export async function buildFakeChroot(tempDir: string): Promise<Chroot> {
  await putFiles(tempDir, {'chroot/etc/cros_chroot_version': '42'});
  return path.join(tempDir, 'chroot') as Chroot;
}