# Proof log — PF12 redlines — gtwpe-20261101-pf10-v14-0-5 (T-04)

## 1. Artifact and association

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Artifact identity | 36,020 bytes; 470 lines; SHA-256 `f7c381cd292ac1f88cfcd2eaeee5faaf63045734afdf90004838f31fa89cb2b3`; ends with `END OF REDLINES` |
| This proof log | `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, beside the artifact. It does not record its own hash. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-04 / preparation revision r1 |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1. Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of this step; the page states "Prompt Version: 100926.1" and was last edited 2026-10-09T11:05:22Z. |
| Originating preparer | One Claude Code session that Nathan started for T-04 on 2026-11-02, with the handoff "GTWPE document session — T-04 — HDE Schemas and Artifacts (drain, then apply)". No subagent, reviewer or other session took part. |
| Authorized next step | TW-APPLY-10 100926.1 in the same session (the handoff authorizes both steps in order). |
| Preparation outcome | `READY` |
| Save outcome | Recorded in §14, after the read-back of both files |

## 2. Canon and rules relied on

Canon was read from `docs/pfcanon/` at `origin/main` `e2b7427`; `origin/main` had moved to `84d6d1c` by the time of this session, with no change under `docs/pfcanon/` (`git diff --stat e2b7427 origin/main -- docs/pfcanon/` was empty).

- PF03 Technical Writing Best Practices, read in full (v1.8.8, 633 lines): §3 "Governing editorial principles" (truth and source fidelity, canonical ownership, claim-state separation, structure and language, the ellipsis prohibition); §4 authoring method; §5 ownership and routing; §6 source precedence; §7 revision and retention; §8 redlines and placement; §9 "Writing PF10-HDE-Build-Notes content" (citation of HDE Build Notes by title only in other PF documents); §11 editorial validation; §12 claim language; §14 final check. Where TW-DRAIN-10's redline contract differs from PF03 §8 (fenced literal payloads), the operator-supplied contract governs, as PF03 §8 provides.
- HDE Schemas and Artifacts (the target), §0.2 "Supersession by HDE Build Notes addenda" (HDE Build Notes is cited by title only; versioned source identities belong in the proof log), §0.2 "Evidence Catalog" (§§8.3 and 8.6 are the single home for governed evidence families and paths), §0.3 tagging (`[Required-Now]` does not claim conformance), §0.4 "Doc-Delta triggers", §9.1 "What requires a Doc-Delta", §9.2 template, and §§9.5 and 9.6 as the established record format.
- HDE Build Notes front matter "Precedence, versioning, and scope" was not re-read; the ledger records it (ledger §1) and nothing in this task depends on it beyond the publication posture already recorded there.
- AGENTS.md: "Canon-first rule", "PF canon is read-only", "Truncation/retrieval-failure guardrail", "Governed evidence rules", "Evidence attribution, currentness and distinct decisions".

## 3. Sources and inputs

| Role | Identity |
| :---- | :---- |
| Target (original baseline) | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`, in-document title PF12-Canon-HDE-Schemas-and-Artifacts, v2.9.7, Status Canon, effective 2026-10-26; Git blob `d5bc01f83078bebe04f0854385317b47c1cd2de3`; SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`; 640,642 bytes; 6,264 lines; one final LF |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; 1,976 lines |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` |
| Routing ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064` (22,735 bytes), read in full. Planning and provenance only; not a change source. |
| Closure and approval evidence | 2.1 and 2.2 are Product Owner decisions, canon from publication (l.211, l.524). 2.8 is cross-cutting close tooling; HDE-CRD-0002 is Closed and HDE-EPIC041 is closed (the 2.10 heading, l.1230, records that Isis closes HDE-EPIC041 with CLOSE / CHANGE\_CLOSED at 2026-11-01T16:39Z). 2.16 is a Product Owner decision, canon from publication (l.1882). |

## 4. Coverage

Target. Every line of PF12 was read, in 18 recorded windows that together cover lines 1 to 6,264 with no gap (checked by script):

| Lines | Bytes |
| :---- | :---- |
| 1–480 | 37,439 |
| 480–781 | 32,461 |
| 782–1161 | 43,738 |
| 1161–1560 | 36,593 |
| 1561–2243 | 59,152 |
| 2244–2773 | 32,286 |
| 2774–3173 | 38,068 |
| 3174–3473 | 40,234 |
| 3474–3702 | 34,381 |
| 3703–4002 | 44,496 |
| 4003–4202 | 42,532 |
| 4203–4402 | 48,605 |
| 4403–4702 | 40,895 |
| 4703–5002 | 28,260 |
| 5003–5302 | 21,669 |
| 5303–5681 | 25,609 |
| 5682–6046 | 19,347 |
| 6047–6264 | 14,879 |

Selected source units, each read in full: 2.1 lines 205–561 (33,981 bytes, covering D-1 to D-5, scope, dependencies and evidence; D-4 397–450, D-5 451–490 and the context units 205–224 and 491–516 are inside this window); 2.2 lines 517–588 (inside the windows 205–561 and 562–588); 2.8 lines 1048–1145 (36,158 bytes); 2.16 lines 1869–1976 (8,408 bytes).

Supporting reading, not drain scope: 2.1 D-1 to D-3 (inside the 2.1 window, read only because the window is contiguous); 2.2 lines 562–588; 2.8 lines 1048–1062, 1107–1110 and 1128–1145; 2.9 lines 1146–1229 (26,466 bytes); 2.10 lines 1230–1232 (closure heading and first paragraph); 2.16 R-3 and the rest of 2.16 (1940–1976).

No read ended mid-unit, and no retrieval failure occurred.

## 5. Change and disposition ledger

Classifications use TW-DRAIN-10's native labels. "Already represented" gives the exact original-baseline location that carries the change.

### C-04 — 2.1 D-4, evidence tools own their output root (controlling)

| Item | Disposition | Location |
| :---- | :---- | :---- |
| Release attestation builder: documented interface unchanged; an absent root is created; an existing, empty, non-symlinked external directory is accepted | Actionable, CANON\_UPDATE | RL-06, §6.2.1 builder-refusal paragraph (original l.2049) |
| Exclusive claim by atomic create before any other write; typed refusal of an unclaimable root; the claim adds no bundle member beyond `hde.release_attestation.v1` | Actionable | RL-06 |
| No writes through symlinks; a pre-existing or substituted symlink below the root is refused, not followed | Actionable | RL-06 |
| Scoped cleanup on failure, then the failure receipt; never removes a path the run did not create | Actionable | RL-06 |
| "Unchanged": the refusal list, the isolated build, the byte-stable checkout and the contracts | Already represented | §6.2.1 l.2040–2049 (interface, contracts, refusal list); §6.2.2 |
| "Left undecided": the mechanism of the exclusive claim | Actionable as a nonclaim | RL-06 last paragraph: "They do not fix the mechanism of the exclusive claim" |
| Sanity pipeline `--log-path` bound | Out of this target's ownership | D-4 names HDE Governance §4.1.8 and HDE Mechanics Guide §27.5 (T-01, T-05). PF12 §8.6.3.4 "Sanity pipeline (gate)" (l.3314–3318) already names `audit/gates/sanity_pipeline/sanity_pipeline.log` as the single canonical surface and does not conflict. |
| Consequences: new owner tests; unchanged builder contracts and CI invocation | Not drained (implementation consequences of the implementing change) | none |

Claim posture: D-4 is canon from publication, and its implementing change (Candidate CRD Items List item 9) is open (2.1 l.223, l.506). RL-06 therefore states the rules as MUST requirements and adds that the section "does not assert that the current builder already enforces them". This follows PF03 §3 "Claim-state separation" and PF12 §0.3 (`[Required-Now]` claims no conformance).

### C-05 — 2.1 D-5, governed gate check rows (controlling)

| Item | Disposition | Location |
| :---- | :---- | :---- |
| Scope: rows of `json_gate_check_log.ndjson`, `json_gate_compare_log.ndjson` and any other PF12-governed gate family are governed logs | Actionable, CANON\_UPDATE (row-content rule added); the governed-log classification itself is routed by title to HDE-Governance | RL-01 |
| Issue entries are closed tokens; an exception contributes at most `validation_error:<ExceptionType>`; no message text or stack trace | Actionable | RL-01 |
| Every recorded path is repository-relative; no absolute or machine-local path | Actionable | RL-01 |
| Diagnostics go to the tool's stderr, which is not governed evidence | Actionable | RL-01 |
| Drain target 1: §1.2 "Canonical JSON gate artifacts" | Actionable | RL-01, a new run-in block "Governed gate check row content (normative)." after the paragraph "Acceptance bindings MUST cite" (original l.549) |
| Drain target 2: Evidence Catalog entry "Canonical JSON and topology" | Actionable | RL-07, §8.6.3.2 (original l.2971–2972): both log entries point to the §1.2 rule, so the rule keeps one home |
| HDE Governance §2.0.10 addition; §6.3.2 unchanged | Out of this target's ownership | HDE Governance (T-01) |
| Consequences: the committed logs carry no such entries; the gate tool changes in the implementing change; frozen captures stay as recorded | Frozen captures: actionable as one sentence in RL-01. The rest is implementation or current-repository fact and is not drained; RL-01 states that the section does not assert current enforcement. | RL-01 |

### C-06 — 2.1 status, scope, dependencies and evidence (supporting context)

Read for C-04 and C-05. It establishes the decisions' standing (canon from publication), their independence, the nonclaims and the open item 9 (held as H-10 by the ledger, future Product Owner authoring). Nothing drains from it to PF12.

### C-07 — 2.2 R-1 and R-2, uncertain for this target through l.525

l.525 supersedes any HDE Schemas and Artifacts requirement that a close pack, tool, test or record read or bind a planning document, or name a PF document by file name or version. PF12 was searched for every such requirement (script over the decoded text for `docs/ephemeral`, `docs/pfcanon`, versioned PF file names, "planning document", "Specification", "implementation plan" and "QA Plan"):

- l.6004, l.6008 and l.6137 name a versioned PF file or a `docs/ephemeral/` path inside the dated records §9.5 and §9.6. Under PF12 §0.2 and PF03 §9, dated historical records keep their original locators; they impose no requirement on a tool. No change.
- l.590 and l.5308 say that the approved CRD Specification records the CRD ID. That locates the record; no tool must read it. No change.
- l.494 ("repo manifests → audit manifests → rendered reports → QA Plan") ranks sources of a bound path when they disagree. It requires no tool to read or bind a plan. No change.
- l.622, l.4015 onward, l.5359 onward: rules about what Live QA Plans may require or contain. They are planning rules, not tool inputs. No change.
- No PF12 text requires the close-pack writer or any other tool to read a planning document or pin a PF version.

Disposition: no conflicting PF12 requirement exists, so l.525 needs no PF12 edit. The rules R-1 and R-2 themselves drain to HDE Governance §9.1.2 and §9.1.3 (T-01) and Plan Templates (T-07), not to PF12. PF12's share of 2.2 is C-10.

### C-10 — 2.2 "Changes delivered", the v2 source fields and the input refusal (controlling)

| Item | Disposition | Location |
| :---- | :---- | :---- |
| A v2 source records `planning_records`, `requirement_ids`, `qa_checks` and `qa_verdict`, and has no plan path or planning-document binding | Actionable, CANON\_UPDATE | RL-02 (new bullet after original l.603). Field meanings taken from 2.8 l.1059 (a) and l.1090. The schema's required properties were confirmed read-only (§8). |
| No path under `docs/ephemeral/` or `docs/pfcanon/` is a causal input, pointer or key output in either schema version (`PLANNING_OR_CANON_INPUT_PROHIBITED`); the v2 schema refuses one too | Actionable | RL-03 (original l.605) |
| A deferral's drain target names its register by PF title; PF titles and register headings resolve at write time only, against the canon tracked at HEAD; check mode reads no PF-Canon file | Actionable | RL-03 |
| A later-drain statement and a superseded artifact may name a planning document by record text | Actionable | RL-03 |
| Close-pack test fixtures and CI classification | Out of this target's ownership | Plan Templates "CI lane classification and automated budget-control discipline" (T-07) |
| ADR amendment; HDE-CRD-0002 close pack rebuilt and regenerated | History, not drained | The record is the ADR and HDE Build Notes; PF12 records no CRD-0002 pack bytes. |

### C-17 — 2.8 decisions 1 to 9, stated limits and drainage table (controlling)

The PF12 rows of the 2.8 drainage table were largely drained on 2026-10-26 (PF12 §9.6). Each item:

| 2.8 item | Disposition | Location in the original baseline |
| :---- | :---- | :---- |
| Decision 1, the v2 schema for one Epic or CRD; v1 unchanged | Already represented | §1.2 l.602–603 |
| Decision 2, one writer, model by `schema_version`, non-writing check mode | Already represented | §1.2 l.601, l.605 ("Check mode writes nothing") |
| Decision 3, paths of record for Epic and CRD | Already represented | §1.2 l.604. The HDE-CRD-0002 candidate-source path is not in the PF12 drainage row and is not added. |
| Decision 4, v2 report contents | Already represented by routing | §1.2 l.606 routes the decision criteria and required content to Change Process Guide and HDE-Governance; the later-drain vocabulary is at l.644–647 |
| Decision 5, v2 manifest and its `key_outputs` minimum | Already represented | §1.2 "Generic v2 writer `key_outputs` minimum" l.942–944 |
| Decision 6, feedback-freedom kept; causal-input refusals | Already represented, plus actionable | l.605 carries the refusal list. The `docs/ephemeral/` and `docs/pfcanon/` refusal is added by RL-03 (C-10). The QA-primary-path and QA-plan-check-ID exceptions are writer details owned by the ADR and Change Process Guide; l.605 "The feedback-dependency refusal is kept" does not conflict. |
| Decision 7, post-verdict close-run family for admitted CRDs | Already represented | §1.2 l.668; §8.17 l.5399–5407; §8.17.1 l.5424, l.5442–5443 |
| Decision 7, extension to admitted Epics (2026-11-01, B-4) | Actionable (C-18) | RL-05, RL-08, RL-09 |
| Decision 8, absent-tolerant CRD rows | Already represented | §1.2 l.607 |
| Decision 8, extension to admitted Epics (B-3) | Actionable (C-18) | RL-04 |
| Decision 9, ADR block | Out of this target's ownership | Change Process Guide §3.5.4 (T-03) |
| Dependency direction | Already represented | §1.2 l.944 (no Index, path-proof, orientation or close-run digest in the manifest); §6.2.2 |
| Stated limits: QA RCA path; doc-deltas and drain-targets explicit-empty rules; byte-identical QA-root copy | Already represented | §1.2 l.615–617, l.658–662. The ADR pins the literals ("Doc Deltas: None", "Drain Targets: None") because §1.2 gives none; PF12 keeps its rule without the literal. |
| Stated limits: tracked-issue ADR-status mapping; ID form (B-1) | ID form actionable (C-18); the mapping form belongs to Change Process Guide §3.5.2.1 (T-03) | RL-02 |
| Stated limits: pointers, including the close-run directory (B-2) | Actionable (C-18) | RL-05 |
| Stated limits: "an Epic close run needs its own explicit admission"; HDE-EPIC041 the one Epic admitted | Actionable (C-18) | RL-08 Epic bullet; RL-04 last sentence |
| Other stated limits (review-trace-only posture, QA plan mapping, closure override, PF title reading, allocation, pinned QA ledger format) | Owned by Change Process Guide, HDE-Governance, Glow QA Guide and HDE Mechanics Guide | No PF12 locus, apart from the posture at l.606, which is already represented |
| Epic-only identity inventory | Already represented, exact equivalence | §1.2 l.597 |
| Drainage row "§1.2 Close-pack artifacts (deterministic path-of-record; baseline artifacts) and Change-container compatibility (normative)" | Represented after RL-02 to RL-05; "Change-container compatibility" l.585–597 needs no change | — |
| Drainage row "§8.17 New standardized evidence families and Current-state evidence; §8.17.1" | Represented for CRDs at l.5346–5350, l.5390–5408 and l.5424; extended to Epics by RL-08 and RL-09. "HDE Build Notes introduced this family" (l.5407) is the title-only form of "introduced by the AQ-1 approval addendum". | — |

### C-18 — 2.8 amendment of 2026-11-01 (l.1060, l.1127), PF12's share

The ledger leaves the apportionment to each editor. PF12's share, decided here:

| Consequence | PF12 home | Redline |
| :---- | :---- | :---- |
| B-1, Epic tracked-issue ID form `ISSUE-EPIC<NNN>-TI-<nn>` beside `TI-NNN`; refusal of another Epic's ID (`TRACKED_ISSUE_UNBOUND`) | §1.2 v2 schema bullet, because PF12 records the v2 schema's closed domain | RL-02 |
| B-2, an Epic may point to its own close-run directory before it exists; a CRD must point to its own; any other unresolved pointer is refused (`POINTER_UNRESOLVED`) | §1.2 same-run close evidence paragraph | RL-05 |
| B-3, absent-tolerant `epicNNN.close_report` and `epicNNN.manifest` rows with `epic_id` for every Epic in `ADMITTED_EPIC_CLOSE` | §1.2 writer bullet | RL-04 |
| B-4, the Epic close-run family, `publish_epic_close_run_family`, the QA harness's renderer, the Epic's QA family not written and refused if changed, `epic_id` on rows | §1.2 same-run paragraph; §8.17 exception; §8.17.1 `close/` | RL-05, RL-08, RL-09 |
| Admission: `ADMITTED_EPIC_CLOSE` admits HDE-EPIC041 only; another Epic needs its own row and the Product Owner's explicit admission (l.1103, l.1131) | §8.17 exception; §1.2 writer bullet | RL-08, RL-04 |
| The false current statements "No Epic close-run family is admitted" (l.668, l.5408) and "admitted CRDs only" (l.5399, l.5424) | Replaced | RL-05, RL-08, RL-09 |
| HDE-CRD-0002's close pack regenerated in #811 | History, not drained | none |

### C-20 — 2.9 (supporting)

Read in full as support for C-18. It confirms B-1 to B-4 and their owner tests, the explicit admission of HDE-EPIC041's close run, and the nine close-run primaries with `epic_id`. CCR-5 in 2.9 is held (H-06) and has no PF12 locus: PF12 states no ordering between the close-pack write and the closure decision.

### C-29 — 2.16 status, R-1 and R-2, uncertain

PF12 was searched (decoded text, escapes removed) for every entry 2.16 R-2 retires: `make_compat_determinism`, `IDENTITY_OK.txt`, `artifacts/cards`, `preimage_recompute_and_compare`, `ab_ba_parity_bytecompare`, `two_run_identity_bytecompare`, `fixtures/composite`, `abba_compare`, `CORE-DET` and `GATE:`. Each search found 0 occurrences. `ci/jobs/` occurs only at l.3323–3324 (`logs_keys_only_redaction.yml`, `rails_open_conformance.yml`), neither of which R-2 names. `artifacts/compat/` occurs at l.3062–3064 and l.3118–3128, the "Compat closure artifacts" and HDE-EPIC030 PR-03 entries. R-2 does not retire those captures (l.1937 keeps them "as history"), and PF12 does not present them as GATE:CORE-DET evidence.

Disposition: no PF12 home. C-29 is out of this target's ownership; its drainage targets are HDE Governance §12.2, Appendix B.2, Appendix D.1 and Appendix D.3 (2.16 l.1965; T-01).

### Doc-Delta hook

PF12 §9.1 requires a Doc-Delta when governed evidence rules change, and §§9.5 and 9.6 set the documentary drainage record form. RL-10 adds §9.7 in that form (NEW\_CANON), with `document_version: "v2.9.8"`, `date: "2026-11-02"` and a `change_log_entry` naming `v2.9.8 / 2026-11-02`. Following §0.2, the record cites HDE Build Notes by title and keeps addendum IDs and versioned identities in this log. Its release-identity fields carry the SHA-256 of the unchanged `catalog/manifest.json` at `e2b7427` (`77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, computed read-only).

