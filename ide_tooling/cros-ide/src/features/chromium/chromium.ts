// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as path from 'path';
import * as bgTaskStatus from '../../ui/bg_task_status';
import * as config from '../../services/config';
import * as metrics from '../metrics/metrics';
import * as boilerplate from '../boilerplate';
import * as chromiumBuild from './chromium_build';
import * as outputDirectories from './output_directories';

/**
 * Extension context value provided to this class. We omit subscriptions here
 * because the lifetime of the context might be longer than this class and thus
 * we should not put disposables created under this class to
 * context.subscriptions.
 */
type Context = Omit<vscode.ExtensionContext, 'subscriptions'>;

/**
 * The root class of all the Chromium features.
 *
 * This class should be instantiated only when the workspace contains chromium source code.
 */
export class Chromium implements vscode.Disposable {
  private readonly subscriptions: vscode.Disposable[] = [
    this.boilerplateInserter.addBoilerplateGenerator(
      new boilerplate.ChromiumBoilerplateGenerator(path.join(this.root, 'src'))
    ),
  ];
  dispose() {
    vscode.Disposable.from(...this.subscriptions.reverse()).dispose();
  }

  /**
   * @param context The context of the extension itself.
   * @param root Absolute path to the chromium root directory.
   */
  constructor(
    context: Context,
    private readonly root: string,
    private readonly statusManager: bgTaskStatus.StatusManager,
    private readonly boilerplateInserter: boilerplate.BoilerplateInserter
  ) {
    void (async () => {
      try {
        // The method shouldn't throw an error as its API contract.
        await this.activate(context);
      } catch (e) {
        console.error('Failed to activate chromium features', e);
        metrics.send({
          category: 'error',
          group: 'misc',
          description: `failed to activte chromium feature ${this.featureName}`,
        });
      }
    })();
  }

  // feature name being activated to include in error message
  private featureName = 'Chromium';

  private async activate(context: Context) {
    const ephemeralContext = newContext(context, this.subscriptions);

    if (config.underDevelopment.chromiumBuild.get()) {
      this.featureName = 'chromiumBuild';
      chromiumBuild.activate(ephemeralContext, this.statusManager);
    }
    if (config.underDevelopment.chromiumOutputDirectories.get()) {
      this.featureName = 'chromiumOutputDirectories';
      outputDirectories.activate(
        ephemeralContext,
        this.statusManager,
        this.root
      );
    }
  }
}

// TODO(oka): The same function exists in chromiumos.ts. Move the function to a
// common place and share it.
function newContext(
  context: Context,
  subscriptions: vscode.Disposable[]
): vscode.ExtensionContext {
  return {
    environmentVariableCollection: context.environmentVariableCollection,
    extension: context.extension,
    extensionMode: context.extensionMode,
    extensionPath: context.extensionPath,
    extensionUri: context.extensionUri,
    globalState: context.globalState,
    globalStoragePath: context.globalStoragePath,
    globalStorageUri: context.globalStorageUri,
    logPath: context.logPath,
    logUri: context.logUri,
    secrets: context.secrets,
    storagePath: context.storagePath,
    storageUri: context.storageUri,
    subscriptions,
    workspaceState: context.workspaceState,
    asAbsolutePath: context.asAbsolutePath.bind(context),
  };
}
