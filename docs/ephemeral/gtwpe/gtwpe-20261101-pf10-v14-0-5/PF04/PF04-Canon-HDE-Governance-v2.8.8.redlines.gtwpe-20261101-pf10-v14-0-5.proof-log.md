# Proof log — PF04-Canon-HDE-Governance v2.8.8 redlines — gtwpe-20261101-pf10-v14-0-5 (T-01)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.8.redlines.gtwpe-20261101-pf10-v14-0-5.md` (52,073 bytes; SHA-256 `992b46396e5be5586645135f63e39521fc963f8da633b464d02323bb0cc31958`) |
| This log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.8.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/drain-1`, prepared 2026-11-02 |
| Preparation outcome | `READY` |
| Save completeness | Recorded in §10 after read-back. |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff` (page last edited 2026-10-09T11:05:22.094Z), fetched live at the start of this step |
| Originating preparer | The executing document agent in the Claude Code session that Nathan started for T-01 (session `session_01Q789tyrM8bruo2RGNCMLM8`). No subagent, reviewer or other session took part. |
| Handoff | Nathan's GTWPE document-session handoff for T-01, which authorizes TW-DRAIN-10 then, on a `READY` / `COMPLETE_PACKAGE` result, TW-APPLY-10 in this session |
| Correction route | An Apply diagnostic returns to this preparer in this session; a corrected package takes a new run identity (`drain-2`) |

## 2. Sources, inputs and roles