## 6. Uncertainty decided in this session

- The owner of the C-05 Evidence Catalog entry is PF12. The heading "Canonical JSON and topology" exists only in PF12 §8.6.3.2 (`git grep` over `origin/main` `docs/pfcanon/`). PF12 §0.2 makes §§8.3 and 8.6 the single home of the Evidence Catalog, and other PF documents must not keep parallel path lists. The row-content rule has one home (§1.2, RL-01); the catalog entry points to it (RL-07).
- C-29 has no PF12 home (§5, C-29).
- C-07 needs no PF12 edit (§5, C-07).

## 7. Held, out-of-scope and routed items

- H-07 (CCR-1 / P-2), held: whether a tokenless Epic needs an acceptance map. It waits for the Product Owner's decision (2.10 l.1299, recorded by the ledger). PF12 "Optional token compatibility" (§8.6.1, l.2818–2824) and "Acceptance map — legacy token compatibility shape" (l.2873–2884) are left unchanged.
- H-06 (CCR-5), held by the ledger: no PF12 locus.
- H-10 (item 9 CRD identity and Specification): nothing to drain; RL-06 and RL-01 carry their nonclaims instead.
- Routed, not drafted here: D-4 `--log-path` (T-01, T-05); D-5 §2.0.10 (T-01); 2.2 R-1 and R-2 (T-01, T-07); 2.2 R-3 and the close-pack test (T-07); 2.8 decision 9 and the deferral and tracked-issue mapping forms (T-03); 2.16 (T-01).

