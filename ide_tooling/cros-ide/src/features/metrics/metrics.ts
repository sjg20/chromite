// Copyright 2022 The Chromium OS Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as https from 'https';
import * as os from 'os';
import * as queryString from 'querystring';
import * as vscode from 'vscode';
import * as ideUtil from '../../ide_util';
import * as metricsConfig from './metrics_config';
import * as metricsUtils from './metrics_util';

const informationMessageTitle =
  'CrOS IDE team would like to collect metrics to have a better understanding and improve on ' +
  'your experience!';

const informationMessageDetail =
  'This includes data on install, uninstall, and invocation events of extension features, to ' +
  'obtain insights on how users are using our extension and their satisfaction level.\n' +
  'Working directories of these events will be recorded to help us to identify repositories / ' +
  'projects that the extension is less popular and/or helpful so we can improve on user ' +
  'experience for the teams specifically.\n' +
  'The data is pseudonymous. i.e. it is associated with a randomly generated unique user ID ' +
  'which resets every 180 days automatically, and you can also reset it from the Command ' +
  'Palette.\n' +
  'Raw data is only accessible by the modern IDE team. However, aggregated data (e.g. trend ' +
  'of number of users against time) might be shared with a broader audience for retrospective or ' +
  'advertising purposes.\n' +
  'You can opt-in or out of metrics collection anytime in settings (> extension > CrOS IDE).\n' +
  'Metrics from external (non-googler) users will not be collected.' +
  '\n' +
  'Would you like to assist us by turning on metrics collection for CrOS IDE extension?';

// This variable is set by activate() to make the extension mode available globally.
let extensionMode: vscode.ExtensionMode | undefined = undefined;
let extensionVersion: string | undefined = undefined;

export function activate(context: vscode.ExtensionContext) {
  extensionMode = context.extensionMode;
  extensionVersion = context.extension.packageJSON.version;

  // Do not show the consent dialog if the extension is running for integration tests.
  // Modal dialogs make tests fail.
  if (context.extensionMode !== vscode.ExtensionMode.Test) {
    const showMessage = ideUtil
      .getConfigRoot()
      .get<boolean>('metrics.showMessage');
    if (showMessage) {
      vscode.window
        .showInformationMessage(
          informationMessageTitle,
          {detail: informationMessageDetail, modal: true},
          'Yes'
        )
        .then(selection => {
          if (selection && selection === 'Yes') {
            ideUtil
              .getConfigRoot()
              .update(
                'metrics.collectMetrics',
                true,
                vscode.ConfigurationTarget.Global
              );
          }
        });
      ideUtil
        .getConfigRoot()
        .update(
          'metrics.showMessage',
          false,
          vscode.ConfigurationTarget.Global
        );
    }
  }

  vscode.commands.registerCommand('cros-ide.resetUserID', async () => {
    await metricsConfig.generateValidUserId();
  });
}

const trackingIdTesting = 'UA-221509619-1';
const trackingIdReal = 'UA-221509619-2';

const optionsGA = {
  hostname: 'www.google-analytics.com',
  path: '/collect',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
};

// Exhaustive list of feature groups.
type FeatureGroup = 'codesearch' | 'device' | 'lint' | 'package' | 'misc';

// Fields common to InteractiveEvent and BackgroundEvent.
interface EventBase {
  // Describes the feature group this event belongs to.
  group: FeatureGroup;
  // Describes an operation the extension has just run.
  // You can optional add a prefix with a colon to group actions in the same feature set.
  // Examples:
  //   "select target board"
  //   "device: connect to device via VNC"
  action: string;
  // Label is an optional string that describes the operation.
  label?: string;
  // Value is an optional number that describes the operation.
  value?: number;
}

// Describes an event triggered by an explicit user action, such as VSCode command invocation.
interface InteractiveEvent extends EventBase {
  category: 'interactive';
}

// Describes an event triggered implicitly in the background, such as lint computation.
interface BackgroundEvent extends EventBase {
  category: 'background';
}

// Describes an error event.
interface ErrorEvent {
  category: 'error';
  group: FeatureGroup;
  description: string;
}