| Input | Identity | Role and timestamp |
| :---- | :---- | :---- |
| Original target | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md`; in-document title `PF04-Canon-HDE-Governance`; v2.8.8; status Canon; effective 2026-10-26; Last Update Gate `BN 13.8.8`; invocation tag `INV-f2ac55d77ce9aacc`; git blob `0c3ce100f9429435bce8e021f36e405120159e4a`; SHA-256 `7a50dbe3d4eb67a1d01bab89e55d6ed0c0570258b5f7b9c4251626277c76ee72`; 580,196 bytes; 4,748 LF-terminated lines; no CR byte | Current authoritative PF04, read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56` (the ledger baseline). `origin/main` advanced to `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` during the session with no change under `docs/pfcanon/` (`git diff --stat e2b7427 84d6d1c -- docs/pfcanon/` empty), so the target and source identities are unchanged. |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`; HDE Build Notes v14.0.5, effective 2026.11.01; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; one unlettered logical base version | Controlling source for the selected units, read at `e2b7427` |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` (43,953 bytes, 633 lines; SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462`) | Read in full as the common editorial standard. PF03 §8 defers to an operator-supplied redline format; TW-DRAIN-10's literal fenced-payload contract is that format. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064` | Routing only; not a change source or a Last Update Gate. Task T-01; rows C-03, C-04, C-05, C-07, C-08, C-17, C-18, C-26, C-29; supporting C-06, C-20, C-30; held H-07. |
| Repository facts | `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, read only | Bounded inspection of the paths named in RL-04, RL-06, RL-11, RL-13 and RL-14 (§7) |

Branch: `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826 (open when this step began), fast-forwarded to `39981112f1b96c651bb3bbb202005c78e6d6c2bf` before saving. Other sessions' commits on the branch (T-02, T-03, T-09) touch only their own directories and the T-09 ledger row.

## 3. Coverage

Target. PF04 was read completely in eleven contiguous windows, recorded with byte counts:

| Lines | Bytes |
| :---- | ----: |
| 1–474 | 55,035 |
| 475–760 | 55,267 |
| 761–1129 | 55,097 |
| 1130–1609 | 55,060 |
| 1610–2133 | 55,078 |
| 2134–2500 | 55,119 |
| 2501–2907 | 55,019 |
| 2908–3266 | 55,131 |
| 3267–3757 | 55,015 |
| 3758–4342 | 55,112 |
| 4343–4748 | 29,263 |
| Total | 580,196 (equals the file size) |

Selected source units, each read in full:

| Unit | Lines | Bytes read | Ledger rows |
| :---- | :---- | ----: | :---- |
| 2.1 context, D-1 to D-3 window (D-3 is 345–396) | 205–396 | 18,333 | C-03, C-06 |
| 2.1 D-4, D-5 and context; 2.2 status, R-1, R-2 | 397–546 | 12,851 | C-04, C-05, C-06, C-07, C-08 |
| 2.8 (decisions 1–9, stated limits, drainage table and note; amendment) | 1048–1145 | 36,158 | C-17, C-18 (supporting 1048–1062, 1107–1110, 1128–1145) |
| 2.15 status, R-1 to R-6 | 1650–1868 | 15,246 | C-26 (supporting 1805–1868) |
| 2.16 status, R-1, R-2 (and R-3 onward) | 1869–1977 | 8,416 | C-29 (supporting 1940–1976, C-30) |

2.1 D-1 and D-2 (225–344) were read as part of the first window; they belong to other tasks (T-02, T-05, T-07, T-08) and are not drained here. Supporting reading only: 2.9 (1146–1229, 26,466 bytes), for close-tooling repair B-1 to B-4 (C-20). The source ends with the authored `\<eof\>` marker after line 1976.

## 4. Change and disposition ledger

| Row | Source change | Disposition | Target locations |
| :---- | :---- | :---- | :---- |
| C-03 | 2.1 D-3: the compat namespace is a dev/admin surface; gate order; no credential while gated; wider-exposure rule; accepted residual risk | Actionable: RL-05 (§4.1.4). §8.3 unchanged, as D-3 states. PF05 §5.5 and PF29 §16 belong to T-02 and T-08. | §4.1.4 block "Dev/admin APP\_ENV gating" (lines 1300–1312) |
| C-04 | 2.1 D-4: `--log-path` bound of the sanity pipeline | Actionable: RL-06 (§4.1.8 "Sanity log artifact"). The attestation-builder rules go to PF12 §6.2.1 and PF14 §27.3 and §27.5 (T-04, T-05). | §4.1.8 lines 1386–1394 |
| C-05 | 2.1 D-5: governed gate check rows carry closed tokens and repository-relative paths only | Actionable: RL-01 (§2.0.10 `LOGS_KEYS_ONLY_OK`). §6.3.2 unchanged, as D-5 states. PF12 §1.2 and the Evidence Catalog entry belong to T-04. | §2.0.10 line 584 |
| C-06 | 2.1 status, nonclaims, item 9 | Supporting. The drafted rules state requirements only and claim no implementation; item 9 is H-10. | — |
| C-07 | 2.2 R-1: planning documents serve planning only | Actionable: RL-08 (§9.1.2) and RL-09 (§9.1.3 pointer). | §9.1.2 line 2442; §9.1.3 line 2452 |
| C-08 | 2.2 R-2: PF-Canon is resolved by stable identity, never by version | Actionable: RL-07 (§9.1.2). §9.1.3 needs no change: it pins no PF file name or version. Already consistent: §9.1.2 line 2444 (board links must not depend on version-numbered PF filenames) and §9.1.6 line 2528 (no version-pinned external filenames). | §9.1.2 line 2438 |
| C-17 | 2.8 decisions and the HDE Governance drainage row (line 1121): CRD prefix beside `EPIC-###`, the v2 writer as producer, the literal `ADR status line:` field for a TI item | Already represented (drained by v2.8.8, `GOV-20261026-gtwpe-pf04`, lines 2627–2665): CRD prefix and producer at lines 892–894; close report CRD prefix at 898 and 908; `ADR status line:` rendering at 914; closure override at 915; key\_outputs CRD prefix at 980; Appendix D.0 CRD pair and producer pointer at 4585–4591; key\_outputs minimum routed at 894. Decision 7's consequence for the close report is carried with C-18 in RL-03. Other 2.8 rows belong to T-03, T-04, T-05 and T-06. | Lines 887–994, 4574–4594 |
| C-18 | 2.8 amendment of 2026-11-01 (line 1060), unapportioned (line 1127): Epic close-run family; Epic tracked-issue ID form | Actionable, PF04's share as decided in §5: RL-02 (tracked-issue ID forms in the TI item) and RL-03 (the close report's same-run evidence pointer to the close-run family). Not PF04's share: the family's path and status (PF12), publication interface (PF14) and same-run evidence home (Change Process Guide, Glow QA Guide). Appendix D.0 lists only the close-pack pair and needs no change. | Lines 914, 977–978 |
| C-20 | 2.9 close-tooling repair B-1 to B-4 | Supporting for RL-02 and RL-03. CCR-5 is H-06. | — |
| C-26 | 2.15 R-1, R-2, R-5 into §3.4 (dependencies line 1846) | Actionable: RL-04. R-6 is already represented and is carried into the RL-04 text (execution controls at the paragraph beginning "Each live step", the nonclaims paragraph and the secret-safety paragraph at line 1208; delegated execution at line 1184). R-3 and R-4 belong to T-03, T-06 and T-07; RL-04 routes stage enforcement to them by title. The HDE-EPIC041 disposition (C-27) belongs to T-10. | §3.4 lines 1192–1200 |
| C-29 | 2.16 R-1 and R-2 into §12.2, B.2, D.1, D.3 | Actionable: RL-11, RL-12, RL-13, RL-14. The retired entries occur only at lines 4207, 4208, 4451–4453, 4602–4604, 4617 and 4618 (exact search). The §12.1 pass conditions are unchanged, as 2.16 states. | §12.2 lines 4206–4208; B.2 4450–4453; D.1 4602–4604; D.3 4617–4618 |
| C-30 | 2.16 R-3: SYN-A and SYN-B stored and registered; 2.15's "not yet" bullets superseded | Supporting. RL-04 describes SYN-A and SYN-B as kept fixtures and drafts no "not yet stored" text. | — |
| — | PF04 §9.3: every normative change adds a §9.3.1 entry | Actionable: RL-10, a `NON_EPIC` entry `GOV-20261102-gtwpe-pf04` for v2.8.9 | §9.3.1, after line 2665 |