## 8. Read-only repository inspection

All at `e2b7427ff418ca8f08f05587c4a541308a76da56`, with `git show`, `git grep` and `git ls-tree`. Nothing was executed or written.

- `tools/evidence/update_evidence_index.py`: `ADMITTED_CRD_QA` (l.51) maps HDE-CRD-0001 and HDE-CRD-0002; `ADMITTED_EPIC_CLOSE` (l.62) maps only `"HDE-EPIC041": ("audit/qa/hde-epic041", "audit.qa.hde_epic041")`; `publish_crd_close_run_family` (l.5439) and `publish_epic_close_run_family` (l.5568) exist; Epic close-run entries use `f"{key_prefix}.close.{check_id}.primary.log"`, `role: "log"` and `epic_id`; Epic close-pack keys are `"epic" + <NNN>` with suffixes `close_report` and `manifest`.
- `docs/evidence/INDEX.json` (678 rows): `epic041.close_report`, `epic041.manifest` and the nine `audit.qa.hde_epic041.close.<check_id>.primary.log` rows carry `epic_id: HDE-EPIC041`; the nine HDE-CRD-0002 close-run rows carry no `crd_id` in the Human Index, so RL-08 claims `epic_id` for Epic rows only.
- `audit/qa/hde-epic041/close/final-lf/primary.log` and `audit/qa/hde-crd-0002/close/final-lf/primary.log` both open with a `pf27.step_log_header.v2` header, so the existing header bullet applies to both families unchanged.
- `schemas/close_candidate_source.v2.json`: the required properties include `planning_records`, `requirement_ids`, `qa_checks` and `qa_verdict`; there is no plan-path property; `ti_id` is `^(?:TI-[0-9]{3,}|ISSUE-EPIC[0-9]{3}-TI-[0-9]{2,})$`.
- `tools/qa/generate_epic_close_pack.py`: the refusal codes `PLANNING_OR_CANON_INPUT_PROHIBITED` (l.2351) and `TRACKED_ISSUE_UNBOUND` (l.2721, l.2727) exist.
- `audit/` holds `EPIC-041_close_candidate_source.json`, `EPIC-041_close_report.md`, `EPIC-041_MANIFEST.json` and the matching HDE-CRD-0002 files.
- `catalog/manifest.json`: version 1.3.0, built 2026-08-24T18:04:49Z, 45 members, SHA-256 `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`.

