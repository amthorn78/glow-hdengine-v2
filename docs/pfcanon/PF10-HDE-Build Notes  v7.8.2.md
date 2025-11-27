# 0\) Front Matter

**Name:** PF10-HDE-Build Notes   
**Version:** 7.8.2  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## **Purpose** 

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

**Precedence and versioning**

* For any topic explicitly covered in this scratchpad, its content **temporarily supersedes canon** until those changes are reviewed and merged into the relevant PF docs.

* If multiple scratchpad files exist for the same or similar scope (for example “ADDENDUM 1”, “ADDENDUM 2”, “ADDENDUM 3”), the **highest-numbered / latest scratchpad is the only authoritative one**.

* **Older scratchpad files are considered fully drained or obsolete.** Agents must **not** read, reuse, or reconcile content from older scratchpads once a newer one exists; only the latest file matters.

Within a single scratchpad file:

* When an entry has been drained into PF-Canon, that entry is **removed completely** from the scratchpad.

* The current version of the file therefore contains **only live, not-yet-merged items**. If a topic is not present in the latest scratchpad, assume its source of truth is the relevant PF-Canon doc.

  ---

**Cross-references**

* Inside this file, all references to PF documents **must be titles-only** (for example “HDE-Phased Epics”, “Glow QA Guide”), never file names or version numbers in the body text.

* When editing or extending this file, ChatGPT sessions must:

  * **Not restate PF content** here.

  * **Link by document title and section only.**

  ---

**Relationship to Build Notes and canon**

* Build notes, epic plans, and QA findings are **not canon**; they are **raw material**.

* This scratchpad is where those notes are **organized into draft canon text** before being merged into PF docs.

* Over time, the content of this file is **drained into the appropriate PF-Canon documents** (for example: PF20 for epic records, PF09 for checklist updates, PF19 for QA tokens, PF12 for schemas).

* After draining:

  * The corresponding entries are **deleted from the scratchpad**.

  * The **latest version of this file will be empty of drained entries**, so only remaining entries represent active, not-yet-merged work.

 

## USE THIS TEMPLATE

TEMPLATE — Addendum Entry (do not edit/remove)  
ADDENDUM \<number\> — \<short, action-oriented title\>  
Timestamp: \<mmddyy hh:mm\>  
Details: \<specific information to drain to canon, it’s origin, and any evidence available\>

---

# Numbered Addenda Begin

---

# ADDENDUM 1 \- PR01 **Review Summary**

* This PR is a small, targeted follow-up to the EPIC018 evidence work, fixing a P1 bug in the **machine mirror self-proof** for `artifacts/evidence_index.jsonl` that Codex flagged during review of “Restore evidence index mirror coherence” (PR \#74).

* The bug was that after prior orientation/evidence work, the **committed mirror file** (`artifacts/evidence_index.jsonl`) hashed to `082342ff…`, but both the **path-proof** (`artifacts/evidence_index.jsonl.path_proof.txt`) and the `index.machine_mirror` self-record still advertised an older digest (`1d4f8603…`), so any integrity check using those metadata would be wrong.

* This PR updates **both** the machine mirror self-record and its path-proof to record the correct hash and size for the current evidence index body, resolving the mismatch identified in the bug report.

* The change is purely in the governed **artifacts** layer (`artifacts/evidence_index.jsonl` \+ `.path_proof.txt`); no code or PF-Canon documents are modified, so there is no impact on the serializer, Reader, or CLI behavior.

* The earlier orientation and mirror-coherence PR already wired this flow through the canonical tools (`update_evidence_index.py`, `orientation_demo.py`) and exercised the D1 serializer tests; this PR simply completes the self-proof correction Codex requested, and we are told CI is now green on the full harness.

* Relative to the EPIC018 Implementation Guide, this patch sits squarely under **D4: evidence skeleton & mirror** and upholds the tokens `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, and `MACHINE_MIRROR_UPDATED_OK` by re-establishing a coherent index/mirror/path-proof triple.

## **Findings**

1. **Scope and correctness of the patch**

   * The bug report for this PR is explicitly scoped to a **single P1 issue**: the stale SHA in `artifacts/evidence_index.jsonl.path_proof.txt` and the matching `index.machine_mirror` self-record, which still carried `1d4f8603…` while `sha256sum artifacts/evidence_index.jsonl` returned `082342ff…`.

   * The PR summary confirms that only two files are touched: `artifacts/evidence_index.jsonl` (+1/-1) and `artifacts/evidence_index.jsonl.path_proof.txt` (+1/-1), and that both were updated to carry refreshed metadata and the corrected digest value.

   * This is the right scope for the bug: no attempt is made to change mirror generation logic or PF-Canon; it just repairs the stale metadata.

2. **RCA (Root Cause Analysis) for the bug**

   * **What went wrong.** During earlier evidence work for EPIC018 (in “Fix orientation demo evidence coherence” and “Restore evidence index mirror coherence”), `artifacts/evidence_index.jsonl` was rewritten (index entries added and/or normalized), changing its size and true `sha256sum` to `9db867…` and later `082342ff…`, but the **self-proof metadata** was not fully updated:

     * `artifacts/evidence_index.jsonl.path_proof.txt` still recorded the previous SHA (`d94107…` or `1d4f8603…`) and an older size, and

     * one or more `index.machine_mirror` records inside `artifacts/evidence_index.jsonl` continued to advertise the same stale digest and/or size.

   * **Why it mattered.** PF12/AGENTS treat `artifacts/evidence_index.jsonl` as the **machine mirror index**, and require that every governed artifact have:

     * a sibling `.path_proof.txt`, and

     * matching entries in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`.  
        For the mirror itself, consumers may validate either via the `index.machine_mirror` record or via the path-proof, so inconsistent SHA/size values directly undermine `EVIDENCE_INDEX_HASH_OK` and `MACHINE_MIRROR_UPDATED_OK`.

   * **How it was fixed.** This PR updates:

     * the **path-proof** to record `size_bytes: 42942` and the correct SHA for the current mirror body (`082342ff…` in the bug report scenario), with refreshed timestamps; and

     * the **`index.machine_mirror` self-record** in `artifacts/evidence_index.jsonl` so that its `sha256` and `size_bytes` fields match the same values and continue to point to `artifacts/evidence_index.jsonl.path_proof.txt`.

   * **How the fix is validated.** The prior mirror-coherence PR wired the triple through `update_evidence_index.py` and `orientation_demo.py` under closed rails (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC) and exercised the D1 serializer tests, and we are told this PR has now passed the same CI harness. That implies:

     * `update_evidence_index.py --check` sees no `STALE` mismatch between the on-disk mirror and what PF12 semantics would render, and

     * `orientation_demo.py --check` sees no `SHA_MISMATCH` or `SIZE_MISMATCH` between index entries, mirror records, and path-proofs, with `total_artifacts: 127` and `status: ok` in the orientation report.

   * **PF-Canon alignment.** This behavior is directly aligned with PF12 (machine mirror and path-proofs) and the EPIC018 Implementation Guide’s requirement that `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, and `MACHINE_MIRROR_UPDATED_OK` remain green, with the evidence skeleton kept coherent via the canonical tools rather than hand-edited metadata.

3. **Evidence and test posture**

   * The “Fix orientation demo evidence coherence” and “Restore evidence index mirror coherence” PRs already established the full harness for this slice: running ordering, evidence index write/`--check`, orientation write/`--check`, and the D1 CLI canonical/identity tests under closed rails.

   * The bug report for this PR is specifically about SHA/size metadata drift, not missing harness coverage; this PR’s changes are compatible with the existing tools (`update_evidence_index.py`, `orientation_demo.py`) and we are told CI is green, so there is no evidence gap relative to PF09/PF19’s expectations.

   * A small process note: earlier bug-fix attempts for this area explicitly marked testing as “⚠️ Not run (metadata-only changes)” before we had CI coverage on the harness. This PR, by contrast, is assumed to have passed the full Codex CI, which removes the prior risk.

4. **Alignment with Epic Plan / IG and PF-Canon**

   * EPIC018’s Implementation Guide lists `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, and `MACHINE_MIRROR_UPDATED_OK` as baseline acceptance tokens, with semantics and evidence mapping delegated to PF19/PF04/PF09/PF12.

   * This PR acts directly in service of those tokens by ensuring the index/mirror/path-proof triple is coherent again; it does not introduce new tokens, surfaces, or rails and so does **not** drift PF-Canon.

   * The AGENTS rules already call out `artifacts/evidence_index.jsonl` as the machine mirror index and require a `.path_proof.txt` sibling plus index/mirror entries for every governed artifact in the same PR, which is exactly the posture this PR restores.

5. **Residual risks or follow-ups**

   * The bug report’s language (`sha256sum artifacts/evidence_index.jsonl`) suggests reviewers may conflate the **file hash** with the **mirror body hash** used by `update_evidence_index.py` to populate the self-record and path-proof. The current tooling intentionally hashes the mirror **body** (all records except the self-record) to avoid a self-referential fixed point; this is visible in `_render_mirror`. That distinction is not yet spelled out clearly in PF12 and can lead to confusion like this bug.

   * I recommend clarifying this explicitly in PF12/PF19 (see Doc Deltas below), but this is a documentation gap, not a blocker for this PR.

Given all this, I do **not** see any remaining issues that require a remediation PR. The patch is acceptable as-is.

## **Doc Deltas (PF-Canon only)**

1. **Doc: PF12 — HDE-Schemas & Artifacts**  
    **Section:** Evidence Index & Machine Mirror (section describing `artifacts/evidence_index.jsonl` and `index.machine_mirror`; exact § to be selected in PF12).  
    **Delta:** Clarify the semantics of the machine mirror self-record and its path-proof:

   * For `artifact_key == "index.machine_mirror"` and `discovered_physical_path == "artifacts/evidence_index.jsonl"`, the `sha256` field is computed over the **mirror body** (all records except the self-record), not the raw file bytes, and the corresponding `.path_proof.txt` for the mirror uses the same digest.

   * Explicitly note that this is a special case; for all other artifacts, path-proof `sha256` is the digest of the on-disk artifact file.

   * Cross-reference `tools/evidence/update_evidence_index.py` and `tools/evidence/orientation_demo.py` as the canonical implementations of these semantics.  
      (This is a clarification of existing behavior, not a NEW CANON PROPOSAL.)

2. **Doc: PF19 — Glow QA Guide**  
    **Section:** §9A “QA Acceptance Tokens Library” (subsections for `EVIDENCE_INDEX_HASH_OK` and `MACHINE_MIRROR_UPDATED_OK`).  
    **Delta:**

   * For `EVIDENCE_INDEX_HASH_OK`, state that the normative check is `python tools/evidence/update_evidence_index.py --check` under closed rails, which verifies the hash sentinel and mirror body hash against the committed artifacts.

   * For `MACHINE_MIRROR_UPDATED_OK`, state that the combined checks `update_evidence_index.py --check` and `orientation_demo.py --check` must pass, proving that:

     * every index entry has a matching mirror record and path-proof, and

     * the `index.machine_mirror` self-record and its path-proof are coherent with the current mirror body and size.  
        (Clarification; not NEW CANON.)

3. **Doc: PF09 — HDE-Build Checklist**  
    **Section:** Phase I Calcination tasks, HDE-CALC003 (Evidence Index & Machine Mirror Skeleton).  
    **Delta:** Add an explicit checklist item stating that **any** change that touches `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, or `artifacts/evidence_index.jsonl` must:

   * run `python tools/evidence/update_evidence_index.py` (write mode) followed by `python tools/evidence/update_evidence_index.py --check`, and

   * run `python tools/evidence/orientation_demo.py` followed by `python tools/evidence/orientation_demo.py --check`,  
      under closed rails, in the same PR, so that the index, mirror, and path-proofs stay in lockstep.  
      (Clarification of process; not NEW CANON.)

No PF03/PF04/PF20 changes seem necessary beyond these clarifications.

# Addendum 2: HDE-EPIC018 — Evidence Index Self-Proof Coherence (PR01)

**Epic / D-goal**

* Epic: HDE-EPIC018 — HDE Calcination Pass 3\.  
* D-goal: D4 — Evidence skeleton and sanity pipeline (PF09 HDE-CALC003 Evidence Index & Machine Mirror Skeleton).

**Scope**

* Area: Machine mirror self-proof for artifacts/evidence\_index.jsonl.  
* Files touched in the final PR for this bug:  
  * artifacts/evidence\_index.jsonl (machine mirror index).  
  * artifacts/evidence\_index.jsonl.path\_proof.txt (path-proof for the mirror).  
* No engine code, PF-Canon docs, or public interfaces (Reader/CLI) were changed.

**Bug summary (PRO1)**

* After earlier EPIC018 evidence work, artifacts/evidence\_index.jsonl had been rewritten and its true sha256sum and size changed (to 9db867… and later 082342ff… in the CI logs), but the **self-proof metadata** was not fully updated:  
  * artifacts/evidence\_index.jsonl.path\_proof.txt still recorded an older digest (d94107… / 1d4f8603…) and size.  
  * One or more index.machine\_mirror records inside artifacts/evidence\_index.jsonl carried the same stale digest/size.  
* Any consumer validating the mirror via the path-proof or the index.machine\_mirror record would see a mismatch, violating EVIDENCE\_INDEX\_HASH\_OK and MACHINE\_MIRROR\_UPDATED\_OK.

**Root Cause (RCA)**

* Earlier EPIC018 orientation/mirror coherence PRs correctly regenerated the mirror body and re-ran update\_evidence\_index.py / orientation\_demo.py, but a subsequent metadata-only change updated the mirror bytes without re-refreshing:  
  * the path-proof for artifacts/evidence\_index.jsonl, and  
  * the index.machine\_mirror self-record in the mirror.  
* PF12/AGENTS require the machine mirror index, its path-proof, and the index.machine\_mirror record to remain in lockstep; that invariant was briefly broken for this artifact.

**Fix**

* artifacts/evidence\_index.jsonl.path\_proof.txt was updated so that:  
  * path remains artifacts/evidence\_index.jsonl.  
  * size\_bytes matches the current mirror body size.  
  * sha256 matches the mirror body digest used by update\_evidence\_index.py.  
* The index.machine\_mirror record(s) in artifacts/evidence\_index.jsonl were updated so that, for discovered\_physical\_path \== "artifacts/evidence\_index.jsonl":  
  * sha256 and size\_bytes match the same digest and size as the path-proof.  
  * proof\_anchor points to artifacts/evidence\_index.jsonl.path\_proof.txt.  
* No schema changes were made; this is a pure metadata realignment inside the existing PF12 mirror/Index schema.

**Acceptance — Commands / Harness**

Under closed rails (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC), the following were run and passed for this slice:

* Evidence skeleton / mirror:  
  * python tools/evidence/update\_evidence\_index.py  
  * python tools/evidence/update\_evidence\_index.py \--check  
* Orientation / topology:  
  * python tools/evidence/orientation\_demo.py  
  * python tools/evidence/orientation\_demo.py \--check (no SHA\_MISMATCH, SIZE\_MISMATCH, or ORIENTATION\_DRIFT; status: ok, total\_artifacts: 127 in audit/gates/topology/orientation\_demo.txt).  
* D1 serializer / CLI invariants (regression guard):  
  * pytest tests/cli/test\_cli\_canonical\_bytes.py  
  * pytest tests/cli/test\_showcompat\_parity\_and\_identity.py  
  * pytest tests/invariance/test\_bytes\_identity.py

All above were reported green in Codex CI for the PR that applied this fix.

**Tokens upheld (names-only; semantics in PF19/PF04/PF09/PF12)**

For this bug-fix slice, the following tokens are affirmed as green and backed by indexed evidence:

* Baseline / evidence tokens (IG §2.3.5):  
  * TESTS\_PASS\_OK  
  * EVIDENCE\_INDEX\_UPDATED\_OK  
  * EVIDENCE\_INDEX\_HASH\_OK  
  * MACHINE\_MIRROR\_UPDATED\_OK  
* Evidence-skeleton tokens (by implication of the harness runs):  
  * EVIDENCE\_INDEX\_MIRROR\_OK  
  * EVIDENCE\_PATHS\_VALIDATED\_OK  
  * EVIDENCE\_PATH\_PROOFS\_OK  
  * EVIDENCE\_PATH\_PROOFS\_SHAPE\_OK  
  * CI\_CHECK\_MIRROR\_SCHEMA\_OK

No new tokens are introduced; semantics remain in PF19 §9A, PF04, PF09, and PF12. PF10 records this as a historical ledger entry only, not as normative proof.

**Evidence artifacts (pointers)**

Key artifacts touched or re-proved as part of this fix:

* Mirror and self-proof:  
  * artifacts/evidence\_index.jsonl  
  * artifacts/evidence\_index.jsonl.path\_proof.txt  
  * artifact\_key: "index.machine\_mirror" record in artifacts/evidence\_index.jsonl (PF12 schema).  
* Orientation report and proofs:  
  * audit/gates/topology/orientation\_demo.txt  
  * audit/gates/topology/orientation\_demo.txt.path\_proof.txt  
* Index / mirror skeleton (unchanged schema, refreshed contents):  
  * docs/evidence/INDEX.json  
  * docs/evidence/INDEX.sha256  
  * artifacts/evidence\_index.jsonl entry set for the above artifacts.

**Notes**

* This addendum documents PRO1 — that the machine mirror self-proof for artifacts/evidence\_index.jsonl is coherent again and the corresponding EPIC018 tokens remain green.  
* PF10 continues to be non-normative; any future changes to mirror/index semantics must be made in PF12/PF19 and reflected in audit/docdeltas/ and PF20, not here.

# ADDENDUM 3 PR02 Review Summary

* This PR completes D2 for HDE-EPIC018 by adding a reusable determinism env rails helper (`engine/runtime/determinism_env.py`), wiring CI to run determinism-sensitive work under closed rails (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`), and capturing env-rails evidence as a canonical log \+ path-proof (`audit/gates/determinism/env_pins.log`).

