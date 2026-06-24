import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  console.log('open-teams extension is now active');

  const disposable = vscode.commands.registerCommand('open-teams.start', () => {
    vscode.window.showInformationMessage(
      'Open Teams: Extension scaffold loaded. Ready to build!'
    );
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
