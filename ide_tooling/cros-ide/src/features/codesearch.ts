// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
import * as vscode from 'vscode';
import * as commonUtil from '../common/common_util';
import * as ideUtil from '../ide_util';
import * as metrics from './metrics/metrics';

export function activate(context: vscode.ExtensionContext) {
  const openFileCmd = vscode.commands.registerTextEditorCommand(
    'cros-ide.codeSearchOpenCurrentFile',
    (textEditor: vscode.TextEditor) => openCurrentFile(textEditor)
  );

  const searchSelectionCmd = vscode.commands.registerTextEditorCommand(
    'cros-ide.codeSearchSearchForSelection',
    (textEditor: vscode.TextEditor) => searchSelection(textEditor)
  );

  context.subscriptions.push(openFileCmd, searchSelectionCmd);
}

const generateCsPath = '/mnt/host/source/chromite/contrib/generate_cs_path';
const codeSearch = 'codeSearch';

async function openCurrentFile(textEditor: vscode.TextEditor) {
  const fullpath = textEditor.document.fileName;

  // Which CodeSearch to use, options are public, internal, or gitiles.
  const csInstance = ideUtil.getConfigRoot().get<string>(codeSearch);

  const line = textEditor.selection.active.line + 1;

  const res = await commonUtil.exec(
    generateCsPath,
    ['--show', `--${csInstance}`, `--line=${line}`, fullpath],
    ideUtil.getUiLogger().append,
    {logStdout: true, ignoreNonZeroExit: true}
  );

  if (res instanceof Error) {
    vscode.window.showErrorMessage('Could not run generate_cs_path: ' + res);
    return;
  }

  const {exitStatus, stdout, stderr} = res;
  if (exitStatus) {
    vscode.window.showErrorMessage(
      `generate_cs_path returned an error: ${stderr}`
    );
    metrics.send({
      category: 'codesearch',
      action: 'generate CodeSearch path',
      label: `Failed: ${stderr}`,
    });
    return;
  }

  // trimEnd() to get rid of the newline.
  vscode.env.openExternal(vscode.Uri.parse(stdout.trimEnd()));
  metrics.send({
    category: 'codesearch',
    action: 'open current file',
    label: `${fullpath}:${line}`,
  });
}

// TODO: Figure out if the search should be limited to the current repo.
function searchSelection(textEditor: vscode.TextEditor) {
  if (textEditor.selection.isEmpty) {
    return;
  }

  // If the setting is gitiles, we use public CodeSearch
  const csInstance = ideUtil.getConfigRoot().get<string>(codeSearch);
  const csBase =
    csInstance === 'internal'
      ? 'https://source.corp.google.com/'
      : 'https://source.chromium.org/';

  const selectedText = textEditor.document.getText(textEditor.selection);
  const uri = vscode.Uri.parse(csBase).with({
    path: '/search',
    query: `q=${selectedText}`,
  });
  vscode.env.openExternal(uri);
  metrics.send({
    category: 'codesearch',
    action: 'search selection',
    label: selectedText,
  });
}

export const TEST_ONLY = {
  openCurrentFile,
  searchSelection,
};