These observations support the drafted wording only. They are not QA, not a test run, not governed evidence and not proof of behaviour. `tools/evidence/build_release_attestation.py` and `tools/evidence/run_canonical_json_gate.py` were not inspected; RL-06 and RL-01 assert nothing about their current behaviour.

## 9. Redline summary

| ID | Operation | Original location | Rows | Change |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | INSERT | §1.2, gap before l.551 | C-05 | New run-in block "Governed gate check row content (normative)." |
| RL-02 | REPLACE | §1.2 l.603 | C-10, C-18, C-17 | v2 schema bullet gains the tracked-issue ID form; new bullet for the v2 planning-record fields |
| RL-03 | REPLACE | §1.2 l.605 | C-10, C-17 | Planning and PF-Canon input refusal; write-time PF title resolution; check mode reads no PF-Canon file |
| RL-04 | REPLACE | §1.2 l.607 | C-18, C-17 | Absent-tolerant Epic close-pack rows for `ADMITTED_EPIC_CLOSE` |
| RL-05 | REPLACE | §1.2 l.668 | C-18, C-17 | Same-run close evidence for an admitted CRD or Epic; close-run pointer rule |
| RL-06 | REPLACE | §6.2.1 l.2049 | C-04 | Builder output-root ownership: exclusive claim, no symlink writes, scoped cleanup |
| RL-07 | REPLACE | §8.6.3.2 l.2971–2972 | C-05 | Evidence Catalog entries point to the §1.2 row rule |
| RL-08 | REPLACE | §8.17 l.5399–5408 | C-18, C-17 | Close-run family exception covers admitted Epics |
| RL-09 | REPLACE | §8.17.1 l.5424 | C-18, C-17 | `close/` bullet covers admitted Epics |
| RL-10 | INSERT | §9.6 end, gap before l.6165 | C-04, C-05, C-10, C-17, C-18 | New §9.7 documentary drainage record |

