#!/usr/bin/env bash
# HDE-CRD-0002 WU-OPS-01: production identity read and binding-presence record (v1.0).
# Task record: docs/ephemeral/HDE-CRD-0002-WU-OPS-01-ops-task-v1.0.md
#
# Reads GET /internal/version on the HD Engine production base URL (PF07), compares the
# release_id it reports with the candidate's, and records the presence of seven named
# production variables as the operator observes them. It records no response body, no
# header value and no variable value. It writes only into WORK_DIR, an absent or empty
# directory outside the repository. It changes nothing in production or in the repository.
#
# Run from the root of a clean checkout of amthorn78/glow-hdengine-v2 main:
#   EXECUTOR=PO WORK_DIR=/abs/dir ATTEMPT=1 bash HDE-CRD-0002-WU-OPS-01-run-v1.0.sh
#   EXECUTOR=PO-delegated-agent DELEGATION_REF='<ref>' WORK_DIR=/abs/dir ATTEMPT=1 bash ...
# Rehearsal, never evidence: add REHEARSAL_BASE_URL=http://127.0.0.1:<port>
#   and optionally REHEARSAL_DELAYS_S="0 1 1".
#
# Exit status: 0 PASS; 2 FAIL_BEHAVIOR, the service answered without the candidate's
# release_id; 5 FAIL_BEHAVIOR, the service did not answer (the rollback condition);
# 6 FAIL_BEHAVIOR, identity reported and a variable UNSET; 3 TOOLING_BLOCKED; 4 FAIL_TOOLING.
set -euo pipefail
export LC_ALL=C LANG=C TZ=UTC

readonly PROD_BASE_URL="https://glow-hdengine-v2-production.up.railway.app"
readonly EXPECTED_RELEASE_ID="77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e"
readonly EXPECTED_VERSION="1.3.0"
readonly EXPECTED_BUILT_AT="2026-08-24T18:04:49Z"
readonly EXPECTED_MEMBERS=45
readonly CANDIDATE_FLOOR="f508dcf"    # WU-DOC-01's last merge (#700); the candidate includes it
readonly PROD_DELAYS_S="0 300 600"    # read 1 at once, read 2 after 5 min, read 3 after 10 more
readonly VARIABLES="APP_ENV SAFE_MODE ALLOW_NETWORK HD_API_BASE_URL HD_API_KEY GEO_API_KEY DATABASE_URL"
readonly EVIDENCE_REL="audit/ops/hde-crd-0002/wu-ops-01"

utc() { date -u +%Y-%m-%dT%H:%M:%SZ; }
LOG=""
log() { printf '%s\n' "$*"; if [ -n "$LOG" ]; then printf '%s\n' "$*" >> "$LOG"; fi; }
STARTED="$(utc)"

blocked() {  # preflight failure: TOOLING_BLOCKED, nothing read
  log "PREFLIGHT_FAIL: $1"
  log "RESULT: TOOLING_BLOCKED (exit 3)"
  if [ -n "$LOG" ]; then
    printf 'classification\tTOOLING_BLOCKED\nexit_status\t3\nreason\t%s\n' "$1" > "$WORK_DIR/result.attempt${ATTEMPT}.txt"
    ( cd "$WORK_DIR" && sha256sum -- *.attempt"${ATTEMPT}".* > "SHA256SUMS.attempt${ATTEMPT}" )
  fi
  exit 3
}
trap 'rc=$?; case "$rc" in 0|2|3|4|5|6) ;; *) log "RESULT: FAIL_TOOLING (exit 4; a step failed with status $rc)"; exit 4;; esac' EXIT

