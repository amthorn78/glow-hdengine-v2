# T-PF27 — application proof log for revised PF27 from v2.0.5

This is the application report for `PF27-from-v2.0.5.md` in this directory. It records how the revised PF was produced from the exact original and the validated redline package, and what was verified. The revised PF is a working output under `docs/ephemeral/`. It is not authoritative publication, canon adoption, QA, acceptance or closure, and nothing was written to `docs/pfcanon/`.

## 1. Identity

| Item | Value |
| :- | :- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf27/PF27-from-v2.0.5.md`: `PF27-Canon-Plan-Templates` v2.0.6; 323,765 bytes; 3,938 LF-terminated lines; ends `\n\n`, like the original; UTF-8, no CR; SHA-256 `850dc1a3c8294a0e0521f02cb7300fb05233beccb1ecadf611b41e8ea9adfb00` |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf27/PF27-from-v2.0.5.proof-log.md` |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b, fetched live in this session (page state 2026-10-09T11:05:22Z) |
| Applier | TW-APPLY-10 in the same Nathan-started T-PF27 document session, Claude Code cloud session https://claude.ai/code/session_01QRazLg2AQgDCgvdFbDJG1C. The handoff authorizes preparation then Apply in this one session; no subagent or other session was used |
| Run identity | `gtwpe-20261026-pf10-v13-8-8/T-PF27`; package preparation revision `P1` |
| Application outcome | `SUCCESS`: 12 content operations and 3 header metadata edits applied; zero operations rejected, skipped or converted |
| Execution date | 2026-10-26 (UTC) |

## 2. Inputs

