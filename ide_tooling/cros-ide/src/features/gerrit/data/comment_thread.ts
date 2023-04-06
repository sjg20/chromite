// Copyright 2023 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as path from 'path';
import * as vscode from 'vscode';
import * as gitDocument from '../../../services/git_document';
import * as api from '../api';
import * as git from '../git';
import * as virtualDocument from '../virtual_document';
import {getCommentContextValue, toVscodeComment} from './comment';
import {Comment} from '.';

// TODO(oka): Make this class immutable.
/**
 * Represents a Gerrit comment thread that belongs to a Gerrit CL.
 * The usage of this class is as follows.
 * 1. Initialize with the comment infos and the local git log info for the CL.
 * 2. Call setShift to update the shift count and displayForVscode to display the comment thread
 *    on VSCode.
 * 3. To clear the comment thread from VSCode, call clearFromVscode
 */
export class CommentThread {
  private readonly comments: readonly Comment[];
  private vscodeCommentThread?: VscodeCommentThread;
  /**
   * Line shift for repositioning the comment thread from the original
   * location to the corresponding line in the working tree.
   * (Column shift is ignored)
   */
  private shift = 0;

  constructor(
    private readonly localCommitId: string,
    readonly repoId: git.RepoId,
    private readonly changeId: string,
    readonly changeNumber: number,
    private readonly revisionNumber: number | 'edit',
    commentInfos: api.CommentInfo[]
  ) {
    this.comments = commentInfos.map(
      commentInfo => new Comment(repoId, changeNumber, commentInfo)
    );
  }

  get firstComment(): Comment {
    return this.comments[0];
  }
  private get lastComment(): Comment {
    return this.comments[this.comments.length - 1];
  }

  /** Original line */
  private get originalLine(): number | undefined {
    return this.firstComment.commentInfo.line;
  }

  /** Shifted line */
  private get line(): number | undefined {
    const ol = this.originalLine;
    if (ol === undefined) return undefined;
    return ol + this.shift;
  }

  /** Shifted range */
  private get range(): api.CommentRange | undefined {
    const r = this.firstComment.commentInfo.range;
    if (r === undefined) return undefined;
    return {
      start_line: r.start_line + this.shift,
      start_character: r.start_character,
      end_line: r.end_line + this.shift,
      end_character: r.end_character,
    };
  }

  /** A thread is unresolved if its last comment is unresolved. */
  get unresolved(): boolean {
    // Unresolved can be undefined according to the API documentation,
    // but Gerrit always sent it on the changes the we inspected.
    return this.lastComment.commentInfo.unresolved!;
  }

  /**
   * Repositions threads based on the given hunks.
   *
   * Thread position is determined by its first comment,
   * so only the first comment is updated. The updates are in-place.
   */
  setShift(hunks: readonly git.Hunk[], filePath: string): void {
    let shift = 0;
    const ol = this.originalLine;
    for (const hunk of hunks) {
      if (this.followsHunk(hunk)) {
        // Comment outside the hunk
        shift += hunk.sizeDelta;
      } else if (this.withinRange(hunk.originalStart, hunk.originalEnd)) {
        // Comment within the hunk
        // Ensure the comment within the hunk still resides in the
        // hunk. If the hunk removes all the lines, the comment will
        // be moved to the line preceding the hunk.
        if (hunk.sizeDelta < 0 && ol !== undefined) {
          const protrusion = ol - (hunk.originalStart + hunk.currentSize) + 1;
          if (protrusion > 0) shift -= protrusion;
        }
      }
    }
    // Make sure we do not shift comments before the first line
    // because it causes errors (lines beyond the end of file are fine though).
    //
    // Note, that line numbers are 1-based. The code that shifts comments within
    // deleted hunks may put comments on line 0 (we use `<=` in case of unknown bugs),
    // so we adjust `shift` so that `originalLine + shift == 1`.
    if (ol !== undefined && ol + shift <= 0) shift = -(ol - 1);
    if (filePath === '/COMMIT_MSG' && ol !== undefined) {
      // Compensate the difference between commit message on Gerrit and Terminal
      shift -= ol > 6 ? 6 : ol - 1;
    }
    this.shift = shift;
  }

  overwriteShiftForTesting(shift: number): void {
    this.shift = shift;
  }

