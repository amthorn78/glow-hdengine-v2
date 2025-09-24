#!/usr/bin/env bash
# Card closeout: env check → tests → sanity (if present) → source bundle → audit (if present) → commit+push → report
set -euo pipefail

# ---- args -------------------------------------------------------------------
CARD=""
FAST=0
MAX_MB="${MAX_MB:-5}"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --card) CARD="${2:-}"; shift 2;;
    --fast) FAST=1; shift 1;;
    --max-mb) MAX_MB="${2:-5}"; shift 2;;
    *) echo "usage: bash scripts/card_close.sh --card \"CARD-ID\" [--fast] [--max-mb N]" >&2; exit 2;;
  esac
done
[[ -n "${CARD}" ]] || { echo "error: --card is required"; exit 2; }

# ---- setup ------------------------------------------------------------------
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUTDIR="audit"; mkdir -p "$OUTDIR"

BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'unknown')"
SHORT_SHA_BEFORE="$(git rev-parse --short HEAD 2>/dev/null || echo 'unknown')"
STATUS_BEFORE="$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')"

ENV_STATUS="SKIPPED"
TEST_STATUS="SKIPPED"
SANITY_STATUS="SKIPPED"
SANITY_OPTS=()
[[ $FAST -eq 1 ]] && SANITY_OPTS+=(--fast)

BUNDLE_PATH=""
MANIFEST_PATH=""
AUDIT_BUNDLE="(none)"

# ---- step 1: env check ------------------------------------------------------
if [[ -f scripts/ensure_env.py ]]; then
  set +e
  python scripts/ensure_env.py >/tmp/_env_out.txt 2>&1
  rc=$?; set -e
  if [[ $rc -eq 0 ]]; then ENV_STATUS="OK"; else ENV_STATUS="FAIL"; fi
else
  ENV_STATUS="MISSING"
fi

# ---- step 2: tests -----------------------------------------------------------
if command -v pytest >/dev/null 2>&1 && [[ -d tests ]]; then
  set +e
  pytest -q >/tmp/_pytest_out.txt 2>&1
  rc=$?; set -e
  if [[ $rc -eq 0 ]]; then TEST_STATUS="OK"; else TEST_STATUS="FAIL"; fi
else
  TEST_STATUS="MISSING"
fi

# ---- step 3: sanity (optional) ----------------------------------------------
if [[ -x ./make_sanity.sh ]]; then
  set +e
  ./make_sanity.sh "${SANITY_OPTS[@]}" >/tmp/_sanity_out.txt 2>&1
  rc=$?; set -e
  if [[ $rc -eq 0 ]]; then SANITY_STATUS="OK"; else SANITY_STATUS="FAIL"; fi
elif [[ -x scripts/make_sanity.sh ]]; then
  set +e
  bash scripts/make_sanity.sh "${SANITY_OPTS[@]}" >/tmp/_sanity_out.txt 2>&1
  rc=$?; set -e
  if [[ $rc -eq 0 ]]; then SANITY_STATUS="OK"; else SANITY_STATUS="FAIL"; fi
fi

# ---- step 4: source bundle (always) -----------------------------------------
if [[ -x scripts/make_source_bundle.sh ]]; then
  set +e
  BOUT="$(bash scripts/make_source_bundle.sh --card "${CARD}" --max-mb "${MAX_MB}" 2>/tmp/_bundle_err.txt)"
  rc=$?; set -e
  BUNDLE_PATH="$(printf '%s\n' "$BOUT" | sed -n 's/^\[bundle\] //p' | tail -n1)"
  MANIFEST_PATH="$(printf '%s\n' "$BOUT" | sed -n 's/^.*OUT=\(.*\)$/\1/p' | tail -n1)"
else
  echo "error: scripts/make_source_bundle.sh is missing or not executable" >&2
  exit 3
fi

# ---- step 5: heavy audit (optional) -----------------------------------------
if [[ -x ./make_audit.sh ]]; then
  set +e
  ./make_audit.sh >/tmp/_audit_out.txt 2>&1
  rc=$?; set -e
  latest="$(ls -1t audit_bundle_*.zip 2>/dev/null | head -n1 || true)"
  [[ -n "$latest" ]] && AUDIT_BUNDLE="$latest"
