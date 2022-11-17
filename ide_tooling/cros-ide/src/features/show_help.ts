// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as metrics from '../features/metrics/metrics';

export function activate(context: vscode.ExtensionContext) {
  const commandLink: [string, vscode.Uri][] = [
    [
      'cros-ide.showHelpForBoardsPackages',
      vscode.Uri.parse('http://go/cros-ide-doc-boards-pkgs'),
    ],
    [
      'cros-ide.showHelpForDevices',
      vscode.Uri.parse('http://go/cros-ide-doc-device-management'),
    ],
    [
      'cros-ide.showHelpForIdeStatus',
      vscode.Uri.parse('http://go/cros-ide-doc-ide-status'),
    ],
    // TODO(b:256974503): Add buttons in Problems for liners and in Comments for Gerrit.
  ];

  for (const [command, link] of commandLink) {
    context.subscriptions.push(
      vscode.commands.registerCommand(command, () => {
        void vscode.env.openExternal(link);
        metrics.send({
          category: 'interactive',
          group: 'misc',
          action: command,
        });
      })
    );
  }
}
