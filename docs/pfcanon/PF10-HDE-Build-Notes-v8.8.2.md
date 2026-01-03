# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v8.8.2  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## Purpose

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

**Precedence and versioning**

* For any topic explicitly covered in this scratchpad, its content **temporarily supersedes canon** until those changes are reviewed and merged into the relevant PF docs.

* If multiple addenda exist for the same or similar scope (for example “1.”, “2.”, “ 3.”), the **highest-numbered / latest addendum is the only authoritative one**.

* **Older scratchpad files are considered fully drained or obsolete.** Agents must **not** read, reuse, or reconcile content from older scratchpads once a newer one exists; only the latest file matters.

Within a single scratchpad file:

* When an entry has been drained into PF-Canon, that entry is **removed completely** from the scratchpad.

* The current version of the file therefore contains **only live, not-yet-merged items**. If a topic is not present in the latest scratchpad, assume its source of truth is the relevant PF-Canon doc.

## Cross-references

 Inside this file, all references to PF documents MUST be **titles-only** (for example “HDE-Phased Epics”, “Glow QA Guide”), never file names or version numbers in the body text.

When editing or extending this file, ChatGPT sessions must:

* Not restate PF content here.

* Link by **document title and section only**.

# 1\) TEMPLATE

TEMPLATE Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\>  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## Addendum Index:

**This section should be considered current and authoritative. Index all addenda numbers listed below.**

1. 2.1 HDE-EPIC022 — Close-pack artifact registration vs observed repo layout (audit/EPIC-022\_\* vs audit/qa/hde-epic022/close\_pack/\*)  
2. 2.2  HDE-EPIC022 — Governance Token Registry completion for EPIC022 closure token set  
3. 2.3 HDE-EPIC022 — FAIL/TOOLING\_BLOCKED step-log claim hygiene (no \_OK token claims)

4. 2.4 — Live QA runbooks are gitless; traceability must come from governed identity artifacts (not `git …`)

5. 2.5 — Step-log header schema must include command and captured\_env (minimum reproducibility \+ machine-indexability)

6. 2.6 — Token semantics in logs must separate “intent” from “claim” (`intended_tokens` vs `claimed_tokens`)

7. 2.7 — Live QA plans must not pin version-stale PF filenames; canon references must be stable and workspace-resolvable

8. 2.8 — EPIC022 token registry single-home and “no unregistered tokens” rule  
9. 2.9 — Tokens in step logs are claims (no `_OK` claims on non‑PASS)

10. 2.10 — QA step-log manifest validity is a closure gate (schema \+ run grouping \+ uniqueness)

11. 2.11 — Evidence index ↔ mirror ↔ path-proof parity is mandatory for governed EPIC022 artifacts

12. 2.12 — /internal/version interim auth posture is canon (drain conflicts)

13. 2.13 — Standardize Live QA exit-code ↔ status mapping and token-claim reporting

14. 2.14 — Closure-scoped Live QA plans must not include placeholder non-PASS steps for required closure artifact families

# 2\) Numbered Addendum List

## 2.1 HDE-EPIC022 — Close-pack artifact registration vs observed repo layout (audit/EPIC-022\_\* vs audit/qa/hde-epic022/close\_pack/\*)

**Why:** The audit confirms close-pack artifacts exist under `audit/qa/hde-epic022/close_pack/…`, while PF20/PF12 register EPIC022 close-pack artifacts at `audit/EPIC-022_close_report.md` and `audit/EPIC-022_MANIFEST.json`. This mismatch makes closure non-defensible unless canon is explicit about which paths are authoritative for EPIC022 close-pack acceptance artifacts. (PF20 — HDE Phased Epics, §2.7.6; PF12 — Schemas & Artifacts, §8.17.11)

**Decision / rule / clarification:**

* For EPIC022, close-pack acceptance artifacts must have a **single canon-registered location**; any alternate location is drift and must be either:

  * (A) corrected in repo outputs to match the registered locations, **or**

  * (B) formally re-registered in PF-Canon as the new canonical locations (with legacy paths explicitly deprecated for EPIC022).

