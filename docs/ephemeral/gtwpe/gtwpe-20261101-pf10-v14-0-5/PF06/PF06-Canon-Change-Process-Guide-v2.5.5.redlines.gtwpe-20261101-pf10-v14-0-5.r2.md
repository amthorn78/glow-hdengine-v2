# PF06 redlines — gtwpe-20261101-pf10-v14-0-5, package r2

Exact one-pass redlines for the Change Process Guide, prepared under TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1. Package r2 is complete: it supersedes package r1 and is applied on its own against the unchanged original.

## 1. Identity

| Field | Value |
| :---- | :---- |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-03 / package revision `r2` |
| Supersedes | Package `r1`, `PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.md` (commit `7e710d5c5a69617f896fb1db8bb07ad515491e0f`), applied in commit `ac5870fe2d8466fbad791c61f3b72011d9dfd37f`. RL-01, RL-02, RL-04, RL-05 and RL-06 are carried byte-identical; RL-03 is carried with its INSERT payload extended; RL-07 onward are new. |
| Preparation outcome | `READY` |
| Target (original baseline) | `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.5.md` at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`; in-document title `PF06-Canon-Change-Process-Guide`, version `v2.5.5`; git blob `e9f4d7d6146364f7c59ed360990d8c4ec633a59f`; SHA-256 `d046d7eeed6eee029b63392bc32cd67d9073f7c31ff9676a0448c11a2bce21c2`; 439442 bytes; 4684 lines |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56` |
| Decisions applied | GTWPE-D3 (context and scope); the Product Owner's CCR-5 ruling of 2026-11-02 and the answer in this session releasing H-06 for §3.5.1; Nathan's instruction of 2026-11-02 to fix the defects and inconsistencies this session noticed (the DOC_HYGIENE authorization). The proof log quotes each. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` (handoff pin `142feb35144d8795f927e0c78b665ace52279064`); task T-03; rows C-10, C-17, C-18, C-26; uncertain C-07; supporting C-20 |
| Proof log | `PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.r2.proof-log.md`, beside this file |
| Originating preparer | The TW-DRAIN-10 document session for T-03, a Claude Code session on `amthorn78/glow-hdengine-v2` (session `session_01Q789tyV3UxPrkptsceraud`), started by Nathan on 2026-11-02 |

## 2. Payload and location convention

* Every location is resolved against the unchanged original baseline above, never against text another redline produces.
* Each payload block is the exact text between its opening and closing fence lines. Every line in the block is one payload line, and each payload line is terminated by one LF. An empty line inside a block is a payload line holding only its LF. Trailing spaces are part of the payload (list-item lines of the target end with two spaces).
* `REPLACE`: the OLD block occurs exactly once in the original and consists of whole original lines with their LF; the REPLACE block takes its place.
* `INSERT`: the BEFORE block and the AFTER block are contiguous in the original (BEFORE ends exactly where AFTER begins) and occur exactly once each; the INSERT block goes into that gap; neither anchor is changed.
* No redline uses `FIND AND REPLACE` or `FIND_AND_REPLACE`. No header or document-control field is edited here; TW-APPLY-10 derives those.

## 3. Redlines

### RL-01 — REPLACE

* Source rows: C-18 (Epic close-run family), C-17 (2.8 decision 7, stated limits, drainage row §3.5.2/§3.5.2.1), C-10 (2.2 "Changes delivered": v2 source fields and input refusal), C-07 (2.2 precedence scope l.525)
* Change type: CANON_UPDATE (sentences 3 to 7 of the original paragraph) and NEW_CANON (new second paragraph)
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.8: 2026-11-01 amendment (B-3, B-4) l.1060, decision 7 l.1082, stated limit "An Epic close run needs its own explicit admission" l.1103, effects l.1109, drainage row l.1117 and l.1127; addendum 2.2 "Changes delivered" close-pack writer bullet l.556, R-1 l.533-538, R-2 l.540-545, "Relation to other canon" l.525; 2.8 2026-10-28 amendment (a) to (c) l.1059
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.1 Close-pack files**`
* Location: original line 3004, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
The generic producer of an Epic or CRD close pack is the v2 close-pack writer, `tools/qa/generate_epic_close_pack.py`, reading a `close_candidate_source.v2` candidate source; HDE Schemas and Artifacts owns the source schema, the manifest and the close-pack paths of record. For a CRD admitted in the canonical evidence updater's CRD admission, the same-run close evidence home is its post-verdict close-run family under `audit/qa/<change-dir>/close/`, where `<change-dir>` is the lower-case directory form of the CRD ID; only the canonical evidence updater writes it. That family is never listed in, and never reopens, the change's approved QA step-logs manifest or any `checks/` primary. No Epic close-run family is admitted; an Epic close run needs its own explicit admission.
````

REPLACE:

````
The generic producer of an Epic or CRD close pack is the v2 close-pack writer, `tools/qa/generate_epic_close_pack.py`, reading a `close_candidate_source.v2` candidate source; HDE Schemas and Artifacts owns the source schema, the manifest and the close-pack paths of record. For a CRD admitted in the canonical evidence updater's CRD admission, or an Epic admitted in its Epic close admission, the same-run close evidence home is the change's post-verdict close-run family under `audit/qa/<change-dir>/close/`, where `<change-dir>` is the change's lower-case QA directory: the lower-case CRD ID for a CRD (for example `hde-crd-0002`), or the Epic QA root directory of §0.5.1 for an Epic (for example `hde-epic041`). Only the canonical evidence updater writes it. That family is never listed in, and never reopens, the change's approved QA step-logs manifest or any `checks/` primary. An Epic close run needs its own explicit Product Owner admission; HDE-EPIC041 is the one Epic admitted. A later Epic's v2 close pack is written and checked by the same writer, but its close-run family and its Human Evidence Index rows need that Epic's own admission.

