// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as parser from '../../../../../features/chromiumos/platform2_gtest/parser';

describe('platform2 gtest parser', () => {
  it('parses gtest cases', async () => {
    const content = [
      //             v 14
      'TEST(foo, bar) {', // Line 0
      '}',
      '// TEST(comment, out) {}',
      'TEST(A_b, c) {}', // Line 3
      //           ^ 12
    ].join('\n');

    expect(parser.parse(content)).toEqual([
      {
        range: new vscode.Range(
          new vscode.Position(0, 0),
          new vscode.Position(0, 14)
        ),
        suite: 'foo',
        name: 'bar',
      },
      {
        range: new vscode.Range(
          new vscode.Position(3, 0),
          new vscode.Position(3, 12)
        ),
        suite: 'A_b',
        name: 'c',
      },
    ]);
  });
});
