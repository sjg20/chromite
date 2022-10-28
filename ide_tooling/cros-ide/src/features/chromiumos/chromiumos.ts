// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as cipd from '../../common/cipd';
import * as services from '../../services';
import * as config from '../../services/config';
import * as bgTaskStatus from '../../ui/bg_task_status';
import * as metrics from '../metrics/metrics';
import * as boardsPackages from './boards_packages';
import {Coverage} from './coverage';
import * as cppCodeCompletion from './cpp_code_completion';
import * as deviceManagement from './device_management';
import {NewFileTemplate} from './new_file_template';
import {Platform2Gtest} from './platform2_gtest';
import * as platformEc from './platform_ec';
import * as targetBoard from './target_board';
import {Tast} from './tast';
import * as tricium from './tricium';

/**
 * Extension context value provided to this class. We omit subscriptions here
 * because the lifetime of the context might be longer than this class and thus
 * we should not put disposables created under this class to
 * context.subscriptions.
 */
type Context = Omit<vscode.ExtensionContext, 'subscriptions'>;

/**
 * The root class of all the ChromiumOS features.
 *
 * This class should be instantiated only when the workspace contains chromiumos source code.
 */
export class Chromiumos implements vscode.Disposable {
  private readonly subscriptions: vscode.Disposable[] = [
    new NewFileTemplate(this.root),
  ];
  dispose() {
    vscode.Disposable.from(...this.subscriptions.reverse()).dispose();
  }

  /**
   * @param context The context of the extension itself.
   * @param root Absolute path to the chormiumos root directory.
   */
  constructor(
    context: Context,
    private readonly root: string,
    private readonly statusManager: bgTaskStatus.StatusManager,
    private readonly cipdRepository: cipd.CipdRepository
  ) {
    void (async () => {
      try {
        // The method shouldn't throw an error as its API contract.
        await this.activate(context);
      } catch (_e) {
        metrics.send({
          category: 'error',
          group: 'misc',
          description: `failed to activte ${this.featureName}`,
        });
      }
    })();
  }

  // feature name being activated to include in error message
  private featureName = 'Chromiumos';

  // TODO(oka): Cancel ongoing activation when this class is disposed.
  private async activate(context: Context) {
    const ephemeralContext = newContext(context, this.subscriptions);

    const gitDirsWatcher = new services.GitDirsWatcher(this.root);

    // Spellchecker is a corner case. It requires access to CrOS source
    // directory, which is detected by the presence .repo subdirectory, but
    // doesn't need chroot subdirectory to exist.
    if (config.spellchecker.get()) {
      this.featureName = 'spellchecker';
      const textEditorsWatcher = new services.TextEditorsWatcher();
      await tricium.activateSpellchecker(
        ephemeralContext,
        this.statusManager,
        this.root,
        this.cipdRepository,
        textEditorsWatcher,
        gitDirsWatcher
      );
    }

    const chrootService = services.chromiumos.ChrootService.maybeCreate(
      this.root
    );

    if (chrootService) {
      this.featureName = 'cppCodeCompletion';
      cppCodeCompletion.activate(
        this.subscriptions,
        this.statusManager,
        chrootService
      );

      this.featureName = 'boardsPackages';
      await boardsPackages.activate(this.subscriptions, chrootService);

      this.featureName = 'deviceManagement';
      await deviceManagement.activate(
        ephemeralContext,
        this.statusManager,
        chrootService,
        this.cipdRepository
      );

      if (config.underDevelopment.testCoverage.get()) {
        this.featureName = 'testCoverage';
        new Coverage(chrootService, this.statusManager).activate(
          ephemeralContext
        );
      }

      if (config.underDevelopment.platformEc.get()) {
        this.featureName = 'platformEc';
        platformEc.activate(
          ephemeralContext,
          this.statusManager,
          chrootService
        );
      }

      this.featureName = 'targetBoard';
      targetBoard.activate(ephemeralContext, chrootService);

      if (config.underDevelopment.platform2GtestDebugging.get()) {
        this.subscriptions.push(new Platform2Gtest(this.root, chrootService));
      }

      if (config.underDevelopment.tast.get()) {
        this.subscriptions.push(new Tast());
      }
    }
  }
}

// We cannot use spread syntax for context (b:253964293)
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