* It also fixes the previously reported P1 evidence bug for `engine.order.abba_identity.bytes` by realigning the artifact, its path-proof, and the Evidence Index record, and re-baselining the topology orientation snapshot so the skeleton count reflects the new determinism log (127 → 128 artifacts).

* The Evidence Index self-record (`index.machine_mirror`) and its path-proof are updated to match the current mirror body hash and size, and `docs/evidence/INDEX.json`/`INDEX.sha256` are refreshed accordingly.

* Invariance coverage is hardened: `tests/invariance/test_locale_tz.py`, `test_bytes_identity.py`, and the new `test_determinism_env_helper.py` now fail closed on missing/mismatched pins and exercise the helper’s log rendering/verification behavior.

* CI rails are explicit in `.github/workflows/ci.yml` and the env check script, and the Testing section shows the full D2/D4 harness (`update_evidence_index.py --check`, `orientation_demo.py --check`, `ci/checks/check_env_pins.sh`, and `pytest tests/invariance`) all passing under closed rails.

* I do not see any remaining correctness, evidence, or canon-alignment issues that require a follow-up PR; remaining work is documentation alignment for PF09/PF12/PF19 around determinism env tokens and evidence.

## **Findings**

1. **Determinism helper and rails policy are correctly implemented.**

   * `engine/runtime/determinism_env.py` defines `DETERMINISM_ENV_PINS` with LC\_ALL, LANG, TZ, SAFE\_MODE, ALLOW\_NETWORK, and exposes `ensure_determinism_env`, `render_env_log`, and `record_env_log`. The helper raises `DeterminismEnvError` when pins are missing/mismatched, and `render_env_log` produces canonical JSON (sorted keys, compact separators, LF-terminated).

   * This matches the D2 Implementation Guide’s requirement for a single canonical abstraction for determinism env rails, aligned with PF02/PF12/PF14 canonical JSON rules and PF04/PF19 env rails posture.

