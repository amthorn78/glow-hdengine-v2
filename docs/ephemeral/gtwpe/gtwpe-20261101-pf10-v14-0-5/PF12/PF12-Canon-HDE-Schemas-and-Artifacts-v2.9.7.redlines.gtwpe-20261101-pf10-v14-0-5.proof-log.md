# Proof log — PF12 redlines — gtwpe-20261101-pf10-v14-0-5 (T-04)

## 1. Artifact and association

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Artifact identity | Revision r4: recorded in §15 after read-back; ends with `END OF REDLINES` |
| This proof log | `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, beside the artifact. It does not record its own hash. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-04 / preparation revision r4. r4 supersedes r3 (commit `4c859cc`), which TW-APPLY-10 applied (commit `5c10ee5`). r3 superseded r2 (commit `2a2325b`, returned by the TW-APPLY-10 diagnostic at commit `5716f60`), and r2 superseded r1 (commit `324de26`). §11 records why. |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1. Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of this step and fetched again before r4; both times the page stated "Prompt Version: 100926.1" and was last edited 2026-10-09T11:05:22Z. |
| Originating preparer | One Claude Code session that Nathan started for T-04 on 2026-11-02, with the handoff "GTWPE document session — T-04 — HDE Schemas and Artifacts (drain, then apply)". No subagent, reviewer or other session took part. |
| Authorized next step | TW-APPLY-10 100926.1 in the same session (the handoff authorizes both steps in order; Nathan's direction of 2026-11-02 asks for the corrected result). |
| Product Owner direction for r4 | Nathan, in this session on 2026-11-02, after the r3 application was reported with its observations: "fix the defects and inconsistencies you noticed". §11 item 4 records how it was applied. |
| Preparation outcome | `READY` |
| Save outcome | Recorded in §15, after the read-back of both files |

## 2. Canon and rules relied on

Canon was read from `docs/pfcanon/` at `origin/main` `e2b7427`. `origin/main` had moved to `84d6d1c` by the time of this session, with no change under `docs/pfcanon/` (`git diff --stat e2b7427 origin/main -- docs/pfcanon/` was empty).

- PF03 Technical Writing Best Practices, read in full (v1.8.8, 633 lines): §3 "Governing editorial principles" (truth and source fidelity, canonical ownership, claim-state separation, structure and language, the ellipsis prohibition); §4 authoring method; §5 ownership and routing; §6 source precedence; §7 revision and retention; §8 redlines and placement; §9 "Writing PF10-HDE-Build-Notes content" (citation of HDE Build Notes by title only in other PF documents); §11 editorial validation; §12 claim language; §14 final check. Where TW-DRAIN-10's redline contract differs from PF03 §8 (fenced literal payloads), the operator-supplied contract governs, as PF03 §8 provides.
- HDE Schemas and Artifacts (the target): §0.2 "Supersession by HDE Build Notes addenda" (HDE Build Notes cited by title only; versioned source identities belong in the proof log); §0.2 "Evidence Catalog" (§§8.3 and 8.6 are the single home for governed evidence families and paths); §0.3 tagging (`[Required-Now]` does not claim conformance); §0.4 "Doc-Delta triggers"; §9.1 "What requires a Doc-Delta"; §9.2 template; §§9.5 and 9.6 as the established record format.
- HDE CLI/API/Vendor Ref §7.1.10 "Endpoint policy (explicit version-gated dual lineage)" (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md` l.3472–3500, read in full): the owner of vendor route selection. A terminal, case-sensitive `v1` segment selects the retained legacy resource `bodygraphs`; every other non-v2 base fails with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or external I/O; "The explicit v1 `bodygraphs` path is retained legacy selection, not fallback." Read in support of C-02 (RL-13, RL-14).
- HDE CRD Records, the HDE-CRD-0002 record (`docs/pfcanon/PF30.1-Canon-HDE-CRD-Records-v0.9.2.md` l.553): "Release `1.3.0` kept its version, build time and 45 members; same-version refreshes at the WU-PR-03, WU-PR-04 and WU-PR-05 merges moved `release_id` from `52be4558` through `72fca4c3`, `d84d99e1` and `2f18a5eb` to `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`." Read in support of RL-07. It is not a change source.
- HDE Governance §4.1.8 "Sanity pipeline & evidence skeleton (EPIC018+)", whose "Sanity log artifact (records-only; governed)" block (l.1370, l.1386 on `main`) is the home of the sanity log contract. Located by `git grep`; read only to settle ownership.
- GTWPE-D3 in `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md`: every eligible document is updated on context and scope, never gated on a named drain target, and a change is already represented only on a pass's verified finding. The ledger's correction of 2026-11-02 restates it.
- AGENTS.md: "Canon-first rule", "PF canon is read-only", "Truncation/retrieval-failure guardrail", "Governed evidence rules", "Evidence attribution, currentness and distinct decisions".

## 3. Sources and inputs

