# Proof log: redlines for PF04-Canon-HDE-Governance from v2.8.7 (T-PF04)

This is the processing report of TW-DRAIN-10 for task T-PF04. It records how `redlines-PF04-from-v2.8.7.md` was prepared, from what, and what was checked. It is not QA, acceptance, canon adoption or closure, and it writes nothing to `docs/pfcanon/`.

## 1. Artifact and identity

| Field | Value |
| --- | --- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf04/redlines-PF04-from-v2.8.7.md` |
| Artifact size and SHA-256 | 33,229 bytes; `f176994249c55726ab66ab2a56b32f4fe458807946db06b85d5a1d91fadda632` |
| Operations | 11: RL-01 to RL-11 (7 `INSERT`, 4 `REPLACE`); ends with `END OF REDLINES` |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff, fetched live in this session (page edited 2026-10-09T11:05:22Z), as pinned by Nathan's handoff and by the ledger's prompt table |
| Run identity | `gtwpe-20261026-pf10-v13-8-8 / T-PF04 / prep-1` |
| Preparer | The Claude Code cloud session https://claude.ai/code/session_016CSjfJr3cAwrXWvB9NRJt9, started by Nathan for T-PF04 (GTWPE 100926.1 handoff of 2026-10-26). No subagent, reviewer or other session took part |
| Date | 2026-10-26 |
| Preparation outcome | `READY` |
| Branch and PR | `docs/20261026-gtwpe-pf10-v13-8-8-documents`, shared draft PR [amthorn78/glow-hdengine-v2#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761) |

## 2. Turn preflight

1. Task: T-PF04 preparation (TW-DRAIN-10), then application (TW-APPLY-10) in the same session, as Nathan's handoff authorizes. Target: one unlettered PF, `PF04-Canon-HDE-Governance`, no volume or phase parts.
2. Access: the target, PF10 v13.8.8, the ADR, PF03, PF06, the ledger, the closure evidence and the prompt pages were all read in this session (paths, blobs and hashes below). Notion read only; no Notion write.
3. Selected scope: ledger rows A01, A11, A15, A16, A17 and A18, with X03 as supporting reading, as the handoff and the ledger's T-PF04 row both state. They agree.
4. Full target reading: done, 22 bounded windows covering 570,610 bytes (§4). Output size: 11 operations, about 9.6 KB of added text.
5. Capability: Python 3.12 and git in the container; closed-rails defaults kept (`SAFE_MODE=1`, `ALLOW_NETWORK=0` were not changed; no product command ran).

## 3. Destination and state checks

- PR #760 (the ledger PR) had merged at 2026-10-26T21:18:51Z, so the continuation branch applies. When this session began, `git ls-remote` showed neither branch. Before the first write it showed `docs/20261026-gtwpe-pf10-v13-8-8-documents`, created meanwhile by the T-PF07 session, with shared draft PR #761 recorded on the ledger's continuation line (commit `f262af8`). This session fetched that branch and works on its tip; it did not create a branch or a PR.
- The branch held other sessions' outputs (PF02, PF07, PF09.4, PF09.7) and no `pf04/` path, so there was no output-name collision. The ledger on the branch differs from `13b64ddd` only in the T-PF07 completion cell and the continuation line.

## 4. Target identity and coverage

| Field | Value |
| --- | --- |
| Path | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md` |
| Commit read | `origin/main` at `9dda63dd3f05f496c3ff67e95da78550d3950c5a` (the handoff baseline); `origin/main` had advanced to `0838ba08254eaefc888019df49a06aa2ae99cc6c` (the #760 merge), where the blob is identical and no `docs/pfcanon/` file differs from the baseline. No newer PF04 exists on `main` |
| Native identity | Title `PF04-Canon-HDE-Governance`, Version `v2.8.7`, Status `Canon`, Effective date `2026-10-09`, Last Update Gate `BN 13.5`, Invocation tag `INV-f2ac55d77ce9aacc` (§0.1 Header) |
| Blob | `86cf613ce7f90ad7fd64c33ab3c808543a1c9581` |
| Bytes, lines | 570,610 bytes; 4,674 lines; LF only (0 CR); the file ends with two LF bytes |
| SHA-256 | `eb36f8e4cc038e73f5e497c857b05fc06724f01bcb3a68683d94e4a065ead367` (raw bytes) |

Coverage proof. The target was read whole in 22 consecutive line windows, each at most 27,000 bytes so that no long line was cut: 1–283, 284–464, 465–585, 586–744, 745–916, 917–1080, 1081–1288, 1289–1563, 1564–1797, 1798–2080, 2081–2326, 2327–2462, 2463–2609, 2610–2838, 2839–2937, 2938–3177, 3178–3401, 3402–3643, 3644–3938, 3939–4219, 4220–4561, 4562–4674. The windows' bytes, concatenated, equal the file exactly (570,610 bytes, the SHA-256 above). No read ended mid-line.

## 5. Sources and inputs

Change source (the only source of the changes):

| Unit | Path and identity | Lines read in full |
| --- | --- | --- |
| F00, front matter and application rules | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, HDE Build Notes v13.8.8, effective 2026.10.26, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, 729,539 bytes, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f` | 1–223 |
| A01, 2.1 TypeSafe reading is the GCFPE model guidance | same | 224–257 |
| A11, 2.11 Business case and real inputs | same | 1205–1318 |
| A15, 2.15 AQ-1: S21 ADR approved with changes; close-run family | same | 1620–1690 |
| A16, 2.16 WU-PR-07 lineage review v1.0 ACCEPT | same | 1691–1825 |
| A17, 2.17 The S21 ADR defers to HDE Build Notes; resolutions A and B | same | 1826–1955 |
| A18, 2.18 No cost ceiling | same | 1956–2081 |

Each boundary was checked: the line before each start is blank or the previous addendum's last line, and each end is followed by the next `## 2.x` heading. PF10 is one unlettered logical version; no other PF10 version was read.

Supporting reading (not a change source; it bounds or confirms meaning only):

- X03, `docs/adr/hde/close_pack_writer_adr.md`, blob `2d91679a198168958bf8b32c5f8b5459ee13de5b`, 25,360 bytes: "Decision" (lines 18–35) and "Affected canon and drainage consequences" (lines 76–88), the HDE Governance row: "§2.0.19 'Close-pack baseline artifacts', 'Close report minimal content (normative)' and 'Close-pack manifest `key_outputs` shape (normative)'; Appendix D.0 | Name the CRD prefix beside `EPIC-###`, the v2 writer as the producer, and the literal `ADR status line:` field it renders for a TI item". The ADR's own status and amendment lines (1–7) were read for context.
- PF03, `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, blob `504712df548a`, 43,953 bytes, read in full as the editorial standard.
- PF06 (Change Process Guide v2.5.4, blob `d2df157b4014`): §3.5.2.1 "Close-pack files" (forms (a) and (b) of the tracked-issue mapping, lines 2969–2985) and §3.5.4 "ADR block in the close-pack (all epics)" ("Closure override" and "No posture-only PASS"), read to cite them correctly. PF06's own drainage is T-PF06's.
- Repository facts, inspected read-only on `origin/main` `0838ba08`: `tools/qa/generate_epic_close_pack.py` exists, derives `audit/{prefix}_close_report.md` and `audit/{prefix}_MANIFEST.json` with the CRD ID as prefix (function `_derived_paths_v2`), renders `- {id} ADR status line: {adr_status}` for each tracked issue (line 3125), and refuses a duplicated or non-`TOOLING_BLOCKED` override gap with `CLOSURE_OVERRIDE_INVALID` (`_qa_coverage_v2`); `schemas/close_candidate_source.v2.json` pins the change ID to `^HDE-(?:EPIC[0-9]{3}|CRD-[0-9]{4,})$`; `schemas/epic_close_candidate_source.v1.json` exists; `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and both `.path_proof.txt` siblings exist.

Routing record: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0ebb2f80a416fb004b9a913da592d1`, identical on `main`), read in full, including "Precedence and closure controls" and "Held and deferred items". The ledger routes the work; it is not a change source.

Closure and approval evidence (verified by blob on `main` and by its decisive lines):

| Ref | Path, blob | Decisive fact read |
| --- | --- | --- |
| X10 | `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md`, `c48f77a0c220` | `decision: INITIAL_APPROVE`; reviewer Thoth; `created_at: 2026-10-12T19:39:51Z` |
| SR4 | `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`, `5a6cecc86f60` | `decision: DELTA_APPROVE`; `created_at: 2026-10-21T18:36:00Z` |
| X11 | `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md`, `2260eae17974` | `decision: CLOSE`, `state: CHANGE_CLOSED`, `decision_time: 2026-10-26T16:40:00Z`, Isis |
| X12 | `docs/ephemeral/HDE-CRD-0002-CL-20-post-closure-record-v1.0.md`, `ac60f368f6d9` | M-0 "PF10 drainage of HDE Build Notes 2.2 to 2.32 for this change": Pending; M-3 board update: Pending |
| X13 | `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md`, `d6cceaf3a019` | `verdict: PASS`; 21 checks, all `PASS` |
| X14 | `audit/HDE-CRD-0002_close_report.md`, `0bbc8050d3c1` | `- Closure decision: SATISFIED`; 34 deferral entries; a later-drain statement names "HDE Governance. Locators: 2.0.19 Close report minimal content; 9.7.7 Business Case" |

## 6. Canon and controls relied on

- PF04 (target, v2.8.7): §0.1 Header; §0.2 "HDE Build Notes reference posture (titles only)"; §0.3 Tagging convention; §0.4 Change policy; §2.0.19 (close-pack baseline artifacts, close report minimal content, canon-pointer fields, `key_outputs` shape); §9.1.1 (left unchanged); §9.1.3; §9.1.6; §9.3 and §9.3.1 (Doc-Delta entries and the Change Log grammar); §9.4 Doc-Delta template; §9.7.7 Plan approval gate; §11.2; Appendix D.0.
- HDE Build Notes v13.8.8: front matter §1 to §9 (precedence, supersession, live content, silence, operational rule) and addenda 2.1, 2.11, 2.15, 2.16, 2.17, 2.18 (this proof log is not a PF document, so it cites addendum numbers; the redline payloads do not).
- PF03 Technical Writing Best Practices: §3 (truth and source fidelity, canonical ownership, claim-state separation, structure and language, no ellipsis), §5, §6, §7, §8, §9 (PF10 cited by title only outside PF10), §11, §14.
- Change Process Guide §3.5.2.1 and §3.5.4 (supporting).
- AGENTS.md: canon-first rule; PF canon read-only; "PF documents other than PF10 never cite PF10 by section"; truncation guardrail; write destinations.

## 7. Precedence and supersession applied

- 2.18 withdraws the cost-ceiling passages of 2.11 to 2.16. No ceiling text was drafted; RL-09 states that a requirement or work unit carries no cost ceiling, and its gates follow 2.18 rule 3. The ceiling sentences of 2.15 ("A projected pass of the unit's cost ceiling returns to the Product Owner") and 2.16 ("Cost against the ceiling") are not drained.
- 2.14 narrows 2.11 rules 7 and 8 for P1 findings. Those rules drain to Plan Templates and the Change Process Guide, not to PF04, so nothing here depends on the narrowing.
- 2.17 amends 2.15: C-3's pointer clause is superseded for pointer items (resolution B), C-1 is extended by resolution A. RL-04 drains the surviving text only: `ADR status line:` for an ADR-status item, and the SATISFIED treatment of resolution A.
- 2.11's misnumbered internal cross-references were read by the rule their text describes: rule 7's "real input (rule 3)" is rule 4; the drainage table's "rule 5 disposition" and "rule 6 trigger" are rules 7 and 8.
- HDE-CRD-0002 is closed (X11 after X13), so no change is held on closure grounds. 2.1, 2.11 and 2.18 are Product Owner directions in force now and wait on no closure.

## 8. Change and disposition ledger

| Source change | Disposition | Redline or location |
| --- | --- | --- |
| A01 rule 1, scope (GCFPE downstream prompts, handoffs, relays) | Redline | RL-06 |
| A01 rule 2, the TypeSafe reading, reported as printed; Product Owner picks; pick recorded | Redline | RL-06 |
| A01 rule 3, no AI recommendation | Redline | RL-06 |
| A01 rule 4, no reading reported as not read; no substitute | Redline | RL-06 |
| A01 rule 5, provider neutrality not applied to the TypeSafe skill within scope | Redline | RL-06 (bullet 4 scopes the next paragraph's "No governance rule requires a particular AI provider, product, model or effort level") |
| A01 superseded passage §9.1.3 sentence | Redline; the sentence stays for execution surface and for other ecosystems, as 2.1 supersedes it only for GCFPE model and reasoning-level advice | RL-06, placed directly after that paragraph |
| A01 superseded passage §9.1.6 "model guidance" | Redline | RL-07 |
| A01 nonclaims (no other ecosystem, selects no model, not an approval or gate) | Redline | RL-06 bullet 5 |
| A01 GCFPE prompt and skill changes | Out of PF04 ownership; GCFPE-MGMT-10 (ledger) | none |
| A11 rule 1 (beneficiary, evidence, benefit, measure) for every requirement and work unit | Redline; the cost-ceiling field is withdrawn by 2.18 rule 1 | RL-09 |
| A11 rule 2 (what is not a business case; internal tooling) | Redline, with 2.18 rule 4's restated sentence | RL-09 |
| A11 rule 3 gates | Redline, as narrowed by 2.18 rule 3 (Specification approval blocks; IA-30 checks; PR-10 carries; the Proceed is given against it; a met business case stops) | RL-09 |
| A11 rules 4 to 8 (real inputs, emulation, finding disposition, repeated class) | Out of PF04 ownership: Plan Templates "Source-bound review authority and exact-fix limits" and Change Process Guide §1.1.4 (T-PF27, T-PF06); AGENTS.md row landed through #661 (ledger) | none |
| A11 HDE CRD Records §4.1 | Out of PF04 ownership; T-PF30.1 | none |
| A18 rules 1, 2, 3, 4 | Redline | RL-09 |
| A18 rule 5 (no recording against a ceiling) | Already represented: PF04 states no ceiling and no recording duty; a search of the baseline for "ceiling" finds only §11.2.3's `exp_ceiling_ms` (lines 4041, 4044, 4045) | none |
| A18 rule 6 (unchanged rules) | Respected; RL-09 states that the CI cost stewardship rules of §4.3.9 are unchanged | RL-09 |
| A15 AQ-1 decision, C-1, C-2, C-4, ADR status line text | Not PF04: the ADR and its owner; HDE Schemas and Artifacts; the Change Process Guide | none |
| A15 C-3 literal canon-pointer fields | Redline for the surviving form (`ADR status line:`), with 2.17 resolution B | RL-04 |
| A15 close-run family | Not PF04: the ADR table routes it to HDE Schemas and Artifacts §8.17 and Glow QA Guide §3.4.3 (T-PF12, T-PF19) | none |
| A15, A16, A17 ADR canon table, HDE Governance row (X03): CRD prefix beside `EPIC-###` | Redline | RL-01 (path-of-record), RL-02 (close report), RL-03 (manifest pointer), RL-05 (`key_outputs` shape), RL-11 (Appendix D.0) |
| Same row: the v2 writer as producer | Redline | RL-01 (Producer item); RL-11 points to it |
| Same row: the literal `ADR status line:` field for a TI item | Redline | RL-04 |
| A16 LR7-O9 (TI closed as satisfied cannot be expressed in v2; HDE Governance §2.0.19 row) | Redline, as 2.17 resolution B | RL-04 |
| A16 other drainage (Change Process Guide §3.5.2, §3.5.2.1; HDE Schemas and Artifacts §1.2; Glow QA Guide) | Not PF04; T-PF06, T-PF12, T-PF19 | none |
| A17 resolution A into "Close report minimal content" | Redline | RL-04 |
| A17 resolution B into the canon-pointer fields | Redline | RL-04 |
| A17 the ADR revision | Not PF; the ADR's owner (ledger: N, A34 D-9 and D-10) | none |
| A17 Change Process Guide §3.5.4 and §3.5.2.1 | Not PF04; T-PF06 | none |
| PF04 §9.3 and §9.3.1 change-log duty | Redline (the target's own rule) | RL-08 |
| TW-DRAIN-10 marker rule, §11.2 "draft" label | Redline (hygiene) | RL-10 |
| H-06, the §9.1.1 review-chain entry | Held; untouched. No redline touches §9.1.1 | none |

No source change is left blocked or unaccounted for.

## 9. Interpretations and constraints

- RL-06 is placed as a new paragraph and list directly after the §9.1.3 sentence that 2.1 supersedes, rather than replacing it, because 2.1 supersedes the sentence only for GCFPE model and reasoning-level advice; execution-surface advice and other ecosystems keep it.
- RL-09 includes 2.11 rule 3's gates as 2.18 narrows them. The drainage row names "rules 1 and 2" for HDE Governance §9.7.7; §9.7.7 is PF04's plan approval gate and already carries the Epic Business Case review posture, so the gate that blocks approval without a business case belongs beside it. `IA-30` and `PR-10` are the GCFPE stage codes the source uses; the Implementation Plan review (IA-30, from 2.16's "review v1.1 (IA-30 INITIAL_APPROVE)") and "PR-10 — Create PR Work-Unit Instructions" are named with them.
- The Epic Specification Business Case section (§9.7.7, including its fenced "Content constraints" and "Review posture" block) is unchanged. The fence around that block is a pre-existing formatting artifact; removing it is not authorized hygiene, so RL-09 is inserted after it.
- `HDE-CRD-NNNN` follows the ADR's notation; "zero-padded to at least four digits" follows the v2 schema pattern `CRD-[0-9]{4,}`.
- Payloads name HDE Build Notes by title only and cite no addendum number (PF04 §0.2; AGENTS.md; PF03 §3 and §9). The validator rejects any payload containing "PF10" or "addendum".
- Hygiene scan (TW-DRAIN-10 marker rule) over the whole baseline for `TODO`, `FIXME`, `XXX`, `TBD`, "fill later", "placeholder", "Draft", "draft", "Editor", and ellipses:
  - Removed: §11.2 line 4016 "**Scope (normative, draft).**" (RL-10). §0.3 makes `[Speculative]` the section's status tag and no canon requires "draft" there.
  - Kept, canon rule text about placeholders, editorial changes or the doc-delta "draft/staging surface" artifact name: lines 116 ("Editorial vs normative"), 526, 628, 629, 631, 634, 635, 878, 1160, 1181, 1217, 1219, 1221, 1751, 1855, 2022, 2060, 2194, 2459 ("Asset Draft Packs"), 2563, 2564, 2572, 2586 ("Draft / binding surface" field of the existing entry), 2727, 2741, 2758, 2824, 2924, 3102, 3108, 3112, 3146, 3168, 3336, 3480, 3500, 3522.
  - Kept, template: §9.4 (lines 2617–2686), including its `GOV-YYYYMMDD-\\` and `\\` fields, its "Draft / binding surface" field (line 2631) and `> 2\) ...`.
  - Kept, normative maintenance rules, not notes to a writer: §15.2 "Keep this list short and actionable" and "Update this list as items close"; Appendix A.6 and B "Maintenance rule (MUST)".
- Observations outside this task, not drafted (no source authorizes them, and repair would need text the sources do not supply):
  - Ellipses inside code spans on lines 736, 743, 793, 797, 801, 872, 884, 2367, 3163, 3164, 3193, 3200, against PF03 §3's prohibition.
  - Damaged value notation from an earlier export: line 749 `audit/qa/\\/qa\_step\_logs\_manifest.json.path\_proof.txt` (the adjacent line 746 uses `<epic-id>`); line 3604 `ETag: "\\"`; line 3606 `Content-Length: \\`.
  - Line 3727: "**nterim auth posture**" (missing "I").
  - These are for the Product Owner to direct; the redlines leave them as they are.

## 10. Document-control provenance for TW-APPLY-10

- Native header schema (§0.1 Header, lines 5–10): `**Title:**`, `**Version:**`, `**Status:**`, `**Effective date:**` (format `YYYY-MM-DD`), `**Last Update Gate:**`, `**Invocation tag:**`; each line ends with two spaces except the last.
- Sources that justified the update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, HDE Build Notes version 13.8.8. Gate form: `BN 13.8.8`. X03 (the ADR) is supporting reading under the ledger, not a change source, so it is not a gate source. No other source.
- Version scheme: dotted numeric `v2.8.7`; one bump of the final component gives `v2.8.8`.
- The change-history entry the target's rules require is RL-08 (§9.3.1 Change Log), naming `v2.8.8` and the preparation date `2026-10-26` as its "Date / Author" date. TW-APPLY-10 derives the header fields; RL-08 must agree with them.
- No header redline is included. Status `Canon` is not stale. No internal restatement of the document's own version or date exists outside the header: the "v2.8.7" and "2026-10-09" in the §9.3.1 entry `GOV-20261009-gtwpe-pf04` are that entry's history and are not restatements.

## 11. Validation performed

Producer validation ran twice: on the in-memory batch against the unchanged baseline (`rl_validate.py`), then on the saved redlines file by an independent parser (`apply_from_md.py`) that reads only the saved Markdown, checks every literal's byte length and SHA-256, and resolves each operation against the baseline. Both scripts are in the session scratchpad and are not committed.

| ID | Operation | Baseline location | Expected | Observed | Old block or anchors (bytes, SHA-256 prefix) | Inserted or replacement (bytes, SHA-256 prefix) |
| --- | --- | --- | --- | --- | --- | --- |
| RL-01 | INSERT | gap after line 891, byte 127135 | 1 gap | BEFORE 1, AFTER 1, contiguous 1 | BEFORE 62 B `ce07f08dbf0b`; AFTER 67 B `312b3e0e983b` | 571 B, `f240faf11b01` |
| RL-02 | REPLACE | line 895, bytes 127464–127601 | 1 block | 1 | old 137 B, `43aa94418d67` | new 208 B, `e299cce9080a` |
| RL-03 | REPLACE | line 905, bytes 130290–130384 | 1 block | 1 | old 94 B, `6773554a6928` | new 144 B, `083c5f561bee` |
| RL-04 | INSERT | gap after line 910, byte 130928 | 1 gap | BEFORE 1, AFTER 1, contiguous 1 | BEFORE 79 B `8e4f490dd538`; AFTER 113 B `816fada86ae0` | 1120 B, `b80a2f7e439d` |
| RL-05 | REPLACE | line 975, bytes 147801–147881 | 1 block | 1 | old 80 B, `3f9174d6822b` | new 156 B, `4cf6ad4829ff` |
| RL-06 | INSERT | gap after line 2454, byte 319407 | 1 gap | BEFORE 1, AFTER 1, contiguous 1 | BEFORE 50 B `d3a0a9c5efb9`; AFTER 43 B `8e2e34740f2b` | 1316 B, `5a94125091f1` |
| RL-07 | REPLACE | line 2505, bytes 331764–331833 | 1 block | 1 | old 69 B, `7d728735d046` | new 121 B, `10d40893f004` |
| RL-08 | INSERT | gap after line 2612, byte 349634 | 1 gap | BEFORE 1, AFTER 1, contiguous 1 | BEFORE 447 B `0fc70cc46cc9`; AFTER 57 B `66c397ea614c` | 4098 B, `317eb0563b62` |
| RL-09 | INSERT | gap after line 2826, byte 368599 | 1 gap | BEFORE 1, AFTER 1, contiguous 1 | BEFORE 74 B `9a2f4fa2f7a1`; AFTER 117 B `4c45a9e4fc59` | 1825 B, `d28d89437de8` |
| RL-10 | REPLACE | line 4016, bytes 518843–518872 | 1 block | 1 | old 29 B, `8943e11382e6` | new 22 B, `218632be990f` |
| RL-11 | INSERT | gap after line 4517, byte 561319 | 1 gap | BEFORE 1, AFTER 1, contiguous 1 | BEFORE 49 B `ff0328d99058`; AFTER 53 B `c7052d1213b6` | 412 B, `4e00b6be2585` |

- Dialect: only `INSERT` and `REPLACE`; no `FIND AND REPLACE`, so the RL-045 rule does not arise.
- Conflicts: every pair of operations was checked on original-bound spans and gaps (intersecting spans, two insertions at one gap, an insertion at or inside a replaced span). None found.
- One-pass simulation (descending offsets, no rematching) gives a content-only result of 580,194 bytes, SHA-256 `8c178d234a91db9b64954357bc4231b0bd9d05339b991094991d86ebb79662e4`, with every untouched baseline interval preserved in order. The saved file's independent simulation is byte-identical to it. This result excludes the header fields that TW-APPLY-10 derives.
- Each payload was checked for the prohibited ellipsis forms and for PF10 locators; none occurs.
- One self-correction before READY: the first validated batch had 10 operations. Re-reading the TW-DRAIN-10 marker rule against the §11.2 "draft" label led to RL-10; the Appendix D.0 insertion was renumbered RL-11, the change-log entry's targets and summary were updated, and the whole batch was validated again from the start. No earlier batch was saved to the repository.

## 12. Dependencies, limitations and remaining work

- No blocking dependency. All required sources were available and read completely.
- Drafting is limited to PF04's ownership. Related drainage in other documents stays with T-PF06, T-PF12, T-PF14, T-PF19, T-PF27 and T-PF30.1; GCFPE prompt and skill wording stays with GCFPE-MGMT-10; the ADR revision stays with its owner.
- The `EPIC-###` example in §9.7.9 (line 2938, "for example, `audit/EPIC-###_MANIFEST.json`") is left as an example; only the loci the ADR row names were changed.
- The observations in §9 are recorded, not fixed.

## 13. Outcome and next step

- Preparation outcome: `READY`.
- Save completeness: recorded in §14 after read-back.
- Next step: TW-APPLY-10 — Apply Validated Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b), in this same session as Nathan's handoff authorizes, with the baseline above, this package, ledger rows A01, A11, A15, A16, A17, A18 (X03), branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, outputs `pf04/PF04-from-v2.8.7.md` and `pf04/PF04-from-v2.8.7.proof-log.md`, or `pf04/apply-diagnostic-PF04-from-v2.8.7.md` on failure.
- Correction route: a TW-APPLY-10 diagnostic returns to this preparer (this session, under TW-DRAIN-10 100926.1), which issues a complete corrected package with a new run identity.

## 14. Save verification receipt

Recorded after both files were saved and read back in full on 2026-10-26:

- `redlines-PF04-from-v2.8.7.md`: 33,229 bytes, 485 lines, SHA-256 `f176994249c55726ab66ab2a56b32f4fe458807946db06b85d5a1d91fadda632`, ends with `END OF REDLINES`. The repository copy was parsed again by the independent parser: 11 operations, every literal's length and SHA-256 matching, every count 1, no conflict.
- This proof log: read back in full; its corrections (the hygiene line list, two line references in §9 and the §12 example locus) were made before this receipt. Its own hash is not recorded here.
- Save completeness: `COMPLETE_PACKAGE`. The commit that holds the pair is given in the final response and in the ledger's T-PF04 Completion cell.
