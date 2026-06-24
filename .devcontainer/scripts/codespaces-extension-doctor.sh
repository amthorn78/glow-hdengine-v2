#!/usr/bin/env bash
set -uo pipefail

# Read-only Codespaces / VS Code extension diagnostics.
# This script writes nothing intentionally: all output goes to stdout/stderr.

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd -P)"
TIMEOUT_SECONDS="${DOCTOR_TIMEOUT_SECONDS:-15}"
PERSISTED_SHARE="/workspaces/.codespaces/.persistedshare"
DOTFILES_DIR="${PERSISTED_SHARE}/dotfiles"

warns=()
fails=()

section() { printf '\n## %s\n' "$1"; }
kv() { printf '%-34s %s\n' "$1:" "$2"; }
add_warn() { warns+=("$1"); }
add_fail() { fails+=("$1"); }
have() { command -v "$1" >/dev/null 2>&1; }

is_sensitive_name() {
  case "$1" in
    *TOKEN*|*token*|*SECRET*|*secret*|*KEY*|*key*|*PASSWORD*|*password*|*PASS*|*pass*|*AUTH*|*auth*|*CREDENTIAL*|*credential*|*COOKIE*|*cookie*|*BASE_URL*|*base_url*) return 0 ;;
    *) return 1 ;;
  esac
}

redact_value() {
  local name="$1" value="${2-}"
  if is_sensitive_name "$name"; then
    if [ -n "$value" ]; then printf 'REDACTED'; else printf 'UNSET'; fi
  else
    if [ -n "$value" ]; then printf '%s' "$value"; else printf 'UNSET'; fi
  fi
}

run_timeout() {
  local seconds="$1"; shift
  if have timeout; then
    timeout "$seconds" "$@"
  else
    "$@"
  fi
}

redact_stream() {
  sed -E "s/([A-Za-z_]*(TOKEN|SECRET|KEY|PASSWORD|PASS|AUTH|CREDENTIAL|COOKIE|BASE_URL)[A-Za-z_]*[[:space:]]*[:=][[:space:]]*)[^[:space:]\"',}]+/\\1REDACTED/gI"
}

print_file_if_present() {
  local file="$1"
  if [ -f "$file" ]; then
    printf -- '--- %s ---\n' "$file"
    sed -n '1,220p' "$file"
  else
    printf '%s not found\n' "$file"
  fi
}