* If repo reality differs during execution, closure must include an explicit drift note and a drain target to reconcile canon, per the closure drift handling rule. (PF20 — HDE Phased Epics, §2.7.7.2)

**Drain targets (PF09/PF20 first; then others only if required):**

* Doc: **PF20 — HDE Phased Epics, §2.7.6**  
   Delta intent: Update the EPIC022 “Acceptance artifacts” list to reflect the canon-registered close-pack artifact paths chosen for EPIC022, and mark any alternate paths as deprecated/legacy for EPIC022 closure.

* Doc: **PF20 — HDE Phased Epics, §2.7.7.2**  
   Delta intent: Add a one-line EPIC022-specific note clarifying how drift is recorded in the close report when repo reality differs from registered paths (and what must be drained before claiming closure).

* Doc: **PF09 — Build Checklist, §2.4.2**  
   Delta intent: Ensure EPIC022 bridge notes do not imply acceptance can be claimed with unregistered close-pack artifact paths; explicitly tie close-pack acceptance to the PF20-registered artifact paths.

* Doc: **PF12 — Schemas & Artifacts, §8.17.11**  
   Delta intent: Register the EPIC022 close-pack artifact paths that PF20 now specifies (or explicitly note EPIC022 exceptions if the audit/qa close-pack location is adopted).

**Supersedes/conflicts (if applicable):**

* Conflicts with current EPIC022 close-pack registration in **PF20 §2.7.6** and **PF12 §8.17.11** if EPIC022 is already producing close-pack outputs under `audit/qa/hde-epic022/close_pack/…`.

---

## 2.2  HDE-EPIC022 — Governance Token Registry completion for EPIC022 closure token set

**Why:** PF20 explicitly flags token registry drift for EPIC022 closure tokens as a blocker to claiming acceptance; the audit also surfaced token/claim hygiene issues in step logs and manifests. Closure cannot be canon-defensible if closure tokens are referenced/claimed but not registered. (PF20 — HDE Phased Epics, §2.7.8.2; PF04 — HDE Governance, §9.7.10)

**Decision / rule / clarification:**

* Any token referenced by EPIC022 acceptance artifacts (step logs, token-evidence matrix, manifests) must exist in the Governance Token Registry **before** EPIC022 can be claimed SATISFIED.

* If an EPIC022 artifact currently references a non-registered token, it must be treated as **TOOLING\_BLOCKED evidence** until either:

  * the token is registered, or

  * the artifact is regenerated to reference the canonical registered token(s). (PF04 — HDE Governance, §9.7.10)

**Drain targets (PF09/PF20 first; then others only if required):**

* Doc: **PF20 — HDE Phased Epics, §2.7.5**  
   Delta intent: Confirm the EPIC022 “baseline token set” is the authoritative roster for closure artifacts, and reconcile names against the Governance Token Registry (remove placeholders; align names).

* Doc: **PF20 — HDE Phased Epics, §2.7.8.2**  
   Delta intent: Update the tracked issue to reflect current registry status (which tokens are now registered vs still pending) so closure-readiness is not ambiguous.

* Doc: **PF09 — Build Checklist, §4.4**  
   Delta intent: Add a cross-reference that the token roster validator is authoritative for closure claims; unregistered tokens force TOOLING\_BLOCKED and prohibit claiming SATISFIED.

* Doc: **PF04 — HDE Governance, §2.0**  
   Delta intent: Register any remaining EPIC022 closure tokens referenced by PF20 baseline closure requirements (minimal definitions; consistent naming).

**Supersedes/conflicts (if applicable):**

* Supersedes the “tracked issue” posture in **PF20 §2.7.8.2** once drained, by converting it into resolved registry entries or corrected token naming.

---

## 2.3 HDE-EPIC022 — FAIL/TOOLING\_BLOCKED step-log claim hygiene (no \_OK token claims)