## 10. Producer validation

A local script resolved every operation against the unchanged original (decoded as UTF-8; offsets are character offsets), checked the batch, and simulated one-pass application by original position.

| ID | Operation | Expected | Observed | Span or gap (characters) | Old length | New length |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | INSERT | 1 | 1 (BEFORE 1, AFTER 1) | gap 42,968 | — | 974 |
| RL-02 | REPLACE | 1 | 1 | 47,027–47,259 | 232 | 1,029 |
| RL-03 | REPLACE | 1 | 1 | 47,570–48,072 | 502 | 1,060 |
| RL-04 | REPLACE | 1 | 1 | 48,350–48,766 | 416 | 870 |
| RL-05 | REPLACE | 1 | 1 | 53,920–54,660 | 740 | 1,164 |
| RL-06 | REPLACE | 1 | 1 | 190,147–190,560 | 413 | 1,505 |
| RL-07 | REPLACE | 1 | 1 | 256,293–256,424 | 131 | 245 |
| RL-08 | REPLACE | 1 | 1 | 587,223–589,738 | 2,515 | 3,225 |
| RL-09 | REPLACE | 1 | 1 | 590,517–590,721 | 204 | 249 |
| RL-10 | INSERT | 1 | 1 (BEFORE 1, AFTER 1) | gap 630,886 | — | 7,017 |

