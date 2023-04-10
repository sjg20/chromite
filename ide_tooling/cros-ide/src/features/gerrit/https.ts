// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as https from 'https';
import {Sink} from './sink';

/**
 * Fetches a raw string from https.
 *
 * Returns the response if it is successful or undefined on 404 error.
 * Everything else throws an error.
 */
export async function getOrThrow(
  url: string,
  options: https.RequestOptions = {}
): Promise<string | undefined> {
  return new Promise((resolve, reject) => {
    https
      .get(url, options, res => {
        if (res.statusCode === 404) {
          resolve(undefined);
        }
        if (res.statusCode !== 200) {
          reject(new Error(`status code: ${res.statusCode}`));
        }
        const body: Uint8Array[] = [];
        res.on('data', data => body.push(data));
        res.on('end', () => {
          resolve(Buffer.concat(body).toString());
        });
      })
      .on('error', reject);
  });
}

/**
 * Sends PUT request over https.
 *
 * Returns the response if it is successful (200).
 * Otherwise throws an error.
 */
export async function putJsonOrThrow(
  url: string,
  postData: Object,
  options: https.RequestOptions = {},
  sink: Sink
): Promise<string> {
  const postDataString = JSON.stringify(postData);

  const opts = {
    method: 'PUT',
    ...options,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Content-Length': Buffer.byteLength(postDataString),
      ...options.headers,
    },
  };

  sink.appendLine(`PUT ${url} ${postDataString} ${JSON.stringify(opts)}`);

  return new Promise((resolve, reject) => {
    const req = https
      .request(url, opts, res => {
        const body: Uint8Array[] = [];
        res.on('data', data => body.push(data));
        res.on('end', () => {
          const status = res.statusCode!;
          if (200 <= status && status < 300) {
            resolve(Buffer.concat(body).toString());
            return;
          }
          reject(
            new Error(`status code ${res.statusCode}: ${body.toString()}`)
          );
        });
      })
      .on('error', reject);

    req.write(postDataString);
    req.end();
  });
}
