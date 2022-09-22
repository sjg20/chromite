// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as os from 'os';
import * as path from 'path';
import * as process from 'process';
import * as vscode from 'vscode';
import * as config from '../services/config';
import * as commonUtil from './common_util';

const defaultInstallDir = path.join(os.homedir(), '.cache/cros-ide/cipd');

/**
 * Interacts with CIPD CLI client (http://go/luci-cipd).
 *
 * It manages a repository of locally installed CIPD binaries. Call ensure*()
 * to download and install a CIPD package (if one is missing or stale) and
 * get its file path.
 */
export class CipdRepository {
  private readonly cipdMutex = new commonUtil.Mutex();

  constructor(public readonly installDir = defaultInstallDir) {}

  private async ensurePackage(
    packageName: string,
    version: string,
    output: vscode.OutputChannel
  ): Promise<void> {
    // Expand PATH to <custom_setting>:$PATH:~/depot_tools.
    // This gives preference to the custom setting and fallback on a default.

    const depotToolsSetting = config.paths.depotTools.get();
    const originalPath = process.env['PATH'];
    const homeDepotTools = path.join(os.homedir(), 'depot_tools');

    const expandedPath: string[] = [];
    if (depotToolsSetting) {
      expandedPath.push(depotToolsSetting);
    }
    if (originalPath) {
      expandedPath.push(originalPath);
    }
    expandedPath.push(homeDepotTools);

    const env = {
      ...process.env,
      PATH: expandedPath.join(':'),
    };

    await this.cipdMutex.runExclusive(async () => {
      const result = await commonUtil.exec(
        'cipd',
        ['install', '-root', this.installDir, packageName, version],
        {
          logger: output,
          env,
        }
      );
      if (result instanceof Error) {
        throw result;
      }
    });
  }

  async ensureCrosfleet(output: vscode.OutputChannel): Promise<string> {
    await this.ensurePackage(
      'chromiumos/infra/crosfleet/${platform}',
      'prod',
      output
    );
    return path.join(this.installDir, 'crosfleet');
  }

  async ensureTriciumSpellchecker(
    output: vscode.OutputChannel
  ): Promise<string> {
    await this.ensurePackage(
      'infra/tricium/function/spellchecker',
      'live',
      output
    );
    return path.join(this.installDir, 'spellchecker');
  }
}
