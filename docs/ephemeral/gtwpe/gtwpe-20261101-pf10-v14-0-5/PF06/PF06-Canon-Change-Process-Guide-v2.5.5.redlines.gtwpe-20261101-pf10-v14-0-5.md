# PF06 redlines — gtwpe-20261101-pf10-v14-0-5

Exact one-pass redlines for the Change Process Guide, prepared under TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1.

## 1. Identity

| Field | Value |
| :---- | :---- |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-03 / package revision `r1` |
| Preparation outcome | `READY` |
| Target (original baseline) | `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.5.md` at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`; in-document title `PF06-Canon-Change-Process-Guide`, version `v2.5.5`; git blob `e9f4d7d6146364f7c59ed360990d8c4ec633a59f`; SHA-256 `d046d7eeed6eee029b63392bc32cd67d9073f7c31ff9676a0448c11a2bce21c2`; 439442 bytes; 4684 lines |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-03; rows C-10, C-17, C-18, C-26; uncertain C-07; supporting C-20 |
| Proof log | `PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, beside this file |
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

* Source rows: C-26 (2.15 R-1 and R-4; 2.15 "Relation to other canon")
* Change type: NEW_CANON
* Target document: PF06-Canon-Change-Process-Guide
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15: "Relation to other canon" l.1666-1681, R-1 l.1704-1740, R-4 l.1761-1786; supporting addendum 2.16 R-3 l.1940-1948 (SYN-A and SYN-B stored and registered)
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

`MISSING` blocks each stage as the table shows. No agent may override the block. Only the Product Owner may waive the live test or any part of it, by a written waiver specific to the change (HDE Governance §3.4).

| Stage | Effect of `MISSING` |
| :---- | :---- |
| QA readiness | Not `READY_FOR_QA` |
| QA plan | Not approval-ready |
| QA plan review | Not approvable |
| QA evidence review | Not acceptable |
| Final QA report | No `PASS` verdict |
| Close mutation set | Not close-PR-ready |
| Closure decision | Not `CLOSE` |

Every prompt that produces one of these records, including the Change Flow and GCFPE prompts, applies this rule. An agent running a prompt that does not yet state the rule applies it from this section.

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

END OF REDLINES
