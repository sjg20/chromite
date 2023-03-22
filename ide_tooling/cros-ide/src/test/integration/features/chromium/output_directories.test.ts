// Copyright 2023 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as fs from 'fs/promises';
import * as path from 'path';
import {
  DirNode,
  LinkNode,
  OutputDirectoriesDataProvider,
} from '../../../../features/chromium/output_directories';
import * as testing from '../../../testing';
import * as fakes from '../../../testing/fakes';

describe('OutputDirectoriesDataProvider', () => {
  const tempDir = testing.tempDir();
  const {fakeExec} = testing.installFakeExec();

  beforeEach(() => {
    // By default, pretend that `gn args` errors.
    fakeExec.on(
      'gn',
      testing.prefixMatch(['args'], async (args, options) => {
        expect(options.cwd).toBe(tempDir.path);
        return {exitStatus: 1, stderr: '', stdout: ''};
      })
    );
  });

  it('ignores files that are named like output directories', async () => {
    await fs.writeFile(path.join(tempDir.path, 'out'), 'test1');
    await fs.writeFile(path.join(tempDir.path, 'out_hatch'), 'test2');

    const dataProvider = new OutputDirectoriesDataProvider(
      {subscriptions: []},
      new fakes.VoidOutputChannel(),
      tempDir.path
    );

    const nodes = await dataProvider.getChildren();
    expect(nodes).toEqual([]);
  });

  it('ignores output directories that are just one level deep', async () => {
    await fs.mkdir(path.join(tempDir.path, 'out'));

    const dataProvider = new OutputDirectoriesDataProvider(
      {subscriptions: []},
      new fakes.VoidOutputChannel(),
      tempDir.path
    );

    const nodes = await dataProvider.getChildren();
    expect(nodes).toEqual([]);
  });

  it('ignores output directories that contain additional files on the first level', async () => {
    // `out/blah` is a valid output directory in theory, except that there are also files in `out/`,
    // which no longer makes `out/blah` a valid output directory.
    await fs.mkdir(path.join(tempDir.path, 'out'));
    await fs.mkdir(path.join(tempDir.path, 'out/blah'));
    await fs.writeFile(path.join(tempDir.path, 'out/args.gn'), 'foo');

    const dataProvider = new OutputDirectoriesDataProvider(
      {subscriptions: []},
      new fakes.VoidOutputChannel(),
      tempDir.path
    );

    const nodes = await dataProvider.getChildren();
    expect(nodes).toEqual([]);
  });

  it('finds output directories', async () => {
    await fs.mkdir(path.join(tempDir.path, 'random-non-out-dir'));
    await fs.mkdir(path.join(tempDir.path, 'non-out-dir_out'));
    await fs.mkdir(path.join(tempDir.path, 'out'));
    await fs.mkdir(path.join(tempDir.path, 'out/dir2'));
    await fs.mkdir(path.join(tempDir.path, 'out_hatch'));
    await fs.mkdir(path.join(tempDir.path, 'out/dir1'));
    await fs.mkdir(path.join(tempDir.path, 'out_hatch/dir4'));
    await fs.mkdir(path.join(tempDir.path, 'out_hatch/dir3'));

    const dataProvider = new OutputDirectoriesDataProvider(
      {subscriptions: []},
      new fakes.VoidOutputChannel(),
      tempDir.path
    );

    const nodes = await dataProvider.getChildren();
    await dataProvider.getNodeCacheForTesting()!.gnArgsPromise;
    // This also tests that the nodes are sorted.
    expect(nodes).toEqual([
      new DirNode('out_hatch/dir3', false, 'error'),
      new DirNode('out_hatch/dir4', false, 'error'),
      new DirNode('out/dir1', false, 'error'),
      new DirNode('out/dir2', false, 'error'),
    ]);
  });

  it('finds symlinks', async () => {
    await fs.mkdir(path.join(tempDir.path, 'out'));
    await fs.mkdir(path.join(tempDir.path, 'out/dir2'));
    await fs.mkdir(path.join(tempDir.path, 'out_hatch'));
    await fs.mkdir(path.join(tempDir.path, 'out_hatch/dir3'));
    await fs.symlink(
      path.join(tempDir.path, 'out/dir2'),
      path.join(tempDir.path, 'out/current_link')
    );
    await fs.symlink(
      path.join(tempDir.path, 'out_hatch/dir3'),
      path.join(tempDir.path, 'out_hatch/a_link')
    );
    await fs.symlink(
      '/this/path/does/not/exist',
      path.join(tempDir.path, 'out_hatch/non_existing_link')
    );
    await fs.symlink(
      tempDir.path,
      path.join(tempDir.path, 'out_hatch/outside_link')
    );

    const dataProvider = new OutputDirectoriesDataProvider(
      {subscriptions: []},
      new fakes.VoidOutputChannel(),
      tempDir.path
    );

    const nodes = await dataProvider.getChildren();
    await dataProvider.getNodeCacheForTesting()!.gnArgsPromise;
    // This also tests that the nodes are sorted.
    expect(nodes).toEqual([
      new LinkNode('out_hatch/a_link', 'out_hatch/dir3'),
      new LinkNode('out_hatch/outside_link', null),
      new LinkNode('out/current_link', 'out/dir2'),
      new DirNode('out_hatch/dir3', false, 'error'),
      new DirNode('out/dir2', true, 'error'),
    ]);
  });

  it('can refresh output directories', async () => {
    await fs.mkdir(path.join(tempDir.path, 'out'));
    await fs.mkdir(path.join(tempDir.path, 'out/dir1'));

    const dataProvider = new OutputDirectoriesDataProvider(
      {subscriptions: []},
      new fakes.VoidOutputChannel(),
      tempDir.path
    );

    let nodes = await dataProvider.getChildren();
    await dataProvider.getNodeCacheForTesting()!.gnArgsPromise;
    expect(nodes).toEqual([new DirNode('out/dir1', false, 'error')]);

    await fs.mkdir(path.join(tempDir.path, 'out/dir2'));
    dataProvider.refresh();

    nodes = await dataProvider.getChildren();
    await dataProvider.getNodeCacheForTesting()!.gnArgsPromise;
    // This also tests that the nodes are sorted.
    expect(nodes).toEqual([
      new DirNode('out/dir1', false, 'error'),
      new DirNode('out/dir2', false, 'error'),
    ]);
  });

  [true, false, 'unset'].forEach(useGoma => {
    it(`queries GN args correctly when GOMA is ${useGoma}`, async () => {
      await fs.mkdir(path.join(tempDir.path, 'out'));
      await fs.mkdir(path.join(tempDir.path, 'out/dir1'));

      fakeExec.handlers.set('gn', []);
      fakeExec.on(
        'gn',
        testing.exactMatch(
          [
            'args',
            path.join(tempDir.path, 'out', 'dir1'),
            '--list',
            '--short',
            '--overrides-only',
            '--json',
          ],
          async options => {
            expect(options.cwd).toBe(tempDir.path);
            switch (useGoma) {
              case true:
                return JSON.stringify([
                  {name: 'foo_bar', current: {value: 'true'}},
                  {name: 'use_goma', current: {value: 'true'}},
                ]);
              case false:
                return JSON.stringify([
                  {name: 'foo_bar', current: {value: 'true'}},
                  {name: 'use_goma', current: {value: 'false'}},
                ]);
              case 'unset':
                return JSON.stringify([
                  {name: 'foo_bar', current: {value: 'false'}},
                ]);
              default:
                throw new Error('not reached');
            }
          }
        )
      );

      const dataProvider = new OutputDirectoriesDataProvider(
        {subscriptions: []},
        new fakes.VoidOutputChannel(),
        tempDir.path
      );

      const nodes = await dataProvider.getChildren();
      await dataProvider.getNodeCacheForTesting()!.gnArgsPromise;
      expect(nodes).toEqual([
        new DirNode('out/dir1', false, {use_goma: useGoma === true}),
      ]);
    });
  });
});