Held, not drafted:

* H-07, CCR-1 / P-2 (2.10 line 1299): whether a tokenless Epic needs an acceptance map. It waits for the Product Owner's pending decision. PF04 §2.0.19's acceptance-map wording (the `QA_ACCEPTANCE_MAP_VIABILITY_OK` block, lines 848–864, and "Acceptance-evidence cross-reference (conditional)", line 923) is unchanged.

No change in the selected units belongs to an Epic or CRD that the inputs do not show closed: 2.1, 2.2, 2.15 and 2.16 are Product Owner decisions active from publication (lines 211, 524, 1665, 1882); 2.8 carries HDE-CRD-0002 (Closed, `CLOSE / CHANGE_CLOSED`, 2026-10-26, per the handoff and ledger) and HDE-EPIC041 (closed, 2.10; `docs/ephemeral/HDE-EPIC041-CL-E-10-closure-decision-v1.0.md`).

## 5. Decisions on the handoff's uncertainties

1. PF04's share of the 2.8 amendment (unapportioned, line 1127). The PF04 drainage row (line 1121) covers the close-pack pair, the v2 writer and the TI item's `ADR status line:` field. The amendment adds two canon consequences for "the rows above". PF04's share is the part that lands in sections PF04 owns: the TI item's accepted ID forms (B-1) in the TI bullet of "Close report minimal content", and the close report's same-run evidence pointer to the change's own close-run directory (decision 7, B-2, B-4) in the "Same-run evidence pointer rule". The family's path, admission, publication and evidence home stay with HDE Schemas and Artifacts, HDE Mechanics Guide, Change Process Guide and Glow QA Guide, which RL-03 names by title.
2. 2.16 R-2 placement in Appendix D.1. Line 1888 names D.1's "Byte-compare scripts", "Composite fingerprint" and "Integration set"; lines 1932–1935 assign the generator to D.1 and the four composite fixture and log entries to D.1. Checked against the target: "Byte-compare scripts" is line 4602 (holds the generator), "Composite fingerprint" is line 4603 (`fixtures/composite/abba/*.json`, `audit/gates/determinism/abba_compare.log`) and "Integration set" is line 4604 (`fixtures/composite/integration_abba/*.json`, `audit/gates/determinism/abba_compare_integration.log`). The mapping holds exactly. D.3's "Identity marker/logs" (4617) and "Recompute scripts" (4618) match lines 1889 and 1932–1933.
3. "Status. Proposed." in 2.2, 2.15 and 2.16 is not drained. No payload contains "Proposed" (§8 scan).

## 6. Constraints, interpretations and outside observations

Constraints applied:

* HDE Build Notes is named by title only in every payload, with no addendum number, section, version or locator (PF04 §0.2; PF03 §3 "Canonical ownership"). Other PFs are routed by title, using the forms PF04 already uses nearby.
* Exact bytes owned elsewhere are routed, not restated: the compat route's status and error codes (HDE CLI/API Vendor Ref), gate-family row schemas and the close-run family's path (HDE Schemas and Artifacts).
* The header document-control fields (original lines 5–10) are reserved for TW-APPLY-10.

Interpretations:

