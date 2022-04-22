// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as assert from 'assert';
import {CompdbServiceImpl} from '../../../features/cpp_code_completion/compdb_service';
import {SpiedCompdbService} from './spied_compdb_service';

describe('Compdb service', () => {
  it('uses legacy service when instructed', async () => {
    const legacyService = new SpiedCompdbService();
    const compdbService = new CompdbServiceImpl(legacyService, () => true);
    await compdbService.generate('foo', {sourceDir: 'bar', atom: 'baz'});
    assert.deepStrictEqual(legacyService.requests, [
      {board: 'foo', packageInfo: {sourceDir: 'bar', atom: 'baz'}},
    ]);
  });
});
