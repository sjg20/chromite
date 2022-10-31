// Copyright 2022 The ChromiumOS Authors
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as metrics from '../features/metrics/metrics';

/**
 * Manages UI elements showing task status: two status bar items, which are created here,
 * and `cros-ide-status` view, which is defined in `package.json`.
 *
 * @returns `StatusManager` which allows other packages to create tasks with a status.
 */
export function activate(context: vscode.ExtensionContext): StatusManager {
  const showIdeStatusCommand = 'cros-ide.showIdeStatus';
  context.subscriptions.push(
    vscode.commands.registerCommand(showIdeStatusCommand, () => {
      void vscode.commands.executeCommand('cros-ide-status.focus');
      metrics.send({
        category: 'interactive',
        group: 'idestatus',
        action: 'show ide status',
      });
    })
  );

  const statusBarItem = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Right
  );
  statusBarItem.command = showIdeStatusCommand;
  statusBarItem.show();

  const progressItem = vscode.window.createStatusBarItem(
    vscode.StatusBarAlignment.Left
  );
  progressItem.command = 'cros-ide-status.focus';

  context.subscriptions.push(statusBarItem, progressItem);

  const statusManager = new StatusManagerImpl();

  const statusBarHandler = new StatusBarHandler(statusBarItem, progressItem);
  statusManager.onChange(statusBarHandler.refresh.bind(statusBarHandler));

  const statusTreeData = new StatusTreeData();
  statusManager.onChange(statusTreeData.refresh.bind(statusTreeData));
  context.subscriptions.push(
    vscode.window.registerTreeDataProvider('cros-ide-status', statusTreeData)
  );

  return statusManager;
}

export enum TaskStatus {
  OK,
  ERROR,
  RUNNING,
}

function getIcon(ts: TaskStatus): string {
  switch (ts) {
    case TaskStatus.OK:
      return 'check';
    case TaskStatus.ERROR:
      return 'error';
    case TaskStatus.RUNNING:
      return 'sync~spin';
  }
}

export type TaskName = string;

export interface TaskData {
  status: TaskStatus;

  /**
   * Command to be executed when the task is clicked in the UI. It can, for instance,
   * open a UI panel with logs.
   */
  command?: vscode.Command;
}

/**
 * Reports the status of background tasks indicating if the IDE works well or not.
 * It is meant for continuously running background tasks, which should not overuse popups.
 *
 * The status is shown in an abbreviated for in the status bar. Clicking on the status bar item
 * takes the user to a longer view, with a detailed view of all available tasks.
 *
 * Tasks are identified by a human-readable `TaskName`, which is display in various UI locations.
 */
export interface StatusManager {
  setTask(taskName: TaskName, taskData: TaskData): void;
  deleteTask(taskName: TaskName): void;
  setStatus(taskName: TaskName, status: TaskStatus): void;
}

type ChangeHandler = (arg: StatusManagerImpl) => void;

class StatusManagerImpl implements StatusManager {
  private tasks = new Map<TaskName, TaskData>();
  private handlers: ChangeHandler[] = [];

  setTask(taskName: TaskName, taskData: TaskData) {
    this.tasks.set(taskName, taskData);
    this.handleChange();
  }

  deleteTask(taskName: TaskName) {
    this.tasks.delete(taskName);
    this.handleChange();
  }

  setStatus(taskName: TaskName, status: TaskStatus) {
    const data = this.tasks.get(taskName);
    this.tasks.set(taskName, {...data, status});
  }

  getTasks(): TaskName[] {
    return Array.from(this.tasks.keys());
  }

  getTaskData(taskName: TaskName): TaskData | undefined {
    return this.tasks.get(taskName);
  }

  private get(status: TaskStatus): TaskName[] {
    const taskNames = [];
    for (const [id, data] of this.tasks) {
      if (data.status === status) {
        taskNames.push(id);
      }
    }
    return taskNames;
  }

  getErrorTasks(): TaskName[] {
    return this.get(TaskStatus.ERROR);
  }

  getRunningTasks(): TaskName[] {
    return this.get(TaskStatus.RUNNING);
  }

  onChange(handler: ChangeHandler) {
    this.handlers.push(handler);
    handler(this);
  }

  handleChange() {
    for (const handler of this.handlers) {
      handler(this);
    }
  }
}

class StatusBarHandler {
  constructor(
    private readonly statusBarItem: vscode.StatusBarItem,
    private readonly progressItem: vscode.StatusBarItem
  ) {}

  /**
   * Adjusts appearance of the status bar items based on status of tasks.
   *
   * The background of the main status bar item is determined by the presence of errors.
   *
   * If there are running tasks, then they are shown as a separate item
   * with a spinner icon.
   */
  refresh(statusManagerImpl: StatusManagerImpl) {
    const errorTasks = statusManagerImpl.getErrorTasks();
    if (errorTasks.length) {
      this.statusBarItem.text = `$(${getIcon(TaskStatus.ERROR)}) CrOS IDE`;
      this.statusBarItem.backgroundColor = new vscode.ThemeColor(
        'statusBarItem.errorBackground'
      );
      this.statusBarItem.tooltip = `Errors: ${errorTasks.sort().join(', ')}`;
    } else {
      this.statusBarItem.text = `$(${getIcon(TaskStatus.OK)}) CrOS IDE`;
      this.statusBarItem.backgroundColor = undefined;
      this.statusBarItem.tooltip = 'No Problems';
    }

    const runningTasks = statusManagerImpl.getRunningTasks();
    if (runningTasks.length) {
      const icon = getIcon(TaskStatus.RUNNING);
      const list = runningTasks.sort().join(', ');
      this.progressItem.text = `$(${icon}) Running ${list}...`;
      this.progressItem.show();
    } else {
      this.progressItem.hide();
    }
  }
}

class StatusTreeData implements vscode.TreeDataProvider<TaskName> {
  private statusManagerImpl?: StatusManagerImpl;

  private onDidChangeTreeDataEmitter = new vscode.EventEmitter<
    TaskName | undefined | null | void
  >();
  readonly onDidChangeTreeData = this.onDidChangeTreeDataEmitter.event;

  getTreeItem(element: TaskName): vscode.TreeItem | Thenable<vscode.TreeItem> {
    const statusManagerImp = this.statusManagerImpl!;
    const taskData = statusManagerImp.getTaskData(element)!;
    return new TaskTreeItem(element, taskData.status, taskData.command);
  }

  getChildren(_element?: TaskName): vscode.ProviderResult<TaskName[]> {
    return this.statusManagerImpl!.getTasks();
  }

  refresh(statusManagerImpl: StatusManagerImpl): void {
    this.statusManagerImpl = statusManagerImpl;
    this.onDidChangeTreeDataEmitter.fire();
  }
}

class TaskTreeItem extends vscode.TreeItem {
  constructor(
    readonly title: string,
    status: TaskStatus,
    command?: vscode.Command
  ) {
    super(title, vscode.TreeItemCollapsibleState.None);
    this.iconPath = new vscode.ThemeIcon(getIcon(status));
    this.command = command;
  }
}

export const TEST_ONLY = {
  StatusManagerImpl,
  StatusBarHandler,
  StatusTreeData,
};