* I-1. RL-04 places the live compat test, the Product Owner-only waiver and the blocked-test rule before §3.4's existing live-proof rules. 2.15 supersedes §3.4's dependence on a surface finding for the minimum test, the waiver authority, the meaning of Live QA and stage enforcement (lines 1666–1682). Its R-1 states that §3.4 keeps governing the Epic's own-surface live step, so the production-functional and production-affecting paragraphs stay and are aligned: the surface finding becomes a question for the Product Owner, and the exemption of the broader-scope paragraph becomes a Product Owner waiver with R-2's content.
* I-2. R-1's list of what does not satisfy the test is merged into §3.4's existing non-satisfaction paragraph, widening "an unrun smoke procedure" to "an unrun procedure", as R-1 states it.
* I-3. 2.16 retires only R-2's entries; "every other entry in those sections still governs" (line 1890). The Reader goldens and `scripts/make_reader_v1_goldens.py` therefore stay in §12.2 GATE:CORE-DET, relabeled by R-1 as proof of emitter canonical bytes and preimage hashing, not of compat AB↔BA.
* I-4. 2.2 R-2 does not conflict with §9.1.4's rule to record the PF versions a task read: such a record is provenance and does not require the cited bytes to stay unchanged. No extra wording was added for this.
* I-5. "QA-10 readiness" in RL-04 uses PF04 §9.1.5's own name for QA readiness.
* I-6. RL-10's `Acceptance:` field names `LOGS_KEYS_ONLY_OK` because RL-01 extends that token's stated scope; no token is created or satisfied.

Outside observations, not changed:

* O-1. PF04 §9.8.3 (line 3611): "Closure records and rollups MUST NOT include path references to artifacts that do not exist at the time the record is produced." 2.8's pointer rule lets a CRD's close report name, and an Epic's name, its own close-run directory before the close run writes it (line 1100). HDE Build Notes governs in its scope, and RL-03 states the exception in §2.0.19. §9.8.3 is outside this task's selected targets; aligning its wording is a later drain or a decision for Nathan.
* O-2. The original holds sixteen pre-existing ellipsis forms in path patterns and lists (for example lines 736, 743, 793, 797, 801, 872, 884, 2372, 3229, 3230, 3259, 3266, and the §9.4 template), which PF03 §3 "Structure and language" prohibits in PF documents. They are not drafting markers under TW-DRAIN-10's hygiene rule, so no redline changes them. The payloads add none (§8).
* O-3. Line 3793 reads "**nterim auth posture" (a dropped letter). Outside scope; not changed.
* O-4. §3.4 line 1206 (stage accounting for the production-functional scope) is unchanged: 2.15 R-4 drains into Change Process Guide, Glow QA Guide and Plan Templates, and RL-04 routes stage enforcement to them.
* O-5. 2.15's known nonconforming item on the environment-label write guard (owner: the Product Owner) carries no decided text and is not drained.

Hygiene. No `Draft` status language, TODO, unresolved drafting note or editorial comment needs removal. The search (`TODO`, `TBD`, `FIXME`, `XXX`, `draft`, `fill later`, `[OMITTED`, `placeholder`) found only normative uses, canon-required template text (§9.4) and history (§9.3.1, line 2653).

## 7. Repository inspection

Bounded read-only checks on `origin/main` `84d6d1c` (`git cat-file -e` per path and `git show` with fixed-string search), for paths the payloads name:

* Present: `tests/core/test_engine_core_abba.py`, `tests/core/test_engine_core_determinism.py`, `tests/compat/test_evaluate_pair_eligibility.py`, `tests/compat/test_compat_public_ab_ba_identity.py`, `tests/cli/test_showcompat_parity_and_identity.py`, `scripts/make_compat_determinism_artifacts.py`, `tests/scripts/test_make_compat_determinism_artifacts.py`, `scripts/make_reader_v1_goldens.py`, `artifacts/cards/a3/IDENTITY_OK.txt`, `artifacts/compat/AB.json`, `tools/evidence/run_sanity_pipeline.py`, `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`.
* Absent, as 2.16 records: `artifacts/cards/A3/IDENTITY_OK.txt`, `ci/jobs/preimage_recompute_and_compare.yml`, `ci/jobs/ab_ba_parity_bytecompare.yml`, `ci/jobs/two_run_identity_bytecompare.yml`, `audit/gates/determinism/abba_compare.log`, `audit/gates/determinism/abba_compare_integration.log`; `fixtures/composite/` has no tracked file.
* `tests/compat/test_evaluate_pair_eligibility.py` (lines 453–460) and `tests/cli/test_showcompat_parity_and_identity.py` (lines 171–180) recompute `idempotence_hash` from the preimage, supporting RL-14.
* `tools/evidence/run_sanity_pipeline.py` takes a `log_path` (line 345) and resolves symlinks (line 347), as D-4 records.

These checks prove checked-in bytes only. No test, pipeline or tool was run, and no runtime, deployment or production-database state is claimed. The payloads state requirements; they do not claim that the compat route, the sanity pipeline or the gate tool conforms today.

## 8. Producer validation

Validation 1, at build (`tools/build_redlines.py` in the session scratchpad): each operation resolved against the unchanged original; observed counts equal expected; spans checked for overlap and shared boundaries; payloads checked for the fence string and ellipsis; one-pass simulated application by original offsets.