A v2 candidate source records what the writer needs from the change's planning documents, so the writer reads none of them: each planning document's identity and SHA-256 as a record text (`planning_records`, for the Specification, the implementation plan, the QA plan and the final QA report), the approved Specification's requirement IDs (`requirement_ids`), the QA plan's checks in plan order with the criteria each maps (`qa_checks`) and the final QA report's verdict (`qa_verdict`). It has no plan path and binds no planning document. No path under `docs/ephemeral/` or `docs/pfcanon/` is a causal input, pointer or key output of a v1 or v2 close pack, and the writer refuses one (`PLANNING_OR_CANON_INPUT_PROHIBITED`). A later-drain statement or a superseded artifact may name a planning document by a record text instead of a binding. A deferral's drain target names its register by PF title and gives one of its headings. The writer resolves PF titles and register headings at write time only, by title, against the PF-Canon files tracked at `HEAD`; its check mode reads no PF-Canon file, so a later canon version does not invalidate a committed close pack.
````

### RL-02 — REPLACE

* Source rows: C-18 (Epic tracked-issue ID form), C-17 (2.8 decision 4 tracked-issue mapping, stated limit on tracked issues)
* Change type: CANON_UPDATE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.8: 2026-11-01 amendment B-1 l.1060; stated limit "A tracked issue maps only through an ADR status" l.1099; l.1127 ("Epic tracked-issue ID form"); supporting addendum 2.9 B-1 table row l.1179
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.1 Close-pack files**`
* Location: original line 3011, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* a tracked-issue closeout mapping in the close report for any TI-\* items cited by the epic (example: TI-002): each TI item MUST map to either (a) PF09 subtask pointers (repo path plus section heading) that demonstrate closure, or (b) an ADR status line in the close report that records Deferred with drain targets so closure is unambiguous. The generic v2 close-pack writer supports only form (b): it renders each tracked issue as an ADR-status item in HDE Governance's literal `ADR status line:` field and refuses form (a), because no PF09 or PF30 file cites a TI ID. A close whose tracked issue is closed as satisfied through PF09 or PF30 pointers needs a later source-schema version.  
````

REPLACE:

````
* a tracked-issue closeout mapping in the close report for any TI-\* items cited by the epic (example: TI-002): each TI item MUST map to either (a) PF09 subtask pointers (repo path plus section heading) that demonstrate closure, or (b) an ADR status line in the close report that records Deferred with drain targets so closure is unambiguous. The generic v2 close-pack writer supports only form (b): it renders each tracked issue as an ADR-status item in HDE Governance's literal `ADR status line:` field and refuses form (a), because no PF09 or PF30 file cites a TI ID. A close whose tracked issue is closed as satisfied through PF09 or PF30 pointers needs a later source-schema version. A tracked-issue ID is `TI-NNN` or the Epic's own `ISSUE-EPIC<NNN>-TI-<nn>` (Plan Templates, “Tracked Issues”); the writer refuses an `ISSUE-EPIC` ID that names another Epic (`TRACKED_ISSUE_UNBOUND`).  
````

### RL-03 — INSERT

* Source rows: C-26 (2.15 R-1 and R-4, and, by context and scope under GTWPE-D3, R-2, R-3, R-5 and R-6; 2.15 "Relation to other canon")
* Change type: NEW_CANON
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15: "Relation to other canon" l.1666-1681, R-1 l.1704-1740, R-2 l.1741-1753, R-3 l.1755-1759, R-4 l.1761-1786, R-5 l.1787-1790, R-6 l.1792-1804; supporting addendum 2.16 R-3 l.1940-1948 (SYN-A and SYN-B stored and registered)
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.8 Live QA via harness (required for epic closeout)**`
* Location: the gap after original line 3182 and before original line 3183, inside the last heading of the path
* Expected occurrence of BEFORE and of AFTER in the original: 1 each; expected gap occurrence: 1

BEFORE:

````
Minimum requirements (all epics) are listed below.

````

AFTER:

````
Functional proof requirement (functional changes)  
````

INSERT:

````
Live compat test (all Epics). Every Epic's QA plan MUST include, and its QA run MUST execute, the live compat test below, whatever the Epic changed and whether or not its own surfaces are on a production path. Compat is the product, so a QA verdict that has not seen compat work live says nothing about the product. The requirement does not depend on a finding that the Epic touches or can affect a production surface.

* Live vendor compat. `hdctl showcompat --source vendor` runs under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, step-local, on synthetic birth data only, at the Epic's QA execution source, for at least two distinct pairs, each run as AB and as BA, with one pair run twice. It passes only when each output has the canonical result shape and the release identity of the source, AB and BA are byte-identical, the two runs are byte-identical, the Reader bytes stay `{id, band}` only, and the two pairs produce different results.  
* Deployed-service check. A check of the production HD Engine compares its `/internal/version` release identity with the release on `main`, and has the production Reader, for each Reader version, score the two synthetic stored people SYN-A and SYN-B in both orders. It passes only when each answer is eligible and bands-only and AB and BA are byte-identical. A mismatch between the deployed release and `main`, and a difference between the deployed bands and the CLI bands for the same birth data, are reported as findings with the QA result.  
* Synthetic stored people. The deployed Reader scores only people whose charts are stored in the production database, so SYN-A and SYN-B are kept there as permanent QA fixtures under fixed UUIDs: SYN-A `9cff60ae-6eb6-5618-aec5-8acaa4f290d2`, born 1990-01-01 at 12:00 in Amsterdam, Netherlands, and SYN-B `57f0c055-ff09-5fdb-aedb-def880437e6f`, born 1985-07-15 at 08:30 in London, United Kingdom. If either is missing when a QA run starts, the deployed-service check is `TOOLING_BLOCKED` until it is stored again.  
* Own live surfaces. When the Epic's own surfaces are on a production or vendor path, the plan also includes at least one open-rails step that exercises those surfaces live, as HDE Governance §3.4 requires.  
* Not sufficient. Closed-rails tests, fixture replay, mocks, static analysis, governed evidence artifacts, review approval and an unrun procedure do not satisfy the live compat test.  
* Other controls. Every other control of this section and of HDE Governance §3.4 still governs the test: authorization, request limits and synthetic data; redaction, secret scanning and the classification of failures; Ops evidence staying Ops evidence; and the nonclaims of a passing test.