type Event = InteractiveEvent | BackgroundEvent | ErrorEvent;

export class Analytics {
  private constructor(
    private readonly trackingId: string,
    private readonly userId: string | null
  ) {}

  // Constructor cannot be async.
  static async create(): Promise<Analytics> {
    const uid = await metricsConfig.getOrGenerateValidUserId();
    // Send metrics to testing-purpose Google Analytics property to avoid polluting
    // user data when debugging the extension for development.
    const tid =
      extensionMode === vscode.ExtensionMode.Production
        ? trackingIdReal
        : trackingIdTesting;
    return new Analytics(tid, uid);
  }

  /**
   * Creates query from event for Google Analytics measurement protocol, see
   * https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide
   *
   * See go/cros-ide-metrics for the memo on what values are assigned to GA parameters.
   */
  private eventToQuery(event: Event, gitRepo: string | undefined): string {
    if (!this.userId) {
      throw new Error(
        'BUG: Cannot build a query for an external user; check shouldSend() first'
      );
    }

    const data: Record<string, string | number> = {
      v: '1',
      tid: this.trackingId,
      cid: this.userId,
      // Document: Git repository info.
      dh: 'cros',
      dp: '/' + (gitRepo ?? 'unknown'),
      dt: gitRepo ?? 'unknown',
      // User agent: OS + VSCode version.
      ua: `${os.type()}-${vscode.env.appName}-${vscode.version}`,
      // Custom dimensions.
      cd1: os.type(),
      cd2: vscode.env.appName,
      cd3: vscode.version,
      cd4: extensionVersion ?? 'unknown',
      cd5: event.group,
    };

    if (event.category === 'error') {
      Object.assign(data, {
        t: 'exception',
        exd: `${event.group}: ${event.description}`,
      });
    } else {
      Object.assign(data, {
        t: 'event',
        ec: event.category,
        ea: `${event.group}: ${event.action}`,
      });
      if (event.label !== undefined) {
        data.el = event.label;
      }
      if (event.value !== undefined) {
        data.ev = event.value;
      }
    }

    return queryString.stringify(data);
  }

  /**
   * Decides if we should upload metrics.
   */
  private shouldSend(): boolean {
    return (
      // The extension should have been activated for production or development.
      // Note that we use a different tracking ID in the development mode.
      (extensionMode === vscode.ExtensionMode.Production ||
        extensionMode === vscode.ExtensionMode.Development) &&
      // User ID should be available.
      !!this.userId &&
      // User should have accepted to collect metrics.
      ideUtil.getConfigRoot().get<boolean>('metrics.collectMetrics', false)
    );
  }

  private getCurrentGitRepo(): string | undefined {
    const editor = vscode.window.activeTextEditor;
    if (editor) {
      return editor.document.fileName;
    }
    const folders = vscode.workspace.workspaceFolders;
    if (folders && folders.length >= 1) {
      return folders[0].uri.fsPath;
    }
    return undefined;
  }

  /**
   * Send event as query. Does not wait for its response.
   */
  send(event: Event, options = optionsGA) {
    if (!this.shouldSend()) {
      return;
    }

    const filePath = this.getCurrentGitRepo();
    const gitRepo = filePath
      ? metricsUtils.getGitRepoName(filePath)
      : undefined;
    const query = this.eventToQuery(event, gitRepo);
    console.debug(
      `sending query ${query} to GA ${this.trackingId} property with uid ${this.userId}`
    );

    const req = https.request(options, res => {
      console.debug(`Sent request, status code = ${res.statusCode}`);
      const body: Buffer[] = [];
      res.on('data', (chunk: Buffer) => {
        body.push(chunk);
      });
      res.on('end', () => {
        const resString = Buffer.concat(body).toString();
        console.debug(`Sent request, response = ${resString}`);
      });
    });

    req.on('error', error => {
      console.error(error);
    });

    req.write(query);
    req.end();
  }
}

let analytics: Promise<Analytics> | null;
export function send(event: Event) {
  if (!analytics) {
    analytics = Analytics.create();
  }
  analytics.then(a => a.send(event));
}