**Why:** The audit shows a `FAIL_TOOLING` step log listing `_OK` tokens. Canon treats these as claims; this blocks closure and creates ambiguity about what actually passed. (PF20 — HDE Phased Epics, §2.7.7.2)

**Decision / rule / clarification:**

* Step logs and close-pack manifests must treat any listed tokens as **claims**, not “intended token rosters.”

* For any status other than PASS (including FAIL, FAIL\_TOOLING, TOOLING\_BLOCKED), **no `_OK` tokens may appear as claimed tokens** in that log’s claim surface.

* If tooling needs to record “intended tokens,” it must do so in a **non-claim** field or separate non-claim artifact explicitly labeled as non-canon.

**Drain targets (PF09/PF20 first; then others only if required):**

* Doc: **PF20 — HDE Phased Epics, §2.7.7.2**  
   Delta intent: Add an explicit note that “tokens listed in step logs are claims,” and define a canonical non-claim field/escape hatch for intended tokens (to prevent future violations).

* Doc: **PF19 — Glow QA Guide, §4.4**  
   Delta intent: Add a concise statement that the manifest/log claim surface must not include `_OK` token claims on non-PASS runs, aligning QA rails with PF20 claim semantics.

* Doc: **PF09 — Build Checklist, §4.4**  
   Delta intent: Align the close-pack generator and manifest emitter rules to explicitly prohibit `_OK` token claims on failed/blocked checks.

**Supersedes/conflicts (if applicable):**

* Clarifies and strengthens cross-doc alignment; no direct supersede unless PF19/PF09 currently permit non-PASS logs to list `_OK` claims.

## 2.4 — Live QA runbooks are gitless; traceability must come from governed identity artifacts (not `git …`)

**Why**

* Live QA runbooks are PO-executable operational procedures. Embedding `git` commands inside execution steps violates the gitless Live QA rail and creates non-portable runs (requires repo state \+ VCS tooling in the execution environment). This has repeatedly produced review blockers and closure-risk.

* Canon anchor: PF19 — Canon Glow QA Guide, §3.6.2.

**Decision / rule / clarification**

* **Hard rule:** PO-executable Live QA runbooks MUST NOT execute any `git …` command (including `git status`, `git rev-parse`, `git diff`, `git log`, etc.). (PF19 — Canon Glow QA Guide, §3.6.2)

* **Allowed exception boundary:** `git …` operations are allowed **only** in a *Codex planning/audit prompt* (read-only repo audit), not in the PO runbook execution steps. The PO runbook must remain executable without repo checkout or VCS tooling.

* **RUN\_ID rule (git-free):** RUN\_ID MUST be derived without git. Approved default: **timestamp-only** (UTC) with a deterministic suffix if needed for uniqueness (e.g., `YYYYMMDDThhmmssZ` plus a short monotonic counter). No commit hash is permitted as an input to RUN\_ID generation.

* **Traceability rule (governed artifacts):** If run traceability requires “what build did we test?”, the runbook MUST record build identity using governed build/identity artifacts and/or `/internal/version` identity fields (e.g., build\_commit/release\_id/emitter\_sha256), not `git rev-parse`. The “build\_commit” surfaced by the system is the canonical trace for the deployed build; git state is not a Live QA dependency.

* **Evidence rule:** The runbook MUST capture the identity values into governed evidence logs (under `audit/qa/...`) so reviewers can correlate the run with the deployed identity without requiring VCS access.

**Drain targets (doc delta intents)**

* **Doc:** PF19 — Canon Glow QA Guide, §3.6.2  
   **Delta intent:** Add an explicit example list of prohibited git operations in PO runbooks, and explicitly state the allowed boundary: “Codex planning prompt only.”

* **Doc:** PF27 — Canon Plan Templates, §2.1  
   **Delta intent:** Update the Live QA Plan template preflight section to require git-free RUN\_ID generation and to require build identity capture via governed identity artifacts (not VCS).

**Supersedes/conflicts**

* Supersedes any prior “convenience” patterns that used `git …` in run steps for run IDs or traceability.

