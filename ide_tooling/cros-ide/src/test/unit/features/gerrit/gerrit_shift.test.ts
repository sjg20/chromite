// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'jasmine';
import * as gerrit from '../../../../features/gerrit/gerrit';
import * as git from '../../../../features/gerrit/git';

function hunk(
  originalStartLine: number,
  originalLineSize: number,
  currentStartLine: number,
  currentLineSize: number
): git.Hunk {
  return {
    originalStartLine,
    originalLineSize,
    currentStartLine,
    currentLineSize,
  };
}

function range(
  startLine: number,
  startCharacter: number,
  endLine: number,
  endCharacter: number
): gerrit.CommentRange {
  return {
    startLine,
    startCharacter,
    endLine,
    endCharacter,
  };
}

const testHunks: git.Hunks = {
  'foo.ts': [
    // First line added.
    hunk(0, 0, 1, 1),
    // Third line removed.
    hunk(3, 1, 3, 0),
    // Fifth to seventh line removed.
    hunk(5, 3, 5, 0),
  ],
  'bar.ts': [
    // First line added.
    hunk(0, 0, 1, 1),
  ],
};

const changeComments = {
  'foo.ts': [
    {message: 'foo'}, // comment on a file
    {range: range(1, 1, 1, 2), line: 1}, // comment on characters
    {line: 1}, // comment on a line
    {line: 4},
    // Not yet implemented
    // {line: 6}, // comment in a removed hunk
    // {range: range(3, 1, 6, 2), line: 1}, // comment across multiple hunks.
  ],
  'bar.ts': [{line: 1}],
} as unknown as gerrit.ChangeComments;

const wantComments = {
  'foo.ts': [
    {message: 'foo'}, // comment on a file
    {range: range(2, 1, 2, 2), line: 2}, // comment on characters
    {line: 2}, // comment on a line
    {line: 4},
    // Not yet implemented
    // {line: 6}, // comment in a removed hunk
    // {range: range(3, 1, 5, 2), line: 1}, // comment across multiple hunks.
  ],
  'bar.ts': [{line: 2}],
  // TODO(teramon): Add other test cases
  // comments for a whole file and characters.
} as unknown as gerrit.ChangeComments;

describe('Gerrit support', () => {
  it('update change comments', () => {
    const updatedChangeComments = gerrit.updateChangeComments(
      testHunks,
      changeComments
    );
    expect(updatedChangeComments).toEqual(wantComments);
  });
});