elif [[ -x scripts/make_audit.sh ]]; then
  set +e
  bash scripts/make_audit.sh >/tmp/_audit_out.txt 2>&1
  rc=$?; set -e
  latest="$(ls -1t audit_bundle_*.zip 2>/dev/null | head -n1 || true)"
  [[ -n "$latest" ]] && AUDIT_BUNDLE="$latest"
fi

# ---- step 6: commit & push (best-effort; never fails closeout) --------------
set +e
git add -A >/tmp/_git_add.txt 2>&1
git commit -m "${CARD}: closeout (env=${ENV_STATUS}, tests=${TEST_STATUS}, sanity=${SANITY_STATUS})" >/tmp/_git_commit.txt 2>&1
COMMIT_RC=$?
NEW_SHORT_SHA="$(git rev-parse --short HEAD 2>/dev/null || echo 'unknown')"
git push -u origin "$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "$BRANCH")" >/tmp/_git_push.txt 2>&1
PUSH_RC=$?
set -e
[[ $COMMIT_RC -eq 0 ]] || true
[[ $PUSH_RC -eq 0 ]] || true

STATUS_AFTER="$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')"

# ---- step 7: write closeout report ------------------------------------------
REPORT="${OUTDIR}/${CARD}_closeout_${STAMP}.md"
{
  echo "# Card Closeout — ${CARD}"
  echo
  echo "**Repo:** $(basename "$ROOT")  |  **Branch:** ${BRANCH}  |  **Commit(before):** ${SHORT_SHA_BEFORE}  |  **Commit(final):** ${NEW_SHORT_SHA}  |  **Dirty(before/after):** ${STATUS_BEFORE}/${STATUS_AFTER}"
  echo
  echo "## Gates"
  echo "- Env: \`${ENV_STATUS}\`"
  echo "- Tests: \`${TEST_STATUS}\`"
  echo "- Sanity: \`${SANITY_STATUS}\`"
  echo
  echo "## Deliverables"
  echo "- Source bundle: \`${BUNDLE_PATH}\`"
  echo "- Manifest: \`${MANIFEST_PATH}\`"
  echo "- Audit bundle (if any): \`${AUDIT_BUNDLE}\`"
  echo
  echo "## VCS"
  if [[ $COMMIT_RC -eq 0 ]]; then
    echo "- Commit: \`${NEW_SHORT_SHA}\` (message: \`${CARD}: closeout (env=${ENV_STATUS}, tests=${TEST_STATUS}, sanity=${SANITY_STATUS})\`)"
  else
    echo "- Commit: *(no changes or commit failed — see /tmp/_git_commit.txt)*"
  fi
  if [[ $PUSH_RC -eq 0 ]]; then
    echo "- Push: \`origin/${BRANCH}\` OK"
  else
    echo "- Push: *(failed or remote missing — see /tmp/_git_push.txt)*"
  fi
  echo
  echo "## Operator"
  echo "Run: \`bash scripts/card_close.sh --card \"${CARD}\"${FAST:+ --fast}\`"
} > "$REPORT"

echo "[closeout] $REPORT"
echo "[bundle]  $BUNDLE_PATH"
[[ -n "$MANIFEST_PATH" ]] && echo "[manifest] $MANIFEST_PATH"
[[ -n "$AUDIT_BUNDLE" ]] && echo "[audit]   $AUDIT_BUNDLE"
if [[ $COMMIT_RC -eq 0 ]]; then
  echo "[commit]  $NEW_SHORT_SHA"
else
  echo "[commit]  (none) — see /tmp/_git_commit.txt"
fi
if [[ $PUSH_RC -eq 0 ]]; then
  echo "[pushed]  origin/${BRANCH}"
else
  echo "[pushed]  (failed or missing remote) — see /tmp/_git_push.txt"
fi

# Always succeed; statuses above capture failures.
exit 0