  /**
   * True if a thread starts after the hunk ends. Such threads should be moved
   * by the size change introduced by the hunk.
   */
  private followsHunk(hunk: git.Hunk): boolean {
    const ol = this.originalLine;
    if (!ol) return false;
    // Case 1: hunks that insert lines.
    // The original side is `N,0` and the hunk inserts lines between N and N+1.
    if (hunk.originalSize === 0) return ol > hunk.originalStart;
    // Case 2: Modifications and deletions
    // The original side is `N,size` and the hunk modifies 'size' lines starting from N.
    return ol >= hunk.originalStart + hunk.originalSize;
  }

  /**
   * Returns whether the comment is in the range between
   * minimum (inclusive) and maximum (exclusive).
   */
  private withinRange(minimum: number, maximum: number): boolean {
    const ol = this.originalLine;
    return ol !== undefined && ol >= minimum && ol < maximum;
  }

  /**
   * Displays the comment thread in the UI,
   * creating a VS Code comment thread if not yet created.
   * To reposition by local changes, call setShift before calling it.
   */
  displayForVscode(
    controller: vscode.CommentController,
    gitDir: string,
    filePath: string
  ): void {
    if (this.vscodeCommentThread) {
      // Recompute the range
      this.vscodeCommentThread.range = this.getVscodeRange();
      return;
    }
    this.createVscodeCommentThread(controller, gitDir, filePath);
  }

  private createVscodeCommentThread(
    controller: vscode.CommentController,
    gitDir: string,
    path: string
  ): void {
    const dataUri = this.getDataUri(gitDir, path);
    const vscodeCommentThread = controller.createCommentThread(
      dataUri,
      this.getVscodeRange(),
      this.comments.map(comment => toVscodeComment(comment))
    ) as VscodeCommentThread;
    vscodeCommentThread.gerritCommentThread = this; // Remember the comment thread
    vscodeCommentThread.canReply = false;
    const revisionNumber = this.revisionNumber;
    // TODO(b:216048068): We should indicate resolved/unresolved with UI style.
    if (this.unresolved) {
      vscodeCommentThread.label = `Patchset ${revisionNumber} / Unresolved`;
      vscodeCommentThread.collapsibleState =
        vscode.CommentThreadCollapsibleState.Expanded;
    } else {
      vscodeCommentThread.label = `Patchset ${revisionNumber} / Resolved`;
    }
    // A comment thread's context is based off the first comment.
    vscodeCommentThread.contextValue = getCommentContextValue(
      this.comments?.[0]?.commentInfo
    );
    this.vscodeCommentThread = vscodeCommentThread;
  }

  private getDataUri(gitDir: string, filePath: string): vscode.Uri {
    if (filePath === '/COMMIT_MSG') {
      return gitDocument.commitMessageUri(
        gitDir,
        this.localCommitId,
        'gerrit commit msg'
      );
    } else if (filePath === '/PATCHSET_LEVEL') {
      return virtualDocument.patchSetUri(gitDir, this.changeId);
    } else {
      return vscode.Uri.file(path.join(gitDir, filePath));
    }
  }

  /** Gets vscode.Range for the comment. */
  private getVscodeRange(): vscode.Range {
    const r = this.range;
    if (r !== undefined) {
      // Comment thread for some range
      // VSCode is 0-base, whereas Gerrit has 1-based lines and 0-based columns.
      return new vscode.Range(
        r.start_line - 1,
        r.start_character,
        r.end_line - 1,
        r.end_character
      );
    }
    const l = this.line;
    if (l !== undefined) {
      // Comment thread for a line
      return new vscode.Range(l - 1, 0, l - 1, 0);
    }
    // Comment thread for the entire file
    return new vscode.Range(0, 0, 0, 0);
  }

  clearFromVscode(): void {
    if (this.vscodeCommentThread) {
      this.vscodeCommentThread.dispose();
      this.vscodeCommentThread = undefined;
    }
  }

  collapseInVscode(): void {
    if (this.vscodeCommentThread) {
      this.vscodeCommentThread.collapsibleState =
        vscode.CommentThreadCollapsibleState.Collapsed;
    }
  }
}

/** vscode.CommentThread extended with a reference to CommentThread */
export interface VscodeCommentThread extends vscode.CommentThread {
  /**
   * Reference to the comment thread, which we can use in
   * event callbacks on the VS Code comment thread
   */
  gerritCommentThread: CommentThread;
}
