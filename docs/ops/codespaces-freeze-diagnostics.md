# Codespaces freeze diagnostics

This note supports a diagnostic-only investigation into Codespaces freezes or very slow startup. It does **not** disable, remove, or override any VS Code extension, and it does not change Codespaces defaults, secrets, runtime behavior, or application code.

## Run the probe manually

From the repository root inside the affected Codespace, run:

```bash
bash tools/diagnostics/codespaces_freeze_probe.sh
```

The script writes a local report under the temporary diagnostics directory:

```text
/tmp/glow-codespaces-freeze-diagnostics/codespaces-freeze-probe-YYYYMMDD-HHMMSS.txt
```

The script avoids network calls, package installs, repo-file writes, user-setting changes, and extension changes.

## What the report captures

Review the report sections for:

- Timestamp, working directory, system, git, disk, memory, and process context.
- Redacted presence of relevant environment keys; values are reported only as set/empty and redacted.
- Whether the `code` CLI is available and whether `code --list-extensions --show-versions` completed.
- Installed VS Code extensions and extension directories under common VS Code server paths.
- OpenAI-related matches from extension IDs, extension directory names, or repo recommendations.
- Repo-level VS Code recommendation and devcontainer customization snippets, if present.
- Codespaces/devcontainer config files present in the repo.
- Recent VS Code server log directory names, without dumping large logs by default.

## Interpreting OpenAI-related findings

OpenAI-related matches are correlation evidence only. They can show that an OpenAI, ChatGPT, GPT, or Codex-related extension is installed, present on disk, or recommended by repo configuration, but they do not prove root cause by themselves.

If a freeze or slowdown happens at the same time an OpenAI-related extension is installed or activated, attach the redacted report to the investigation and compare it with a report from a healthy Codespace when possible.

## Secret handling

Do not paste raw secrets into issues, PR comments, chat, or external tools. The probe redacts sensitive environment values, but operators should still review the report before sharing it.

## Next steps after evidence review

A future remediation PR may remove, disable, or override auto-installed extensions only after the PO reviews diagnostic evidence. This diagnostic PR intentionally does not change extension recommendations or auto-install behavior.
