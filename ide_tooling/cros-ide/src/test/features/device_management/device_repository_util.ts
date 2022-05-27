// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as ideUtil from '../../../ide_util';

export async function setOwnedDevices(hosts: string[]): Promise<void> {
  return await ideUtil
    .getConfigRoot()
    .update(
      'deviceManagement.devices',
      hosts,
      vscode.ConfigurationTarget.Global
    );
}
