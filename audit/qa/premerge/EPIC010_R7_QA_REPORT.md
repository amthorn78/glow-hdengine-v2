# EPIC-010 R7 Pre-Merge QA Report

## 1) Route & alias parity (AUX surface wired)
**Context:** Confirmed canonical and alias Aux narrative routes serve identical bytes for text and suppressed outcomes.

**Method:** Exercised both `/api/aux/narrative?v=1` and `/aux/narrative?v=1` via the Flask test client for a text tuple and a suppressed tuple under pinned C/UTC env vars; compared response bytes and header subsets.

**Findings:** Both parity diffs are empty; header subset and body hashes match for canonical vs alias text responses as recorded in [`audit/qa/premerge/routes/route_probe.json`](audit/qa/premerge/routes/route_probe.json). Suppressed parity diff is also empty (`audit/qa/premerge/routes/parity_suppressed.diff`).

**Result:** PASS (artifacts: [`parity_text.diff`](audit/qa/premerge/routes/parity_text.diff), [`parity_suppressed.diff`](audit/qa/premerge/routes/parity_suppressed.diff), [`route_probe.json`](audit/qa/premerge/routes/route_probe.json)).

## 2) Suppressed posture & normalization
**Context:** Validate the approved suppressed transport posture and internal normalization to `policy_reason:"conflict"`.

**Method:** Captured canonical suppressed response headers/body and inspected composer output for an unsorted families tuple.

**Findings:** Suppressed response returns 200 with empty body, no ETag, and the optional generic policy header (`audit/qa/premerge/suppression/posture_headers.txt`, `audit/qa/premerge/suppression/posture_assert.json`). Composer normalization reports `policy_reason: conflict` (`audit/qa/premerge/suppression/normalization_check.txt`).

**Result:** PASS.

## 3) Provenance echoes on both outcomes
**Context:** Ensure provenance headers (`X-Narrative-Pack-Sha`, `X-Narrative-Composition`) emit on text and suppressed, and alias matches canonical.

**Method:** Read headers from canonical text/suppressed responses and compared them with alias counterparts.

**Findings:** Both outcomes include non-empty provenance headers (`audit/qa/premerge/provenance/echo_assert.json`); alias headers equal canonical (`audit/qa/premerge/provenance/alias_parity.txt`).

**Result:** PASS.

## 4) Determinism (two-run identity under C/UTC)
**Context:** Re-prove determinism for both routes/outcomes under pinned locale/timezone env vars.

**Method:** Set `LC_ALL=C LANG=C TZ=UTC` (`audit/qa/premerge/determinism/env.txt`) and issued back-to-back requests, comparing status, body, and header subsets.

**Findings:** All four route/outcome combinations returned identical responses (`audit/qa/premerge/determinism/two_run_assert.json`).

**Result:** PASS.

## 5) Text header snapshot sanity
**Context:** Verify refreshed text snapshot captures the approved headers/body posture.

**Method:** Inspected snapshot excerpt and validated structural checks.

**Findings:** Snapshot shows 200 text/plain, quoted strong ETag, provenance headers, and LF-terminated non-empty body (`audit/qa/premerge/text_snapshot/excerpt.txt`, `audit/qa/premerge/text_snapshot/assert.json`).

**Result:** PASS.

## 6) Coverage lock (10×4)
**Context:** Confirm cataloged 10×4 coverage artifact is intact.

**Method:** Counted rows and sampled entries from `audit/gates/narratives/keys_10x4.table.json`.

**Findings:** Artifact contains 40 rows with both shared/personal keys populated; sample rows recorded in `audit/qa/premerge/coverage/sample_rows.json` with summary in `audit/qa/premerge/coverage/summary.json`.

**Result:** PASS.

## 7) Pack identity & sidecars
**Context:** Validate pack manifest canonicality, sidecar matches, and runtime mount presence.

**Method:** Canonicalized `catalog/narratives/manifest.json`, verified sidecar digests, and checked `narratives/<pack_sha>/` mount.

**Findings:** Manifest canonical hash matches pack SHA; all five sidecars verified and runtime mount exists (`audit/qa/premerge/pack/identity.json`, `audit/qa/premerge/pack/mount_exists.txt`).

**Result:** PASS.

## 8) Composer validation & lints (spot checks)
**Context:** Spot-check representative text samples for lint compliance.

**Method:** Selected first three non-suppressed templates by ASCII key, stored bodies, and executed lint predicates.

**Findings:** All lint checks pass for sampled texts (`audit/qa/premerge/lints/report.json`, samples under `audit/qa/premerge/lints/samples/`).

**Result:** PASS.

## 9) Evidence indices & machine mirror hygiene
**Context:** Ensure human index/hash sentinel and single-file machine mirror reference the refreshed Aux artifacts and remain schema-compliant.

**Method:** Parsed human index + sha256 sentinel and inspected JSONL mirror field structure and targeted paths.

**Findings:** Human index lists both Aux snapshots and coverage artifact with matching hash (`audit/qa/premerge/indices/human_assert.json`). Machine mirror is a single canonical JSONL file with required records (`audit/qa/premerge/indices/mirror_assert.json`).

**Result:** PASS.

## 10) Docs currency (README, CHANGELOG, AGENTS, ./docs/**)
**Context:** Confirm public docs reflect current Aux posture without legacy guidance.

**Method:** Counted Aux sections/legacy tokens and captured representative excerpt lines.

**Findings:** README has one Aux section; no legacy routes, per-reason policy strings, 10×2 references, or Aux HEAD/304 guidance detected (`audit/qa/premerge/docs/scan.json`). Excerpts show the correct posture/provenance/evidence pointers (`audit/qa/premerge/docs/samples.txt`).

**Result:** PASS.

## Verified PASS tokens
AUX_SURFACE_OK · AUX_SUPPRESSION_NO_BODY_NO_ETAG_OK · COMPOSE_IDS_DETERMINISM_OK · ENV_LC_ALL_C_OK · NARR_REGISTRY_CLOSURE_OK · EVIDENCE_INDEX_UPDATED_OK · EVIDENCE_INDEX_HASH_OK · EVIDENCE_INDEX_MIRROR_OK · EVIDENCE_PATHS_VALIDATED_OK · MACHINE_MIRROR_UPDATED_OK