Live-test line at every stage. Each of these records carries a line `Live test:` with one of `RAN` with its evidence references, `WAIVED` with the Product Owner's quoted words and date, or `MISSING`:

* the QA readiness record  
* the QA plan and its review  
* the QA task set  
* the QA execution result  
* the QA evidence review  
* the final QA report and RCA  
* the close mutation set result (§3.5.1)  
* the closure decision

`MISSING` blocks each stage as the table shows. No agent may override the block. Only the Product Owner may waive the live test or any part of it. A waiver is written and specific to the change, quotes the Product Owner's words with their date, and carries the content HDE Governance §3.4 requires of an exemption. An agent's finding that the Epic's surfaces are not on a live path, or that the test cannot run meaningfully, is a question for the Product Owner, put as a named decision no later than QA readiness; the QA plan is not approval-ready until the Product Owner answers. Silence, reviewer agreement, convenience, closed-rails success or a finding of non-applicability is not a waiver.

| Stage | Effect of `MISSING` |
| :---- | :---- |
| QA readiness | Not `READY_FOR_QA` |
| QA plan | Not approval-ready |
| QA plan review | Not approvable |
| QA evidence review | Not acceptable |
| Final QA report | No `PASS` verdict |
| Close mutation set | Not close-PR-ready |
| Closure decision | Not `CLOSE` |

A live test that cannot run, for want of credentials, target facts, an available vendor or an authorization, is `TOOLING_BLOCKED` under HDE Governance §3.4. The Epic waits. A blocked live test is never converted into a `PASS`, a waiver or a closure, and the Product Owner decides how to proceed.

Every prompt that produces one of these records, including the Change Flow and GCFPE prompts, applies this rule. An agent running a prompt that does not yet state the rule applies it from this section.

The name “Live QA”. A guide, plan, task set, evidence branch, report or verdict may use “Live QA” only if it covers or records the live compat test, or a recorded waiver of it. Any other QA is called “closed-rails QA” in its title, branch name and verdict line. A QA report without the live compat test says so in its first line, “No live test ran.”, and names the waiver or the missing test.

````

### RL-04 — REPLACE

* Source rows: C-26 (2.15 R-1 scope "whatever the Epic changed"; only the Product Owner may waive, as R-4 restates)
* Change type: CONSISTENCY
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15: R-1 "Scope" l.1706, R-2 "The rule" l.1743 as R-4 "Who may override" l.1784 restates it, "Relation to other canon" supersession l.1671-1676
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.8 Live QA via harness (required for epic closeout)**`
* Location: original line 3195, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* Exemption boundary: truly non-functional-only epics (docs, refactors with no behavior changes, schema-only updates with no runtime behavior changes) MAY omit functional proof, but the exemption MUST be explicitly justified and validated by the IG. This does not exempt an Epic within the mandatory production-functional vendor scope in §1.1.5A.
````

REPLACE:

````
* Exemption boundary: truly non-functional-only epics (docs, refactors with no behavior changes, schema-only updates with no runtime behavior changes) MAY omit functional proof, but the exemption MUST be explicitly justified and validated by the IG. This does not exempt an Epic within the mandatory production-functional vendor scope in §1.1.5A, and it never exempts an Epic from the live compat test above, which only the Product Owner may waive.
````

### RL-05 — REPLACE

* Source rows: C-26 (2.15 R-1: every Epic's QA plan includes the live compat test)
* Change type: CONSISTENCY
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15 R-1 "Scope" l.1706 and "What the test runs" l.1708
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.8 Live QA via harness (required for epic closeout)**`
* Location: original line 3200, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* closed-rails default posture (env pins), with the bounded open-rails live vendor step required for the scope in §1.1.5A  
````

REPLACE:

````
* closed-rails default posture (env pins), with the step-local open-rails steps of the live compat test above, and the bounded open-rails live vendor step required for the scope in §1.1.5A  
````

### RL-06 — REPLACE