| Role | Identity |
| :---- | :---- |
| Target (original baseline) | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`, in-document title PF12-Canon-HDE-Schemas-and-Artifacts, v2.9.7, Status Canon, effective 2026-10-26; Git blob `d5bc01f83078bebe04f0854385317b47c1cd2de3`; SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`; 640,642 bytes; 6,264 LF characters; the last line is empty, so the file ends with two LF bytes |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; 1,976 lines |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` |
| Supporting reading (r4) | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md`, Git blob `53e6a9028dfa5d79b91e9b98cc949160c5a5cefe`; `docs/pfcanon/PF30.1-Canon-HDE-CRD-Records-v0.9.2.md`, Git blob `6177325208a026063e94fe9a8a53742274a1b8bc`. Both unchanged between `e2b7427` and `origin/main` `84d6d1c`. |
| Routing ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064` (22,735 bytes), read in full; planning and provenance only. The later ledger commit `a3632c0` (another session, 2026-11-02) adds a correction banner, §8 (T-11 to T-18) and amended holds H-01, H-02 and H-12. It leaves T-04's row and selections unchanged. Before r4 the ledger was read again at the branch head `aaa4146`: T-04's assignment row and rows C-02 and C-29 are unchanged. |
| Closure and approval evidence | 2.1 and 2.2 are Product Owner decisions, canon from publication (l.211, l.524). 2.8 is cross-cutting close tooling; HDE-CRD-0002 is Closed, and HDE-EPIC041 is closed (the 2.10 heading, l.1230, records that Isis closes HDE-EPIC041 with CLOSE / CHANGE\_CLOSED at 2026-11-01T16:39Z). 2.16 is a Product Owner decision, canon from publication (l.1882). |

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

Selected source units, each read in full: 2.1 lines 205–561 (33,981 bytes, covering D-1 to D-5, scope, dependencies and evidence; D-2 277–344, D-4 397–450, D-5 451–490 and the context units 205–224 and 491–516 lie inside it; D-2 was added to the selection by Nathan's direction for r4, and was read in full again before r4); 2.2 lines 517–588 (inside the windows 205–561 and 562–588); 2.8 lines 1048–1145 (36,158 bytes); 2.16 lines 1869–1976 (8,408 bytes).

Supporting reading, not drain scope: 2.1 D-1 and D-3 (inside the 2.1 window, which is contiguous); 2.2 lines 562–588; 2.8 lines 1048–1062, 1107–1110 and 1128–1145; 2.9 lines 1146–1229 (26,466 bytes); 2.10 lines 1230–1232 (closure heading and first paragraph); 2.16 R-3 and the rest of 2.16 (1940–1976). For r4: HDE CLI/API/Vendor Ref §7.1.10 (l.3472–3500) and HDE CRD Records l.553, as §2 records.

No read ended mid-unit, and no retrieval failure occurred.

## 5. Change and disposition ledger

Classifications use TW-DRAIN-10's native labels. "Already represented" gives the exact original-baseline location that carries the change. Under GTWPE-D3, each disposition below rests on PF12's context and scope, not on whether an addendum names PF12 as a drain target.

### C-04 — 2.1 D-4, evidence tools own their output root (controlling)

| Item | Disposition | Location |
| :---- | :---- | :---- |
| Release attestation builder: documented interface unchanged; an absent root is created; an existing, empty, non-symlinked external directory is accepted | Actionable, CANON\_UPDATE | RL-08, §6.2.1 builder-refusal paragraph (original l.2049) |
| Exclusive claim by atomic create before any other write; typed refusal of an unclaimable root; the claim adds no bundle member beyond `hde.release_attestation.v1` | Actionable | RL-08 |
| No writes through symlinks; a pre-existing or substituted symlink below the root is refused, not followed | Actionable | RL-08 |
| Scoped cleanup on failure, then the failure receipt; never removes a path the run did not create | Actionable | RL-08 |
| "Unchanged": the refusal list, the isolated build, the byte-stable checkout and the contracts | Already represented | §6.2.1 l.2040–2049 (interface, contracts, refusal list); §6.2.2 |
| "Left undecided": the mechanism of the exclusive claim | Actionable as a nonclaim | RL-08 last paragraph |
| Sanity pipeline `--log-path` bound | Out of this target's ownership, by single home | The sanity log's artifact contract lives in HDE Governance §4.1.8 "Sanity log artifact" and the runner's behaviour in HDE Mechanics Guide §27.5 (T-01, T-05). PF12's catalog entry §8.6.3.4 "Sanity pipeline (gate)" (l.3314–3318) only names `audit/gates/sanity_pipeline/sanity_pipeline.log` as the single canonical surface, which the bound preserves. Restating the bound in PF12 would make a second home. |
| Consequences: new owner tests; unchanged builder contracts and CI invocation | Not drained (implementation consequences of the implementing change) | none |

Claim posture: D-4 is canon from publication, and its implementing change (Candidate CRD Items List item 9) is open (2.1 l.223, l.506). RL-08 states the rules as MUST requirements and adds that the section "does not assert that the current builder already enforces them" (PF03 §3 "Claim-state separation"; PF12 §0.3).

### C-05 — 2.1 D-5, governed gate check rows (controlling)

| Item | Disposition | Location |
| :---- | :---- | :---- |
| Scope: rows of `json_gate_check_log.ndjson`, `json_gate_compare_log.ndjson` and any other PF12-governed gate family are governed logs | Actionable, CANON\_UPDATE (row-content rule added); the governed-log classification is routed by title to HDE-Governance | RL-01 |
| Issue entries are closed tokens; an exception contributes at most `validation_error:<ExceptionType>`; no message text or stack trace | Actionable | RL-01 |
| Every recorded path is repository-relative; no absolute or machine-local path | Actionable | RL-01 |
| Diagnostics go to the tool's stderr, which is not governed evidence | Actionable | RL-01 |
| §1.2 "Canonical JSON gate artifacts" | Actionable | RL-01: a new run-in block "Governed gate check row content (normative)." after the paragraph "Acceptance bindings MUST cite" (original l.549) |
| Evidence Catalog entry "Canonical JSON and topology" | Actionable | RL-11, §8.6.3.2 (original l.2971–2972): both log entries point to the §1.2 rule, so the rule keeps one home |
| HDE Governance §2.0.10 addition; §6.3.2 unchanged | Out of this target's ownership | HDE Governance (T-01) |
| Consequences: the committed logs carry no such entries; the gate tool changes in the implementing change; frozen captures stay as recorded | Frozen captures: one sentence in RL-01. The rest is implementation or current-repository fact; RL-01 states that the section does not assert current enforcement. | RL-01 |

### C-06 — 2.1 status, scope, dependencies and evidence (supporting context)

Read for C-04 and C-05. It establishes the decisions' standing (canon from publication), their independence, the nonclaims and the open item 9 (held as H-10, future Product Owner authoring). Nothing drains from it to PF12.

### C-07 — 2.2 R-1 and R-2 (uncertain for this target; decided actionable)

PF12 was searched for every requirement that a close pack, tool, test or record read or bind a planning document, or name a PF document by file name or version (l.525), and for any PF12 rule that R-1 or R-2 constrains. The search ran over the decoded text for `docs/ephemeral`, `docs/pfcanon`, versioned PF file names, "planning document", "Specification", "implementation plan" and "QA Plan", and the §8.3 path rules were read again in full.

| Finding | Disposition |
| :---- | :---- |
| §8.3 "Governed locations only." (l.2262) names `docs/` as a governed root for Mirror-referenced files and does not exclude `docs/ephemeral/` or `docs/pfcanon/`. R-1 says no Index or Mirror row or path proof binds a path under `docs/ephemeral/`, and R-2 says no governed artifact pins a PF document's file name, version or digest. §8.3 is the single home of the Mirror record and path rules (§0.2), so the consequence belongs there. | Actionable, CLARIFY: RL-10. A read-only check at `e2b7427` found 0 rows binding `docs/ephemeral/` or `docs/pfcanon/` in `docs/evidence/INDEX.json` and 0 in `artifacts/evidence_index.jsonl`, so the sentence matches the current ledgers. |
| The close-pack writer's planning and PF-Canon input refusal | Actionable through C-10 (RL-02, RL-03) |
| l.6004, l.6008, l.6137: versioned PF file names and `docs/ephemeral/` paths inside the dated records §9.5 and §9.6 | No change. Dated historical records keep their original locators (PF12 §0.2; PF03 §9); they impose nothing on a tool. |
| l.590, l.5308: the approved CRD Specification records the CRD ID | No change. They locate the record; no tool must read it. |
| l.494: "repo manifests → audit manifests → rendered reports → QA Plan" | No change. It ranks sources of a bound path when they disagree and requires no tool to read a plan. |
| l.622, l.4015 onward, l.5359 onward: rules about what Live QA Plans may require or contain | No change. They are planning rules, not tool inputs. |

R-1 and R-2 as general rules stay with HDE Governance §9.1.2 and §9.1.3 (T-01) and Plan Templates (T-07). RL-10 states only their consequence for PF12's own records.

### C-10 — 2.2 "Changes delivered", the v2 source fields and the input refusal (controlling)

| Item | Disposition | Location |
| :---- | :---- | :---- |
| A v2 source records `planning_records`, `requirement_ids`, `qa_checks` and `qa_verdict`, and has no plan path or planning-document binding | Actionable, CANON\_UPDATE | RL-02 (new bullet after original l.603). Field meanings follow 2.8 l.1059 (a) and l.1090; the schema's required properties were confirmed read-only (§8). |
| No path under `docs/ephemeral/` or `docs/pfcanon/` is a causal input, pointer or key output in either schema version (`PLANNING_OR_CANON_INPUT_PROHIBITED`); the v2 schema refuses one too | Actionable | RL-03 (original l.605) |
| A deferral's drain target names its register by PF title (with one of its headings, 2.8 l.1095); PF titles and register headings resolve at write time only, against the canon tracked at HEAD; check mode reads no PF-Canon file | Actionable | RL-03 |
| A later-drain statement and a superseded artifact may name a planning document by record text | Actionable | RL-03 |
| Close-pack test fixtures and CI classification | Out of this target's ownership | Plan Templates "CI lane classification and automated budget-control discipline" (T-07) |
| ADR amendment; HDE-CRD-0002 close pack rebuilt and regenerated | History, not drained | The record is the ADR and HDE Build Notes; PF12 records no CRD-0002 pack bytes. |

### C-17 — 2.8 decisions 1 to 9, stated limits and drainage table (controlling)

The PF12 rows of the 2.8 drainage table were largely drained on 2026-10-26 (PF12 §9.6). Each item:

| 2.8 item | Disposition | Location in the original baseline |
| :---- | :---- | :---- |
| Decision 1, the v2 schema for one Epic or CRD; v1 unchanged | Already represented | §1.2 l.602–603 |
| Decision 2, one writer, model by `schema_version`, non-writing check mode | Already represented | §1.2 l.601, l.605 ("Check mode writes nothing") |
| Decision 3, paths of record for Epic and CRD | Already represented | §1.2 l.604. The HDE-CRD-0002 candidate-source path is a single-change fact outside PF12's family paths and is not added. |
| Decision 4, v2 report contents | Already represented by routing | §1.2 l.606 routes decision criteria and required content to Change Process Guide and HDE-Governance; the later-drain vocabulary is at l.644–647 |
| Decision 5, v2 manifest and its `key_outputs` minimum | Already represented | §1.2 "Generic v2 writer `key_outputs` minimum" l.942–944 |
| Decision 6, feedback-freedom kept; causal-input refusals | Already represented, plus actionable | l.605 carries the refusal list; RL-03 adds the `docs/ephemeral/` and `docs/pfcanon/` refusal (C-10). The QA-primary-path and QA-plan-check-ID exceptions are internal to the refusal, which PF12 does not detail; l.605 "The feedback-dependency refusal is kept" does not conflict. |
| Decision 7, post-verdict close-run family for admitted CRDs | Already represented | §1.2 l.668; §8.17 l.5399–5407; §8.17.1 l.5424, l.5442–5443 |
| Decision 7, extension to admitted Epics (2026-11-01, B-4) | Actionable (C-18) | RL-05, RL-15, RL-16 |
| Decision 8, absent-tolerant CRD rows | Already represented | §1.2 l.607 |
| Decision 8, extension to admitted Epics (B-3) | Actionable (C-18) | RL-04 |
| Decision 9, ADR block | Out of this target's ownership | Change Process Guide §3.5.4 (T-03); PF12 carries no ADR-block contract |
| Dependency direction | Already represented | §1.2 l.944 (no Index, path-proof, orientation or close-run digest in the manifest); §6.2.2 |
| Stated limits: QA RCA path; doc-deltas and drain-targets explicit-empty rules; byte-identical QA-root copy | Already represented | §1.2 l.615–617, l.658–662. The ADR pins the literals ("Doc Deltas: None", "Drain Targets: None") because §1.2 gives none; PF12 keeps its rule without the literal. |
| Stated limits: a tracked issue maps only through an ADR status, the schema refusing the register-pointer form; the ID form (B-1) | Actionable (C-18) for PF12's record of the v2 schema; the close report's mapping form stays with Change Process Guide §3.5.2.1 (T-03) | RL-02 |
| Stated limits: a deferral's register pointer names the register by PF title and one of its headings | Actionable (C-10) | RL-03 |
| Stated limits: pointers, including the close-run directory (B-2) | Actionable (C-18) | RL-05 |
| Stated limits: "an Epic close run needs its own explicit admission"; HDE-EPIC041 the one Epic admitted | Actionable (C-18) | RL-15 Epic bullet; RL-04 last sentence |
| Other stated limits (review-trace-only posture, QA plan mapping, closure override, PF title reading, allocation, pinned QA ledger format) | Owned by Change Process Guide, HDE-Governance, Glow QA Guide and HDE Mechanics Guide | No PF12 locus, apart from the posture at l.606, already represented |
| Epic-only identity inventory | Already represented, exact equivalence | §1.2 l.597 |
| Drainage row "§1.2 Close-pack artifacts (deterministic path-of-record; baseline artifacts) and Change-container compatibility (normative)" | Represented after RL-02 to RL-05; "Change-container compatibility" l.585–597 needs no change | — |
| Drainage row "§8.17 New standardized evidence families and Current-state evidence; §8.17.1" | Represented for CRDs at l.5346–5350, l.5390–5408 and l.5424; extended to Epics by RL-15 and RL-16. "HDE Build Notes introduced this family" (l.5407) is the title-only form of "introduced by the AQ-1 approval addendum". | — |

### C-18 — 2.8 amendment of 2026-11-01 (l.1060, l.1127), PF12's share

The ledger leaves the apportionment to each editor. PF12's share, decided here:

| Consequence | PF12 home | Redline |
| :---- | :---- | :---- |
| B-1, Epic tracked-issue ID form `ISSUE-EPIC<NNN>-TI-<nn>` beside `TI-NNN`; refusal of another Epic's ID (`TRACKED_ISSUE_UNBOUND`); the ADR-status-only mapping it keeps | §1.2 v2 schema bullet, because PF12 records the v2 schema's closed domain | RL-02 |
| B-2, an Epic may point to its own close-run directory before it exists; a CRD must point to its own; any other unresolved pointer is refused (`POINTER_UNRESOLVED`) | §1.2 same-run close evidence paragraph | RL-05 |
| B-3, absent-tolerant `epicNNN.close_report` and `epicNNN.manifest` rows with `epic_id` for every Epic in `ADMITTED_EPIC_CLOSE` | §1.2 writer bullet | RL-04 |
| B-4, the Epic close-run family, `publish_epic_close_run_family`, the QA harness's renderer, the Epic's QA family not written and refused if changed, `epic_id` on rows | §1.2 same-run paragraph; §8.17 exception; §8.17.1 `close/` | RL-05, RL-15, RL-16 |
| Admission: `ADMITTED_EPIC_CLOSE` admits HDE-EPIC041 only; another Epic needs its own row and the Product Owner's explicit admission (l.1103, l.1131) | §8.17 exception; §1.2 writer bullet | RL-15, RL-04 |
| The false current statements "No Epic close-run family is admitted" (l.668, l.5408) and "admitted CRDs only" (l.5399, l.5424) | Replaced | RL-05, RL-15, RL-16 |
| HDE-CRD-0002's close pack regenerated in #811 | History, not drained | none |

### C-20 — 2.9 (supporting)

Read in full as support for C-18. It confirms B-1 to B-4 and their owner tests, the explicit admission of HDE-EPIC041's close run, and the nine close-run primaries with `epic_id`. CCR-5 in 2.9 is held (H-06) and has no PF12 locus: PF12 states no ordering between the close-pack write and the closure decision.

### C-29 — 2.16 status, R-1 and R-2 (uncertain; actionable by context in r4)

The handoff routes C-29 to PF12 "only if PF12 itself restates a retired GATE:CORE-DET evidence entry". PF12 was searched (decoded text, escapes removed) for every entry 2.16 R-2 retires: `make_compat_determinism`, `IDENTITY_OK.txt`, `artifacts/cards`, `preimage_recompute_and_compare`, `ab_ba_parity_bytecompare`, `two_run_identity_bytecompare`, `fixtures/composite`, `abba_compare`, `CORE-DET` and `GATE:`. Each search found 0 occurrences. `ci/jobs/` occurs only at l.3323–3324 (`logs_keys_only_redaction.yml`, `rails_open_conformance.yml`), which R-2 does not name. Under that condition alone, r3 found no PF12 home and reported the context bearing for Nathan.

By context (GTWPE-D3), and at Nathan's direction for r4, 2.16 bears on PF12 §8.6.3.3 "Compat closure artifacts" (l.3060–3064), which presents `artifacts/compat/AB.json`, `BA.json` and `identity_hash.txt` as governed compat proof artifacts without qualification. 2.16's facts (l.1896–1899) record that `scripts/make_compat_determinism_artifacts.py` checked the placeholder `compat_public`, that HDE-EPIC040 PR-04 (#467) replaced it with the real calculation, that the generator has exited 2 since, and that its stored outputs are placeholder-era captures. R-1 (l.1921) defines GATE:CORE-DET evidence as the real compat path only, and R-2 (l.1937) keeps the captures "as they are, as history".

| Item | Disposition | Location |
| :---- | :---- | :---- |
| The compat closure captures are placeholder-era history, not evidence of the current compat calculation; current GATE:CORE-DET evidence is the real compat path | Actionable, CLARIFY | RL-12, a run-in block after the `identity_hash.txt` bullet (gap before original l.3066) |
| The generator exits 2 | Actionable, as a stated fact | RL-12. Inspected read-only: the generator prints `compat_public not implemented` and exits 2 (l.18–19). |
| HDE-EPIC030 PR-03 reuses `AB.json` and `BA.json` (l.3118–3119, l.3127–3128) | Actionable, one sentence | RL-12 last sentence; the PR-03 entry itself is unchanged |
| The retired entries as general rules, and HDE Governance §12.2, Appendix B.2, D.1 and D.3 | Out of this target's ownership | HDE Governance (T-01) |
| The generator, its exit-2 test and the captures stay as they are | Already represented by no-change | RL-12 changes no path, key or binding; the existing MUST rules for the captures' bytes and parity stay. |

Claim posture: RL-12 uses no MUST or MAY. It describes standing, and routes the definition of GATE:CORE-DET evidence by title to HDE-Governance and HDE Build Notes.

### C-02 — 2.1 D-2, vendor route selection (added by Nathan's direction for r4)

The ledger routes C-02 to T-02, T-05, T-07 and T-08, not to T-04. r3 reported its PF12 context bearing for Nathan (§13), and Nathan directed the fix. D-2 decides that only a terminal, case-sensitive `v1` base selects the legacy `bodygraphs` route, as retained legacy selection and not fallback, and that every other non-v2 base fails closed. It keeps the label `explicit_legacy_fallback` as an existing wire value that "makes no fallback claim", leaves name corrections to the owners of tests and evidence in the implementing change, and keeps frozen HDE-EPIC036 and HDE-EPIC037 captures as history.

| PF12 wording | Disposition | Location |
| :---- | :---- | :---- |
| §8.6.3.10 required proof contents: "an explicit legacy fallback" (l.3733), "whether any legacy fallback remains" (l.3738), "any legacy fallback or vendor-route gap that remains" (l.3749) | Actionable, CLARIFY, by a section-wide reading rule rather than rewording each bullet | RL-13, "Legacy route reading (normative)." (gap before original l.3752) |
| Mapped-cache family: "legacy non-v2 fallback preservation" (l.3772) | Actionable, CLARIFY | RL-14. The key `epic038.pr05.v2_mapped_cache.legacy_fallback` and file `legacy_fallback_preservation.log` (l.3762) keep their names. Inspected read-only: the predicate `explicit_legacy_fallback` is computed from a run with `HD_API_BASE_URL` `https://fixture.invalid/v1` (`tools/evidence/generate_v2_mapped_cache_evidence.py` l.267, l.275), so it holds under D-2. |
| HDE-EPIC036 family: "non-v2 explicit legacy fallback" and "explicit legacy fallback" (l.3778, l.3784, l.3788) | Covered by RL-13's frozen-capture sentence; no rewording | These artifacts record HDE-EPIC036's posture at capture time. |
| HDE-EPIC037 legacy-fallback snapshot (l.3823–3824) and key (l.3932) | Covered by RL-13; names kept | Frozen captures, as D-2 says |
| HDE-EPIC038 OPS-02 packet: key `legacy_fallback_preservation_log` (l.3414) and "legacy-fallback observations recorded for OPS-02" (l.3421), in §8.6.3.9 | No change | Retained OPS evidence that names recorded observations. D-2 says governed evidence bytes need no regeneration and names are corrected by their owners. |
| Route selection rules themselves, the configured-base boundary, and the §7.2.0 gap | Out of this target's ownership | HDE CLI/API/Vendor Ref §7.1.10 (T-02); RL-13 routes to it by title |

