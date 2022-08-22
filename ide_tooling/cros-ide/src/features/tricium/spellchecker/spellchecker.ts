// Copyright 2022 The ChromiumOS Authors.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import * as vscode from 'vscode';
import * as chroot from '../../../services/chroot';
import * as bgTaskStatus from '../../../ui/bg_task_status';
import * as tricium from '../tricium';
import * as cipd from '../../../common/cipd';
import * as executor from './executor';

// Spellchecker demonstrates integration between Tricium's functions
// and CrOS IDE.
//
// If cros-ide.underDevelopment.triciumSpellchecker is not empty,
// then we use it as the path to the spellchecker and surface its findings
// in the IDE.

const STATUS_BAR_TASK_ID = 'Tricium';
const SHOW_LOG_COMMAND: vscode.Command = {
  command: 'cros-ide.showTriciumLog',
  title: 'Show Tricium Log',
};

/**
 * Activate should handle the errors instead of throwing them.
 * In particular, CIPD interaction is wrapped in try-catch block, which logs
 * an error and exits if the spellchecker cannot be installed.
 */
export async function activate(
  context: vscode.ExtensionContext,
  statusManager: bgTaskStatus.StatusManager,
  chrootService: chroot.ChrootService,
  cipdRepository: cipd.CipdRepository
) {
  const outputChannel = vscode.window.createOutputChannel('CrOS IDE: Tricium');
  context.subscriptions.push(
    vscode.commands.registerCommand(SHOW_LOG_COMMAND.command, () =>
      outputChannel.show()
    )
  );

  let triciumSpellchecker: string;
  try {
    triciumSpellchecker = await cipdRepository.ensureTriciumSpellchecker(
      outputChannel
    );
  } catch (err) {
    // TODO(b:217287367): send metrics
    outputChannel.append(`Could not download Tricium spellchecker: ${err}`);
    return;
  }

  const spellchecker = new Spellchecker(
    context,
    triciumSpellchecker,
    statusManager,
    chrootService,
    outputChannel
  );
  spellchecker.subscribeToDocumentChanges(context);

  // Action provider takes warning generated by Spellchecker and creates
  // code actions for them (clickable fixes).
  context.subscriptions.push(
    vscode.languages.registerCodeActionsProvider(
      {scheme: 'file'},
      new SpellcheckerActionProvider()
    )
  );
}

const DIAGNOSTIC_CODE = 'tricium-spellchecker';

class SpellcheckerDiagnostic extends vscode.Diagnostic {
  replacements: string[];

  constructor(range: vscode.Range, message: string) {
    super(range, message, vscode.DiagnosticSeverity.Information);
    this.code = DIAGNOSTIC_CODE;
    this.replacements = [];
  }
}

class Spellchecker {
  readonly diagnosticCollection: vscode.DiagnosticCollection;

  constructor(
    context: vscode.ExtensionContext,
    readonly toolPath: string,
    readonly statusManager: bgTaskStatus.StatusManager,
    readonly chrootService: chroot.ChrootService,
    readonly outputChannel: vscode.OutputChannel
  ) {
    this.diagnosticCollection =
      vscode.languages.createDiagnosticCollection('spellchecker');
    context.subscriptions.push(this.diagnosticCollection);
  }

  /** Attach spellchecker to editor events. */
  subscribeToDocumentChanges(context: vscode.ExtensionContext): void {
    if (vscode.window.activeTextEditor) {
      void this.refreshDiagnostics(vscode.window.activeTextEditor.document);
    }
    context.subscriptions.push(
      vscode.window.onDidChangeActiveTextEditor(editor => {
        if (editor) {
          void this.refreshDiagnostics(editor.document);
        }
      })
    );

    context.subscriptions.push(
      vscode.workspace.onDidChangeTextDocument(ev =>
        this.refreshDiagnostics(ev.document)
      )
    );

    context.subscriptions.push(
      vscode.workspace.onDidCloseTextDocument(doc => this.delete(doc.uri))
    );
  }

  /** Execute Tricium binary and refreshes diagnostics for the document. */
  private async refreshDiagnostics(doc: vscode.TextDocument): Promise<void> {
    if (doc.uri.scheme !== 'file') {
      return;
    }

    const sourceRoot = this.chrootService.source()?.root;
    if (!sourceRoot) {
      return;
    }

    // TODO(b:217287367): Cancel the operation if the active editor changes.
    const results = await executor.callSpellchecker(
      sourceRoot,
      doc.uri.fsPath,
      this.toolPath,
      this.outputChannel
    );

    if (results instanceof Error) {
      // TODO(ttylenda): send metrics
      this.setStatus(bgTaskStatus.TaskStatus.ERROR);
      return;
    }

    const diagnostics: vscode.Diagnostic[] = [];

    if (results.comments) {
      for (const comment of results.comments) {
        const range = Spellchecker.range(comment);
        if (!range) {
          continue;
        }
        const diagnostic = new SpellcheckerDiagnostic(range, comment.message);
        // We expect exactly one suggestion, but the keep the code flexible.
        if (comment.suggestions) {
          for (const s of comment.suggestions) {
            if (s.replacements) {
              for (const r of s.replacements) {
                diagnostic.replacements.push(r.replacement);
              }
            }
          }
        }
        diagnostics.push(diagnostic);
      }
    }

    this.diagnosticCollection.set(doc.uri, diagnostics);
    this.setStatus(bgTaskStatus.TaskStatus.OK);
  }

  private setStatus(status: bgTaskStatus.TaskStatus) {
    this.statusManager.setTask(STATUS_BAR_TASK_ID, {
      status,
      command: SHOW_LOG_COMMAND,
    });
  }

  /** Clear diagnostics for the specified uri. */
  private delete(uri: vscode.Uri) {
    this.diagnosticCollection.delete(uri);
  }

  private static range(comment: tricium.Comment): vscode.Range | undefined {
    if (!comment.startLine) {
      return undefined;
    }
    return new vscode.Range(
      comment.startLine - 1,
      comment.startChar,
      comment.endLine - 1,
      comment.endChar
    );
  }
}

/**
 * Adds suggested fixes to SpellcheckerDiagnostics.
 */
class SpellcheckerActionProvider implements vscode.CodeActionProvider {
  constructor() {}

  provideCodeActions(
    document: vscode.TextDocument,
    _range: vscode.Range | vscode.Selection,
    context: vscode.CodeActionContext,
    _token: vscode.CancellationToken
  ): vscode.ProviderResult<vscode.CodeAction[]> {
    return context.diagnostics
      .filter(diagnostic => diagnostic.code === DIAGNOSTIC_CODE)
      .flatMap(diagnostic =>
        this.createFix(document, diagnostic as SpellcheckerDiagnostic)
      );
  }

  private createFix(
    document: vscode.TextDocument,
    diagnostic: SpellcheckerDiagnostic
  ): vscode.CodeAction[] {
    const codeActions: vscode.CodeAction[] = [];
    for (const replacement of diagnostic.replacements) {
      const fix = new vscode.CodeAction(
        `Replace with: "${replacement}"`,
        vscode.CodeActionKind.QuickFix
      );
      fix.edit = new vscode.WorkspaceEdit();
      fix.edit.replace(document.uri, diagnostic.range, replacement);
      codeActions.push(fix);
    }
    return codeActions;
  }
}
