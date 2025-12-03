# 0\) Front Matter

**Name:** PF10-HDE-Build Notes   
**Version:** v8.0.3  
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

#  ADDENDUM 1 \- Dev sampler HTTP harness — Codespaces discovery and gaps

Type: CLARIFICATION

Context:  
 This addendum records the first concrete discovery run of the dev sampler HTTP harness in a Codespace and clarifies the distinction between **what is implemented in the adapter** vs. **what is still missing in infra and governance** for HDE-EPIC019 D3. It concerns:

* The behavior of `POST /internal/dev/sampler` when the Reader is started via `python -m adapter.http_reader` in a Codespace.

* The actual HTTP/1.1 transport posture observed in this environment.

* The provisional `DEV_SAMPLER_URL` chosen for the remedial plan.

Rule / Change:

* When the Reader is started in a Codespace with:

  * `PORT=8000`

  * `LC_ALL=C`, `LANG=C`, `TZ=UTC`

  * `SAFE_MODE=1`, `ALLOW_NETWORK=0`

  * `APP_ENV=dev`  
     and the adapter module `adapter.http_reader` is launched as `python -m adapter.http_reader`, the dev sampler HTTP harness **does respond on** `http://127.0.0.1:8000/internal/dev/sampler` and speaks well-formed HTTP/1.1 with canonical JSON as expected by the Mechanics Guide:

A POST request with:

 {"viewer\_id":"qa-viewer","candidate\_ids":\["A","B"\],"seed":"111"}

*  yields an `HTTP/1.1 200 OK` response with:

  * `Content-Type: application/json; charset=utf-8`

    * `Cache-Control: no-store`

Canonical JSON body:

 {"candidate\_ids":\["A","B"\],"meta":{"seed":"111"},"viewer\_id":"qa-viewer"}

*   
  * exactly matching the dev sampler contract (IDs-only plus seed echo).

* However, when the same harness is invoked with `APP_ENV=prod` (other pins unchanged), the observed behavior in this discovery run is **still** `HTTP/1.1 200 OK` with the same canonical JSON body, not a 403 writer envelope. That is:

  * The APP\_ENV gating which PF20 and earlier EPIC019 PRs describe as “dev/test/local-only” is **not currently enforced in the running Codespace Reader**; `/internal/dev/sampler` responds with 200 under APP\_ENV=prod in this environment.

* For the purposes of the remedial plan and Codespaces/local dev, the Engine team has selected and validated the following **provisional** DEV\_SAMPLER\_URL (infra-owned value):

  * `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`

* derived from:

  * The successful APP\_ENV=dev 200 run against `127.0.0.1:8000` in this Codespace.

* This addendum does **not** change the canonical D3 requirement; it records that:

  * The adapter/harness contract and canonical JSON behavior are correct and proven in a Codespace for APP\_ENV=dev.

  * The APP\_ENV gating is currently **not enforced** for APP\_ENV=prod in this environment and must be treated as a behavioral bug or infra mis-wiring to be addressed by the remedial implementation (PRs per the escalation CRD).

Rationale / Source:

* The discovery logs collected in this Codespace show:

  * For `APP_ENV=dev`, the dev sampler harness returns an HTTP/1.1 200 with canonical JSON and no ETag; this matches PF05 — HDE-CLI-API-Vendor-Ref dev/internal route semantics and PF14 — Mechanics Guide dev harness JSON emitter posture.

  * For `APP_ENV=prod`, the harness returns the **same** HTTP/1.1 200 response, not a 403, contradicting the EPIC019 D3 gating intent recorded in PF20 — HDE-Phased Epics and prior PF10 addenda (dev/test/local-only, prod denied).

* PF07 — Glow Infrastructure and PF19 — Glow QA Guide both state that **canonical infra/env values must be derived from the actual running system**, not PO guesses; this discovery run is the first explicit evidence that 127.0.0.1:8000 is a working Reader harness in a Codespace, and that APP\_ENV gating needs remediation.

* The `DEV_SAMPLER_URL` decision file created during this session is not evidence by itself; it is a **proposed infra binding** for use in the remedial PR that will add a dev Reader start command, a healthcheck script, and a canonical DEV\_SAMPLER\_URL binding in either the devcontainer or an env file. This addendum captures that proposal so PF04/PF07/PF09 can be updated later with precise infra guidance once the remedial PR is merged.

Impact:

* **Implementation / Remedial PRs (D3):**

  * The remedial implementation MUST:

    * Wire a dev Reader start command in Codespaces/local dev that matches this observed host/port (`127.0.0.1:8000`), or else explicitly change and document the port if a different one is chosen.

    * Introduce a single infra-owned DEV\_SAMPLER\_URL binding (most likely via `.devcontainer/devcontainer.json` or a dev env file) set to `http://127.0.0.1:8000/internal/dev/sampler` or the chosen host/port, and ensure all QA harnesses consume this binding.

    * Fix the APP\_ENV gating discrepancy so that APP\_ENV in {prod, missing, empty} yields a 403 writer envelope, while APP\_ENV in {dev, test, local} continues to return 200 with canonical JSON, as originally specified in PF20/PF14/PF05.

* **QA and evidence (EPIC019 D3):**

  * Future D3 Live QA scripts must:

    * Use DEV\_SAMPLER\_URL as defined by infra (not re-derive host/port).

    * Record in their logs which env pins (including APP\_ENV, SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ) were used and whether the harness behaved according to PF05/PF14/PF20 (200 vs 403).

    * Treat any 200 response under APP\_ENV=prod as either a behavior bug or configuration bug, not a “pass.”

* **Docs and PF updates (after merge):**

  * Once the remedial PR lands, PF07 — Glow Infrastructure and PF14 — Mechanics Guide should be updated (via PF03 redlines) to:

    * Document the canonical dev Reader start command and DEV\_SAMPLER\_URL for Codespaces/local dev by title and section only.

    * Clarify the APP\_ENV gating behavior for internal/dev harnesses (dev/test/local allowed, prod/empty/missing forbidden) as a normative requirement, with the dev sampler HTTP harness as a worked example.

# ADDENDUM 2 \- HDE-EPIC019 REMEDIATION PR01

## **Review Summary**