- Conflicts: none. No replaced spans intersect or touch, no insertion gap lies at or inside a replaced span, and no two insertions share a gap.
- Operation dialects: only `REPLACE` and `INSERT`. No repeated-replacement operation, so the RL-045 rule does not arise.
- Post-simulation: each replacement or insertion text occurs exactly once in the output, and each replaced old block occurs 0 times.
- Simulated output: 652,835 bytes; 6,398 lines; ends with LF; SHA-256 `80222678e43477ed9f246402e0056ee9341f3ae976afef771f841b27efa488c4`. This is a preparation-time simulation, not the final PF; TW-APPLY-10 also derives the header.
- Saved-file revalidation: a separate script parsed the saved redlines file by its literal-block convention, re-resolved all ten operations against the original (each count 1), re-simulated, and reproduced SHA-256 `80222678e43477ed9f246402e0056ee9341f3ae976afef771f841b27efa488c4` exactly.
- Editorial checks on the new text: no ASCII three-period or Unicode ellipsis; no `Draft`, TODO, placeholder or drafting note; HDE Build Notes cited by title only; no PF version or addendum number in new prose; MUST and MAY used only for normative requirements.
- Hygiene scan of the original for markers TW-DRAIN-10 requires removed (Draft status language, TODO, unresolved drafting note): none found. `SCHEMA-DRAFT`, `Draft-07` and `[OPEN]` are canon names or conventions.

