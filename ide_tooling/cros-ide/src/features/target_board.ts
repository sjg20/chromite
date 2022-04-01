// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

/**
 * Manages the target board config.
 */

import * as vscode from 'vscode';
import * as ideUtil from '../ide_util';

const BOARD_CONFIG = 'cros-ide.board';

export function activate(context: vscode.ExtensionContext) {
  const boardStatusBarItem = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Left
  );
  boardStatusBarItem.command = 'cros-ide.selectBoard';

  context.subscriptions.push(
    vscode.workspace.onDidChangeConfiguration(
      (e: vscode.ConfigurationChangeEvent) => {
        if (e.affectsConfiguration(BOARD_CONFIG)) {
          updateBoardStatus(boardStatusBarItem);
        }
      }
    )
  );
  updateBoardStatus(boardStatusBarItem);

  vscode.commands.registerCommand('cros-ide.selectBoard', async () => {
    const board = await ideUtil.selectAndUpdateTargetBoard({
      suggestMostRecent: false,
    });
    if (board instanceof ideUtil.NoBoardError) {
      await vscode.window.showErrorMessage(`Selecting board: ${board.message}`);
      return;
    }
    // Type-check that errors are handled.
    ((_: string | null) => {})(board);
  });
}

function updateBoardStatus(boardStatusBarItem: vscode.StatusBarItem) {
  const board = ideUtil.getConfigRoot().get<string>(ideUtil.BOARD) || '';
  boardStatusBarItem.text = board;
  if (board) {
    boardStatusBarItem.show();
  } else {
    boardStatusBarItem.hide();
  }
}