* This PR implements Card C1 of the HDE-EPIC019 remedial plan by wiring a canonical dev Reader start command for /internal/dev/sampler, introducing a single infra-owned DEV\_SAMPLER\_URL in the Codespaces devcontainer, and adding a Python-based healthcheck/diagnostic harness plus a pytest that exercises the harness end-to-end.  
* The changes are confined to infra/dev surfaces and docs: .devcontainer/devcontainer.json, README, a small EPIC019 remediation doc, a discovery note, scripts/dev\_start\_reader.sh, scripts/qa/dev\_sampler\_healthcheck.py, and tests/scripts/test\_dev\_sampler\_healthcheck.py. No adapter behavior, sampler core logic, PF-Canon, or governed evidence artifacts (Index/Mirror/path-proofs) are modified.  
* The dev Reader start script enforces PF-Canon rails for internal/dev harness infra: it pins APP\_ENV=dev by default, sets SAFE rails (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC), and binds adapter.http\_reader to port 8000 via python \-m adapter.http\_reader, matching the existing “dev runner” posture in the adapter module and PF14’s examples.  
* The devcontainer now exports DEV\_SAMPLER\_URL=http://127.0.0.1:8000/internal/dev/sampler, aligning with PF07/PF14/PF09’s requirement that DEV\_SAMPLER\_URL be a single infra-owned binding derived from actual Reader wiring, not guessed by PO/QA. The README and a focused docs/hde\_epic019\_remediation.md doc both refer to DEV\_SAMPLER\_URL as infra-owned and show how to start the Reader and run the healthcheck harness.  
* The scripts/qa/dev\_sampler\_healthcheck.py harness encapsulates the infra validation recommended in PF14/PF09: it parses DEV\_SAMPLER\_URL, starts the Reader in dev and prod modes with pinned rails, performs HTTP/1.1 POSTs using a minimal sampler payload, logs env pins and responses, and explicitly logs any gating discrepancy (status ≠ 403 for APP\_ENV=prod) without changing behavior. The pytest tests/scripts/test\_dev\_sampler\_healthcheck.py runs the harness against a dynamically chosen local port and asserts a 200 dev response plus presence of the “sampler\_response mode=dev” log line, ensuring the harness and script wiring are test-covered.  
* Overall, the PR faithfully implements PR 1 of the approved remedial Implementation Plan, remains within the rails of PF-Canon, and adds the infra \+ harness surfaces needed for Cards C2/C3 without introducing drift; I judge it acceptable as-is.

## **Findings**

1. **Canonical dev Reader start command is consistent with PF-Canon and prior behavior**  
   * scripts/dev\_start\_reader.sh exports APP\_ENV (default "dev"), SAFE\_MODE (default "1"), ALLOW\_NETWORK (default "0"), LC\_ALL, LANG, TZ, and PORT (default "8000"), then runs python \-m adapter.http\_reader with those envs. This matches the dev runner posture in adapter/http\_reader.py (host 0.0.0.0, port from PORT, dev harness only) and respects the closed-rails rails from PF09/PF19/PF14 for deterministic/dev harness work.  
   * The script is small, explicit, and lives under scripts/, which aligns with PF07’s expectation that infra owns start commands for internal/dev harnesses; there’s no attempt to re-wire Flask or alter the blueprint.  
2. **DEV\_SAMPLER\_URL binding in devcontainer matches PF07/PF14/PF09 expectations**  
   * .devcontainer/devcontainer.json now includes a containerEnv block with DEV\_SAMPLER\_URL set to http://127.0.0.1:8000/internal/dev/sampler. This makes DEV\_SAMPLER\_URL available in all Codespace shells and binds it to the same port and path the dev Reader script uses.  
   * PF07 (Glow Infrastructure) and PF14 (Mechanics) both require infra to provide a single infra-owned binding for DEV\_SAMPLER\_URL per environment and classify failures to reach or use it as infra/tooling issues, not sampler bugs; this change satisfies that requirement for the Codespaces environment without pinning the value in PF-Canon itself.  
3. **Healthcheck harness behavior aligns with the remedial plan and PF-Canon**  
   * scripts/qa/dev\_sampler\_healthcheck.py:  
     * Derives LOG\_DIR and LOG\_PATH from env (DEV\_SAMPLER\_LOG\_DIR, DEV\_SAMPLER\_LOG\_PATH) with sane defaults under notes/dev-sampler/, so tests can redirect logs to tmp paths and the repo is not polluted by default.  
     * Validates DEV\_SAMPLER\_URL scheme and host/port, waits for the Reader port to open via a small socket helper, and then issues HTTP/1.1 POSTs using urllib.request with Content-Type: application/json; charset=utf-8.  
     * For mode="dev": starts the Reader with APP\_ENV=dev and closed rails, posts a minimal payload, logs sampler\_response mode=dev and returns 0 only if status==200, which matches PF05/PF14/PF20’s dev sampler success path.  
     * For mode="prod": starts the Reader with APP\_ENV=prod, posts the same payload, logs gating\_diagnostic expected=403? actual\_status=… and, if status\!=403, logs “gating\_discrepancy observed”. Importantly, it does not fail the script purely on gating mismatch; it just records it, which is exactly what the remedial plan asked for (diagnostic, not behavior change).  
4. **Test harnesses are minimal and focused on infra, not on re-testing adapter semantics**  
   * tests/scripts/test\_dev\_sampler\_healthcheck.py selects an open port via a small socket helper, sets env (DEV\_SAMPLER\_URL, rails pins, PORT, and log dir/path overrides), and runs the healthcheck script as a subprocess. It asserts returncode==0 and then inspects the redirected log to confirm the presence of "sampler\_response mode=dev" and "status=200".  
   * The test does not assert on APP\_ENV=prod gating, which remains the adapter/Mechanics’ responsibility and is already covered by adapter tests (PF09 references tests/adapter/test\_dev\_sampler\_http.py::test\_dev\_sampler\_rejected\_in\_prod); this keeps responsibilities clear and avoids duplication.  
5. **Docs accurately describe the new infra and harness, and keep PF-Canon as authority**  
   * README’s quickstart now includes the dev Reader start script as the canonical dev harness command, under the existing closed-rails env pins. It also adds a “Dev sampler HTTP harness (dev/admin-only)” subsection that explains the start command, DEV\_SAMPLER\_URL, and the healthcheck harness at a high level without restating canonical contract details (those remain in PF05/PF14/PF19/PF20).  
   * docs/hde\_epic019\_remediation.md provides a focused note for Card C1: canonical start command, DEV\_SAMPLER\_URL as exported in the devcontainer, and a concrete command to run scripts/qa/dev\_sampler\_healthcheck.py under APP\_ENV=dev, with behavior expectations for dev and prod modes clearly labeled as QA/diagnostic only. It explicitly says the harness does not alter APP\_ENV semantics or promote evidence, which is consistent with the approved plan.  
6. **Discovery note is accurate and consistent with PF-Canon and code**  
   * notes/dev-sampler/dev\_sampler\_http\_discovery.md describes:  
     * The route and handler in adapter/http\_reader.py.  
     * The APP\_ENV gate \_dev\_admin\_gate() semantics (dev/test/local vs forbidden).  
     * Validation rules and response schema.  
     * The dev runner v.s. PF-Canon expectations for a dev Reader start command.  
     * The absence of a repo-wide DEV\_SAMPLER\_URL binding prior to this PR.  
   * This file is correctly treated as a discovery aide, not evidence; it has no impact on runtime behavior.  