json_extract_devcontainer() {
  local file="$1"
  if ! [ -f "$file" ]; then
    printf 'devcontainer.json not found\n'
    return 0
  fi
  if have python3 || have python; then
    local py=python3
    have python3 || py=python
    "$py" - "$file" <<'PY'
import json, sys
from pathlib import Path
p = Path(sys.argv[1])
try:
    data = json.loads(p.read_text(encoding='utf-8'))
except Exception as exc:
    print(f"Unable to parse {p}: {exc}")
    raise SystemExit(0)

def sensitive(k):
    u = str(k).upper()
    return any(x in u for x in ("TOKEN", "SECRET", "KEY", "PASSWORD", "PASS", "AUTH", "CREDENTIAL", "COOKIE", "BASE_URL"))

def walk_env(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            name = f"{prefix}.{k}" if prefix else str(k)
            if isinstance(v, (dict, list)):
                yield from walk_env(v, name)
            elif sensitive(k):
                yield name

print(f"image: {data.get('image', 'UNSET')}")
for key in ("postCreateCommand", "postStartCommand", "postAttachCommand", "initializeCommand", "onCreateCommand", "updateContentCommand", "waitFor"):
    if key in data:
        print(f"hook {key}: {data[key]}")
print("customizations.vscode snippet:")
print(json.dumps(data.get("customizations", {}).get("vscode", {}), sort_keys=True, indent=2))
keys = sorted(set(walk_env({"remoteEnv": data.get("remoteEnv", {}), "containerEnv": data.get("containerEnv", {})})))
if keys:
    print("sensitive env key names (values redacted):")
    for k in keys:
        print(f"- {k}=REDACTED")
else:
    print("sensitive env key names (values redacted): none found")
PY
  else
    sed -n '/"image"/p;/Command"/p;/customizations"/,+25p;/Env"/,+20p' "$file"
  fi
}

json_extract_settings() {
  local file="$1"
  if ! [ -f "$file" ]; then
    printf '.vscode/settings.json not found\n'
    return 0
  fi
  if have python3 || have python; then
    local py=python3
    have python3 || py=python
    "$py" - "$file" <<'PY'
import json, sys
from pathlib import Path
p = Path(sys.argv[1])
try:
    data = json.loads(p.read_text(encoding='utf-8'))
except Exception as exc:
    print(f"Unable to parse {p}: {exc}")
    raise SystemExit(0)
for k in sorted(data):
    lk = k.lower()
    if "watch" in lk or "search" in lk or "remote.extensionkind" in lk or "extensionkind" in lk:
        print(f"{k}: {json.dumps(data[k], sort_keys=True)}")
PY
  else
    sed -n '/watch/p;/search/p;/extensionKind/p;/remote.extensionKind/p' "$file"
  fi
}

section "Basic host facts"
kv "utc_datetime" "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
kv "user" "$(id -un 2>/dev/null || printf unknown)"
kv "host" "$(hostname 2>/dev/null || printf unknown)"
kv "repo_root" "$ROOT"
kv "uname" "$(uname -a 2>/dev/null || printf unavailable)"
section "OS release"
print_file_if_present /etc/os-release

section "Codespaces / client environment"
for name in CODESPACES GITHUB_CODESPACE_TOKEN GITHUB_TOKEN GH_TOKEN CODESPACE_NAME CODESPACE_VSCODE_FOLDER VSCODE_AGENT_FOLDER VSCODE_CWD REMOTE_CONTAINERS DOCKER_BUILDKIT DEVCONTAINER; do
  value="${!name-}"
  kv "$name" "$(redact_value "$name" "$value")"
done

section "code CLI"
if have code; then
  kv "code_path" "$(command -v code)"
  printf '\n### code --list-extensions --show-versions\n'
  if ! run_timeout "$TIMEOUT_SECONDS" code --list-extensions --show-versions; then
    add_warn "code extension list unavailable or timed out"
  fi
  printf '\n### filtered extension matches (codex|openai|vcs|chatgpt)\n'
  if ! run_timeout "$TIMEOUT_SECONDS" code --list-extensions --show-versions 2>/dev/null | sed -n '/codex\|openai\|vcs\|chatgpt/Ip'; then
    add_warn "filtered extension matches unavailable"
  fi
  printf '\n### code --status\n'
  if ! run_timeout "$TIMEOUT_SECONDS" code --status; then
    add_warn "code --status unavailable or timed out"
  fi
else
  kv "code_path" "UNAVAILABLE"
  add_warn "code is unavailable"
  add_warn "exact extension ID/version cannot be discovered"
fi

describe_tool() {
  local tool="$1"
  if have "$tool"; then
    kv "$tool" "$(command -v "$tool")"
  else
    kv "$tool" "UNAVAILABLE"
    add_warn "$tool is unavailable"
  fi
}

section "Tool availability"
for tool in git gh curl jq ps ssh gpg dbus-daemon secret-tool xdg-open node npm python python3 timeout; do
  describe_tool "$tool"
done

section "Certificate availability"
cert_found=0
if [ -f /etc/ssl/certs/ca-certificates.crt ]; then
  kv "ca-certificates bundle" "/etc/ssl/certs/ca-certificates.crt"
  cert_found=1
else
  kv "ca-certificates bundle" "UNAVAILABLE"
fi
if [ -d /etc/ssl/certs ]; then
  cert_count="$(find /etc/ssl/certs -type f \( -name '*.crt' -o -name '*.pem' \) 2>/dev/null | wc -l | tr -d ' ')"
  kv "certificate path /etc/ssl/certs" "exists (${cert_count} cert files)"
  [ "${cert_count:-0}" -gt 0 ] && cert_found=1
else
  kv "certificate path /etc/ssl/certs" "UNAVAILABLE"
fi
if have dpkg-query && dpkg-query -W -f='${Status}' ca-certificates 2>/dev/null | grep -q 'install ok installed'; then
  kv "ca-certificates package" "installed"
  cert_found=1
else
  kv "ca-certificates package" "UNAVAILABLE"
fi
[ "$cert_found" -eq 0 ] && add_warn "ca-certificates bundle/package and common certificate paths are unavailable"

section "Devcontainer files found"
find "$ROOT/.devcontainer" -maxdepth 4 -type f -print 2>/dev/null | sort || true

section "devcontainer.json summary"
json_extract_devcontainer "$ROOT/.devcontainer/devcontainer.json"

section ".vscode/settings.json watcher/search/remote extension-kind summary"
json_extract_settings "$ROOT/.vscode/settings.json"

section "Large watched roots"
for rel in .git/objects .git/subtree-cache node_modules .venv venv __pycache__ .pytest_cache .mypy_cache .ruff_cache dist build coverage artifacts audit/qa; do
  if [ -e "$ROOT/$rel" ]; then kv "$rel" "exists"; else kv "$rel" "absent"; fi
done

section "Codespaces persisted share / dotfiles"
if [ -e "$PERSISTED_SHARE" ]; then
  kv "$PERSISTED_SHARE" "exists"
else
  kv "$PERSISTED_SHARE" "absent"
  add_warn "persisted share is unavailable"
fi
if [ -d "$DOTFILES_DIR" ]; then
  kv "$DOTFILES_DIR" "exists"
  find "$DOTFILES_DIR" -maxdepth 4 -type f -print 2>/dev/null | sort || true
  printf '\n### read-only dotfiles matches\n'
  find "$DOTFILES_DIR" -maxdepth 6 -type f -print0 2>/dev/null | xargs -0 sed -n '/code .*install-extension/Ip;/codex/Ip;/openai/Ip;/vcs/Ip;/settings\.json/Ip;/extensions\.json/Ip' 2>/dev/null | redact_stream || true
  if find "$DOTFILES_DIR" -maxdepth 6 -type f -print0 2>/dev/null | xargs -0 sed -n '/code .*install-extension/Ip;/codex/Ip' 2>/dev/null | sed -n '1q' | grep -q .; then
    add_warn "off-repo persistence contains extension/Codex-related dotfiles matches"
  fi
else
  kv "$DOTFILES_DIR" "absent"
fi

repo_scan_has() {
  local pattern="$1"
  find "$ROOT/.devcontainer" "$ROOT/.vscode" -type f \( -name '*.json' -o -name '*.sh' \) ! -path "$ROOT/.devcontainer/scripts/codespaces-extension-doctor.sh" -print0 2>/dev/null | \
    xargs -0 grep -IilE "$pattern" >/dev/null 2>&1
}

devcontainer_scan_has() {
  local pattern="$1"
  find "$ROOT/.devcontainer" -type f ! -path "$ROOT/.devcontainer/scripts/codespaces-extension-doctor.sh" -print0 2>/dev/null | \
    xargs -0 grep -IilE "$pattern" >/dev/null 2>&1
}

section "Repo safety scans"
repo_install_loop=0
repo_forced_vcs=0
repo_prints_secrets=0
repo_codex_reinstall=0
watcher_exclusions=0
unsafe_repo_persistence=0

if repo_scan_has "code .*install-extension|codex|openai|vcs|chatgpt"; then
  repo_install_loop=1
fi
if repo_scan_has "code .*install-extension.*vcs"; then
  repo_forced_vcs=1
fi
if repo_scan_has "echo .*[$].*TOKEN|printf .*[$].*TOKEN|echo .*[$].*SECRET|printf .*[$].*SECRET|set -x"; then
  repo_prints_secrets=1
fi
if devcontainer_scan_has "post.*codex|codex.*install|npm .*install.*codex|pip .*install.*codex"; then
  repo_codex_reinstall=1
fi
if [ -f "$ROOT/.vscode/settings.json" ] && grep -Eiq '"files\.watcherExclude"|"search\.exclude"' "$ROOT/.vscode/settings.json"; then
  watcher_exclusions=1
fi
if repo_scan_has "persistedshare|[.]codespaces|dotfiles"; then
  unsafe_repo_persistence=1
fi

kv "repo Codex/extension install loop scan" "$repo_install_loop"
kv "repo forced VCS extension install scan" "$repo_forced_vcs"
kv "repo secret-print scan" "$repo_prints_secrets"
kv "startup Codex reinstall scan" "$repo_codex_reinstall"
kv "watcher/search exclusions configured" "$watcher_exclusions"
kv "unsafe repo persistence scan" "$unsafe_repo_persistence"

[ "$repo_install_loop" -eq 1 ] && add_fail "repo config forces repeated extension/Codex installs"
[ "$repo_forced_vcs" -eq 1 ] && add_fail "repo config forces VCS extension installs"
[ "$repo_prints_secrets" -eq 1 ] && add_fail "repo config appears able to print raw secrets"
[ "$repo_codex_reinstall" -eq 1 ] && add_fail "startup hooks reinstall Codex tooling by default"
[ "$watcher_exclusions" -eq 0 ] && add_warn "watcher/search exclusions were not found"
[ "$unsafe_repo_persistence" -eq 1 ] && add_warn "off-repo persistence is referenced by repo config"

section "Final summary"
if [ "${#fails[@]}" -gt 0 ]; then
  printf 'FAIL\n'
  for f in "${fails[@]}"; do printf -- '- FAIL: %s\n' "$f"; done
elif [ "$repo_install_loop" -eq 0 ] && [ "$repo_forced_vcs" -eq 0 ] && [ "$watcher_exclusions" -eq 1 ] && [ "$unsafe_repo_persistence" -eq 0 ]; then
  printf 'PASS\n'
else
  printf 'WARN\n'
fi
for w in "${warns[@]}"; do printf -- '- WARN: %s\n' "$w"; done

exit 0