Validation 2, independent (`tools/verify_package.py`): parses the saved redlines file as an applier would, checks every literal's stated byte length and SHA-256, re-resolves each operation, re-checks counts and non-overlap, applies in one pass and compares with validation 1's output. Result: identical.

| ID | Op | Original byte span or gap | Occurrences expected / observed | New bytes |
| :---- | :---- | :---- | :---- | ----: |
| RL-01 | REPLACE | 79252–79459 | old block 1 / 1 | 932 |
| RL-02 | REPLACE | 131622–132094 | old block 1 / 1 | 613 |
| RL-03 | INSERT | gap at 149554 | BEFORE 1, AFTER 1, gap 1 / 1, 1, 1 | 679 |
| RL-04 | REPLACE | 172842–176235 | old block 1 / 1 | 7,497 |
| RL-05 | INSERT | gap at 191277 | BEFORE 1, AFTER 1, gap 1 / 1, 1, 1 | 1,646 |
| RL-06 | INSERT | gap at 199034 | BEFORE 1, AFTER 1, gap 1 / 1, 1, 1 | 460 |
| RL-07 | INSERT | gap at 316708 | BEFORE 1, AFTER 1, gap 1 / 1, 1, 1 | 881 |
| RL-08 | INSERT | gap at 317634 | BEFORE 1, AFTER 1, gap 1 / 1, 1, 1 | 1,039 |
| RL-09 | REPLACE | 318954–319451 | old block 1 / 1 | 590 |
| RL-10 | INSERT | gap at 356990 | BEFORE 1, AFTER 1, gap 1 / 1, 1, 1 | 4,524 |
| RL-11 | REPLACE | 539486–539826 | old block 1 / 1 | 1,598 |
| RL-12 | REPLACE | 561369–561542 | old block 1 / 1 | 362 |
| RL-13 | REPLACE | 571588–571921 | old block 1 / 1 | 460 |
| RL-14 | REPLACE | 572251–572420 | old block 1 / 1 | 209 |

* Spans are disjoint, and no insertion gap touches a replaced span or another gap.
* Dialects: only `REPLACE` and `INSERT`. No `FIND AND REPLACE` or `FIND_AND_REPLACE`, so the RL-045 count rule has nothing to apply to.
* Simulated revised body (header fields still at baseline values, for TW-APPLY-10 to derive): 596,102 bytes, 4,821 lines, SHA-256 `844d90aa6e8bb4d605ba3c8abd4d0ec61de3391b5e9a262d1cf30a84dbfb2e11`.
* Payload scan: no `PF10`, no addendum number, no `Proposed`, no ellipsis, no `TODO` or `TBD`, no four-backtick run, no model identifier. The simulated body's ellipsis count equals the original's (16).
* Limits: the simulation applies the redlines only; it does not derive the header fields, which TW-APPLY-10 owns.

## 9. Header provenance for TW-APPLY-10

* Baseline native header (lines 5–10): `**Title:** PF04-Canon-HDE-Governance`, `**Version:** v2.8.8`, `**Status:** Canon`, `**Effective date:** 2026-10-26`, `**Last Update Gate:** BN 13.8.8`, ``**Invocation tag:** `INV-f2ac55d77ce9aacc` ``; each line but the last ends with two spaces.
* Sources in source order: `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5 (the only source). The baseline gate form is `BN <version>`.
* RL-10 names v2.8.9 and the preparation date 2026-11-02 in the §9.3.1 entry's `PF04 version` and `Date / Author` fields. The original restates its own version and date nowhere else except as history in §9.3.1.

## 10. Save verification

Save completeness: `COMPLETE_PACKAGE`. Both files were saved in the working tree of `claude/gtwpe-triage-authoring-j94ewf` and read back completely on 2026-11-02:

* Redlines file: 52,073 bytes, 514 lines, SHA-256 `992b46396e5be5586645135f63e39521fc963f8da633b464d02323bb0cc31958`, byte-identical to the built package; it ends with `END OF REDLINES` and one line feed. Validation 2 run on the saved copy, against the original read straight from git blob `0c3ce100f942` at `e2b7427`, re-resolved all fourteen operations with the counts in §8 and produced the 596,102-byte result with SHA-256 `844d90aa6e8bb4d605ba3c8abd4d0ec61de3391b5e9a262d1cf30a84dbfb2e11`.
* This proof log: read back in full after this section was written; its own hash is not recorded inside it.

The commit that holds the pair is reported in the session's final response and in the ledger's T-01 row.