---

## 2.5 — Step-log header schema must include `command` and `captured_env` (minimum reproducibility \+ machine-indexability)

**Why**

* Step logs are governed evidence. A step-log header that omits the literal executed command(s) and a rails/environment snapshot cannot be deterministically reviewed or machine-indexed, and makes closure contestable.

* Canon anchor: PF19 — Canon Glow QA Guide, §4.4.

**Decision / rule / clarification**

* **Hard rule:** Every QA step MUST produce a primary step log with a header that includes **at minimum**:

  * `command`: the literal command line(s) or explicit non-command action string executed for the step (not a human paraphrase).

  * `captured_env`: a structured snapshot of the rails/environment fields required by PF19 for reproducibility. (PF19 — Canon Glow QA Guide, §4.4)

* **Normalization rule:** `captured_env` must be the authoritative representation; any legacy string field like `rails` may remain as a human-readable summary, but MUST NOT replace the structured `captured_env`.

* **Operational determinism rule:** For steps that set rails pins (SAFE\_MODE, ALLOW\_NETWORK, APP\_ENV, TZ, LANG/LC\_ALL, PYTHONHASHSEED, etc.), the `captured_env` must include those rails pins as explicit key/value pairs.

* **Harness responsibility rule:** If a runbook uses a helper (e.g., a step recorder), it must accept/receive `command` and `captured_env` per step and write them into every step log header. Missing fields is a canonical nonconformance, not a caveat.

**Drain targets (doc delta intents)**

* **Doc:** PF19 — Canon Glow QA Guide, §4.4  
   **Delta intent:** Add a “minimum required header fields” checklist that explicitly includes `command` and `captured_env` and clarifies that these fields are required even when a step is TOOLING\_BLOCKED/FAIL.

* **Doc:** PF27 — Canon Plan Templates, §2.1  
   **Delta intent:** Require Live QA plans to explicitly state the step-log schema expectations and to require `command`/`captured_env` population for every step’s primary log.

**Supersedes/conflicts**

* Supersedes any step-log schemas that omit `command` or `captured_env`, or that treat them as optional.

---

## 2.6 — Token semantics in logs must separate “intent” from “claim” (`intended_tokens` vs `claimed_tokens`)

**Why**

* Token acceptance must be defensible. A single `tokens` field conflates what a step *intended* to satisfy with what the run *actually claims* was satisfied, creating canon ambiguity and weakening closure defensibility.

* Canon anchors: PF19 — Canon Glow QA Guide, §4.4; PF10 — HDE-Build Notes, §2.3.

**Decision / rule / clarification**

* **Hard rule:** Token-bearing steps MUST record both:

  * `intended_tokens`: tokens this step is designed to satisfy **if PASS** (always populated for token-relevant steps).

  * `claimed_tokens`: tokens actually satisfied by this run (MUST be populated **only when** `status=PASS`; MUST be an empty list for any non-PASS status). (PF19 — Canon Glow QA Guide, §4.4; PF10 — HDE-Build Notes, §2.3)

* **Legacy compatibility rule:** If a legacy `tokens` field is retained, it MUST be treated as an alias of `intended_tokens` only, and MUST NOT be interpreted as “claimed/satisfied.”

* **Acceptance defensibility rule:** Any acceptance/closure artifact (matrices, manifests, gate summaries) MUST treat **claimed tokens** as the basis for satisfaction. Intended tokens are routing/planning metadata and cannot be used as evidence of satisfaction.

* **Failure posture rule:** A step may still record `intended_tokens` on TOOLING\_BLOCKED/FAIL\_\*; but `claimed_tokens` MUST remain empty and MUST NOT be inferred or filled.

**Drain targets (doc delta intents)**

* **Doc:** PF19 — Canon Glow QA Guide, §4.4  
   **Delta intent:** Define token fields explicitly as intended-vs-claimed, and specify the population rule (claimed only on PASS).