# --- Parameters and mode ---------------------------------------------------
ATTEMPT="${ATTEMPT:-}"
WORK_DIR="${WORK_DIR:-}"
EXECUTOR="${EXECUTOR:-}"
DELEGATION_REF="${DELEGATION_REF:-}"
case "$ATTEMPT" in ''|*[!0-9]*|0*) echo "PREFLIGHT_FAIL: ATTEMPT must be a positive integer"; exit 3;; esac
case "$WORK_DIR" in /*) ;; *) echo "PREFLIGHT_FAIL: WORK_DIR must be an absolute path"; exit 3;; esac

if [ -n "${REHEARSAL_BASE_URL:-}" ]; then
  MODE="REHEARSAL"
  case "$REHEARSAL_BASE_URL" in
    http://127.0.0.1:[0-9]*) ;;
    *) echo "PREFLIGHT_FAIL: REHEARSAL_BASE_URL must be http://127.0.0.1:<port>"; exit 3;;
  esac
  BASE_URL="$REHEARSAL_BASE_URL"; PROTO="=http"; DELAYS="${REHEARSAL_DELAYS_S:-$PROD_DELAYS_S}"
else
  MODE="EXECUTION"
  [ -z "${REHEARSAL_DELAYS_S:-}" ] || { echo "PREFLIGHT_FAIL: REHEARSAL_DELAYS_S is for rehearsal only"; exit 3; }
  BASE_URL="$PROD_BASE_URL"; PROTO="=https"; DELAYS="$PROD_DELAYS_S"
fi

# --- Preflight ---------------------------------------------------------------
REPO="$(pwd -P)"
case "$WORK_DIR/" in "$REPO"/*) echo "PREFLIGHT_FAIL: WORK_DIR is inside the repository"; exit 3;; esac
if [ -e "$WORK_DIR" ] && [ -n "$(ls -A "$WORK_DIR")" ]; then echo "PREFLIGHT_FAIL: WORK_DIR is not empty"; exit 3; fi
mkdir -p "$WORK_DIR"
LOG="$WORK_DIR/run.attempt${ATTEMPT}.log"
: > "$LOG"
log "WU-OPS-01 run v1.0 mode=$MODE attempt=$ATTEMPT started_at=$STARTED"
SCRIPT_SHA256="$(sha256sum "$0" | cut -d' ' -f1)"
log "script_sha256=$SCRIPT_SHA256"

[ "${BASH_VERSINFO[0]}" -ge 4 ] || blocked "bash 4 or later is required"
for tool in curl python3 git sha256sum; do
  command -v "$tool" > /dev/null 2>&1 || blocked "$tool is not on PATH"
done
case "$EXECUTOR" in
  PO) DELEGATION_REF="not applicable (the Product Owner executes personally)";;
  PO-delegated-agent)
    [ -n "$DELEGATION_REF" ] || blocked "DELEGATION_REF is required for a delegated executor"
    [ "${#DELEGATION_REF}" -le 256 ] || blocked "DELEGATION_REF is longer than 256 characters"
    case "$DELEGATION_REF" in *[!\ -~]*) blocked "DELEGATION_REF must be printable ASCII on one line";; esac;;
  *) blocked "EXECUTOR must be PO or PO-delegated-agent";;
esac
[ "$(git rev-parse --show-toplevel 2> /dev/null || true)" = "$REPO" ] || blocked "not run from a repository root"
HEAD_SHA="$(git rev-parse HEAD)"
git cat-file -e "${CANDIDATE_FLOOR}^{commit}" 2> /dev/null || blocked "commit $CANDIDATE_FLOOR is not in this checkout"
git merge-base --is-ancestor "$CANDIDATE_FLOOR" HEAD || blocked "HEAD $HEAD_SHA does not contain $CANDIDATE_FLOOR"
[ -z "$(git status --porcelain)" ] || blocked "the working tree is not clean"
for existing in "$EVIDENCE_REL"/*.attempt"${ATTEMPT}".*; do
  [ -e "$existing" ] && blocked "attempt $ATTEMPT evidence already exists at $existing"
done
MANIFEST_FACTS="$(python3 -I -c '
import hashlib, json, sys
raw = open("catalog/manifest.json", "rb").read()
doc = json.loads(raw)
print(hashlib.sha256(raw).hexdigest(), doc["version"], doc["built_at_utc"], len(doc["files"]))
')" || blocked "catalog/manifest.json is unreadable"
read -r M_RID M_VERSION M_BUILT M_COUNT <<< "$MANIFEST_FACTS"
log "candidate head=$HEAD_SHA manifest release_id=$M_RID version=$M_VERSION built_at_utc=$M_BUILT members=$M_COUNT"
[ "$M_RID" = "$EXPECTED_RELEASE_ID" ] && [ "$M_VERSION" = "$EXPECTED_VERSION" ] \
  && [ "$M_BUILT" = "$EXPECTED_BUILT_AT" ] && [ "$M_COUNT" = "$EXPECTED_MEMBERS" ] \
  || blocked "the checkout's release differs from the task's pinned candidate; return to OPS-10"
{
  printf 'candidate_head\t%s\n' "$HEAD_SHA"
  printf 'contains_commit\t%s\n' "$CANDIDATE_FLOOR"
  printf 'manifest_sha256\t%s\n' "$M_RID"
  printf 'manifest_version\t%s\n' "$M_VERSION"
  printf 'manifest_built_at_utc\t%s\n' "$M_BUILT"
  printf 'manifest_members\t%s\n' "$M_COUNT"
  printf 'pinned_release_id\t%s\n' "$EXPECTED_RELEASE_ID"
  printf 'pinned_equal\tyes\n'
} > "$WORK_DIR/expected_identity.attempt${ATTEMPT}.txt"
log "PREFLIGHT: PASS"

# --- Binding presence (operator observation; names only) ----------------------
PRESENCE="$WORK_DIR/binding_presence.attempt${ATTEMPT}.tsv"
printf 'variable\tpresence\tobserved_at_utc\n' > "$PRESENCE"
log "Binding presence: for each name, look at the variables of Railway project ample-illumination,"
log "service glow-hdengine-v2, environment production. Answer SET if a variable with exactly that"
log "name is listed, UNSET if it is not, NOT_OBSERVED if you cannot see the list. Do not reveal or type a value."
PRESENCE_STATE="ALL_SET"
for name in $VARIABLES; do
  answer=""
  for _try in 1 2 3; do
    printf '%s: ' "$name"
    IFS= read -r answer || answer=""
    case "$answer" in SET|UNSET|NOT_OBSERVED) break;; esac
    log "invalid answer for $name (not recorded); answer SET, UNSET or NOT_OBSERVED"
    answer=""
  done
  [ -n "$answer" ] || answer="NOT_OBSERVED"
  printf '%s\t%s\t%s\n' "$name" "$answer" "$(utc)" >> "$PRESENCE"
  log "presence: $name is $answer"
  case "$answer" in
    UNSET) [ "$PRESENCE_STATE" = "NOT_OBSERVED" ] || PRESENCE_STATE="SOME_UNSET";;
    NOT_OBSERVED) PRESENCE_STATE="NOT_OBSERVED";;
  esac
done

# --- Identity reads ------------------------------------------------------------
READS="$WORK_DIR/identity_reads.attempt${ATTEMPT}.tsv"
printf 'read\tread_at_utc\thttp_status\tcurl_exit\tclass\trelease_id_reported\tbody_keys\tbody_sha256\tbody_bytes\n' > "$READS"
BODY="$(mktemp "${TMPDIR:-/tmp}/wu-ops-01-body.XXXXXX")"
n=0; READ_STATE="NO_ANSWER"
for delay in $DELAYS; do
  if [ "$delay" -gt 0 ]; then log "waiting ${delay}s before the next read"; sleep "$delay"; fi
  n=$((n + 1)); at="$(utc)"; : > "$BODY"
  set +e
  status="$(curl --silent --show-error --proto "$PROTO" --max-time 30 --header 'Accept: application/json' \
    --output "$BODY" --write-out '%{http_code}' "$BASE_URL/internal/version" 2> "$BODY.err")"
  cexit=$?
  set -e
  [ -s "$BODY.err" ] && log "read $n curl: $(head -c 200 "$BODY.err" | tr '\n' ' ')"
  facts="$(python3 -I - "$BODY" << 'PY'
import hashlib, json, re, sys
raw = open(sys.argv[1], "rb").read()
rid, keys = "-", "-"
try:
    doc = json.loads(raw.decode("utf-8"))
except (UnicodeDecodeError, ValueError):
    doc = None
if isinstance(doc, dict):
    keys = ",".join(doc) or "-"
    value = doc.get("release_id")
    if isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value):
        rid = value
print(rid, keys, hashlib.sha256(raw).hexdigest(), len(raw))
PY
)"
  rm -f "$BODY.err"; : > "$BODY"
  read -r rid keys bsha blen <<< "$facts"
  if [ "$cexit" -ne 0 ] || [ "$status" = "000" ]; then class="NO_RESPONSE"
  elif [ "$status" = "502" ] || [ "$status" = "503" ] || [ "$status" = "504" ]; then class="GATEWAY_NO_ANSWER"
  elif [ "$status" = "200" ] && [ "$rid" = "$EXPECTED_RELEASE_ID" ]; then class="MATCH"
  elif [ "$status" = "200" ] && [ "$rid" != "-" ]; then class="OTHER_RELEASE"
  else class="NO_IDENTITY"
  fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$n" "$at" "$status" "$cexit" "$class" "$rid" "$keys" "$bsha" "$blen" >> "$READS"
  log "read $n at $at: http_status=$status curl_exit=$cexit class=$class release_id=$rid"
  case "$class" in
    MATCH) READ_STATE="MATCH"; break;;
    OTHER_RELEASE|NO_IDENTITY) READ_STATE="ANSWERED_NO_MATCH";;
  esac
done
rm -f "$BODY"

# --- Classification ------------------------------------------------------------
if [ "$READ_STATE" = "NO_ANSWER" ]; then CLASS="FAIL_BEHAVIOR"; RC=5; WHY="the service did not answer any read: rollback condition met; stop, the Product Owner acts"
elif [ "$READ_STATE" = "ANSWERED_NO_MATCH" ]; then CLASS="FAIL_BEHAVIOR"; RC=2; WHY="the service answered without the candidate's release_id; stop, the Product Owner decides"
elif [ "$PRESENCE_STATE" = "NOT_OBSERVED" ]; then CLASS="TOOLING_BLOCKED"; RC=3; WHY="identity matched; a variable's presence was not observed"
elif [ "$PRESENCE_STATE" = "SOME_UNSET" ]; then CLASS="FAIL_BEHAVIOR"; RC=6; WHY="identity matched; a named variable is UNSET (environment not yet closed)"
else CLASS="PASS"; RC=0; WHY="identity matched; all seven variables SET (environment validated)"
fi
FINISHED="$(utc)"
{
  printf 'task\tHDE-CRD-0002 WU-OPS-01\n'
  printf 'mode\t%s\n' "$MODE"
  printf 'attempt\t%s\n' "$ATTEMPT"
  printf 'classification\t%s\n' "$CLASS"
  printf 'exit_status\t%s\n' "$RC"
  printf 'reason\t%s\n' "$WHY"
  printf 'identity_reads\t%s (reads=%s)\n' "$READ_STATE" "$n"
  printf 'binding_presence\t%s\n' "$PRESENCE_STATE"
  printf 'base_url\t%s\n' "$BASE_URL"
  printf 'endpoint\tGET /internal/version, no credential header\n'
  printf 'executor\t%s\n' "$EXECUTOR"
  printf 'delegation_ref\t%s\n' "$DELEGATION_REF"
  printf 'candidate_head\t%s\n' "$HEAD_SHA"
  printf 'script_sha256\t%s\n' "$SCRIPT_SHA256"
  printf 'started_at_utc\t%s\n' "$STARTED"
  printf 'finished_at_utc\t%s\n' "$FINISHED"
  printf 'nonclaims\tno QA PASS, Live QA, acceptance, deployment by this task, closure or PF09/PF30 movement; presence only, values not verified\n'
} > "$WORK_DIR/result.attempt${ATTEMPT}.txt"
log "RESULT: $CLASS (exit $RC): $WHY"

# --- Secret scan, then checksum ledger ---------------------------------------------
if grep -l -i -E 'bearer[[:space:]]+[a-z0-9]|postgres(ql)?://|api[_-]?key[[:space:]]*[=:]|hd-api-key[[:space:]]*:|hd-geocode-key[[:space:]]*:' "$WORK_DIR"/* > "$WORK_DIR/.scan" 2> /dev/null; then
  echo "SECRET_SCAN_HIT in: $(sed 's|.*/||' "$WORK_DIR/.scan" | tr '\n' ' ')"
  rm -f -- "$WORK_DIR"/* "$WORK_DIR/.scan"
  echo "RESULT: FAIL_TOOLING (exit 4): every output file was deleted; nothing may be copied into the repository"
  exit 4
fi
rm -f "$WORK_DIR/.scan"
if [ "$MODE" = "REHEARSAL" ]; then log "REHEARSAL output: not evidence; do not copy it into $EVIDENCE_REL"; fi
log "finished_at_utc=$FINISHED; checksum ledger follows as the last write"
( cd "$WORK_DIR" && sha256sum -- *.attempt"${ATTEMPT}".* > "SHA256SUMS.attempt${ATTEMPT}" )
echo "ledger written: $WORK_DIR/SHA256SUMS.attempt${ATTEMPT}"
exit "$RC"
