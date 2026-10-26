# T-PF27 — preparation proof log for redlines from PF27 v2.0.5

This is the processing report for `redlines-PF27-from-v2.0.5.md` in this directory. It records how the redlines were prepared, from what, and what was verified. It is not QA, acceptance, canon adoption or closure, and it writes nothing to `docs/pfcanon/`.

## 1. Identity

| Item | Value |
| :- | :- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf27/redlines-PF27-from-v2.0.5.md`: 422 lines, 39,287 bytes, SHA-256 `42206d707394cb4fa354131aef7bb622c8731d4be2960d09673f3cfeb5a0c686` |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf27/redlines-PF27-from-v2.0.5.proof-log.md` |
| Run identity | `gtwpe-20261026-pf10-v13-8-8/T-PF27`, preparation revision `P1` (first and only preparation of this run) |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff, fetched live in this session (page state 2026-10-09T11:05:22Z) |
| Originating preparer | TW-DRAIN-10 in the Nathan-started T-PF27 document session, Claude Code cloud session https://claude.ai/code/session_01QRazLg2AQgDCgvdFbDJG1C. One session; no subagent, reviewer, controller or other session was used |
| Handoff | GTWPE 100926.1 T-PF27 document session (TW-DRAIN-10 then TW-APPLY-10), sent 2026-10-26T21:08:31Z; it authorizes preparation and Apply in this one session |
| Preparation outcome | `READY` |
| Save completeness | `COMPLETE_PACKAGE` (receipt in §8) |
| Preparation date | 2026-10-26 (UTC) |

## 2. Target

| Item | Value |
| :- | :- |
| Logical title and version | `PF27-Canon-Plan-Templates`, v2.0.5, Status Canon |
| Path | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`; the only PF27 file in `docs/pfcanon/` on `main`; no volume or phase parts |
| Commits read | Ledger baseline `9dda63dd3f05f496c3ff67e95da78550d3950c5a`; current `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c` (re-fetched before writing). The blob is identical at both, and `main` carries no newer PF27 version |
| Blob | `96becf4158c0a7b294c38d1eb503e2c280de2cd9`, matching the handoff and the ledger (`96becf4158c0`) |
| Bytes | 312,281 bytes; 3,859 LF-terminated lines; UTF-8, no BOM, no CR; the last line is empty, so the file ends `\n\n` |
| Raw SHA-256 | `1542ba9e4752a1ad3f6985dfd7e84961d0fc5fc46b3dcbaacc529bbddfc3c7f8`, computed over the raw blob bytes |
| Coverage | Read in full, lines 1–3859, including every table, template block and the final §12 Approval block |
| Last change on `main` | `2ff696b4d9e7` (2026-10-24T01:18:47Z) |

Native document-control header (lines 3–15), supplied for TW-APPLY-10's metadata plan:

| Field | Value at v2.0.5 | Native format |
| :- | :- | :- |
| `**Title:**` | `PF27-Canon-Plan-Templates` | no embedded version |
| `**Version:**` | `v2.0.5` | `v` plus dotted numeric `MAJOR.MINOR.PATCH` |
| `**Status:**` | `Canon` | not stale; no change |
| `**Effective date:**` | `2026-10-09` | `YYYY-MM-DD` |
| `**Last Update Gate:**` | `BN 13.5` | `BN <PF10 version>`, with other sources separated by `; ` |
| `**Invocation tag:**` | `INV-f2ac55d77ce9aacc` | protected; no change |

- No other occurrence of `v2.0.5`, `2.0.5` or `2026-10-09` exists in the body, so no internal restatement needs synchronizing.
- PF27 has no change log, revision history or Doc-Delta section, and none of its rules requires an entry for a revision. No history redline is prepared.

Sources that justified the update, in source order, for the Last Update Gate:

1. `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, PF10 v13.8.8, gate form `BN 13.8.8` (RL-001, RL-003 to RL-005, RL-012).
2. `HDE-CRD-0002-specification-v1.1-approved.md` (RL-006 to RL-011).
3. `HDE-CRD-0002-QA70-qa-plan-review-v1.0.md` (RL-002).

Delta 01 (`HDE-CRD-0002-specification-delta-v1.0.md`) was read to confirm that it leaves CR-1 and CR-2 unchanged; its §4 preserves "the canon-conflict register CR-1 to CR-3 as carried". No redline rests on it, so it is not a gate source. No PF document other than PF10 is a gate source.

## 3. Ledger and selected scope

- Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`, identical on `main`). The shared branch carried a later ledger blob from other sessions' Completion cells (`9c2633e32cb5` when this preparation was written); the T-PF27 row is unchanged in it.
- Row read: T-PF27. Its target, baseline blob, rows and uncertainty note match the handoff exactly.
- "Precedence and closure controls" and "Held and deferred items" were read before work began.
- Assigned rows: S-CR1, S-CR2, A11 with A18, A11 and A14, A31, A30, X07.

| Source | Identity | Selected boundary, read in full |
| :- | :- | :- |
| PF10 v13.8.8 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`; blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`; 729,539 bytes; SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`, verified | Front matter 1–223; 2.11 (1205–1318); 2.14 (1549–1619); 2.18 (1956–2081); 2.30 (3259–3360); 2.31 (3361–3470). Each addendum was read from its H2 to the next H2 |
| HDE-CRD-0002 Specification v1.1 (approved) | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`; blob `c4802a5a7fa3` | CR-1 (199–208), CR-2 (210–219); also read: the canon conflict register's lead-in (193–197), CR-3 (221–230) for context, and the "Format and register posture" lines 24–39 and 112, as supporting reading |
| Delta 01 | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`; blob `9408d6ed091b`; approved in SR4 | Read in full (1–162). It removes S01 and keeps the release at 1.3.0; C-1 to C-14 do not touch CR-1 or CR-2 |
| X07 | `docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.0.md`; blob `b083486fc768` | §5, "CR-11 — decided" (256–274) |
| Closure evidence | X10 `c48f77a0c220`, SR4 `5a6cecc86f60`, X11 `2260eae17974`, X12 `ac60f368f6d9`, X13 `d6cceaf3a019`, X14 `0bbc8050d3c1` | Identities verified on `main`. They establish, as the ledger records, that HDE-CRD-0002 is closed (CLOSE, CHANGE_CLOSED by Isis, 2026-10-26T16:40:00Z) |

