#!/usr/bin/env bash
# Diagnostic-only Codespaces startup/extension probe.
# Safe posture: no network calls, no installs, no extension changes, no settings writes.

set -u

repo_root="$(pwd)"
timestamp="$(date -u +%Y%m%d-%H%M%S 2>/dev/null || date +%Y%m%d-%H%M%S)"
out_dir="${TMPDIR:-/tmp}/glow-codespaces-freeze-diagnostics"
report="${out_dir}/codespaces-freeze-probe-${timestamp}.txt"

mkdir -p "${out_dir}" || {
  printf 'ERROR: could not create output directory: %s\n' "${out_dir}" >&2
  exit 1
}
: > "${report}" || {
  printf 'ERROR: could not write report: %s\n' "${report}" >&2
  exit 1
}

exec 3>&1
exec >> "${report}" 2>&1

append() {
  printf '%s\n' "$*"
}

section() {
  append ""
  append "## $*"
}

run_section() {
  section "$1"
  shift
  append "\$ $*"
  if "$@" >> "${report}" 2>&1; then
    append "[exit=0]"
  else
    status=$?
    append "[exit=${status}]"
  fi
}

run_optional() {
  section "$1"
  shift
  if command -v "$1" >/dev/null 2>&1; then
    append "\$ $*"
    if "$@" >> "${report}" 2>&1; then
      append "[exit=0]"
    else
      status=$?
      append "[exit=${status}]"
    fi
  else
    append "$1: not available"
  fi
}

run_with_timeout() {
  section "$1"
  shift
  if command -v timeout >/dev/null 2>&1; then
    append "\$ timeout 15s $*"
    if timeout 15s "$@" >> "${report}" 2>&1; then
      append "[exit=0]"
    else
      status=$?
      append "[exit=${status}]"
    fi
  else
    append "timeout: not available; running without timeout"
    append "\$ $*"
    if "$@" >> "${report}" 2>&1; then
      append "[exit=0]"
    else
      status=$?
      append "[exit=${status}]"
    fi
  fi
}

redact_sensitive_stream() {
  sed -E \
    -e 's#https?://[^[:space:]]+#REDACTED_URL#g' \
    -e 's#([A-Za-z0-9_]*(KEY|TOKEN|SECRET|PASSWORD|DATABASE_URL|DB_|GEO_API_KEY|HD_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL|AUTH|BEARER|URL)[A-Za-z0-9_]*[=:])[^[:space:]]+#\1REDACTED#g'
}

redacted_env_presence() {
  env | LC_ALL=C sort | awk -F= '
    function relevant(k) {
      return k ~ /(GLOW|HD|HDAPI|GEO|SAFE_MODE|ALLOW_NETWORK|APP_ENV|DEV_SAMPLER_URL|CODESPACE|DEVCONTAINER|VSCODE|KEY|TOKEN|SECRET|PASSWORD|DATABASE_URL|DB_|AUTH|BEARER|URL)/
    }
    relevant($1) {
      state = (length($2) > 0) ? "SET" : "EMPTY"
      print $1 "=" state ":REDACTED"
    }
  '
}

repo_file_presence() {
  for path in \
    ".devcontainer/devcontainer.json" \
    ".vscode/extensions.json" \
    ".vscode/settings.json" \
    "devcontainer.json"
  do
    if [ -e "${path}" ]; then
      printf 'present: %s\n' "${path}"
    else
      printf 'absent: %s\n' "${path}"
    fi
  done
  if [ -d ".github/codespaces" ]; then
    find .github/codespaces -maxdepth 2 -type f -print | LC_ALL=C sort
  else
    printf 'absent: .github/codespaces/\n'
  fi
}

repo_extension_recommendations() {
  for path in ".vscode/extensions.json" ".devcontainer/devcontainer.json" "devcontainer.json"; do
    if [ -f "${path}" ]; then
      printf -- '--- %s ---\n' "${path}"
      awk '
        /extensions|recommendations|unwantedRecommendations|customizations|vscode|openai|OpenAI|chatgpt|ChatGPT/ { print }
      ' "${path}" | redact_sensitive_stream
    fi
  done
}

