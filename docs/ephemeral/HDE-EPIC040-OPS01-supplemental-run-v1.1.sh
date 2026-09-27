#!/usr/bin/env bash
# HDE-EPIC040-OPS01 supplemental run (OPS_TASK v1.1). Run from the repository root:
#   P0_FILE=/tmp/ops01_p0.txt bash /tmp/ops01-run.sh
# It writes nothing inside the repository. Everything goes to one /tmp work dir.
# Exit 0 = PASS. Exit 2 = FAIL_BEHAVIOR (a check did not refuse as required).
# Exit 3 = STOP (a precondition failed; nothing was concluded).
set -uo pipefail
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0
unset HD_API_KEY HD_API_BASE_URL HDAPI_BASE_URL GEO_API_KEY DATABASE_URL

W=$(mktemp -d /tmp/hde-epic040-ops01-supp.XXXXXX)
LOG="$W/ops01_execution_log.attempt4.md"
exec > >(tee "$LOG") 2>&1
TOOL=tools/evidence/build_release_attestation.py
stop() { echo "RESULT: STOP — $*"; echo "WORKDIR=$W"; exit 3; }
fail() { echo "RESULT: FAIL_BEHAVIOR — $*"; echo "WORKDIR=$W"; exit 2; }
h() { echo; echo "## $*"; }

echo "# HDE-EPIC040-OPS01 supplemental run (attempt 4)"
echo "date_utc=$(date -u +%FT%TZ)"
echo "workdir=$W"

h "P-0 delegation (verbatim)"
[ -n "${P0_FILE:-}" ] && [ -s "$P0_FILE" ] || stop "P0_FILE missing or empty"
cat "$P0_FILE"

h "Preflight"
REPO=$(git rev-parse --show-toplevel) || stop "not in a git repository"
[ "$REPO" = "$(pwd -P)" ] || stop "run from the repository root"
case "$W" in "$REPO"*) stop "workdir inside repository";; esac
HEAD0=$(git rev-parse HEAD); echo "candidate_head=$HEAD0"
echo "key_probe:"; for k in HD_API_KEY HD_API_BASE_URL HDAPI_BASE_URL GEO_API_KEY DATABASE_URL; do
  if [ -n "${!k:-}" ]; then echo "  $k=SET"; else echo "  $k=UNSET"; fi; done
git rev-parse --verify -q edbd414 >/dev/null || stop "edbd414 not present; fetch main"
D=$(git diff --name-only edbd414 HEAD -- . ':!docs/ephemeral' ':!audit/ops/hde-epic040')
[ -z "$D" ] || { echo "$D"; stop "candidate differs from PR07 landing outside records"; }
echo "P-2 candidate_equivalence=OK"
S=$(git status --porcelain); [ -z "$S" ] || { echo "$S"; stop "tree not clean"; }
echo "P-3 clean_tree=OK"
python scripts/release_id_recompute.py --check-manifest-only || stop "release_id_recompute failed"
echo "P-4 manifest_only=OK"

h "Fixture bundle (for A-5 and A-6 only)"
B="$W/bundle"
python "$TOOL" --output "$B" --require-clean; rc=$?; echo "build_exit=$rc"
[ $rc -eq 0 ] || stop "fixture build failed; see $B/failure.json"
python "$TOOL" --verify "$B" --require-clean; rc=$?; echo "verify_exit=$rc"
[ $rc -eq 0 ] || stop "fixture verify failed"

expect_refusal() {  # $1=id $2=required code prefix $3=forbidden code (optional); rest=command
  local id=$1 want=$2 forbid=$3; shift 3
  local err rc
  err=$("$@" 2>&1 >/dev/null); rc=$?
  local code; code=$(printf '%s\n' "$err" | grep -o 'RELEASE_ATTESTATION_FAILED:[a-z_]*' | tail -n 1)
  echo "$id exit=$rc code=${code:-NONE}"
  echo "$id stderr_tail:"; printf '%s\n' "$err" | tail -n 5
  [ $rc -ne 0 ] || fail "$id did not refuse"
  case "$code" in "RELEASE_ATTESTATION_FAILED:$want"*) ;; *) fail "$id refused with unexpected code";; esac
  if [ -n "$forbid" ] && [ "$code" = "RELEASE_ATTESTATION_FAILED:$forbid" ]; then fail "$id refused for the wrong reason"; fi
  echo "$id=REFUSED_AS_REQUIRED"
}

h "A-5 tampered attestation.json"
cp -a "$B" "$W/a5"
python - "$W/a5/attestation.json" <<'PY' || stop "A-5 setup failed"
import sys; p=sys.argv[1]; b=bytearray(open(p,'rb').read())
i=b.index(b'"PASS"')+1; b[i]=ord('X'); open(p,'wb').write(bytes(b))
PY
expect_refusal A-5 attestation_ "" python "$TOOL" --verify "$W/a5" --require-clean

h "A-6 tampered evidence file"
cp -a "$B" "$W/a6"
F=$(cd "$W/a6/evidence" && find . -type f | LC_ALL=C sort | head -n 1)
[ -n "$F" ] || stop "A-6 setup: no evidence file"
echo "a6_file=$F"; printf 'X' >> "$W/a6/evidence/$F"
expect_refusal A-6 attestation_ "" python "$TOOL" --verify "$W/a6" --require-clean

h "A-7 committed change to a release member, clean clone"
T7="$W/a7-clone"
git clone -q "$REPO" "$T7" || stop "A-7 clone failed"
M=schemas/reader.v2.schema.json
printf '\n' >> "$T7/$M"
git -C "$T7" -c user.name=ops01 -c user.email=ops01@invalid commit -qam "A-7 tamper $M" || stop "A-7 commit failed"
S7=$(git -C "$T7" status --porcelain); [ -z "$S7" ] || { echo "$S7"; stop "A-7 clone not clean"; }
echo "a7_member=$M a7_clone_clean=OK a7_head=$(git -C "$T7" rev-parse HEAD)"
expect_refusal A-7 "" source_tree_not_clean bash -c "cd '$T7' && python $TOOL --output '$W/a7-out' --require-clean"

h "Post-check"
[ "$(git rev-parse HEAD)" = "$HEAD0" ] || fail "candidate HEAD changed"
[ -z "$(git status --porcelain)" ] || fail "candidate tree changed"
echo "post_check=OK"

h "Result"
echo "RESULT: PASS (A-5, A-6, A-7 refused as required)"
echo "WORKDIR=$W"
exit 0
