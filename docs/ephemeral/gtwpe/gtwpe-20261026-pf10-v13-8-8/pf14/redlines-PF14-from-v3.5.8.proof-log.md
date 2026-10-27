# T-PF14 — proof log for the redlines from PF14 v3.5.8

This is the processing report for `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf14/redlines-PF14-from-v3.5.8.md`. It records how that redlines file was prepared, what it rests on and what was verified. It is not QA, acceptance, canon adoption or closure.

## 1. Identity

| Field | Value |
| :- | :- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf14/redlines-PF14-from-v3.5.8.md`, 37,476 bytes, 379 lines, SHA-256 `ea1c20e710d149bc5c5fa3af1a3f353f1c2708fa6b5c47de8019a079ee84f6d3` |
| Run | `gtwpe-20261026-pf10-v13-8-8/T-PF14`, preparation revision `P1` (first and only preparation) |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff, fetched live in this session (page state as of 2026-10-09T11:05:22Z; matches the ledger's pin) |
| Next step | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b, authorized by Nathan's handoff to run in this same session |
| Originating preparer | TW-DRAIN-10 in the Nathan-started T-PF14 document session, Claude Code cloud session https://claude.ai/code/session_017fZuKCTMJn4EwZYu5ENvh1. No subagent, reviewer or other session took part |
| Preparation time | 2026-10-26, completed about 21:52Z |
| Preparation outcome | `READY` |
| Save completeness | recorded in §9 after read-back |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0ebb2f80a416fb004b9a913da592d1`, equal on `main`); task `T-PF14`; rows A06, A07, A10, A15, A26, X07 |
| Destination | branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, shared draft PR [#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761). #760 merged at 2026-10-26T21:18:51Z, so the ledger's continuation route applies; the T-PF07 session had already created the branch and opened #761, and this session reuses them |

## 2. Target

| Field | Value |
| :- | :- |
| Path | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md` |
| Logical title and version | `PF14-Canon-HDE-Mechanics-Guide` v3.5.8, Status Canon, Effective date 2026-10-09 |
| Repository identity | `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a` (the handoff baseline); byte-identical at the current `main` `0838ba08254eaefc888019df49a06aa2ae99cc6c` (the only change between them is the ledger) |
| Bytes | blob `3360a9eb1a5056274a31ad36739df8b04a4864c3`; 663,440 bytes; 7,722 LF characters, so 7,723 lines with no final LF on line 7,723; LF only, no CR; longest line 908 bytes |
| SHA-256 (raw bytes) | `0fb34a6534f685eb7abeeaab43e848f02e780d903507a597cee669678257b63a` |
| Newer version on `main` | none; `docs/pfcanon/` holds only this PF14 file |

Complete reading. The whole target was read in 15 contiguous line-aligned windows from a scratch copy of the blob, each about 45 KB, under the line-length limit of the reading tool: lines 1–364, 365–837, 838–1234, 1235–1802, 1803–2299, 2300–2904, 2905–3425, 3426–4003, 4004–4780, 4781–5352, 5353–5833, 5834–6295, 6296–6682, 6683–7278 and 7279–7723. The windows' byte counts sum to 663,441: the file's 663,440 bytes plus one phantom LF for the unterminated last line. No window was truncated, and no line exceeds 908 bytes.

## 3. Sources and their roles

Change source (the only one): PF10 v13.8.8, `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, 729,539 bytes, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`, effective 2026.10.26, the sole unlettered logical representation on `main`. Read in full at these boundaries, each from its heading to the next heading of the same level:

* front matter, precedence rules §1–§9, cross-references, template and Addendum Index, lines 1–223;
* 2.6 (A06), lines 531–687;
* 2.7 (A07), lines 688–889;
* 2.10 (A10), lines 1102–1204, read in two windows (1102–1139 and 1140–1204);
* 2.15 (A15), lines 1620–1690;
* 2.26 (A26), lines 2900–2986.

Supersession applied (front matter §5): 2.18 withdraws the cost-ceiling passages of 2.11 to 2.16, including 2.15's sentence on a projected pass of the unit's cost ceiling, which bears on no PF14 text. 2.17 amends 2.15; it was read in full (lines 1826–1955) as supporting reading: it supersedes 2.15 C-3 for pointer items only, extends C-1 and 2.15's approved design by its table, and, under "Does not change", keeps the close-run family and its `close/`-only membership exception. 2.14's narrowing of 2.11 rules 7 and 8 and 2.11's misnumbered cross-references bear on no PF14 change.

Supporting cross-references, each read only at its ledger boundary as supporting reading, not as a change source in its own right (ledger "Source register"):

| Ref | File and blob | Read | Used for |
| :- | :- | :- | :- |
| X03 | `docs/adr/hde/close_pack_writer_adr.md`, blob `2d91679a1981` | lines 1–35 (status, amendment notes, Problem, Decision items 1–9) and 76–91 ("Affected canon and drainage consequences") | The two HDE Mechanics Guide rows of the canon table and the Decision items they rest on (2, 3, 5, 7) |
| X04 | `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md`, blob `1d6a92a483e2` | §18, lines 751–794 (boundary 753–792 plus two lines of context) | The §34 stale statements and the `/api/reader?v=1` alias row |
| X06 | `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.0.md`, blob `20b170490447` | §10, lines 154–167 (boundary 156–165) | §34 among the stale canon passages, and its pointer to plan §19 |
| X07 | `docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.0.md`, blob `b083486fc768` | §5, lines 252–276 (the "CR-11 — decided" block, 256–274) | The CR-11 decision, its change and its HDE Mechanics Guide §1.6.3 drainage target |

Further supporting reading, bounded and named so that no reading is implied beyond it:

* PF10 v13.8.8 addendum 2.35: its heading (line 3725) and lines 3808–3822 only, to confirm that 2.35 lists CR-11 among its canon drainage items. The rest of 2.35 was not read.
* `docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-plan-v1.0.md` (blob `54809ffbaf34`) §19, lines 717–740: the plan §19 that X06 points to. Its §34 row names "the production mount of the dev routes".
* `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md` (HDE-CLI-API-Vendor-Ref): lines 2071 and 2420 (§5.4 "Production mount" and the `/api/reader` method contract), plus a search of its `/api/reader` lines.
* `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` (blob `504712df548a`), read in full, lines 1–633, as the common editorial standard.
* Closure evidence. The ledger's "Precedence and closure controls" record HDE-CRD-0002 as closed. A bounded read of X11, `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md` (blob `2260eae17974`), lines 16–19, confirms `decision: CLOSE` by Isis at 2026-10-26T16:40:00Z. The blob identities of X10 to X14 were checked against `main`; their bodies were not otherwise read.
* Canon-first search (AGENTS.md "Canon-first rule"). `git grep` on `origin/main` across `docs/pfcanon/` covered `ADMITTED_CRD_QA`, `publish_crd_close_run_family`, close-run, Step-0B, `dev_start_reader`, the §34 and §1.6.3 references, `generate_epic_close_pack` and `key_outputs`. Hits outside PF10 and PF14 were inspected at line level only. They establish that Plan Templates owns Step-0B (its "Step-0B — Doc Delta Capture" template, including the no-deltas determination and preservation rules), that the Change Process Guide restates Step-0B preservation, and that HDE Governance §2.0.19 and HDE Schemas & Artifacts own the governance and schema homes of the close-pack `key_outputs` shape. No hit changes a PF14 drain.

Current-repository inspection (read-only, at `main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`, whose code tree equals `9dda63d`):

* `scripts/dev_start_reader.sh` (26 lines): defaults, `APP_ENV` propagation, `<UNSET>` display, banner `host=127.0.0.1`;
* `adapter/http_reader.py`: `_reader_dev_env_explicit` (exact `APP_ENV == "dev"`), `_reader_method_not_allowed`, `_PRODUCTION_DEV_WRITER_ROUTES`, `_PRODUCTION_RETIRED`, `_mount_for_production`, `get_reader_api_bp`, `get_reader_bp`, `create_app`, and the `__main__` run call (`host="127.0.0.1"`, `PORT` default `8000`, `debug=False`, `use_debugger=False`, `use_reloader=False`);
* `adapter/env_guard.py` `_compute_env_mode` and `_PROD_ALIASES`; `adapter/factory.py` and `adapter/wsgi.py` blueprint registration;
* `tests/http/test_reader_a7_transport.py`: `test_dev_runner_binds_loopback_with_debugger_and_reloader_off` and `test_dev_runner_emits_no_cors_headers` (definitions only, not executed);
* a case-insensitive search for `cors` and `Access-Control` in Python modules under `adapter/` and `engine/http/`, which returned no line;
* `docs/ENDPOINTS_CATALOG.json` (18 records) and `.devcontainer/devcontainer.json` (`DEV_SAMPLER_URL`);
* `tools/evidence/update_evidence_index.py`: `ADMITTED_CRD_QA`, `_crd_qa_entry`, `_load_crd_qa_entries`, `_crd_close_run_entry`, `_crd_close_run_check_ids`, `_crd_close_pack_entries`, `publish_crd_check_family`, `publish_crd_close_run_family`;
* `tests/evidence/test_evidence_index_missing_state.py`: the unadmitted-ID refusals (definitions only);
* `tools/qa/generate_epic_close_pack.py`: `CHANGE_RE`, `_derived_paths_v2`, `_supporting_paths_v2`, `_require_v2_semantics`, CLI arguments; `audit/HDE-CRD-0002_MANIFEST.json` `key_outputs`; `audit/HDE-CRD-0002_close_report.md.path_proof.txt` format; `audit/qa/hde-crd-0002/` contents; `audit/docdeltas/hde-crd-0002_*`.

Static inspection proves checked-in bytes only. No test, tool, service or CI run was executed, and no runtime, QA, deployment or acceptance state is claimed.

## 4. Coverage and disposition ledger

Every change in the selected units is accounted for below. "Out of target" means the change belongs to another PF document's task in the ledger, which carries it.

| Row | Selected change | Disposition | Target location |
| :- | :- | :- | :- |
| A06 | Doc-delta candidate: after S10, §34 "Current repository posture" says the Reader handler treats missing `APP_ENV` as dev | Redline RL-008 | §34, lines 4944–4951 |
| A06 | CR-6 decided (a), canon governs: the start-helper passages stand, among them the HDE Mechanics Guide passage "Dev Reader start helpers (APP_ENV propagation)" and §34's required start command | No change; already represented. 2.6 locates the helper passage in §5.6, but in v3.5.8 it sits under §5.8 "Dev sampler HTTP harness" | §5.8, lines 1682–1687; §34, lines 4932–4934 |
| A06 | RP-3, RP-2, VERIFY.sh, repository documents | Out of target: no PF14 change named; repository items are not PF canon | none |
| A07 | §34 "Current repository posture": bind, flags, CORS, `APP_ENV` default | Redline RL-008; consistency redlines RL-006 and RL-007 remove two sentences that hedge the now-delivered bind | §34, lines 4930, 4936, 4944–4951 |
| A07 | §34 route table's `/api/reader` alias row | Redline RL-005 | §34, line 4915 |
| A07 | AD-2's exact `APP_ENV=dev` and AD-3's "Shared environments" bind, both citing §34 | No change; already represented | §34, lines 4904, 4914, 4942 |
| A07 | Doc-delta candidates for HDE Schemas & Artifacts §8.8, HDE-CLI-API-Vendor-Ref §5.6 and HDE Architecture §3.4 | Out of target: T-PF12, T-PF05, T-PF02 | none |
| A10 | Stale canon passage: HDE Mechanics Guide §34, which WU-PR-05 plan §19 names as "the production mount of the dev routes" | Redline RL-008, a new posture bullet. §34 v3.5.8 carries no sentence about the production mount, so the drain records the delivered production-like posture (S19-F02 and S19-F03) instead of correcting a sentence | §34, posture block |
| A10 | Stale passages in HDE Architecture §3.3, §3.5, §3.8.1 and HDE Users Guide §1.1 | Out of target: T-PF02, T-PF29 | none |
| A10 | LR5-O1 (router-level `OPTIONS` and redirect answers) | Held, H-03; not drafted. RL-008 states only requests dispatched to the routes' handlers | none |
| A10 | The "never fires" wording of 2.7 AD-4 item 4; WU-PR-08's "cuts 1.4.0" | Not a PF14 drain: a PF10 publication fact (Product Owner) and an out-of-force clause (2.19, 2.20) | none |
| A15 with X03 | ADR row: §1.6.3 gains the close-run publication API | Redline RL-003, first bullet | §1.6.3, after line 918 |
| A15 with X03 | ADR row: §37.2 names `tools/qa/generate_epic_close_pack.py` as the generic v2 generator beside the EPIC-025 entrypoint | Redline RL-009 | §37.2, lines 5029–5031 |
| A15 with X03 | ADR row: §37.2 epic-scoped filename list gains the CRD filename form | Redline RL-009 | §37.2, lines 5029–5031 |
| A15 with X03 | ADR row: §37.3 `key_outputs` rule gains the v2 minimum | Redline RL-010 | §37.3, after line 5124 |
| A15 | C-1 to C-4 (ADR, schema and writer changes before #668 merged); the approval and status line | Not a PF14 drain: delivered in the repository and recorded in the ADR | none |
| A15 with X03 | Other ADR rows (Change Process Guide, HDE Schemas & Artifacts §1.2, §8.17, §8.17.1, Glow QA Guide, HDE Governance §2.0.19 and Appendix D.0) | Out of target: T-PF06, T-PF12, T-PF19, T-PF04 | none |
| A26 | FND-040: §1.6.3 admission text states the `ADMITTED_CRD_QA` set, today HDE-CRD-0001 and HDE-CRD-0002, with roots and Index keys, beside the close-run API | Redlines RL-001 and RL-002; consistency redline RL-004 for the same rule restated in the regression responsibilities | §1.6.3, lines 913, 915, 1158 |
| A26 | CR-10 into HDE Schemas & Artifacts §8.3 | Out of target: T-PF12 | none |
| A26 | FND-021 (HDE Math Spec §§6.1–6.2) | Held, H-01; not a PF14 item | none |
| A26 | FND-017 to FND-020 | Repository documents, not PF canon (ledger row A34) | none |
| X07 | CR-11: §1.6.3 Step-0B for a CRD | Redline RL-003, second bullet, routing Step-0B's own rules to Plan Templates by title | §1.6.3, after line 918 |
| X07 | CR-11: Plan Templates Step-0B (CRD applicability) | Out of target: T-PF27 | none |
| Target hygiene | Two empty list items at the end of the document | Redline RL-011, authorized as hygiene by TW-DRAIN-10's rule on placeholders and drafting markers; PF03 §14 forbids empty bullets | §37.18.3, lines 7721–7723 |

Held items. None was touched. H-01 and H-03 are named above only to record that nothing was drafted for them. H-02, H-04, H-05 and H-06 have no PF14 bearing.

Closure. HDE-CRD-0002 is closed (CL-C-10 v1.2, CLOSE, Isis, 2026-10-26T16:40:00Z; X11), so no change is held on closure grounds. The cross-cutting rules of 2.1, 2.3, 2.11, 2.14, 2.18, 2.31 and 2.34 are not among T-PF14's rows.

## 5. The redlines

Eleven independent operations against the unchanged original: nine `REPLACE` and two `INSERT`. Offsets are byte offsets into the original. The redlines file carries each operation's full basis, rationale and literals.

| ID | Type | Op | Original bytes | Summary |
| :- | :- | :- | :- | :- |
| RL-001 | CANON_UPDATE | REPLACE | 100806–101221 | Admission is the `ADMITTED_CRD_QA` table; it admits HDE-CRD-0001 and HDE-CRD-0002; a CRD outside it gains no admission |
| RL-002 | CANON_UPDATE | REPLACE | 101693–102116 | Both admitted roots with their Human Index key prefixes; key forms by prefix, with the existing HDE-CRD-0001 keys as examples |
| RL-003 | NEW_CANON | INSERT | gap at 103329 | Two bullets: the close-run publication API and family mechanics; Step-0B for a CRD (CR-11) |
| RL-004 | CONSISTENCY | REPLACE | 124701–125077 | The regression responsibility: admission limited to the table, unadmitted IDs refused by both entrypoints |
| RL-005 | CANON_UPDATE | REPLACE | 413933–414101 | §34 route table: `/api/reader` is the production `POST` surface (§9.2), not an alias of `/reader` |
| RL-006 | CONSISTENCY | REPLACE | 415768–415899 | Drop "After the runner is hardened to the required profile" |
| RL-007 | CONSISTENCY | REPLACE | 416011–416230 | Drop the caution that the command is not a claim that the bind satisfies loopback |
| RL-008 | CANON_UPDATE | REPLACE | 417089–418296 | §34 posture re-inspected at `0838ba0`: helper, loopback run call and flags, CORS absence and its tests, exact gate, production-like posture, catalog |
| RL-009 | CANON_UPDATE | REPLACE | 426411–426857 | §37.2: CRD close-pack filename form; the generic v2 generator beside the EPIC-025 entrypoint |
| RL-010 | NEW_CANON | INSERT | gap at 436191 | §37.3: the v2 `key_outputs` minimum and its binding rule |
| RL-011 | DOC_HYGIENE | REPLACE | 663389–663440 | Remove the two empty list items at the end of the document |

Interpretations and constraints applied:

* The PF14 text names HDE-Build Notes by title only and routes other PF documents by title (PF03 §3 "Canonical ownership"; AGENTS.md "PF10's authority in the canon").
* Step-0B's own rules stay in Plan Templates. RL-003 names the two CRD doc-delta surfaces and routes the rules there rather than restating them (PF03 §5).
* In RL-008, each posture bullet states only what the inspected bytes show. The CORS bullet says that tests assert the posture and that this inspection does not establish that they pass (PF03 §3 "Claim-state separation"). The catalog bullet drops the earlier unverified negative about the complete PF05 and PF12 projection, because this inspection did not re-establish it, and keeps the nonclaim. The posture heading names the inspected commit.
* RL-006 and RL-007 are consistency changes inside §34. Their conditional and cautionary wording described a runner that had not yet been hardened, and they would contradict the re-inspected posture.
* RL-009 combines two ADR rows into one operation because both share the boundary between the same two paragraphs; the existing EPIC-025 sentence is kept verbatim.
* Pre-existing rendering loss in the target, such as `audit/EPIC-\\\_close\_report.md` and `Where \\ is a zero-padded 3-digit epic number` in raw bytes, is template notation whose angle-bracket placeholders were lost before v3.5.8. It is not a drafting marker; restoring it would need a source that establishes the lost text, which none of the inputs supply. No redline touches it, and the new text keeps every placeholder inside a code span.
* Document control is left to TW-APPLY-10. The header schema, the native version and date formats and the single source identity are recorded at the top of the redlines file. The source identity is PF10 v13.8.8, giving the gate form `BN 13.8.8`. PF14 has no change log or revision-history section and no rule requiring one, so no change-history entry is prepared.

## 6. Producer validation

Two independent validations ran against the unchanged original, each by script.

1. The preparer (`prepare.py`, scratch only) built every OLD block from complete original lines. It asserted the original's SHA-256 and blob identity, every heading-path line's uniqueness, an expected-equal-observed count of 1 for every OLD block (non-overlapping and overlapping counts alike) and for every BEFORE, AFTER and BEFORE+AFTER pair, line-start and line-end alignment of every OLD block (and the document end for RL-011), and the absence of any conflict in the batch. A conflict here means intersecting or touching replaced spans, an insertion at or inside a replaced span, or two insertions at one gap. It also asserted that no operation touches header lines 1–10, and that no literal holds four backticks or a CR. It then simulated one-pass application in descending original order.
2. A separate parser (`redlines_parse.py`, scratch only) read the saved redlines file alone. It found exactly RL-001 to RL-011 in order, an accepted operation spelling for each, the required literal set for each operation, and a byte count and SHA-256 matching the stated values for all 24 literals (two for each `REPLACE`, three for each `INSERT`). It re-checked every count, alignment and conflict rule against the original and re-simulated the application.

Results: 11 of 11 operations valid, 0 conflicts, 0 header overlaps. Both simulations give the same revised content without document control: 669,451 bytes, SHA-256 `6c9964c8abcb19b65a9948134e10af87a0491e255c24af46c32fc7dfde8f7acc`. No literal contains an ASCII three-period ellipsis or the Unicode ellipsis. The RL-045 rule is not engaged: the package uses no `FIND_AND_REPLACE`.

Corrections made during preparation, before READY: three wording precisions in rationale and payload text. RL-003's note on 2.17 now matches 2.17's supersession wording. RL-006 cites 2.8 only through its Addendum Index entry. RL-008 names the three factories as `adapter.factory.create_app`, `adapter.wsgi.create_app` and `adapter.http_reader.create_app`. The whole batch was regenerated and both validations were re-run on the corrected package. The values above are from that final run.

## 7. Outside dependencies and limits

* No blocking dependency. Every change in the selected scope is either drafted or dispositioned above.
* The repository-posture statements rest on static inspection at `0838ba0`. If `main` changes the inspected code before Apply or before canon adoption, RL-008's heading identifies the snapshot the statements describe.
* The supporting cross-references were read only at their ledger boundaries, and the PF10 addenda only as selected. No other PF10 addendum was used as authority.
* The prompt bodies were fetched once, live, in this session. Neither page names a newer version.

## 8. Correction route

A TW-APPLY-10 diagnostic on this package returns to this preparer, TW-DRAIN-10 in this session, which must correct the package under a distinguishable revision identity (`P2`) and re-run both validations before any further Apply.

## 9. Save verification

Recorded only after both files were saved and read back completely.

* `redlines-PF14-from-v3.5.8.md`: present at its repository path, 37,476 bytes, 379 lines, SHA-256 `ea1c20e710d149bc5c5fa3af1a3f353f1c2708fa6b5c47de8019a079ee84f6d3`, byte-identical to the validated copy. Read back in full, and parsed back independently from the saved bytes: 11 operations, 24 literals with matching byte counts and SHA-256, and the same simulated result (`6c9964c8abcb19b65a9948134e10af87a0491e255c24af46c32fc7dfde8f7acc`). It ends with `END OF REDLINES`.
* This proof log: present beside it. Sections 1 to 8 were read back in full before this section was added (21864 bytes, SHA-256 `5da20b07232eaa6826485d27f8bdee972f08271c294b9105f3efa6187646fb25`); the file was read back again after this section was added. A report does not carry its own final hash.
* Save completeness: `COMPLETE_PACKAGE`. Preparation outcome: `READY`. The package is ready for TW-APPLY-10 100926.1 in this session, against the same original, ledger rows, source boundaries and branch.
