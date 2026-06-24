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

append() {
  printf '%s\n' "$*" >> "${report}"
}

section() {
  append ""
  append "## $*"
}

redact_sensitive_stream() {
  sed -E \
    -e 's#https?://[^[:space:]"'"'"'<>]+#REDACTED_URL#g' \
    -e 's#("[^"]*(KEY|TOKEN|SECRET|PASSWORD|DATABASE_URL|DB_|GEO_API_KEY|HD_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL|AUTH|BEARER|URL|APIKEY|API_KEY)[^"]*"[[:space:]]*:[[:space:]]*")[^"]*"#\1REDACTED"#gI' \
    -e 's#([A-Za-z0-9_.-]*(KEY|TOKEN|SECRET|PASSWORD|DATABASE_URL|DB_|GEO_API_KEY|HD_API_KEY|HD_API_BASE_URL|HDAPI_BASE_URL|AUTH|BEARER|URL|APIKEY|API_KEY)[A-Za-z0-9_.-]*[=:])["'"'"']?[^[:space:]"'"'"']+["'"'"']?#\1REDACTED#gI'
}

append_redacted() {
  redact_sensitive_stream >> "${report}"
}

run_command() {
  section "$1"
  shift
  append "\$ $*"
  output="$({ "$@"; } 2>&1)"
  status=$?
  printf '%s\n' "${output}" | append_redacted
  append "[exit=${status}]"
}

run_optional() {
  section "$1"
  shift
  if command -v "$1" >/dev/null 2>&1; then
    append "\$ $*"
    output="$({ "$@"; } 2>&1)"
    status=$?
    printf '%s\n' "${output}" | append_redacted
    append "[exit=${status}]"
  else
    append "$1: not available"
  fi
}

run_with_timeout() {
  section "$1"
  shift
  if command -v timeout >/dev/null 2>&1; then
    append "\$ timeout 15s $*"
    output="$({ timeout 15s "$@"; } 2>&1)"
    status=$?
  else
    append "timeout: not available; running without timeout"
    append "\$ $*"
    output="$({ "$@"; } 2>&1)"
    status=$?
  fi
  printf '%s\n' "${output}" | append_redacted
  append "[exit=${status}]"
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

repo_config_files() {
  for path in \
    ".devcontainer/devcontainer.json" \
    ".devcontainer.json" \
    ".vscode/extensions.json" \
    ".vscode/settings.json"
  do
    [ -f "${path}" ] && printf '%s\n' "${path}"
  done
  [ -d ".devcontainer" ] && find .devcontainer -mindepth 2 -type f \
    \( -name devcontainer.json -o -name 'post*' -o -name 'install*' \) -print 2>/dev/null
  find . -maxdepth 2 -name '*.code-workspace' -type f -print 2>/dev/null
  [ -d ".github/codespaces" ] && find .github/codespaces -maxdepth 2 -type f -print 2>/dev/null
}

repo_file_presence() {
  for path in \
    ".devcontainer/devcontainer.json" \
    ".devcontainer.json" \
    ".vscode/extensions.json" \
    ".vscode/settings.json"
  do
    if [ -e "${path}" ]; then
      printf 'present: %s\n' "${path}"
    else
      printf 'absent: %s\n' "${path}"
    fi
  done
  if [ -d ".devcontainer" ]; then
    find .devcontainer -mindepth 2 -type f \
      \( -name devcontainer.json -o -name 'post*' -o -name 'install*' \) -print 2>/dev/null | LC_ALL=C sort | sed 's/^/present devcontainer scanned: /'
  else
    printf 'absent: .devcontainer/ selectable configs and scripts\n'
  fi
  find . -maxdepth 2 -name '*.code-workspace' -type f -print 2>/dev/null | LC_ALL=C sort | sed 's/^/present workspace: /'
  if [ -d ".github/codespaces" ]; then
    find .github/codespaces -maxdepth 2 -type f -print 2>/dev/null | LC_ALL=C sort | sed 's/^/present: /'
  else
    printf 'absent: .github/codespaces/\n'
  fi
}

repo_extension_recommendations() {
  repo_config_files | LC_ALL=C sort -u | while IFS= read -r path; do
    printf -- '--- %s ---\n' "${path}"
    awk '
      /extensions|recommendations|unwantedRecommendations|customizations|vscode|openai|OpenAI|chatgpt|ChatGPT|codex|Codex|vcs|VCS|apiKey|API_KEY|apikey/ { print }
    ' "${path}"
  done
}

repo_extension_install_commands() {
  repo_config_files | LC_ALL=C sort -u | while IFS= read -r path; do
    matches="$({
      grep -En 'code(-insiders)?[[:space:]]+--install-extension' "${path}" || true
      grep -Ein -- '--install-extension.*(openai|codex|vcs|chatgpt)|(openai|codex|vcs|chatgpt).*--install-extension' "${path}" || true
    } | LC_ALL=C sort -u)"
    if [ -n "${matches}" ]; then
      printf -- '--- %s ---\n' "${path}"
      printf '%s\n' "${matches}"
    fi
  done
}