extension_dirs() {
  for dir in \
    "${HOME:-}/.vscode-server/extensions" \
    "${HOME:-}/.vscode-server-insiders/extensions" \
    "${HOME:-}/.vscode-remote/extensions" \
    "${HOME:-}/.vscode/extensions" \
    "/workspaces/.codespaces/.persistedshare/extensions"
  do
    if [ -n "${dir}" ] && [ -d "${dir}" ]; then
      printf -- '--- %s ---\n' "${dir}"
      find "${dir}" -maxdepth 1 -mindepth 1 -type d -printf '%f\n' 2>/dev/null | LC_ALL=C sort | sed -n '1,200p'
    else
      printf 'absent: %s\n' "${dir}"
    fi
  done
}

openai_matches() {
  {
    if command -v code >/dev/null 2>&1; then
      if command -v timeout >/dev/null 2>&1; then
        timeout 15s code --list-extensions --show-versions 2>/dev/null || true
      else
        code --list-extensions --show-versions 2>/dev/null || true
      fi
    fi
    for dir in \
      "${HOME:-}/.vscode-server/extensions" \
      "${HOME:-}/.vscode-server-insiders/extensions" \
      "${HOME:-}/.vscode-remote/extensions" \
      "${HOME:-}/.vscode/extensions" \
      "/workspaces/.codespaces/.persistedshare/extensions"
    do
      [ -d "${dir}" ] && find "${dir}" -maxdepth 1 -mindepth 1 -type d -printf '%f\n' 2>/dev/null
    done
    repo_extension_recommendations
  } | LC_ALL=C grep -Ei 'openai|chatgpt|gpt|codex' | LC_ALL=C sort -u || true
}

vscode_log_dirs() {
  for dir in \
    "${HOME:-}/.vscode-server/data/logs" \
    "${HOME:-}/.vscode-server-insiders/data/logs" \
    "${HOME:-}/.vscode-remote/data/logs"
  do
    if [ -d "${dir}" ]; then
      printf -- '--- %s ---\n' "${dir}"
      find "${dir}" -maxdepth 2 -type d -printf '%TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null | LC_ALL=C sort | tail -50
    else
      printf 'absent: %s\n' "${dir}"
    fi
  done
}

append "# Codespaces Freeze Probe"
  append "Generated UTC: $(date -u '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || date)"
  append "Report path: ${report}"
  append "Safety: diagnostic only; no network calls, installs, settings changes, or extension changes."

  section "Header"
  append "Current working directory: ${repo_root}"
  append "User: $(id -un 2>/dev/null || printf 'unknown')"
  append "Hostname: $(hostname 2>/dev/null || printf 'unknown')"

  run_section "System" uname -a
  run_optional "OS release" cat /etc/os-release

  section "Git"
  if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    git branch --show-current 2>&1 || true
    git rev-parse HEAD 2>&1 || true
    git status --short --branch 2>&1 || true
  else
    append "git repo: unavailable"
  fi

  run_optional "Disk usage" df -h
  run_optional "Memory usage" free -h

  section "Process snapshot"
  if command -v ps >/dev/null 2>&1; then
    append "Top by CPU:"
    ps -eo pid,ppid,pcpu,pmem,comm --sort=-pcpu 2>/dev/null | sed -n '1,16p'
    append ""
    append "Top by memory:"
    ps -eo pid,ppid,pcpu,pmem,comm --sort=-pmem 2>/dev/null | sed -n '1,16p'
  else
    append "ps: not available"
  fi

  section "Relevant environment presence (values redacted)"
  redacted_env_presence

  section "VS Code CLI status"
  if command -v code >/dev/null 2>&1; then
    append "code CLI: available ($(command -v code))"
    run_with_timeout "VS Code CLI version" code --version
    run_with_timeout "Installed VS Code extensions" code --list-extensions --show-versions
  else
    append "code CLI: not available"
  fi

  section "Extension directory scan"
  extension_dirs

  section "OpenAI-related extension matches"
  openai_matches

  section "Repo extension recommendations"
  repo_extension_recommendations

  section "Devcontainer/Codespaces config presence"
  repo_file_presence

  section "Recent VS Code server log directories"
  vscode_log_dirs

  section "Interpretation notes"
  append "- OpenAI-related matches show extension IDs, directory names, or repo recommendations containing openai/chatgpt/gpt/codex."
  append "- A match is correlation evidence only; it does not prove root cause."
  append "- Share this report only after confirming it contains no raw secrets. Do not paste secrets into issues, PR comments, or chat."

printf 'Codespaces freeze diagnostic report written to: %s\n' "${report}" >&3
