# T-PF07 — preparation proof log for `redlines-PF07-from-v2.3.3.md`

This is the processing report for the redlines file beside it, `redlines-PF07-from-v2.3.3.md` in `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf07/`. Both files carry run `gtwpe-20261026-pf10-v13-8-8/T-PF07`, preparation revision `P1`.

## Outcome

- Preparation outcome: **READY**. Eight operations: seven `REPLACE` and one `FIND_AND_REPLACE`. Every selected change is accounted for, and no blocking dependency remains.
- Save completeness: see "Save verification" at the end. It is recorded only after both files were read back.
- Next step: TW-APPLY-10 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b) in the same Nathan-started document session, as the handoff authorizes.

## Identity

| Item | Value |
| --- | --- |
| Task | T-PF07, ledger `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`; byte-identical on `main` `0838ba08`) |
| Assigned rows | A19; A09 with X05; A20 and A35. Held H-05 is not touched |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff, fetched live on 2026-10-26 (Notion page state 2026-10-09T11:05:22Z) |
| Originating preparer | TW-DRAIN-10 in the Nathan-started T-PF07 document session: Claude Code cloud session https://claude.ai/code/session_01Tgfx3BStUkwc3FCxt1iDDU. One session, no subagent, no reviewer |
| Target | `PF07-Canon-Glow-Infrastructure` v2.3.3, Status Canon, Effective date 2026-10-09; `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md` |
| Target baseline | `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a` (handoff and ledger baseline); byte-identical at the current `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`, which changed only the ledger. Git blob `7d2734ce2b75a7277a632b881bfb931ff88bf7af`; 98,175 bytes; 1,431 lines; the file ends without a trailing newline; raw UTF-8 SHA-256 `573ceecfb93557cb93db04179a535a0d3c1209a99f5128e0408384f22b4110cc`. `main` carries no newer PF07 |
| Change source | PF10-HDE-Build-Notes v13.8.8, `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, 729,539 bytes, 3,955 lines, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`, effective 2026.10.26. It is the sole unlettered logical representation on `main` |
| Selected units, read in full | Front matter, lines 1–223 (application rules §1–§9, cross-references, Addendum Index); 2.9, lines 1003–1101; 2.19, lines 2082–2321; 2.20, lines 2322–2395; 2.35, lines 3725–3955 (`\<eof\>` on line 3955) |
| Supporting cross-reference | X05: `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md`, blob `6baead456619af1e73e15ace1079380f5797ca85`, §17, lines 701–739, read in full. Supporting reading, not a change source |
| Output | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf07/redlines-PF07-from-v2.3.3.md` and this proof log, on branch `docs/20261026-gtwpe-pf10-v13-8-8-documents` |

Every source was read from `origin/main`. No native Google Doc, Drive copy, Library copy or memory was used.

## Coverage

- **Target.** The complete PF07 v2.3.3, lines 1–1431, was read, including all tables and the three §10 code blocks.
- **Selected sources.** Each selected unit was read in full, heading to next heading of the same level. No unselected PF10 addendum was read for this task.
- **Editorial standard.** `PF03-Reference-Technical-Writing-Best-Practices` v1.8.8 (blob `504712df548a`, 633 lines) was read in full.
- **Supporting reading, read to establish ownership only:**
  - HDE-CLI-API-Vendor-Ref v2.5.3 §7.1.11 to §7.1.11f, lines 3498–3597. The audit sink's contract lives there; the key's name does not.
  - `engine/bodygraph/vendor_audit.py` on `main` `0838ba08`, read-only: lines 1–50 and 85–107. Last changed by `2ff696b4`.
  - The prior T-PF07 package `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/pf07/`, for format and marker precedent only.
- **Canon-first search on `main`.** `git grep` over `docs/pfcanon/` found `HDE_VENDOR_OVERRIDE_AUDIT_PATH` in no permanent PF document. PF10 names it once, in 2.9's unset-variable list. The search also covered "deploy source", "landing on `main`", "start setting" and "audit sink".

## Precedence and closure

- **Closure.** HDE-CRD-0002 is closed, by CL-C-10 v1.2 (CLOSE, CHANGE_CLOSED, Isis, 2026-10-26T16:40:00Z; X11), after the QA-120 PASS (X13). 2.32 to 2.35 record the closure. No assigned change is held back on closure grounds.
- **Supersession** (PF10 front matter §5):
  - 2.18 withdraws the cost-ceiling passages of 2.11 to 2.16 and of the Specification delta addendum's record. 2.20's sentence "Its business case and cost ceiling are in the Product Owner decision record §2" is therefore not applied. It bears on no PF07 text.
  - The narrowings by 2.14 and 2.17, and 2.11's misnumbered cross-references, touch no passage used here.
  - 2.19 and 2.20 overlap on one point: who records the deployment facts. 2.20, published higher, keeps "WU-OPS-01 records the deployment facts" as a stated limit. 2.19, written later under its lower published number, says the Product Owner's deployment direction discharges that obligation.
  - Either reading leaves the PF07 content the same. The live Railway start setting is unverified, and no start command was recorded. 2.35, the latest addendum, confirms "the unverified live Railway start setting (a stated limit with a Glow Infrastructure doc-delta candidate)".
- **PF10 silence** (front matter §8). No selected addendum states replacement wording for PF07. The wording below is drafted within PF07's own section conventions.

## Change and disposition ledger

Every change identified in the selected units is listed with its disposition. "Elsewhere" means the triage ledger routes it to another task or owner; no PF07 edit is made for it.

### 2.19 (A19)

| Item | Disposition |
| --- | --- |
| P-18 and "Unresolved obligations": the HD Engine deploy source is commits landing on `main` of `amthorn78/glow-hdengine-v2`, a Product Owner-provided fact, with doc-delta targets Glow Infrastructure §3.1 and §4.1 | **RL-001** (§3.1) and **RL-002** (§4.1) |
| P-9, P-18, P-19: build and start commands are not discovered or recorded | Carried in RL-002's parenthetical and in **RL-003**. §4.1's "Build artifact … TBD" is kept |
| P-9: GET /internal/version reporting the release_id is the deployment proof; the rollback intent | Not drafted. This is an OPS success criterion and a procedure, and PF07 §1 defines no procedures |
| Facts behind: "No PF document states the HD Engine service's deploy source"; the start setting unverified (§10); Build artifact TBD (§4.1); §2.4's no-downgrade rule | Confirmed against the target. RL-001 and RL-002 fill the deploy source; §10 and the TBD are kept |
| build_commit is a fixed source value | Elsewhere: PF09.7 relation R-4 (T-PF09.7) |
| P-1 to P-17, P-20; the `.env.example` classifier facts; business cases; the PF10 numbering corrections | Elsewhere: Implementation Plan text, repository facts, the Product Owner, PF10 publication facts |
| The WU-OPS-01 evidence root `audit/ops/hde-crd-0002/wu-ops-01/` | Not drafted. No source directs it, and PF07 §10.5 assigns evidence roots to HDE-Schemas & Artifacts |

### 2.9 with X05 §17 (A09)

| Item | Disposition |
| --- | --- |
| X05 §17: "Glow Infrastructure §8 config keys — the new key `HDE_VENDOR_OVERRIDE_AUDIT_PATH`", carried by 2.9's "Required canon drainage" | **RL-007** (§8.2.1). The key name was confirmed at `engine/bodygraph/vendor_audit.py:23`: `VENDOR_OVERRIDE_AUDIT_PATH_KEY = "HDE_VENDOR_OVERRIDE_AUDIT_PATH"` |
| X05 §17 rows for HDE-CLI-API-Vendor-Ref §7.1.11 and §7.2.0 | Elsewhere: T-PF05 |
| X05 §17 rows for HDE Users Guide §16, §10.1 and Recipe F | Elsewhere: T-PF29 |
| §7.1.11f "governed clock boundary" (OBS-W4-4) | Held as H-04 for the Product Owner, and not a PF07 section. Not drafted |
| README.md, AGENTS.md and runbook mentions | Elsewhere: repository documentation (WU-DOC-01; 2.34's D-items) |
| OBS-P4-4: `scripts/ops/admin_vendor_qa.py` is non-functional (missing `--user`; F-10). Owner: the Product Owner | Not drafted; no source directs a PF07 change. 2.35 lists it as an operational item, not a candidate. Observation for the Product Owner: PF07 §2.5.1, §5.1.1 and §5.1.3 still name this script as the supported prod-QA operator harness |
| LR4-O1 to LR4-O4, OBS-P4-1 to P4-3 and P4-5 to P4-7, OBS-W4-1 to OBS-W4-3, carried items, review history | Elsewhere: owners as 2.9 names them; history for T-PF30.1 |

### 2.20 (A20)

| Item | Disposition |
| --- | --- |
| "Facts behind": "The live Railway start setting is unverified (Glow Infrastructure §10)"; the Procfile reads `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' …` | **Already represented.** §10's opening paragraph (original line 1357): "This section does not assert that any declaration is the current Railway start command or the normative production command. The current Railway setting is not verified." The `Procfile` declaration is at §10.1, lines 1367–1371. No §10 wording change is needed |
| "Unresolved obligations": the live Railway start setting, "A stated limit, not a blocker" | The stated limit is represented at §10 (line 1357). **RL-003** carries it to §4.1's pointer, which called §10 "canonical Railway command kept verbatim". "Not a blocker" is HDE-CRD-0002's posture; PF07's PF07-gap rules are not changed |
| C-1 to C-14 (the effective Specification); "no canon change" | Elsewhere: T-PF30.1 |

