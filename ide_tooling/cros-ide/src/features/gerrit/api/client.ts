// Copyright 2023 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as git from '../git';
import * as https from '../https';
import * as api from '.';

/**
 * Provides primitive methods to call Gerrit REST APIs.
 */
export class RawGerritClient {
  /**
   * Gets a raw string from Gerrit REST API with an auth cookie, returning
   * undefined on 404 error. It can throw an error from https.getOrThrow.
   */
  async fetchOrThrow<T>(
    repoId: git.RepoId,
    path: string,
    authCookie?: string
  ): Promise<T | undefined> {
    const url = `${git.gerritUrl(repoId)}/${path}`;
    const options =
      authCookie !== undefined ? {headers: {cookie: authCookie}} : undefined;
    const str = await https.getOrThrow(url, options);
    return str === undefined ? undefined : api.parseResponse(str);
  }
}

/**
 * Provides custom APIs which use Gerrit REST APIs under the hood.
 */
export class GerritClient {
  private readonly client = new RawGerritClient();

  constructor() {}

  /** Fetches the user's account info */
  async fetchMyAccountInfoOrThrow(
    repoId: git.RepoId,
    authCookie?: string
  ): Promise<api.AccountInfo | undefined> {
    return this.client.fetchOrThrow(repoId, 'accounts/me', authCookie);
  }

  /** Fetches the change with all revisions */
  async fetchChangeOrThrow(
    repoId: git.RepoId,
    changeId: string,
    authCookie?: string
  ): Promise<api.ChangeInfo | undefined> {
    return await this.client.fetchOrThrow(
      repoId,
      `changes/${changeId}?o=ALL_REVISIONS`,
      authCookie
    );
  }

  /** Fetches all public comments of the change */
  async fetchPublicCommentsOrThrow(
    repoId: git.RepoId,
    changeId: string,
    authCookie?: string
  ): Promise<api.FilePathToCommentInfos | undefined> {
    const baseCommentInfosMap: api.FilePathToBaseCommentInfos | undefined =
      await this.client.fetchOrThrow(
        repoId,
        `changes/${changeId}/comments`,
        authCookie
      );
    if (!baseCommentInfosMap) return undefined;

    const res: {[filePath: string]: api.CommentInfo[]} = {};
    for (const [filePath, baseCommentInfos] of Object.entries(
      baseCommentInfosMap
    )) {
      res[filePath] = baseCommentInfos.map(c => ({
        ...c,
        author: c.author!,
        isPublic: true,
      }));
    }
    return res;
  }

  /** Fetches all draft comments of the change */
  async fetchDraftCommentsOrThrow(
    repoId: git.RepoId,
    changeId: string,
    myAccountInfo: api.AccountInfo,
    authCookie?: string
  ): Promise<api.FilePathToCommentInfos | undefined> {
    const baseCommentInfosMap: api.FilePathToBaseCommentInfos | undefined =
      await this.client.fetchOrThrow(
        repoId,
        `changes/${changeId}/drafts`,
        authCookie
      );
    if (!baseCommentInfosMap) return undefined;

    const res: {[filePath: string]: api.CommentInfo[]} = {};
    for (const [filePath, baseCommentInfos] of Object.entries(
      baseCommentInfosMap
    )) {
      res[filePath] = baseCommentInfos.map(c => ({
        ...c,
        author: myAccountInfo,
        isPublic: false,
      }));
    }
    return res;
  }
}
