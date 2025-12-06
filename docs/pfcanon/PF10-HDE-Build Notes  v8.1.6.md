# 0\) Front Matter

**Name:** PF10-HDE-Build Notes   
**Version:** v8.1.6  
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

# ADDENDUM 1 — ADR: Phase Exit Criteria for Alchemical Phases

 Timestamp: 120225 16:00

Details:

This addendum records an Architectural Decision Record (ADR) for **phase exit criteria** in the alchemical delivery cycle for the Glow HD Engine. It is a **planning rule** to be drained into **HDE Phased Epics** as a short “Phase Exit Criteria” note and used by **Epic-Process-Guide** and **Glow Development Philosophy** as a reference when deciding whether to stay in the current phase or move to the next.

**Decision (phase exit criteria, per phase)**

1. **Close-out epic required.**  
    A phase is eligible to “exit” once at least one **close-out epic** in that phase has:

   * a complete epic record in **HDE Phased Epics** with `Status: Done` and a completed **Tokens and Evidence** roster for its D-goals, and

   * a close pack with Live QA evidence and Doc-Delta mapping that is indexed in the Human Evidence Index and Machine Mirror under the standard **HDE-Schemas & Artifacts** and **HDE-Build Checklist** discipline.

2. **No “Not done” foundation rows for the phase.**  
    For the phase being exited, **HDE-Build Checklist** must show:

   * no **Not done** rows for **foundation tasks** in that phase (Calcination foundations or phase-defining Dissolution/Separation tasks), and

   * any remaining **Not done** rows must be explicitly re-scoped into later phases or marked as “Won’t Do” in **HDE Phased Epics**, not left ambiguous in PF09. This follows PF13’s tenet that foundations must be clear before moving on, and that incomplete ideas must become explicit debt, not silent drift.

3. **Partial / Consolidation pending rows are debt, not blockers, when:**  
    Remaining **Partial** or **Consolidation pending** rows for a phase are treated as **carry-over debt** (not phase blockers) if and only if:

   * their notes in **HDE-Build Checklist** clearly show that they are **enhancements, tuning, or consolidation**, not missing foundational behavior, and

   * they are either:

     * linked to an **Outstanding Issue** row in **HDE Phased Epics §1**, or

     * explicitly called out in one or more future epic records as “Existing work / Debt to absorb,” so the next epic’s scope and acceptance can take them on.

4. **Tracked issues must be disposed of; none may be silently dropped.**  
    Before a phase exits, each epic in that phase that reaches `Status: Done` must:

   * list its tracked issues in **HDE Phased Epics §2.1.7**, and

   * for each issue, mark it as “Completed under \<EPIC\>”, “Carried forward to \<EPIC\>”, “Promoted to ISSUE-XXX”, or “Explicitly dropped (with rationale).”  
      A phase cannot be treated as exit-ready if any epic in that phase is `Done` in PF20 but still has unresolved, undocumented issues in reality. This aligns PF13’s “controlled change” and PF21’s phase-discipline guidance with PF20’s tracked issue rules.

5. **Phase exit is a planning decision; open work becomes cross-epic or next-phase scope.**  
    When criteria (1)–(4) are satisfied, **phase exit** is treated as a **planning decision**, not as an assertion that all work tagged with that phase is finished. Remaining work for that phase must be:

   * captured as cross-epic issues in **HDE Phased Epics §1**, or

   * explicitly listed as inputs to the next phase’s epics (for example, Dissolution sampler tuning carried into Separation’s error-envelope work).  
      This implements PF13’s instruction to avoid over-tuning and PF21’s expectation that phases do not mix: once the phase’s core aim is achieved and its debt is made explicit, new epics should be created in the next phase rather than reopening more epics in the current one.

**Applied example (Dissolution → Separation, HD Engine)**

6. **Current posture (informative, for draining later):**

   * **HDE-EPIC019 — Dissolution Pass 2** is `Done` in **HDE Phased Epics**, with D-goals (sampler core, deterministic Engine Core, dev sampler HTTP harness, sampler evidence & indexing, Live Vendor QA D6) accepted and evidenced under the standard PF06/PF09/PF12/PF19 rails.

   * **HDE-Build Checklist Phase II — Dissolution** has no **Not done** rows for its foundational tasks; remaining **Partial** cells are localized to sampler/pool tuning (`HDE-DISS003.x`) and are already represented as future work and Outstanding Issues in PF20, not as untracked gaps.

   * Cross-epic issues such as `ISSUE-017-STATELESS-JSON-QA`, `ISSUE-QA-TOKENS-LIBRARY`, and `ISSUE-APPENV-D3-GATING` are explicitly allocated in PF20 as ongoing, cross-phase concerns rather than as EPIC019-blocking tasks.

7. **ADR application (Dissolution exit):**  
    Under this ADR, the Dissolution phase for the HD Engine is now considered **exit-ready**:

   * Its designated close-out epic (**HDE-EPIC019**) is `Done` with D-goals accepted and Live QA complete.

   * No Dissolution foundation tasks remain Not done in **HDE-Build Checklist**; Partial rows are explicitly recognized as tuning/consolidation debt.

   * Cross-epic issues and residual Dissolution work are captured in **HDE Phased Epics §1** and will be scoped into future epics (likely under **Separation** and later phases), rather than keeping the meta-sprint parked in Dissolution.

**NEW CANON PROPOSAL (for later drain to “HDE Phased Epics”):**  
 Add a short **“Phase Exit Criteria”** note to **HDE Phased Epics** stating that a phase may be treated as complete for planning when:

* at least one epic in that phase is `Done` with all its D-goals accepted and evidence indexed;

* PF09 for that phase has no **Not done** foundation rows; and

* any remaining Partial or Consolidation pending tasks are explicitly carried forward as cross-epic issues or next-phase epic scope, with tracked-issue disposition per PF20 §2.1.7.

This proposal does **not** change current behavior; it formalizes the pattern already applied when leaving Calcination and now Dissolution, and should be implemented via a future PF20 Doc-Delta.

# ADDENDUM 2 \- PR01 HDE-EPIC020 

## **Review Summary**

* This PR wires HDE-EPIC020 into the acceptance infrastructure by adding `docs/acceptance_map_epic020.json`, `audit/EPIC020_MANIFEST.json`, extending `docs/acceptance_maps.json`, and creating EPIC020 QA harness roots (with READMEs) under `audit/qa/hde-epic020/**`.

* The EPIC020 acceptance map mirrors the EPIC017/019 pattern and PF20’s D1/D2/D3 token rosters, including a GLOBAL QA rails cluster, and now correctly references PF20 §2.5 via `pf20_ref: "PF20 §2.5 HDE-EPIC020"`.

* The manifest stub defines `epic_id: "HDE-EPIC020"` with a tokens→\[\] map that is token-complete relative to the acceptance map and PF20, and is appropriate for PR-1 scaffolding where no artifacts are bound yet.

* The consolidated index `docs/acceptance_maps.json` now lists EPIC017, EPIC019, and EPIC020 with map and manifest paths and continues to be validated by `tests/audit/test_acceptance_maps_index.py`, which passes in CI.

* New QA harness READMEs explicitly call out PF19’s “one command → one primary artifact” Live QA pattern and cleanly separate D1 errors, D2 CLI presenter/emitter, and D3 `/internal/version` identity, aligning with PF19 and PF20’s QA rail guidance.

I don’t see any remaining drift from the approved EPIC020 plan or PF-Canon for a scaffolding-only PR; no remediation is needed.

---

## **Findings**

1. **Scope is correctly limited to scaffolding; no behavior changes.**  
    The diff only touches acceptance and QA scaffolding: new EPIC020 acceptance map, manifest, QA harness READMEs, and an extension to `docs/acceptance_maps.json` plus its index test. There are no changes to engine logic, HTTP adapters, CLI behavior, serializers, or `/internal/version`, satisfying the Implementation Plan’s constraint that PR 1 must not change runtime behavior or add new tests beyond what’s needed to keep the index green.

2. **EPIC020 acceptance map structure and contents match PF20 and EPIC019 precedent.**  
    `docs/acceptance_map_epic020.json` uses the same “foundations” layout as the EPIC019 map: each deliverable (D1/D2/D3/GLOBAL) has `deliverable`, `name`, `status`, `tokens`, and `manifest_tokens`, and the D1/D2/D3 token lists exactly match PF20’s EPIC020 D-goal token definitions (error envelope, presenter/emitter, `/internal/version` identity) plus the GLOBAL QA rails tokens from PF19. The `pf20_ref` now correctly points to “PF20 §2.5 HDE-EPIC020”, aligning the map with its canonical epic record.

3. **Manifest stub is token-complete and consistent with the map.**  
    `audit/EPIC020_MANIFEST.json` declares `epic_id: "HDE-EPIC020"` and a `tokens` object whose keys are exactly the union of all EPIC020 tokens in the acceptance map (D1/D2/D3/QA). Each token maps to an empty list, following the EPIC017/019 pattern where detailed test/artifact bindings are added in later PRs. There are no extra or missing tokens relative to the map or PF20.

4. **Acceptance index file is extended cleanly and remains test-backed.**  
    `docs/acceptance_maps.json` now contains three records: EPIC017, EPIC019, and EPIC020. Each record includes `epic_id`, `epic_name`, a `path` to the acceptance map, and the more explicit `acceptance_map_path`/`manifest_path` fields for downstream tooling. The index test (`tests/audit/test_acceptance_maps_index.py`) still constructs `{epic_id: item["path"]}` and asserts that each referenced map exists and has a matching `epic_id`, and has been updated to include EPIC020; it passes in logs. This keeps the index aligned with PF06/PF12’s emphasis on governed, machine-checkable catalog/index files.

5. **QA harness READMEs align with PF19’s Live QA pattern and EPIC020’s D-goal split.**  
    The new `audit/qa/hde-epic020/README.md` and per-surface READMEs (`errors/`, `cli_presenter/`, `internal_version/`) clearly label D1, D2, and D3 surface responsibilities and explicitly mention PF19’s “one command → one primary artifact” requirement for QA runs. This matches PF19’s generalized Live QA rule and PF20’s requirement that EPIC-level QA harnesses live under `audit/qa/<epic-id>/…` with one primary artifact per step.

6. **pf20\_ref drift identified in r1 is corrected.**  
    In the earlier review, `pf20_ref` used a placeholder `"PF20 §2.x HDE-EPIC020"`. In the current PR, that is fixed to `"PF20 §2.5 HDE-EPIC020"`, matching PF20’s EPIC020 section heading format and following the pattern used by the EPIC019 acceptance map (e.g., `"PF20 §2.4 HDE-EPIC019"`). This restores the canonical cross-reference from repo acceptance artifacts back to PF-Canon.

7. **Test posture is minimal but appropriate for PR-1 scaffolding.**  
    The only test run is `pytest tests/audit/test_acceptance_maps_index.py`, which ensures that the consolidated index and all three acceptance maps exist and have matching `epic_id` values. Given this PR does not alter schemas, tokens semantics, or behavior, and only introduces scaffolding and an index entry, this minimal test coverage is acceptable and consistent with PF06’s guidance that planning/acceptance scaffolding can land with narrow but direct tests.

I don’t see any remaining issues that require remediation for this PR’s limited scope.

---

## **Doc Deltas (PF-Canon only)**

* None required for this PR. The changes are purely repo-level scaffolding (acceptance map/index, manifest shell, QA harness directories) that implement patterns already described in PF20 (epic records) and PF19 (QA rails/Live QA) without changing or extending canon.

---

# ADDENDUM 3 \- PRO2a HDE-EPIC020

## **Review Summary**

* This PR implements the “first half” of EPIC020 D1 by introducing a canonical governed error token map, upgrading `error_envelope` to emit `error_v1` JSON with `schema: "v1"` and typed `code` values, and routing writer and reader error surfaces through this single helper and the canonical serializer.

* The adapter is upgraded to expose `/internal/healthz` and `/internal/readyz` plus 404/405 handlers that all return canonical JSON via the shared emitter and match the existing `healthz_v1`, `readyz_v1`, and `error_v1` schemas, while leaving `/internal/version` unchanged and explicitly x-failing its schema tests for now, per the PR scope.

* CLI error handling is normalized so that argparse usage errors now exit with 64 (EX\_USAGE semantics), success writes only to stdout (LF-terminated), and engine/usage/file/JSON errors write only to stderr, with an expanded test matrix in `tests/cli/test_cli_usage_and_errors.py`.

* EPIC020 D1 tokens (`ERROR_JSON_CANON_OK`, `JSON_CANONICAL_CHECK_OK`, `ERROR_TOKEN_MAP_OK`, `CLI_STDOUT_LF_OK`, `CLI_STDERR_ONLY_ON_ERROR_OK`) are moved to PARTIAL in `docs/acceptance_map_epic020.json` and bound to concrete tests in `audit/EPIC020_MANIFEST.json`, without touching Evidence Index/Mirror or parity artifacts (which remain for PR 2b).

* A high-priority bug introduced by the new token map (the dev sampler APP\_ENV gate accidentally emitting `ERR_READER_FORBIDDEN` instead of `ERR_WRITER_FORBIDDEN` due to a shared `"forbidden"` alias) is fixed in this PR by switching `_dev_admin_gate` to call `_writer_error("ERR_WRITER_FORBIDDEN", ...)`, restoring the intended writer “insufficient scope” envelope for `/internal/dev/sampler` in non-dev APP\_ENV modes.

* Tests run and reported for this PR are `pytest tests/adapter/test_jsonschema.py` and `pytest tests/cli/test_cli_usage_and_errors.py`, which jointly cover the new error envelopes on health/ready/not-found surfaces and CLI stream/exit behavior; version/error schema tests for `/internal/version` are explicitly marked xfail to keep that surface in scope for later D3 work.

Overall, the PR is large but coherent, implements the PR 2a plan, and the one discovered regression (dev sampler forbidden token) is fixed in a simple, well-scoped way. I don’t see remaining issues that require remediation.

---

## **Findings**

1. **Canonical error token map and envelope are correctly introduced and used.**

   * `engine/compat/error_tokens.py` defines `ERROR_TOKEN_MAP` as the single home for governed error tokens, with UPPER\_SNAKE canonical `code` values for compat/reader inputs (`ERR_COMPAT_INVALID_JSON`, `ERR_INVALID_VIEWER_PREFS`, `ERR_MISSING_NARRATIVE_KEY`, `ERR_READER_*`) and for writer/diagnostic surfaces (`ERR_WRITER_*`) plus a generic `ERR_NOT_FOUND`. Aliases are provided for legacy lowercase codes such as `"invalid_json"`, `"invalid_prefs"`, `"forbidden"`, etc., matching existing PF-Canon naming.

   * `engine/compat/errors.py` now builds a legacy `ERROR_MESSAGES` alias map from `ERROR_TOKEN_MAP` purely to satisfy older tests, and `error_envelope(code, details=None)` canonicalizes any input code/alias via `canonical_token_for` then emits a numeric-free `{"schema": "v1", "ok": false, "code": "<ERR_*>", "error": "<message>"}` envelope (plus optional `details`), which matches `error_v1`’s `required` and `additionalProperties: false` schema.

