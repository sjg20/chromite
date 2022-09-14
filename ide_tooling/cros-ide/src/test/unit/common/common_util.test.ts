// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as assert from 'assert';
import * as fs from 'fs';
import * as path from 'path';
import * as vscode from 'vscode';
import * as commonUtil from '../../../common/common_util';
import * as testing from '../../testing';

class SimpleLogger {
  constructor(private readonly f: (s: string) => void) {}

  append(s: string): void {
    this.f(s);
  }
}

describe('Job manager', () => {
  it('throttles jobs', async () => {
    const manager = new commonUtil.JobManager();

    const guard = await testing.BlockingPromise.new(undefined);

    const p1 = manager.offer(async () => {
      await guard.promise;
      return true;
    });

    await testing.flushMicrotasks();

    const p2 = manager.offer(async () => {
      assert.fail('Intermediate job should not run');
    });

    let p3Run = false;
    const p3 = manager.offer(async () => {
      // The last-offered job should be queued.
      p3Run = true;
    });

    // Cancelled job should return immediately.
    assert.strictEqual(await p2, null);

    assert.strictEqual(p3Run, false); // p3 should not run while p1 is running

    guard.unblock();

    assert.strictEqual(await p1, true);
    await p3;

    assert.strictEqual(p3Run, true);
  });

  it('handles errors', async () => {
    const manager = new commonUtil.JobManager();

    const guard = await testing.BlockingPromise.new(undefined);

    const p1 = manager.offer(async () => {
      await guard.promise;
      throw new Error('p1');
    });

    await testing.flushMicrotasks();

    const p2 = manager.offer(async () => {
      assert.fail('Intermediate job should not run');
    });
    const p3 = manager.offer(async () => {
      throw new Error('p3');
    });

    await p2;

    guard.unblock();
    await assert.rejects(p1);
    await assert.rejects(p3);
  });
});

