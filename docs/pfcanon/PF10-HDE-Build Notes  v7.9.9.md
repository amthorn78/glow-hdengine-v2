# 0\) Front Matter

**Name:** PF10-HDE-Build Notes   
**Version:** 7.9.9  
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

#  ADDENDUM 1 Dev sampler HTTP harness — Codespaces discovery and gaps

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

