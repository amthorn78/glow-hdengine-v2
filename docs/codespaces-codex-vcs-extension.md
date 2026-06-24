# Codespaces Codex VCS extension support

## Scope

This repository supports the OpenAI/Codex VCS VS Code extension as the target VS Code integration for Codex VCS workflows in Codespaces. The repository-side goal is a clean startup environment with explicit support boundaries: the repo should not repeatedly install tools, should keep watcher pressure low, and should make user-level persistence visible without mutating it.

This is not a request to disable the plugin. If the extension is involved in startup or editor-health investigations, the solution is clean repo startup, reduced watcher pressure, and validated support boundaries rather than disabling the extension by default.

## What the repository does and does not install

- The repo does **not** install the Codex CLI by default.
- The repo does **not** install or reinstall the OpenAI/Codex VCS VS Code extension by default.
- The VCS extension may still be present because a user installed it manually, Settings Sync restored it, a dotfiles setup installed it, or an existing Codespace already had it on disk.
- The repo doctor can detect signs of user-level persistence, Settings Sync/dotfiles influence, and installed extension state when the VS Code `code` CLI is available, but it is read-only and will not modify those settings, files, extensions, or persisted shares.

## Supported client mode must come from validation evidence

Record supported client mode only after validation evidence has been captured with the doctor output and any follow-up QA notes. Supported modes are:

- Browser Codespaces.
- Desktop VS Code attached to Codespaces.
- Both browser Codespaces and desktop VS Code attached to Codespaces.

Do not infer support from expectation or local preference. If validation only covers one client mode, record only that mode as supported. If browser Codespaces or desktop VS Code attached to Codespaces remains unsupported after validation, state that explicitly in the validation note and in any issue/PR summary that relies on the evidence.

## Run the doctor

From the repository root, run:

```bash
bash .devcontainer/scripts/codespaces-extension-doctor.sh
```

The script is diagnostic-only. It writes no repo files intentionally, avoids extension changes, and prints a redacted report to stdout/stderr.

## Interpret the output

### Extension ID/version

When the `code` CLI is available, use the `code --list-extensions --show-versions` section and the filtered `codex|openai|vcs|chatgpt` section to identify the exact extension ID and version.

The exact extension ID/version must come from doctor output or equivalent validation evidence. Do not guess the extension ID, do not assume a marketplace identifier, and do not write docs or repo settings that depend on an ID until the ID/version has been captured.

If the extension appears in installed-extension output but not in repo recommendations or startup scans, treat it as user-level or existing Codespace state unless other evidence says otherwise.

### Missing `code` CLI

If the `code CLI` section reports `code_path: UNAVAILABLE`, the doctor cannot discover exact installed extension IDs or versions from `code --list-extensions --show-versions`. That is a diagnostic limitation, not proof that the extension is absent.

In that case, record that exact ID/version discovery is unavailable for that run and validate again in a client/session where the `code` CLI is present before making extension-ID-specific claims.

### Off-repo persistence

The `Codespaces persisted share / dotfiles` section reports whether common Codespaces persisted-share and dotfiles locations exist and prints redacted matches for extension-install or Codex/OpenAI/VCS-related lines. These findings can explain why an extension returns after rebuilds even when the repo does not install it.

The doctor may warn about off-repo persistence, but it does not edit persisted share content, dotfiles, Settings Sync, user settings, or installed extensions. Remediation for off-repo persistence belongs to the user or environment owner, not to repo startup hooks.

### Watcher exclusion health

The `.vscode/settings.json watcher/search/remote extension-kind summary`, `Large watched roots`, and `Repo safety scans` sections show whether watcher/search exclusions are configured and whether large generated or cached directories exist.

A healthy repo posture has watcher/search exclusions configured for high-churn or large roots so VS Code and extensions have less filesystem pressure during startup. If `watcher/search exclusions configured` is `0`, treat that as a warning to improve repo settings rather than a reason to disable the VCS extension.

### Startup hook health

The `Repo safety scans` section reports whether repo devcontainer or VS Code configuration appears to force extension installs, force VCS extension installs, reinstall Codex tooling from startup hooks, print secrets, or reference off-repo persistence.

Healthy startup-hook posture means:

- `repo Codex/extension install loop scan` is `0`.
- `repo forced VCS extension install scan` is `0`.
- `startup Codex reinstall scan` is `0`.
- `repo secret-print scan` is `0`.
- `unsafe repo persistence scan` is `0` or is explained as a warning with no repo mutation.

If these scans fail, fix the repo startup/config behavior. Do not paper over repeated installs or excessive startup work by telling users to disable the extension.

## Recording validation

When recording a validation result, include:

- Date/time of the doctor run.
- Client mode tested: browser Codespaces, desktop VS Code attached to Codespaces, or both.
- Exact extension ID/version from the doctor output when available.
- Whether the `code` CLI was available.
- Whether off-repo persistence was observed.
- Watcher exclusion health.
- Startup hook health.
- Any unsupported client mode, stated explicitly after validation.

A concise validation statement should distinguish repo behavior from user-level state, for example: the repo does not install/reinstall the Codex CLI or VCS extension by default; the observed extension ID/version came from doctor output; and any persisted user-level install source was detected but not modified by the repo doctor.
