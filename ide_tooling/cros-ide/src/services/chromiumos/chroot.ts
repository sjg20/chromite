// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as fs from 'fs';
import * as path from 'path';
import * as vscode from 'vscode';
import {ChrootExecOptions, CrosFs, execInChroot} from '../chroot';
import * as commonUtil from '../../common/common_util';
import {WrapFs} from '../../common/cros';

/**
 * Provides tools to operate chroot.
 */
export class ChrootService implements vscode.Disposable {
  private readonly chrootPath = path.join(this.chromiumosRoot, 'chroot');

  // Throws if chroot is not found.
  private constructor(
    private readonly chromiumosRoot: string,
    private readonly setContext: boolean
  ) {
    if (!fs.existsSync(this.chrootPath)) {
      throw new Error('chroot not found');
    }
    if (setContext) {
      void vscode.commands.executeCommand(
        'setContext',
        'cros-ide.chrootPath',
        this.chrootPath
      );
    }
  }

  dispose() {
    if (this.setContext) {
      void vscode.commands.executeCommand(
        'setContext',
        'cros-ide.chrootPath',
        undefined
      );
    }
  }

  /**
   * Creates the service or returns undefined with showing an error if chroot is
   * not found under the given chromiumos root. Specify setContext = true to set
   * `cros-ide.chrootPath` context for the custom `when` clauses in boards and
   * packages view etc.
   *
   * TODO(oka): remove setContext. This value is false by default for unit
   * tests' convenience where vscode.commands.executeCommand is not implemented.
   * We should fake the method and let it always run.
   */
  static maybeCreate(
    root: string,
    setContext = false
  ): ChrootService | undefined {
    try {
      return new ChrootService(root, setContext);
    } catch (_e) {
      void showChrootNotFoundError(root);
      return undefined;
    }
  }

  /**
   * Returns an accessor to files under chroot.
   */
  get chroot(): WrapFs<commonUtil.Chroot> {
    return new WrapFs(this.chrootPath as commonUtil.Chroot);
  }

  /**
   * Returns an accessor to files under source.
   */
  get source(): WrapFs<commonUtil.Source> {
    return new WrapFs(this.chromiumosRoot as commonUtil.Source);
  }

  get crosFs(): CrosFs {
    return {
      chroot: this.chroot,
      source: this.source,
    };
  }

  /**
   * Executes command in chroot. Returns InvalidPasswordError in case the user
   * enters invalid password.
   */
  async exec(
    name: string,
    args: string[],
    options: ChrootExecOptions
  ): ReturnType<typeof commonUtil.exec> {
    const source = this.source;
    if (source === undefined) {
      return new Error(
        'cros_sdk not found; open a directory under which chroot has been set up'
      );
    }
    return await execInChroot(source.root, name, args, options);
  }
}

async function showChrootNotFoundError(root: string) {
  const OPEN = 'Open';
  const answer = await vscode.window.showErrorMessage(
    `chroot not found under ${root}: follow the developer guide to create a chroot`,
    OPEN
  );
  if (answer === OPEN) {
    await vscode.env.openExternal(
      vscode.Uri.parse(
        'https://chromium.googlesource.com/chromiumos/docs/+/HEAD/developer_guide.md#Create-a-chroot'
      )
    );
  }
}
