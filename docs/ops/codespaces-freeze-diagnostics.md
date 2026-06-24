# Codespaces freeze diagnostics

This note supports a diagnostic-only investigation into Codespaces freezes or very slow startup. It does **not** disable, remove, or override any VS Code extension, and it does not change Codespaces defaults, secrets, runtime behavior, or application code.

## Current investigation scope

The current PR target is the OpenAI/Codex VCS VS Code extension startup path, not the Codex CLI as a product or runtime surface. Treat VS Code extension evidence, Codespaces extension activation, and devcontainer startup evidence as separate from normal `codex` command-line behavior.

Earlier repository discussion referenced `openai.chatgpt` as a VS Code extension recommendation. The currently inspected repository configuration does **not** show an `openai.chatgpt` recommendation in `.devcontainer/devcontainer.json`; the devcontainer VS Code customizations contain an empty `settings` object and no extension recommendation list. If a diagnostic report still shows `openai.chatgpt` as installed or present on disk, treat that as user-level or existing Codespace state unless a repo recommendation is also captured in the same report.

The current repo startup issue is the `@openai/codex` CLI install path in `.devcontainer/devcontainer.json`. Investigate that startup/install behavior separately from any VS Code extension recommendation or activation question.

## Run the extension doctor manually

The current extension-focused doctor lives at:

```bash
bash .devcontainer/scripts/codespaces-extension-doctor.sh
```

Use this doctor when the investigation needs to distinguish repo devcontainer configuration, VS Code extension recommendation state, installed extension state, and OpenAI/Codex-related startup evidence. The doctor is diagnostic-only: it does not modify user settings, install or uninstall extensions, edit dotfiles, write secrets, or change repository startup configuration.

## Run the legacy freeze probe manually

The older probe remains available for broader Codespaces freeze context:

```bash
bash tools/diagnostics/codespaces_freeze_probe.sh
```

The script writes a local report under the temporary diagnostics directory:

```text
/tmp/glow-codespaces-freeze-diagnostics/codespaces-freeze-probe-YYYYMMDD-HHMMSS.txt
```

The legacy probe is diagnostic-only. It avoids network calls, package installs, repo-file writes, user-setting changes, extension changes, dotfile edits, and secret writes. Keep using it as supporting evidence only; it should not be treated as the remediation mechanism for VS Code extension or devcontainer startup issues.

## What the reports capture

Review the doctor and probe report sections for:

- Timestamp, working directory, system, git, disk, memory, and process context.
- Redacted presence of relevant environment keys; values are reported only as set/empty and redacted.
- Whether the `code` CLI is available and whether `code --list-extensions --show-versions` completed.
- Installed VS Code extensions and extension directories under common VS Code server paths.
- OpenAI-related matches from extension IDs, extension directory names, repo recommendations, or devcontainer startup configuration.
- Repo-level VS Code recommendation and devcontainer customization snippets, including `.devcontainer/devcontainer.json`, root `.devcontainer.json`, selectable `.devcontainer/**/devcontainer.json` files, `.vscode/settings.json`, `.vscode/extensions.json`, `*.code-workspace`, and `.devcontainer/**/post*` or `.devcontainer/**/install*` scripts when present.
- Repo script/config matches for `code --install-extension`, `code-insiders --install-extension`, extension install commands, or package install commands containing `openai`, `codex`, `vcs`, or `chatgpt`.
- Codespaces/devcontainer config files present in the repo.
- Recent VS Code server log directory names, without dumping large logs by default.

## Interpreting OpenAI-related findings

OpenAI-related matches are correlation evidence only. They can show that an OpenAI, ChatGPT, GPT, Codex, or VCS-related extension is installed, present on disk, or recommended by repo configuration, but they do not prove root cause by themselves.

For this investigation, keep these cases distinct:

- **VS Code extension target:** evidence about the OpenAI/Codex VCS VS Code extension, extension IDs, extension recommendations, and extension activation belongs to the current PR target.
- **Prior `openai.chatgpt` discussion:** prior discussion of `openai.chatgpt` was about a VS Code extension recommendation, but the current inspected config does not show that recommendation.
- **Devcontainer startup issue:** evidence about installing `@openai/codex` from `.devcontainer/devcontainer.json` belongs to the current Codespaces startup/install issue, not to a repo recommendation for `openai.chatgpt`.
- **Codex CLI behavior:** ordinary CLI behavior is out of scope unless the devcontainer startup install path is the evidence being inspected.

If a freeze or slowdown happens at the same time an OpenAI-related extension is installed or activated, attach the redacted report to the investigation and compare it with a report from a healthy Codespace when possible.

## Secret handling

Do not paste raw secrets into issues, PR comments, chat, or external tools. The doctor and the legacy probe redact sensitive environment values and sensitive-looking key/value snippets from inspected config lines, but operators should still review reports before sharing them.

Neither diagnostic script modifies user settings, extensions, dotfiles, or secrets. If either report shows a user setting, installed extension, dotfile path, or secret-like key, that entry is observational evidence only.

## Next steps after evidence review

Remediation should change extension recommendations only after diagnostic evidence review. The diagnostic scripts themselves remain safe to run and do not change extension recommendations, auto-install behavior, user settings, installed extensions, dotfiles, or secrets. Do not add `.vscode/extensions.json` or any repo-level host-placement setting for an OpenAI/Codex VCS extension unless the diagnostic report identifies the exact extension ID first. If an exact ID is discovered later, record that ID in the diagnostic report or follow-up documentation before making a recommendation or placement change.

Host placement is intentionally not pinned in this initial repository PR. Do not add a `remote.extensionKind` entry to `.vscode/settings.json` yet because the exact VCS extension ID was not discoverable in the inspected environment, the `code` CLI was unavailable during inspection, and hardcoding a guessed extension ID could break browser Codespaces or desktop VS Code attached to Codespaces.

If later validation discovers the exact extension ID and proves a host-placement mismatch, propose a separate small patch that records the exact extension ID, observed current host behavior, desired host kind, affected client mode, and rollback instruction to remove the single `remote.extensionKind` setting.

If startup evidence points instead to the `@openai/codex` CLI install path in `.devcontainer/devcontainer.json`, scope remediation to that devcontainer startup path and document it as a Codespaces startup/install fix rather than as a Codex CLI product change or an `openai.chatgpt` extension recommendation change.