Corrections made during preparation, before READY: the heading paths were first written by hand, and RL-01's wrongly began at §0 while RL-08's and RL-09's quoted the §8.17 heading inexactly. The builder was changed to derive every heading path from the raw original headings, outside code fences, and the package was rebuilt and revalidated. The redline payloads did not change.

## 11. Constraints, assumptions and interpretations

- New text is normative contract text (`[Required-Now]` posture). For D-4 and D-5, whose implementing change is open, each addition says plainly that it does not assert current enforcement.
- The Epic admission sentence names HDE-EPIC041 as the only current row, as 2.8 l.1103 does and as the inspected table shows. It will need maintenance when another Epic is admitted, as the replaced sentence "No Epic close-run family is admitted" did.
- RL-05 renames the run-in label "Same-run close evidence for a CRD (normative)." and RL-08 renames "(normative; admitted CRDs only)". Neither is a section heading, and no other PF document cites either label (`git grep` over `docs/pfcanon/` on `origin/main`). Keeping them would leave false labels.
- The §9.7 record cites its proof-log path under `docs/ephemeral/` as a reference only, as §9.6 does; under 2.2 R-1, a prose citation of a planning document in a permanent record is a reference.
- This package edits no PF canon. The revised PF exists only as TW-APPLY-10's output under `docs/ephemeral/`.