7. **Rails semantics are honored, and SAFE vs ALLOW\_NETWORK behavior is surfaced rather than changed**  
   * The start script and healthcheck harness both default to SAFE rails (SAFE\_MODE=1, ALLOW\_NETWORK=0, locale/TZ pins), but because they use Python’s networking primitives in a dev-only QA harness, any deeper question about whether loopback HTTP is “allowed” under SAFE\_MODE=1 is appropriately deferred to PF-Canon. The harness logs the rails snapshot, and the plan explicitly says any SAFE semantics changes must be done in PF-Canon, not here. This PR does not change SAFE semantics; it only measures and logs.

Given all this, I do not see any correctness, safety, or PF-Canon alignment issues that require remediation.

## **Doc Deltas (PF-Canon only)**

* Doc: PF07 — Glow Infrastructure  
  Section: §8.2.1 “Infrastructure keys and URLs” (or the closest section that lists DEV\_SAMPLER\_URL)  
  Delta: Clarify that for the Codespaces dev environment, DEV\_SAMPLER\_URL is now wired via the devcontainer configuration as a single infra-owned binding, derived from the dev Reader process started by scripts/dev\_start\_reader.sh (titles only; do not pin host/port). Note that infra’s responsibilities for DEV\_SAMPLER\_URL now explicitly include maintaining that containerEnv binding and validating it via a healthcheck harness before QA uses it.  
* Doc: PF14 — HDE-Mechanics Guide  
  Section: §5.8/§10.x “Internal/dev HTTP harnesses” (the section that already describes /internal/dev/sampler)  
  Delta: Extend the dev sampler HTTP harness example to mention (by title) that the Engine repo provides a canonical dev Reader start helper script and a dedicated healthcheck harness for /internal/dev/sampler, and that infra uses these to validate the harness against the PF05/PF14 contract before handing DEV\_SAMPLER\_URL to QA; emphasize that this reinforces, not replaces, the existing APP\_ENV gating and SAFE rails semantics.  
* Doc: PF09 — HDE-Build Checklist  
  Section: HDE-CONJ001.4 “Dev/internal HTTP harness infra wiring” (or the subtask that mentions internal/dev HTTP harness start commands and URLs)  
  Delta: Update the HDE-EPIC019 row for D3 to state that, for the Codespaces environment, the “canonical dev Reader start command and DEV\_SAMPLER\_URL binding” requirement is satisfied by scripts/dev\_start\_reader.sh and the devcontainer’s DEV\_SAMPLER\_URL binding, with infra validation performed by the dev\_sampler\_healthcheck harness (titles only; no script paths in canon).

I do not see a need to update PF05, PF19, or PF20 at this stage: their dev sampler HTTP harness descriptions, Live QA semantics, and D3 narrative already match the behavior and responsibilities implemented here; this PR simply provides the infra/harness realizations that those documents anticipated.

# ADDENDUM 3 \-**REMEDIATION PR02A \+ BUG FIX**

## **Review Summary**

* This PR is a follow-up bugfix to the HDE-EPIC019 D3 dev sampler Live QA harness work: it changes scripts/dev\_start\_reader.sh so that APP\_ENV is **no longer forced to** dev **when unset or empty**, but instead respects whatever the caller sets (including empty or unset), allowing the dev sampler Live QA harness to accurately test forbidden APP\_ENV modes.  
* The key bug, flagged in Codex review of the previous “Enforce dev sampler status expectations” PR, was that the start script’s line : "${APP\_ENV:=dev}" meant the Live QA harness could never truly exercise the "empty" or "unset" modes it was expecting 403 for; the Reader always started in dev mode, returned 200, and the harness correctly flagged those modes as ok=False, but this made the harness unusable even when service behavior was correct.  
* The fix removes the defaulting of APP\_ENV to dev, introduces an APP\_ENV\_DISPLAY for logging, and exports APP\_ENV only if it is present in the environment; SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ, and PORT remain pinned. This preserves the deterministic rails while allowing Live QA harness calls to control APP\_ENV explicitly (dev/prod/empty/unset) as required by PF19/PF20 for ENV\_RAILS\_POLICY\_OK.  
* No tests were run in this PR (as explicitly noted in the Codex task), but the change is small, localized, and consistent with the approved remedial plan: it adjusts infra behavior to make previously-introduced harness expectations achievable, without touching adapter or sampler core behavior, evidence structures, or PF-Canon.  
* Overall, this PR corrects a harness/infra bug that would otherwise force the D3 Live QA harness to fail in “empty” and “unset” modes regardless of service correctness; it aligns the dev Reader start helper with PF-Canon’s expectation that APP\_ENV gating be testable per EPIC019 D3 and does not introduce new drift.

## **Findings**

1. The change in scripts/dev\_start\_reader.sh is narrowly scoped and mechanically correct  
   * Before this PR, the script contained:  
     * : "${APP\_ENV:=dev}"  
   * which sets APP\_ENV to dev whenever it is empty or unset, and then exports it along with SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ, PORT.  
   * After this PR, the script:  
     * Adds comments clarifying that it should “Allow APP\_ENV to be empty or unset so harnesses can verify forbidden modes. Avoid setting a default to ensure the Reader sees the caller's intent.”  
     * Introduces APP\_ENV\_DISPLAY="${APP\_ENV-}" purely for logging.  
     * Removes the : "${APP\_ENV:=dev}" line entirely.  
     * Exports APP\_ENV only if it is present (if \[\[ \-v APP\_ENV \]\]; then export APP\_ENV; fi), and still exports SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ, PORT.  
     * Logs \[dev-start\] APP\_ENV=${APP\_ENV\_DISPLAY} instead of ${APP\_ENV} so readers can see when APP\_ENV is unset or empty.  
2. RCA: Empty/unset APP\_ENV expectations in the Live QA harness were impossible to satisfy  
   * The previous “Enforce dev sampler status expectations” change in scripts/qa/dev\_sampler\_live\_qa.py added a mode table:  
     * ("dev", 200, "dev"), ("prod", 403, "prod"), ("empty", 403, ""), ("unset", 403, None)  
   * and \_run\_mode started the Reader with \_start\_reader(app\_env\_value, host, port) and asserted that the returned status matched expected\_status.  
   * However, \_start\_reader ultimately invoked scripts/dev\_start\_reader.sh, which unconditionally defaulted APP\_ENV to dev when unset/blank. For the "empty" mode (app\_env\_value="") and "unset" mode (app\_env\_value=None, causing APP\_ENV to be removed in \_base\_env), the child Reader process still saw APP\_ENV=dev because of : "${APP\_ENV:=dev}". That meant those modes always exercised the dev path and returned 200; the harness faithfully logged them as ok=False, but expectation of 403 was never achievable, even when the adapter gating was correct.  
   * In other words, the **root cause** was a mismatch between the harness’s expectations (403 for empty/unset) and the start script’s behavior (forcing dev), so the harness’s forbidden-mode tests would always fail for “empty” and “unset” regardless of service correctness, making ENV\_RAILS\_POLICY\_OK unachievable for those modes.  