* **Doc:** PF04 — HDE-Governance, §2.0.x (token semantics area; exact section to be selected by owner)  
   **Delta intent:** Add a short reinforcement that “token intent” and “token claim” are distinct evidence concepts for governed runs, and that claims must be backed by PASS evidence.

* **Doc:** PF27 — Canon Plan Templates, §2.1  
   **Delta intent:** Require the Live QA plan template to declare intended vs claimed token fields and require their correct population.

**Supersedes/conflicts**

* Supersedes any schema or interpretation that treats a single `tokens` list as a satisfaction claim.

---

## 2.7 — Live QA plans must not pin version-stale PF filenames; canon references must be stable and workspace-resolvable

**Why**

* Plans that hard-pin PF doc filenames/versions in “canon set” or preflight path checks create unnecessary TOOLING\_BLOCKED failures and undermine canon-fidelity (the plan can point at deprecated/nonexistent paths).

* Canon anchor: PF27 — Canon Plan Templates, §2.1.

**Decision / rule / clarification**

* **Hard rule:** Live QA plans MUST specify the governing canon set by **PF IDs \+ titles \+ sections** (e.g., “PF19 — Canon Glow QA Guide, §X.Y”), not by versioned filenames.

* **Preflight rule:** Any preflight “required PF doc paths” check MUST use a **stable-pointer approach** that is resilient to filename/version updates in the workspace.

  * Acceptable mechanisms:

## **2.8 — EPIC022 token registry single-home and “no unregistered tokens” rule**

### **Why**

EPIC022 closure artifacts/plans reference tokens, and PF‑Canon explicitly treats “token presence in artifacts” as meaningful. Closure cannot be canon-defensible if the token spellings used in step logs / manifests are not registered.

r2 Epic Closure Analysis HDE-E…

Also, PF‑Canon build gating explicitly treats **token naming disputes/placeholders** and **unregistered tokens** as blockers at approval/acceptance time.

PF04-Canon-HDE-Governance-v1.7.7

### **Decision / rule / clarification**

1. **Single home rule (firm):**  
   **PF04 Governance Token Registry is the only authority** for whether a token exists / is claimable. Any other document listing tokens is **advisory** until those tokens are present in PF04.  
    PF04-Canon-HDE-Governance-v1.7.7  
2. **No unregistered tokens rule (firm):**  
   If an EPIC022 artifact references a token that is not registered, that artifact is treated as **TOOLING\_BLOCKED evidence** and **cannot be used to claim acceptance**.  
    r2 Epic Closure Analysis HDE-E…  
3. **EPIC022 scope rule (firm):**  
   The EPIC022 token rosters enumerated for the epic (baseline \+ D-goals) must be reconciled against PF04 before closure can be claimed; **no alternate token namespaces** are permitted as substitutes.  
    r2 Epic Closure Analysis HDE-E…

### **Drain targets**

* **PF20 — HDE Phased Epics, §2.7.5**: reconcile the EPIC022 baseline \+ D-goal token rosters against PF04; remove placeholders and resolve spelling conflicts.  
   r2 Epic Closure Analysis HDE-E…  
* **PF04 — HDE Governance, §9.7.10**: add any missing EPIC022 tokens (or explicitly deprecate them in PF20 if they are not meant to exist).  
   r2 Epic Closure Analysis HDE-E…

### **Supersedes/conflicts**

* Supersedes any EPIC022 plan guidance that treats a non-PF04 token spelling as acceptable “for now.”  
   PF04-Canon-HDE-Governance-v1.7.7

---

## **2.9 — Tokens in step logs are claims (no `_OK` claims on non‑PASS)**

### **Why**

Audit evidence shows a step log marked `FAIL_TOOLING` still lists `_OK` tokens—canon treats this as an invalid claim surface and a closure blocker.

r2 Epic Closure Analysis HDE-E…

### **Decision / rule / clarification**

1. **Hard rule:** Step-log token lists are **claims**.  
2. **Therefore:** If `status != PASS`, then:  
   * `tokens_claimed` (or equivalent token list field) **must be empty**.  
   * Any tokens that were “intended” must be expressed only as non-claim narrative (see Addendum 3.4).  
      r2 Epic Closure Analysis HDE-E…  