### 2.35 (A35)

| Item | Disposition |
| --- | --- |
| "Not candidates": "the unverified live Railway start setting (a stated limit with a Glow Infrastructure doc-delta candidate)" | As for 2.20: §10 (line 1357) represents it, and **RL-003** removes the contradicting §4.1 pointer wording. Decision on the ledger's uncertainty: §10 itself needs no change |
| R-1 to R-5 PF09 relations; items 9 to 11; the remaining "not candidates" dispositions | Elsewhere: T-PF09.3, T-PF09.4, T-PF09.7, the Product Owner and the CRD candidate list |

### Front matter (F00)

The application rules (§1 to §9) were applied as stated above. There is no standalone change.

### Held items

- **H-05**, the PF07 procedure gap for observing production variable names, is untouched. RL-007 records per-environment bindings as **OPEN/TBD**.
- `audit/qa/hde-crd-0002/checks/qa-20-live-vendor-override/primary.log` records a presence-only production read of `HDE_VENDOR_OVERRIDE_AUDIT_PATH=UNSET`. That is QA evidence, not a selected source or a Product Owner-provided fact. It is not drafted as a PF07 value.

## Marker and hygiene classification (TW-DRAIN-10 document-control rule)

The prompt requires that the revised PF carry no placeholder, TODO, unresolved drafting note, editorial comment or instruction to a future writer unless canon requires that exact language there. It authorizes, as hygiene, the redlines that remove any other such marker. A complete scan of the target gives:

| Marker | Classification | Disposition |
| --- | --- | --- |
| 117 `TBD` tokens (30 of them `OPEN/TBD`) | Canon-required inventory notation for unconfirmed facts: §6.5 Notes ("Use **OPEN/TBD** when not confirmed (no guessing)") and the §8 policy ("When unknown, the value is marked **OPEN/TBD**"). This matches the prior PF07 run's finding | Kept |
| Lines 149 and 190, "replace **TBD** … as facts are confirmed" | A standing no-guess maintenance rule of the inventory, not a one-time note | Kept |
| Lines 163, 877–879, 883–885, 1005, 1020, 1272, 1281, 1409 ("record … only when confirmed", "until confirmed", "unless confirmed") | Conditional rules that limit what may be recorded | Kept |
| Line 871, "— confirm" | Bare to-do | **RL-004** removes it; **TBD** keeps the uncertainty |
| Line 895, "(confirm exact hostnames as we populate)" | To-do with drafting-status language | **RL-005**: "(exact hostnames OPEN/TBD)" |
| Lines 956, 965 and 974, "(via DB proxy; confirm)" | Bare to-do; the qualifier is real uncertainty | **RL-006**: "(via DB proxy; unconfirmed)", ×3 |
| Line 1295, "Please supply the value when known." | A request to the reader | **RL-008** deletes that sentence; the OPEN/TBD definition stays |
| `[Required-Now]`, `[Implemented]`, `[Speculative]` in headings | Content status labels, not document status | Kept |
| Ellipses: `Bearer …` (line 220) and `<epic-id>/...`-style path patterns (lines 23, 108, 459, 538, 717, 725, 1233, 1324) | Example and path-pattern notation, not drafting placeholders. PF03 §3 prohibits ellipses in PF documents, but PF03 is not an independent change source and no selected source covers these lines | Kept; a limitation for the Product Owner |

