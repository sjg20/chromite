// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// APIs Gerrit defines

/**
 * Response from Gerrit 'Get Change' API
 *
 * https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#change-info
 * https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#get-change
 */
export type ChangeInfo = {
  readonly change_id: string;
  readonly _number: number;
  readonly revisions?: CommitIdToRevisionInfo;
  readonly owner: AccountInfo;
  readonly created: string;
  readonly updated: string;
};

/**
 * The revisions field of a response from
 * Gerrit 'Get Change' API (called with the ALL_REVISIONS flag)
 */
export type CommitIdToRevisionInfo = {
  readonly [commitId: string]: RevisionInfo;
};

/**
 * One revision of a change uploaded to Gerrit, aka a patch set
 *
 * https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#revision-info
 */
export type RevisionInfo = {
  readonly _number: number | 'edit';
  readonly uploader: AccountInfo;
  readonly created: string;
};

/**
 * Response from Gerrit 'List Change Comments' API
 *
 * https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#list-change-comments
 */
export type FilePathToCommentInfos = {
  readonly [filePath: string]: readonly CommentInfo[];
};

/**
 * Special identifiers that can be used instead of a path to a file
 *
 * https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#file-id
 */
export const MAGIC_PATHS = Object.freeze([
  '/COMMIT_MSG',
  '/MERGE_LIST',
  '/PATCHSET_LEVEL',
]);

/**
 * Comment information in a response from Gerrit 'List Change Comments' API
 *
 * https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#comment-info
 */
export type CommentInfo = {
  readonly id: string;
  // TODO(b:216048068): author is optional in the API
  readonly author: AccountInfo;
  readonly range?: CommentRange;
  // Comments on entire lines have `line` but not `range`.
  readonly line?: number;
  readonly in_reply_to?: string;
  readonly updated: string;
  // TODO(b:216048068): message is optional in the API
  readonly message: string;
  readonly unresolved?: boolean;
  // SHA of the Git commit that the comment applies to.
  readonly commit_id?: string;
};

/**
 * Account information used in Gerrit APIs
 *
 * https://gerrit-review.googlesource.com/Documentation/rest-api-accounts.html#account-info
 */
export type AccountInfo = {
  readonly _account_id: number;
  readonly name?: string;
  readonly display_name?: string;
  readonly email?: string;
  readonly status?: string;
};

/**
 * Range of a comment, used in the range field of CommentInfo
 *
 * https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#comment-range
 */
export type CommentRange = {
  readonly start_line: number; // 1-based
  readonly start_character: number; // 0-based
  readonly end_line: number; // 1-based
  readonly end_character: number; // 0-based
};