3. How the fix resolves the bug  
   * By removing the defaulting of APP\_ENV and only exporting it when it already exists, the dev Reader process now sees APP\_ENV as:  
     * "dev" when the harness passes APP\_ENV=dev.  
     * "prod" when the harness passes APP\_ENV=prod.  
     * "" (empty) when the harness passes an empty string.  
     * Unset when the harness deliberately omits APP\_ENV from the child environment.  
   * This means the Reader’s gating logic in adapter/http\_reader.py (which PF-Canon already defines for different APP\_ENV values) can now be exercised exactly as the Live QA harness expects: dev should continue to return 200, prod should return 403, and empty/unset can now be verified against governance/Mechanics expectations without being silently remapped to dev.  
   * The harness’s status expectations (200 for dev, 403 for prod/empty/unset) now represent meaningful tests rather than impossible constraints.  
4. Alignment with PF-Canon (PF07, PF14, PF19, PF20)  
   * PF07 — Glow Infrastructure expects infra-owned start commands (like scripts/dev\_start\_reader.sh) to propagate rails and environment to child processes, not to rewrite APP\_ENV semantics themselves; APP\_ENV gating policy is owned by PF14 (Mechanics) and PF20 (EPIC-level behavior), and QA harnesses must be able to exercise it. This change restores that division of responsibility: infra’s start helper now simply forwards APP\_ENV from the harness, while PF14/PF20 continue to define what the Reader should do for each value.  
   * PF19 — Glow QA Guide §9A treats environment-gating tokens (including ENV\_RAILS\_POLICY\_OK) as contractual: there must be at least one harness that asserts per-APP\_ENV behavior and fails when gating regressions occur. The earlier harness change introduced per-mode expected\_status; this PR now ensures the infra layer no longer sabotages those expectations by forcing APP\_ENV to dev.  
   * PF20 — HDE-Phased Epics EPIC019 D3 describes “dev-only sampler endpoint harness” as relying on APP\_ENV gating to restrict HTTP harness usage to dev/test/local; with this fix, the infrastructure around the harness finally allows the gating semantics to be exercised for all relevant variants.  
5. Evidence and tests posture  
   * No new tests were run or added in this PR (explicitly recorded as “not run (not requested)” in the Codex task), and nothing in the diff suggests this change breaks existing tests:  
     * It affects only scripts/dev\_start\_reader.sh.  
     * It does not introduce new dependencies or modify adapter code.  
   * Residual risk:  
     * Developers who previously assumed scripts/dev\_start\_reader.sh defaulted APP\_ENV=dev for manual local use will now get APP\_ENV unset unless they explicitly set it. This is intentional for EPIC019’s QA posture, but it should be documented in non-PF docs (AGENTS.md/README) so people know to set APP\_ENV=dev when they want a “normal” dev session.  
     * The harness status expectations remain strict; until adapter gating is actually fixed for empty/unset according to PF-Canon, the harness will correctly report those modes as ok=False, and ENV\_RAILS\_POLICY\_OK should not be considered truly Green.  
6. No additional remediation appears necessary for this PR  
   * The fix is precisely scoped to the infra bug identified, it restores the ability of the harness to test APP\_ENV semantics as designed, and it doesn’t introduce any PF-Canon drift or obvious regressions.  
   * Future work is still required at the behavior level (for APP\_ENV empty/unset semantics in the adapter) and at the CI level (wiring the harness into automated checks), but those are correctly scoped to the broader remedial plan and not to this bugfix PR.

## **Doc Deltas (PF-Canon only)**

* Doc: PF07 — Glow Infrastructure  
  Section: §8.2 “HD Engine dev/QA services” (or the closest section that describes internal/dev Reader harnesses and environment config)  
  Delta: Clarify that infra-owned dev Reader start commands (like the internal dev\_start\_reader helper) must **propagate APP\_ENV from callers without forcing defaults**, so that QA harnesses can exercise APP\_ENV variants (dev/prod/empty/unset) as specified by HDE-Mechanics and HDE-Phased Epics; emphasize that APP\_ENV gating semantics are owned by PF14/PF20, not by the start script.  
* Doc: PF14 — HDE-Mechanics Guide  
  Section: §5.8 “Internal/dev HTTP harnesses” (or equivalent section describing /internal/dev/sampler and APP\_ENV gating)  
  Delta: Add a short note that the dev sampler HTTP harness is exercised via an infra-owned Reader start helper which must not override APP\_ENV, so QA harnesses like dev\_sampler\_live\_qa can enforce per-APP\_ENV expected statuses (200 for dev, 403 for forbidden modes) in line with PF19/PF20 tokens such as ENV\_RAILS\_POLICY\_OK.

(These are clarifications of existing responsibilities rather than new canon; they explain that infra start helpers must not silently force APP\_ENV and that gating behavior must remain testable from the harness layer.)

# ADDENDUM 4 \- REMEDIATION PR03  

## **Review Summary**

* This PR implements Card C3 (D6) of HDE-EPIC019 by adding a dedicated open-rails Live Vendor QA harness `scripts/qa/d6_live_vendor_qa.py` that exercises the HDAPI BodyGraph endpoint, classifies outcomes as `OK` / `FAIL_VENDOR` / `FAIL_TOOLING`, and writes governed JSONL logs plus a rails snapshot under `audit/qa/hde-epic019/d6-vendor-live-qa/`.

* It adds four new evidence families to the Human Evidence Index for EPIC019 D6 (`epic019.d6.vendor_live_qa.discovery_notes`, `…happy_path`, `…fail_vendor`, `…fail_tooling`, `…rails_snapshot`), updates the Machine Mirror and its path-proof, and refreshes the topology orientation demo to cover the expanded skeleton (total\_artifacts now 163).

* The EPIC019 acceptance map is extended with a D6 foundation “D6 — Live vendor QA and classification (HDE-EPIC019 remedial)” and token bindings for `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, and `DISCOVERY_BASELINE_OK`, each wired to the new harness and artifacts, and the EPIC019 manifest is updated accordingly with correct paths, hashes, sizes, and proof anchors for those artifacts.

* Rails posture for the D6 harness is explicit and correct for vendor Live QA: the script sets `ALLOW_NETWORK=1`, `SAFE_MODE=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`, and the rails snapshot records these pins plus PF-Canon references and the vendor host, satisfying PF19/PF04 open-rails documentation requirements while leaving the CI evidence jobs (D1–D5) on closed rails.

* The three D6 log files record a genuine happy path (200 \+ fully parsed HDAPI BodyGraph payload), a vendor-side failure (401 Invalid API Key) classified as `FAIL_VENDOR`, and a tooling failure (`https://invalid.invalid` host) classified as `FAIL_TOOLING`, all without logging secrets; together with the rails snapshot and discovery notes, they provide a coherent, auditable baseline for EPIC019’s D6 Live Vendor QA.