* Source rows: C-17 (2.8 decision 4 SATISFIED rule; stated limit on qa_checks), C-07 (2.2 precedence scope l.525)
* Change type: CLARIFY
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.8: decision 4 SATISFIED bullet l.1073 ("records every check of the recorded QA plan"), stated limit l.1093 (the QA plan's checks are the source's qa_checks, and the writer reads no QA plan), 2026-10-28 amendment l.1059; addendum 2.2 "Relation to other canon" l.525
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.4 ADR block in the close-pack (all epics)**`
* Location: original line 3348, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Closure override in a v2 close pack. A v2 `SATISFIED` decision requires every check of the change's current QA plan to be recorded in the QA step-logs manifest in one of two ways: as `PASS`, or as `TOOLING_BLOCKED` where a closure-override gap in the ADR block names that check, once. A check recorded as `FAIL_BEHAVIOR`, `FAIL_TOOLING` or `PARKED`, and a planned check the manifest does not record, block `SATISFIED`. A `TOOLING_BLOCKED` check accepted under a closure override is never `PASS` evidence for a met acceptance criterion.
````

REPLACE:

````
Closure override in a v2 close pack. A v2 `SATISFIED` decision requires each of the change's QA plan checks, as recorded in the candidate source (`qa_checks`), to be recorded in the QA step-logs manifest in one of two ways: as `PASS`, or as `TOOLING_BLOCKED` where a closure-override gap in the ADR block names that check, once. A check recorded as `FAIL_BEHAVIOR`, `FAIL_TOOLING` or `PARKED`, and a planned check the manifest does not record, block `SATISFIED`. A `TOOLING_BLOCKED` check accepted under a closure override is never `PASS` evidence for a met acceptance criterion.
````

### RL-07 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.2 Policy and principles**`
* Location: original lines 402–403, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* audit/ops/\\/ for Ops execution evidence, or  
* audit/qa/\\/ when the evidence is part of QA execution.
````

REPLACE:

````
* audit/ops/\<epic-id\>/ for Ops execution evidence, or  
* audit/qa/\<epic-id\>/ when the evidence is part of QA execution.
````

### RL-08 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.4 4 Execution posture and flow (route-aware)**`
  * `### **0.4.1 Live QA discovery and RCA (execution requirements)**`
  * `#### **0.4.1.1 Mandatory D0 Discovery artifact**`