| Input | Identity |
| :- | :- |
| Exact original | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md` on `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`, re-fetched immediately before application. Blob `96becf4158c0a7b294c38d1eb503e2c280de2cd9`; 312,281 bytes; 3,859 lines; raw SHA-256 `1542ba9e4752a1ad3f6985dfd7e84961d0fc5fc46b3dcbaacc529bbddfc3c7f8`, equal to the preparer's fingerprint (same raw-byte representation) |
| Drift check | `main` is unchanged since preparation, and the blob is identical at the ledger baseline `9dda63dd3f05`. `docs/pfcanon/` holds exactly one PF27 file and no newer version. The branch edits no `docs/pfcanon/` file |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf27/redlines-PF27-from-v2.0.5.md` at commit `22e60e3745aa009db558b77b438a03bbad97a786` (pushed); SHA-256 `42206d707394cb4fa354131aef7bb622c8731d4be2960d09673f3cfeb5a0c686`, re-extracted from that commit for application |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf27/redlines-PF27-from-v2.0.5.proof-log.md` at `22e60e3745aa009db558b77b438a03bbad97a786`; SHA-256 `b150d037ab4c97f90c8101a0e162f0d7df8108fa1b83cc825bf6dca8e6131fa7` |
| Preparer and state | TW-DRAIN-10 100926.1, this session; `READY` / `COMPLETE_PACKAGE`; no unresolved item; complete target reading (1–3859) and complete selected-source reading recorded |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` (ledger commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7`), task T-PF27, rows S-CR1, S-CR2, A11 with A18, A11 and A14, A31, A30, X07 |
| Selected sources | PF10 v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter 1–223, addenda 2.11 (1205–1318), 2.14 (1549–1619), 2.18 (1956–2081), 2.30 (3259–3360) and 2.31 (3361–3470). HDE-CRD-0002 Specification v1.1 (approved), blob `c4802a5a7fa3`, CR-1 (199–208) and CR-2 (210–219), overlaid by delta 01 (blob `9408d6ed091b`). X07, QA-70 review v1.0 §5 "CR-11 — decided" (256–274), blob `b083486fc768` |

The preparer's selected-source boundaries agree with the handoff and with the ledger row; they were checked against both. No unselected PF10 addendum was needed for this step.

## 3. Whole-batch validation before any edit

Every operation was resolved independently against the unchanged original before any output byte was written:

- All 12 are `REPLACE`, each with a nonempty OLD of complete lines, expected count 1 and observed count 1 (overlapping matches counted), a complete NEW, and NEW different from OLD.
- No `FIND_AND_REPLACE` is present, so the RL-045 rule has nothing to reject.
- The three metadata edits were added to the same original-bound plan. The 15 spans are pairwise disjoint, and none shares a boundary.
- The redlines file carries `END OF REDLINES`; its IDs run contiguously from RL-001 to RL-012.

## 4. Document-control header plan

| Field | Before | After | Basis |
| :- | :- | :- | :- |
| `**Version:**` (line 7) | `v2.0.5` | `v2.0.6` | One bump of the final numeric component of the native dotted version |
| `**Effective date:**` (line 11) | `2026-10-09` | `2026-10-26` | Actual application execution date, native `YYYY-MM-DD` |
| `**Last Update Gate:**` (line 13) | `BN 13.5` | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-QA70-qa-plan-review-v1.0.md` | The sources the package records as justifying the update, in recorded source order, deduplicated, joined by `; ` (preparation proof log §2) |
| `**Title:**`, `**Status:**`, `**Invocation tag:**` | unchanged | unchanged | Title carries no version; Status `Canon` is not stale; the invocation tag is protected |

- Source-file provenance for the gate: the PF10 file `PF10-HDE-Build-Notes-v13.8.8.md` (v13.8.8) as `BN 13.8.8`, then the two non-PF source filenames.
- Delta 01 is not a gate source, because no redline rests on it. No PF document other than PF10 is a gate source.
- No internal restatement of the version or date exists in the body.
- PF27 keeps no change log or revision history, so no history entry is required.
- The package carried no header operation, so there is no duplicate authorization to reconcile.
- The version, date and gate agree with one another and with the package.

## 5. Operation ledger and basis

Each line states the redline's basis as the preparer's proof log and the redline record give it. The positions are where each payload sits in the output.

| ID | Original line | Output line | Basis (rationale; source-ledger reference) |
| :- | :- | :- | :- |
| META-VERSION | 7 | 7 | TW-APPLY-10 header contract; version bump |
| META-DATE | 11 | 11 | TW-APPLY-10 header contract; execution date |
| META-GATE | 13 | 13 | TW-APPLY-10 header contract; package source order |
| RL-001 | 35 | 35 | Adds "Close Mutation Set Task Record" to the governed-artifact list after "Epic Remediation Plan", matching the new §3B; A31 (2.31 "Required canon drainage") |
| RL-002 | 666–668 | 667 | Step-0B CRD applicability. For a CRD the capture goes in the performing check's indexed `primary.log`, not an unindexed `00_meta/doc_deltas.md` (HDE Mechanics Guide §1.6.3). Step-0B's rules apply in full, both doc-delta surfaces are checked before "no deltas", and proof-bearing content is preserved; X07 (CR-11 `APPROVED_AS_CHANGED`, alternative (a)) |
| RL-003 | 1014 | 1021 | Real-input finding disposition, P1 rules and the PR-review repeated-finding-class trigger in "Source-bound review authority and exact-fix limits". The text is the surviving text only: P1 narrowing per 2.14, and no ceiling or budget per 2.18. 2.11's misnumbered cross-references were read by the rule their text describes; A11 (2.11 rules 4, 5, 7, 8), A14 (2.14 rules 1–4, 6), A18 (2.18 rules 1, 2, 6) |
| RL-004 | 1018 | 1042 | Code-identity guards that exclude storage paths use the classifier's whole CI-exempt prefix set (for HDE, `_DOCUMENTATION_PREFIXES` in `ci/checks/classify_ci_changes.py`, verified read-only on `main`); A30 (2.30 RCA D-1, O-11, L-3) |
| RL-005 | 1398 | 1423 | Business case for every requirement and work unit of Epics and CRDs: beneficiary, evidence, benefit and measure; no cost ceiling; rule 2's exclusions and the internal-tooling test against expected cost; A11 (2.11 rules 1, 2) with A18 (2.18 rules 1, 4) |
| RL-006 | 1872 | 1906 | §2A: a CRD is accountable through its approved Specification, Implementation Plan and decision lineage. HDE CRD Records is historical and reference only, and PF30 registration is not a prerequisite (HDE Governance §9.1.1; Glow QA Guide "Change-lane QA applicability"); S-CR1 (CR-1) |
| RL-007 | 1891–1892 | 1925 | Removes the intake prompt "Planned PR and Ops units"; S-CR2 (CR-2; HDE Governance §9.1.1) |
| RL-008 | 1898 | 1931 | Implementation precondition without a PF30 record, and the planned-unit rule stated once; S-CR1 (CR-1), S-CR2 (CR-2) |
| RL-009 | 1904 | 1937 | Phase-block fields without "included PR and Ops units"; the change-wide Implementation Plan allocates units to phase blocks (HDE CRD Records §4.3); S-CR2 (CR-2) |
| RL-010 | 1913–1915 | 1946 | CRD substitution for PF09 work-item mapping, and CRD results and closure posture kept in the change's own records rather than a PF30 entry; S-CR1 (CR-1, with the Change Process Guide §1.0.4 counterpart) |
| RL-011 | 1941–1943 | 1974 | HDE CRD Records as historical and reference home and CRD Specification format owner; a material change is recorded in the Specification's material-change history; PF30 history only by separately authorized historical drainage; S-CR1 (CR-1) |
| RL-012 | 2185–2187 | 2218 | New §3B Close Mutation Set Task Record (Template), drafted only from 2.31 rules 4 to 8: entries, exit, ownership; Dev, not Ops; authority and actor; close-tooling repair; record fields. The rule and the §4 heading are reproduced after it; A31 (2.31 "Required canon drainage") |

## 6. Preservation and output verification

- Application used one original-bound plan in descending offset order, with raw UTF-8 handling and no rematching on changed text.
- **Reconstruction.** The output equals the expected stream rebuilt from the untouched original intervals and the exact payloads, in order.
- **Untouched intervals.** Every untouched original interval sits unchanged at its place in the output: 308,548 of the original's 311,833 characters lie outside the 15 replaced spans and are preserved byte for byte. Every payload is present at its place.
- **Cross-check against preparation.** The output was compared byte for byte with the preparer's independent one-pass simulation (SHA-256 `098ee7e59cf0def3cfcafe7b5dfe4690c85e0eba984d3abe3eb7771d5b960267`). It differs only in lines 7, 11 and 13, the three header edits.
- **End of file, tables and code.** The original's final `\n\n` is preserved, and no CR was introduced. No table row, fenced block or heading outside the replaced spans changed.
- **Header.** The version appears once as `v2.0.6`; `v2.0.5` and `2026-10-09` no longer appear; the effective date and gate each appear once.
- **Markers.** The lines added by the package carry no Draft status, TODO, FIXME, TBD, placeholder or ellipsis. The scan's only hit, "draft/staging", is PF27's existing name for the doc-delta draft surface. Template placeholders elsewhere in PF27 are canon-required template content and are unchanged.
- These are text checks. They are not product QA.

## 7. Limitations and unresolved items

- None blocking.
- The revised PF is not live canon. Transferring it to `docs/pfcanon/` is a separate manual action for Nathan; this session wrote nothing there.
- The preparation proof log's §7 observations stay unchanged and undrafted, because no source authorizes them: the duplicate bullet at original lines 1174–1175, the rendered `\\` template placeholders, and §12's absence from the governed-artifact list.
- §2A follows HDE Governance §9.1.1, Glow QA Guide and HDE CRD Records as they stand on `main`. T-PF06 and T-PF30.1 drain their own owners separately.

## 8. Next manual action

Nathan reviews this revised PF and its package on the shared draft PR [amthorn78/glow-hdengine-v2#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761) (branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`). He decides whether and when to transfer it to `docs/pfcanon/`; Nathan alone merges.