* CI remains fully green: the harness itself was exercised under open rails (`ALLOW_NETWORK=1 SAFE_MODE=0 … python scripts/qa/d6_live_vendor_qa.py`), and both `python tools/evidence/update_evidence_index.py --check` and `python tools/evidence/orientation_demo.py --check` pass, confirming that Index, Mirror, orientation demo, and path-proofs are self-consistent after the D6 additions.

## **Findings**

1. **D6 harness behavior is aligned with PF-Canon and Card C3**

   * `scripts/qa/d6_live_vendor_qa.py` sets open rails by default (`ALLOW_NETWORK=1`, `SAFE_MODE=0`, locale/TZ pins to C/UTC), enforces presence of `HDAPI_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY`, and builds an HTTPS POST to `…/bodygraphs` with a minimal BodyGraph payload. The harness does not log the keys themselves, only a redacted URL (scheme \+ host) and a stable payload shape, which matches PF05/PF07/PF14 guidance on vendor transport posture and secret handling.

2. **Failure classification semantics match PF19/PF20 intent**

   * The harness runs three scenarios and logs them as structured JSONL:

     * `happy_path.jsonl`: status 200, parsed JSON body with HD attributes, `result: "OK"`.

     * `fail_vendor.jsonl`: POST to the real HDAPI host with deliberately invalid credentials, status 401, parsed JSON error body (`code`, `message`, `status`), `result: "FAIL_VENDOR"`.

     * `fail_tooling.jsonl`: POST to `https://invalid.invalid`, status 503 with a decode error, `result: "FAIL_TOOLING"`.

   * The classification logic only marks a run `OK` for 2xx responses with no parse\_error; 4xx/5xx and unreachable cases map to `FAIL_VENDOR` or `FAIL_TOOLING`, which is exactly the split PF19 expects between vendor, infra/tooling, and behavioral problems.

3. **Rails snapshot and discovery notes provide a solid D0 baseline**

   * `audit/qa/hde-epic019/d6-vendor-live-qa/rails_snapshot.json` records:

     * Schema name (`epic019-d6-vendor-live-qa`), rails map (`ALLOW_NETWORK=1`, `SAFE_MODE=0`, locale/TZ pins), payload\_keys, vendor\_host (`api.humandesignapi.nl`), surface string `engine.cli vendor HTTP POST /bodygraphs`, and PF-Canon references (PF04, PF05, PF07, PF19).

   * `notes/d6_vendor_live_qa_discovery.md` documents the pre-implementation discovery: existing vendor surfaces (`scripts/ops/admin_vendor_qa.py`, `scripts/ingest/run_vendor_ingest.py`), lack of any prior D6-specific harness, and closed-rails-only CI posture, which matches the remedial CRD’s starting assumptions for D6.

4. **Evidence Index, Mirror, and orientation demo are updated correctly**

   * `docs/evidence/INDEX.json` now includes new entries for:

     * `epic019.d6.vendor_live_qa.discovery_notes` → `notes/d6_vendor_live_qa_discovery.md`

     * `epic019.d6.vendor_live_qa.happy_path` → `audit/qa/hde-epic019/d6-vendor-live-qa/happy_path.jsonl`

     * `epic019.d6.vendor_live_qa.fail_vendor` → `…/fail_vendor.jsonl`

     * `epic019.d6.vendor_live_qa.fail_tooling` → `…/fail_tooling.jsonl`

     * `epic019.d6.vendor_live_qa.rails_snapshot` → `…/rails_snapshot.json`

   * `artifacts/evidence_index.jsonl` contains matching Mirror records for each of these artifact\_keys, with sha256 and size\_bytes consistent with their `.path_proof.txt` siblings, and the Mirror self-record for `index.machine_mirror` and its path-proof have been refreshed. `docs/evidence/INDEX.sha256` and the orientation demo (`audit/gates/topology/orientation_demo.txt` with `total_artifacts: 163`) are also updated and pass `--check`, so there is no evidence skeleton drift.

5. **Acceptance map and manifest bindings for D6 tokens are coherent**

   * `docs/acceptance_map_epic019.json` now has a D6 foundation with `manifest_tokens` and `tokens` set to `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, and `DISCOVERY_BASELINE_OK`, status `"green"`. In `token_status`:

     * `LIVE_VENDOR_TRANSPORT_OK` lists the three JSONL logs (happy\_path, fail\_vendor, fail\_tooling) and uses `python scripts/qa/d6_live_vendor_qa.py` as its test.

     * `OPEN_RAILS_ENV_OK` lists `rails_snapshot.json` and `happy_path.jsonl` and uses the same harness as test.

     * `DISCOVERY_BASELINE_OK` lists the discovery notes and rails snapshot and also uses the harness as test.

   * `audit/EPIC019_MANIFEST.json` mirrors these bindings with correct artifact\_keys, discovered\_physical\_path values, proof\_anchor paths, sha256 hashes, and size\_bytes taken from the path-proofs, so map and manifest are in sync for D6.

6. **Rails separation between closed-rails CI and open-rails D6 remains intact**

   * The CI workflow `ci.yml` continues to pin `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` for all CI jobs (test and sanity-pipeline). The D6 harness is not wired into CI; it is expected to be a manual or separately triggered job. This respects PF07/PF09/PF19 guidance that determinism-sensitive CI stay closed while D6 Live Vendor QA runs explicitly open rails outside that pipeline.

7. **No remediation required for this PR**

   * The harness is conservative about secrets, clearly classifies outcomes, and uses a non-PII test identity; evidence artifacts are wired cleanly into Index, Mirror, path-proofs, acceptance map, and manifest; orientation and INDEX checks pass; and closed-rails determinism posture for the rest of EPIC019 is unchanged. I don’t see any correctness, safety, or PF-Canon alignment issue that would require a remediation PR.

## **Doc Deltas (PF-Canon only)**

* Doc: PF19 — Glow QA Guide  
   Section: §9.A “QA Acceptance Tokens” (or the nearest section where environment and vendor QA tokens are defined)  
   Delta: Extend the registry to explicitly document the semantics of the D6 tokens `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, and `DISCOVERY_BASELINE_OK` for EPIC019:

  * `LIVE_VENDOR_TRANSPORT_OK` is satisfied when an open-rails Live Vendor QA harness exercises a canonical vendor BodyGraph flow (HDAPI /bodygraphs), logs at least one `RESULT=OK` happy-path run and at least one classified failure (`FAIL_VENDOR` and/or `FAIL_TOOLING`), and leaves governed evidence under an EPIC-scoped audit path.

  * `OPEN_RAILS_ENV_OK` is satisfied when the same harness produces a rails snapshot that makes ALLOW\_NETWORK, SAFE\_MODE, and locale/TZ pins explicit, referencing PF04/PF05/PF07 as the basis for that posture.

  * `DISCOVERY_BASELINE_OK` is satisfied when a discovery note and rails snapshot exist for the D6 harness, documenting vendor surfaces, env keys, and rail choices.