## 12. Observations outside the selected scope (not acted on)

- PF12 §5.3 "Current repository posture" (l.1959, l.1970) still gives `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` as the current `release_id`; the baseline manifest digest is `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`. §9.6 records that §5.3 was not refreshed. No selected unit covers it.
- l.1968 contains a Unicode ellipsis character after the recorded identity prefix `988ed2a7`, which PF03 §3 prohibits, and l.2144 ends with a doubled period. Neither is authorized hygiene under TW-DRAIN-10, and no source covers them.
- §8.6.3.10 describes evidence families with "explicit legacy fallback" wording (for example l.3772, l.3778, l.3823). 2.1 D-2 keeps the wire label and governed bytes and assigns name corrections to their owners; D-2 is not routed to this target.

## 13. Header provenance for TW-APPLY-10

Baseline header (§0.1): Title PF12-Canon-HDE-Schemas-and-Artifacts; Version v2.9.7; Status Canon; Effective date 2026-10-26; Last Update Gate "BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md"; Invocation tag INV-f2ac55d77ce9aacc. Each line but the last ends with two spaces.

Source that justified the update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, version v14.0.5. No other file was a change source. The closure records it relies on are inside that same file (2.10).

Version scheme: v2.9.5, v2.9.6, v2.9.7 (§§9.5, 9.6); expected derived version v2.9.8. RL-10 names v2.9.8 and the preparation date 2026-11-02. No redline touches §0.1.

## 14. Save verification and completion receipt

Save outcome: `COMPLETE_PACKAGE`. Both required files were written under `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/` and read back completely from disk before this receipt was written:

- the redlines file: 36,020 bytes; 470 lines; SHA-256 `f7c381cd292ac1f88cfcd2eaeee5faaf63045734afdf90004838f31fa89cb2b3`; ends with `END OF REDLINES`; its parsed operations re-simulate to `80222678e43477ed9f246402e0056ee9341f3ae976afef771f841b27efa488c4`;
- this proof log, read back in full; it then received this receipt only, which was read back again.

The two files agree on the original and source identities, the run identity, the preparer and the `READY` outcome. The package is ready for TW-APPLY-10 with the exact original, these two files, ledger rows C-04, C-05, C-10, C-17 and C-18, the selected source units in §4, branch `claude/gtwpe-triage-authoring-j94ewf`, and the output directory above. The commit that holds the package is reported in the session's final response and in the ledger's T-04 row; this log does not carry its own commit.
