# PF07 redlines proof log, revision r2 — gtwpe-20261101-pf10-v14-0-5 — T-18

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF07/PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md` (43 `REPLACE` redlines, RL-01 to RL-43, ending `END OF REDLINES`) |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF07/PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.r2.proof-log.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-18/drain-r2` |
| Supersedes | Package `drain-r1` (`PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.md` and its `.proof-log.md`, commit `19a92a9`), which stays in place and in git history. RL-01 to RL-04 are carried byte-identical, blocks included. RL-05 to RL-43 are new. |
| Why a revision | After drain-r1 and apply-r1 were reported, Nathan directed, on 2026-11-02 in this session: "you can fix the defects and discrepancies you noticed". The defects are observations O-1 to O-9 in the drain-r1 proof log §8. That direction is the authorization TW-DRAIN-10 requires for hygiene and for changes outside the selected sources ("Nathan's, given in the handoff or an accessible file"). This log records it. |
| Preparer | TW-DRAIN-10 "Prepare PF Document Redlines", Prompt Version 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff` (last edited 2026-10-09T11:05:22Z), fetched live again at the start of this revision |
| Session | The Claude Code document session Nathan started for T-18 on 2026-11-02, the same session as drain-r1 and apply-r1. No subagent, reviewer or other session was used. |
| Preparation outcome | `READY` |
| Save outcome | Recorded in §10 after read-back |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`; draft PR amthorn78/glow-hdengine-v2#826 (open) |

## 2. Sources and inputs

| Role | Identity |
| :---- | :---- |
| Target (original) | `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.4.md`, title `PF07-Canon-Glow-Infrastructure`, v2.3.4, git blob `60fd3f0b3feff007491dc7add29a9c4491cbdf95`, SHA-256 `9e00712a3af2c1b498b5dddf5ada35c72b44952293d3b73ec3915cbba586d790`, 99,393 bytes, 1,443 LF characters (1,444 lines). Read completely in drain-r1 (windows listed in its proof log §2). The blob is unchanged from `e2b7427` to `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, so that full read is reused. |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`. The drain-r1 selected units (2.1 l.205–224, l.277–396, l.491–516; 2.8 l.1048–1145; 2.15 l.1650–1868) plus 2.1 D-1, l.225–276, read completely for O-1. Reading D-1 and drafting RL-37 under row C-01 extends T-18's ledger scope by Nathan's direction. |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, v1.8.8, blob `504712df548a02f3aa4e7b8c37027385e46a3878`, read completely in drain-r1 |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `a3632c0`; task T-18 (§8); rows C-02, C-03, C-17, C-18, C-26, and C-01 for O-1 |
| Authorization | Nathan, 2026-11-02, this session (quoted in §1) |

Supporting reading for the new redlines (not sources; no edit scope beyond PF07):

- PF06 Change Process Guide v2.5.5 front matter on `main`: in-document title `PF06-Canon-Change-Process-Guide` (RL-06, RL-07, RL-09, RL-18, RL-19, RL-42).
- PF05 HDE-CLI-API-Vendor-Ref v2.5.4 on `main`: title `PF05-Canon-HDE-CLI-API-Vendor-Ref` (RL-23). Reader v2 is selected by `POST /api/reader?v=2` (l.2202), and the production blueprint serves `?v=1` and `?v=2` (l.2420) (RL-21).
- Repository at `84d6d1c`, read-only (identical to `e2b7427` for `engine/`, `adapter/`, `docs/ENDPOINTS_CATALOG.json` and `docs/pfcanon/`):
  - `adapter/http_reader.py` l.380 `_READER_VERSIONS = {"1": "v1", "2": "v2"}`, and the Endpoint Catalog's `/api/reader` POST entry "Production Reader (POST; v=1 Reader v1, v=2 Reader v2)" (RL-21);
  - `engine/bodygraph/vendor_audit.py` l.140 fixes the event `command` to `bg:resolve`, and `engine/cli/main.py` l.53 accepts `--allow-prod-vendor` only for `bg:resolve --source vendor` (RL-37).
- PF07's own rules, cited where each redline relies on them: §0 l.23; §5.1 l.729; §7.0 l.930; §8.1 l.1144–1150; §10.5 l.1438; the `{redacted}` form at l.1269–1271; `<base_url>` at l.1227.