There is no `Draft` or similar status language about the document. Status Canon is current.

## Redlines and their basis

| ID | Rows | Type | Location (original) | Change |
| --- | --- | --- | --- | --- |
| RL-001 | A19 | CANON_UPDATE | §3.1 Railway, lines 582–584 | Adds **Deploy source (names-only)** → HD Engine: commits landing on `main` of `amthorn78/glow-hdengine-v2` (Product Owner-provided deployed environment fact) |
| RL-002 | A19 | CANON_UPDATE | §4.1 HD Engine, lines 632–633 | Adds a **Deploy source** bullet between Source and Build artifact, noting that the build and start commands are not recorded |
| RL-003 | A20, A35, A19 | CONSISTENCY | §4.1, line 638 | Start command pointer: "(canonical Railway command kept verbatim)" → "(checked-in declarations only; the live Railway start setting is not verified)" |
| RL-004 | marker rule | DOC_HYGIENE | §6.3.1, line 871 | Removes "— confirm" |
| RL-005 | marker rule | DOC_HYGIENE | §6.4, line 895 | "(confirm exact hostnames as we populate)" → "(exact hostnames OPEN/TBD)" |
| RL-006 | marker rule | DOC_HYGIENE | §7.1, lines 956, 965, 974 | `FIND_AND_REPLACE` ×3: "(via DB proxy; confirm)" → "(via DB proxy; unconfirmed)" |
| RL-007 | A09 with X05 | NEW_CANON | §8.2.1, after line 1268 | New key block `HDE_VENDOR_OVERRIDE_AUDIT_PATH`: what it names; not a secret; bindings OPEN/TBD; the checked-in fallback locations and refused paths; semantics routed to HDE-CLI-API-Vendor-Ref by title |
| RL-008 | marker rule | DOC_HYGIENE | §8.2.3 Notes, line 1295 | Deletes "Please supply the value when known." |

Notes on the wording:

- **RL-007.** The new block follows the neighbouring `HDE_WRITE_A7_PROOFS` entry: a key heading, names-only content, and the observed behaviour labelled routing-only.
  - Its fallback statements describe checked-in code only (PF03 §3: static inspection proves checked-in bytes, not deployed configuration).
  - It routes the flag, the event fields, durability and the unavailable-sink refusal to HDE-CLI-API-Vendor-Ref by title, without restating them (PF03 §5).
- **Section numbers.** No PF07 cross-reference was given a section number for HDE Build Notes. PF07 prose names other PFs by title only.

## Constraints, assumptions and interpretations

- **Gate source.** The ledger defines X05 as supporting reading, not a change source. The Last Update Gate source is therefore PF10 v13.8.8 alone.
- **Hygiene redlines.** RL-004 to RL-006 and RL-008 rest on the prompt's marker rule, not on a ledger row. They are reported as such.
- **Deploy-source wording.** "Commits landing on `main`" is 2.19's approved wording of the Product Owner direction of 2026-10-21 ("deploys come from github commits, this should already be well established"). PF07 does not record a deployment trigger, since 2.19 records none.
- **Raw section structure.** Several PF07 headings sit inside list items in the raw Markdown, at lines 592, 594, 840, 1173, 1192 and 1194. Section paths are therefore given for orientation. Uniqueness is proved over the whole original, not within a heading-bounded section.

## Producer validation

Validation ran on the unchanged original bytes with a local Python 3 script. Exact literal matching was used throughout, with no normalization, regex or fuzzy matching. Byte spans below are half-open.