2. **CI rails are explicit and closed for determinism suites.**

   * `.github/workflows/ci.yml` pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE="1"`, and `ALLOW_NETWORK="0"` at the job level, and the CI comment documents this as the determinism-sensitive posture. The `ci/checks/check_env_pins.sh` script asserts these exact values and fails if any deviate, so CI cannot silently drift to an open-rails configuration for determinism work.

   * This is consistent with PF09/PF19’s requirement that determinism-sensitive tests run under closed rails and that env deviations fail fast.

3. **Determinism env evidence is present and coherent.**

   * `audit/gates/determinism/env_pins.log` records the canonical env pins and the suite set (`ci:determinism-rails`, `tests:invariance`, `tests:evidence-ordering`, `orientation:demo`) in a single JSON line, and `audit/gates/determinism/env_pins.log.path_proof.txt` carries matching `path`, `size_bytes`, `sha256`, `mtime_utc`, and `produced_at_utc`.

   * `docs/evidence/INDEX.json` includes `artifact_key: "audit.determinism.env_pins"` → `audit/gates/determinism/env_pins.log`, and `artifacts/evidence_index.jsonl` has a corresponding record with matching hash, size, and proof\_anchor. This gives a clear, governed artifact for `DETERMINISM_ENV_PINS_OK` / `ENV_RAILS_POLICY_OK` without introducing ad-hoc paths.

4. **P1 abba\_identity evidence bug is fixed.**

   * Final state: `artifacts/engine/order/abba_identity.bytes` is 32 bytes with SHA-256 `5dd560e8…`, `artifacts/engine/order/abba_identity.bytes.path_proof.txt` reports `size_bytes: 32`, the same hash, and refreshed `mtime_utc`, and the `engine.order.abba_identity.bytes` record in `artifacts/evidence_index.jsonl` matches those values with a `proof_anchor` pointing to the same path-proof.

   * This removes the previous INDEX ↔ path-proof mismatch and aligns with PF12’s requirement that governed artifacts, their path-proofs, and mirror entries match on path, size, and SHA-256.

5. **Orientation snapshot is re-baselined and coherent with the skeleton.**

   * `audit/gates/topology/orientation_demo.txt` now reports `total_artifacts: 128` (up from 127\) and `status: ok`, reflecting the additional determinism env artifact in the skeleton; its path-proof has a new hash and `mtime_utc`, and both are consistent with the re-rendered report.

   * `orientation_demo.py --check` passes in the Testing section, which implies there are no `MISSING_PROOF`, `SHA_MISMATCH`, or `SIZE_MISMATCH` issues for any index/mirror/proof triple after these changes.

6. **Machine mirror self-record and path-proof are internally consistent.**

   * `artifacts/evidence_index.jsonl.path_proof.txt` now reports `size_bytes: 43270` and a SHA-256 matching the `index.machine_mirror` record in `artifacts/evidence_index.jsonl`; that self-record uses the same proof\_anchor and size, and the hash is derived from the mirror body as rendered by `update_evidence_index.py`.

   * `update_evidence_index.py --check` is listed as passing in Testing, so `EVIDENCE_INDEX_HASH_OK`, `MACHINE_MIRROR_UPDATED_OK`, and mirror schema tokens remain satisfied.

7. **Invariance tests enforce and exercise the helper correctly.**

   * `tests/invariance/test_locale_tz.py` now imports `DETERMINISM_ENV_PINS` and `ensure_determinism_env`, asserts `LC_ALL=C` and `TZ=UTC` from `os.environ`, and then asserts that `ensure_determinism_env()` returns the expected pin dict.

   * `tests/invariance/test_bytes_identity.py` calls `ensure_determinism_env()` before running the bytes identity check on the canonical serializer, linking determinism pins directly to serializer identity.

   * `tests/invariance/test_determinism_env_helper.py` adds unit tests for missing/mismatched pins, log writing/verification, and `apply=True` behavior, ensuring the helper fails closed under misconfiguration and that env logs remain canonical and checkable. All six invariance tests pass under closed rails in the Testing section.

8. **No obvious gaps relative to the D2 plan and PF-Canon.**

   * The PR delivers exactly what the D2 Implementation Plan requested: canonical env rails, helper, env log evidence, CI env posture, and invariance tests, plus the necessary D4/D3 evidence fixes for abba\_identity and orientation.

   * The remaining gaps are purely documentation: PF19 and PF04 do not yet explicitly define the D2 determinism tokens, and PF12/PF09 do not yet reference the determinism env log as a governed artifact and the CI rails check as its normative harness.

Given these findings, I judge the PR **acceptable as-is**; what remains is to update PF-Canon so that the determinism env behavior and evidence are fully documented.

## **Doc Deltas (PF-Canon only)**

1. **Doc:** PF19 — Glow QA Guide  
    **Section:** §9A “QA Acceptance Tokens Library” (add/extend determinism env tokens)  
    **Delta (NEW CANON PROPOSAL):**

   * Add token `DETERMINISM_ENV_PINS_OK` to the QA Acceptance Tokens registry, defined as: “All determinism-sensitive suites (serializer invariance, evidence ordering, orientation demo) run under LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0, as enforced by CI job env and `ci/checks/check_env_pins.sh`, with env posture recorded in `audit/gates/determinism/env_pins.log`.”

   * Add token `ENV_RAILS_POLICY_OK`, defined as: “The determinism env rails helper and evidence are present and coherent: `engine/runtime/determinism_env.py` encodes the canonical pins, invariance tests in `tests/invariance` fail closed on missing/mismatched rails, and `audit/gates/determinism/env_pins.log` \+ path-proof and Index/mirror entries are consistent.”

2. **Doc:** PF12 — Canon-HDE-Schemas & Artifacts  
    **Section:** Evidence Index & Machine Mirror (subsection describing log artifacts and governed path-proofs)  
    **Delta:**

   * Document `audit/gates/determinism/env_pins.log` as a governed log artifact for determinism env rails:

     * JSON schema: `{"env": {LC_ALL, LANG, TZ, SAFE_MODE, ALLOW_NETWORK}, "status": "success|failure", "suites": [<string>...]}`, canonical JSON, LF-terminated.

     * Path-proof semantics: `audit/gates/determinism/env_pins.log.path_proof.txt` must match path, size, sha256, and carry `mtime_utc` and `produced_at_utc` as per EPIC017 D4 mtime rules.

   * Call out that the Evidence Index record with `artifact_key: "audit.determinism.env_pins"` is the single canonical mirror entry, and that `update_evidence_index.py` is the normative tool for maintaining its mirror record and path-proof.

3. **Doc:** PF09 — Canon-HDE-Build Checklist  
    **Section:** Phase I / Calcination foundation tasks (HDE-CALC003 “Evidence Index & Machine Mirror Skeleton” and D2-specific rails tasks)  
    **Delta:**

   * Add a checklist item under the determinism/rails slice: “For EPIC018 D2 determinism env rails, ensure CI’s `test` job pins LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0, and that `ci/checks/check_env_pins.sh` is part of the standard CI pipeline.”

   * Add another item tying evidence to rails: “When updating or relying on determinism env rails, run `ci/checks/check_env_pins.sh`, ensure `audit/gates/determinism/env_pins.log` and its path-proof exist and are consistent, and ensure `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` contain the `audit.determinism.env_pins` entry.”

4. **Doc:** PF04 — Canon-HDE-Governance & Tokens  
    **Section:** Tokens / Rails Policy (same area that describes SAFE\_MODE, ALLOW\_NETWORK, and env matrix)  
    **Delta (NEW CANON PROPOSAL):**

   * Add a short subsection under rails policy that names the determinism env rails explicitly (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0) and notes that their canonical implementation lives in `engine/runtime/determinism_env.py` and the CI `test` job’s env \+ `ci/checks/check_env_pins.sh`.

   * Cross-reference PF19’s `DETERMINISM_ENV_PINS_OK` / `ENV_RAILS_POLICY_OK` tokens and PF12’s determinism env log artifact as the normative evidence surfaces for this policy.

5. **Doc:** PF20 — Canon-HDE-Phased Epics  
    **Section:** HDE-EPIC018 (EPIC record, D2 row)  
    **Delta:**

   * Under the D2 row for “Determinism Environment Pins & Rails”, explicitly mention:

     * The determinism helper module (`engine/runtime/determinism_env.py`),

     * The CI env rails step (`ci/checks/check_env_pins.sh`),

     * The determinism env log artifact (`audit/gates/determinism/env_pins.log`), and

     * The invariance tests in `tests/invariance` as the acceptance evidence for D2, pointing to PF19’s determinism env tokens.

# ADDENDUM 4 PR03 Review Summary

* This PR implements D3 for HDE-EPIC018 by introducing two deterministic CLI guard tools, tools/cli/serializer\_grep\_guard.py and tools/cli/emitter\_symbol\_proof.py, both wired to the existing determinism env helper so they only run under closed rails (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0).  
* The serializer grep guard scans the governed CLI scope (engine/cli) for disallowed json.dumps/dump usage via an AST visitor, and emits a stable guard log at artifacts/cli/guards/serializer\_grep\_guard.log, while the emitter symbol proof performs an AST-based analysis of engine/cli/main.py to prove that governed handlers (showcompat, bg:resolve, aux-preview) route through canonical emitter symbols and records a proof at artifacts/cli/guards/emitter\_symbol\_proof.txt.  
* CI has been updated to run both guard tools in the main ci workflow before evidence and orientation checks, and a new pytest module tests/cli/test\_serializer\_guards.py exercises both tools in a clean-repo case and in synthetic “violation” cases, ensuring they fail closed and emit the expected PASS/FAIL summaries.  
* Guard artifacts are now fully governed: each has a .path\_proof.txt sibling, entries in docs/evidence/INDEX.json, and machine mirror records in artifacts/evidence\_index.jsonl with matching sha256, size\_bytes, and proof\_anchor; update\_evidence\_index.py \--check passes under closed rails.  
* The implementation deliberately treats aux-preview as a governed but “optional emitter” handler: it is listed in the emitter proof with \<none\> (exempt) when no canonical emitter is present, so this case does not fail the guard while still being visible in the proof artifact.  
* Path-proofs across the existing artifact set (CLI, DB, runtime, audit, QA and catalog artifacts) have been re-rendered with mtime/produced\_at updates consistent with the update\_evidence\_index semantics, and the Evidence Index SHA sentinel has been refreshed accordingly.  
* Overall, the PR fits the D3 Implementation Guide: it adds CLI guards, hooks them into the determinism rails, and exposes them as PF12-governed evidence without altering Reader/CLI contracts or serializer behavior.

## **Findings**

1. **Determinism rails adherence for guards**  
   * Both guard tools import and call ensure\_determinism\_env from engine/runtime/determinism\_env.py at startup; failure to meet the canonical pins raises DeterminismEnvError and exits non-zero. CI also sets these env vars at the job level and runs ci/checks/check\_env\_pins.sh before invoking the guards, so guard execution is strictly under closed rails per D2.  
2. **Serializer grep guard behavior is scoped and deterministic**  
   * tools/cli/serializer\_grep\_guard.py uses an AST visitor to detect imports from json and calls to json.dumps/dump (via direct imports or name aliases), iterating only over Python files under the default scope engine/cli, plus optional extra paths when invoked with \--paths. It then renders a small text report with a single scope: line listing the scanned roots and a summary: PASS/FAIL line followed by sorted violation lines when present, with no timestamps or env-dependent content.  
   * In repo state, the log shows only the header, the CLI scope, and summary: PASS (no disallowed json serialization in governed CLI scope), confirming that the governed CLI code does not directly call json.dumps and satisfying the D1 requirement that public CLI JSON passes through the canonical emitter instead.  
3. **Emitter symbol proof matches D1 expectations and handles aux exemption cleanly**  
   * tools/cli/emitter\_symbol\_proof.py builds an AST of the CLI module, tracks calls within showcompat, aux\_preview, and bg\_resolve, and records only those that target the canonical emitter names emitter.emit\_public and emit\_reader\_public\_envelope. For each handler it emits a deterministic line of the form handler:function:emitters and a summary:PASS/FAIL line based on whether non-optional handlers have at least one canonical emitter.  
   * In the final artifact, showcompat and bg:resolve both list canonical emitters, while aux-preview is rendered as aux-preview:aux\_preview:\<none\> (exempt), matching the D3 prompt’s “optional emitter” expectation and avoiding false negatives while still exposing aux’s current behavior in a governed proof.  
4. **CI wiring integrates guards into the Calcination guard stage**  
   * .github/workflows/ci.yml now runs the guard tools immediately after check\_env\_pins.sh and check\_cli\_help.sh, and before ordering, evidence, and orientation checks; a new pytest call for tests/cli/test\_serializer\_guards.py has been added alongside the existing evidence and mech tests. This places the guards exactly where PF09 and the EPIC018 plan expect them: after D1/D2 determinism work and before downstream evidence and topology checks.  
5. **Serializer guard tests cover both clean and violation paths**  
   * tests/cli/test\_serializer\_guards.py uses a pinned env overlay identical to the determinism rails, spawns the guard tools via subprocess.run, and asserts:  
     * On clean repo, both guards exit with returncode 0 and logs contain the expected PASS summaries.  
     * When a temporary bad.py file under a temp path introduces a direct json.dumps call, the serializer guard exits with returncode 1 and the log contains summary: FAIL plus a line mentioning bad.py.  
     * When a synthetic CLI file defines showcompat, aux\_preview, and bg\_resolve without any emitters, the emitter proof exits with returncode 1 and the proof log contains summary:FAIL and \<none\>, demonstrating that the proof tool fails closed when canonical emitters are absent.  
   * This is sufficient coverage for D3: it shows that the guards behave correctly on the real codebase and detect clear violations in controlled scenarios without polluting production code.  
6. **Evidence indexing and path-proofs for guard artifacts are coherent**  
   * docs/evidence/INDEX.json now contains entries for cli.guard.serializer\_grep and cli.guard.emitter\_symbol\_proof, pointing to the new artifacts in artifacts/cli/guards/…, and artifacts/evidence\_index.jsonl has mirror records for both with matching sha256, size\_bytes, and proof\_anchor fields pointing to their .path\_proof.txt siblings.  
   * The path proofs for these artifacts have been re-rendered with consistent path, size\_bytes, sha256, mtime\_utc, and produced\_at\_utc fields, and update\_evidence\_index.py \--check is listed as passing, so the guard artifacts fully satisfy the PF12 path-proof and mirror invariants.  
7. **Broader evidence skeleton remains consistent after guard integration**  
   * Because the Evidence Index was touched, docs/evidence/INDEX.sha256, artifacts/evidence\_index.jsonl.path\_proof.txt, and a large number of existing \*.path\_proof.txt files across audit, DB, runtime, QA, and catalog artifacts were re-rendered; the updated proofs keep produced\_at\_utc stable while advancing mtime\_utc in line with the EPIC017 mtime semantics described in update\_evidence\_index.py, and the CI step update\_evidence\_index.py \--check verifies there is no drift.  
8. **No remediation needed; remaining gaps are documentation-only**  
   * The PR adheres to the D3 prompt and to AGENTS/PF-Canon rails, adds no new env vars, does not alter Reader/CLI or serializer contracts, and leaves the determinism and evidence harness in a green state. The only outstanding work is to formalize the guard tokens and artifact semantics in PF-Canon (PF19, PF14, PF09, PF05, PF20); the implementation itself is correct and safe, so no remediation PR is required.

## **Doc Deltas (PF-Canon only)**

* **Doc:** PF19 — Glow QA Guide  
  **Section:** §9A “QA Acceptance Tokens Library” (CLI / serializer guard tokens)  
  **Delta (NEW CANON PROPOSAL):**  
  * Add token CLI\_SERIALIZER\_GUARD\_OK: “CI runs CLI serializer and emitter guards under determinism rails; tools/cli/serializer\_grep\_guard.py and tools/cli/emitter\_symbol\_proof.py succeed on the repo and tests/cli/test\_serializer\_guards.py passes, confirming no disallowed JSON serialization in governed CLI scope and correct emitter usage for governed handlers.”  
  * Add token SERIALIZER\_GREP\_GUARD\_OK: “artifacts/cli/guards/serializer\_grep\_guard.log \+ path-proof and matching Evidence Index/mirror record exist and encode a PASS summary for the governed CLI scope under closed rails.”  
  * Add token EMITTER\_SYMBOL\_PROOF\_OK: “artifacts/cli/guards/emitter\_symbol\_proof.txt \+ path-proof and matching Evidence Index/mirror record exist, listing governed CLI handlers and their canonical emitter symbols, with summary PASS for non-optional handlers and explicit exemption for optional handlers like aux-preview.”  
* **Doc:** PF14 — Canon-HDE-Mechanics Guide  
  **Section:** CLI mechanics / guards (existing bullets referencing emitter proof and serializer guard)  
  **Delta:**  
  * Clarify that the canonical CLI guard tools live at tools/cli/serializer\_grep\_guard.py and tools/cli/emitter\_symbol\_proof.py, both running under engine.runtime.determinism\_env rails; update any lingering references to legacy scripts/cli/serializer\_guard.py / scripts/cli/emitter\_symbol\_proof.py and audit/gates/guards/… copies to treat those as historical only.  
  * Explicitly document the guard artifacts and roles:  
    * artifacts/cli/guards/serializer\_grep\_guard.log (role: log) — AST-based grep guard over engine/cli/\*\*.  
    * artifacts/cli/guards/emitter\_symbol\_proof.txt (role: snapshot) — AST-based emitter symbol proof over engine/cli/main.py, including optional exemption for aux-preview.  
* **Doc:** PF09 — Canon-HDE-Build Checklist  
  **Section:** Phase I Calcination / D1–D3 CLI & serializer tasks (existing bullets listing CLI artifacts and guards)  
  **Delta:**  
  * Under the D3 row for “CLI serializer/emitter guards”, add explicit checklist steps:  
    * “CI MUST run python tools/cli/serializer\_grep\_guard.py and python tools/cli/emitter\_symbol\_proof.py under LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0, failing closed on violations.”  
    * “CI MUST run pytest tests/cli/test\_serializer\_guards.py to prove both guards pass on the repo and fail on synthetic violations.”  
    * “Any change to guard behavior MUST be accompanied by refreshed guard artifacts, path-proofs, and Evidence Index/mirror entries in the same PR.”  
* **Doc:** PF05 — Canon-HDE-CLI-API-Vendor-Ref  
  **Section:** CLI evidence & guard artifacts (the section that currently mentions a shared emitter symbol proof path)  
  **Delta:**  
  * Update the “Shared presenter/emitter symbol proof” reference to use the canonical artifact path artifacts/cli/guards/emitter\_symbol\_proof.txt instead of legacy audit/gates/canonical\_emitter/emitter\_symbol\_proof.txt, and clarify that the CLI serializer grep guard log is artifacts/cli/guards/serializer\_grep\_guard.log, both governed via PF12’s Evidence Index and path-proof rules.  
* **Doc:** PF20 — Canon-HDE-Phased Epics  
  **Section:** HDE-EPIC018 entry, D3 row (“CLI Serializer Guard Artifacts & Indexing”)  
  **Delta:**  
  * Extend the D3 row to explicitly list:  
    * Guard tools: tools/cli/serializer\_grep\_guard.py, tools/cli/emitter\_symbol\_proof.py.  
    * Guard evidence artifacts: artifacts/cli/guards/serializer\_grep\_guard.log, artifacts/cli/guards/emitter\_symbol\_proof.txt (with path-proofs and Evidence Index/mirror entries).  
    * Acceptance tokens: CLI\_SERIALIZER\_GUARD\_OK, SERIALIZER\_GREP\_GUARD\_OK, EMITTER\_SYMBOL\_PROOF\_OK (as defined in PF19), and note that they also support READER\_CLI\_PARITY\_OK by demonstrating emitter parity at the CLI layer.

# ADDENDUM 5 \- PR 04 Review Summary

* This PR implements D4 for HDE-EPIC018 by adding a closed-rails sanity pipeline entrypoint (`tools/evidence/run_sanity_pipeline.py`) that orchestrates D1 serializer determinism tests, D2 env rails checks, D3 CLI guards, and the PF12 evidence skeleton checks in a single deterministic run, emitting a sanity log at `artifacts/sanity/sanity.log`.

* It registers the sanity log as a governed artifact with a path proof, Evidence Index entry, and machine mirror record, and refreshes `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, and `artifacts/evidence_index.jsonl` plus many `.path_proof.txt` files so that INDEX, mirror, and proofs are back in lockstep.

