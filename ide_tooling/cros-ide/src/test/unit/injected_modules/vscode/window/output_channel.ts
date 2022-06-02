// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import type * as vscode from 'vscode'; // import types only

class VoidOutputChannel implements vscode.OutputChannel {
  constructor(public readonly name: string) {}

  append(): void {}
  appendLine(): void {}
  replace(): void {}
  clear(): void {}
  show(): void {}
  hide(): void {}
  dispose(): void {}
}

export function createOutputChannel(name: string): vscode.OutputChannel {
  return new VoidOutputChannel(name);
}
