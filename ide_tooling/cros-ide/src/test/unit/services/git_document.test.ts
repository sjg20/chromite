// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as gitDocument from '../../../services/git_document';
import * as testing from '../../testing';
import * as metrics from '../../../features/metrics/metrics';

describe('Git document provider', () => {
  const tempDir = testing.tempDir();

  const state = testing.cleanState(() => {
    return {
      gitDocumentProvider: new gitDocument.GitDocumentProvider(),
    };
  });

  it('retrieves git commit messages (HEAD)', async () => {
    spyOn(metrics, 'send');

    const git = new testing.Git(tempDir.path);
    await git.init();
    await git.commit('sample commit message');

    const uri = vscode.Uri.parse(
      `gitmsg://${git.root}/COMMIT%20MESSAGE?HEAD#spellchecker`
    );
    const doc = await state.gitDocumentProvider.provideTextDocumentContent(uri);
    expect(doc).toContain('sample commit message');
    expect(metrics.send).toHaveBeenCalledOnceWith({
      category: 'interactive',
      group: 'virtualdocument',
      action: 'open git document',
      label: 'spellchecker',
    });
  });

  it('retrieves git commit messages (SHA)', async () => {
    spyOn(metrics, 'send');

    const git = new testing.Git(tempDir.path);
    await git.init();
    const commitId = await git.commit('first commit');
    await git.commit('second commit');

    const uri = vscode.Uri.parse(
      `gitmsg://${git.root}/COMMIT%20MESSAGE?${commitId}#gerrit`
    );
    const doc = await state.gitDocumentProvider.provideTextDocumentContent(uri);
    expect(doc).toContain('first commit');
    expect(metrics.send).toHaveBeenCalledOnceWith({
      category: 'interactive',
      group: 'virtualdocument',
      action: 'open git document',
      label: 'gerrit',
    });
  });

  it('shows the link to file a bug', async () => {
    const uri = vscode.Uri.parse('gitmsg:///does/not/matter/no_file?HEAD');
    const doc = await state.gitDocumentProvider.provideTextDocumentContent(uri);
    expect(doc).toContain('go/cros-ide-new-bug');
  });
});