* Location: original line 544, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* The Discovery artifact is a governed, mechanical file under the epic’s QA root (audit/qa//). It is evidence that the session ran under known, documented conditions.  
````

REPLACE:

````
* The Discovery artifact is a governed, mechanical file under the epic’s QA root (audit/qa/\<epic-id\>/). It is evidence that the session ran under known, documented conditions.  
````

### RL-09 — REPLACE

* Source rows: O-3; C-17 (2.8 decision 4 and the stated limit on the QA RCA path)
* Change type: CONSISTENCY
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.8: decision 4 l.1078 ("the QA RCA, embedded or bound as audit/<prefix>_QA_RCA.md") and the stated limit l.1097 ("A bound QA RCA must be audit/<prefix>_QA_RCA.md, using the close report's own prefix (Change Process Guide §0.4.1.2; QA_RCA_UNBOUND)")
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.4 4 Execution posture and flow (route-aware)**`
  * `### **0.4.1 Live QA discovery and RCA (execution requirements)**`
  * `#### **0.4.1.2 Mandatory QA RCA & Doc Delta summary**`
* Location: original line 600, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
If the QA RCA & Doc Delta summary is maintained as a separate governed artifact, it MUST use the canonical filename `audit/EPIC-<NNN>_QA_RCA.md`. The epic close report MUST reference this artifact by path.
````

REPLACE:

````
If the QA RCA & Doc Delta summary is maintained as a separate governed artifact, it MUST use the canonical filename `audit/<prefix>_QA_RCA.md`, where `<prefix>` is the close report's own prefix: `audit/EPIC-<NNN>_QA_RCA.md` for an epic and `audit/HDE-CRD-<NNNN>_QA_RCA.md` for a CRD. The close report MUST reference this artifact by path.
````

### RL-10 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
* Location: original lines 677–678, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
  * audit/qa//remediation/moon\_loop/patch.diff (or equivalent)  
  * audit/qa//remediation/moon\_loop/changed\_files.txt (paths \+ sha256)  
````

REPLACE:

````
  * audit/qa/\<epic-id\>/remediation/moon\_loop/patch.diff (or equivalent)  
  * audit/qa/\<epic-id\>/remediation/moon\_loop/changed\_files.txt (paths \+ sha256)  
````

### RL-11 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
  * `### **0.5.1 Epic path normalization (close-pack \+ QA root)**`
* Location: original lines 963–964, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Epic number (\\)  
is the zero-padded 3-digit epic number (example: 022). When an epic ID is HDE-EPIC022, then \\ is 022\.
````

REPLACE:

````
Epic number (\<NNN\>)  
is the zero-padded 3-digit epic number (example: 022). When an epic ID is HDE-EPIC022, then \<NNN\> is 022\.
````

### RL-12 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
  * `### **0.5.1 Epic path normalization (close-pack \+ QA root)**`
* Location: original lines 967–970, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Epic close-pack artifacts MUST use:

* audit/EPIC-\\\_close\_report.md  
* audit/EPIC-\\\_MANIFEST.json
````

REPLACE:

````
Epic close-pack artifacts MUST use:

* audit/EPIC-\<NNN\>\_close\_report.md  
* audit/EPIC-\<NNN\>\_MANIFEST.json
````

### RL-13 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
  * `### **0.5.1 Epic path normalization (close-pack \+ QA root)**`
* Location: original lines 975–976, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* audit/EPIC-\\\_close\_report.md.path\_proof.txt  
* audit/EPIC-\\\_MANIFEST.json.path\_proof.txt
````

REPLACE:

````
* audit/EPIC-\<NNN\>\_close\_report.md.path\_proof.txt  
* audit/EPIC-\<NNN\>\_MANIFEST.json.path\_proof.txt
````

### RL-14 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
  * `### **0.5.1 Epic path normalization (close-pack \+ QA root)**`
* Location: original line 983, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
audit/EPIC-\\\_MANIFEST.json MUST include key\_outputs as a JSON object (map) where:
````

REPLACE:

````
audit/EPIC-\<NNN\>\_MANIFEST.json MUST include key\_outputs as a JSON object (map) where:
````

### RL-15 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
  * `### **0.5.1 Epic path normalization (close-pack \+ QA root)**`
* Location: original line 995, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* audit/qa/hde-epic\\/ (example: audit/qa/hde-epic022/)
````

REPLACE:

````
* audit/qa/hde-epic\<NNN\>/ (example: audit/qa/hde-epic022/)
````

### RL-16 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
  * `### **0.5.1 Epic path normalization (close-pack \+ QA root)**`
* Location: original line 997, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
When this guide uses audit/qa//, it means the epic QA root audit/qa/hde-epic\\/.
````

REPLACE:

````
When this guide uses audit/qa/\<epic-id\>/, it means the epic QA root audit/qa/hde-epic\<NNN\>/.
````

### RL-17 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
  * `### **0.5.1 Epic path normalization (close-pack \+ QA root)**`
* Location: original lines 1006–1007, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
   audit/docdeltas/hde-epic\\\_doc\_deltas.md  
   Where hde-epic\\ is the canonical lowercase epic QA slug (for example hde-epic022). This draft surface is the primary surface for doc-delta evidence binding when a doc-delta deliverable is claimed.  
````

REPLACE:

````
   audit/docdeltas/hde-epic\<NNN\>\_doc\_deltas.md  
   Where hde-epic\<NNN\> is the canonical lowercase epic QA slug (for example hde-epic022). This draft surface is the primary surface for doc-delta evidence binding when a doc-delta deliverable is claimed.  
````

### RL-18 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.5 Routing and evidence discipline**`
  * `### **0.5.1 Epic path normalization (close-pack \+ QA root)**`
* Location: original line 1010, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
   audit/qa/hde-epic\\/00\_meta/doc\_deltas.md
````

REPLACE:

````
   audit/qa/hde-epic\<NNN\>/00\_meta/doc\_deltas.md
````

### RL-19 — REPLACE

* Source rows: O-1; C-26 (2.15 R-1 scope and "Relation to other canon", by context and scope under GTWPE-D3)
* Change type: CONSISTENCY
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15: R-1 "Scope" l.1706 ("whatever the Epic changed"), R-1 "Where an Epic's own surfaces are live" l.1726, R-2 l.1743, "Relation to other canon" l.1671-1677; GTWPE-D3 (context and scope)
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.2 Rails and environments (closed-rails vs open-rails QA)**`
* Location: original line 1106, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Open-rails testing may be included in implementation or QA planning when live operational information is necessary and the work is otherwise in scope. The plan MUST bound the task, identify PO authorization, preserve secret safety, state what may be recorded, state what must not be recorded, and avoid treating vendor smoke success as broader conformance than it proves.
````

REPLACE:

````
Open-rails testing may be included in implementation or QA planning when live operational information is necessary and the work is otherwise in scope. The plan MUST bound the task, identify PO authorization, preserve secret safety, state what may be recorded, state what must not be recorded, and avoid treating vendor smoke success as broader conformance than it proves. Separately, every Epic's QA plan MUST include the live compat test in §3.5.2.8, whatever the Epic changed.
````

### RL-20 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.3 Prod behavior vs Codespaces artifact sink (Live QA)**`
* Location: original line 1147, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* receive and store artifacts (logs, JSON, headers, transcripts) under audit/qa//  
````

REPLACE:

````
* receive and store artifacts (logs, JSON, headers, transcripts) under audit/qa/\<epic-id\>/  
````

### RL-21 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.3 Prod behavior vs Codespaces artifact sink (Live QA)**`
* Location: original line 1164, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* an artifact capture & analysis phase (where artifacts from that run are copied or uploaded into the Codespace under audit/qa// and analyzed offline)
````

REPLACE:

````
* an artifact capture & analysis phase (where artifacts from that run are copied or uploaded into the Codespace under audit/qa/\<epic-id\>/ and analyzed offline)
````

### RL-22 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.3 Prod behavior vs Codespaces artifact sink (Live QA)**`
* Location: original line 1170, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
When a token is about prod behavior, its satisfaction MUST be tied to a prod-facing behavior run as described above, with artifacts captured under audit/qa//.
````

REPLACE:

````
When a token is about prod behavior, its satisfaction MUST be tied to a prod-facing behavior run as described above, with artifacts captured under audit/qa/\<epic-id\>/.
````

### RL-23 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.4 PO Live QA vendor-first scope**`
* Location: original line 1197, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
  * the rail-opening is documented (env vars set, commands logged, and artifacts captured under audit/qa//logs/)
````

REPLACE:

````
  * the rail-opening is documented (env vars set, commands logged, and artifacts captured under audit/qa/\<epic-id\>/logs/)
````

### RL-24 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.7 Mechanical evidence (Live QA)**`
* Location: original line 1251, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* audit/qa//checks/\\/primary.log
````

REPLACE:

````
* audit/qa/\<epic-id\>/checks/\<check\_id\>/primary.log
````

### RL-25 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.7 Mechanical evidence (Live QA)**`
* Location: original line 1255, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* audit/qa//qa\_step\_logs\_manifest.json
````

REPLACE:

````
* audit/qa/\<epic-id\>/qa\_step\_logs\_manifest.json
````

### RL-26 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.7 Mechanical evidence (Live QA)**`
* Location: original line 1263, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* audit/qa//qa\_step\_logs\_manifest.json.path\_proof.txt
````

REPLACE:

````
* audit/qa/\<epic-id\>/qa\_step\_logs\_manifest.json.path\_proof.txt
````

### RL-27 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **0\. Front Matter**`
  * `## **0.6 Discipline**`
  * `### **0.6.7 Mechanical evidence (Live QA)**`
* Location: original line 1283, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Each QA step MUST explicitly name the expected artifacts (paths and filenames) it will produce under the canonical QA root audit/qa//. Naming the per-check primary.log satisfies this requirement by default.
````

REPLACE:

````
Each QA step MUST explicitly name the expected artifacts (paths and filenames) it will produce under the canonical QA root audit/qa/\<epic-id\>/. Naming the per-check primary.log satisfies this requirement by default.
````

### RL-28 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.3 “Prod via Codespaces” requirements (Epic Specification)**`
* Location: original line 1572, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Example: Step 0: curl the production /internal/version endpoint from Codespaces and store the output under audit/qa/\\/logs/ before running deeper QA.
````

REPLACE:

````
Example: Step 0: curl the production /internal/version endpoint from Codespaces and store the output under audit/qa/\<epic-id\>/logs/ before running deeper QA.
````

### RL-29 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.3 “Prod via Codespaces” requirements (Epic Specification)**`
* Location: original line 1579, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Live QA plans MUST NOT use /internal/version to satisfy any behavior D-goals (for example compat math, narratives, vendor ingest, admin bundle). Those goals require separate behavior steps that exercise prod-facing behavior surfaces and produce their own artifacts under audit/qa/\\/\\.
````

REPLACE:

````
Live QA plans MUST NOT use /internal/version to satisfy any behavior D-goals (for example compat math, narratives, vendor ingest, admin bundle). Those goals require separate behavior steps that exercise prod-facing behavior surfaces and produce their own artifacts under audit/qa/\<epic-id\>/\<SUBPATH\>.
````

### RL-30 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.3 “Prod via Codespaces” requirements (Epic Specification)**`
* Location: original line 1585, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* The current Epic Specification acceptance criteria and evidence requirements explicitly declare this posture by title (for example: “Live QA will exercise vendor-backed behavior in prod via Codespaces → Railway, with artifacts under audit/qa/\\/\\”).  
````

REPLACE:

````
* The current Epic Specification acceptance criteria and evidence requirements explicitly declare this posture by title (for example: “Live QA will exercise vendor-backed behavior in prod via Codespaces → Railway, with artifacts under audit/qa/\<epic-id\>/\<SUBPATH\>”).  
````

### RL-31 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.3 “Prod via Codespaces” requirements (Epic Specification)**`
* Location: original lines 1587–1588, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
  * uses or references the prod identity handshake artifact (for example the /internal/version capture under audit/qa/\\/logs/) to anchor which engine instance is under test  
  * demonstrates a vendor-backed end-to-end flow (for example vendor-backed resolve or compat) executed against the production HD Engine service, with its own mechanical artifacts captured under audit/qa/\\/\\ as required by §1.1.4–§1.1.6.
````

REPLACE:

````
  * uses or references the prod identity handshake artifact (for example the /internal/version capture under audit/qa/\<epic-id\>/logs/) to anchor which engine instance is under test  
  * demonstrates a vendor-backed end-to-end flow (for example vendor-backed resolve or compat) executed against the production HD Engine service, with its own mechanical artifacts captured under audit/qa/\<epic-id\>/\<SUBPATH\> as required by §1.1.4–§1.1.6.
````

### RL-32 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.4 Live QA mechanical evidence expectations**`
* Location: original line 1602, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* a pointer to the QA Plan (titles-only reference) and the epic QA root (audit/qa/\\/)
````

REPLACE:

````
* a pointer to the QA Plan (titles-only reference) and the epic QA root (audit/qa/\<epic-id\>/)
````

### RL-33 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.4 Live QA mechanical evidence expectations**`
* Location: original line 1608, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* Deliverables: exact file artifacts to be produced or updated, with stable step-scoped paths under audit/qa/\\/checks/\\/.  
````

REPLACE:

````
* Deliverables: exact file artifacts to be produced or updated, with stable step-scoped paths under audit/qa/\<epic-id\>/checks/\<check\_id\>/.  
````

### RL-34 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.4 Live QA mechanical evidence expectations**`
* Location: original line 1765, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
No manual-result placeholders (hard rule). Live QA plans and runbooks MUST NOT include instructions that require the operator to manually fill results (for example “Result: (fill PASS/FAIL/SKIPPED)” or equivalent). Step outcomes must be determined mechanically from the step’s commands and the resulting artifacts under audit/qa/\\/\\.
````

REPLACE:

````
No manual-result placeholders (hard rule). Live QA plans and runbooks MUST NOT include instructions that require the operator to manually fill results (for example “Result: (fill PASS/FAIL/SKIPPED)” or equivalent). Step outcomes must be determined mechanically from the step’s commands and the resulting artifacts under audit/qa/\<epic-id\>/\<SUBPATH\>.
````

### RL-35 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.5 Live QA behavior vs artifact pattern**`
* Location: original line 1837, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Artifact capture \+ analysis phase: Capture governed evidence artifacts under audit/qa/\\/\\ (and related required closeout artifacts). Perform analysis offline (e.g., in Codespace), producing the required summaries, diffs, and verification notes as governed artifacts.
````

REPLACE:

````
Artifact capture \+ analysis phase: Capture governed evidence artifacts under audit/qa/\<epic-id\>/\<SUBPATH\> (and related required closeout artifacts). Perform analysis offline (e.g., in Codespace), producing the required summaries, diffs, and verification notes as governed artifacts.
````

### RL-36 — REPLACE

* Source rows: O-1; C-26 (2.15 R-1 scope and "Relation to other canon", by context and scope under GTWPE-D3)
* Change type: CONSISTENCY
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15: R-1 "Scope" l.1706 ("whatever the Epic changed"), R-1 "Where an Epic's own surfaces are live" l.1726, R-2 l.1743, "Relation to other canon" l.1671-1677; GTWPE-D3 (context and scope)
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.5 Live QA behavior vs artifact pattern**`
  * `#### **1.1.5A Production-affecting open-rails Live QA requirement**`
* Location: original line 1843, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
For any epic that can affect real production functionality, QA readiness and closeout review MUST account for at least one bounded open-rails Live QA step that proves relevant production-facing behavior in the deployed or PO-approved live target, unless an explicit exemption is approved and recorded.
````

REPLACE:

````
For any epic that can affect real production functionality, QA readiness and closeout review MUST account for at least one bounded open-rails Live QA step that proves relevant production-facing behavior in the deployed or PO-approved live target, unless an explicit exemption is approved and recorded. This section governs the open-rails proof of the Epic's own production-facing surfaces. It does not govern the live compat test in §3.5.2.8, which every Epic's QA runs whatever the Epic changed: no finding or exemption under this section applies to that test, and only the Product Owner may waive it.
````

### RL-37 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.6 PO Live QA vendor-first scope**`
* Location: original line 1913, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* omit mechanical vendor evidence expectations for PO-run vendor steps under audit/qa/\\/\\
````

REPLACE:

````
* omit mechanical vendor evidence expectations for PO-run vendor steps under audit/qa/\<epic-id\>/\<SUBPATH\>
````

### RL-38 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**`
  * `## **1.1 Epic-lane workflow at a glance**`
  * `### **1.1.10 PLAN submission preflight (mechanical gate: exact sources \+ evidence paths)**`
  * `#### **1.1.10.4 Canonical evidence-path binding validation (acceptance integrity)**`
* Location: original line 2121, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* The EPIC-local variant under audit/qa/\\/\\/evidence\_index\_snapshot.json is non-authoritative; it MAY exist for compatibility or run-local context, but it MUST NOT be treated as canonical closure evidence.  
````

REPLACE:

````
* The EPIC-local variant under audit/qa/\<epic-id\>/\<SUBPATH\>/evidence\_index\_snapshot.json is non-authoritative; it MAY exist for compatibility or run-local context, but it MUST NOT be treated as canonical closure evidence.  
````

### RL-39 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.1 Machine header**`
* Location: original lines 2883–2884, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
"audit/EPIC-\\\_close\_report.md",  
"audit/EPIC-\\\_MANIFEST.json"  
````

REPLACE:

````
"audit/EPIC-\<NNN\>\_close\_report.md",  
"audit/EPIC-\<NNN\>\_MANIFEST.json"  
````

### RL-40 — REPLACE

* Source rows: C-07/C-09 (2.2 R-3 first bullet) under CCR-5 alternative (A); H-06 released
* Change type: CONSISTENCY (CCR-5 alternative (A), Product Owner ruling)
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.2 R-3 first bullet l.549 ("The close-pack writer writes a close pack only at the close stage, at the end of a full work-unit cycle, after the authorized QA verdict and the closure decision exist"); CCR-5 and its alternative (A), addendum 2.5 l.856 (supporting). Product Owner ruling, 2026-11-02, recorded in the T-07 preparation proof log: "close pack should go after the decision to close is confirmed". Product Owner answer in this session, 2026-11-02, to whether T-03's corrected package drains (A) into §3.5.1: "Yes, drain (A) into §3.5.1 (Recommended)". Wording aligned with Plan Templates §3B as revised under the same ruling (T-07 RL-16 to RL-18).
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.1 Requirement**`
* Location: original lines 2954–2960, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Close-mutation-set stage. The close mutation set is produced by its own stage of the change flow, the close-mutation-set stage, which serves every Epic and CRD. It sits between the final QA Report and the closure decision.

* Entries. The stage starts from the final QA Report with verdict `PASS`, or from a closure decision of `DO_NOT_CLOSE` whose return work is the close mutation set because it is missing, incomplete or defective.  
* Exit. The stage exits to the closure decision after the Product Owner merges the close PR.  
* What it owns. The stage owns the close mutation set: the close pack, its doc-delta and drain-target ledgers, the same-run close evidence, and their Human Evidence Index and Machine Mirror registration. It also owns any repair of the close tooling that the close needs.  
* What it never does. The stage never reopens implementation, QA or the closure decision.  
* Authority and actor. The Product Owner's invocation of the stage for a change authorizes that change's close mutation set and any close-tooling repair it needs, and is the Proceed for both. The stage runs as a standalone top-level session that the Product Owner starts with the stage prompt and the change ID; it needs no handoff to start and resolves its inputs from the change's records. The closure authority judges its result at the closure decision, and the Product Owner alone merges.  
````

REPLACE:

````
Close-mutation-set stage. The close mutation set is produced by its own stage of the change flow, the close-mutation-set stage, which serves every Epic and CRD. It follows the closure decision: the close mutation set, the close pack included, is written only after the authorized QA verdict and a closure decision of `CLOSE` exist.

* Entry. The stage starts from a closure decision of `CLOSE` for the change. The close mutation set, the close pack included, is written only after that decision confirms the close.  
* Exit. The stage ends when the Product Owner merges the close PR.  
* What it owns. The stage owns the close mutation set: the close pack, its doc-delta and drain-target ledgers, the same-run close evidence, and their Human Evidence Index and Machine Mirror registration. It also owns any repair of the close tooling that the close needs.  
* What it never does. The stage never reopens implementation, QA or the closure decision.  
* Authority and actor. The Product Owner's invocation of the stage for a change authorizes that change's close mutation set and any close-tooling repair it needs, and is the Proceed for both. The stage runs as a standalone top-level session that the Product Owner starts with the stage prompt and the change ID; it needs no handoff to start and resolves its inputs from the change's records. The stage starts only after the closure authority has decided to close the change, and it does not revisit that decision; the Product Owner alone merges.  
````

### RL-41 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.1 Close-pack files**`
* Location: original lines 2992–2995, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
The close PR MUST include the change's close-pack (canonical filenames). For an epic:

* audit/EPIC-\\\_close\_report.md  
* audit/EPIC-\\\_MANIFEST.json
````

REPLACE:

````
The close PR MUST include the change's close-pack (canonical filenames). For an epic:

* audit/EPIC-\<NNN\>\_close\_report.md  
* audit/EPIC-\<NNN\>\_MANIFEST.json
````

### RL-42 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.1 Close-pack files**`
* Location: original line 2997, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Where \\ is the zero-padded 3-digit epic number (see §0.5.1).
````

REPLACE:

````
Where \<NNN\> is the zero-padded 3-digit epic number (see §0.5.1).
````

### RL-43 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.8 Live QA via harness (required for epic closeout)**`
* Location: original line 3201, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* expected evidence under audit/qa/\\/checks/\\/ (stable check-scoped evidence; no per-run nesting, no run-id directories, and no operator-selected fresh-run root)
````

REPLACE:

````
* expected evidence under audit/qa/\<epic-id\>/checks/\<check\_id\>/ (stable check-scoped evidence; no per-run nesting, no run-id directories, and no operator-selected fresh-run root)
````

### RL-44 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.8 Live QA via harness (required for epic closeout)**`
* Location: original line 3212, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
Execution environment and venue materiality. Every governed Live QA execution MUST use an environment permitted by the governing Live QA Plan or applicable QA authority, execute the required governed harness, and produce governed, reproducible evidence under audit/qa/\\/checks/\\/ using the stable check-scoped layout.
````

REPLACE:

````
Execution environment and venue materiality. Every governed Live QA execution MUST use an environment permitted by the governing Live QA Plan or applicable QA authority, execute the required governed harness, and produce governed, reproducible evidence under audit/qa/\<epic-id\>/checks/\<check\_id\>/ using the stable check-scoped layout.
````

### RL-45 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.8 Live QA via harness (required for epic closeout)**`
* Location: original line 3242, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* Live QA step artifacts under audit/qa/\\/checks/\\  
````

REPLACE:

````
* Live QA step artifacts under audit/qa/\<epic-id\>/checks/\<check\_id\>  
````

### RL-46 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.2 Close PR contents**`
  * `#### **3.5.2.8 Live QA via harness (required for epic closeout)**`
* Location: original line 3257, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
CI tests MUST NOT be treated as a source of governed evidence and MUST NOT require committing audit/qa/\\/\\ outputs to the repo.
````

REPLACE:

````
CI tests MUST NOT be treated as a source of governed evidence and MUST NOT require committing audit/qa/\<epic-id\>/\<SUBPATH\> outputs to the repo.
````

### RL-47 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**`
  * `## **3.5 Close Gate (route-aware)**`
  * `### **3.5.4 ADR block in the close-pack (all epics)**`
* Location: original line 3352, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* audit/EPIC-\\\_close\_report.md for an epic  
````

REPLACE:

````
* audit/EPIC-\<NNN\>\_close\_report.md for an epic  
````

### RL-48 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **4\) PR & COMMIT PLAN (PR-first via the executing agent; Lead Dev gates)**`
  * `## **4.5 PR template — evidence-only QA**`
  * `### **Exact-source QA evidence (check what applies)**`
  * `#### **Close-pack (when this mutation set carries epic closeout)**`
* Location: original line 3755, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
* Close-pack baseline present — audit/EPIC-\\\_close\_report.md; audit/EPIC-\\\_MANIFEST.json
````

REPLACE:

````
* Close-pack baseline present — audit/EPIC-\<NNN\>\_close\_report.md; audit/EPIC-\<NNN\>\_MANIFEST.json
````

### RL-49 — REPLACE

* Source rows: O-4 (damaged placeholder in a path pattern; Nathan's instruction of 2026-11-02)
* Change type: DOC_HYGIENE
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: Nathan, 2026-11-02: "fix the defects and inconsistencies you noticed" (authorization for this hygiene). The restored variable names are attested by the target itself: `audit/qa/<epic-id>/<SUBPATH>` (line 1906), `audit/qa/<epic-id>/logs/` (line 1415), `audit/EPIC-<NNN>_QA_RCA.md` (line 600), the epic `EPIC-NNN` form (line 2999), the epic QA root example `audit/qa/hde-epic022/` (line 995) and the `check_id` field (line 1257). Each `\\` is the remnant of an escaped `\<VAR\>` whose name was stripped; each repair restores `\<VAR\>` in the line's own escaping style and changes nothing else.
* Section path (exact original heading lines, outermost first):
  * `# **6\) PHASE EXIT DISCIPLINE (ALCHEMICAL PHASES)**`
  * `## **6.3 Close-out epic required**`
* Location: original line 4212, inside the last heading of the path
* Expected occurrence of OLD in the original: 1

OLD:

````
  * lives under governed roots, including audit/EPIC-\\\_close\_report.md and audit/EPIC-\\\_MANIFEST.json;  
````

REPLACE:

````
  * lives under governed roots, including audit/EPIC-\<NNN\>\_close\_report.md and audit/EPIC-\<NNN\>\_MANIFEST.json;  
````

END OF REDLINES
