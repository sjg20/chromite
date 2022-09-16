// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as chroot from '../../services/chroot';
import * as bgTaskStatus from '../../ui/bg_task_status';
import * as statusBar from './status_bar';
import * as tasks from './tasks';

export const STATUS_TASK_NAME = 'Platform EC';
export const SHOW_LOG_COMMAND: vscode.Command = {
  command: 'cros-ide.showPlatformEcLog',
  title: 'Show Platform EC Log',
};

export function activate(
  context: vscode.ExtensionContext,
  statusManager: bgTaskStatus.StatusManager,
  chrootService: chroot.ChrootService
) {
  // We are using one output channel for all platform EC related tasks.
  // TODO(b:236389226): when servod is integrated, send its logs somewhere else
  const outputChannel = vscode.window.createOutputChannel(
    'CrOS IDE: Platform EC'
  );
  context.subscriptions.push(
    vscode.commands.registerCommand(SHOW_LOG_COMMAND.command, () =>
      outputChannel.show()
    )
  );

  // TODO(b:236389226): Make sure the features are available only if
  // we are in platform/ec or they are needed otherwise (for example, tasks.json).

  statusBar.activate(context);
  tasks.activate(context, statusManager, chrootService, outputChannel);
}