2. **Adapter writer surfaces now consistently use the canonical error envelope and headers.**

   * `adapter/http_reader.py`’s `_writer_error` no longer hard-codes a message map; instead it calls `error_envelope(code)` and passes the result to `_emit_writer_response`, which uses `emit_compact_json` to produce LF-terminated JSON and sets `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, strips `ETag`, `Content-Encoding`, `Vary`, and sets `Content-Length` to the byte length of the canonical body.

   * All validation paths for the diagnostic writer route (`_read_writer_json`, `_require_admin_scope`, etc.) switch from aliases like `"invalid_content_type"`, `"invalid_json"`, `"invalid_input"`, `"unknown_key"`, `"request_too_large"`, `"unauthorized"`, `"forbidden"` to canonical writer tokens (`ERR_WRITER_INVALID_CONTENT_TYPE`, `ERR_WRITER_INVALID_JSON`, `ERR_WRITER_INVALID_INPUT`, `ERR_WRITER_UNKNOWN_KEY`, `ERR_WRITER_REQUEST_TOO_LARGE`, `ERR_WRITER_UNAUTHORIZED`, `ERR_WRITER_FORBIDDEN`). The tests in `tests/adapter/test_diagnostic_writer.py` now assert these canonical codes and the expected messages exactly, verifying the new contract.

3. **Reader `/reader` route is upgraded to use canonical reader tokens while preserving behavior.**

   * `adapter/http_reader.get_reader_bp` now calls `_error("ERR_READER_INVALID_VERSION")`, `_error("ERR_READER_FORBIDDEN", 403)`, `_error("ERR_READER_MISSING_PARAM")`, and converts validation `ValueError`s from `_safe_load_chart` and `_require_tz_or_raise` into canonical codes such as `ERR_READER_INVALID_CHART`, `ERR_READER_INVALID_PATH`, and `ERR_READER_MISSING_TZ_A/B`. `_error(token, code)` uses `error_envelope(token)` and returns a canonical `error_v1` JSON body plus status code. These changes align reader errors with the new token map without touching the successful Reader v1 envelope or its A7 semantics.

4. **Adapter WSGI stack now exposes canonical health/ready/error surfaces.**

   * `adapter/wsgi.create_app` is expanded to register both `reader_bp` and `compat_blueprint`, install the logging filter and env guard, and define `/internal/healthz` and `/internal/readyz` as simple JSON endpoints returning `{"ok": true, "schema": "v1"}`. These are wrapped in `_apply_common_headers`, which sets `Cache-Control: no-store`, `Content-Type: application/json; charset=utf-8`, `X-Adapter-Version`, `X-Engine-Tag`, `X-Release-Id`, `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options`, and conditionally `Strict-Transport-Security` in prod, matching the expectations in the health/headers tests.

   * 404 and 405 errors are centralized using Flask error handlers that call `error_envelope("ERR_NOT_FOUND")` and wrap the `error_v1` envelope in the same header policy. `tests/adapter/test_jsonschema.py::test_notfound_uses_error_schema` validates that `/nope` in dev returns a 404 whose body ends with `\n` and matches the `error_v1` JSON schema, and the test suite for adapter headers (healthz/readyz) is consistent with these changes.

5. **`/internal/version` is intentionally left for a later phase and tests are xfailed accordingly.**

   * The version schema (`version_v1.schema.json`) expects a richer identity document with `ok`, `schema`, `engine_tag`, `release_id`, `checksums`, `toggles_sha`, and `build{commit,timestamp}`, but `/internal/version` still returns only `engine_tag`, `release_id`, `invocation_tag`, `build_commit`, `emitter_sha256`, etc. Rather than silently changing `/internal/version` in this PR, the version tests in `tests/adapter/test_jsonschema.py` (`test_version_schema_ok_dev`, `test_error_envelope_schema_on_unauthorized_prod`) are marked `xfail` with `reason="/internal/version untouched in PR scope"`, so the adapter JSON schema checks still run for healthz/readyz/not-found but explicitly treat version as out-of-scope until D3. This matches the PR 2a plan (no `/internal/version` changes yet) and avoids accidental contract drift for that surface.

6. **CLI error stream discipline is enforced and tested.**

   * In `engine/cli/main.py`, the top-level `cli()` function now intercepts `SystemExit` raised by `argparse` and maps non-zero codes to 64 and zero to 0, so usage errors return 64 while `--help` exits cleanly with 0\. All CLI errors raised via `CliError` still produce a single error code line on stderr and the provided `exit_code`, and unhandled exceptions continue to yield `CLI_UNEXPECTED:…` with exit code 1\.

   * `tests/cli/test_cli_usage_and_errors.py` is expanded to cover:

     * `test_missing_file_returns_64_and_stderr` and `test_bad_json_returns_64_and_stderr`: file/JSON failures exit 64, write nothing to stdout, and write a non-empty error line to stderr.

     * `test_success_writes_stdout_only`: a synthetic valid pair file causes `hdctl showcompat` to exit 0, with LF-terminated JSON on stdout and empty stderr.

     * `test_usage_error_writes_stderr_only`: invoking `hdctl` with no args yields exit 64, no stdout, and usage text on stderr.

     * `test_engine_error_writes_stderr_only`: a vendor path error results in exit 1, empty stdout, and a newline-terminated error line on stderr (exact code is not asserted, only presence and newline).  
        These tests collectively satisfy `CLI_STDOUT_LF_OK` and `CLI_STDERR_ONLY_ON_ERROR_OK` for the D1 error flows.

7. **Acceptance map and manifest wiring for EPIC020 D1 tokens is correct and conservative.**

   * `audit/EPIC020_MANIFEST.json` now records, for D1 tokens:

     * `CLI_STDOUT_LF_OK`: bound to `tests/cli/test_cli_usage_and_errors.py::test_success_writes_stdout_only`.

     * `CLI_STDERR_ONLY_ON_ERROR_OK`: bound to the four CLI error tests.

     * `JSON_CANONICAL_CHECK_OK` and `ERROR_JSON_CANON_OK`: bound to `test_error_envelope_schema_on_unauthorized_prod` and `test_notfound_uses_error_schema` in `tests/adapter/test_jsonschema.py`.

     * `ERROR_TOKEN_MAP_OK`: bound to the five diagnostic writer tests validating content-type, JSON, unknown keys, size cap, and non-object payloads.

   * `docs/acceptance_map_epic020.json` mirrors this by populating `token_status` with `status: "PARTIAL"` and the same test lists for these tokens. Evidence tokens (`EVIDENCE_INDEX_*`) and parity tokens remain unbound and “pending”, as intended for PR 2a.

8. **RCA: dev sampler APP\_ENV gate emitting reader forbidden envelope.**

   * **Root cause:** Before PR 2a, `_dev_admin_gate` in `adapter/http_reader.py` called `_writer_error("forbidden", status=403)` to signal that `/internal/dev/sampler` is restricted outside dev/test/local. After introducing `ERROR_TOKEN_MAP` and `canonical_token_for`, `"forbidden"` became an alias for both `ERR_READER_FORBIDDEN` and `ERR_WRITER_FORBIDDEN`. Because `canonical_token_for` iterates `ERROR_TOKEN_MAP` in order, `"forbidden"` resolved to the first match: `ERR_READER_FORBIDDEN`. This caused the dev sampler APP\_ENV gate to emit the reader forbidden envelope (`code: "ERR_READER_FORBIDDEN", error: "reader endpoint disabled"`) instead of the intended writer forbidden envelope (`ERR_WRITER_FORBIDDEN`, “insufficient scope”), changing the governed error contract for that internal writer surface.

   * **Fix:** The bug fix patch for this PR switches `_dev_admin_gate` from `_writer_error("forbidden", ...)` to `_writer_error("ERR_WRITER_FORBIDDEN", status=403)`, bypassing alias resolution and guaranteeing that APP\_ENV gating for `/internal/dev/sampler` always yields the writer forbidden token. This is consistent with other writer surfaces, which now use explicit `ERR_WRITER_*` codes, and with PF-Canon’s separation between reader and writer surfaces.

   * **Why it was not caught earlier:** PR 2a correctly refactored most call sites to canonical tokens, but `_dev_admin_gate` remained on the legacy `"forbidden"` alias. There was no dedicated test asserting the *token* returned by `/internal/dev/sampler` under closed APP\_ENV rails, only higher-level EPIC019 sampler harnesses that were not wired into this PR’s CLI/adapter test set. The bug surfaced when Codex review reasoned through `canonical_token_for("forbidden")` and identified the mismatch.

   * **How tests/evidence confirm the fix:** Although no new dedicated dev sampler test is added in this PR, the fix is local, explicit, and consistent with the new error token map. Other writer surfaces already use `ERR_WRITER_FORBIDDEN`, and the error envelope helper plus diagnostic writer tests confirm that writer tokens map to the correct messages and error\_v1 schema. EPIC019’s existing dev sampler QA harnesses (run under closed rails) will now see the writer forbidden token again, aligning behavior with the approved rails posture. Residual risk is low; as a follow-up, a small EPIC019/EPIC020 dev sampler QA test that asserts the exact forbidden code in non-dev APP\_ENV would fully close this gap.

9. **Residual risks and follow-ups.**

   * The alias `"forbidden"` still exists for both reader and writer forbidden tokens; the explicit fix in `_dev_admin_gate` avoids the ambiguous path, and other call sites use canonical tokens, but more generic use of alias-only codes in new code would be risky. This is mitigated by the current patterns (canonical codes in adapter and reader) but worth calling out in code review guidelines.

   * `/internal/version` remains non-conforming to `version_v1` and has xfailed tests; this is deliberate and should be addressed in the D3 PR according to the EPIC020 plan, not here.

---

## **Doc Deltas (PF-Canon only)**

* Doc: PF05 — Canon-HDE-CLI-API-Vendor-Ref  
   Section: error response semantics for compat/writer surfaces (the section that currently describes typed errors like `invalid_json`, `invalid_prefs`, and `missing_narrative_key`).  
   Delta: Update the description of HTTP error `code` values to state that the canonical codes are now UPPER\_SNAKE tokens from a governed map (e.g., `ERR_COMPAT_INVALID_JSON`, `ERR_INVALID_VIEWER_PREFS`, `ERR_MISSING_NARRATIVE_KEY`, `ERR_WRITER_INVALID_CONTENT_TYPE`, `ERR_WRITER_INVALID_JSON`, etc.), and that lowercase names such as `invalid_json`/`invalid_prefs` are maintained as aliases for backward compatibility in internal code and tests. This aligns PF05 with the new token map and error\_v1 envelopes implemented in this PR.

* Doc: PF14 — Canon-HDE-Mechanics Guide  
   Section: error\_v1 schema and adapter transport (the section that defines the error JSON schema and describes error vs success surfaces).  
   Delta: Clarify that all governed error surfaces now emit `error_v1` envelopes via `error_envelope`, which sets `schema: "v1"`, `ok: false`, canonical `code` tokens, and `error` messages drawn from `ERROR_TOKEN_MAP`, and that adapter-level health/ready/404/405 surfaces now use this schema consistently where appropriate. Also note the existence of the canonical error token map and alias behavior, with `ERR_NOT_FOUND` as the canonical code for adapter 404/405.

* Doc: PF20 — Canon-HDE-Phased Epics  
   Section: EPIC020 D1 — Error Envelope & Token Set (the HDE-EPIC020 Epic Plan subsection).  
   Delta: Confirm/clarify that the D1 tokens `ERROR_JSON_CANON_OK`, `JSON_CANONICAL_CHECK_OK`, `ERROR_TOKEN_MAP_OK`, `CLI_STDOUT_LF_OK`, and `CLI_STDERR_ONLY_ON_ERROR_OK` are now partially satisfied by the specific tests recorded in `audit/EPIC020_MANIFEST.json` and `docs/acceptance_map_epic020.json` (naming the test modules generically), and note that Evidence Index/Mirror and parity artifacts remain for D1 PR 2b. This is a documentation alignment, not new canon.

(If PF05/PF14 already refer to the `ERR_*` tokens explicitly, these deltas are effectively clarifications; apply them only where the docs still name the older lowercase codes as the public `code` values.)

---

# ADDENDUM 4 — Tie error evidence generators to orientation demo

Timestamp: 120425 05:30

Details:

During HDE-EPIC020 PR 2b (“D1 error parity, headers, artifacts, and Evidence Index wiring”), CI failed in the final evidence step:

* `python tools/evidence/update_evidence_index.py --check` passed, confirming the Human Index, sentinel, and Machine Mirror were internally consistent after adding new error artifacts under `errors/*` and `parity/*`.

* `python tools/evidence/orientation_demo.py --check` then emitted `ORIENTATION_DRIFT` and exited non-zero, because `audit/gates/topology/orientation_demo.txt` and its path proof still reflected the pre-PR evidence skeleton (older `total_artifacts` and layout) even though the Index/Mirror had been expanded to include the new EPIC020 D1 error artifacts.

Root cause:

* PF09 and PF14 make orientation\_demo part of the canonical “evidence skeleton” workflow: any PR that changes governed evidence under `docs/evidence/**`, `artifacts/**`, or `audit/**` must use the canonical tools to update *both* the Index/Mirror (`update_evidence_index.py`) and the topology orientation report (`orientation_demo.py`), then validate both with their `--check` variants in the same PR.

* PR 2b followed the first half of that workflow (ran `update_evidence_index.py` in write mode and `--check`, and committed new Index/Mirror entries for error-parity and schema artifacts) but did not run `orientation_demo.py` in write mode before CI. As a result, `orientation_demo.py --check` saw a real drift (new artifacts in Index/Mirror vs old orientation report) and correctly failed CI with ORIENTATION\_DRIFT.

* The new error evidence generator (`tools/errors/generate_error_artifacts.py`) is not wired to orientation\_demo at all; it refreshes governed error artifacts and calls the evidence index updater, but leaves orientation demo as a manual, easy-to-forget step. This is a design gap in the current evidence workflow.

Implications:

* Any future PR that adds or removes governed artifacts and updates INDEX/Mirror via the canonical tools, but forgets to run `orientation_demo.py` in write mode, will reproduce the same ORIENTATION\_DRIFT CI failure even if all tests and index checks are green.

* The dev sampler APP\_ENV gating bug that surfaced in PR 2a (fixed by switching to `ERR_WRITER_FORBIDDEN`) shows that error evidence is now a first-class part of the topology skeleton: parity and schema artifacts live in the same Index/Mirror/Orientation graph as sampler/core artifacts, so orientation drift is no longer just a sampler/topology concern.

Proposed resolution to drain into PF-Canon:

* For PF09 (HDE-Build Checklist), tighten the “Evidence index touch discipline” language so that any task or epic that calls `update_evidence_index.py` in write mode is REQUIRED to also call `orientation_demo.py` in write mode and commit the updated `audit/gates/topology/orientation_demo.txt` and `*.path_proof.txt` in the same PR, before running `--check`.

* For PF14 (Mechanics Guide), extend the evidence-jobs section to treat `orientation_demo.py` as part of the *same* single-writer pipeline as `update_evidence_index.py` for the evidence skeleton: “Index/Mirror changes without a fresh orientation demo are out of spec and MUST fail CI via ORIENTATION\_DRIFT.”

* For EPIC020 and future error evidence work, strongly prefer a single closed-rails harness (script or make target) that runs, in order:

  1. the error evidence generator (`tools/errors/generate_error_artifacts.py`),

  2. `python tools/evidence/update_evidence_index.py` (write) \+ `--check`,

  3. `python tools/evidence/orientation_demo.py` (write) \+ `--check`,  
      and treats all four steps as one atomic evidence job per PR. This harness should be the default way to refresh error evidence and avoid evidence skeleton/orientation skew.

Evidence:

* CI logs from PR 2b show `update_evidence_index.py --check` passing and `orientation_demo.py --check` failing with ORIENTATION\_DRIFT immediately afterward, with no other test failures.

* Diffs for PR 2b show new error artifacts (`parity/errors_reader_cli.*`, `errors/schema_check/*`, `errors/token_map/token_map.json`) and updated Index/Mirror entries, but no changes to `audit/gates/topology/orientation_demo.txt` or its path proof.

# ADDENDUM 5 \- PR02b HDE-EPICO20

## Review Summary

* This PR implements the “second half” of EPIC020 D1 by adding a governed error parity harness (`tools/errors/generate_error_artifacts.py` \+ `tests/cli/test_errors_parity.py`), generating deterministic error artifacts under `parity/*` and `errors/*`, and wiring them into the Evidence Index and Machine Mirror with EPIC020 metadata.

* It adds a transport snapshot and header test for the diagnostic writer route (`tests/transport/headers/no_store_writers_errors.snap` \+ `tests/transport/test_writers_errors_headers.py`) to enforce PF04’s writer/error header posture (UTF-8 JSON, `Cache-Control: no-store`, no ETag) for both success and 401 error paths.

* Error schema logs (`errors/schema_check/error_envelope_invalid_*.log`) and a token map snapshot (`errors/token_map/token_map.json`) are produced under closed rails, with path-proofs and Evidence Index/Mirror entries keyed as `ERROR_SCHEMA_CHECK_V1`, `ERROR_TOKEN_MAP_V1`, and `ERRORS_READER_CLI_PARITY_V1`, bringing error evidence into the same skeleton as sampler/core artifacts.

* EPIC020 D1 tokens in `docs/acceptance_map_epic020.json` and `audit/EPIC020_MANIFEST.json` are updated to DONE and bound to specific tests and artifacts (schema tests, CLI error tests, parity harness, token map snapshot, evidence skeleton tests), closing the loop from behavior to indexed evidence without touching Reader v1 success or `/internal/version` behavior.

* CI logs show the new harness running under determinism pins (LC\_ALL=C, LANG=C, TZ=UTC, SAFE\_MODE=1, ALLOW\_NETWORK=0, APP\_ENV=dev) for adapter JSON schema tests, CLI usage/error tests, and the new parity tests, all passing; there are no new test failures or rails violations.

I judge the PR acceptable as-is; it matches the PR 2b plan, respects PF-Canon, and provides the expected behavior \+ evidence for D1.

---

## **Findings**

1. **Error parity harness and artifacts are correctly implemented under closed rails.**

   * `tools/errors/generate_error_artifacts.py` defines `write_parity_artifacts()`, pins determinism env via `ensure_determinism_env`, iterates over `SCENARIOS`, and for each scenario captures HTTP and CLI results via `capture_http`/`capture_cli`, then writes HTTP JSON bodies and CLI text logs under `parity/errors_reader_cli.{scenario}.http.json` and `.cli.txt`. At the end it generates schema logs under `errors/schema_check/*` and a token map snapshot under `errors/token_map/token_map.json`, plus a parity README describing the scenarios.

   * The CLI parity test module `tests/cli/test_errors_parity.py` is marked `pytest.mark.epic020`, applies the determinism pins for every test, and defines `test_http_and_cli_parity` parametrized over `SCENARIOS`. For each case it reads the stored HTTP artifact, calls `capture_http`, asserts `body.code == scenario.token` and that the token is in `ERROR_TOKEN_MAP`, and checks exact equality with the stored JSON; it then does the same for the CLI artifacts, asserting non-zero return code, empty stdout, stderr containing a scenario-specific expectation, and exact equality with the stored CLI text. A separate `test_token_map_snapshot_matches_canonical` verifies that `errors/token_map/token_map.json` equals `render_token_map()` and that every `code` in the snapshot appears in `ERROR_TOKEN_MAP`.

   * This aligns with PF19’s CLI parity guidelines: error parity is exercised under closed rails, HTTP and CLI error envelopes are aligned and numeric-free, and artifacts are captured and indexed as governed evidence.

2. **Error schema logs and token map snapshot give concrete evidence for envelope & map tokens.**

   * `errors/schema_check/error_envelope_invalid_json.log` and `error_envelope_invalid_viewer_prefs.log` are small text logs recording the scenario name, HTTP status, canonical `code` (`ERR_COMPAT_INVALID_JSON` and `ERR_INVALID_VIEWER_PREFS`), and `schema: ok`, demonstrating that `error_v1` envelopes for these scenarios are schema-valid. Each has a path-proof with size, sha256, mtime\_utc, and produced\_at\_utc recorded.

   * `errors/token_map/token_map.json` is a JSON array of records, each with `aliases`, `code`, and `message` for error tokens such as `ERR_COMPAT_INVALID_JSON`, `ERR_INVALID_VIEWER_PREFS`, `ERR_MISSING_NARRATIVE_KEY`, `ERR_NOT_FOUND`, reader codes, and writer codes (including `ERR_WRITER_FORBIDDEN`, `ERR_WRITER_INVALID_CONTENT_TYPE`, etc.). A path-proof records its hash and size.

   * The parity test `test_token_map_snapshot_matches_canonical` asserts that the on-disk snapshot equals `render_token_map()` and that every `code` appears in `ERROR_TOKEN_MAP`, providing a direct behavioral check that the snapshot and runtime token map are in sync. Together with the schema logs, this is strong evidence for `ERROR_JSON_CANON_OK`, `JSON_CANONICAL_CHECK_OK`, and `ERROR_TOKEN_MAP_OK`.

3. **Writer/error header posture is snapshotted and enforced per PF04.**

   * `tests/transport/headers/no_store_writers_errors.snap` defines two sections, `[success]` and `[error]`, each capturing expected status, `cache-control: no-store`, `content-type: application/json; charset=utf-8`, and lengths; the error section also requires `www-authenticate: Bearer`.

   * `tests/transport/test_writers_errors_headers.py` loads the snapshot, uses `adapter.http_reader.app.test_client()` under EPIC020 rails (`APP_ENV=dev`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, test tokens set), and calls `/ops/writer/diagnostic` twice: once with an admin token expecting the “success” snapshot and once with a wrong token expecting the “error” snapshot. `_headers()` lower-cases header keys and asserts that `etag` is absent; then it asserts that the actual headers match the snapshot fields for each case.

   * PF04’s Appendix D.4 already lists `tests/transport/headers/no_store_writers_errors.snap` as the canonical writer/error header snapshot. This PR brings that snapshot into existence and wires it to a concrete test, fully enforcing the “no-store, no ETag” writer/error posture under D1 without touching Reader A7 surfaces.

4. **Evidence Index and Mirror entries for new error artifacts are consistent with PF12.**

   * The Evidence Index gains new entries with artifact\_keys `ERRORS_READER_CLI_PARITY_V1`, `ERROR_SCHEMA_CHECK_V1`, and `ERROR_TOKEN_MAP_V1` pointing to the parity artifacts, schema logs, and token map snapshot under `parity/*`, `errors/schema_check/*`, and `errors/token_map/token_map.json`. The Machine Mirror contains corresponding JSONL records, including a `topology.orientation_demo` entry and existing sampler/bodygraph artifacts.

   * Path-proofs for the new error artifacts and for touched pre-existing artifacts (`tests/transport/headers/aux_*`, sampler schemas, PF09 audit reports) are updated mechanically by the evidence index tool, with only mtime and hash changes, indicating that they reflect the new artifact set without manual editing.

   * While orientation\_demo refresh is handled in a follow-up PR, the Index and Mirror structure in this PR is internally coherent; CI logs in this PR show index checks passing, and there are no signs of malformed Mirror records or missing proofs for the new error artifacts. This satisfies the D1 evidence-side tokens once orientation is brought in line.

5. **EPIC020 D1 tokens are wired to tests and artifacts as planned.**

   * The acceptance map’s `token_status` block is updated so that D1 tokens `ERROR_JSON_CANON_OK`, `JSON_CANONICAL_CHECK_OK`, `ERROR_TOKEN_MAP_OK`, `CLI_READER_EMITTER_PARITY_OK`, `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_MIRROR_OK`, and `EVIDENCE_PATHS_VALIDATED_OK` are set to `status: "DONE"`, with `tests` and `artifacts` lists populated. For example, `ERROR_JSON_CANON_OK` and `JSON_CANONICAL_CHECK_OK` list adapter schema tests and `tests/cli/test_errors_parity.py::test_http_and_cli_parity` plus the two schema logs; `ERROR_TOKEN_MAP_OK` adds diagnostic writer tests and the token map snapshot; the evidence index tokens bind to `tests/evidence/test_evidence_skeleton.py`, `tests/ops/test_evidence_index.py`, and Machine Mirror self-proof tests.

   * `audit/EPIC020_MANIFEST.json` is updated consistently via `update_token(...)` calls: the same test names and artifact paths appear there for each token, matching PF20’s expectation that acceptance decisions are backed by specific tests and evidence families, and aligning D1 acceptance wiring with the PR 2b plan.

6. **Tests and rails posture are adequate for D1 scope.**

   * Local logs show `pytest tests/adapter/test_jsonschema.py` (with two known xfails for `/internal/version`), `pytest tests/cli/test_cli_usage_and_errors.py`, and `pytest tests/cli/test_errors_parity.py` all running under `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0` with APP\_ENV=dev and passing. The parity tests include a `pytestmark = pytest.mark.epic020` and apply determinism pins via an autouse fixture, satisfying PF19’s closed-rails requirement for CLI/HTTP QA.

   * There are no changes to Reader v1 success or `/internal/version`, and no CI evidence of regressions in other epic evidence tests; the PR’s changes are tightly scoped to D1 error parity, headers, and evidence, as required.

7. **Minor note: error parity scenarios are intentionally narrow.**

   * The current SCENARIOS cover two data-validation errors: compat invalid JSON and invalid viewer\_prefs. PF19 also calls out error parity for DB-unavailable and closed-rails vendor scenarios; those cases remain for future epics or D-goals. The present selection is consistent with EPIC020’s D1 scope (error envelope & token set), but should be expanded later if PF19 error parity expectations extend to vendor/DB errors for this epic.

Given the epic’s scope and PF-Canon, I don’t see any issues that require remediation now; the narrow scenario set is acceptable for D1 but worth revisiting in future epic QA work.

---

## **Doc Deltas (PF-Canon only)**

* Doc: PF12 — Canon-HDE-Schemas and Artifacts  
   Section: §8.6 “Evidence skeleton entries” (or the existing section that lists artifact\_key families for CLI/API evidence).  
   Delta: Add the three new error evidence families as named artifact keys: `ERRORS_READER_CLI_PARITY_V1` (pointing to `parity/errors_reader_cli.*`), `ERROR_SCHEMA_CHECK_V1` (pointing to `errors/schema_check/error_envelope_*.log`), and `ERROR_TOKEN_MAP_V1` (pointing to `errors/token_map/token_map.json`) as the canonical EPIC020 D1 error evidence entries in the skeleton, with a short note that they support tokens `CLI_READER_EMITTER_PARITY_OK`, `ERROR_JSON_CANON_OK`, `JSON_CANONICAL_CHECK_OK`, and `ERROR_TOKEN_MAP_OK`.

* Doc: PF04 — Canon-HDE-Governance  
   Section: Appendix D.4 “Endpoint Catalog & transport proofs (Reader A7)” under the “Writer/error posture (headers-only)” bullet list.  
   Delta: Confirm that `tests/transport/headers/no_store_writers_errors.snap` and its companion test `tests/transport/test_writers_errors_headers.py` are the canonical enforcement mechanism for writer/error header posture, explicitly mentioning the success/error sections and the requirement that writer diagnostics send `Cache-Control: no-store`, UTF-8 JSON, and no ETag on both success and error responses (this is more a clarification than new canon, since the snapshot is already named there).

(These deltas clarify how the new artifacts and tests fit into existing PF-Canon; they do not introduce new tokens or behavior.)

---

# ADDENDUM 6 \- PR03 HDE-EPIC020

## **Review Summary**

* This PR implements D2 of HDE-EPIC020 (“Public Presenter / Emitter”) by centralizing all governed public JSON emission behind `engine.presenter.emitter`, so both Reader/compat HTTP surfaces and the CLI `showcompat` command use a single allow-listed emitter \+ canonical serializer, without changing Reader v1 schema or idempotence math.

* It adds a presenter identity harness (`tools/presenter/generate_presenter_artifacts.py`) that runs under closed rails and produces deterministic presenter artifacts under `artifacts/presenter/*` (two-run and AB↔BA bytes, Reader/CLI parity bytes, preimage recompute logs, and a showcompat identity summary), which are registered in the Evidence Index and Machine Mirror under new `PRESENTER_*` artifact\_keys.

* CLI tests are extended so that `test_cli_canonical_bytes.py` proves `showcompat` emits LF-terminated canonical JSON that matches `emitter.emit_public`, `test_showcompat_parity_and_identity.py` proves two-run identity, AB↔BA identity, Reader dump parity and preimage recompute parity, and `test_serializer_guards.py` asserts that governed CLI handlers use only the allow-listed emitters and no ad-hoc `json.dumps`.

* EPIC020 D2 tokens (`CLI_SHOWCOMPAT_CANON_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `PREIMAGE_RECOMPUTE_OK`) are now marked DONE and wired to these tests and presenter artifacts in both `docs/acceptance_map_epic020.json` and `audit/EPIC020_MANIFEST.json`, and earlier structural issues (duplicated keys / malformed arrays) have been fixed in a follow-up patch so that both files are valid JSON and consistent with each other.

* Evidence skeleton jobs (`update_evidence_index.py --check`, `orientation_demo.py --check`) pass under closed rails after the new presenter artifacts and path-proofs are added, keeping the Evidence Index, Machine Mirror, and orientation demo in lockstep. There are no changes to `/internal/version` behavior or Reader v1 success semantics, and no drift from PF-Canon is introduced.

---

## **Findings**

1. **Presenter/emitter centralization and rails alignment**

   * The emitter layer now exposes a clear, single public entrypoint (`emit_public(envelope, sort_keys=True)`) that delegates to the canonical serializer for LF-terminated, deterministic bytes, plus a companion `emit_public_with_envelope` for callers needing `(bytes, envelope)` and a compatibility alias `emit_compact_json` that just forwards to the canonical emitter.

   * Reader and compat HTTP routes that return governed JSON (Rails probes, dev sampler success, compat IDs-only responses, health/ready endpoints) and CLI `showcompat` now consistently use these entrypoints; there are no remaining ad-hoc `json.dumps` call sites for governed public JSON. This is in line with PF14’s single-emitter intent and respects PF01/PF05 by not touching Reader v1 schema or idempotence math.

2. **CLI showcompat canonical bytes and stream discipline**

   * `showcompat` now builds its payload and emits it via `emitter.emit_public`, with no stderr output on success and exit code 0; any error/pathological conditions still follow the D1 rails (stderr-only, non-zero exit code).

   * `tests/cli/test_cli_canonical_bytes.py` proves:

     * `showcompat` stdout is canonical JSON (matching the canonical serializer).

     * The final line is LF-terminated.

     * stderr is empty.

     * The bytes returned by `emitter.emit_public` over the payload are exactly equal to the CLI’s stdout.

   * Together with the existing D1 CLI error tests, this satisfies `CLI_SHOWCOMPAT_CANON_OK` for the presenter path and reinforces `CLI_STDOUT_LF_OK` and `CLI_STDERR_ONLY_ON_ERROR_OK` in the D2 context.

3. **Two-run and AB↔BA identity proofs for presenter surfaces**

   * The identity test suite now covers:

     * Two-run identity: two separate `showcompat` invocations under closed rails produce byte-identical stdout and stderr, and the presenter artifact for AB (e.g. `artifacts/presenter/showcompat_ab.bytes`) is asserted equal to the CLI bytes, with re-emission via `emit_public` reproducing the same bytes.

     * AB↔BA identity: swapping left/right inputs for showcompat yields the same canonical JSON; CLI artifacts (AB and BA JSON) and presenter artifacts (`showcompat_ab.bytes`, `showcompat_ba.bytes`) all agree.

     * Reader dump parity: `showcompat`’s `--dump-reader` path produces the same bytes as the presenter’s Reader emitter, and the Reader CLI parity artifact matches those bytes; idempotence hashes computed from the canonical preimage match those embedded in the Reader envelope.

     * Preimage recompute: a preimage recompute log is written and tests assert that its computed digest matches both the preimage bytes and the stored hash in the associated envelope.

   * These tests are appropriately wired to D2 tokens (`TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, `PREIMAGE_RECOMPUTE_OK`), and they respect PF01’s identity math by recomputing rather than redefining the preimage.

4. **Serializer guard coverage for presenter flows**

   * The serializer guard tools and tests have been updated so the allow-listed canonical emitters for CLI are exactly `emit_reader_public_envelope` and `emitter.emit_public`; the guard test verifies that the current repo state passes and that the CLI guard report identifies `showcompat` as using only these emitters.

   * A negative test still injects a dummy `json.dumps` into a temporary module and asserts that the guard fails with a clear mention of the offending file, so the guard remains effective and would catch regressions (new ad-hoc serializers) in future PRs.

5. **Presenter artifacts and evidence skeleton integration**

   * The presenter harness script generates a small set of deterministic artifacts under `artifacts/presenter/*`:

     * AB and BA showcompat bytes.

     * A Reader CLI parity bytes sample.

     * A preimage recompute log.

     * A showcompat identity summary.

   * These are registered in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` under stable artifact\_keys (`PRESENTER_IDENTITY_SUMMARY_V1`, `PRESENTER_PREIMAGE_RECOMPUTE_V1`, `PRESENTER_READER_CLI_PARITY_V1`, `PRESENTER_SHOWCOMPAT_AB_BYTES_V1`, `PRESENTER_SHOWCOMPAT_BA_BYTES_V1`), with path-proofs updated mechanically via the canonical evidence updater. The Machine Mirror self-record and orientation demo are regenerated once to incorporate the new artifacts, and the evidence skeleton tests remain green.

6. **EPIC020 acceptance wiring for D2 tokens**

   * In `audit/EPIC020_MANIFEST.json`, the D2 tokens now have:

     * Appropriate tests listed in the `tokens[...]` entries (canonical bytes test, identity tests, preimage tests).

     * Presenter artifacts listed in a parallel `token_artifacts` or equivalent mapping.

   * In `docs/acceptance_map_epic020.json`, `token_status` is updated so:

     * D2 tokens are marked `status: "DONE"`.

     * Their `tests` arrays reference the same identity and canonicality tests.

     * Their `artifacts` arrays reference the new `artifacts/presenter/*` files as evidence.

   * A follow-up cleanup PR fixed earlier JSON structural issues (missing commas, duplicated token keys), so both files now parse correctly and have one consistent entry per token; the token sets between manifest and acceptance map are identical.

7. **Tests and CI coverage are appropriate for D2 scope**

   * CLI tests for canonical bytes, parity/identity, and guards are run under closed rails (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC) and pass.

   * Evidence index checks (`update_evidence_index.py --check` and `orientation_demo.py --check`, if exercised in later runs) pass for the updated skeleton, and existing D1 error/tokens tests remain green. No new behavior surfaces outside of D2 are touched.

8. **Residual follow-ups (non-blocking)**

   * D2 parity scenarios focus on the showcompat surface; PF19 contemplates additional presenter-level parity (e.g., for other CLI/reporting surfaces). Those remain candidates for future epics or D-goals rather than scope for this PR.

   * The error-evidence vs orientation design gap has been addressed in a separate build-notes addendum and later evidence PR; this PR’s presenter artifacts respect that updated workflow but do not attempt to generalize it further.

Taken together, the PR is correct, aligned with PF-Canon and the EPIC020 plan, and has no remaining issues that require remediation.

---

## **Doc Deltas (PF-Canon only)**

* Doc: PF12 — Canon-HDE-Schemas and Artifacts  
   Section: §8.6 “Evidence skeleton entries” (or the section that enumerates canonical artifact\_key families)  
   Delta: Extend the list of evidence skeleton families to include the EPIC020 D2 presenter artifacts with their canonical artifact\_keys, for example: `PRESENTER_IDENTITY_SUMMARY_V1` (showcompat identity summary), `PRESENTER_PREIMAGE_RECOMPUTE_V1` (preimage recompute log), `PRESENTER_READER_CLI_PARITY_V1` (Reader/CLI parity bytes), and `PRESENTER_SHOWCOMPAT_AB_BYTES_V1` / `PRESENTER_SHOWCOMPAT_BA_BYTES_V1` (AB/BA showcompat bytes), and note that they support D2 tokens such as `CLI_SHOWCOMPAT_CANON_OK`, `TWO_RUN_IDENTITY_OK`, `COMPOSITE_ABBA_IDENTITY_OK`, and `PREIMAGE_RECOMPUTE_OK`.

* Doc: PF04 — Canon-HDE-Governance  
   Section: Appendix on CLI and presenter transport behavior (the section that describes Reader/public JSON surfaces and CLI behavior)  
   Delta: Clarify that governed presenter/CLI responses (e.g., `showcompat`) must emit public JSON via the canonical emitters `emit_reader_public_envelope` and `emitter.emit_public`, with CLI success writing canonical JSON to stdout only and errors writing to stderr only, and reference the serializer guards as the enforcement mechanism. This ties PF04’s high-level CLI/presenter contract directly to the concrete emitter and guard machinery introduced in this PR.

* Doc: PF20 — Canon-HDE-Phased Epics  
   Section: EPIC020 — D2 “Public Presenter / Emitter” acceptance section  
   Delta: Update the D2 acceptance description so that, in addition to listing D2 tokens, it references the presenter identity tests and presenter artifact families (as defined in PF12) as the canonical evidence for D2 being DONE, and explicitly notes that D1 error tokens and artifacts remain separate from D2’s presenter artifacts.

(These deltas are clarifications and integration of existing behavior into canon; they do not change runtime behavior.)

---

# ADDENDUM 7 \- PR04 HDE-EPIC020

## **Review Summary**

* This PR delivers D3 of HDE-EPIC020 (“Internal Ops Identity Surface `/internal/version`”) by turning `/internal/version` into a fully Separation-grade identity surface: a fixed-order six-field body emitted via the canonical emitter, with strict no-store/HEAD parity, and each field explicitly coupled to frozen identity artifacts.

* It adds a dedicated transport contract test (`tests/transport/test_internal_version_contract.py::test_internal_version_invariants_and_artifacts`) that validates header posture, GET/HEAD/conditional parity, two-run identity, and field-level coupling to `service_identity.json`, `invocation.json`, `release_id` artifacts, and `emitter_sha256.txt`, and writes deterministic identity artifacts under `artifacts/ops/internal_version/*`.

* These identity artifacts (`body_get.json`, `body_get.sha256`, `headers_get.txt`, `headers_head.txt`, `two_run_identity.log`) are registered in the Evidence Index and Machine Mirror under new `INTVER_*` artifact\_keys with path-proofs and orientation refreshed, bringing the `/internal/version` identity proofs into the same governed skeleton as the D1 error and D2 presenter evidence.

* EPIC020 acceptance metadata is updated so that D3 tokens (`INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, and the `/internal/version` portion of `TWO_RUN_IDENTITY_OK`) are marked DONE and bound to the new test and artifacts, and a small follow-up adjustment scopes those INTVER tokens exclusively to the D3 foundation (no longer claimed by D1), keeping foundations consistent with the EPIC020 D1/D2/D3 split.

* CI runs the new internal-version test under closed rails, adds a dedicated `epic020` marker in `pytest.ini`, and re-runs the test to green with no warnings; evidence index checks and orientation demo also pass after the new identity artifacts are added.

I judge the PR acceptable as-is; it meets the EPIC020 D3 plan, is aligned with PF-Canon, and its evidence and acceptance wiring are complete.

---

## **Findings**

1. **Identity body matches PF14 contract and uses canonical serialization**

   * `_build_internal_version_payload` (in `adapter/http_reader.py`, referenced in the PR logs) now constructs a JSON payload with exactly six fields: `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, and `release_id`. The captured `body_get.json` artifact shows these keys in that order and no others.

   * The test harness emits the body via the canonical emitter (`emit_public(..., sort_keys=False)`), so key order is preserved while still using the canonical UTF-8/LF-terminated serializer; this is consistent with PF14’s special-case rules for `/internal/version` (fixed key order, no A7 behavior) while reusing the same serialization discipline as other canonical surfaces.

2. **Header posture and GET/HEAD/conditional parity are enforced and evidenced**

   * The updated `/internal/version` handler retains its PF04/PF09 rails: `Cache-Control: no-store`, no `ETag`, and `Content-Type: application/json; charset=utf-8`. The new test `test_internal_version_invariants_and_artifacts` issues GET, HEAD, and conditional GET requests and asserts:

     * All status codes are 200\.

     * HEAD mirrors GET’s headers (including `Content-Type`) with no body.

     * Conditional GET ignores `If-None-Match` and returns status 200, not 304\.

   * Helper `_write_headers_artifact` writes `headers_get.txt` and `headers_head.txt` under `artifacts/ops/internal_version/`, logging status and headers and an explicit `ETag: <absent>` plus a `Body-Length` line, giving a stable snapshot of transport posture for GET and HEAD.

3. **Two-run identity and field-level coupling are proven against frozen artifacts**

   * `tests/transport/test_internal_version_contract.py::test_internal_version_invariants_and_artifacts`:

     * Calls GET `/internal/version` twice under closed rails and asserts that `list(payload.keys())` equals `_REQUIRED_KEYS` (the six identity fields, in order), that both payloads are equal, and that `sha256(get_resp1.data) == sha256(get_resp2.data)`.

     * Reads `artifacts/identity/service_identity.json`, `artifacts/invocation.json`, `artifacts/math/release_id.txt`, `artifacts/math/freeze_pack_manifest.json`, and `artifacts/identity/emitter_sha256.txt`, and asserts:

       * `engine_tag` and `build_commit` match the service identity fields.

       * `invocation_tag` equals the `tag` in `invocation.json`.

       * `invocation_sha256` equals both the `sha256` in `invocation.json` and `sha256(tag)` recomputed in the test.

       * `emitter_sha256` matches `emitter_sha256.txt`.

       * `release_id` matches `release_id.txt`, the `release_id` in `service_identity.json`, and the `release_id` embedded in `freeze_pack_manifest.json`.

     * Writes `body_get.json`, `body_get.sha256`, and `two_run_identity.log` to `artifacts/ops/internal_version/`, and `_write_two_run_log` records both run hashes and the stored digest, with `hash_match=True` when all three match.

4. **Identity artifacts are integrated into Evidence Index & Mirror**

   * New entries in `artifacts/evidence_index.jsonl`/`docs/evidence/INDEX.json` map:

     * `INTVER_BODY_GET_V1` → `artifacts/ops/internal_version/body_get.json`.

     * `INTVER_BODY_GET_SHA256_V1` → `artifacts/ops/internal_version/body_get.sha256`.

     * `INTVER_HEADERS_GET_V1` → `artifacts/ops/internal_version/headers_get.txt`.

     * `INTVER_HEADERS_HEAD_V1` → `artifacts/ops/internal_version/headers_head.txt`.

     * `INTVER_TWO_RUN_IDENTITY_V1` → `artifacts/ops/internal_version/two_run_identity.log`.

   * Each record has a path-proof (`*.path_proof.txt`) and a role (`snapshot` or `log`) consistent with PF12; the machine mirror self-record (`index.machine_mirror`) is updated with the new hash/size, and orientation demo is regenerated, increasing `total_artifacts` and aligning orientation with the new identity artifacts. Evidence index checks (`update_evidence_index.py --check`) and orientation checks pass in the PR logs.

5. **EPIC020 acceptance wiring for D3 tokens is functionally correct**

   * In `audit/EPIC020_MANIFEST.json`:

     * `TWO_RUN_IDENTITY_OK`’s `tests` list now contains both the showcompat identity test and `tests/transport/test_internal_version_contract.py::test_internal_version_invariants_and_artifacts`, so the token covers both presenter and `/internal/version` identity behaviors.

     * `INTVER_200_CTYPE_JSON_UTF8_OK` and `INTVER_HEAD_PARITY_OK`’s `tests` lists now include `test_internal_version_invariants_and_artifacts`, and their `token_artifacts` entries list the relevant header/body/hash/two-run artifacts under `artifacts/ops/internal_version/*`.

   * In `docs/acceptance_map_epic020.json`:

     * `token_status.TWO_RUN_IDENTITY_OK` is updated so its `tests` array includes both the showcompat and `/internal/version` identity tests, and its `artifacts` array includes `showcompat_identity_summary.json`, `body_get.sha256`, and `two_run_identity.log`.

     * `INTVER_200_CTYPE_JSON_UTF8_OK` and `INTVER_HEAD_PARITY_OK` are marked `status: "DONE"` with `tests` pointing to the internal-version contract test and `artifacts` pointing to headers/body/hash artifacts, reflecting that these tokens are now fully satisfied by D3.

6. **Pytest marking and CI rails are properly configured**

   * `tests/transport/test_internal_version_contract.py` is marked with `pytestmark = pytest.mark.epic020` so EPIC020’s D3 test can be selected via markers; the PR adds `epic020: EPIC020 acceptance tests` to `pytest.ini` so this mark is recognized and no longer triggers `PytestUnknownMarkWarning`.

   * The test sets `DATABASE_URL`, `SAFE_MODE`, `ALLOW_NETWORK`, `LC_ALL`, `LANG`, and `TZ` env defaults to the closed-rails values before creating a test client, which is consistent with PF09/ PF19 determinism requirements.

7. **Foundations are now correctly scoped: D1 vs D3**

   * In a follow-up change, `docs/acceptance_map_epic020.json`’s D1 foundation no longer lists `INTVER_200_CTYPE_JSON_UTF8_OK` and `INTVER_HEAD_PARITY_OK` in its `manifest_tokens` and `tokens` arrays; those tokens remain under the D3 foundation, which owns `/internal/version` identity. This restores the intended split: D1 for error envelope & evidence, D2 for presenter/emitter, D3 for `/internal/version` identity.

8. **Earlier structural JSON issues have been resolved**

   * Previous iterations of EPIC020 acceptance wiring had malformed JSON (missing commas and duplicate keys); subsequent cleanups (including the D1/D2 metadata fixes) have restored `audit/EPIC020_MANIFEST.json` and `docs/acceptance_map_epic020.json` to syntactically valid JSON, with one key per token and fully separated `tests`/`artifacts` arrays. The PR and follow-ups explicitly use `python -m json.tool` and line-numbered patches to validate acceptance files.

   * Given the latest state reflected in the patch and r1 review, there are no remaining structural issues in the acceptance metadata; they cleanly reflect the D3 behavior and evidence.

No further remedial work is required for PR04; any future work around QA rails tokens or broader INTVER semantics belongs in later epics.

---

## **Doc Deltas (PF-Canon only)**

* **Doc:** PF14 — Canon-HDE-Mechanics Guide  
   **Section:** Identity & Provenance Module / Internal Meta Surface `/internal/version`  
   **Delta:** Extend the `/internal/version` section to explicitly document the final D3 identity contract: the JSON body must contain exactly six scalar fields (`engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`) in that order with no extras, emitted via the canonical emitter under no-store/HEAD parity, and each field must be explicitly coupled to the frozen identity artifacts (`service_identity.json`, `invocation.json`, `release_id` artifacts, and `emitter_sha256.txt`) with two-run identity guaranteed under closed rails.

* **Doc:** PF12 — Canon-HDE-Schemas and Artifacts  
   **Section:** §8.6 “Evidence skeleton entries” (identity & ops surfaces)  
   **Delta:** Add the D3 identity artifact families for `/internal/version` to the evidence skeleton enumeration, with artifact\_keys `INTVER_BODY_GET_V1`, `INTVER_BODY_GET_SHA256_V1`, `INTVER_HEADERS_GET_V1`, `INTVER_HEADERS_HEAD_V1`, and `INTVER_TWO_RUN_IDENTITY_V1`, and note that they support the D3 tokens `INTVER_200_CTYPE_JSON_UTF8_OK`, `INTVER_HEAD_PARITY_OK`, and the `/internal/version` portion of `TWO_RUN_IDENTITY_OK` in EPIC020.

* **Doc:** PF20 — Canon-HDE-Phased Epics  
   **Section:** EPIC020 — D3 “Internal Ops Identity Surface `/internal/version`”  
   **Delta:** Update the D3 acceptance description to reference the new `/internal/version` identity test (`test_internal_version_invariants_and_artifacts`) and the INTVER identity artifacts listed in PF12 as the canonical evidence for D3 tokens being DONE, and clarify that D1 no longer owns the INTVER contract tokens, which are exclusively D3’s responsibility.

(These are clarifications and cross-document alignments; they do not change runtime behavior.)

---

# ADDENDUM 8

## **Review Summary**

* This PR introduces an explicit **EPIC020 CI job** (`epic020 acceptance suites (closed rails)`) in `.github/workflows/ci.yml` that runs all D1–D3 tests and the new QA metadata test under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`), making the EPIC020 suite a first-class, determinism-pinned CI job.

* It adds `docs/QA_CHECKLIST_EPIC020.md`, which codifies EPIC020 QA expectations (pre-commit, post-commit, evidence-only, diff-scoped CI, and rails posture) in a single checklist that complements PF19/PF20 without opening new rails, and a corresponding test module `tests/qa/test_epic020_qa_docs.py` that asserts the checklist covers required sections and that QA tokens are wired into acceptance metadata and evidence index.

* `docs/acceptance_map_epic020.json` is updated so D1–D3 foundations are marked DONE, ENV/QA tokens (`QA_PRECOMMIT_CHECKLIST_OK`, `QA_POSTCOMMIT_CHECKLIST_OK`, `QA_EVIDENCE_ONLY_OK`, `QA_CI_DIFF_SCOPED_OK`, `ENV_RAILS_POLICY_OK`, `DETERMINISM_ENV_PINS_OK`) appear in the appropriate foundations, and `token_status` for these tokens now contains explicit test and artifact bindings that match the new CI/QA harness.

* `audit/EPIC020_MANIFEST.json` is extended so QA/ENV tokens have both `tests` and `token_artifacts` entries: QA tokens bind to the QA checklist and EPIC020 QA README, and ENV tokens bind to `ci/checks/check_env_pins.sh` and the determinism env log (`audit/gates/determinism/env_pins.log` \+ path proof), coherently tying these tokens to concrete scripts and evidence artifacts.

* Evidence Index/Mirror remains structurally consistent; the PR does not introduce new EPIC020 artifact\_keys but relies on existing entries (e.g., `audit.determinism.env_pins`) and refreshes path proofs and the mirror self-record via the canonical evidence updater, so env-pin logs and QA docs are properly indexed and path-proofed.

Overall, this PR converges CI, QA rails, acceptance metadata, and evidence for EPIC020 in a way that is consistent with PF04, PF09, PF12, PF19, and PF20. The only concern is the large set of path\_proof updates generated by `update_evidence_index.py`; they are mechanically consistent but should be noted as such. No further remediation is required.

---

## **Findings**

1. **EPIC020 CI job is explicit and correctly pinned to closed rails**

   * `.github/workflows/ci.yml` now contains a dedicated `epic020` job with `env` pinned to `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`. The job:

     * Installs dependencies the same way as the main `test` job.

     * Runs `ci/checks/check_env_pins.sh` to exercise determinism env pins.

     * Runs the EPIC020 D1–D3 test suites and QA metadata tests:

       * `tests/adapter/test_jsonschema.py`

       * `tests/cli/test_cli_usage_and_errors.py`

       * `tests/cli/test_errors_parity.py`

       * `tests/cli/test_cli_canonical_bytes.py`

       * `tests/cli/test_showcompat_parity_and_identity.py`

       * `tests/cli/test_serializer_guards.py`

       * `tests/transport/test_internal_version_contract.py`

       * `tests/qa/test_epic020_qa_docs.py`

   * This aligns with PF20’s requirement that determinism-sensitive epic suites run under closed rails and are explicitly wired to ENV/QA tokens, without adding any new rails-open jobs.

2. **EPIC020 QA checklist is well-scoped and validated by tests**

   * `docs/QA_CHECKLIST_EPIC020.md` documents:

     * Pre-commit checklist: run EPIC020 deterministic suites under closed rails and run evidence index/orientation checks when evidence changes; verify env pins via `ci/checks/check_env_pins.sh` so `audit/gates/determinism/env_pins.log` stays fresh and indexed.

     * Post-commit checklist: ensure all CI jobs (including `epic020`) are green under closed rails; confirm determinism env-pin evidence is present and indexed; require optional Live QA to follow PF19’s “one command → one primary artifact” pattern under `audit/qa/hde-epic020/{errors,cli_presenter,internal_version}/`.

     * Evidence-only PRs: define evidence-only diffs and minimal CI subset.

     * Diff-scoped CI expectations: how to scope EPIC020-specific CI vs falling back to full CI.

     * Rails posture: reaffirm closed rails and indexing expectations for QA/evidence artifacts.

   * `tests/qa/test_epic020_qa_docs.py::test_checklist_covers_required_sections` asserts that:

     * The checklist contains required headings (pre-commit, post-commit, evidence-only, diff-scoped, rails posture).

     * It mentions required commands (`check_env_pins.sh`, `update_evidence_index.py --check`, `orientation_demo.py --check`) and references all EPIC020 test modules.

   * `test_acceptance_metadata_captures_qa_tokens` asserts:

     * For each QA/ENV token (`QA_PRECOMMIT_CHECKLIST_OK`, `QA_POSTCOMMIT_CHECKLIST_OK`, `QA_EVIDENCE_ONLY_OK`, `QA_CI_DIFF_SCOPED_OK`, `ENV_RAILS_POLICY_OK`, `DETERMINISM_ENV_PINS_OK`):

       * `token_status[token]["status"] == "DONE"`.

       * `token_status[token]["tests"]`, `manifest["tokens"][token]`, and `manifest["token_artifacts"][token]` are non-empty.

   * `test_env_pin_artifact_is_indexed` asserts:

     * `artifacts/evidence_index.jsonl` has an entry whose `discovered_physical_path` is `audit/gates/determinism/env_pins.log`.

     * `docs/acceptance_map_epic020.json.token_status[ENV_RAILS_POLICY_OK].artifacts` and `token_status[DETERMINISM_ENV_PINS_OK].artifacts` both include `audit/gates/determinism/env_pins.log`.

3. **Acceptance map foundations and token\_status for QA/ENV tokens are now coherent**

   * In `docs/acceptance_map_epic020.json`:

     * D1 foundation’s `manifest_tokens` and `tokens` arrays now include `DETERMINISM_ENV_PINS_OK` alongside `ENV_RAILS_POLICY_OK` and QA tokens, and D1’s `status` is set to `DONE`. D2 and D3 foundations likewise include `ENV_RAILS_POLICY_OK` and `DETERMINISM_ENV_PINS_OK` and are marked `DONE`. The GLOBAL foundation’s `manifest_tokens` and `tokens` include QA tokens plus both ENV tokens and is marked `DONE`.

   * `token_status` for QA/ENV tokens is updated:

     * `QA_PRECOMMIT_CHECKLIST_OK`: artifacts → `docs/QA_CHECKLIST_EPIC020.md`; tests → the two QA docs tests.

     * `QA_POSTCOMMIT_CHECKLIST_OK`: artifacts → `docs/QA_CHECKLIST_EPIC020.md` and `audit/qa/hde-epic020/README.md`; tests → the two QA docs tests.

     * `QA_EVIDENCE_ONLY_OK`, `QA_CI_DIFF_SCOPED_OK`: artifacts → `docs/QA_CHECKLIST_EPIC020.md`; tests → same QA docs tests.

     * `ENV_RAILS_POLICY_OK`: artifacts → `docs/QA_CHECKLIST_EPIC020.md`, `audit/gates/determinism/env_pins.log`, and its path proof; tests → `ci/checks/check_env_pins.sh` and the two QA docs tests.

     * `DETERMINISM_ENV_PINS_OK`: artifacts → env pins log \+ path proof; tests → `ci/checks/check_env_pins.sh` and env-pin QA doc test.

   * This wiring ensures that all QA/ENV tokens now have concrete tests and artifacts, satisfying PF19/PF20’s requirement that acceptance tokens must be backed by both tests and evidence.

4. **Manifest token/tests/token\_artifacts now match acceptance map and QA docs**

   * In `audit/EPIC020_MANIFEST.json`:

     * The `tokens` mapping for QA/ENV tokens is populated:

       * Each QA token lists the two QA doc tests.

       * `ENV_RAILS_POLICY_OK` lists `ci/checks/check_env_pins.sh` plus the two QA doc tests.

       * `DETERMINISM_ENV_PINS_OK` lists `ci/checks/check_env_pins.sh` and env-pin QA doc test.

     * `token_artifacts` for QA/ENV tokens mirror the acceptance map:

       * QA tokens reference `docs/QA_CHECKLIST_EPIC020.md` (and EPIC020 QA README for `QA_POSTCOMMIT_CHECKLIST_OK`).

       * ENV tokens reference env-pin log and path proof.

   * The manifest and acceptance map are consistent for these tokens, and QA docs tests enforce that consistency.

5. **Evidence Index/Mirror remain valid and incorporate existing ENV artifacts**

   * `artifacts/evidence_index.jsonl` already contained an entry with `artifact_key: "audit.determinism.env_pins"` and `discovered_physical_path: "audit/gates/determinism/env_pins.log"`; this PR relies on that entry and extends acceptance/manifest references to it.

   * `tools/evidence/update_evidence_index.py` and `tools/evidence/orientation_demo.py --check` are run under closed rails; they refresh path proofs and the self-record for the machine mirror. Many path\_proof files and the mirror self-record change, but only in `mtime_utc` or mirror digest, consistent with the tool’s behavior. There is no evidence of schema breakage or missing EPIC020 artifacts.

6. **D1–D3 behavior and evidence remain unchanged; this is pure wiring/metadata work**

   * There are no code changes to error envelope, presenter, or `/internal/version` handlers; all D1–D3 behavioral and evidence surfaces remain as established in PRs 2a/2b/3/4.

   * The only behavioral “effect” is that EPIC020 tests are now guaranteed to run in CI under a dedicated closed-rails job, and QA/ENV tokens are wired to the tests and artifacts that already exist. This aligns with PF06/PF19/PF20 and completes EPIC020’s acceptance.

7. **Potential concern: large path\_proof churn**

   * Running `update_evidence_index.py` refreshed path proofs for a wide swath of artifacts unrelated to EPIC020 (EPIC017/018/019, sampler/core, DB, etc.). All changes appear to be consistent mtime updates with preserved `size_bytes`, `sha256`, `path`, and `produced_at_utc` values.

   * While this is technically correct and keeps proofs in sync with current file mtimes, it does increase PR size and could be noisy. For future epics, it may be worth constraining path-proof refreshes to relevant artifact families for smaller diffs, but it does not warrant remediation here.

Given the strong alignment with PF-Canon, the correctly wired CI job, and the coherent acceptance/evidence bindings, no remediation is needed.

---

## **Doc Deltas (PF-Canon only)**

* **Doc:** PF19 — Glow QA Guide  
   **Section:** §9 “QA Tokens and Rails Patterns” (or equivalent QA token registry section)  
   **Delta:** Extend the examples for `QA_PRECOMMIT_CHECKLIST_OK`, `QA_POSTCOMMIT_CHECKLIST_OK`, `QA_EVIDENCE_ONLY_OK`, `QA_CI_DIFF_SCOPED_OK`, `ENV_RAILS_POLICY_OK`, and `DETERMINISM_ENV_PINS_OK` to reference EPIC020 as a concrete implementation: mention that EPIC020 uses `docs/QA_CHECKLIST_EPIC020.md`, `ci/checks/check_env_pins.sh`, and the determinism env-pin log (`audit/gates/determinism/env_pins.log`) as the evidence/test bindings for these tokens.

* **Doc:** PF20 — Canon-HDE-Phased Epics  
   **Section:** §2.5 “HDE-EPIC020 Epic Plan” — QA/rails acceptance subsection  
   **Delta:** Update the EPIC020 QA/rails acceptance narrative to note that:

  * EPIC020 has a closed-rails CI job (`epic020 acceptance suites`) that runs all D1–D3 tests and QA docs tests under the deterministic rails.

  * QA/ENV tokens are wired to the EPIC020 QA checklist and env-pin evidence, and the acceptance map/manifest show all QA/ENV tokens as DONE with corresponding tests and artifacts.

* **Doc:** PF12 — Canon-HDE-Schemas and Artifacts  
   **Section:** §8.x “CI & Rails Evidence Families” (where `audit.determinism.env_pins` is mentioned)  
   **Delta:** Clarify that the `audit.determinism.env_pins` artifact family backs both global determinism tokens and EPIC020-specific ENV/rails tokens (`ENV_RAILS_POLICY_OK`, `DETERMINISM_ENV_PINS_OK`), and that it is enforced in CI via `ci/checks/check_env_pins.sh` and QA docs tests validating INDEX/Mirror/acceptance bindings.

(These are clarifications and cross-linking, not new canon; the semantics of the tokens are already defined.)

# ADDENDUM 9 \- QA01 HDE-EPIC020

## **Review Summary**

* This QA run executed **Step 1 — D0 / Session bootstrap & environment snapshot** from the approved EPIC020 QA Plan: it captured a minimal rails snapshot and attempted to record `hdctl` CLI presence under `audit/qa/hde-epic020/d0-baseline/`.

* The rails snapshot shows `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`, matching the approved plan and PF19/PF07 expectations for a dev, deterministic Codespaces run.

* The `hdctl_version.log` file contains a CLI usage/argument error (indicating `hdctl` is present but `--version` is not accepted), which partially meets the intended “CLI present” check but does not produce a version string as the QA Plan text anticipated.

* There is no evidence of forbidden writes or drift outside `audit/qa/hde-epic020/...`, and no indication of production code changes. Given Step 1’s goal (confirm rails and CLI availability), the run is acceptable with a noted caveat about the `hdctl --version` behavior.

## **Findings**

1. **Rails snapshot matches approved plan rails (OK)**

   * What happened: `env_rails_snapshot.log` contains four lines: `APP_ENV=dev`, `LANG=C`, `LC_ALL=C`, `TZ=UTC`.

   * PF-Canon / QA Plan: The approved plan pins `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` for EPIC020 Live QA in Codespaces; PF19/PF07 call for deterministic locale/TZ pins in dev/test/CI.

   * Why it matters: This confirms the session rails for EPIC020 are consistent with both the QA Plan and PF-Canon; there is no misalignment in environment posture.

2. **CLI presence confirmed, but `--version` semantics differ from plan text**

   * What happened: `hdctl_version.log` shows `hdctl` printed its usage text and an error about a missing command:  
      `usage: hdctl [-h] {showcompat,aux-preview,bg:resolve,dev:sampler} ...` and `hdctl: error: the following arguments are required: command`.

   * PF-Canon / QA Plan: The approved plan expected `hdctl --version` to produce a version string; PF-Canon defines CLI surface and behavior but does not rely on `--version` for any acceptance tokens. The important property for EPIC020 is that `hdctl` exists and is runnable for the later D1/D2 tests.

   * Why it matters: This confirms **CLI is installed and discoverable**, which is the core requirement for Step 1\. The mismatch between expected “version string” and actual usage message is a minor plan/implementation discrepancy, not a Canon or QA failure. Later steps that actually exercise CLI behavior will provide more substantive coverage.

3. **Evidence placement and scope (OK)**

   * What happened: Both artifacts are under `audit/qa/hde-epic020/d0-baseline/` as required; there is no evidence of writes outside `audit/qa/...`.

   * PF-Canon / QA Plan: PF19 and PF07 expect Live QA evidence for D0 discovery to be stored under audit/qa//..., with no code changes. The approved plan follows and satisfies this.

   * Why it matters: Evidence is easy to locate, epic-scoped, and compliant with governance; this supports repeatability and auditability.

4. **No explicit artifact for dev HTTP harness status (design observation)**

   * What happened: Step 1’s success condition includes “dev HTTP harness running on 127.0.0.1:5000,” but no artifact captures terminal A output; we infer success only indirectly from later steps.

   * PF-Canon / QA Plan: The approved plan does not require a harness-status file; PF19 leaves it to the plan author whether to capture such evidence.

   * Why it matters: This is a minor design limitation of Step 1, not a failure of this run. Subsequent steps will immediately expose a non-running harness, so no extra remediation is required here.

Overall, Step 1 achieved its goals: rails pinned and recorded, CLI presence confirmed, evidence stored correctly. The only caveat is that `hdctl --version` returned a usage error instead of a version string, which is acceptable for this D0 check.

## **Doc Deltas (PF-Canon only)**

* None required for this step.  
   The behavior observed is consistent with PF19/PF07/PF09/PF20 for D0 discovery; the minor discrepancy in `hdctl --version` output is a QA-plan expectation issue rather than a Canon gap. PF-Canon does not currently rely on `hdctl --version` for any acceptance token, so no PF update is needed based solely on this step.

## **QA Verdict and Next Steps**

**Verdict: PASS WITH NOTED CAVEATS – Step 1 meets PF20/PF19 expectations for D0 rails/CLI baselining; `hdctl --version` behavior is slightly different from the plan’s narrative but sufficient for QA purposes.**

* This QA run proved that EPIC020’s Live QA session is running under the intended dev rails (`APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`) and that `hdctl` is installed and callable in the Codespace.

* Evidence for Step 1 is correctly scoped to `audit/qa/hde-epic020/d0-baseline/`, complying with PF19/PF07’s evidence and scope rules.

* The `hdctl --version` usage output confirms CLI presence, even though it does not produce a version string; later steps that actually invoke `hdctl showcompat` will provide the substantive behavior checks needed for EPIC020.

* Recommended next QA steps are to proceed to Step 2 of the approved plan (CLI usage error stream semantics) and Step 3 (HTTP error envelope), where the dev harness and CLI surfaces will be exercised more deeply under the already-established rails.

# ADDENDUM 10 \- HDE-EPIC020 QA Plan CLI Baseline Mis-Specification (hdctl —version) — RCA & Guardrails

Timestamp: 120525 01:45

Details:

1. Context

* This addendum records a **QA planning failure** in the HDE-EPIC020 Live QA Plan: Step 1 (D0 baseline) used `hdctl --version` as the CLI presence check and described the expected outcome as “hdctl\_version.log reports an hdctl version line.”

* In the actual Codespaces run, `hdctl --version` produced a **usage error** and usage text, not a version string, even though the CLI is installed and working. This forced the QA reviewer to reinterpret Step 1 on the fly and treat “CLI present” as the real acceptance condition, contrary to the written plan.

2. Observation

* The plan’s Step 1 “CLI presence / version” command and expectation were **not derived from**:

  * the **CLI/API/Vendor Reference** (which defines CLI commands and flags by title), or

  * the repo’s CLI help output surfaced in the EPIC020 Codex audit.

* There is no canonical requirement anywhere in **Glow QA Guide**, **HDE-Phased Epics**, or **HDE-Mechanics Guide** that `hdctl --version` must exist or emit a version string. The only canon-backed requirement for D0 here is that `hdctl` be present and runnable in the Codespace for later D1/D2 steps.

* As a result, Step 1’s “Expected Outcome” and Pass/Fail text overstated what was required and did so on the basis of an unverified assumption, not PF-Canon.

3. Root cause

* The CLI baseline in the EPIC020 QA Plan was taken from a **generic CLI habit** instead of the actual engine CLI spec:

  * The Implementation Agent authored Step 1 using `hdctl --version` without re-grounding in **HDE-CLI-API-Vendor-Ref** or in the Codex audit’s list of valid commands/subcommands.

  * The accepted QA Plan’s narrative (“non-empty log with version line”) added a **non-canonical extra** on top of the real acceptance condition (“CLI installed and runnable under the pinned rails”).

* PF10 treats this as a **QA planning defect**, not a product defect: the CLI behavior is consistent with its usage syntax; the plan was wrong in how it tried to probe it.

4. Impact

* For HDE-EPIC020:

  * The PO still proved the important facts: `hdctl` exists in the Codespace, can be invoked, and later D1/D2 steps used it correctly.

  * However, Step 1’s expectation text misled the operator and required ad hoc reinterpretation during QA review, which violates the mechanical, copy/paste-friendly intent of **Glow QA Guide**.

* For future epics:

  * If left uncorrected, this pattern (“invent a CLI baseline command without checking canon”) will repeat, leading to brittle QA Plans that depend on undocumented behaviors and create noise in Live QA.

5. Guardrails (to be drained into canon via PF19 / PF06)

This addendum proposes the following **process guardrails** for QA Plan authors and reviewers:

* CLI presence and baseline checks in QA Plans **must** be derived from **HDE-CLI-API-Vendor-Ref** and/or a Codex audit of the repo, not from generic assumptions.

* For D0 “CLI presence” checks, QA Plans should use **canon-anchored patterns** such as:

  * a shell-level presence check (for example `command -v hdctl`) and/or

  * a help invocation that is explicitly documented as supported (for example `hdctl --help` or a no-argument `hdctl` that prints usage).  
     The exact spellings belong in the CLI spec and Codex audit; QA Plans must copy, not invent, them.

* QA Plan reviewers must treat any CLI command that is **not** traceable to the CLI spec, to tests, or to a Codex audit as a **blocking issue**. Those commands must be replaced with canon-backed equivalents before the Plan is approved.

* D0 steps must be kept **minimal** and must not introduce extra expectations (like “must print a version string”) unless those expectations are explicitly tied to epic acceptance or PF-Canon requirements.

6. Drain targets

When this addendum is accepted, the intended drain is:

* **Glow QA Guide**: Add a short subsection under the Live QA / D0 patterns that shows a canon-backed example of a CLI presence baseline (for example, command presence \+ help/usage invocation) and explicitly warns against ad hoc `--version` assumptions.

* **Epic-Process-Guide**: Add a line to the Live QA Plan review checklist that requires every CLI usage in the Plan to be cross-checked against **CLI/API/Vendor Reference** or a Codex audit before approval.

This addendum is scoped strictly to the QA Plan and QA process; it does not claim any product bug in the CLI behavior itself.

# ADDENDUM 11 \- QA02 HDE-EPIC020

## **Review Summary**

* This QA run executed **Step 2 — D1 CLI error stream semantics (usage error path)** from the approved EPIC020 QA Plan, using `hdctl showcompat` with a missing `--pair-file` and capturing stdout, stderr, and exit code under the `cli_error_missing_pair_file.*` trio of evidence files.

* The summarized deliverables show an exit code of **64**, a typed error `FILE_NOT_FOUND`, and an empty stdout channel, which matches the plan’s expectations and PF14/PF09/PF05’s stream/exit discipline for usage errors (stderr-only, stdout empty, exit 64).

* There is no indication of writes outside the intended QA evidence space, and the behavior observed is consistent with the D1 “CLI error parity” and `CLI_STDERR_ONLY_ON_ERROR_OK` token semantics in PF20/PF19.

Given the data provided, this step’s QA result is acceptable with no remediation required.

---

## **Findings**

1. **Step 2 was executed as specified in the approved QA Plan (OK)**

   * What happened: The PO invoked `hdctl showcompat --pair-file does-not-exist.json` and captured stdout, stderr, and exit code as `cli_error_missing_pair_file.stdout`, `.stderr`, and `.exit` respectively, exactly as the plan describes.

   * PF/Plan basis: QA Plan EPIC020 Step 2 defines this exact command and evidence file set for D1 usage-error coverage; PF09’s subtask HDE-SEPA002.6 calls for CLI stderr/stdout discipline and usage exit 64 to be proven via CLI harness logs.

   * Why it matters: Ensures we are judging the right behavior against the right scenario; there is no drift between the planned and executed command shape.

2. **Exit code is 64 (usage error) as required (OK)**

   * What happened: The `cli_error_missing_pair_file.exit` deliverable is reported as `64`.

   * PF/Plan basis: PF14 §17.2 defines `64` as the canonical exit code for usage errors (`stderr` synopsis; stdout empty). The QA Plan explicitly expects `cli_error_missing_pair_file.exit` to contain `64`.

   * Why it matters: This directly satisfies the “usage exit 64” half of the D1 stream/exit requirement, aligning with PF09’s `CLI_USAGE_ERR_EXIT64_OK`/`CLI_STDERR_ONLY_ON_ERROR_OK` token goals.

3. **Stdout is empty and stderr contains a typed error (OK)**

   * What happened: The summary describes:

     * `cli_error_missing_pair_file.stdout` as “empty”.

     * `cli_error_missing_pair_file.stderr` as containing `FILE_NOT_FOUND`.

   * PF/Plan basis: The Plan requires stdout to be empty and stderr to contain a typed error about the missing file, with no stack trace or raw Python dump. PF14 and PF09 reiterate that usage errors must write a short synopsis to stderr and keep stdout empty; PF05 reinforces usage & typed errors going to stderr only.

   * Why it matters: This demonstrates **no mixed streams** and a clear, token-like message (`FILE_NOT_FOUND`) for a missing file, which is exactly what PF14/PF05 expect for usage errors and what PF20 D1 lists under parity & stream discipline.

4. **Evidence scope and naming align with PF-Canon patterns (OK)**

   * What happened: The file trio is referred to as `cli_error_missing_pair_file.stdout`, `.stderr`, and `.exit`, matching the plan’s naming; the plan places them under `audit/qa/hde-epic020/errors/`.

   * PF/Plan basis: PF07, PF19, and PF20 all anchor Live QA evidence for EPIC020 under `audit/qa/hde-epic020/...`, following the “one command → one primary artifact” pattern.

   * Why it matters: Consistent naming and scoping make this evidence easy to integrate into the acceptance map and Evidence Index, and it avoids any forbidden writes outside `audit/qa/...`.

5. **No indication of stack traces or CLI misbehavior (OK)**

   * What happened: The summary describes a single typed error token (`FILE_NOT_FOUND`) rather than a Python traceback or mixed output.

   * PF/Plan basis: The Plan explicitly calls out that stderr must not contain stack traces or untyped/raw error text for this scenario; PF05/PF14 expect typed, diagnostic messages or envelopes, not unstructured exceptions.

   * Why it matters: Ensures usage errors are presented in a stable, user- and QA-friendly way and that CLI\_STDERR\_ONLY\_ON\_ERROR\_OK is met in spirit as well as letter.

No gaps or contradictions are visible from the deliverables provided; the behavior matches both the QA Plan and PF-Canon for this scenario.

---

## **Doc Deltas (PF-Canon only)**

* None for this step.  
   The observed behavior aligns well with PF14 and PF09’s CLI stream/exit rules and PF20’s D1 acceptance bullets; there is no revealed gap in PF-Canon that needs updating based solely on this result.

---

## **QA Verdict and Next Steps**

**Verdict: PASS – coverage and results meet PF20/PF19 expectations for this D1 CLI usage-error step.**

* This run **proved** that `hdctl showcompat` respects stream/exit discipline on a usage error: stdout is empty, stderr carries a typed error, and the exit code is 64\.

* It directly supports the EPIC020 D1 tokens `CLI_STDERR_ONLY_ON_ERROR_OK` and `CLI_USAGE_ERR_EXIT64_OK` (names per PF09/PF19), providing concrete evidence files under `audit/qa/hde-epic020/errors/`.

* No remediation is needed for this step; the next QA actions should proceed per the approved plan (HTTP error envelope checks and D2/D3 identity/presenter steps), using these CLI artifacts as the D1 stream/exit baseline.

* When updating acceptance, this step’s evidence should be referenced in the EPIC020 D1 parity & stream discipline area (PF20 §2.5.5) and in any future PF19 examples for CLI error-stream QA patterns.

# ADDENDUM 12 \- D1 HTTP error envelope — dev harness port mismatch (RCA & Step 3 refactor) 

HDE-EPIC020 D1 HTTP error envelope — dev harness port mismatch (RCA & Step 3 refactor)

Timestamp: 2025-12-05T00:00:00Z

Epic: HDE-EPIC020 (“Separation Pass 1 — Error & Identity Surfaces”)

Scope: D1 HTTP error-envelope Live QA step (Step 3 in the approved EPIC020 QA Plan)

Status: OPEN — QA planning defect; behavior unverified until remediated

---

1. Context

* The approved EPIC020 QA Plan defines:

  * A D1 CLI usage-error step (Step 2\) using `hdctl showcompat` with a missing `--pair-file`, which has been run and accepted.

  * A D1 HTTP error-envelope step (Step 3\) that calls `/api/compat/v1` via the dev HTTP harness with invalid JSON and asserts:

    * HTTP status 4xx (not 2xx),

    * error\_v1-style envelope (`ok:false`, `code`, `error`, optional `details/ctx`),

    * valid JSON and canonical headers.

* In the approved Plan, Step 3 uses a hard-coded URL:

  * `http://127.0.0.1:5000/api/compat/v1`

* with the dev Reader harness started via:

  * `python -m adapter.http_reader --bind 127.0.0.1:5000`.

* In the actual Codespaces environment for HDE-EPIC020, the dev Reader harness reports:

  * `Running on http://127.0.0.1:8000`

* and the `curl` call to port 5000 fails with:

  * `curl: (7) Failed to connect to 127.0.0.1 port 5000 ... Could not connect to server`.

* As a result, Step 3 produced:

  * `http_compat_error.headers` — empty,

  * `http_compat_error.pretty.json` — empty,

  * `http_compat_error.body` — not created,

* and `python -m json.tool` failed with “No such file or directory.”

---

2. Observation

* For this Codespace, `adapter.http_reader` is actually bound to port 8000, not 5000:

  * Terminal A output:

    * “Running on all addresses (0.0.0.0)”

    * “Running on http://127.0.0.1:8000”

    * “Running on http://10.0.0.159:8000”

* The Step 3 `curl` invocation to port 5000 is therefore guaranteed to fail with `curl: (7)`, regardless of the handler’s actual behavior.

* This matches the QA Plan’s FAIL\_TOOLING branch for this step (curl cannot connect; json.tool fails to read a missing file), not FAIL\_BEHAVIOR:

  * No request ever reached `/api/compat/v1`,

  * The compat handler never had a chance to emit an error envelope.

* The dev harness and Codespaces infra have been consistently documented (PF07, PF10, QA guides) as binding the Reader on port 8000; the 5000 example appears only as an older local-dev illustration in Mechanics, not as the current Codespaces binding for this project.

---

3. Root cause

This is a QA planning failure, not a runtime behavior defect.

* The EPIC020 Step 3 command was copied from a generic PF14-style dev harness example (`127.0.0.1:5000`) instead of being re-derived from:

  * Glow Infrastructure (PF07) and PF10 addenda that describe the **actual** Codespaces binding (port 8000 for `adapter.http_reader`), and

  * The EPIC020 QA Guide and Codex audit, which both assume the Codespaces dev Reader is on port 8000\.

* Canon precedence was misapplied:

  * For EPIC020 in Codespaces, PF07 \+ PF10 \+ EPIC020 QA Guide are the single home for “Reader host:port”,

  * PF14’s 5000 examples are illustrative only and must not be treated as environment-specific bindings.

* The QA Plan did not include a pre-flight sanity check (for example, a quick GET to `/internal/version`) to confirm the chosen base URL was reachable before freezing it into the Live QA step.

---

4. Impact

* On this run of Step 3:

  * The PO followed the Plan correctly and used `http://127.0.0.1:5000/...`; the dev Reader harness was running on 8000\.

  * All Step 3 PASS/FAIL\_BEHAVIOR criteria are unverified; the step ended in FAIL\_TOOLING due to wrong host:port, and the compat error-envelope behavior remains untested in Live QA.

* On EPIC020 acceptance:

  * D1 CLI usage/error semantics have been verified (Step 2),

  * D1 HTTP error-envelope semantics via dev harness have **not** yet been proven in Live QA and must not be marked accepted on the basis of the failed 5000 run.

* On QA process:

  * This repeats the pattern seen in the `hdctl --version` planning defect: a realistic-looking but ungrounded command was added to the Plan without checking the actual interface/binding in PF07/PF10/QA Guide or Codex, undermining trust in the mechanical QA scripts.

ADDENDUM 13 \- Compat drift and failure

**Review Summary**

* This QA run is another attempt at **Step 3 — D1 HTTP error envelope via dev harness (invalid JSON)** for EPIC020, now using the dev Reader on port 8000\.

* The call to `/api/compat/v1` returned a **404 Not Found** HTML page with `Content-Type: text/html; charset=utf-8`, and `python -m json.tool` failed with `Expecting value` because the body was not JSON.

* Canonical docs clearly define `POST /api/compat/v1` as a dev/internal compat route that, on malformed input, MUST emit a typed JSON error envelope (`ok:false, code, error, ...`), so a 404 HTML page from this path is out of spec.

* The port choice (8000) is correct for Codespaces by PF07/PF09; the behavior failure here is **not** a port misconfig but either a route wiring defect or a mismatch between the running app and the documented dev harness.

Given this, Step 3 remains **unaccepted** and requires remediation. Below I narrate the findings, including where my planning was wrong earlier and what this run actually shows.

---

## **Findings**

1. **Canonical route and method for D1 HTTP compat are unambiguous in PF-Canon**

   * PF02 and PF05 both define compat v1 as an HTTP surface at `/api/compat/v1`:

     * PF02 Architecture §3.1: “`/api/compat/v1` is the adapter’s compatibility surface … POST expects a valid pair definition … malformed or incomplete inputs are rejected.”

     * PF05 §5.5 “Compat v1 (dev-only) route & parity harness”: “Path: `POST /api/compat/v1` (dev only). POST is normative and MUST be used for JSON bodies” and “Error body: typed, numeric-free `{\"ok\": false, \"code\": \"…\", \"error\": \"…\"}`”.

     * PF14 Mechanics §9.3 repeats: dev HTTP harness routes include `GET|POST /api/compat/v1` and error posture is JSON with `Content-Type: application/json; charset=utf-8`.

   * So, using `POST /api/compat/v1` for EPIC020 D1 HTTP error-envelope QA is absolutely canon-aligned. There is no ambiguity about the route we *should* be hitting.

2. **Port 8000 is the correct Codespaces binding; the earlier 5000 plan was my planning failure**

   * PF07 §8.2.1 (HD Engine) declares the HD Engine port mapping: “Dev (CodEx): 8000; QA (Codespaces): 8000; Prod (Railway): 8000.”

   * PF09 extends this by saying the devcontainer binding must set `DEV_SAMPLER_URL` with base `http://127.0.0.1:8000` for Codespaces.

   * There are older quick-starts in PF14/PF10 that still show `http://127.0.0.1:5000` as a generic Flask dev pattern, but for EPIC019/EPIC020 infra canon, PF07/PF09 clearly override that with 8000 for Codespaces.

   * The fact that I originally specified `:5000` in Step 3 was a pure QA planning error: I reached for the older PF14 example instead of re-grounding in PF07/PF09, which are the single home for the Codespaces port. You corrected this by showing the actual harness log on 8000; the refactored Step 3 now correctly uses 8000\.

3. **What this run actually did: route reachable, but returns 404 HTML, not JSON**

   * Deliverables show:

`http_compat_error.headers` \=

 HTTP/1.1 404 NOT FOUND  
Server: Werkzeug/3.1.4 Python/3.11.14  
Date: ...  
Content-Type: text/html; charset=utf-8  
Content-Length: 207  
Connection: close

*   
  * `http_compat_error.body` contains an HTML 404 page (`<!doctype html> … <h1>Not Found</h1> …`).

    * `python -m json.tool http_compat_error.body` fails with `Expecting value: line 1 column 1 (char 0)` and `http_compat_error.pretty.json` is empty.

  * This tells us:

    * `curl` successfully reached `127.0.0.1:8000`; we’re no longer in the “cannot connect” case.

    * The server’s routing stack did *not* match `POST /api/compat/v1` to the compat handler advertised in PF05/PF14 (§5.5 / §9.3). Instead, we got the default Flask 404 HTML page.

4. **Why this is a behavior/wiring failure vs PF-Canon, not a tooling/rails failure**

   * Per PF05/PF14, a POST to `/api/compat/v1` with malformed JSON must result in:

     * A 4xx status,

     * `Content-Type: application/json; charset=utf-8`,

     * A JSON body `{"ok": false, "code": "...", "error": "...", ...}`.

   * Instead we saw:

     * 404 Not Found,

     * HTML content,

     * JSON parse failure.

   * The harness is clearly answering, so we aren’t in the FAIL\_TOOLING case for this run (no “could not connect”). The behavior simply doesn’t match the canonical route contract:

     * Either the app running under `python -m adapter.http_reader` in your Codespace is not actually mounting `/api/compat/v1` (e.g., blueprint not registered, wrong app factory, or version drift), or

     * The canonical docs are out of sync with code and the route was removed/renamed without PF05/PF14 being updated.

   * From the QA Plan’s perspective, **this is FAIL\_BEHAVIOR vs PF05/PF14/PF02**, not a harness connectivity failure.

5. **Evidence is correctly scoped; D1 HTTP coverage is still unproven**

   * Evidence for this run is where it should be—`audit/qa/hde-epic020/errors/http_compat_error.headers`, `.body`, `.pretty.json`—and accurately reflects the 404 HTML response.

   * However, none of Step 3’s PASS conditions (4xx JSON, `ok:false`, `code`, `error`) are met; D1 HTTP error-envelope behavior is still unverified for EPIC020.

   * The earlier planning defect (using port 5000\) is now fixed; this run proves that with the **canonical port and path**, the service still isn’t behaving as PF05/PF14 advertise.

---

## **Remediation Needed**

1. Dev harness for EPIC020 is reachable on `127.0.0.1:8000`, but `POST /api/compat/v1` returns a default Flask 404 HTML page instead of the PF05/PF14 error envelope.

2. D1 HTTP error-envelope coverage for EPIC020 **cannot be accepted** until:

   * The route is mounted correctly and

   * Malformed JSON yields the canonical JSON error envelope per PF05/PF14.

3. The previous planning failure (port 5000\) has been addressed in the refactored Step 3; the remaining issue is an **actual mismatch between code behavior and the canonical contract for `/api/compat/v1`**.

---

## **QA Remediation Instructions**

The remediation path has two threads: (a) implementation / wiring fix, and (b) re-running Step 3 once that fix is in. Below, I keep this strictly “what to do next,” grounded in PF-Canon.

### **A. Implementation / wiring remediation (bug to open)**

From this run and PF-Canon, you can confidently open an implementation issue with the following description:

* **Observed behavior**

  * Under `APP_ENV=dev` with the dev Reader harness running on `127.0.0.1:8000`, `POST /api/compat/v1` with an invalid JSON body returns:

    * `HTTP/1.1 404 NOT FOUND`

    * `Content-Type: text/html; charset=utf-8`

    * HTML 404 body.

* **Expected behavior (PF-Canon)**

  * PF02 §3.1 Compat v1: `/api/compat/v1` is the adapter’s compatibility surface; malformed inputs are rejected (not missing).

  * PF05 §5.5: `POST /api/compat/v1` dev-only route; error body is typed JSON `{"ok": false, "code": "...", "error": "..."}`, never echoing request text.

  * PF14 §9.3: dev HTTP harness routes include `GET|POST /api/compat/v1`, with dev error posture `Content-Type: application/json; charset=utf-8`, `Cache-Control: no-store`, no ETag.

* **Conclusion**

  * Under EPIC020’s documented contract, a 404 HTML page from `POST /api/compat/v1` is a behavior bug (or a routing misconfiguration) relative to PF05/PF14/PF02, not a QA or port misconfiguration.

  * A card/bug should be opened to:

    * Ensure `adapter.http_reader` in Codespaces mounts the `/api/compat/v1` blueprint as documented, and

    * Confirm that malformed JSON is handled via `error_envelope` to produce the canonical JSON error body.

### **B. QA rerun for Step 3 once implementation is fixed**

After the implementation/wiring bug is addressed and a fix is deployed to your Codespace:

**Start dev Reader harness in Terminal A as before**, on the canonical port (8000):

 cd /workspaces/glow-hdengine-v2  
source .venv/bin/activate  
export APP\_ENV=dev  
export LC\_ALL=C  
export LANG=C  
export TZ=UTC

python \-m adapter.http\_reader \--bind 127.0.0.1:8000

1. 

**Re-run Step 3 exactly with the canonical route and port** in Terminal B:

 cd /workspaces/glow-hdengine-v2  
source .venv/bin/activate  
export APP\_ENV=dev  
export LC\_ALL=C  
export LANG=C  
export TZ=UTC

mkdir \-p audit/qa/hde-epic020/errors

curl \-sS \\  
  \-D audit/qa/hde-epic020/errors/http\_compat\_error.headers \\  
  \-o audit/qa/hde-epic020/errors/http\_compat\_error.body \\  
  \-H "Content-Type: application/json" \\  
  \-X POST http://127.0.0.1:8000/api/compat/v1 \\  
  \--data 'not json'

python \-m json.tool \\  
  audit/qa/hde-epic020/errors/http\_compat\_error.body \\  
  \> audit/qa/hde-epic020/errors/http\_compat\_error.pretty.json

2.   
3. **Apply the original PASS/FAIL criteria** (unchanged):

   * PASS when:

     * HTTP status is 4xx,

     * `Content-Type` is `application/json; charset=utf-8`,

     * JSON body parses, and

     * pretty JSON has `ok:false`, `code`, `error`, optional `details/ctx`.

   * FAIL\_BEHAVIOR if:

     * Status is 2xx with an error envelope, or

     * JSON missing required fields.

   * FAIL\_TOOLING if:

     * curl cannot connect or

     * json.tool can’t parse at all (for reasons other than malformed JSON designed for this test).

4. **If behavior still diverges after the fix**, keep the new artifacts and escalate; at that point either PF-Canon needs revision (if the route is legitimately changing) or the implementation still isn’t wired to what PF02/PF05/PF14 promise.

---

This is the RCA in plain language:

* My **first** planning failure for Step 3 was choosing port 5000 instead of the codified 8000—directly contradicting PF07/PF09. That’s fixed.

* The **current** failure is not the plan; it is the observed behavior from `POST /api/compat/v1` under APP\_ENV=dev, which contradicts PF05/PF14/PF02’s contract for the compat v1 dev route. The right move now is to fix wiring/implementation and then re-run Step 3 as written.

Short version: the **HTTP compat surface on this harness is broken or missing**, but that doesn’t mean “all of compat” is dead.

Let me separate what we actually know from what we don’t:

1. **What canon says should exist**

    From PF02 / PF05 / PF14, this is unambiguous:

   * There **must** be a dev-only compat HTTP route:

     * `POST /api/compat/v1` on the adapter.

     * On malformed input, it returns a 4xx JSON error envelope with `ok:false`, `code`, `error`, optional `details/ctx`.

   * In Codespaces, the dev Reader harness is supposed to bind on **port 8000**; that part we now align with PF07/PF09.

**What we actually saw in your Codespace**

 When you did:

 curl \-sS \\  
  \-D audit/qa/hde-epic020/errors/http\_compat\_error.headers \\  
  \-o audit/qa/hde-epic020/errors/http\_compat\_error.body \\  
  \-H "Content-Type: application/json" \\  
  \-X POST http://127.0.0.1:8000/api/compat/v1 \\  
  \--data 'not json'

2.  you got:

   * `HTTP/1.1 404 NOT FOUND`

   * `Content-Type: text/html; charset=utf-8`

   * Body \= default Werkzeug/Flask “404 Not Found” HTML page.

3. And `python -m json.tool` failed because that body is HTML, not JSON.

    That means:

   * The **server is up and reachable** (we’re past the port 5000 nonsense).

   * But the app serving on 8000 **is not mounting `/api/compat/v1` at all** in this environment – the router falls through to Flask’s default 404\.

4. **What that means for “compat”**

    Based on this evidence:

   * The **compat HTTP route** on the dev Reader harness in this Codespace is effectively broken/missing right now.

   * That’s a real **behavior/ wiring bug relative to PF02/PF05/PF14**, not a QA misstep at this point.

   * It does **not** automatically mean:

     * The compat math (`engine.core.core` / presenter artifacts) is wrong.

       * We already have CLI/presenter artifacts (`artifacts/cli/ab.json`, `ba.json`, preimage logs) and tests that show the engine/presenter path itself can produce valid compat JSON.

     * `hdctl showcompat` as a CLI entry point is dead.

       * CLI may hit engine/presenter directly without going through the HTTP compat route.

5. So: *compat HTTP surface on this harness is broken or miswired; the underlying compat engine & CLI path probably still work, but that’s not what Step 3 was testing.*

6. **Where my planning was wrong vs where the code is wrong**

    Two separate failures:

   * **My planning failure (earlier):**

     * I originally told you to hit port 5000\. PF07/PF09 have been screaming “8000” for a while; that was on me.

     * We fixed that by refactoring Step 3 to use 8000\.

   * **Current failure (implementation/wiring):**

     * With the **correct** port (8000) and the canonical route (`/api/compat/v1`), the dev harness still returns 404 HTML.

     * That contradicts PF05/PF14’s contract for compat v1 on the dev Reader. That’s not a plan defect anymore; that’s code/router wiring not matching canon.

7. **How I’d label it, precisely**

   * “Compat HTTP route on the dev harness is broken or missing in this Codespaces environment.”

   * “Compat engine (math \+ presenter) is likely fine, because the CLI artifacts/tests exist and pass; we just can’t reach that functionality via the documented HTTP compat v1 surface.”

If you want, we can next draft a very tight bug description you can drop straight into your issue tracker:

* Title: “EPIC020: dev Reader harness does not mount POST /api/compat/v1 (404 HTML instead of JSON error envelope).”

* Body: literally the headers/body you captured \+ the PF05/PF14 citations that show what should be there.

But yes: for the specific thing Step 3 is trying to exercise – **HTTP compat v1 error behavior** – it’s not there right now.

# **ADDENDUM 13 — EPIC020 compat HTTP canon deltas (PF02/PF07/PF09/PF14/PF19/PF20/PF23)**

Timestamp: \<to be filled on merge\>

Epic: **HDE‑EPIC020** (“Separation Pass 1 — Error & Identity Surfaces”)

Status: **OPEN — canon changes not yet drained**

Scope: Canonical documentation updates required by the **EPIC020 Compat HTTP Defect – Remediation Guide (Revised)**, the Codex audit, and the QA escalation for the dev compat HTTP surface at `POST /api/compat/v1`.

These notes do **not** change canon on their own. They describe the doc deltas that must be implemented in PF‑Canon (PF02, PF07, PF09, PF14, PF19, PF20, PF23) once the EPIC020 remediation work lands.

---

## **1\. PF02 — HDE Architecture**

**Goal:** Make the dev Reader harness obligations for compat HTTP explicit, without over‑expanding dev app responsibilities.

**Target location**

* The section that currently describes **adapter HTTP surfaces** and **dev harness responsibilities** (the part that names `adapter/http_reader` and `adapter/wsgi` as separate factories and explains their roles).

**Changes to introduce**

1. **New constraint on the dev Reader harness used for Codespaces Live QA**

    Add a short, normative paragraph along these lines (final wording to be decided in the doc PR, but semantics must match this):

    “The dev Reader harness used for Codespaces Live QA MUST expose all canonically dev/internal HTTP surfaces required for QA — including `POST /api/compat/v1` — using the same emitter and error semantics as the production/stable adapter app.”

    Requirements encoded:

   * The **specific app factory** used in Codespaces (currently `adapter/http_reader.create_app`, launched via `python -m adapter.http_reader`) is the dev harness that must:

     * mount the compat blueprint for `POST /api/compat/v1`, and

     * share error handling and emitter behavior with the production/stable app.

   * Scope is **limited to dev/internal QA surfaces** (e.g., compat v1, internal/version, dev sampler), not “all prod‑only routes”, in line with the “minimal dev harness” posture captured in the Remediation Guide RCA.

2. **Optional cross‑reference (non‑normative)**

   * Add a brief note that details for compat v1 behavior live in **HDE‑CLI‑API‑Vendor‑Ref** and **HDE‑Mechanics Guide** (compat sections), to keep PF02 focused on roles and responsibilities, not on error envelope structure.

---

## **2\. PF07 — Glow Infrastructure & PF09 — HDE‑Build Checklist**

**Goal:** Remove 5000/“toy” ambiguity and lock the 8000 port story and infra‑owned bindings for Codespaces and QA planning.

### **2.1 PF07 — Glow Infrastructure**

**Target location**

* “HD Engine – Port” table and the surrounding **Codespaces dev/QA environment** description.

**Changes to introduce**

1. Re‑affirm that:

   * Dev (Codex), QA (Codespaces), and prod HD Engine all use **port 8000**.

   * `DEV_SAMPLER_URL (Codespaces)` is the **canonical infra‑owned base URL** for the dev Reader harness.

2. Add an explicit statement:

   * QA Plans and developer docs **MUST derive** dev Reader base URLs from infra‑owned bindings (PF07 \+ devcontainer config), and **MUST NOT** guess ports or copy 5000 examples from mechanics docs.

   * Any use of 5000 in non‑PF07 docs must be treated as **local example only**, not as canonical Codespaces guidance.

### **2.2 PF09 — HDE‑Build Checklist**

**Target location**

* The **devcontainer/env guidance** rows for HD Engine and Codespaces QA.

**Changes to introduce**

1. Clarify that for Codespaces:

   * Dev Reader (and thus compat dev HTTP) **must bind** to `http://127.0.0.1:8000`.

   * Devcontainer configs **must set** environment keys (e.g. `DEV_SAMPLER_URL`) based on the 8000 binding, and QA/docs **must consume** those keys, not hard‑code ports.

2. Add a checklist item:

   * Before freezing any QA Plan step that references an HD Engine URL, the author **must** confirm the actual binding from devcontainer/config/infra (PF07) and treat any mismatch (e.g. 404/HTML from a canon JSON surface) as **FAIL\_BEHAVIOR**, not “QA nuance”.

---

## **3\. PF14 — HDE‑Mechanics Guide**

**Goal:** Demote 5000 examples and make 8000‑based Codespaces patterns explicit; optionally host the dev harness entrypoint text if we choose PF14 over PF02 for that.

**Target locations**

* Local dev examples for `flask run` / toy harnesses that still cite port **5000**.

* The section that describes **dev harness usage** and sample commands.

**Changes to introduce**

1. **Port examples**

   * Clearly mark any 5000‑based examples as **non‑canonical local samples** (for toy/local runs only).

   * Add concrete, end‑to‑end examples for Codespaces that:

     * start the dev Reader harness in APP\_ENV=dev,

     * bind to port 8000, and

     * show a curl against `/reader` and `/internal/version` using `http://127.0.0.1:8000`.

2. **(Optional) Dev Reader entrypoint home**

   * If we decide that PF14, not PF02, is the single home for the “canonical dev Reader harness entrypoint”, add a short subsection that:

     * names the entrypoint used in Codespaces (currently `python -m adapter.http_reader`), and

     * states that QA guides and devcontainer configs MUST use this app when validating dev HTTP behavior.

   * If we instead pick PF02 as the home for this sentence, PF14 should **not** re‑define it; it should only reference PF02 by title. Final home to be decided during doc PR; this addendum simply records the requirement.

---

## **4\. PF19 — Glow QA Guide**

**Goal:** Add a per‑route Live QA rule and a compat HTTP token in the **QA Acceptance Tokens Registry**.

**Target locations**

* Live QA / environment section.

* QA Acceptance Tokens Registry (where each token’s owner/scope/evidence mapping is defined).

**Changes to introduce**

1. **Per‑route Live QA rule (NEW RULE)**

    Add a rule in the Live QA / tokens section:

    “If an epic’s D‑goal names a canon HTTP route (per HDE‑CLI‑API‑Vendor‑Ref / HDE Architecture), the acceptance map MUST include at least one governed Live QA token and artifact for that route in the canonical environment.”

    Notes:

   * “Canon HTTP route” is those defined in PF05/PF02 (e.g., `POST /api/compat/v1`).

   * EPIC020 is the first consumer; future HTTP‑surface epics inherit the same rule.

2. **New QA Acceptance Token: compat HTTP malformed JSON**

    In the QA Acceptance Tokens Registry:

   * Add a new token family describing **HTTP compat malformed‑JSON behavior**, with semantics:

     * Scope: dev compat HTTP surface (`POST /api/compat/v1` in APP\_ENV=dev).

     * Behavior: malformed JSON ⇒ 4xx JSON error envelope with `ok:false`, `code`, `error`, via shared emitter/serializer.

     * Evidence: governed Live QA artifacts (headers/body/pretty JSON) captured from the canonical Codespaces dev harness, plus CI tests running against the dev harness and wsgi app.

   * Record that EPIC020 instantiates this as `EPIC020.D1.HTTP_COMPAT_MALFORMED_JSON`, but semantics live in PF19, **not** in EPIC020‑local docs.

---

## **5\. PF20 — HDE‑Phased Epics**

**Goal:** Reconcile EPIC020’s record and acceptance map with its D‑goals and the new PF19 rules/tokens.

**Target locations**

* EPIC020 epic record (D‑goals, Tokens & Evidence, QA Rails).

* Any cross‑epic “Outstanding Issues” entries that reference HTTP compat QA gaps.

**Changes to introduce**

1. **EPIC020 record alignment**

   * In the EPIC020 record, under D1 and Tokens & Evidence:

     * List the new HTTP compat Live QA token name from PF19 (`EPIC020.D1.HTTP_COMPAT_MALFORMED_JSON`).

     * Ensure the “Tokens & Evidence” roster points to:

       * the CI job that runs dev harness \+ dev vs wsgi compat tests, and

       * the governed Live QA artifacts under `audit/qa/hde-epic020/http_compat_malformed/`.

2. **Acceptance map/manifest expectations**

   * Make explicit that `docs/acceptance_map_epic020.json` and `audit/EPIC020_MANIFEST.json` **must** include this token and its artifacts once the fix is merged, and that a future remediation PR is required if they diverge.

3. **Per‑route Live QA rule consumption**

   * Add a short note in EPIC020’s QA Rails or Tokens section referencing the new PF19 per‑route Live QA rule **by title**, not by re‑stating its text, to keep PF19 as the single home for the rule.

---

## **6\. PF23 — Reality‑Audits**

**Goal:** Tighten how PF23 audits are applied to HTTP‑surface epics like EPIC020.

**Target locations**

* Epic audit specification for HDE‑EPICs.

* Any section that describes required audit sections/content.

**Changes to introduce**

1. **Explicit HTTP‑parity requirement for HTTP‑surface epics**

    Add language to the effect of:

    “For any epic that alters or depends on HTTP routing, the PF23 reality audit MUST include an explicit comparison of dev harness and wsgi routing/behavior for each canon HTTP route in scope (including `POST /api/compat/v1` where applicable).”

    Requirements:

   * For EPIC020 and similar epics, PF23 audits must:

     * list which app factories and blueprints own `POST /api/compat/v1`, and

     * show that dev harness and wsgi apps share behavior (status, headers, envelope, canonical JSON output) for malformed and minimal valid payloads.

2. **Clarify timing**

   * Re‑affirm PF23 audits as **epic‑closure** artifacts, and note that for HTTP‑surface epics, the HTTP‑parity audit must be completed and green before D‑goal status is flipped to “Accepted” for any canon HTTP surface.

---

## **7\. Drain plan & linkage to EPIC020 work**

**When to drain**

* These canon changes should be drained **after**:

  1. The dev Reader harness mounts compat v1 and emits JSON error envelopes for malformed JSON (A1–A3).

  2. Dev harness \+ wsgi compat parity tests are in place and green (B1–B2).

  3. EPIC020 Live QA captures governed compat HTTP artifacts and wires them into the Evidence Index & Mirror (C2).

  4. A PF23 audit confirms dev vs wsgi compat parity and EPIC020 acceptance records are in sync (C3).

**How to drain**

* One or more documentation PRs should:

  * Implement the PF02/PF07/PF09/PF14/PF19/PF20/PF23 text changes above.

  * Update EPIC020’s acceptance map/manifest, Evidence Index, and Machine Mirror for the new compat HTTP Live QA artifacts.

  * Mark this ADDENDUM 13 as **drained** once all referenced PF docs have been updated and merged.

Until then, this addendum remains the single scratchpad record for the **canon‑level** side of the EPIC020 compat HTTP remediation.

# Addendum 14 — Token fidelity rails for QA tokens, acceptance maps, and evidence  Type: NEW CANON \+ PROCESS

Context:  
 This addendum concerns governance and process for QA tokens and their wiring into epic-level acceptance maps, manifests, and evidence artifacts across the HD Engine, with immediate application to HDE-EPIC020 compat HTTP work and future epics that define or consume QA Acceptance Tokens. It sits at the intersection of Glow QA Guide (QA Acceptance Tokens, Live QA, CI rails), HDE-Phased Epics (D-goals and token rosters), HDE-Schemas & Artifacts (Evidence Index and Machine Mirror), and HDE-Build Checklist (CI/QA rails and acceptance tasks). It is prompted by a review drift where the same implementation plan for EPIC020 received conflicting approvals on whether token naming and token→evidence wiring were blocking issues, despite no change in PF-Canon or the plan itself.

Rule / Change:

1. **PF23 scope vs PF19 token semantics are independent axes.**  
    PF23 reality-audit scope (whether an epic runs a PF23 audit, and what that audit covers) MUST NOT weaken PF19 token semantics or governance. Decisions to waive or narrow PF23 usage for a specific plan or epic are local to that plan and do not change:

   * Which QA tokens exist in PF19’s registry,

   * How those tokens must be named, and

   * How they must be wired into acceptance maps, manifests, tests, CI jobs, Live QA steps, and evidence artifacts.

2. **Token/evidence matrix is mandatory before approving any plan or epic that touches QA tokens.**  
    For any implementation plan, QA plan, or epic record that introduces or consumes QA tokens, reviewers MUST construct (explicitly or as a checked artifact) a **token/evidence matrix** with, for each token row:

   * PF19 registry name,

   * Epic-level acceptance map name (must match PF19; no local aliases),

   * Tests that exercise the token’s behavior (unit/integration),

   * CI jobs that enforce it under closed rails,

   * Live QA steps that demonstrate it (if applicable),

   * Evidence artifacts (paths) generated by those tests/steps, and

   * Evidence Index & Machine Mirror entries (`artifact_key`, `epic_id`, `tokens`, `proof_anchor`).  
      No token in scope may have any cell in this matrix marked as “e.g.”, “TBD”, or left implicit at approval time. If any such gap exists, the plan MUST NOT be marked approved (`ASK OK`) for that token.

3. **PF19 is the single home for token semantics and names; epics only consume them.**

   * Any QA Acceptance Token used in an acceptance map or manifest MUST be defined in the PF19 registry with a canonical name and clear semantics before it is considered live.

   * Epic-level documents (HDE-Phased Epics records, acceptance maps, manifests, PF10 addenda, implementation plans) MUST reference tokens by their PF19 names only; they MUST NOT invent epic-local token names or synonyms for the same semantics.

   * If an epic needs a new token, that need MUST be recorded as a PF19 doc delta (NEW CANON or CANON UPDATE) and resolved in PF19 before the epic is considered token-complete.

4. **Previously identified token/evidence blockers cannot be silently downgraded.**  
    Once a reviewer has identified token naming or token→evidence wiring as a **blocking** issue (for example, open “e.g.” names, missing PF19 entry for a used token, or incomplete token/evidence matrix), that blocker MAY NOT be downgraded to “non-blocking” in a later review unless:

   * The plan has been updated to resolve the issue (e.g., token names made normative, evidence wired), **or**

   * PF-Canon has been explicitly updated (e.g., PF19 revised to add or change the token).  
      Any downgrade MUST reference the specific change (plan diff or PF doc change) that resolved the blocker; changes in reviewer interpretation or scope alone are not sufficient.

5. **Scope waivers must be explicit and non-transitive.**  
    If the Product Owner or governance chooses to waive or narrow a canon requirement for a particular plan (for example, deciding that PF23 audits are out of scope for a given implementation plan), reviewers MUST:

   * Record that as a local scope directive (e.g., “PF23 audits are not part of this plan’s workflow”), and

   * Explicitly state that other rails (PF19 tokens, PF12 evidence rules, PF20 D-goals, PF09 rails) remain fully in force.  
      Such waivers MUST NOT be interpreted as permission to relax token naming, acceptance mapping, evidence wiring, or other canon-backed rails.

6. **Re-ground in epic-specific approvals before asserting “no canonical token name”.**  
    Before any reviewer asserts that “no canonical token name exists yet” for a QA behavior, they MUST:

   * Re-check the PF19 registry, and

   * Re-read any epic-specific approvals or remediation guides (e.g., “EPIC020 Compat HTTP Defect – Remediation Guide (Revised)”) that may have already chosen a token name and semantics.  
      If such an approval defines a token name (for example, `EPIC020.D1.HTTP_COMPAT_MALFORMED_JSON` for compat malformed-JSON behavior), plans and acceptance maps MUST treat that name as canonical even if PF19 has not yet been updated; PF19 then becomes the drainage target, not a gate to invent new names.

7. **Plan approval requires token fidelity to be fully resolved, not deferred.**  
    For any plan or QA document that touches QA tokens:

   * Token names MUST be final (aligned to PF19 or to approved doc deltas that will land in PF19).

   * The token/evidence matrix MUST be complete, with every token wired to tests, CI, QA steps, and artifacts.

   * Any recognized token gaps (missing PF19 entries, unclear semantics) MUST be captured as PF19/PF20 doc deltas and treated as part of epic scope, not “future governance work” detached from the implementation.  
      A plan with open questions like “which token name do we use here?” or “these tokens are examples only” MUST be treated as **not ready** and returned for revision.

Rationale / Source:  
 This addendum is based on an internal review failure in the EPIC020 compat HTTP defect remediation flow, where the same implementation plan received two contradictory approvals regarding QA tokens and evidence: one review correctly identified open token naming and token→evidence wiring as blocking, while a later review incorrectly treated them as acceptable “examples” and marked the plan approved, despite no change in PF-Canon or the plan content. The drift was caused by conflating PF23 audit scope with PF19 token strictness, failing to re-read the EPIC020 Remediation Guide’s explicit token naming decision, not re-running the token/evidence matrix when revisiting the plan, and prioritizing “plan is close” over the “no guessing” rule for token governance. This addendum encodes the remediation steps from that RCA as explicit, repeatable rails for future reviews and epic planning.

Impact:

* **Implementation & QA plans:**

  * All future epic Implementation Plans and QA Plans that touch QA tokens MUST include (or have attached) a token/evidence matrix before being approved.

  * Reviewers must refuse approval if token names are “e.g.”, “TBD”, or not clearly anchored to PF19 or an explicit doc delta.

* **PF19 — Glow QA Guide:**

  * PF19 MUST be updated to include governance text stating that tokens are centrally defined (names \+ semantics), that acceptance maps may not invent local aliases, and that a token/evidence matrix is required for any epic that adds or consumes tokens.

  * PF19’s QA Acceptance Tokens section MUST include guidance for how to register new tokens and how to wire them into acceptance maps and evidence artifacts.

* **PF20 — HDE-Phased Epics:**

  * PF20 SHOULD be updated to clarify that epic records reference tokens by their PF19 names and that epic acceptance maps must be token-complete and evidence-wired (via PF12) before epic closeout.

* **PF12 — HDE-Schemas & Artifacts:**

  * PF12 SHOULD be updated to note that Evidence Index / Machine Mirror records for QA artifacts must always include the PF19 token names responsible for those artifacts, supporting the token/evidence matrix as a first-class concept.

* **Review process:**

  * Review checklists for Implementation Plans, QA Plans, and epic records MUST add an explicit step for verifying token fidelity (PF19 name, acceptance map link, tests, CI, QA, artifacts, evidence indexing) and MUST treat any gaps as blocking until resolved.

# ADDENDUM 15 \- REMEDIAL PR01

## **Review Summary**

* This PR wires the **dev Reader harness** (`adapter/http_reader.create_app`) to register the existing `compat_blueprint` from `engine/http/compat_handler.py`, so that `POST /api/compat/v1` (and related compat paths) are exposed in the dev app using the same compat handler as the production/wsgi app; this closes the primary compat wiring gap in EPIC020.

* It adds dev-only compat 404/405 handling scoped to the `/api/compat/v1` namespace, using `engine.compat.errors.error_envelope("ERR_NOT_FOUND")` and the canonical emitter `emit_public` to produce governed JSON error envelopes for compat 404/405 while leaving non-compat 404/405 behavior unchanged.

* A new test `tests/adapter/test_compat_http_dev.py::test_dev_compat_malformed_json_returns_compat_envelope` spins up the dev Reader app via `create_app()`, posts malformed JSON to `/api/compat/v1`, and asserts JSON status/headers/body, including LF-terminated bytes and the presence of `ok=False`, `code`, and `error` fields (and absence of HTML), providing an initial automated guard against regression.

* The PR correctly avoids modifying PF-Canon documents under `docs/pfcanon/**`, QA Plans, CI workflows, or Evidence Index/Mirror files; those are delegated to later PRs in the epic (PR2/PR3) as per the approved remediation plan.

* Overall, the changes are behaviorally correct relative to the EPIC020 plan and PF-Canon expectations for compat v1 (PF05, PF14), and the test posture is appropriate for PR1’s “wiring \+ smoke test” scope. I do not see any issues severe enough to require a remediation PR; additional tests, CI gating, and evidence wiring are expected to arrive in PR2.

---

## **Findings**

1. **Compat blueprint registration in dev harness**

   * `adapter/http_reader.py` now imports `compat_blueprint` from `engine.http.compat_handler` and registers it in `create_app()` with `app.register_blueprint(compat_blueprint)`. This respects the URL prefix declared in the blueprint (`url_prefix="/api/compat/v1"`) and matches the production app’s usage in `adapter/wsgi.py`.

   * This exactly addresses the missing compat wiring in the dev harness without introducing new endpoints or changing the wsgi app.

2. **Scoped compat JSON 404/405 behavior**

   * The dev app factory defines `_compat_error_response(status)` which wraps `error_envelope("ERR_NOT_FOUND")` through `emit_public`, setting JSON `Content-Type`, `Cache-Control: no-store`, and `Content-Length`.

   * Two app-level error handlers (`@app.errorhandler(404)` and `@app.errorhandler(405)`) check `request.path.rstrip("/").startswith("/api/compat/v1")`; if true they return `_compat_error_response(status)`, otherwise they return the original `err` object.

   * This yields compat JSON envelopes for 404/405 under `/api/compat/v1` only, and does not change non-compat error behavior, in line with the epic’s scoped 404/405 requirement.

3. **Canonical emitter/serializer usage**

   * `_compat_error_response` uses `emit_public(envelope)` from `engine.presenter.emitter`, which delegates to the canonical serializer in `engine.serializer.canon`.

   * The Response is created with `mimetype="application/json; charset=utf-8"` and `Content-Length` derived from the emitted payload; `ETag` and `Content-Encoding` are stripped.

   * This is consistent with PF14’s canonical JSON rules and matches the production compat error handlers, ensuring compat responses use the same emitter/serializer stack in dev and wsgi.

4. **Dev compat malformed JSON test**

   * `tests/adapter/test_compat_http_dev.py` uses `create_app()` to build a dev app client and posts `data=b"{bad: json"` with `Content-Type: application/json; charset=utf-8` to `/api/compat/v1`.

   * The test asserts:

     * `400 <= resp.status_code < 500` (coverage for compat 4xx).

     * `Content-Type` is exactly `application/json; charset=utf-8`.

     * `resp.data` ends with a newline.

     * Parsed JSON body has `ok is False`, `code` and `error` are strings, and no HTML markup (`"<html"` not present).

   * This provides a strong smoke-level assertion that dev compat returns a governed JSON error envelope for malformed JSON, and it aligns with PF05/PF14 compat schema expectations.

5. **No unintended changes to non-compat behavior**

   * The dev app’s `create_app()` still registers the reader blueprint (`bp`) at root, retains the `/internal/version` endpoint, and uses `_strip_etag_on_internal` after\_request to enforce “no ETag on /internal/\*” behavior.

   * The new compat 404/405 handlers explicitly guard on the path prefix; non-compat routes will continue to use the default Flask/blueprint behavior, avoiding global semantic changes.

6. **Tests and CI rails**

   * The PR adds a single new test module and does not modify CI workflows; pytest for `tests/adapter/test_compat_http_dev.py` passes locally.

   * This matches PR1’s agreed scope (“wiring \+ initial smoke test”), leaving full compat test coverage, parity tests, and CI rails enforcement to PR2.

7. **PF-Canon and scope adherence**

   * The PR does not modify any PF-Canon documents (PF02, PF05, PF07, PF09, PF10, PF12, PF14, PF19, PF20, PF23) or QA Plans, respecting PF06’s separation of implementation vs canon/docs and your explicit instruction for PR1.

   * Behavior is consistent with the compat HTTP semantics described abstractly in PF05/PF14: same path, same error envelope semantics, and use of canonical JSON emitter/serializer; the dev harness now matches the wsgi compat surface at the semantic level.

Given the scope and the larger epic plan, I consider this PR acceptable as-is; the remaining compat test and evidence work is clearly delegated to subsequent PRs.

---

## **Doc Deltas (PF-Canon only)**

No PF-Canon doc changes are strictly required by this PR alone. Production compat behavior and dev compat semantics are already described at a sufficient abstract level in PF05 (compat v1 HTTP surface) and PF14 (compat mechanics), and this PR simply brings the dev Reader harness into alignment with those contracts.

If you wish to record the new wiring explicitly in PF-Canon as part of a later docs pass (not this PR), the following deltas would apply:

* **Doc:** PF02 — Canon-HDE Architecture  
   **Section:** § “Adapter vs Dev Reader Harness” (or closest section on app factories)  
   **Delta:** Clarify that the dev Reader harness app (`adapter/http_reader.create_app`) now registers the same compat blueprint as the wsgi app for `POST /api/compat/v1`, so compat dev behavior in Codespaces uses the shared compat handler; note that this remains a dev/internal surface, not a public Reader API.

* **Doc:** PF05 — Canon-HDE-CLI-API-Vendor-Ref  
   **Section:** §5.5 “Compat v1 HTTP surface”  
   **Delta:** Add a brief note that the compat v1 dev route is exposed both via the wsgi app and via the dev Reader harness in Codespaces, both backed by the same compat handler and error envelope schema, and that malformed JSON on either must return the governed compat JSON error envelope.

(These are doc deltas for a later doc epic and are **not** part of this PR.)

---

## 

# **ADDENDUM 16 — ADR: Evidence Bundles & Manifests (Candidate 1\)**

Timestamp: \<to be filled on merge\>  
 Tag/type: **ADR \+ NEW CANON PROPOSAL \+ Engine Refactor Plan**

---

## **Details**

### **1\. Decision & Intent (ADR)**

**Decision**

We adopt **Candidate 1 — Evidence Bundles with Manifests** as the new baseline evidence architecture for the HD Engine:

* Move from a 1:1 model (“every artifact is a checked‑in file with its own `.path_proof.txt` and Machine Mirror row”) to a **ledger‑centric model** where:

  * Evidence is grouped into **textual bundles** (e.g. consolidated JSON/JSONL files), and

  * Each bundle has a **manifest** that enumerates its members (logical artifact keys, hashes, sizes, etc.).

* The **manifest \+ bundle** are treated as governed artifacts:

  * They are indexed in `docs/evidence/INDEX.json` and mirrored in `artifacts/evidence_index.jsonl` under the existing Evidence Index / Machine Mirror discipline.

* The **new hard requirement** is preserved:

  * **Evidence must be readable per PR by a ChatGPT‑class agent**, via text‑based manifests and bundles under governed paths.

**Non‑goals**

* We **do not** adopt Merkle trees, hash‑only families, or contract‑only (token‑only) evidence in this ADR; those remain future epics (Candidates 2–4).

* We keep **PF12/PF14 determinism and CI gating** intact: same‑PR parity, canonical JSONL Machine Mirror, path‑proof discipline at the bundle level.

---

### **2\. Canon deltas (PF‑Canon drain targets)**

This ADR requires the following **doc deltas**, to be drained into PF‑Canon. Tags follow PF language: `NEW CANON`, `CANON GAP`, `CANON RECONCILIATION NEEDED`.

(Section names are approximate; final anchors should match actual PF headings.)

#### **2.1 PF12 — HDE‑Schemas & Artifacts**

**§Evidence Index & Machine Mirror / Appendix D** — `NEW CANON`

* Introduce **“evidence bundle” artifacts**:

  * A **bundle file** (textual, typically JSON/JSONL) under `artifacts/**` or `docs/evidence/**`.

  * A **bundle manifest** (JSON/JSONL) that lists for each member: logical `artifact_key`, hash (`sha256`), size, and optional descriptors.

* Specify that for selected evidence families, the **Human Evidence Index** and **Machine Mirror**:

  * Track **bundles \+ manifests** as the governed artifacts,

  * Instead of listing every internal member as a separate row.

* Extend Mirror schema to allow **bundle‑oriented fields** (names only here):

  * e.g. `bundle_key`, `bundle_manifest_path`, `bundle_member_count`.

  * Keep existing core fields (`artifact_key`, `discovered_physical_path`, `sha256`, `proof_anchor`) stable.

* Clarify **path‑proof semantics** for bundles:

  * Path proofs live at the **bundle file** level.

  * The manifest is the canonical mapping from logical artifact IDs to bundle membership and hashes.

**§Evidence Index & Machine Mirror / Path‑Proof Semantics** — `CANON RECONCILIATION NEEDED (future)`

* Note (for future Candidate‑4 work):

  * Current canon still expects **per‑artifact path proofs**; this ADR **does not change** that, except that “artifact” can now be “bundle artifact”.

  * If later we introduce pure hash‑only families, PF12 must be explicitly reconciled to allow **index‑only** proof models; that is out of scope for this ADR but should be flagged.

#### **2.2 PF14 — HDE‑Mechanics Guide**

**§1.3.1 Evidence jobs (single‑writer tools)** — `NEW CANON`

* Add a **bundle generation mechanic**:

  * A named evidence tool (titles only in PF14) responsible for:

    * Collecting raw evidence outputs for a family;

    * Building a **textual bundle** (JSON/JSONL);

    * Emitting a **bundle manifest** (list of member artifact keys \+ hashes).

  * Runs under the same pinned env as existing evidence generation (`LC_ALL`, `LANG`, `TZ`, etc.).

* Clarify that `tools/evidence/update_evidence_index.py`:

  * Remains the **single writer** for: `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`, and path proofs;

  * Now **consumes bundle manifests** and writes **bundle‑level Mirror rows** and path proofs while preserving behaviour for non‑bundled families.

* Extend “Index \+ Mirror parity checks” to include:

  * Manifest validity (JSON/JSONL structure, required fields, no unknown keys);

  * Bundle‑level invariants (e.g. member count, deterministic ordering);

  * While preserving canonical JSONL, sorted keys, one trailing LF, and strict key set for the Machine Mirror.

**§Governed locations / Evidence & CI coupling** — `NEW CANON`

* State that **core governed evidence** for the HD Engine:

  * MUST remain **text‑based and agent‑readable** (Human Index, Machine Mirror, bundle manifests, key QA logs).

  * MUST live under governed paths: `artifacts/**`, `audit/**`, `docs/evidence/**`.

* Binary/compressed bundles are allowed only as **supplementary** artifacts, never as the sole governed evidence for any acceptance token that Codex/ChatGPT is expected to reason about.

* Link this posture to PF23 Reality Audits (see below).

#### **2.3 PF09 — HDE‑Build Checklist**

**Phase I/II “Evidence Index / Mirror discipline” tasks** — `NEW CANON`

* Update tasks like `EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_PATHS_VALIDATED_OK` to explicitly cover **bundle‑based evidence families**:

  * Validate that **bundles and manifests are generated** under pinned env;

  * Confirm they are **registered** in Human Index and Machine Mirror;

  * Confirm the presence of **bundle‑level path proofs**;

  * Clarify wording from “one Mirror row per artifact file” to “one Mirror row per governed artifact or bundle, as defined in PF12”.

#### **2.4 PF19 — Glow QA Guide**

**§9A QA Acceptance Tokens Registry & Evidence Posture** — `NEW CANON + CANON GAP`

* Add a QA principle:

  * **Baseline HD Engine evidence must be inspectable via text artifacts at the PR level**, suitable for Codex/ChatGPT agents (PF23).

* Optionally define a new QA token (name only in PF19), e.g. **`EVIDENCE_LEDGER_AGENT_READABLE_OK`**:

  * Semantics anchored in PF04/PF09: ensures that required bundles/manifests/logs exist as plain‑text files under governed paths and are wired into Evidence Index / Machine Mirror.

* Clarify that **pure contract/token families** (Candidate 3\) are allowed only when the evidence consumer does **not** need to inspect payloads; otherwise they must be paired with at least one governed text artifact (bundle manifest, QA log, or summary).

#### **2.5 PF02 — HDE Architecture**

**§5.3 Evidence posture (titles/paths only)** — `NEW CANON`

* Refine architecture‑level evidence posture to explicitly name:

  * **Human Index (`docs/evidence/INDEX.json`)**,

  * **Machine Mirror (`artifacts/evidence_index.jsonl`)**, and

  * **Evidence bundles/manifests**  
     as the primary “public evidence surfaces” for the engine.

* Add an architectural statement that HDE assumes **ledger‑centric, deterministic, text‑based evidence** that can be audited by humans and automated agents, consistent with PF19/PF23.

#### **2.6 PF23 — Reality‑Audits**

**§1 Scope & posture / Evidence & catalogs** — `CANON GAP`

* Add explicit guidance that Reality Audits for HD Engine:

  * **MUST** treat `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`, and any **bundle manifests** as the **authoritative evidence ledger**;

  * Codex should **prioritize** these when auditing evidence posture and D‑goal acceptance.

* Mention that these artifacts are designed to be **agent‑readable per PR**, linking back to PF19’s QA principle.

---

### **3\. Engine implementation & refactor steps (what‑not‑how)**

This section lists **concrete steps** required to implement the ADR in the repo. No code is specified; this is “what”, not “how”. It assumes the current code layout described in the repo map and earlier EPIC020 audit work.

#### **3.1 Evidence tooling**

1. **Introduce a bundle generator tool**

   * Add a new evidence tool under `tools/evidence/…` (name to be canonized in PF14) that:

     * Reads **raw evidence outputs** for one or more high‑churn families (ordering logs, sampler outputs, complex config dumps, etc.).

     * Produces a **textual bundle file** (e.g. JSONL, one artifact per line).

     * Emits a **bundle manifest** (JSON/JSONL) mapping `artifact_key` → `sha256` (+ size, optional metadata).

   * Enforce existing env pins: `APP_ENV`, `LC_ALL`, `LANG`, `TZ` etc., matching current evidence tooling behavior.

2. **Extend `tools/evidence/update_evidence_index.py`**

   * Teach it to:

     * Ingest one or more **bundle manifests** as input;

     * Compute file hashes for bundles and manifests;

     * Write **bundle‑level Machine Mirror rows** (including any new PF12 bundle fields) and bundle **path proofs**;

     * Maintain current behavior for **non‑bundled** evidence families (backwards compatible).

3. **Wire bundle generator into evidence pipelines**

   * In the evidence generation flow defined by PF14 (and the repo’s CI scripts):

     * Run tests/evidence producers as today.

     * Run the **bundle generator** to aggregate outputs.

     * Then run `update_evidence_index.py` as the single writer for Index/Mirror/proofs.

   * Treat failures in bundle generation or manifest validation as **hard CI failures**.

#### **3.2 Evidence artifacts & catalogs**

4. **Introduce bundle artifacts under governed paths**

   * Add new **bundle files** and **manifests** under `artifacts/**` and/or `docs/evidence/**`, following PF12’s bundle schema.

   * Start with **high‑churn** families (per Eval Remediation doc) to maximize file‑count relief:

     * Ordering determinism outputs.

     * Sampler outputs and complex ranking dumps.

     * Any other families currently generating many small JSON/LOG files.

   * Keep low‑volume, high‑value artifacts (identity snapshots, key QA logs) as discrete files initially; they can be migrated later.

5. **Update Human Evidence Index**

   * Update `docs/evidence/INDEX.json` so that:

     * Certain entries now reference **bundle artifacts** (bundle file \+ manifest) instead of every member file.

     * Titles and paths remain canonical and human‑readable.

   * Ensure `docs/evidence/INDEX.sha256` continues to serve as the hash sentinel for the human index, reflecting any structural changes.

6. **Update Machine Mirror**

   * Extend `artifacts/evidence_index.jsonl` to:

     * Include rows for **bundle artifacts** with bundle‑specific fields (per PF12);

     * Preserve schema and behaviour for **legacy artifact rows** (no breaking change for older commits).

   * Ensure Mirror remains: canonical JSONL, sorted keys, one LF, rejecting unknown keys.

7. **Path proofs**

   * Ensure `update_evidence_index.py` writes `.path_proof.txt` (or equivalent existing proof artifacts) at the **bundle file** level, consistent with PF12.

#### **3.3 CI / QA & tests**

8. **Extend Mirror/Index schema checks**

   * Update CI checks (e.g. `ci/checks/check_mirror_schema.sh` or equivalent) to:

     * Validate bundle‑specific fields.

     * Confirm any manifest referenced in the Mirror exists, is well‑formed, and lives under governed paths.

9. **Add tests for bundle generator**

   * Add unit/integration tests that:

     * Verify deterministic ordering of bundle contents under identical inputs/env;

     * Assert stable hashes for unchanged inputs;

     * Validate manifest schema and field ranges against PF12.

10. **Add tests for `update_evidence_index.py` bundle paths**

    * Tests to exercise mixed scenarios (bundled \+ unbundled):

      * Mirror rows generated correctly for bundles;

      * Evidence Index and Mirror stay in sync;

      * Path proofs exist for bundle artifacts.

11. **Tighten CI gates**

    * Extend existing gates (`EVIDENCE_INDEX_UPDATED_OK`, `EVIDENCE_INDEX_HASH_OK`, `MACHINE_MIRROR_UPDATED_OK`, `EVIDENCE_PATHS_VALIDATED_OK`) so that a PR **cannot go green** if:

      * Any bundle manifest referenced in the Mirror is missing/malformed;

      * Any bundle path proof is missing;

      * Bundle membership and manifest hashes are inconsistent.

    * Optionally add a CI check that **all governed bundles and manifests are plain‑text, LF‑terminated** (no opaque binary archives), to enforce agent‑readability.

#### **3.4 Audits & agent posture**

12. **Align PF23‑style Reality Audits**

    * Update any PF23 audit harness for HDE so that it:

      * Reads `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`, and bundle manifests as the **primary ledger**;

      * Reports **bundle coverage and membership** explicitly (e.g., counts, families, token mapping).

13. **Agent‑readable evidence validation**

    * For epics that rely on Codex/ChatGPT for evidence review, add a QA step that confirms:

      * All evidence required by their QA tokens is present in **textual form** (bundle manifests, logs, etc.);

      * Artifacts live under canonical paths and are referenced in Human Index/Mirror.

---

### **4\. Risk notes & constraints (for future work)**

* **Merge conflict risk:** Large JSONL bundles can become hotspots if multiple devs touch the same evidence family. Mitigation:

  * Split bundles by subsystem or epic where reasonable;

  * Keep bundle format and key ordering strictly deterministic.

* **No change to per‑artifact semantics yet:**

  * This ADR does **not** relax PF12/PF14’s current path‑proof and Mirror expectations; it only introduces **bundle artifacts** as a new class of governed artifacts. Any move to **hash‑only** evidence must be a future ADR and PF12 reconciliation.

* **Scope discipline:**

  * Candidate 2 (Merkle trees), Candidate 3 (token/contract‑only), and Candidate 4 (hash‑pinning) remain **future epics**. PF‑Canon impact for those is recorded in the “Scalable Models” doc and Eval Remediation notes but **must not** be implemented under this ADR.

---

### **5\. Drain & closure criteria for this ADR**

This ADDENDUM 14 can be considered **drained** when:

1. **PF‑Canon updates**

   * PF02, PF09, PF12, PF14, PF19, PF23 have doc changes merged that reflect the deltas listed in §2.

2. **Engine implementation**

   * Bundle generator exists and is wired into CI;

   * Human Evidence Index and Machine Mirror include bundle artifacts and manifests;

   * CI gates block missing/invalid bundles and manifests.

3. **Evidence posture**

   * At least one high‑churn evidence family has been migrated to bundles;

   * Per‑PR evidence ledgers (Index/Mirror/manifest) are demonstrably **agent‑readable** for Codex/ChatGPT.

4. **Reality Audit**

   * A PF23 Reality Audit confirms that the new bundle model is correctly reflected in repo reality and that CI/QA posture remains deterministic and trustworthy.

Once these conditions are met, this ADR should be reflected as **Accepted** in PF10 and linked from any future epics that evolve evidence architecture further (Merkle trees, hash‑only families, contracts).

