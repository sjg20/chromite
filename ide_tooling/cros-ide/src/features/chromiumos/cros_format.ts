// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as commonUtil from '../../common/common_util';
import * as ideUtil from '../../ide_util';
import {StatusManager, TaskStatus} from '../../ui/bg_task_status';

// Task name in the status manager.
const FORMATTER = 'Formatter';

export function activate(
  context: vscode.ExtensionContext,
  statusManager: StatusManager
) {
  const outputChannel = vscode.window.createOutputChannel(
    'CrOS IDE: Formatter'
  );
  statusManager.setTask(FORMATTER, {
    status: TaskStatus.OK,
    outputChannel,
  });

  // File name patterns were copied from
  // https://source.chromium.org/chromium/chromium/src/+/main:third_party/chromite/cli/cros/cros_format.py
  // TODO(b:232466489): figure out a better way of sharing what's supported by `cros lint`
  // TODO(b:232466489): revisit intentionally omitted file types
  const globs = [
    // JSON omitted intentionally: there is ongoing discussion about it.
    '*.md',
    '*.cfg',
    '*.conf',
    '*.txt',
    '.clang-format',
    '.gitignore',
    '.gitmodules',
    // GN omitted intentionally: it has its own formatter.
    'COPYING*',
    'LICENSE*',
    'make.defaults',
    'package.accept_keywords',
    'package.force',
    'package.keywords',
    'package.mask',
    'package.provided',
    'package.unmask',
    'package.use',
    'package.use.mask',
    'DIR_METADATA',
    'OWNERS*',
  ];
  const documentSelector = globs.map(g => {
    return {schema: 'file', pattern: '**/' + g};
  });
  context.subscriptions.push(
    vscode.languages.registerDocumentFormattingEditProvider(
      documentSelector,
      new CrosFormat(statusManager, outputChannel)
    )
  );
}

class CrosFormat implements vscode.DocumentFormattingEditProvider {
  constructor(
    private readonly statusManager: StatusManager,
    private readonly outputChannel: vscode.OutputChannel
  ) {}

  async provideDocumentFormattingEdits(document: vscode.TextDocument) {
    this.outputChannel.appendLine(`Formatting ${document.uri.fsPath}...`);

    const formatterOutput = await commonUtil.exec(
      'cros',
      ['format', '--stdout', document.uri.fsPath],
      {
        logger: ideUtil.getUiLogger(),
        ignoreNonZeroExit: true,
      }
    );

    if (formatterOutput instanceof Error) {
      this.outputChannel.appendLine(formatterOutput.message);
      this.statusManager.setStatus(FORMATTER, TaskStatus.ERROR);
      return undefined;
    }

    if (formatterOutput.exitStatus === 0) {
      // 0 means input does not require formatting
      this.outputChannel.appendLine('no changes needed');
      this.statusManager.setStatus(FORMATTER, TaskStatus.OK);
      return undefined;
    } else if (formatterOutput.exitStatus === 1) {
      // 1 means the file required formatting
      this.outputChannel.appendLine('file required formatting');
      this.statusManager.setStatus(FORMATTER, TaskStatus.OK);
      const wholeFileRange = new vscode.Range(
        document.positionAt(0),
        document.positionAt(document.getText().length)
      );
      return [vscode.TextEdit.replace(wholeFileRange, formatterOutput.stdout)];
    } else {
      // Error status other than 1 means that an error occurred.
      // We also handle the case when the command exits due to a signal and there is
      // no exit status.
      this.outputChannel.appendLine(formatterOutput.stderr);
      this.statusManager.setStatus(FORMATTER, TaskStatus.ERROR);
      return undefined;
    }
  }
}

export const TEST_ONLY = {
  CrosFormat,
};
