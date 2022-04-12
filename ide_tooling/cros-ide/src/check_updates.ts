// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as ideUtilities from './ide_utilities';
import * as install from './tools/install';

export async function run(context: vscode.ExtensionContext) {
  const extenstion = vscode.extensions.getExtension('google.cros-ide');
  // This should not happen.
  if (!extenstion) {
    return;
  }
  const installed = install.versionFromString(extenstion.packageJSON.version);

  const latest = (await install.findArchive()).version;

  if (install.compareVersion(installed, latest) < 0) {
    showInstallPrompt(install.versionToString(installed), install.versionToString(latest));
  }
}

const INSTALL = 'Install';

// TODO(oka): Test this function.
async function showInstallPrompt(installed: string, available: string) {
  const selection = await vscode.window.showInformationMessage(
      `New version of CrOS IDE is available (installed: ${installed}, available: ${available}).`,
      INSTALL, 'Dismiss');
  if (selection !== INSTALL) {
    return;
  }

  const exe = ideUtilities.vscodeExecutablePath();
  if (exe instanceof Error) {
    await handleFailure(exe);
    return;
  }

  // HACK(b:228887382): CODE_SERVER_PARENT_PID is set when the extension is running in code-server.
  // When another code-server executable is executed from the extension, it sees the environment
  // variable, and behaves differently than when it's run without it, resulting in installation
  // failure. To workaround, here we temporarily unset the environment variable before calling
  // install().
  const codeServerPid = process.env.CODE_SERVER_PARENT_PID;
  if (codeServerPid) {
    delete process.env.CODE_SERVER_PARENT_PID;
  }

  try {
    await install.install(exe);
  } catch (e) {
    await handleFailure(e as Error);
    return;
  } finally {
    if (codeServerPid) {
      process.env.CODE_SERVER_PARENT_PID = codeServerPid;
    }
  }
  await vscode.window.showInformationMessage(
      'Please reload the window to finish updating CrOS IDE');
}

const UPDATE_MANUALLY = 'Update manually';

async function handleFailure(e: Error) {
  // TODO(oka): add an option to open issue tracker using cros-ide.fileIdeBug command.
  const selection = await vscode.window.showErrorMessage(
      `Failed to install; please file a bug: ${e.message}`, UPDATE_MANUALLY);
  if (selection === UPDATE_MANUALLY) {
    vscode.env.openExternal(vscode.Uri.parse('http://go/cros-ide-quickstart#updating'));
  }
}