## 3. Coverage

- Target: complete (reused drain-r1 read; same verified blob).
- Selected source units: complete, as drain-r1, plus D-1 for O-1.
- Observations: all nine drain-r1 observations are addressed: O-1 to O-9 each have one or more redlines (§5).
- The dispositions for C-02, C-03, C-17, C-18, C-19, C-26 and C-06 are as in the drain-r1 proof log §5, except that O-1 (C-01), O-2 and O-7 (both C-26) are now actionable redlines rather than observations. The `/internal/version` text keeps its no-change disposition except the cross-reference fix in RL-10.

## 4. Redlines carried from drain-r1

| ID | Location | Basis |
| :---- | :---- | :---- |
| RL-01 | §2.4 l.352 | C-02, 2.1 D-2 |
| RL-02 | §2.5 l.372 | C-26, 2.15 R-1, R-2, R-6 |
| RL-03 | §2.8 l.538 | C-17, C-18; 2.15 R-3 wording |
| RL-04 | §8.1 l.1136–1137 | C-17, C-18 |

Their OLD and NEW literals, rationales and metadata are unchanged from drain-r1 (the builder checks each carried block against the r1 file's SHA-256 `4562cef91fdfb9e202bd1989d46f44fe8244438b58bb7d3d9d10e3839e3078c3` and against the r2 definitions).

## 5. New redlines, by observation

| Observation (drain-r1 §8) | Redlines | Original lines | Fix | Basis |
| :---- | :---- | :---- | :---- | :---- |
| O-1 D-1 and the audit-path key | RL-37 | 1278 | The key names the override's audit sink, routes command coverage to HDE-CLI-API-Vendor-Ref, and states that in the checked-in code only `bg:resolve --source vendor` writes events. | 2.1 D-1 l.229–241; item 9 open (l.506); code at `84d6d1c` |
| O-2 Reader v2 route | RL-21 | 648 | "Reader route posture" names `POST /api/reader?v=1` (Reader v1) and `POST /api/reader?v=2` (Reader v2); the rest of the line is unchanged. | 2.15 R-1 l.1719; PF05 l.2202, l.2420 (supporting); code and catalog |
| O-3 Stale §10.5 pointers | RL-10, RL-12 | 215, 228 | The `/internal/version` evidence pointer and the "Ops/QA audit roots" pointer now say where PF07 records QA roots and that other roots, families and paths are HDE-Schemas & Artifacts'. | PF07 §10.5 l.1438 |
| O-4 Retired-key value in §2.4 | RL-15 | 328 | `DB_BRIDGE_URL=<value>` becomes the retired-key posture line, with no value. | PF07 §7.0 l.930, §8.1 l.1144–1150 |
| O-5 Malformed headings | RL-13, RL-14, RL-16, RL-20, RL-25, RL-26, RL-29 to RL-34, RL-39 to RL-41 | 294, 320, 348, 597–599, 785, 808, 846, 905, 986, 1009, 1179, 1198–1200, 1356, 1415, 1423 | Fourteen indented section headings lose their two-space indent. Three list items marked as headings (`* ##`) become plain bullets. | PF03 §7 (formatting repair) and §8 (heading hierarchy) |
| O-6 Ellipses | RL-05, RL-08, RL-11, RL-17, RL-22, RL-24, RL-35, RL-38 (and RL-03 from r1) | 23, 108, 220, 459, 723, 731, 1239, 1336 (538) | Each `audit/qa/<epic-id>/...` becomes the root form plus the CRD root; `Bearer …` becomes `Bearer {redacted}`; `DEV_SAMPLER_URL=...` becomes `DEV_SAMPLER_URL=<url>`; `/narratives/<pack_sha>/...` becomes the prefix `/narratives/<pack_sha>/`. | PF03 §3 "Structure and language" and §13; 2.8 decision 3 for the CRD root |
| O-7 Closed-rails harness called Live QA | RL-27, RL-28, RL-36 | 816, 819, 1243 | The EPIC-019 D3 sampler harness is described as closed-rails sampler QA. Its file path and the EPIC-019 D6 vendor Live QA names are unchanged. | 2.15 R-3 l.1755–1759 |
| O-8 §0 against §10.5 | RL-43 | 1438 | §10.5 names the canonical QA evidence root patterns (§2.8, §8.1) as the exception to "PF07 owns no evidence root". Layout, families and paths stay with their owners. | PF07 §0 l.23 |
| O-9 Stale PF06 title, PF05 variant | RL-06, RL-07, RL-09, RL-18, RL-19, RL-42; RL-23 | 42, 87, 135, 461, 507, 1429; 725 | `Epic-Process-Guide` becomes `Change-Process-Guide` (and `PF06-Canon-Change-Process-Guide`); "Epic Process" becomes "Change Process"; `HDE-CLI API Vendor Ref` becomes `HDE-CLI-API-Vendor-Ref`. | PF06 and PF05 in-document titles; PF03 §3 |

Each redline's full rationale is in the redlines file. RL-23 fixes a variant found while checking O-9's titles. It is the same class of defect, and it is the only other variant PF07 has.

## 6. Constraints and interpretations

- No new redline records 2.1 behavior as delivered. RL-37 states D-1's coverage only as HDE-CLI-API-Vendor-Ref's, and states the current single writer as a code fact.
- RL-21 adds only the route names. Bytes, shapes and eligibility stay with HDE-CLI-API-Vendor-Ref and HDE-Governance.
- RL-15 removes a recorded URL value for a retired key. PF07's own §8.1 rule ("report key names only and never values") requires that removal; the key's history stays in §8.1's retired-key list.
- RL-43 resolves the §0 against §10.5 tension in favor of §0, PF07's scope block, which the handoff names as the scope anchor. The redline adds a qualifier and takes no ownership away from PF12 or PF19.
- The `TBD` and `OPEN/TBD` values (119) and PF07's no-guessing rules stay. They are canon-required gap values (drain-r1 proof log §6).
- Last Update Gate source: still only `PF10-HDE-Build-Notes-v14.0.5.md`. Nathan's direction is an authorization, not a source file. PF05, PF06 and PF07's own rules are supporting reading.
- The document-control fields remain Apply's. PF07 has no change log, so no history entry is needed.

## 7. Newly noticed, not changed (for Nathan)

- Four horizontal rules indented under list items (l.837, l.1161, l.1173, l.1365), and an empty blockquote line before the §5.3 note (l.858). These are formatting quirks of the same family as O-5, but they were not in the reported list, so they are left for your decision.
- PF07 wraps every heading in bold, which PF03 §8 discourages. Headings are protected text, so they are unchanged.
- PF07 writes PF12's title as "HDE-Schemas & Artifacts". PF12's in-document title is `PF12-Canon-HDE-Schemas-and-Artifacts`, and HDE Build Notes 2.8 reads `&` as `and` when it resolves titles, so the form resolves; it is unchanged.

## 8. Producer validation

The batch was validated against the unchanged original before the file was written, and again against the saved file with the independent parser used in drain-r1. That parser reads each block's operation, expected count and two four-backtick literals.

| ID | Original character span | Expected / observed | | ID | Original character span | Expected / observed |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-05 | [691, 789) | 1 / 1 | | RL-25 | [54802, 54865) | 1 / 1 |
| RL-06 | [2343, 2475) | 1 / 1 | | RL-26 | [56848, 56925) | 1 / 1 |
| RL-07 | [10997, 11030) | 1 / 1 | | RL-27 | [57567, 57922) | 1 / 1 |
| RL-08 | [11704, 11877) | 1 / 1 | | RL-28 | [57973, 58281) | 1 / 1 |
| RL-09 | [12841, 12901) | 1 / 1 | | RL-29 | [59965, 60010) | 1 / 1 |
| RL-10 | [18700, 19042) | 1 / 1 | | RL-30 | [63145, 63179) | 1 / 1 |
| RL-11 | [19450, 19782) | 1 / 1 | | RL-31 | [67214, 67267) | 1 / 1 |
| RL-12 | [20078, 20181) | 1 / 1 | | RL-32 | [68559, 68611) | 1 / 1 |
| RL-13 | [23356, 23392) | 1 / 1 | | RL-33 | [77359, 77550) | 1 / 1 |
| RL-14 | [23831, 23863) | 1 / 1 | | RL-34 | [79362, 79425) | 1 / 1 |
| RL-15 | [24005, 24078) | 1 / 1 | | RL-35 | [81868, 82039) | 1 / 1 |
| RL-16 | [24714, 24756) | 1 / 1 | | RL-36 | [82083, 82346) | 1 / 1 |
| RL-01 | [24848, 24973) | 1 / 1 | | RL-37 | [86729, 86948) | 1 / 1 |
| RL-02 | [26311, 27156) | 1 / 1 | | RL-04 | [75300, 75379) | 1 / 1 |
| RL-17 | [31398, 31582) | 1 / 1 | | RL-38 | [91956, 92038) | 1 / 1 |
| RL-18 | [31584, 31985) | 1 / 1 | | RL-39 | [93908, 93928) | 1 / 1 |
| RL-19 | [36469, 36857) | 1 / 1 | | RL-40 | [96743, 96795) | 1 / 1 |
| RL-03 | [39539, 39677) | 1 / 1 | | RL-41 | [97251, 97289) | 1 / 1 |
| RL-20 | [43572, 43813) | 1 / 1 | | RL-42 | [97596, 97779) | 1 / 1 |
| RL-21 | [46728, 47400) | 1 / 1 | | RL-43 | [98029, 98519) | 1 / 1 |
| RL-22 | [51440, 51556) | 1 / 1 | | | | |
| RL-23 | [51558, 51879) | 1 / 1 | | | | |
| RL-24 | [52473, 52646) | 1 / 1 | | | | |

- Every OLD is one or more whole original lines and occurs exactly once. All 43 spans are disjoint; the closest pair, RL-17 and RL-18 (l.459 and l.461), has two characters between them. No `FIND_AND_REPLACE` is used, so the RL-045 rule does not apply.
- Every section-path segment matches exactly one complete original line. For a redline whose OLD is a heading line, the path ends at that heading's parent.
- Simulated one-pass application: 101,233 bytes, 1,446 LF characters, SHA-256 `642c5c1aff0a4c671120f58b82c3a68a400a311851d250ab6d5dbe35b7ea098a`. The original's last line still has no final LF.
- Result checks:
  - ellipses: 0 ASCII three-period forms and 0 U+2026, against 8 and 1 in the original;
  - indented headings 0, and no `* ##` list headings remain;
  - line-start headings: 83, which is the original's 69 plus the 14 restored;
  - `Epic-Process`, `Epic Process`, `CLI API Vendor`, `DB_BRIDGE_URL=` and "Reader v1 route posture" all absent;
  - `TBD` 119 and `placeholder`/`Placeholder` 3, both unchanged, with no `TODO`, `FIXME`, `Draft` or `Proposed`.
- Payload scan: no four-backtick run, no HDE Build Notes addendum number or version, no model identifier.
- Corrections before READY, all to the saved r2 file and all followed by whole-batch revalidation with the same spans and digest:
  1. Section paths for heading-line edits first ended at a sibling heading. They now end at the parent (RL-13, RL-14, RL-16, RL-25, RL-26, RL-30 to RL-32, RL-34, RL-39 to RL-41).
  2. The ledger-row field "hygiene" was replaced by "None; Nathan-authorized fix" or the row it supports.
  3. RL-39's rationale was corrected: l.1356 follows a paragraph, not a list item.

## 9. Outside dependencies

None blocks this package. No Product Owner decision is needed beyond the direction quoted in §1. §7 lists items left for Nathan's decision.

## 10. Save verification

Recorded after both files were written and read back in full, before commit.

| File | Bytes | SHA-256 | Read back |
| :---- | :---- | :---- | :---- |
| `PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md` | 50,674 | `6b9fe687a715b69b7e0ace84f92ac342b2a54041d62918aab9af5cb4bb95443e` | Complete, 1,112 lines; 43 RL blocks; the last line is `END OF REDLINES`, followed by one LF |
| This proof log | Not self-hashed | Not self-hashed | Complete, after this receipt was added |

Save outcome: `COMPLETE_PACKAGE`. Preparation outcome: `READY`. Next step: TW-APPLY-10 100926.1 in this session, fetched live, against the unchanged original and this package. Its output takes the file name `PF07-Canon-Glow-Infrastructure-v2.3.5.md` again, since v2.3.4 bumps once to v2.3.5, and supersedes the apply-r1 output at `6cf30b8`, as the T-08 r2 application did for PF29.
