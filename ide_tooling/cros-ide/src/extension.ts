// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

/**
 * This is the main entry point for the vsCode plugin.
 *
 * Keep this minimal - breakout GUI and App-Behavior to separate files.
 */
import * as vscode from 'vscode';
import * as dutManager from './dut_management/dut_manager';
import * as crosLint from './cros_lint';
import * as boardsPackages from './boards_packages';
import * as shortLinkProvider from './short_link_provider';
import * as codesearch from './codesearch';
import * as workon from './workon';
import * as cppCodeCompletion from './cpp_code_completion';

export function activate(context: vscode.ExtensionContext) {
  dutManager.activateDutManager(context);
  crosLint.activate(context);
  boardsPackages.activate();
  shortLinkProvider.activate(context);
  codesearch.activate(context);
  workon.activate(context);
  cppCodeCompletion.activate(context);
}