3. **Enforcement rule:** Any tool emitting step logs must enforce:  
   * `PASS => may claim *_OK tokens`  
   * `FAIL_* / TOOLING_BLOCKED / N.A. => must not claim *_OK tokens`  
      r2 Epic Closure Analysis HDE-E…  
4. **Non-claim escape hatch (firm, allowed):**  
   EPIC022 step logs may include a **non-claim** field or section (e.g., `intended_tokens:`) that is explicitly non-normative and **ignored for acceptance**.  
    r2 Epic Closure Analysis HDE-E…

### **Drain targets**

* **PF20 — HDE Phased Epics, §2.7.7.2**: explicitly state “tokens listed in step logs are claims” and define the canonical non-claim escape hatch for intended tokens.  
   r2 Epic Closure Analysis HDE-E…  
* **PF19 — Glow QA Guide, §4.4**: align manifest/log claim surface rules with the above (no `_OK` token claims on non-PASS).  
   r2 Epic Closure Analysis HDE-E…  
* **PF09 — Build Checklist, §4.4**: prohibit `_OK` token claims on failed/blocked checks in any EPIC022 QA closure emission tooling.  
   r2 Epic Closure Analysis HDE-E…

---

## **2.10 — QA step-log manifest validity is a closure gate (schema \+ run grouping \+ uniqueness)**

### **Why**

Repo reality shows `audit/qa/hde-epic022/qa_step_logs_manifest.json` has duplicates and lacks `run_id` grouping, violating canonical manifest semantics and blocking closure.

r2 Epic Closure Analysis HDE-E…

### **Decision / rule / clarification**

1. **Canonical structure rule:** The manifest must be organized by `run_id` (or equivalent run grouping) and must be consumable as a closure artifact.  
    r2 Epic Closure Analysis HDE-E…  
2. **Uniqueness rule:** Within a given run, the same `check_id` must not appear more than once. Duplicates invalidate the run for closure consumption.  
    r2 Epic Closure Analysis HDE-E…  
3. **Status \+ token coherence rule:** Non‑PASS steps:  
   * may be recorded as FAIL/FAIL\_TOOLING/TOOLING\_BLOCKED/N.A. as applicable,  
   * but must not claim `_OK` tokens (see Addendum 3).  
      r2 Epic Closure Analysis HDE-E…  
4. **Z1 clarification (firm):** EPIC022 Z1 is **optional/N.A. until defined**; if absent it must be explicitly recorded as `N.A.` (not “missing required”).  
    r2 Epic Closure Analysis HDE-E…

### **Drain targets**

* **PF09 — Build Checklist, §4.4**: update EPIC022 checklist language so “manifest validity” is explicitly required before marking closure steps as complete.  
   r2 Epic Closure Analysis HDE-E…  
* **PF19 — Glow QA Guide, §4.4**: tighten the “duplicates \+ no run grouping \= invalid” language into an explicit consumability rule for closure.  
   r2 Epic Closure Analysis HDE-E…

---

## **2.11 — Evidence index ↔ mirror ↔ path-proof parity is mandatory for governed EPIC022 artifacts**

### **Why**

Audit evidence indicates `docs/evidence/INDEX.json` lists EPIC022 acceptance artifacts (including the close-pack and QA manifest), but mirror records and/or required `.path_proof.txt` transcripts are missing—canon requires strict parity.

r2 Epic Closure Analysis HDE-E…

PF12 explicitly requires 1:1 index↔mirror parity and co-located path-proofs, with same-PR update discipline.

PF12-Canon-HDE-Schemas-and-Arti…

### **Decision / rule / clarification**

1. **Parity is non-negotiable for governed artifacts:**  
   If an EPIC022 artifact is listed in `docs/evidence/INDEX.json`, then it must have:  
   * a corresponding mirror record in `artifacts/evidence_index.jsonl`, and  
   * a valid `proof_anchor` pointing to the matching co-located `.path_proof.txt` transcript.  
      PF12-Canon-HDE-Schemas-and-Arti…  