Claim posture: D-2's basis records that the current classifier reads any path segment, case-folded (2.1 l.304), and its implementing change is not recorded as delivered. RL-13 therefore says that the section "does not assert that the current route classifier already enforces the terminal-segment rule".

### Product Owner-directed corrections (r4)

Authorized by Nathan's direction of 2026-11-02 (§1). No source file justifies these; TW-DRAIN-10 allows hygiene with Nathan's authorization in the handoff.

| Defect | Disposition | Location |
| :---- | :---- | :---- |
| §5.3 "Current repository posture" gives `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` as the current `release_id` (l.1959); the current manifest digest is `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` | CONSISTENCY | RL-06 replaces the digest only. Verified read-only: SHA-256 of `catalog/manifest.json` at `e2b7427` and at `origin/main` `84d6d1c`; `python scripts/release_id_recompute.py --check-manifest-only` exit 0 under closed rails (§8). PF12 §9.6 (l.6109–6110) already records this value as prior and computed `release_id`. |
| §5.3 historical cuts table: l.1970 labels PR06b "current"; the HDE-CRD-0002 refreshes are missing | CONSISTENCY | RL-07: PR06b keeps its row and digest without "current"; a new last row records the HDE-CRD-0002 same-version refreshes and the current digest, as HDE CRD Records states (§2). The intermediate digests are recorded there only as prefixes, and the row says so. |
| l.1968: a Unicode ellipsis after the recorded prefix `988ed2a7`, which PF03 §3 prohibits | DOC\_HYGIENE, inside RL-07 | "Recorded identity prefix `988ed2a7`; the source supplies only this prefix, not a full digest." |
| l.2144 ends with a doubled period | DOC\_HYGIENE | RL-09 removes one period |