* Doc: PF20 — HDE-Phased Epics  
   Section: §2.4 “HDE-EPIC019”  
   Delta (NEW CANON PROPOSAL): Add a paragraph under EPIC019 describing D6 as a remedial deliverable “D6 — Live vendor QA and classification”, listing its acceptance tokens (`LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, `DISCOVERY_BASELINE_OK`) and referencing the D6 harness as the canonical open-rails HDAPI Live QA path that must be run with ALLOW\_NETWORK=1 and governed logs under the EPIC019 audit tree.

* Doc: PF09 — HDE-Build Checklist  
   Section: The EPIC019 row for D6 (or, if not present yet, the “Live Vendor QA” subsection)  
   Delta (NEW CANON PROPOSAL): Add a checklist row for D6 that requires:

  * A documented open-rails vendor harness that matches PF05 request shaping for HDAPI.

  * At least one happy-path run and one classified failure logged under `audit/qa/<epic_id>/d6-vendor-live-qa/…`.

  * Evidence Index/Mirror entries and path-proofs for these artifacts.

  * Acceptance map and manifest entries binding the D6 tokens to this harness and its logs.

# ADDENDUM 5 \- Docs PR

## **Review Summary**

* This PR is a docs-only sweep that aligns README.md, CHANGELOG.md, AGENTS.md, and several `./docs/**` files with the completed state of HDE-EPIC019, including the three remedial cards: C1 (dev Reader helper \+ DEV\_SAMPLER\_URL \+ healthcheck), C2 (D3 dev sampler Live QA evidence and D3 token bindings), and C3 (D6 open-rails vendor Live QA harness and D6 token bindings).

* README is rewritten to introduce a clear EPIC019-aware project overview, explicit architecture/rails sections, a dev vs public surfaces section, and a Quickstart that shows closed-rails public CLI usage plus dev/admin-only sampler harnesses (dev Reader helper, healthcheck, D3 Live QA) and D6 vendor harness at a glance.

* AGENTS.md now makes roles EPIC019-aware (Lead Dev, Codex/dev, Evidence harness, Config/bundle, QA/Verifier, Doc agents), explicitly assigns ownership of the dev Reader helper and DEV\_SAMPLER\_URL to dev/infra agents, and lists the three EPIC019 QA harnesses (`dev_sampler_healthcheck.py`, `dev_sampler_live_qa.py`, `d6_live_vendor_qa.py`) as QA/Verifier responsibilities.

* `docs/CLI_commands.md`, `docs/INDEX.md`, `docs/RUN.md`, and `docs/architecture/emitters.md` now consistently describe the division between public CLI and dev/admin harnesses, closed vs open rails, and the new EPIC019 QA harness scripts, while `docs/evidence/EPIC019_evidence.md` and `docs/hde_epic019_remediation.md` provide focused overviews of EPIC019 evidence posture and remedial rails for Cards C1–C3.

* CHANGELOG gains a new EPIC019 entry (“Remedial harnesses and evidence wiring (C1–C3)”) that clearly documents the new infra and QA harnesses and how they relate to D3 and D6 tokens; older entries for EPIC019 and earlier epics are left intact and still accurate.

* Overall, the PR keeps repo docs in line with the approved implementation plan and PF-Canon titles, reinforces the closed-rails default posture and the narrow open-rails exception for D6, and avoids leaking secrets or over-specifying PF-level edge cases; I do not see any issues requiring remediation.

## **Findings**

1. **README.md is now EPIC019- and remedial-aware and matches the harness layout**

   * The README’s “Project overview” explicitly mentions HDE-EPIC019 as completing Dissolution Pass 2, layering compat, sampler core (HDE-DISS003), and Engine Core (HDE-DISS004), and calling out remedial work for D3 (dev sampler harness \+ evidence) and D6 (open-rails vendor Live QA harness).

   * “Architecture & components” describes sampler and Engine Core modules, the internal/dev HTTP harness `/internal/dev/sampler` started via `scripts/dev_start_reader.sh`, and the evidence structure (Index, Mirror, path proofs, orientation demo, EPIC019 acceptance map \+ manifest, D3/D6 artifacts under `audit/qa/hde-epic019/`).

   * “Determinism & rails” separates closed-rails determinism/evidence runs from D6 open-rails vendor QA and references PF-Canon titles correctly; “Dev vs public surfaces” and “Quickstart” show the dev Reader helper, DEV\_SAMPLER\_URL, healthcheck harness, and D3/D6 harness scripts in context.

2. **AGENTS.md now assigns remedial harness ownership and keeps PF-Canon precedence explicit**

   * Roles section now states that Lead Dev is responsible for sampler \+ Engine Core scope “including remedial Cards C1–C3,” and that Codex/dev agents own the dev Reader helper (`scripts/dev_start_reader.sh`) and DEV\_SAMPLER\_URL wiring for dev/test/local only.

   * Evidence harness responsibilities explicitly include keeping Index and Mirror in sync with EPIC019 acceptance bindings “including D3 dev sampler Live QA and D6 vendor Live QA families under `audit/qa/hde-epic019/`.”

   * QA/Verifier’s role is extended to include running EPIC019 QA harnesses (`dev_sampler_healthcheck.py`, `dev_sampler_live_qa.py`, `d6_live_vendor_qa.py`) in addition to existing sanity pipeline duties, and Doc agents are told to document rails posture for D3 (closed) vs D6 (open vendor rails only). These assignments are consistent with the implementation plan and PF-Canon’s separation of infra, QA, and doc responsibilities.

3. **CHANGELOG.md captures EPIC019 remedial work clearly without leaking internals**

   * The new entry “2025-12-18 — EPIC-019: Remedial harnesses and evidence wiring (C1–C3)” lists:

     * Dev Reader helper \+ DEV\_SAMPLER\_URL \+ dev sampler healthcheck harness.

     * Dev sampler Live QA harness and its governed D3 evidence under `audit/qa/hde-epic019/dev_sampler_http/`.

     * D6 open-rails Live Vendor QA harness, the classification (`OK`, `FAIL_VENDOR`, `FAIL_TOOLING`), and its governed logs/snapshots under `audit/qa/hde-epic019/d6-vendor-live-qa/`.

   * The “Changed / Fixed” section notes that the dev Reader helper now tolerates empty/unset APP\_ENV when invoked by harnesses and that docs have been updated to describe dev/admin-only posture and APP\_ENV semantics without over-specifying edge cases; it also summarizes that evidence docs and acceptance roster reflect D3 and D6 remedial bindings and reference PF-Canon titles for rails semantics. This is exactly what we want in CHANGELOG: visible, non-technical operator-level notes pointing to deeper PF/EPIC docs.

4. **Docs for CLI, index, and runbook now consistently show D3/D6 harnesses and rails separation**

   * `docs/CLI_commands.md` now:

     * States that CLI commands must run under closed rails and explicitly calls out that “Open-rails allowances are limited to the D6 vendor Live QA harness below.”

     * Adds a “Dev/admin harnesses” section listing:

       * Dev Reader helper (`scripts/dev_start_reader.sh`),

       * Dev sampler healthcheck (closed rails),

       * Dev sampler Live QA (closed rails; APP\_ENV permutations),

       * D6 vendor Live QA (`scripts/qa/d6_live_vendor_qa.py`, open rails; SAFE\_MODE 0/1; controlled vendor test identity).

   * `docs/INDEX.md`’s Acceptance & evidence section now references the dev sampler QA harnesses and D6 vendor QA harness along with the usual evidence tools, and its local map links to `docs/hde_epic019_remediation.md` as an EPIC019 remedial summary.

   * `docs/RUN.md` adds a “Dev/admin harnesses” section showing exactly how to:

     * Start the dev Reader helper under closed rails,

     * Run the dev sampler healthcheck and Live QA harness using DEV\_SAMPLER\_URL,

     * Run the D6 vendor Live QA harness under ALLOW\_NETWORK=1 (with a clear “vendor test identity, governed logs only” note), plus log destinations for each.

   * These are all consistent with the remedial plan and do not contradict PF-Canon; they are repo-level runbook and CLI documentation, not new normative rules.

5. **Architecture and evidence docs now have EPIC019 “stories” for sampler and vendor QA**

   * `docs/architecture/emitters.md` now includes a “Sampler and harness layering (EPIC019)” section describing:

     * Public surfaces (Reader v1 and `hdctl showcompat`).

     * Dev/admin sampler surfaces (`hdctl dev:sampler`, `/internal/dev/sampler` via `scripts/dev_start_reader.sh`).

     * QA harnesses (closed-rails healthcheck and Live QA for dev sampler; open-rails vendor Live QA for D6), and the fact that outputs are governed evidence under `audit/qa/hde-epic019/` and indexed into EPIC019 acceptance artifacts.

   * `docs/evidence/EPIC019_evidence.md` (new) gives a concise evidence overview:

     * Evidence layers (Index, Mirror, path proofs, orientation demo, sanity pipeline).

     * Sampler and Engine Core evidence generators.

     * Dev sampler QA families (healthcheck \+ Live QA under closed rails, with logs under `audit/qa/hde-epic019/dev_sampler_http/` and acceptance bindings).

     * D6 vendor Live QA family (open rails; `d6_live_vendor_qa.py`; logs/snapshot under `audit/qa/hde-epic019/d6-vendor-live-qa/`; D6 token bindings).

   * `docs/hde_epic019_remediation.md` is rebuilt as a clear “remedial rails (Cards C1–C3)” doc: it explains the dev Reader helper (C1), DEV\_SAMPLER\_URL, dev sampler healthcheck (closed rails), D3 Live QA harness, and D6 vendor harness and how each maps to evidence and acceptance. These are helpful repo-side guides and do not attempt to duplicate PF-Canon.

6. **No obvious correctness or PF-Canon drift; issues appear minor or stylistic**

   * All scripts and commands referenced in docs exist in the repo and match their names in the diffs (`scripts/dev_start_reader.sh`, `scripts/qa/dev_sampler_healthcheck.py`, `scripts/qa/dev_sampler_live_qa.py`, `scripts/qa/d6_live_vendor_qa.py`, `tools/evidence/*`, etc.).

   * Closed vs open rails semantics are consistently described: closed rails for determinism and D3 harnesses; `ALLOW_NETWORK=1` open rails only for the D6 vendor harness.

   * Doc text repeatedly points readers to PF-Canon by title for canonical behavior and token semantics.

   * The only potential follow-up is ergonomic: for example, some README headings and sections could eventually be split into separate docs if they grow, but nothing here conflicts with canon or misleads operators.

Given all this, I judge the PR acceptable as-is; no remediation prompt is required.

## **Doc Deltas (PF-Canon only)**

* Doc: PF20 — HDE-Phased Epics  
   Section: §2.4 “HDE-EPIC019 — Dissolution Pass 2” (or the EPIC019 section that currently describes D1–D5)  
   Delta (NEW CANON PROPOSAL): Extend the EPIC019 entry to explicitly acknowledge the remedial work for D3 and D6 described in this PR:

  * Note that D3 acceptance now includes a dev-only sampler HTTP harness for `/internal/dev/sampler`, with a canonical dev Reader helper, infra-owned DEV\_SAMPLER\_URL, and closed-rails Live QA harness exercising APP\_ENV permutations and bound to D3 tokens.

  * Note that D6 acceptance includes a single open-rails vendor Live QA harness for HD APIs with classified `OK` / `FAIL_VENDOR` / `FAIL_TOOLING` outcomes, governed logs/snapshots under an EPIC019 audit tree, and D6 token bindings.

* Doc: PF09 — HDE-Build Checklist  
   Section: The Dissolution Phase rows for EPIC019 (HDE-DISS003.5 / D3 and D6 rows)  
   Delta (NEW CANON PROPOSAL): Add explicit checklist items that reference the presence of:

  * A canonical dev Reader helper \+ DEV\_SAMPLER\_URL binding for internal/dev sampler HTTP harness.

  * A closed-rails D3 Live QA harness for `/internal/dev/sampler` that drives APP\_ENV permutations and produces governed logs under `audit/qa/hde-epic019/dev_sampler_http/`.

  * An open-rails D6 Live Vendor QA harness and rails snapshot under `audit/qa/hde-epic019/d6-vendor-live-qa/` with evidence families registered in Index/Mirror and acceptance map/manifest wiring complete.

* Doc: PF19 — Glow QA Guide  
   Section: §9.A “QA Acceptance Tokens” (or the section where environment rails and Live Vendor QA tokens are defined)  
   Delta: Clarify that for EPIC019:

  * `ENV_RAILS_POLICY_OK` for D3 is satisfied using a closed-rails dev sampler healthcheck/Live QA harness that exercises APP\_ENV=dev/prod/empty/unset and treats any unexpected status codes as failures.

  * `LIVE_VENDOR_TRANSPORT_OK`, `OPEN_RAILS_ENV_OK`, and `DISCOVERY_BASELINE_OK` are satisfied by a dedicated D6 harness that runs under explicitly logged open rails and records `OK`, `FAIL_VENDOR`, and `FAIL_TOOLING` classifications, plus a rails snapshot and discovery notes.

* Doc: PF14 — HDE-Mechanics Guide  
   Section: The section describing internal/dev HTTP harnesses and sampler/Engine Core mechanics (e.g., “Internal/dev HTTP surfaces” or the sampler section)  
   Delta: Add a short subsection noting that:

  * `/internal/dev/sampler` is the canonical internal/dev HTTP harness for sampler core parity (APP\_ENV=dev only).

  * It is started for QA via a dev Reader helper script and is consumed by D3 healthcheck/Live QA harnesses under closed rails.

  * D6 Live Vendor QA uses a separate open-rails harness for vendor transport validation and is never part of the determinism CI pipeline.

# ADDENDUM 6 — DEV\_SAMPLER\_URL env binding for Codespaces

Type: CLARIFICATION

Context:  
 This addendum clarifies the **operational definition and ownership** of the `DEV_SAMPLER_URL` environment variable for the HDE-EPIC019 dev sampler HTTP harness in a Codespaces dev environment. It is a direct continuation of Addendum 1 (D3 dev sampler HTTP discovery) and Addendum 2/3 (Remediation PR01 \+ PR02A) and concerns:

* Where `DEV_SAMPLER_URL` **must live** in a Codespaces container.

* Exactly **what value** it must have for this environment.

* How dev harnesses (healthcheck and D3 Live QA) **depend on it** to function.

Rule / Change:

* `DEV_SAMPLER_URL` is a **required environment variable** for all dev sampler HTTP harnesses in this repo (healthcheck, D3 Live QA) and SHALL be treated as an infra-owned binding:

  * For the Codespaces dev environment, `DEV_SAMPLER_URL` MUST be set to:

    * `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`

  * derived from the actual dev Reader wiring: the dev Reader helper (`scripts/dev_start_reader.sh`) binds `adapter.http_reader` on port `8000` and exposes `POST /internal/dev/sampler` on `127.0.0.1`.

* In Codespaces, the **canonical home** for this binding SHALL be the devcontainer configuration, not ad-hoc shell exports:

  * `.devcontainer/devcontainer.json` MUST define `DEV_SAMPLER_URL` under a container environment block (e.g. `containerEnv`), so that every shell in the Codespace sees the same value without manual export.

  * Shell-level `export DEV_SAMPLER_URL=…` MAY be used for one-off debugging, but the devcontainer env is the authoritative source and should be treated as the “infra” binding for this environment.

* The following harnesses MUST NOT hardcode host/port or reconstruct `DEV_SAMPLER_URL` internally; they MUST read it from the environment and fail loudly if it is missing:

  * The dev sampler healthcheck harness (Remediation PR01).

  * The D3 dev sampler Live QA harness (Remediation PR02/PR02A).

  * Any future dev sampler HTTP QA tools.

* For other environments (local non-Codespaces dev, CI, etc.), `DEV_SAMPLER_URL` MAY point to a different host/port, but the **pattern is invariant**:

  * `DEV_SAMPLER_URL = <base_url>/internal/dev/sampler`

* where `<base_url>` describes where the dev Reader is actually bound. Those environments MUST define `DEV_SAMPLER_URL` in their own infra-appropriate way (env files, shell exports, or other container configs), and scripts MUST continue to treat it as an input, not as an algorithmically derived constant.

Rationale / Source:

* Addendum 1 established that in a Codespace, starting the Reader via `python -m adapter.http_reader` under pinned rails (`PORT=8000`, closed rails, `APP_ENV=dev`) makes `/internal/dev/sampler` respond at `http://127.0.0.1:8000/internal/dev/sampler` with the correct HTTP/1.1 \+ canonical JSON behavior, and recorded this as a **provisional DEV\_SAMPLER\_URL**.

* Remediation PR01 introduced `scripts/dev_start_reader.sh` and a devcontainer binding for `DEV_SAMPLER_URL`, but the **ownership and location** of this binding were still implicit: PF-Canon and the Implementation Guide say infra “owns” DEV\_SAMPLER\_URL per environment, and that PO/QA must not guess host/port, but in practice “infra” here is the same person maintaining the repo.

* Remediation PR02/PR02A hardened the D3 dev sampler Live QA harness to expect explicit APP\_ENV and HTTP status behavior and depends on DEV\_SAMPLER\_URL to be set correctly. Any attempt to recompute host/port inside harnesses would violate the “infra-owned binding” principle from HDE-Governance and Glow QA Guide and would make it harder to reason about where the harness is actually pointing.

* This addendum removes the remaining ambiguity by:

  * Pinning the Codespaces value.

  * Pinning the container-local home.

  * Making explicit that all dev sampler harnesses treat DEV\_SAMPLER\_URL as a required input.

Impact:

* **Implementation / infra (Codespaces dev):**

  * `.devcontainer/devcontainer.json` MUST include `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler` in its container env configuration.

  * `scripts/dev_start_reader.sh` and the dev sampler harnesses are considered correctly wired only when starting the Reader and calling DEV\_SAMPLER\_URL yield the behavior and logs described in Addendum 1 and Remediation PR01 (200 \+ canonical JSON for APP\_ENV=dev at `/internal/dev/sampler`).

* **QA and evidence (D3):**

  * The dev sampler healthcheck and D3 Live QA harnesses MUST treat missing or mismatched DEV\_SAMPLER\_URL as infra/tooling failure (e.g., exit non-zero with a clear log), not silently fall back to hardcoded URLs.

  * D3 evidence logs under `audit/qa/hde-epic019/dev_sampler_http/` MUST record the actual DEV\_SAMPLER\_URL and rails in effect (APP\_ENV, SAFE\_MODE, ALLOW\_NETWORK, LC\_ALL, LANG, TZ) so future audits can see which Reader this harness spoke to.

* **Docs and PF updates (future canon):**

  * When this addendum is drained, **Glow Infrastructure** should be updated to document DEV\_SAMPLER\_URL as an infra-owned env for dev environments (Codespaces, local dev, etc.), and to show the pattern `<base_url>/internal/dev/sampler` and the association with the dev Reader helper.

  * **HDE-Mechanics Guide** and **HDE-Build Checklist** should reference DEV\_SAMPLER\_URL by title/section when describing D3 dev sampler HTTP harness checks, but must not restate its exact value; environment-specific bindings remain a repository/devcontainer concern.