Application rules applied (PF10 front matter §5 and the ledger's precedence controls):

- 2.18 withdraws the cost-ceiling passages of 2.11 to 2.16, so no ceiling, budget or spend-recording text is drafted.
- 2.14 narrows 2.11 rules 7 and 8 for P1 findings. Rule 7's decline route and rule 8's "accept a stated limit" survive only below P1, and 2.14 rule 5 is withdrawn by 2.18.
- 2.17 amends 2.15; neither is selected for this target, and no T-PF27 row depends on them.
- 2.11's misnumbered cross-references are read by the rule their text describes:
  - the drainage row's "rule 5 disposition" is rule 7;
  - its "rule 6 trigger" is rule 8;
  - rule 7's "(rule 3)" is rule 4, the real-input definition;
  - "Scope and supersession"'s "a fix under rule 5" is rule 7.
- The published 2.31 numbers its retained decisions 1 to 10. "Rules 4 to 8" means its published items 4 to 8.

## 4. Supporting reading

These sources were read to settle ownership, meaning or wording. They are not drainage. Canon was read from `main` (`0838ba08254e`); the branch edits no `docs/pfcanon/` file.

| Source | Section read | Used for |
| :- | :- | :- |
| `PF03-Reference-Technical-Writing-Best-Practices` v1.8.8 (blob `504712df548a`) | Whole document | The editorial standard: functional naming of actors (§2); no ellipsis; no outer-bold headings on new text (§8); preserving structure; title-only routing; Build Notes cited by title only |
| `PF04-Canon-HDE-Governance` v2.8.7 | §9.1.1 and §9.1.2 in full | The governing position for CR-1 and CR-2: no CRD Plan; HDE CRD Records is historical and reference only, and the active workflow "MUST NOT create, update or synchronize their entries"; Specification content "MUST NOT prescribe atomic implementation tasks, file edits, commands, planned PR/Ops work units"; the Implementation Plan identifies them; "Historical drainage" |
| `PF30.1-Canon-HDE-CRD-Records` v0.9.1 | §1 to §7 (1–362) | The format owner's current wording: §4.1 "Work units" is "Pending — identified by the change-wide Implementation Plan"; §4.3 allocates units to phases as the Implementation Plan identifies them |
| `PF06-Canon-Change-Process-Guide` v2.5.4 | §0.1, §0.1A, §0.2 (the CI-budget paragraph), §1.0 to §1.0.6, §1.1.4 (opening), §3.5.1, §3.5.2.1 | The mirrored "PF30 accountability" and "PF30 work mapping" passages (T-PF06's targets, not changed here); "Specification format authority"; the close PR and close mutation set requirements 2.31 rule 5 cites |
| `PF19-Canon-Glow-QA-Guide` v3.0.6 | "Change-lane QA applicability" | The CRD's accountability wording: "CRD work retains its assigned CRD ID, approved Specification, Implementation Plan and decision lineage; PF30 registration or an invented PF09 mapping is not a prerequisite. PF20 and PF30 are historical records" |
| `PF14-Canon-HDE-Mechanics-Guide` v3.5.8 | §1.6.3, the CRD publication bullets | CR-11's basis: CRD `additional_files` "do not automatically become indexed evidence"; auxiliary output "does not become a primary or indexed family merely by being present" |
| PF10 v13.8.8, 2.35 | Line 3817 only, located by search | 2.35 lists CR-11 among the canon drainage items. No 2.35 content is drained here |
| `ci/checks/classify_ci_changes.py` on `main` (read-only) | `_DOCUMENTATION_PREFIXES`, lines 171–180 | RL-004's locus: eight prefixes (`docs/crd/`, `docs/ephemeral/`, `docs/graph/`, `docs/pfcanon/`, `docs/plans/`, `docs/prompt_ecosystem_management/`, `docs/qa/`, `docs/run/`). File last changed by `2ff696b`. The list is not copied into PF27 |
| `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf07/redlines-PF07-from-v2.3.3.md` | Format only | Package layout consistency with the run's earlier T-PF07 package |

Canon search: `docs/pfcanon/` on `main` and PF10 were searched by exact literal for "Plan Templates", "PF27", "CRD Plan", "PF30", "work mapping", "Step-0B", "CR-11", "business case", "close mutation set" and "five-update circuit breaker". Every governing section found was read as above.

## 5. Change and disposition ledger

Every change in the selected units is accounted for below.

| Row | Selected change | Disposition | Redline or location |
| :- | :- | :- | :- |
| S-CR1 | CR-1: §2A "PF30 accountability", "a concise initial record in the active PF30 volume", "route CRD results and closure posture to the existing PF30 CRD record", "Update the existing CRD record", against HDE Governance §9.1.1 | Actionable | RL-006 (applicability paragraph, including "controlling work register"), RL-008 (implementation precondition), RL-010 (results and closure posture; the "PF30 work mapping" substitution, the §2A counterpart of the Change Process Guide §1.0.4 passage CR-1 names), RL-011 ("accountability register" and "Update the existing CRD record") |
| S-CR1 (CRD Plan) | CR-1's "CRD Plan" wording | Out of this target's ownership | PF27 contains no "CRD Plan" wording (exact search: 0 hits). The PF30.1 wording is T-PF30.1's |
| S-CR2 | CR-2: the §2A intake prompt "Planned PR and Ops units" and "Alchemical phase separation" ("included PR and Ops units") | Actionable | RL-007 (prompt removed), RL-008 (the rule stated once after the prompts), RL-009 (phase-block fields) |
| A11 with A18 | Plan Templates "Business Case (MUST)": every requirement and work unit of Epics and CRDs, rules 1 and 2, with no ceiling | Actionable | RL-005 |
| A11 and A14 | Plan Templates "Source-bound review authority and exact-fix limits": 2.11 rules 7 and 8 (with rule 4's definition and rule 5's constructed-input sentence), and 2.14 rules 2 and 3 with rules 1, 4 and 6 | Actionable | RL-003 |
| A31 | Plan Templates: a close-mutation-set task template beside the Ops Task Record | Actionable, drafted only from 2.31 rules 4 to 8 (the ledger's uncertainty note) | RL-012 (new §3B); RL-001 (governed-artifact list) |
| A30 | RCA D-1: a code-identity guard that excludes storage paths uses the classifier's whole CI-exempt prefix set | Actionable | RL-004 |
| X07 | CR-11: Plan Templates Step-0B (CRD applicability) | Actionable | RL-002 |

Changes in the selected units that belong to other targets. Each is out of this target's ownership, and none is drafted here:

- 2.11: HDE Governance §9.7.7 goes to T-PF04; HDE CRD Records §4.1 goes to T-PF30.1; Change Process Guide §1.1.4 goes to T-PF06. The AGENTS.md row has already landed (ledger A11). The prompt changes go to GCFPE-MGMT-10.
- 2.14: the PR-35 and PR-40 prompts go to GCFPE-MGMT-10; Change Process Guide §1.1.4 goes to T-PF06; the optional AGENTS.md note needs the Product Owner's instruction.
- 2.18: "Required canon drainage: None of its own"; its prompt items go to GCFPE-MGMT-10.
- 2.30:
  - PO-5 goes to Glow QA Guide §3.4.3 (T-PF19).
  - PO-2 is held as H-02, and LR5-O1 as H-03.
  - MB-021 and the QA-100 evidence-commit defect go to GCFPE-MGMT-10.
  - The rest of the addendum (the QA record, RCA causes and lessons) is history with no PF27 change.
- 2.31: Change Process Guide §3.5.1 and §3.5.2 go to T-PF06; Glow QA Guide §3.1.3 goes to T-PF19; installation (MB-030) goes to GCFPE-MGMT-10. Rules 9 (interim operation) and 10 (HDE-CRD-0002) are not drafted, because the template takes only rules 4 to 8.
- X07: HDE Mechanics Guide §1.6.3 goes to T-PF14.
- F00 (front matter): applied as the application rules; no standalone change.

Held and closure posture:

- No held item was touched. H-02 (PO-2) and H-03 (LR5-O1) appear in 2.30 and are not drafted. H-01 and H-04 to H-06 do not arise in the selected units.
- No change is held back on closure grounds. Every selected change belongs to HDE-CRD-0002, which X11 records as closed, or is a cross-cutting Product Owner rule in force (2.11, 2.14, 2.18, 2.31), as the ledger's "Precedence and closure controls" state.

## 6. Interpretations, constraints and assumptions

1. **Insertions as `REPLACE`.** Each insertion is a `REPLACE` that reproduces its anchor unchanged and adds the new text. This keeps every literal newline inside the payload, and Technical Writing Best Practices §8 allows a widened `REPLACE` that carries unchanged material. The RL-007 removal is a two-line `REPLACE`, so the removed line's own LF is consumed and no blank line is left inside the intake list.
2. **Placement of A31's template.** "Beside the Ops Task Record" is met by a new H2, §3B, at the next free position after §3 and §3A. No existing section is renumbered.
   - The name "Close Mutation Set Task Record (Template)" mirrors "Ops Task Record (Template)", since 2.31 gives no name beyond "a close-mutation-set task template".
   - New headings carry no outer bold, under Technical Writing Best Practices §8. The neighboring headings keep theirs. This is presentation only.
3. **A31 content limit.** Every §3B statement maps to 2.31 items 4 to 8; the record fields restate only those elements. The stage code and title (CL-05 — Prepare and Publish the Close Mutation Set) and the closure authority's name (Isis) are 2.31's. Prompt codes appear only where 2.31 uses them as stage identities (ESC, RS, PR-10 to PR-40). No path, schema, command or writer name is minted.
4. **RL-002 placement.** The CRD applicability block sits inside Step-0B, before the existing "Requirements:" list it applies. It uses the target's own terms ("QA RCA & Doc Delta summary", "plan-vs-execution drift") and names no change-specific check number.
5. **RL-003 placement and naming.** The rules are placed in the named section, after its last paragraph. The reviewer is described by function ("an automated code review"), as Technical Writing Best Practices §2 directs. The PR-review trigger is stated as distinct from the Live QA iteration-churn escalation, which **QA planning QoS guardrails** says is its sole local home, and from the CI-budget section, as 2.11 "Scope and supersession" requires. American spelling ("labeled", "behavior") follows the target.
6. **RL-004 placement.** The bullet follows the first "Hard blockers" bullet, which already requires "validation of the required current code posture". The HDE locus is named, but the prefix list is not copied (PF27 "Out of scope and source routing").
7. **RL-005 scope.** Only rules 1 and 2 are drafted, as 2.11's drainage row states. Rule 3's gates belong to prompts and other owners, so the existing "Review posture" bullet is unchanged.
8. **RL-010.** The "PF30 work mapping" substitution is not among CR-1's quoted §2A clauses, but it points at the PF30 entry that HDE Governance §9.1.1 forbids. It is the §2A counterpart of the Change Process Guide §1.0.4 passage CR-1 names, so it is aligned in the same drainage. The replacement wording is Glow QA Guide's own, not new design.
9. **Retained §2A content.** The following stay unchanged:
   - the §2A heading;
   - its governed-artifact list entry ("HDE-CRD-Specification Profile and PF30 Record Contract");
   - the format-ownership sentences, consistent with Change Process Guide §0.1A "Specification format authority";
   - the third paragraph of "PF30-owned Specification format and record contract", which describes historical PF30 records.

## 7. Observations recorded and not drafted

None of the following is a selected change, and no source authorizes a change, so no redline is prepared:

- Lines 1174 and 1175 are an identical duplicated bullet ("Review gates are about execution safety").
- Several templates show rendered `\\` where a placeholder appears to have been lost, for example line 759, `#### **CHECK \\: \\**`. The intended placeholder text is not established by any source.
- The governed-artifact list (lines 31–43) does not list §12, General Implementation Plan.
- These are not markers under the TW-DRAIN-10 marker rule. The scan for draft status, TODO, FIXME, TBD, "fill in", `???` and editorial notes found only canon-required rule text and template content (lines 239, 2210–2225 and template fields). `[Required−Now]` in the "Purpose & scope" heading is a canon heading convention that HDE Governance also uses.

## 8. Producer validation

The validator `validate_redlines.py` was run with `python3 -I` from the session scratchpad. It parses the saved redlines file and checks it against the unchanged original bytes. It checks:

- ID sequence;
- operation dialect;
- the expected count, with overlapping occurrences counted;
- complete-line boundaries;
- empty OLD;
- NEW equal to OLD;
- payload ellipsis, CR, tab and four-backtick runs;
- pairwise overlap and shared boundaries;
- the `END OF REDLINES` sentinel.

It then simulates one-pass application in descending offset order and proves preservation by rebuilding the expected stream from the untouched original intervals and the payloads.

| ID | Operation | Expected | Observed | Original lines | OLD chars | NEW chars |
| :- | :- | :- | :- | :- | :- | :- |
| RL-001 | REPLACE | 1 | 1 | 35 | 25 | 60 |
| RL-002 | REPLACE | 1 | 1 | 666–668 | 59 | 1,062 |
| RL-003 | REPLACE | 1 | 1 | 1014 | 496 | 3,984 |
| RL-004 | REPLACE | 1 | 1 | 1018 | 536 | 1,013 |
| RL-005 | REPLACE | 1 | 1 | 1398 | 168 | 1,138 |
| RL-006 | REPLACE | 1 | 1 | 1872 | 301 | 633 |
| RL-007 | REPLACE | 1 | 1 | 1891–1892 | 75 | 41 |
| RL-008 | REPLACE | 1 | 1 | 1898 | 211 | 353 |
| RL-009 | REPLACE | 1 | 1 | 1904 | 219 | 361 |
| RL-010 | REPLACE | 1 | 1 | 1913–1915 | 281 | 467 |
| RL-011 | REPLACE | 1 | 1 | 1941–1943 | 777 | 1,258 |
| RL-012 | REPLACE | 1 | 1 | 2185–2187 | 59 | 4,205 |

- Result: `VALIDATION PASSED: 12 operations, no overlap, one-pass simulation consistent`.
- No two spans intersect or share a boundary.
- The simulated content output is 323,676 bytes and 3,938 lines, ends with LF, SHA-256 `098ee7e59cf0def3cfcafe7b5dfe4690c85e0eba984d3abe3eb7771d5b960267`. This is before the header metadata that TW-APPLY-10 adds.
- A unified diff of the simulation against the original was reviewed for list continuity, blank lines and section boundaries.
- Corrections during preparation:
  - Redlines file: one, before validation. RL-007's rationale shortened a quotation with an ellipsis, and that was replaced with the full quoted phrase. No payload was changed after the validator first passed.
  - This proof log: its first saved draft stated a save receipt before the read-back had happened. The receipt fields were reset to pending and completed only after the checks below. Two shortened quotations and one shortened path were also written out in full.
- Save verification receipt, recorded after the checks: the saved redlines file was read back in full (422 lines, sentinel present). Its SHA-256 was recomputed (`42206d707394cb4fa354131aef7bb622c8731d4be2960d09673f3cfeb5a0c686`, equal to §1), and the validator was re-run on the saved bytes with the same result. This proof log does not record its own read-back or its own commit hash; the session's final response and the ledger's Completion cell give the commit that holds both files.

## 9. Limitations and unresolved items

- None blocking. No required change or dependency is unresolved.
- The wording drafted for the CRD lane in §2A follows HDE Governance §9.1.1, Glow QA Guide and HDE CRD Records as they stand on `main`. T-PF06 and T-PF30.1 align their own documents separately; if their drainage changes those owners' wording, §2A may need a later consistency pass.
- The §3B template states the stage's boundaries as 2.31 decides them. 2.31 records the CL-05 prompt page as a candidate, not an installed release member. The template makes no claim about installation.

## 10. Next step

READY / COMPLETE_PACKAGE. Nathan's handoff authorizes TW-APPLY-10 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b) in this same session. It uses:

- the original at `0838ba08254e`;
- this package;
- ledger rows T-PF27;
- branch `docs/20261026-gtwpe-pf10-v13-8-8-documents` and shared draft PR [amthorn78/glow-hdengine-v2#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761);
- final outputs `pf27/PF27-from-v2.0.5.md` and its proof log, or on failure `pf27/apply-diagnostic-PF27-from-v2.0.5.md`.