### Doc-Delta hook

PF12 §9.1 requires a Doc-Delta when governed evidence rules change, and §§9.5 and 9.6 set the documentary drainage record form. RL-17 adds §9.7 in that form (NEW\_CANON), with `document_version: "v2.9.8"`, `date: "2026-11-02"` and a `change_log_entry` naming `v2.9.8 / 2026-11-02`. Following §0.2, the record cites HDE Build Notes by title and keeps addendum IDs and versioned identities in this log. Its release-identity fields carry the SHA-256 of the unchanged `catalog/manifest.json` at `e2b7427`, `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, computed read-only. In r4 the record also covers C-02, C-29 and the Product Owner-directed corrections, and its validation list adds the manifest check, the generator inspection and the mapped-cache predicate inspection.

## 6. Uncertainty decided in this session

- The owner of the C-05 Evidence Catalog entry is PF12. The heading "Canonical JSON and topology" exists only in PF12 §8.6.3.2 (`git grep` over `origin/main` `docs/pfcanon/`). PF12 §0.2 makes §§8.3 and 8.6 the single home of the Evidence Catalog, and other PF documents must not keep parallel path lists. The row-content rule has one home (§1.2, RL-01); the catalog entry points to it (RL-11).
- C-29 has no PF12 home under the handoff's condition, but bears on PF12 §8.6.3.3 by context; r3 reported that bearing, and r4 drains it at Nathan's direction (§5, C-29).
- C-02 bears on PF12 §8.6.3.10 by context; r4 drains it at Nathan's direction (§5, C-02).
- C-07 bears on PF12 §8.3 by context and drains there as a clarification (§5, C-07).

## 7. Held, out-of-scope and routed items

- H-07 (CCR-1 / P-2), held: whether a tokenless Epic needs an acceptance map. It waits for the Product Owner's decision (2.10 l.1299, as the ledger records it). PF12 "Optional token compatibility" (§8.6.1, l.2818–2824) and "Acceptance map — legacy token compatibility shape" (l.2873–2884) are left unchanged.
- H-06 (CCR-5), held by the ledger: no PF12 locus.
- H-10 (item 9 CRD identity and Specification): nothing to drain; RL-08 and RL-01 carry their nonclaims instead.
- Owned elsewhere, not drafted here: D-4 `--log-path` (HDE Governance §4.1.8, HDE Mechanics Guide §27.5); D-5 §2.0.10 (HDE Governance); R-1 and R-2 as general rules (HDE Governance §9.1.2, §9.1.3; Plan Templates); R-3 and the close-pack test (Plan Templates); 2.8 decision 9 and the close report's deferral and tracked-issue mapping forms (Change Process Guide); 2.16's retired entries as general rules (HDE Governance); D-2's selection rule, configured-base boundary and §7.2.0 gap (HDE CLI/API/Vendor Ref), and its HDE Mechanics Guide, HDE Users Guide and Plan Templates targets (T-05, T-08, T-07).

## 8. Read-only repository inspection

All at `e2b7427ff418ca8f08f05587c4a541308a76da56`, with `git show`, `git grep` and `git ls-tree`, unless stated. Nothing was written. One read-only check was executed for r4, as stated below.

- `tools/evidence/update_evidence_index.py`: `ADMITTED_CRD_QA` (l.51) maps HDE-CRD-0001 and HDE-CRD-0002; `ADMITTED_EPIC_CLOSE` (l.62) maps only `"HDE-EPIC041": ("audit/qa/hde-epic041", "audit.qa.hde_epic041")`; `publish_crd_close_run_family` (l.5439) and `publish_epic_close_run_family` (l.5568) exist; Epic close-run entries use `f"{key_prefix}.close.{check_id}.primary.log"`, `role: "log"` and `epic_id`; Epic close-pack keys are `"epic" + <NNN>` with suffixes `close_report` and `manifest`.
- `docs/evidence/INDEX.json` (678 rows): `epic041.close_report`, `epic041.manifest` and the nine `audit.qa.hde_epic041.close.<check_id>.primary.log` rows carry `epic_id: HDE-EPIC041`; the nine HDE-CRD-0002 close-run rows carry no `crd_id` in the Human Index, so RL-15 claims `epic_id` for Epic rows only. No row binds a path under `docs/ephemeral/` or `docs/pfcanon/`, and neither does any record of `artifacts/evidence_index.jsonl`.
- `audit/qa/hde-epic041/close/final-lf/primary.log` and `audit/qa/hde-crd-0002/close/final-lf/primary.log` both open with a `pf27.step_log_header.v2` header, so the existing header bullet applies to both families unchanged.
- `schemas/close_candidate_source.v2.json`: the required properties include `planning_records`, `requirement_ids`, `qa_checks` and `qa_verdict`; there is no plan-path property; `ti_id` is `^(?:TI-[0-9]{3,}|ISSUE-EPIC[0-9]{3}-TI-[0-9]{2,})$`.
- `tools/qa/generate_epic_close_pack.py`: the refusal codes `PLANNING_OR_CANON_INPUT_PROHIBITED` (l.2351) and `TRACKED_ISSUE_UNBOUND` (l.2721, l.2727) exist.
- `audit/` holds `EPIC-041_close_candidate_source.json`, `EPIC-041_close_report.md`, `EPIC-041_MANIFEST.json` and the matching HDE-CRD-0002 files.
- `catalog/manifest.json`: version 1.3.0, built 2026-08-24T18:04:49Z, 45 members, SHA-256 `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`; the same SHA-256 at `origin/main` `84d6d1c`.
- r4: `env LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 python scripts/release_id_recompute.py --check-manifest-only`, on the working tree whose `catalog/manifest.json` equals `origin/main`'s, returned exit 0 with no output, and `git status` showed no change. Its `check_manifest_only` path (l.347–355) only reads the manifest and prints problems.
- r4: `scripts/make_compat_determinism_artifacts.py` prints `compat_public not implemented` and exits 2 (l.18–19); it was not run. `artifacts/compat/` holds `AB.json`, `BA.json` and `identity_hash.txt`, each with a sibling path proof.
- r4: `tools/evidence/generate_v2_mapped_cache_evidence.py` computes `explicit_legacy_fallback` (l.275) from a run with `HD_API_BASE_URL` `https://fixture.invalid/v1` (l.267); it was not run.