2. **Same-PR rule (firm):** Any change to a governed artifact must update:  
   * the artifact,  
   * its sibling `<artifact>.path_proof.txt`,  
   * the human index,  
   * the machine mirror,  
     all in the same change-set.  
      v5 Live QA Plan HDE-EPIC022  
3. **EPIC022 implication:** Once Addendum 1 is applied, the EPIC022 close-pack artifacts at:  
   * `audit/qa/hde-epic022/close_pack/close_report.md`  
   * `audit/qa/hde-epic022/close_pack/close_manifest.json`  
     are governed acceptance artifacts and must meet parity rules if indexed.  
      r2 Epic Closure Analysis HDE-E…

### **Drain targets**

* **PF12 — Schemas & Artifacts, §8.17.10**: incorporate EPIC022-specific parity expectations for the audit/qa acceptance artifacts if they’re registered there.  
   r2 Epic Closure Analysis HDE-E…  
* **PF04 — HDE Governance, §9.7.9**: ensure governance-level parity requirements explicitly cover EPIC022 close-pack and QA manifest artifacts once registered.  
   r2 Epic Closure Analysis HDE-E…

---

## **2.12 — `/internal/version` interim auth posture is canon (drain conflicts)**

### **Why**

Canon now states interim auth posture as **operator-network-only**, with **no application-layer request auth enforced**, and optional future auth gating. This removes auth ambiguity as a closure blocker, but conflicts with older “not canonized” language that still appears elsewhere.

r2 Epic Closure Analysis HDE-E…

### **Decision / rule / clarification**

1. **Correct:** Interim posture is canon:  
   * `/internal/version` is constrained by **operator-network-only**, not by request auth.  
   * Runbooks/tests must not require an auth header.  
   * Future auth gating (if desired) is a new epic/ADR and must be explicitly scoped.  
      r2 Epic Closure Analysis HDE-E…  
2. **Incorrect:** Any checklist/template language that states auth posture is “not yet canonized” as a blocker for EPIC022.

### **Drain targets**

* **PF20 — HDE Phased Epics, §2.7.8.4**: align tracked-issue/auth posture language to match the now-canon interim posture.  
   r2 Epic Closure Analysis HDE-E…  
* **PF09 — Build Checklist (front matter)**: remove/replace “auth not canonized” language where it conflicts with PF04.  
   r2 Epic Closure Analysis HDE-E…

---

If you want these written in *exactly* the same markdown/heading conventions as existing PF10 addenda in your repo (so you can paste them in verbatim), I can mirror that structure—but the decisions above are already finalized and internally consistent with the cited canon \+ audit evidence.

1. A canonical PF index/manifest file (if present in the repo) used to locate the current file for each PF ID, or

   2. A pattern-based resolution (e.g., locate `docs/pfcanon/PF19-*.md`), with explicit logging of what was matched.

* **Failure semantics rule:** If multiple candidate files match a PF ID pattern, preflight MUST record them and require the operator to select one explicitly (or use the canonical manifest if present). If none match, preflight must fail with a clear “missing PF doc” error that lists the expected PF IDs, not stale filenames.

* **No silent drift:** If a plan must reference a specific PF section whose numbering differs across versions, the plan must cite the PF section textually (heading name) in addition to the section number to reduce ambiguity.

**Drain targets (doc delta intents)**

* **Doc:** PF27 — Canon Plan Templates, §2.1  
   **Delta intent:** Add explicit rules prohibiting version-pinned PF filenames in Live QA plans and require stable-pointer preflight behavior (manifest-based or pattern-based).

* **Doc:** PF19 — Canon Glow QA Guide, §3.6.x (preflight/rails area; exact section to be selected by owner)  
   **Delta intent:** Clarify that “canon set declaration” is by PF ID/title/section and that filename resolution is an implementation detail handled by stable pointers.