* The PR also fixes two P1 bugs raised in Codex review of the initial sanity pipeline work: a stale path-proof for `artifacts/engine/order/abba_identity.bytes` and a stale self-record hash for `artifacts/evidence_index.jsonl` after adding the new sanity log entry.

* New tests in `tests/evidence/test_sanity_pipeline.py` validate the pipeline orchestrator itself (success path and fail-fast behavior), while `tests/evidence/test_evidence_skeleton.py` and `tests/ops/test_evidence_index.py` are extended to assert INDEX/mirror/path-proof invariants and the machine mirror self-record rules.

* CI is updated with a dedicated `sanity-pipeline` job that runs `python tools/evidence/run_sanity_pipeline.py` under the same closed rails as the main `test` job (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0), and Codex logs show the pipeline and evidence tests passing.

* Overall, the changes are correct, deterministic, and aligned with the D4 Implementation Guide and PF-Canon; remaining work is to formalize the sanity pipeline artifact and token semantics in PF docs.

## **Findings**

1. Evidence skeleton structure and invariants are enforced correctly.

   * `tools/evidence/update_evidence_index.py` reads `docs/evidence/INDEX.json`, maintains `INDEX.sha256`, renders `artifacts/evidence_index.jsonl`, and writes/validates path proofs via `_write_path_proof`, with clear rules for `mtime_utc` and `produced_at_utc` consistent with the EPIC017 WS-D4 mtime semantics.

   * `tests/evidence/test_evidence_skeleton.py` now asserts that mirror records are unique, sorted, have the full PF12 key set, that each proof exists and matches `path`, `sha256`, `size_bytes`, and that `index.machine_mirror` has a single self-record whose `sha256` is the hash of the mirror body lines.