These observations support the drafted wording only. They are not QA, not a test run, not governed evidence and not proof of behaviour. `tools/evidence/build_release_attestation.py`, `tools/evidence/run_canonical_json_gate.py` and the vendor route classifier were not inspected; RL-08, RL-01 and RL-13 assert nothing about their current behaviour.

## 9. Redline summary (r4)

| ID | Operation | Original location | Rows | Change |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | INSERT | §1.2, gap before l.551 | C-05 | New run-in block "Governed gate check row content (normative)." |
| RL-02 | REPLACE | §1.2 l.603 | C-10, C-18, C-17 | v2 schema bullet gains the tracked-issue ID form and ADR-status-only mapping; new bullet for the v2 planning-record fields |
| RL-03 | REPLACE | §1.2 l.605 | C-10, C-17 | Planning and PF-Canon input refusal; deferral register pointer by PF title and heading; write-time PF title resolution; check mode reads no PF-Canon file |
| RL-04 | REPLACE | §1.2 l.607 | C-18, C-17 | Absent-tolerant Epic close-pack rows for `ADMITTED_EPIC_CLOSE` |
| RL-05 | REPLACE | §1.2 l.668 | C-18, C-17 | Same-run close evidence for an admitted CRD or Epic; close-run pointer rule |
| RL-06 | REPLACE | §5.3 "Current repository posture" l.1959 | Product Owner direction | Current `release_id` updated to `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` |
| RL-07 | REPLACE | §5.3 historical cuts table l.1968–1970 | Product Owner direction | Ellipsis removed from the PR06 row; PR06b no longer "current"; new row for the HDE-CRD-0002 same-version refreshes |
| RL-08 | REPLACE | §6.2.1 l.2049 | C-04 | Builder output-root ownership: exclusive claim, no symlink writes, scoped cleanup |
| RL-09 | REPLACE | §6.4 l.2144 | Product Owner direction | Doubled period removed |
| RL-10 | REPLACE | §8.3 "Governed locations only." l.2262 | C-07, C-10 | No Mirror record, Index row or path proof binds a `docs/ephemeral/` or `docs/pfcanon/` path |
| RL-11 | REPLACE | §8.6.3.2 l.2971–2972 | C-05 | Evidence Catalog entries point to the §1.2 row rule |
| RL-12 | INSERT | §8.6.3.3 "Compat closure artifacts", gap before l.3066 | C-29 | New run-in block "Standing of the compat closure captures." |
| RL-13 | INSERT | §8.6.3.10, gap before l.3752 | C-02 | New run-in block "Legacy route reading (normative)." |
| RL-14 | REPLACE | §8.6.3.10 l.3772 | C-02 | Mapped-cache family proves preservation of the terminal-v1 legacy selection, under its existing names |
| RL-15 | REPLACE | §8.17 l.5399–5408 | C-18, C-17 | Close-run family exception covers admitted Epics |
| RL-16 | REPLACE | §8.17.1 l.5424 | C-18, C-17 | `close/` bullet covers admitted Epics |
| RL-17 | INSERT | §9.6 end, gap before l.6165 | C-02, C-04, C-05, C-07, C-10, C-17, C-18, C-29, Product Owner direction | New §9.7 documentary drainage record |