**Supersedes/conflicts**

* Supersedes any template/runbook pattern that enumerates versioned PF filenames as required paths for execution.

## 2.13 — Standardize Live QA exit-code ↔ status mapping and token-claim reporting

**Why:** The review surfaced repeat confusion/implementation drift where non-zero return codes are treated as behavior failures and where token “pass” signaling can appear even when a step is not canonically PASS. This undermines closure defensibility and has been repeatedly escalated as a canon-level clarity gap.  
 **Decision / Rule (implementation-neutral):**

* Live QA harnesses and PO runbooks **MUST** classify outcomes using PF19 status semantics and **MUST NOT** collapse tooling-class failures into behavior failures.

* For Live QA steps, default mapping is:

  * Missing required PO inputs or required local files → `TOOLING_BLOCKED`

  * Tool/command invocation failure (including non-zero RC due to tooling) → `FAIL_TOOLING`

  * Behavioral failure (`FAIL_BEHAVIOR`) **only** when the surface is reachable and a valid response/output is captured, but it fails the canon-defined contract.

* Token claim reporting **MUST** be gated:

  * `claimed_tokens` (and any “tokens passed” messaging) **MUST** be empty unless `status == PASS`.

  * Any claim surface (step logs, manifests, summaries) **MUST NOT** emit `_OK` token claims for non-PASS outcomes.  
     **Drain targets (doc delta intents):**

* **PF19 — Canon Glow QA Guide, §3.5.11** → Add an explicit, harness-oriented mapping rule for exit-code/conditions → PF19 statuses for HTTP and ops/internal surfaces (tooling vs behavior).

* **PF19 — Canon Glow QA Guide, §4.4** → Make token-claim gating explicit for step logs and step summaries/manifests (PASS-only claims).

* **PF27 — Canon Plan Templates, §1.4** → Require that any “required PO input” has an explicit preflight branch that yields `TOOLING_BLOCKED` (not silent crash / not misclassified).  
   **Notes / conflicts (optional):**

* This addendum does not change what constitutes behavioral success; it only eliminates ambiguity in how Live QA records and communicates failure classes and token claims.

## 2.14 — Closure-scoped Live QA plans must not include placeholder non-PASS steps for required closure artifact families

**Why:** The review shows a closure-scoped plan can include an “expected failure” placeholder for close-pack, which creates a recurring approval deadlock and produces a runbook that cannot, by definition, generate closure evidence it claims to generate.  
 **Decision / Rule (implementation-neutral):**

* A Live QA plan that declares itself **closure-scoped** **MUST** include executable steps (with PASS predicates) for every closure-critical artifact family it claims to produce.

* Placeholder “expected non-PASS” steps are **disallowed** for closure-critical artifact families. If an execution entrypoint is unknown, the plan must either:

  * explicitly downgrade scope to “partial evidence run” and state closure cannot be achieved by this plan alone, **or**

  * include a canon-safe ADR path that resolves the missing entrypoint **before execution**, with a named decision owner and an evidence trigger.

* Any missing/unknown enablement for a closure-critical surface **MUST** be recorded as `TOOLING_BLOCKED` (never `FAIL_BEHAVIOR`) and must not be used to claim closure.  
   **Drain targets (doc delta intents):**

* **PF27 — Canon Plan Templates, §1.2** → Add a closure-scope integrity rule: closure plans cannot contain placeholder failure steps for required closure artifacts without an explicit scope downgrade or ADR gating.

* **PF20 — Canon HDE-Phased Epics, §2.7.3** → Add a short note tying closure artifact families to QA plan executability expectations (closure plans must be able to actually emit required families).

* **PF19 — Canon Glow QA Guide, §4.4** → Reinforce that claim surfaces cannot represent placeholder steps as closure-satisfying evidence (PASS-only claims).  
   **Notes / conflicts (optional):**

* This addendum preserves scope discipline: it does not invent new closure artifacts; it prevents plans from claiming closure readiness while structurally unable to complete closure steps.

\<eof\>