extension_roots() {
  for dir in \
    "${HOME:-}/.vscode-server/extensions" \
    "${HOME:-}/.vscode-server-insiders/extensions" \
    "${HOME:-}/.vscode-remote/extensions" \
    "${HOME:-}/.vscode/extensions" \
    "/home/vscode/.vscode-server/extensions" \
    "/home/vscode/.vscode-server-insiders/extensions" \
    "/home/vscode/.vscode-remote/extensions" \
    "/home/vscode/.vscode/extensions" \
    "/workspaces/.codespaces/.persistedshare/extensions"
  do
    [ -n "${dir}" ] && printf '%s\n' "${dir}"
  done | awk '!seen[$0]++'
}

extension_dirs() {
  extension_roots | while IFS= read -r dir; do
    if [ -d "${dir}" ]; then
      printf -- '--- %s ---\n' "${dir}"
      find "${dir}" -maxdepth 1 -mindepth 1 -type d -printf '%f\n' 2>/dev/null | LC_ALL=C sort | sed -n '1,200p'
    else
      printf 'absent: %s\n' "${dir}"
    fi
  done
}

installed_extensions() {
  if command -v code >/dev/null 2>&1; then
    if command -v timeout >/dev/null 2>&1; then
      timeout 15s code --list-extensions --show-versions 2>/dev/null || true
    else
      code --list-extensions --show-versions 2>/dev/null || true
    fi
  fi
}

openai_matches() {
  {
    installed_extensions
    extension_roots | while IFS= read -r dir; do
      [ -d "${dir}" ] && find "${dir}" -maxdepth 1 -mindepth 1 -type d -printf '%f\n' 2>/dev/null
    done
    repo_extension_recommendations
  } | LC_ALL=C grep -Ei 'openai|chatgpt|gpt|codex' | LC_ALL=C sort -u || true
}

vscode_log_dirs() {
  for dir in \
    "${HOME:-}/.vscode-server/data/logs" \
    "${HOME:-}/.vscode-server-insiders/data/logs" \
    "${HOME:-}/.vscode-remote/data/logs" \
    "/home/vscode/.vscode-server/data/logs" \
    "/home/vscode/.vscode-server-insiders/data/logs" \
    "/home/vscode/.vscode-remote/data/logs"
  do
    if [ -d "${dir}" ]; then
      printf -- '--- %s ---\n' "${dir}"
      find "${dir}" -maxdepth 2 -type d -printf '%TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null | LC_ALL=C sort | tail -50
    else
      printf 'absent: %s\n' "${dir}"
    fi
  done | awk '!seen[$0]++'
}

append "# Codespaces Freeze Probe"
append "Generated UTC: $(date -u '+%Y-%m-%dT%H:%M:%SZ' 2>/dev/null || date)"
append "Report path: ${report}"
append "Safety: diagnostic only; no network calls, installs, settings changes, or extension changes."

section "Header"
append "Current working directory: ${repo_root}"
append "User: $(id -un 2>/dev/null || printf 'unknown')"
append "Hostname: $(hostname 2>/dev/null || printf 'unknown')"

run_command "System" uname -a
run_optional "OS release" cat /etc/os-release

section "Git"
if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  {
    git branch --show-current 2>&1 || true
    git rev-parse HEAD 2>&1 || true
    git status --short --branch 2>&1 || true
  } | append_redacted
else
  append "git repo: unavailable"
fi

run_optional "Disk usage" df -h
run_optional "Memory usage" free -h

section "Process snapshot"
if command -v ps >/dev/null 2>&1; then
  append "Top by CPU:"
  ps -eo pid,ppid,pcpu,pmem,comm --sort=-pcpu 2>/dev/null | sed -n '1,16p' | append_redacted
  append ""
  append "Top by memory:"
  ps -eo pid,ppid,pcpu,pmem,comm --sort=-pmem 2>/dev/null | sed -n '1,16p' | append_redacted
else
  append "ps: not available"
fi

section "Relevant environment presence (values redacted)"
redacted_env_presence >> "${report}"

section "VS Code CLI status"
if command -v code >/dev/null 2>&1; then
  append "code CLI: available ($(command -v code))"
  run_with_timeout "VS Code CLI version" code --version
  run_with_timeout "Installed VS Code extensions" code --list-extensions --show-versions
else
  append "code CLI: not available"
fi

section "Extension directory scan"
extension_dirs | append_redacted

section "OpenAI-related extension matches"
openai_matches | append_redacted

section "Repo extension recommendations"
repo_extension_recommendations | append_redacted

section "Repo extension install commands"
install_command_matches="$(repo_extension_install_commands)"
if [ -n "${install_command_matches}" ]; then
  printf '%s\n' "${install_command_matches}" | append_redacted
else
  append "No repo extension install commands matched code/code-insiders --install-extension or openai/codex/vcs/chatgpt install-extension patterns in scanned locations."
fi

section "Devcontainer/Codespaces config presence"
repo_file_presence | append_redacted

section "Recent VS Code server log directories"
vscode_log_dirs | append_redacted

section "Interpretation notes"
append "- OpenAI-related matches show extension IDs, directory names, or repo recommendations containing openai/chatgpt/gpt/codex."
append "- Do not add or recommend a repo-level VS Code extension file or host-placement setting for the OpenAI/Codex VCS extension unless this report identifies the exact extension ID."
append "- A match is correlation evidence only; it does not prove root cause."
append "- Share this report only after confirming it contains no raw secrets. Do not paste secrets into issues, PR comments, or chat."

printf 'Codespaces freeze diagnostic report written to: %s\n' "${report}"