Mapping from r3: RL-01 to RL-05 keep their IDs; r3's RL-06 to RL-11 are r4's RL-08, RL-10, RL-11, RL-15, RL-16 and RL-17. RL-06, RL-07, RL-09, RL-12, RL-13 and RL-14 are new. The operations carried over from r3 are byte-identical, except RL-17 (r3's RL-11), whose record text covers the new changes.

## 10. Producer validation

A local script resolved every operation against the unchanged original (decoded as UTF-8; offsets are character offsets), checked the batch, and simulated one-pass application by original position.

| ID | Operation | Expected | Observed | Span or gap (characters) | Old length | New length |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | INSERT | 1 | 1 (BEFORE 1, AFTER 1) | gap 42,968 | — | 974 |
| RL-02 | REPLACE | 1 | 1 | 47,027–47,259 | 232 | 1,134 |
| RL-03 | REPLACE | 1 | 1 | 47,570–48,072 | 502 | 1,107 |
| RL-04 | REPLACE | 1 | 1 | 48,350–48,766 | 416 | 870 |
| RL-05 | REPLACE | 1 | 1 | 53,920–54,660 | 740 | 1,164 |
| RL-06 | REPLACE | 1 | 1 | 182,071–182,564 | 493 | 493 |
| RL-07 | REPLACE | 1 | 1 | 183,398–184,002 | 604 | 1,032 |
| RL-08 | REPLACE | 1 | 1 | 190,147–190,560 | 413 | 1,505 |
| RL-09 | REPLACE | 1 | 1 | 198,510–198,744 | 234 | 233 |
| RL-10 | REPLACE | 1 | 1 | 210,464–210,690 | 226 | 461 |
| RL-11 | REPLACE | 1 | 1 | 256,293–256,424 | 131 | 245 |
| RL-12 | INSERT | 1 | 1 (BEFORE 1, AFTER 1) | gap 265,592 | — | 671 |
| RL-13 | INSERT | 1 | 1 (BEFORE 1, AFTER 1) | gap 365,753 | — | 883 |
| RL-14 | REPLACE | 1 | 1 | 367,637–368,279 | 642 | 756 |
| RL-15 | REPLACE | 1 | 1 | 587,223–589,738 | 2,515 | 3,225 |
| RL-16 | REPLACE | 1 | 1 | 590,517–590,721 | 204 | 249 |
| RL-17 | INSERT | 1 | 1 (BEFORE 1, AFTER 1) | gap 630,886 | — | 9,871 |

- Conflicts: none. No replaced spans intersect or touch, no insertion gap lies at or inside a replaced span, and no two insertions share a gap. RL-06 and RL-07 are separate operations in §5.3 with untouched text between them (l.1960–1967).
- Operation dialects: only `REPLACE` and `INSERT`. No repeated-replacement operation, so the RL-045 rule does not arise.
- Post-simulation: each replacement or insertion text occurs exactly once in the output. Each replaced old block occurs 0 times, except RL-10's, which occurs once as the unchanged opening of its own replacement; RL-10 appends one sentence.
- Simulated output: 658,173 bytes; 6,441 lines; ends with LF; SHA-256 `a0308f1d4e86589e485ff6775d77d571acd93e009b5402109f9f6df63790ae4d`. This is a preparation-time simulation, not the final PF; TW-APPLY-10 also derives the header.
- The simulated output keeps `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` in two places only: the PR06b row (RL-07) and the 2026-10 record's `prior_release_id` and `computed_release_id` (l.5992–5993), which is dated history. No other current-identity statement in PF12 names a digest (searched for "current" near `release_id`).
- The §9.7 record's YAML block in the simulated output parses (12 documented contracts, 8 validation entries, `document_version` v2.9.8, `date` 2026-11-02).
- Saved-file revalidation: recorded in §15.
- Editorial checks on the new text: no ASCII three-period or Unicode ellipsis (the one Unicode ellipsis in the package is inside RL-07's exact old block, which quotes the original); no `Draft`, TODO, placeholder or drafting note; HDE Build Notes cited by title only; no PF version or addendum number in new prose; MUST and MAY used only for normative requirements; HDE CLI/API/Vendor Ref and HDE-Governance named by title only, as PF12 names them elsewhere.
- Hygiene scan of the original for markers TW-DRAIN-10 requires removed (Draft status language, TODO, unresolved drafting note): none found. `SCHEMA-DRAFT`, `Draft-07` and `[OPEN]` are canon names or conventions. The original holds one Unicode ellipsis (l.1968), removed by RL-07.

## 11. Corrections made during preparation

Each correction was made by this preparer. Apply received r2 and returned it, applied r3, and now receives r4.

1. Within r1: the heading paths were first written by hand. RL-01's wrongly began at §0, and the §8.17 paths quoted the heading inexactly. The builder now derives every heading path from the raw original headings, outside code fences. Payloads were unchanged, and the package was rebuilt and revalidated.
2. r1 to r2. r1 was committed and pushed as `324de26`. Before Apply, the ledger commit `a3632c0` brought GTWPE-D3 to this session's attention ("all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target"). r1 had read C-07 only through l.525's "require" test and found nothing to change. Re-examined by context, R-1 and R-2 bear on PF12's own Mirror path rules (§8.3), so r2 adds the §8.3 clarification (now RL-10). The same review added two supported precision points inside sections already being edited: RL-02 states that a tracked issue maps only through an ADR status, and RL-03 that a deferral's register pointer gives a heading. The record's text and rows were updated to match, and the D-4 `--log-path` disposition now rests on single-home ownership (HDE Governance §4.1.8). r2 was fully revalidated. r1 remains in Git history at `324de26`; nothing was deleted to hide it.
3. r2 to r3, on a returned Apply diagnostic. TW-APPLY-10 validated r2 at `2a2325b` and found all eleven operations and the derived header plan valid. It stopped with zero edits because the package's baseline byte shape was wrong (`PF12-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`, commit `5716f60`): the redlines file (line 25) and this log (§3) said the original "ends with one LF", but its last two bytes are LF LF, with a final empty line. The diagnostic was checked against the original's raw bytes and is correct. r3 corrected that statement in both files and recorded the new revision identity. No operation, payload, anchor or count changed. The saved r3 file reproduced the r2 simulation `07331ff4e0c41b1acb75fafb2718624d9d692a8adfaac38b1da71dc34ffe83f1` exactly. The unchanged PF was not edited during the returned attempt.
4. r3 to r4, at Nathan's direction. TW-APPLY-10 applied r3 (commit `5c10ee5`), and this session reported the four observations r3 recorded in §13, plus a cosmetic defect in the r3 package: its informative locators for RL-08 and RL-09 said "line 2971–2972" and "line 5399–5408". Nathan then directed: "fix the defects and inconsistencies you noticed". r4 adds six operations for those observations: C-02 (RL-13, RL-14), C-29 (RL-12), and the Product Owner-directed corrections (RL-06, RL-07, RL-09). It renumbers the batch by original position, updates the §9.7 record (RL-17), and corrects the informative locator wording to "lines" for every multi-line block (RL-07, RL-11, RL-15). The eleven r3 operations are otherwise byte-identical. The whole batch was revalidated against the unchanged original (§10). The revised PF that r3 produced is replaced by TW-APPLY-10's application of r4 at the same output path; r3 and its application remain in Git history at `4c859cc` and `5c10ee5`.

## 12. Constraints, assumptions and interpretations

- New text is normative contract text (`[Required-Now]` posture). For D-4 and D-5, whose implementing change is open, and for D-2, whose implementing change is not recorded as delivered, each addition says plainly that it does not assert current enforcement.
- The Epic admission sentence names HDE-EPIC041 as the only current row, as 2.8 l.1103 does and as the inspected table shows. It will need maintenance when another Epic is admitted, as did the replaced sentence "No Epic close-run family is admitted".
- RL-05 renames the run-in label "Same-run close evidence for a CRD (normative)." and RL-15 renames "(normative; admitted CRDs only)". Neither is a section heading, and no other PF document cites either label (`git grep` over `docs/pfcanon/` on `origin/main`). Keeping them would leave false labels.
- The §9.7 record cites its proof-log path under `docs/ephemeral/` as a reference only, as §9.6 does; under 2.2 R-1 a prose citation of a planning document in a permanent record is a reference. RL-10 constrains Index, Mirror and path-proof records, not PF prose.
- RL-13 is a reading rule for §8.6.3.10, placed after the required-proof bullets and before the evidence families, so that every legacy-fallback wording, label and name in the section reads as D-2 decides without rewording frozen artifact descriptions. It cites HDE CLI/API/Vendor Ref by title only, as PF12 does elsewhere (for example l.165, l.3058).
- RL-07's new row cites HDE CRD Records by title, as PF12 does at l.590, l.5308 and l.6095. The intermediate refreshes are recorded there as prefixes only, so the row records prefixes and says so.
- This package edits no PF canon. The revised PF exists only as TW-APPLY-10's output under `docs/ephemeral/`.

## 13. Observations for Nathan (not acted on in this task)

- The four observations r3 recorded here (C-02 and 2.16 bearing on PF12, the stale §5.3 `release_id`, the l.1968 ellipsis and the l.2144 doubled period) are acted on in r4 (§11 item 4).
- HDE CLI/API/Vendor Ref still says, in its summary list (l.119), that "non-v2 bases retain an explicit legacy `bodygraphs` fallback", which conflicts with its own §7.1.10 and with D-2. That document belongs to T-02; it is not edited here.

## 14. Header provenance for TW-APPLY-10

Baseline header (§0.1): Title PF12-Canon-HDE-Schemas-and-Artifacts; Version v2.9.7; Status Canon; Effective date 2026-10-26; Last Update Gate "BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md"; Invocation tag INV-f2ac55d77ce9aacc. Each line but the last ends with two spaces.

Source that justified the update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, version v14.0.5. No other file was a change source; the closure records it relies on are inside that same file (2.10). RL-06, RL-07 and RL-09 rest on Nathan's direction in this session, which is an authorization, not a source file. HDE CRD Records and HDE CLI/API/Vendor Ref were read in support only.

Version scheme: v2.9.5, v2.9.6, v2.9.7 (§§9.5, 9.6); expected derived version v2.9.8. RL-17 names v2.9.8 and the preparation date 2026-11-02. No redline touches §0.1.

## 15. Save verification and completion receipt

Save outcome for r4: `COMPLETE_PACKAGE`. Both required files are in `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/` and were read back in full from disk before this receipt was written:

- the redlines file (r4): 54,695 bytes; 699 lines; SHA-256 `c45c20a53334e5a2eba96ee80da8494b4c3497de054cf73188ed2cb1dd169f44`; ends with `END OF REDLINES`. A separate script parsed the saved file by its literal-block convention, re-resolved all seventeen operations against the original (each count 1) and re-simulated one pass, reproducing SHA-256 `a0308f1d4e86589e485ff6775d77d571acd93e009b5402109f9f6df63790ae4d` exactly. The read-back found one wrong location description (RL-09 placed its paragraph after a token list that follows it); the builder was corrected, the file rebuilt and saved again, the changed lines read back, and the re-simulation repeated with the same result.
- this proof log: read back in full; the read-back found two wrong statements (§6 named RL-08 for the catalog entry, and §13 said D-2 supersedes a sentence it does not name), both corrected before this receipt. After that, only this receipt was added, and it was read back too.

The two files agree on the original and source identities, the run identity and revision, the preparer and the `READY` outcome. The package is ready for fresh validation by TW-APPLY-10. Apply's inputs are the exact original, these two files, ledger rows C-02, C-04, C-05, C-07, C-10, C-17, C-18 and C-29, the selected source units in §4, Nathan's direction of 2026-11-02, branch `claude/gtwpe-triage-authoring-j94ewf`, and the output directory above. The commit that holds r4 is reported in the session's final response and in the ledger's T-04 row; this log does not carry its own commit.