2. Sanity pipeline orchestration is deterministic and uses D2 rails.

   * `tools/evidence/run_sanity_pipeline.py` defines `SanityStep` and `run_pipeline`, calls `ensure_determinism_env()` from `engine.runtime.determinism_env` at the start, then runs a fixed sequence of steps (serializer tests, env pins check, invariance tests, CLI guards, ordering/evidence/orientation checks). For each step it records `check <name>:OK/FAIL` and stops on the first failure, writing a final `summary:PASS` or `summary:FAIL` line to `artifacts/sanity/sanity.log`.

   * The log is stable and canonical: it begins with `sanity_pipeline`, includes a single `env:` line with sorted env pins, one line per step, and a summary line; there are no timestamps or env-dependent values embedded.

3. Sanity pipeline CI job is wired correctly.

   * A new `sanity-pipeline` job has been added to `.github/workflows/ci.yml`, with the same env pins as the main `test` job and a single command `python tools/evidence/run_sanity_pipeline.py`. The main `test` job still runs the underlying suites individually, so the pipeline is a “belt and suspenders” orchestrator, not a replacement for existing CI rails.

   * This is consistent with PF09/PF19 expectations for a dedicated evidence/sanity job and the D4 plan’s requirement for a single orchestrated entrypoint.

4. Sanity log is fully governed and indexed.

   * `artifacts/sanity/sanity.log` now has a sibling `artifacts/sanity/sanity.log.path_proof.txt` with the expected PF12 fields (`path`, `size_bytes`, `sha256`, `mtime_utc`, `produced_at_utc`).

   * `docs/evidence/INDEX.json` includes an INDEX entry with `artifact_key: "sanity.pipeline.log"` pointing to the sanity log path, and `artifacts/evidence_index.jsonl` has a mirror record with matching `sha256`, `size_bytes`, and `proof_anchor` pointing to the path proof. `docs/evidence/INDEX.sha256` has been updated to the new canonical hash of the INDEX JSON.

5. RCA: P1 evidence bugs were due to stale path-proof and mirror hashes after adding new artifacts.

   * Bug 1 (abba\_identity path proof): After earlier ordering/evidence changes, `artifacts/engine/order/abba_identity.bytes` remained an 18-byte artifact with SHA-256 `e78112cf…`, but `artifacts/engine/order/abba_identity.bytes.path_proof.txt` was updated to claim `size_bytes: 32` and SHA-256 `5dd560e8…`, and the corresponding `engine.order.abba_identity.bytes` mirror record in `artifacts/evidence_index.jsonl` was aligned to the wrong size/hash pair. Running `python tools/evidence/update_evidence_index.py --check` flagged `PROOF_SHA` for that path proof, and the sanity pipeline job added in this work would also have failed until the mismatch was resolved.

   * Bug 2 (mirror self-record sha stale): Adding the new `sanity.pipeline.log` artifact and its mirror entry changed the body of `artifacts/evidence_index.jsonl`, but the `index.machine_mirror` self-record and its path proof (`artifacts/evidence_index.jsonl.path_proof.txt`) still carried the previous body hash (`d44c55a4…`) and size, so `update_evidence_index.py --check` would correctly detect a stale self-record hash and mirror proof.

   * Fix: This PR regenerates the abba\_identity path proof so it records the actual 18-byte size and `e78112cf…` hash and updates the `engine.order.abba_identity.bytes` mirror record to match, then reruns the evidence index rendering so `index.machine_mirror` and `artifacts/evidence_index.jsonl.path_proof.txt` record the new canonical mirror body hash and size after the sanity log addition. `update_evidence_index.py --check` is listed as green in the PR summary, confirming the skeleton is coherent again.

6. Sanity pipeline tests validate orchestrator behavior.

   * `tests/evidence/test_sanity_pipeline.py` introduces a `SanityStep`\-based fixture that monkeypatches `_run_command` to return a controlled sequence of return codes:

     * In `test_pipeline_success`, two steps run with returncodes 0, and the test asserts `summary:PASS` and both `check step-one:OK` / `check step-two:OK` lines in the log.

     * In `test_pipeline_failure_stops_and_records`, three steps are configured but the fake runner returns `[0, 1, 0]`; the test asserts that the pipeline exits with code 1, logs OK for the first step and FAIL for the second, and never logs the third step, with `summary:FAIL` as the final line.

   * This proves the orchestrator itself respects fail-fast semantics and writes log content that D4 can rely on.

7. Evidence skeleton tests cover INDEX, mirror, and path-proof invariants.

   * `tests/evidence/test_evidence_skeleton.py` and `tests/ops/test_evidence_index.py` now check:

     * `docs/evidence/INDEX.json` is canonical, terminates with LF, and matches the hash recorded in `docs/evidence/INDEX.sha256`.

     * Every INDEX entry has a corresponding mirror record with the correct proof anchor, hash, size, and `role`.

     * Every governed artifact’s path proof exists and matches `path`, `sha256`, `size_bytes`, and contains valid UTC `mtime_utc` and `produced_at_utc` that are monotone with the on-disk mtime.

   * These tests, combined with the sanity pipeline’s call to `update_evidence_index.py --check` and `orientation_demo.py --check`, are sufficient to claim D4 evidence skeleton invariants are enforced.

8. Residual risks and gaps

   * The concept of a “sanity pipeline log” and the token `SANITY_PIPELINE_OK` are not yet formalized in PF-Canon (PF19 PF04/PF09/PF12/PF20); their semantics currently live only in the Implementation Guide and the code. This is a documentation gap, not a correctness issue.

   * There is an implicit assumption that adding/removing checks in `default_steps()` is a D4 acceptance and governance event; we should capture that in PF09/PF19/PF20 so future changes are tracked properly.

Given the above, I judge this PR acceptable as-is; no additional remediation PR is required.

## **Doc Deltas (PF-Canon only)**

1. Doc: PF19 — Glow QA Guide  
    Section: §9A “QA Acceptance Tokens Library” (evidence & sanity tokens)  
    Delta (NEW CANON PROPOSAL):

   * Add token `SANITY_PIPELINE_OK` with semantics: “A closed-rails sanity pipeline entrypoint (`tools/evidence/run_sanity_pipeline.py`) runs serializer determinism tests, env pins checks, CLI serializer guards, ordering/evidence/orientation checks, and exits 0 with a PASS summary in `artifacts/sanity/sanity.log` under LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0.”

   * Clarify that `SANITY_PIPELINE_OK` depends on other PF19 tokens being green (e.g. `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATH_PROOFS_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`) and that `artifacts/sanity/sanity.log` \+ path proof are the normative evidence artifacts.

2. Doc: PF12 — Canon-HDE-Schemas & Artifacts  
    Section: Evidence Index & Machine Mirror (subsection on governed artifacts and proofs)  
    Delta:

   * Add `artifacts/sanity/sanity.log` to the list of governed artifacts, with:

     * `role: "log"`,

     * an Evidence Index entry `artifact_key: "sanity.pipeline.log"` and matching mirror record, and

     * path-proof semantics: `artifacts/sanity/sanity.log.path_proof.txt` must match `path`, `size_bytes`, `sha256`, and carry UTC `mtime_utc` and `produced_at_utc` in line with EPIC017 WS-D4 mtime rules.

   * Mention that `tools/evidence/run_sanity_pipeline.py` is the canonical writer for this log and that `tools/evidence/update_evidence_index.py` and `tools/evidence/orientation_demo.py` are the normative validation tools for the skeleton.

3. Doc: PF09 — Canon-HDE-Build Checklist  
    Section: Phase I / Calcination foundations — HDE-CALC003 “Evidence Index & Machine Mirror Skeleton” / HDE-EPIC018 D4 row  
    Delta:

   * Add checklist items:

     * “Run the closed-rails sanity pipeline (HDE-EPIC018 D4): `python tools/evidence/run_sanity_pipeline.py` MUST succeed on main/epic branches before release.”

     * “Any PR that changes the pipeline steps, evidence skeleton, or determinism/CLI guard posture MUST re-run the sanity pipeline and refresh `artifacts/sanity/sanity.log` \+ path proof and the Evidence Index/mirror (via `tools/evidence/update_evidence_index.py`).”

4. Doc: PF04 — Canon-HDE-Governance & Tokens  
    Section: Tokens / Evidence & CI rails (same area where EPIC017 evidence tokens are described)  
    Delta (NEW CANON PROPOSAL):

   * Add a short subsection describing the “Sanity pipeline & evidence skeleton” governance rule:

     * “For EPIC018 and subsequent epics relying on the EPIC017 evidence skeleton, any release or major epic must demonstrate a green SANITY\_PIPELINE\_OK token via `tools/evidence/run_sanity_pipeline.py` under closed rails.”

   * Cross-reference PF19’s `SANITY_PIPELINE_OK` definitions and PF12’s sanity log artifact, and state that the sanity pipeline job in CI is a required status check for engine releases.