describe('Logging exec', () => {
  const temp = testing.tempDir();

  it('returns stdout and logs stderr', async () => {
    let logs = '';
    const res = await commonUtil.exec('sh', ['-c', 'echo foo; echo bar 1>&2'], {
      logger: new SimpleLogger(log => {
        logs += log;
      }),
    });
    assert(!(res instanceof Error));
    assert.strictEqual(res.stdout, 'foo\n');
    assert.strictEqual(logs, "sh -c 'echo foo; echo bar 1>&2'\nbar\n");
  });

  it('mixes stdout and stderr if logStdout flag is true', async () => {
    let logs = '';
    await commonUtil.exec('sh', ['-c', 'echo foo; echo bar 1>&2'], {
      logger: new SimpleLogger(log => {
        logs += log;
      }),
      logStdout: true,
    });
    assert.strictEqual(
      logs.length,
      "sh -c 'echo foo; echo bar 1>&2'\nfoo\nbar\n".length
    );
  });

  it('returns error on non-zero exit status when unrelated flags are set', async () => {
    let logs = '';
    const res = await commonUtil.exec('sh', ['-c', 'echo foo 1>&2; exit 1'], {
      logger: new SimpleLogger(log => {
        logs += log;
      }),
      logStdout: true,
    });
    assert(res instanceof commonUtil.AbnormalExitError);
    assert(
      res.message.includes("sh -c 'echo foo 1>&2; exit 1'"),
      'actual message: ' + res.message
    );
    assert.strictEqual(logs, "sh -c 'echo foo 1>&2; exit 1'\nfoo\n");
  });

  it('returns error on non-zero exit status when no flags are specified', async () => {
    let logs = '';
    const res = await commonUtil.exec('sh', ['-c', 'echo foo 1>&2; exit 1'], {
      logger: new SimpleLogger(log => {
        logs += log;
      }),
    });
    assert(res instanceof commonUtil.AbnormalExitError);
    assert(
      res.message.includes("sh -c 'echo foo 1>&2; exit 1'"),
      'actual message: ' + res.message
    );
    assert.strictEqual(logs, "sh -c 'echo foo 1>&2; exit 1'\nfoo\n");
  });

  it('ignores non-zero exit status if ignoreNonZeroExit flag is true', async () => {
    let logs = '';
    const res = await commonUtil.exec(
      'sh',
      ['-c', 'echo foo 1>&2; echo bar; exit 1'],
      {
        logger: new SimpleLogger(log => {
          logs += log;
        }),
        ignoreNonZeroExit: true,
      }
    );
    assert(!(res instanceof Error));
    const {exitStatus, stdout, stderr} = res;
    assert.strictEqual(exitStatus, 1);
    assert.strictEqual(stdout, 'bar\n');
    assert.strictEqual(stderr, 'foo\n');
    assert.strictEqual(logs, "sh -c 'echo foo 1>&2; echo bar; exit 1'\nfoo\n");
  });

  it('appends new lines to log', async () => {
    let logs = '';
    const res = await commonUtil.exec(
      'sh',
      ['-c', 'echo -n foo; echo -n bar 1>&2;'],
      {
        logger: new SimpleLogger(log => {
          logs += log;
        }),
        logStdout: true,
      }
    );
    assert(!(res instanceof Error));
    assert.strictEqual(res.stdout, 'foo');
    assert.deepStrictEqual(logs.split('\n').sort(), [
      '',
      'bar',
      'foo',
      "sh -c 'echo -n foo; echo -n bar 1>&2;'",
    ]);
  });

  it('can supply stdin', async () => {
    const res = await commonUtil.exec('cat', [], {pipeStdin: 'foo'});
    assert(!(res instanceof Error));
    assert.strictEqual(res.stdout, 'foo');
  });

  it('returns error when the command fails', async () => {
    const res = await commonUtil.exec('does_not_exist', ['--version']);
    assert(res instanceof commonUtil.ProcessError);
    assert(
      res.message.includes('does_not_exist --version'),
      'actual message: ' + res.message
    );
  });

  it('can abort command execution', async () => {
    const canceller = new vscode.CancellationTokenSource();
    const process = commonUtil.exec('sleep', ['100'], {
      cancellationToken: canceller.token,
    });
    canceller.cancel();
    const res = await process;
    assert(res instanceof commonUtil.CancelledError);
  });

  it('changes the directory if cwd is specified', async () => {
    const res = await commonUtil.exec('pwd', [], {cwd: temp.path});
    assert(!(res instanceof Error));
    expect(res.stdout).toContain(temp.path);
  });
});

describe('withTimeout utility', () => {
  it('returns before timeout', async () => {
    assert.strictEqual(
      await commonUtil.withTimeout(Promise.resolve(true), 1 /* millis*/),
      true
    );
  });

  it('returns undefined after timeout', async () => {
    const f = await testing.BlockingPromise.new(true);
    try {
      assert.strictEqual(await commonUtil.withTimeout(f.promise, 1), undefined);
    } finally {
      f.unblock();
    }
  });
});

function assertNotGitRepository(tempDir: string) {
  const tempRoot = /(\/\w+)/.exec(tempDir)![1];
  if (fs.existsSync(path.join(tempRoot, '.git'))) {
    throw new Error(
      `bad test environment: please remove ${tempRoot}/.git and rerun the test`
    );
  }
}

describe('getGitDir', () => {
  const tempDir = testing.tempDir();

  it('returns Git root directory', async () => {
    assertNotGitRepository(tempDir.path);

    await testing.putFiles(tempDir.path, {
      'a/b/c/d.txt': '',
      'a/e.txt': '',
      'x/y/z.txt': '',
    });
    await commonUtil.exec('git', ['init'], {
      cwd: path.join(tempDir.path, 'a/b'),
    });
    await commonUtil.exec('git', ['init'], {cwd: path.join(tempDir.path, 'a')});

    expect(
      commonUtil.findGitDir(path.join(tempDir.path, 'a/b/c/d.txt'))
    ).toEqual(path.join(tempDir.path, 'a/b'));
    expect(commonUtil.findGitDir(path.join(tempDir.path, 'a/e.txt'))).toEqual(
      path.join(tempDir.path, 'a')
    );
    expect(
      commonUtil.findGitDir(path.join(tempDir.path, 'x/y/z.txt'))
    ).toBeUndefined();
  });
});
