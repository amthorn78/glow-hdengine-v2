#!/usr/bin/env bash
# Card closeout: env check → tests → sanity (if present) → source bundle → audit (if present)
# → artifacts checksums → report → commit & push
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

SHORT_SHA="$(git rev-parse --short HEAD 2>/dev/null || echo 'unknown')"
BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'unknown')"
STATUS="$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')"

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
  python -m pytest -q >/tmp/_pytest_out.txt 2>&1
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
  # [bundle] line
  BUNDLE_PATH="$(printf '%s\n' "$BOUT" | sed -n 's/^\[bundle\] //p' | tail -n1)"
  # manifest line (FILES=.. OUT=...)
  MANIFEST_PATH="$(printf '%s\n' "$BOUT" | sed -n 's/^.*OUT=\(.*\)$/\1/p' | tail -n1)"
else
  echo "error: scripts/make_source_bundle.sh is missing or not executable" >&2
  exit 3
fi

# ---- step 5: heavy audit (optional) -----------------------------------------
if [[ -x ./make_audit.sh ]]; then
  set +e; ./make_audit.sh >/tmp/_audit_out.txt 2>&1; rc=$?; set -e
  latest="$(ls -1t audit_bundle_*.zip 2>/dev/null | head -n1 || true)"
  [[ -n "$latest" ]] && AUDIT_BUNDLE="$latest"
elif [[ -x scripts/make_audit.sh ]]; then
  set +e; bash scripts/make_audit.sh >/tmp/_audit_out.txt 2>&1; rc=$?; set -e
  latest="$(ls -1t audit_bundle_*.zip 2>/dev/null | head -n1 || true)"
  [[ -n "$latest" ]] && AUDIT_BUNDLE="$latest"
fi

# ---- step 6: artifacts checksums (NEW) --------------------------------------
ART_SHA="${OUTDIR}/${CARD}_artifacts_sha256_${STAMP}.txt"
ART_SHA_LINES=0
if [[ -d artifacts ]]; then
  set +e
  # stable order, POSIX paths
  if command -v sha256sum >/dev/null 2>&1; then
    LC_ALL=C find artifacts -type f -print | LC_ALL=C sort | xargs -r sha256sum > "$ART_SHA"
  else
    # fallback (macOS): shasum -a 256
    LC_ALL=C find artifacts -type f -print | LC_ALL=C sort | xargs -r shasum -a 256 > "$ART_SHA"
  fi
  rc=$?; set -e
  if [[ $rc -eq 0 ]]; then
    ART_SHA_LINES="$(wc -l < "$ART_SHA" | tr -d ' ')"
  else
    rm -f "$ART_SHA"
  fi
fi

# ---- step 7: write closeout report ------------------------------------------
REPORT="${OUTDIR}/${CARD}_closeout_${STAMP}.md"
{
  echo "# Card Closeout — ${CARD}"
  echo
  echo "**Repo:** $(basename "$ROOT")  |  **Branch:** ${BRANCH}  |  **Commit:** ${SHORT_SHA}  |  **Dirty files:** ${STATUS}"
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
  echo "## Artifact checksums (${ART_SHA_LINES} files)"
  if [[ -f "$ART_SHA" ]]; then
    echo
    echo '```'
    cat "$ART_SHA"
    echo '```'
  else
    echo "_No \`artifacts/\` directory or no files to hash._"
  fi
  echo
  echo "## Operator"
  echo "Run: \`bash scripts/card_close.sh --card \"${CARD}\"${FAST:+ --fast}\`"
} > "$REPORT"

echo "[closeout] $REPORT"
echo "[bundle]  $BUNDLE_PATH"
[[ -n "$MANIFEST_PATH" ]] && echo "[manifest] $MANIFEST_PATH"
[[ -n "$AUDIT_BUNDLE" ]] && echo "[audit]   $AUDIT_BUNDLE"
[[ -f "$ART_SHA" ]] && echo "[artifacts_sha] $ART_SHA"

# ---- step 8: commit & push ---------------------------------------------------
set +e
git add -A >/dev/null 2>&1
git commit -m "${CARD}: closeout (env=${ENV_STATUS} tests=${TEST_STATUS} sanity=${SANITY_STATUS})" >/tmp/_git_commit.txt 2>&1
COMMIT_SHA="$(git rev-parse --short HEAD 2>/dev/null || echo 'unknown')"
echo "[commit]  ${COMMIT_SHA}"
CUR_BRANCH="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'main')"
git push origin "${CUR_BRANCH}" >/tmp/_git_push.txt 2>&1
echo "[pushed]  origin/${CUR_BRANCH}"
set -e

# always exit 0; report recorded even if gates failed
exit 0
```0