| ID | Operation | Expected / observed count | Original byte span(s) | Payload bytes | Overlap |
| --- | --- | --- | --- | --- | --- |
| RL-001 | REPLACE | 1 / 1 | 42620–42803 | 354 | none |
| RL-002 | REPLACE | 1 / 1 | 44980–45133 | 334 | none |
| RL-003 | REPLACE | 1 / 1 | 46155–46244 | 126 | none |
| RL-004 | REPLACE | 1 / 1 | 61134–61226 | 80 | none |
| RL-005 | REPLACE | 1 / 1 | 63015–63067 | 38 | none |
| RL-006 | FIND_AND_REPLACE, whole PF | 3 / 3 | 66570–66595; 66879–66904; 67113–67138 | 29 each | none |
| RL-007 | REPLACE | 1 / 1 | 86527–86760 | 1,156 | none |
| RL-008 | REPLACE | 1 / 1 | 89591–89715 | 88 | none |

What the checks established:

- **Locators.** Every `REPLACE` OLD block starts at a line start, ends at a line end, and occurs once in the whole original.
- **RL-006.** FIND is nonempty and REPLACE does not contain it. After the simulated application FIND is absent, and REPLACE occurs exactly 3 times.
- **Overlap.** No two spans intersect, and there is no insertion gap.
- **Simulation.** A one-pass, original-bound application in descending offset order, with no rematching, gives 99,437 bytes, SHA-256 `1da5dc0a9f43550646325b8978dbfab4986838f3078c96415e52e7db3c452e8d`. This excludes the header fields that Apply derives. It is a simulation only; no revised PF was written by this step.
- **Parse-back.** The saved redlines file was parsed back. All eight operations, counts, OLD/NEW and FIND/REPLACE payloads match the authored plan byte for byte. The IDs are in order, and the file ends with `END OF REDLINES`.
- **Payload hygiene.** No new payload contains an ellipsis. The longest backtick run in any payload is 1, so the four-backtick fences are safe. No payload contains a secret or a value beyond what the target already records.

## Header provenance reserved for TW-APPLY-10

- **Version.** The native scheme is dotted numeric `v2.3.3`. One final-component increment gives `v2.3.4`.
- **Date.** The only revision date field is `**Effective date:** 2026-10-09`, format `YYYY-MM-DD`. Apply sets it to the execution date.
- **Last Update Gate.** Current value `BN 13.5; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`. The source that justified this update, in source order, is `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, PF10 version 13.8.8, so the derived gate is `BN 13.8.8`.
- **Other fields.** Title, Status (Canon) and Invocation tag `INV-f2ac55d77ce9aacc` stay unchanged.
- **No history entry needed.** PF07 has no change log or revision-history requirement, and no internal restatement of its own version or date. `### **2.3.3 Ops-only identity**` (line 213) is a section number and must not be changed.
- **No header redline.** The package carries no header redline.

## Limitations and unresolved items

- **Not shown in the batch:** the ellipses and the `scripts/ops/admin_vendor_qa.py` observation, both above, for the Product Owner.
- **No live observation.** No production, Railway, vendor or database surface was observed. Rails stayed closed, with `SAFE_MODE=1` and `ALLOW_NETWORK=0`.
- **No QA claim.** This package establishes no QA verdict, acceptance, canon adoption, drainage into `docs/pfcanon/` or closure. PF07 on `main` is unchanged.

## Save verification

Recorded after both files were saved and read back in full.

- `redlines-PF07-from-v2.3.3.md`: 13,363 bytes, 240 lines, UTF-8, LF only, final LF, SHA-256 `59c2ce8541a1da19814d06341a421ca7bb1ba074124870a15340ae5d9dcd6148`. It was parsed back against the plan: 8 of 8 operations match, and it ends with `END OF REDLINES`.
- This proof log was read back complete before this receipt was added, and read again after it. It does not carry its own hash.
- Both files carry run `gtwpe-20261026-pf10-v13-8-8/T-PF07`, revision `P1`, and the same preparer session.
- Save completeness: **COMPLETE_PACKAGE**. Preparation outcome: **READY**.