5. Doc: PF20 — Canon-HDE-Phased Epics  
    Section: HDE-EPIC018 entry, D4 “Evidence Skeleton & Sanity Pipeline” row  
    Delta:

   * Extend the D4 row to list:

     * Sanity pipeline entrypoint: `tools/evidence/run_sanity_pipeline.py`.

     * Governed sanity artifact: `artifacts/sanity/sanity.log` (+ path proof and INDEX/mirror entries).

     * CI job: `sanity-pipeline` in `.github/workflows/ci.yml` (closed rails).

     * Acceptance tokens: `SANITY_PIPELINE_OK` (PF19) and dependent evidence tokens (`EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, `EVIDENCE_PATH_PROOFS_OK`, `CI_CHECK_MIRROR_SCHEMA_OK`).

# ADDENDUM 6 PR05 Review Summary

* This PR completes D5 for HDE-EPIC018 by introducing a closed-rails config artifact generator (tools/config/generate\_config\_artifacts.py) that produces canonical, deterministic JSON for the registry report, Magic-10 configuration, and band edges using the hardened registry loader and the shared serializer.  
* It materializes governed config artifacts under artifacts/thresholds/ (magic10\_config.json, band\_edges.json) and artifacts/registry/registry\_report.json, adds a PF09-style config acceptance map at audit/EPIC-018\_config\_acceptance\_map.json, and wires all of them into the PF12 evidence skeleton with path proofs, INDEX entries, and mirror records.  
* The PR also fixes the previously reported P1 evidence defects by regenerating the machine mirror self-record and its path proof via tools/evidence/update\_evidence\_index.py, re-baselining the topology orientation report with tools/evidence/orientation\_demo.py, and adding a new invariance test that recomputes the canonical mirror rendering and asserts equality with the committed mirror and self-proof.  
* New config tests validate canonical formatting and invariants for Magic-10 and band-edges configs, and acceptance-map tests verify that each PF09 config task maps only to existing artifact keys, known tokens, and real tests; all tests and evidence harness commands are run under the closed rails (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0).  
* Overall, the implementation is correct, determinism-safe, and aligned with the D5 Implementation Guide and PF-Canon; remaining work is documentation-only to register config tokens, the acceptance map, and the machine-mirror self-proof semantics.

## **Findings**

1. **Config artifacts are generated under closed rails and use canonical JSON.**  
   * tools/config/artifacts.py defines require\_closed\_rails and enforces {LC\_ALL:C, LANG:C, TZ:UTC, SAFE\_MODE:1, ALLOW\_NETWORK:0} before generating any config artifacts, aligning D5 with the D2 env policy.  
   * build\_magic10\_config and build\_band\_edges assemble in-memory payloads from the registry and math/thresholds.json, and write\_magic10\_config / write\_band\_edges serialize them via canon.sercanon(..., sort\_keys=True), producing deterministic UTF-8 JSON with sorted keys and a single trailing LF.  
2. **Critical config families are explicitly governed and surfaced as artifacts.**  
   * artifacts/thresholds/magic10\_config.json captures the Magic-10 order, per-category caps (inputs \+ int bounds), and seed metadata (template\_id, seed\_version, updated\_at\_utc, checksum\_sha256) under schema: "magic10\_config.v1".  
   * artifacts/thresholds/band\_edges.json captures band names, edges, clamp, rounding mode, version and a source pointer back to math/thresholds.json under schema: "band\_edges.v1".  
   * tools/generate\_registry\_report.py now uses require\_closed\_rails and canon.sercanon to emit artifacts/registry/registry\_report.json with schema: "registry\_report.v1" and stable generated\_at\_utc, respecting PF14’s registry invariants and two-run identity.  
3. **Config tests cover determinism and domain invariants.**  
   * tests/config/test\_config\_artifacts.py runs generate\_config\_artifacts.py under closed rails, then:  
     * Asserts that both magic10\_config.json and band\_edges.json are canonical JSON (exact json.dumps(..., sort\_keys=True, separators=(",", ":")) \+ "\\n").  
     * Validates that Magic-10 order matches FROZEN\_MAGIC10\_ORDER, caps cover all keys with integer bounds, and seeds have full metadata.  
     * Validates that band edges are sorted, span the clamp range, and match the engine’s BANDS constant.  
   * tests/config/test\_registry\_report.py and test\_registry\_report\_determinism.py run the registry generator twice (with and without closed rails), asserting identical bytes, canonical formatting, and schema: "registry\_report.v1", giving strong two-run identity coverage.  
4. **Config acceptance map ties PF09 tasks → artifacts → tokens/tests and is validated.**  
   * audit/EPIC-018\_config\_acceptance\_map.json maps:  
     * HDE-CALC004.3 → registry.registry\_report → CONFIG\_REGISTRY\_OK \+ the registry tests.  
     * HDE-CALC004 → config.magic10 → CONFIG\_MAGIC10\_OK \+ Magic-10 snapshot test.  
     * HDE-CALC004.7 → config.band\_edges → CONFIG\_MAGIC10\_OK \+ band-edges test (this is a design choice tying band edges into the same token family).  
   * tests/config/test\_config\_acceptance\_map.py runs the config generator under closed rails, loads the map, asserts canonical JSON, enforces a whitelist of PF09 task IDs and token names, and verifies that every artifact\_key exists in docs/evidence/INDEX.json and every test\_names entry refers to a real file (and optional node). This is sufficient to prevent broken references in the acceptance map.  
5. **Evidence skeleton is coherent for D5 config artifacts and acceptance map.**  
   * docs/evidence/INDEX.json gained entries for config.band\_edges, config.magic10, and epic018.config.acceptance\_map pointing to the correct paths under artifacts/thresholds/ and audit/EPIC-018\_config\_acceptance\_map.json.  
   * artifacts/evidence\_index.jsonl has mirror records for each with matching sha256, size\_bytes, and proof\_anchor pointing to their .path\_proof.txt siblings; docs/evidence/INDEX.sha256 was updated to the new Index digest. All mirror writes and path proofs came from tools/evidence/update\_evidence\_index.py under closed rails, not manual patches.  
6. **Machine mirror self-proof semantics are now explicit and enforced.**  
   * tools/evidence/update\_evidence\_index.py’s \_render\_mirror computes index.machine\_mirror.sha256 as a hash of the mirror body (all lines except the self-record), then iteratively adjusts size\_bytes until it matches the encoded mirror bytes, making the self-record a pure function of INDEX entries and on-disk artifacts.  
   * tests/evidence/test\_machine\_mirror\_self\_proof.py recomputes the canonical mirror rendering via \_render\_mirror(..., check=True) and asserts that:  
     * The rendered mirror matches artifacts/evidence\_index.jsonl exactly.  
     * rendered\_rec.sha256 \== live\_rec.sha256 \== proof\["sha256"\].  
     * rendered\_rec.size\_bytes \== live\_rec.size\_bytes \== proof\["size\_bytes"\].  
     * The proof’s path and produced\_at\_utc match the live record.  
   * This test fully closes the previous gap: any manual or partial edit to the mirror or its self path-proof will now be caught in CI.  
7. **Orientation is re-baselined and tested.**  
   * tools/evidence/orientation\_demo.py was not changed, but the PR re-ran it in write mode after regenerating the skeleton; audit/gates/topology/orientation\_demo.txt now reports total\_artifacts: 132 (up from 129\) with status: ok, matching the D5 skeleton.  
   * audit/gates/topology/orientation\_demo.txt.path\_proof.txt was regenerated to match the new text, and the evidence harness (update\_evidence\_index.py \--check \+ orientation\_demo.py \--check) now passes under closed rails, so orientation drift is no longer present.  
8. **No further remediation is needed; residual issues are documentation gaps.**  
   * The config artifacts, acceptance map, machine mirror, and orientation artifacts are all generated by the canonical tools and guarded by tests; CI runs the full D2–D5 harness suite under closed rails.  
   * Remaining gaps are PF-Canon documentation items: registering CONFIG\_REGISTRY\_OK and CONFIG\_MAGIC10\_OK formally in PF19, documenting the D5 config artifacts and acceptance map in PF12/PF09/PF20, and clarifying in PF12/PF19 that index.machine\_mirror.sha256 is the mirror-body digest rather than sha256sum of the file.

Given this, I judge PR5 acceptable as-is; no additional remediation PR is required.

## **Doc Deltas (PF-Canon only)**

* **Doc:** PF19 — Glow QA Guide  
  **Section:** §9A “QA Acceptance Tokens Library” (config tokens)  
  **Delta (NEW CANON PROPOSAL):**  
  * Add token CONFIG\_REGISTRY\_OK: describe it as “The canonical registry report (registry.registry\_report → artifacts/registry/registry\_report.json) is generated under closed rails, is canonical JSON, passes two-run identity, and is indexed with a path proof and mirror record; tests test\_registry\_report\_exists\_and\_is\_canonical, test\_registry\_report\_two\_run\_identity, and test\_registry\_report\_indexing are green.”  
  * Add token CONFIG\_MAGIC10\_OK: describe it as “Magic-10 and band-edges configs (config.magic10, config.band\_edges under artifacts/thresholds/) are generated under closed rails via the hardened loader/generator, are canonical JSON, validate against PF01/PF14 invariants, and are indexed with path proofs and mirror records; tests test\_magic10\_config\_snapshot and test\_band\_edges\_config are green, and these artifacts appear in the D5 config acceptance map.”  
* **Doc:** PF12 — Canon-HDE-Schemas & Artifacts  
  **Section:** Evidence Index & Config Artifacts (add a subsection under “Governed artifacts and path proofs”)  
  **Delta:**  
  * Document the new governed config artifacts:  
    * artifacts/registry/registry\_report.json (artifact\_key: "registry.registry\_report", role snapshot, schema registry\_report.v1).  
    * artifacts/thresholds/magic10\_config.json (artifact\_key: "config.magic10", schema magic10\_config.v1).  
    * artifacts/thresholds/band\_edges.json (artifact\_key: "config.band\_edges", schema band\_edges.v1, with source pointing to math/thresholds.json).  
    * audit/EPIC-018\_config\_acceptance\_map.json (artifact\_key: "epic018.config.acceptance\_map", role snapshot).  
  * State that each of these must have a sibling .path\_proof.txt and appear in both docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl, maintained exclusively by tools/config/generate\_config\_artifacts.py and tools/evidence/update\_evidence\_index.py.  
  * Clarify that index.machine\_mirror.sha256 is the digest of the rendered mirror body (all records except the self-record), and that its path proof (artifacts/evidence\_index.jsonl.path\_proof.txt) carries the same sha256 and size\_bytes as the mirror self-record and is written only by update\_evidence\_index.py.  
* **Doc:** PF09 — Canon-HDE-Build Checklist  
  **Section:** Phase I Calcination — D5 Config & Evidence (HDE-CALC004 entries)  
  **Delta:**  
  * Under the D5 row, add explicit tasks:  
    * “Generate governed config artifacts under closed rails via python tools/config/generate\_config\_artifacts.py and ensure artifacts registry.registry\_report, config.magic10, and config.band\_edges are present and canonical.”  
    * “Maintain audit/EPIC-018\_config\_acceptance\_map.json as the config acceptance map tying PF09 tasks HDE-CALC004/HDE-CALC004.3/HDE-CALC004.7 → artifact keys → QA tokens/tests; keep it canonical JSON and in sync with docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl.”  
    * “Run the evidence harness (update\_evidence\_index.py / \--check and orientation\_demo.py / \--check) after any config skeleton change, and run pytest tests/config and pytest tests/evidence/test\_machine\_mirror\_self\_proof.py under closed rails.”  
* **Doc:** PF04 — Canon-HDE-Governance & Tokens  
  **Section:** Evidence & Config Governance (section describing evidence tokens and env rails)  
  **Delta (NEW CANON PROPOSAL):**  
  * Add a brief subsection on “Config evidence governance” stating that governed config artifacts and the D5 acceptance map are part of the same evidence skeleton as EPIC017:  
    * They must be generated under closed rails, remain canonical and deterministic, and be tied to specific QA tokens (CONFIG\_REGISTRY\_OK, CONFIG\_MAGIC10\_OK) and tests.  
  * Cross-reference PF19’s config tokens and PF12’s new artifact descriptions, and state that manual editing of config artifacts, INDEX/mirror, or their path proofs is prohibited; all changes must flow through the canonical generators/writers.  
* **Doc:** PF14 — Canon-HDE-Mechanics Guide  
  **Section:** Config Mechanics & Registry (where registry loader and Magic-10/band thresholds are described)  
  **Delta:**  
  * Document tools/config/generate\_config\_artifacts.py as the canonical entrypoint for governed config artifacts under closed rails, and tools/config/artifacts.py as the source of Magic-10 and band-edges payloads.  
  * Clarify that math/thresholds.json is the input for band edges and that its edges, clamp, and rounding fields are reflected directly in band\_edges.json under PF14’s band mechanics.  
* **Doc:** PF20 — Canon-HDE-Phased Epics  
  **Section:** HDE-EPIC018 entry, D5 “Config Artifacts, Registry, and Acceptance Mapping” row  
  **Delta:**  
  * Extend the D5 row to list:  
    * Config generator: tools/config/generate\_config\_artifacts.py (closed-rails).  
    * Governed artifacts: registry.registry\_report, config.magic10, config.band\_edges, and epic018.config.acceptance\_map.  
    * Acceptance tokens: CONFIG\_REGISTRY\_OK, CONFIG\_MAGIC10\_OK (PF19).  
    * Evidence harness/tests: pytest tests/config and pytest tests/evidence/test\_machine\_mirror\_self\_proof.py plus the D4 sanity pipeline, as the acceptance evidence for D5.

# ADDENDUM 07 \- PR06 Review Summary

* This PR implements D6 for HDE-EPIC018 by adding typed backend and frontend config bundles built from the existing governed config artifacts (Magic-10 config, band edges, registry report) and the registry loader, and serializing them via the canonical JSON emitter.  
* It introduces a closed-rails bundle generator (engine/config/bundles.py \+ tools/config/generate\_bundles.py) that writes canonical FE/BE bundle JSON under artifacts/config\_bundles/, plus local JSON Schemas for FE/BE bundles used only in tests.  
* The PR wires both bundles into the PF12 evidence skeleton with path proofs, INDEX entries (config\_bundle.fe, config\_bundle.be), and mirror records, and refreshes the INDEX/mirror and topology orientation artifacts via update\_evidence\_index.py and orientation\_demo.py.  
* New tests (tests/config/test\_typed\_bundles.py) validate canonical formatting, two-run identity, JSON Schema conformance, and strict linkage back to governed config artifacts (including digests and sizes recorded in a sources block in each bundle).  
* CI runs the bundle generator under closed rails (via the same closed\_rails\_env helpers used in D5) and executes the new typed bundle tests alongside existing config and evidence tests, with the full D2–D5 harness remaining green.  
* I do not see any correctness, safety, or canon-alignment issues that require remediation; gaps are documentation-only (formalizing bundle tokens and artifact descriptions in PF-Canon).

## **Findings**

1. **Bundle generation obeys closed rails and canonical JSON rules.**  
   * engine/config/bundles.py calls require\_closed\_rails() before building bundles and writes them via canon.sercanon(..., sort\_keys=True), so generation is deterministic, UTF-8, sorted-key, compact JSON with a trailing LF, consistent with AGENTS and PF02/PF12 canonical serializer rules.  
2. **Bundles derive only from governed config artifacts and registry loader.**  
   * The BE/FE builders load config exclusively through load\_registry\_config (which is already hardened by PF14/PF12 for catalogs) and reuse the D5 helpers build\_magic10\_config and build\_band\_edges; their content is further checked in tests against artifacts/thresholds/magic10\_config.json, artifacts/thresholds/band\_edges.json, and artifacts/registry/registry\_report.json. This satisfies the D6 requirement that bundles be projections of governed config plus registry, not ad-hoc new sources.  
3. **Typed bundle structure matches the intended FE/BE scopes.**  
   * The backend bundle (config\_bundle.be.v1) exposes: full Magic-10 config (order, caps, seeds, schema), full band-edges payload (schema, source, bands, edges, clamp, rounding, version), full channel objects (id, gates, centers, circuit\_primary, substream, primary\_domain, domains, flags), centers, domains, alias\_policy, and a sources block with digests for each upstream artifact.  
   * The frontend bundle (config\_bundle.fe.v1) provides a slimmer view: Magic-10 order \+ caps, band edges/bands/clamp/rounding/version, channel ids \+ centers/domains \+ alias policy, and the same sources block. This aligns with PF14’s division between engine-internal vs client-facing semantics.  
4. **Local JSON Schemas are used correctly and kept non-canonical.**  
   * docs/schemas/config\_bundle\_fe.json and config\_bundle\_be.json define FE/BE structures (schema string, required sections, object shapes) and are only referenced from tests via jsonschema.validate; PF12’s canonical schema catalogs are untouched in this PR, which matches the Implementation Guide’s instruction to treat these as internal aids until PF-Canon is updated.  
5. **Evidence indexing and path proofs for bundles are complete and coherent.**  
   * The PR adds INDEX entries for config\_bundle.be and config\_bundle.fe pointing to artifacts/config\_bundles/be\_bundle.json and fe\_bundle.json, and update\_evidence\_index.py generates mirror records with matching sha256, size\_bytes, and proof\_anchor pointing to \*.path\_proof.txt.  
   * orientation\_demo.py is re-run in write mode, and the new orientation report (total\_artifacts: 134, status: ok) plus path proof are committed; orientation\_demo.py \--check and update\_evidence\_index.py \--check now pass under closed rails, so the new bundle artifacts are fully incorporated into the skeleton and topology snapshot.  
6. **Typed bundle tests are strong and aligned with D6 goals.**  
   * tests/config/test\_typed\_bundles.py uses closed\_rails\_env() to generate config artifacts and bundles, tests that FE/BE bundle bytes are identical across two runs (two-run identity), validates structures against the local JSON Schemas, and asserts that:  
     * FE/BE Magic-10 and band edges match D5 artifacts exactly.  
     * FE channel ids equal registry\_report\["artifacts"\]\["registry"\]\["channel\_ids"\].  
     * BE channels, centers, domains, and alias\_policy match the registry report.  
     * sources path/sha256/size\_bytes fields for each artifact line up with the current governed artifacts. This is sufficient coverage for a future CONFIG\_BUNDLES\_DETERMINISTIC\_OK token.  
7. **Exposure via engine.config is deliberate and low-risk.**  
   * engine/config/\_\_init\_\_.py re-exports build\_backend\_bundle, build\_frontend\_bundle, and generate\_bundles via \_\_all\_\_, giving other modules a stable, typed entrypoint to bundles without leaking implementation details (paths, schemas).  
   * Nothing in the PR wires these bundles into public Reader/CLI surfaces yet; they remain internal artifacts governed by PF12/PF09, which is appropriate for D6 Calcination work.  
8. **Remaining gaps are documentation, not code.**  
   * There is no PF-Canon entry yet for the new bundle token (CONFIG\_BUNDLES\_DETERMINISTIC\_OK), nor for the artifact\_keys config\_bundle.fe and config\_bundle.be and their roles; PF19/PF12/PF09/PF20 need small updates to record the semantics of D6 bundles and their acceptance tests.  
   * That doc work can be done separately; it does not undermine the correctness of this PR.

I do not see code-level issues that warrant remediation; I recommend accepting the PR and following up with the PF-Canon doc deltas below.

## **Doc Deltas (PF-Canon only)**

* **Doc:** PF19 — Glow QA Guide  
  **Section:** §9A “QA Acceptance Tokens Library” (Config & Evidence tokens)  
  **Delta (NEW CANON PROPOSAL):**  
  * Add token CONFIG\_BUNDLES\_DETERMINISTIC\_OK with semantics: “Typed frontend and backend config bundles (config\_bundle.fe, config\_bundle.be) are generated under closed rails from governed config artifacts and the registry loader, are canonical JSON, satisfy two-run identity, and are linked back to their sources by a sources digest block; tests tests/config/test\_typed\_bundles.py::test\_two\_run\_identity, ::test\_frontend\_bundle\_schema\_and\_sources, and ::test\_backend\_bundle\_schema\_and\_sources are green.”  
* **Doc:** PF12 — Canon-HDE-Schemas & Artifacts  
  **Section:** Evidence Index & Governed Artifacts (subsection for config and bundles)  
  **Delta:**  
  * Add config\_bundle.fe and config\_bundle.be to the governed artifacts list:  
    * artifact\_key: "config\_bundle.fe" → artifacts/config\_bundles/fe\_bundle.json, role bundle/snapshot.  
    * artifact\_key: "config\_bundle.be" → artifacts/config\_bundles/be\_bundle.json, role bundle/snapshot.  
  * Note that both bundles:  
    * Are written by tools/config/generate\_bundles.py using the canonical serializer,  
    * Have .path\_proof.txt siblings,  
    * Are indexed in docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl, and  
    * Contain a sources block with digests for magic10\_config, band\_edges, and registry\_report.  
  * Explicitly state that the FE/BE bundle JSON Schemas live under docs/schemas as local test aids and are not PF12 canonical schemas (yet).  
* **Doc:** PF09 — Canon-HDE-Build Checklist  
  **Section:** Phase I / Calcination — HDE-EPIC018 D5/D6 config tasks  
  **Delta:**  
  * Under the D6 row:  
    * Add a checklist item: “Generate typed FE/BE config bundles under closed rails via python tools/config/generate\_bundles.py (and/or the combined config generator), ensuring bundles are present and canonical at artifacts/config\_bundles/fe\_bundle.json and be\_bundle.json.”  
    * Add a second item: “Run pytest tests/config/test\_typed\_bundles.py to validate two-run identity, schema conformance, and linkage to governed config artifacts; any failure MUST block epic closure.”  
* **Doc:** PF14 — Canon-HDE-Mechanics Guide  
  **Section:** Config Mechanics & Bundle Consumers  
  **Delta:**  
  * Document D6 typed bundles as part of the config mechanics:  
    * Describe that the backend bundle (config\_bundle.be.v1) contains Magic-10 config, band edges, full channel rows, centers, domains, alias policy, and sources, for use by internal scoring and order/comparison logic;  
    * Describe that the frontend bundle (config\_bundle.fe.v1) contains a reduced Magic-10/caps view, band edges, channel ids plus centers/domains/alias policy, and sources, for use by clients and adapters.  
  * Reference engine/config/bundles.py and tools/config/generate\_bundles.py as the canonical generation path, and clarify that bundles are read-only projections of the governed config artifacts from D5.  
* **Doc:** PF20 — Canon-HDE-Phased Epics  
  **Section:** HDE-EPIC018 entry, D6 “Typed FE/BE Bundles” row  
  **Delta:**  
  * Extend the D6 row to list:  
    * Artifacts: config\_bundle.fe, config\_bundle.be under artifacts/config\_bundles/\*.json.  
    * Generator: tools/config/generate\_bundles.py (closed-rails).  
    * Acceptance tests: tests/config/test\_typed\_bundles.py (two-run identity, schema and source linkage), plus the D4 sanity pipeline job once it includes bundle checks.  
    * Token: CONFIG\_BUNDLES\_DETERMINISTIC\_OK (PF19), referencing PF12 and PF09 as the source of structural and process invariants.  
* **Doc:** PF04 — Canon-HDE-Governance & Tokens  
  **Section:** Evidence & Config Governance (subsection for config bundles)  
  **Delta (NEW CANON PROPOSAL):**  
  * Add a short note under Config Governance stating that typed bundles are governed artifacts, not runtime configuration switches:  
    * They MUST be generated under closed rails from the same governed config artifacts as D5.  
    * They MUST not include secrets or dynamic runtime state.  
    * Any change in bundle shape or content is treated as a config/evidence change and MUST be accompanied by updated evidence skeleton and tests.

# ADDENDUM 8 PR07 Review Summary

* This PR updates the repo-facing documentation (README.md, CHANGELOG.md, AGENTS.md, and several ./docs/\*\* files) so they now reflect the full scope of HDE-EPIC018: closed-rails determinism, CLI guard rails, evidence skeleton & sanity pipeline, governed config artifacts and acceptance map, typed FE/BE bundles, and the epic manifest/close report.  
* It removes or rewrites older EPIC017-centric and Alpha/A7-only copy, replacing it with concise EPIC018-aligned sections that point to PF-Canon titles where the normative rules live, and introduces two new docs (docs/config\_and\_bundles.md and docs/evidence/EPIC018\_evidence.md) to give a local, implementation-focused view of config/bundles and evidence posture.  
* The key bug addressed here was documentation drift: top-level docs still centered EPIC017 and earlier epics, mentioned outdated evidence practices (e.g. manual edits to the index/mirror), and did not describe the D1–D7 rails and artifacts. The PR realigns these docs to the current engine and evidence behavior without touching any ./docs/pfcanon canonical files.  
* No code, tests, or evidence artifacts were modified; CI passes for the repo, although the Codex run notes that no additional doc-specific tests were executed for this PR (“Not run (not requested)”), which is acceptable but worth tightening in future via a doc-lint harness.

## **Findings**

1. **README.md now reflects EPIC018 determinism & evidence posture (RCA).**  
   * RCA: The previous README was anchored to older epics (EPIC006/009/011/017) and Alpha transport, with long sections about the Reader harness, A7 transport, and EPIC-specific acceptance notes; it did not mention D1–D7 as EPIC018 outcomes and still implied that only EPIC017 close-out was complete.  
   * Fix: The new README opens with an EPIC018-centric description of Glow HD Engine and explicitly lists D1–D7, including canonical JSON rules, closed-rails env policy, CLI guards, evidence skeleton & sanity pipeline, governed config artifacts & acceptance map, typed FE/BE bundles, and the EPIC018 manifest & close report, plus a closed-rails “Quickstart” and an evidence-harness workflow. This is tightly aligned with the EPIC018 Implementation Plan and PF-Canon (PF12, PF19, PF20) by title.  
2. **CHANGELOG.md now has a clear EPIC018 entry.**  
   * It adds a 2025-12-02 — EPIC-018: HD Calcination Pass 3 close-out section summarizing what was added (determinism rails, CLI guards, evidence skeleton & sanity, D5 config artifacts & acceptance map, D6 typed bundles, D7 manifest & close report) and what changed (docs refreshed, deprecated guidance about manual evidence edits removed). This is consistent with EPIC018’s D1–D7 scope and leaves earlier entries intact.  
3. **AGENTS.md is simplified and brought under EPIC018 rails.**  
   * Old AGENTS content included a lot of EPIC011/017-specific instructions (DB bridge harness, S10 invariance chart, etc.) and only implicitly referenced EPIC018 rails.  
   * The new AGENTS.md explicitly sets PF-Canon as the hierarchy (PF12/PF19/PF20 by title), states “never hand-edit governed artifacts,” and focuses on:  
     * Roles: Codex/dev agents, evidence harness, config/bundle agents, doc agents.  
     * Rails: closed env via engine.runtime.determinism\_env.ensure\_determinism\_env, single emitter/serializer, CLI guards, evidence tools.  
     * Workflows: steps before merging governed changes (guards, regenerate artifacts, update evidence, run orientation & sanity, confirm manifest/close-pack).  
   * This matches PF-Canon’s process expectations and the EPIC018 rails without redefining canon.  
4. **Docs index and runbooks point to the correct EPIC018 surfaces and tools.**  
   * docs/INDEX.md now:  
     * Lists EPIC018 close-out artifacts (manifest, close report, config acceptance map) as governed and references PF20/PF19 by title.  
     * Points to the evidence index, orientation demo, sanity pipeline, CLI guards, config/bundle generators, and determinism helper.  
     * Provides an “Evidence posture crib,” “Config & bundles (D5/D6),” and “Epic references” sections aligned with EPIC018.  
   * docs/RUN.md has been rewritten as “Developer flight checks (EPIC018)” and now:  
     * Pins closed rails.  
     * Shows a short quick-check flow (env check, serializer parity test).  
     * Documents an evidence & guard workflow (CLI guards, evidence index update, orientation/demo, sanity pipeline).  
     * Documents config/bundles generation and acceptance map location.  
5. **Architecture docs encode emitter & guard semantics correctly.**  
   * docs/architecture/emitters.md now focuses on EPIC018: single emitter, canonical serializer, AB↔BA/two-run identity requirements, determinism helper, CLI guard tools, and evidence coupling via INDEX/mirror/orientation/sanity.  
   * docs/architecture/emitters\_guardrail.md now frames forbidden serializers (“json.dumps”, “jsonify”, etc.) specifically in governed CLI scope, strongly links to the serializer grep guard and emitter symbol proof tools, and explicitly states that both guard scripts call the determinism helper and that guard outputs are governed evidence.  
   * This is fully aligned with D3/D4 PF-Canon descriptions and D2’s rails.  
6. **CLI docs show EPIC018-aligned usage, guards, and evidence discipline.**  
   * docs/CLI\_commands.md now:  
     * Centers on closed-rails usage (engine.runtime.determinism\_env.ensure\_determinism\_env).  
     * Documents hdctl showcompat usage and exit codes, and clarifies that stdout is canonical, numeric-free JSON matching Reader bytes with AB↔BA and two-run identity.  
     * Has explicit “Guards (D3)” and “Evidence discipline (D4)” sections that reference the guard tools and evidence harness commands under PF05/PF12 titles.  
7. **New docs for config/bundles and EPIC018 evidence posture are well-scoped.**  
   * docs/config\_and\_bundles.md provides a concise D5/D6 view: governed config artifacts (Magic-10 bands, toggles), D5 acceptance map as governed evidence, typed FE/BE bundles and schemas, and the requirement to use the canonical tools and PF12 discipline.  
   * docs/evidence/EPIC018\_evidence.md documents the skeleton, orientation, sanity pipeline, evidence-update commands, and rails, all referencing PF12/PF19 by title and forbidding manual edits.  
   * These files are clearly “implementation docs” whose content is consistent with PF-Canon and do not re-state canonical rules.  
8. **Residual issues and gaps.**  
   * The docs PR itself did not run any repo tests in the Codex environment (“⚠️ Not run (not requested)”), but repo CI passes, and this PR is documentation-only; adding a doc-lint/Markdown check in future would tighten the process.  
   * PF-Canon already defines tokens and semantics; this PR does not attempt to introduce new tokens, but PF docs may want to reference these new repo docs explicitly (e.g., PF19 pointing to docs/evidence/EPIC018\_evidence.md as an implementation crib). That is documentation work outside this PR.

Given the above, I judge the PR acceptable as-is; no remediation prompt is needed.

## **Doc Deltas (PF-Canon only)**

* **Doc:** PF19 — Glow QA Guide  
  **Section:** §9A “QA Acceptance Tokens Library” / Implementation Cribs  
  **Delta:**  
  * Add a short note pointing to the new repo doc docs/evidence/EPIC018\_evidence.md as the implementation-level crib for evidence skeleton, orientation demo, and sanity pipeline for EPIC018 (title-only reference); clarify that PF19 remains normative, and repo docs are operational guides, not specs.  
* **Doc:** PF12 — HDE Schemas & Artifacts  
  **Section:** Evidence Index & Governed Artifacts  
  **Delta:**  
  * Mention that repository docs now include docs/config\_and\_bundles.md and updated docs/INDEX.md/docs/RUN.md as non-canonical implementation references for:  
    * D5 governed config artifacts and the EPIC018 config acceptance map, and  
    * D6 typed FE/BE bundles and their schemas under docs/schemas/.  
  * Clarify that these docs mirror PF12 expectations but PF12 remains the single source of truth for artifact shapes and indexing rules.  
* **Doc:** PF20 — Phased Epics  
  **Section:** HDE-EPIC018 entry, Close-Pack / Documentation row  
  **Delta:**  
  * Extend the D7/Close-Pack description to note that, in addition to the manifest and close report, EPIC018 includes a “repo docs alignment” step which refreshed README.md, AGENTS.md, CHANGELOG.md, and key ./docs/\*\* files to be consistent with PF-Canon and the EPIC018 manifest; these docs should be listed as part of the epic’s non-canonical but required deliverables.  
* **Doc:** PF06 — Epic Process  
  **Section:** Docs & Evidence Close-Out  
  **Delta (NEW CANON PROPOSAL):**  
  * Add a bullet under “Close-out tasks” stating that, for major epics like EPIC018, a final “repo docs sweep” MUST be performed to align top-level docs (README, CHANGELOG, AGENTS, non-pfcanon ./docs) with PF-Canon and the manifest/close report, and that this sweep must not change PF-Canon docs themselves.

