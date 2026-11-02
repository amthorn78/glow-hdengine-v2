# Proof log: PF02-Canon-HDE-Architecture v2.4.7 redlines (gtwpe-20261101-pf10-v14-0-5, T-09)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF02/PF02-Canon-HDE-Architecture-v2.4.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / T-09 / preparation revision `r1` |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of this step (page state 2026-10-09T11:05:22Z) |
| Preparer | The T-09 document session Nathan started (Claude Code, https://claude.ai/code/session_01Q789u3YHoFbcNNPspHj1tZ), 2026-11-02. No subagent, reviewer or other session took part. |
| Authorized sequence | Nathan's handoff "GTWPE document session — T-09 — HDE Architecture (drain, then apply)" authorizes TW-DRAIN-10, then TW-APPLY-10 after a `READY` / `COMPLETE_PACKAGE` result, in this session |
| Preparation outcome | `READY` |
| Save outcome | `COMPLETE_PACKAGE`: the redlines file and this proof log were saved and read back in full (§8) |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826 (open, not merged, when this step began) |

## 2. Sources and inputs

| Role | Identity | Coverage |
| :---- | :---- | :---- |
| Target (original baseline) | `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.7.md`; in-document title `PF02-Canon-HDE-Architecture`, version v2.4.7, status Canon, effective date 2026-10-26, Last Update Gate `BN 13.8.8`. Read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. Git blob `9a23eec67198b86768d3b7fcef2e1b864cb9d998`; SHA-256 `fc0001e215e5a42bcf91f1e043f0f88a94867e00edae2ab387535869b855a149`; 142,444 bytes; 1,624 LF characters and no final LF, so 1,625 text lines (`wc -l` reports 1,624, the figure the ledger gives) | Complete. Every line was read, including front matter, change control, all eight top-level sections and their subsections. |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5. Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d` (recomputed in this session); 385,734 bytes; 1,976 lines | Selected units read completely: addendum 2.4, lines 673–753 (DELTA-001 at l.707, l.723, l.729); addendum 2.5, lines 754–883 (DELTA-001 wording at l.853) |
| Supporting reading (not drain scope) | The same PF10: addendum 2.3, lines 589–672 (delivered `adapter/chart_orchestration.py` and `engine/charts/pure.py`); addendum 2.7, lines 962–1047, read at the DELTA lines (l.985, l.995, l.1021, l.1027) and their entries; addendum 2.10, lines 1230–1332, read at its title and details (l.1230, l.1232), the delivered-boundary retrospective (l.1263, l.1271, l.1276), the open-item table (l.1301) and the PF09 row-closure table (l.1309–1321) | Read as needed to establish meaning and closure; nothing in them was drained |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, git blob `504712df548a02f3aa4e7b8c37027385e46a3878`, at `origin/main` | §1 to §8, §11 and §14 to §15 read in full |
| Triage ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064` | Read in full. Task T-09; assigned rows C-13, C-14; supporting rows C-12, C-16, C-21 |
| Closure evidence | `docs/ephemeral/HDE-EPIC041-CL-E-10-closure-decision-v1.0.md`, blob `5075f5ea5a2e60e0987ce427df4c4c5b796f662b`, at `origin/main`: `closure_state: CHANGE_CLOSED`, decision CLOSE by Isis at 2026-11-01T16:39Z | Header and decision lines read; agrees with PF10 addendum 2.10 |
| Supporting record | `audit/docdeltas/hde-epic041_drain_targets.md` at `origin/main`, "Canon drainage" list | Read; DELTA-001 is listed there for the Product Owner after all QA tasks |

Baseline currency. When this step began, `origin/main` was `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, two commits after the baseline `e2b7427`. `git diff --stat e2b7427 origin/main -- docs/pfcanon/` is empty, and the target and source blobs on `origin/main` equal the recorded identities. `git diff --stat e2b7427 origin/main -- engine adapter tests scripts` is also empty. No affected row needs reconciliation.

## 3. Repository inspection behind the current-state claims

The replacement text states current repository reality, so the state was inspected read-only at the baseline commit `e2b7427ff418ca8f08f05587c4a541308a76da56` and confirmed unchanged at `origin/main` `84d6d1c`:

- `git ls-files engine/charts adapter/chart_orchestration.py` lists `adapter/chart_orchestration.py` and `engine/charts/pure.py` only. `git ls-tree -r --name-only` at both commits gives the same result for `engine/charts`, `adapter/chart_orchestration.py` and `tests/charts`. `engine/charts/loader.py` is not tracked at either commit.
- `adapter/chart_orchestration.py` (read at `e2b7427`): its docstring and code show the `SAFE_MODE` read (`_os.getenv("SAFE_MODE", "0")`), both clocks (`time.perf_counter`, `datetime.now(UTC)`), the correlation identifier (`ensure_cid`), pinned-list reads anchored at `_ROOT = Path(__file__).resolve().parents[1]`, fixture acquisition (`_fixture_chart`) and one log line per call through `_emit` to an injected sink or the module logger. It imports `normalize_chart` and `validate_birth_inputs` from `engine.charts.pure`. A bounded search of the two modules for `resolve_provider`, `bodygraph`, `requests`, `urllib`, `psycopg`, `write_text` and `open(` found no occurrence.
- `engine/charts/pure.py` imports only `re`, `unicodedata` and `typing` (plus `from __future__ import annotations`).
- `tests/charts/test_chart_loader_import_guard.py` defines `test_no_tracked_python_file_imports_the_retired_loader` and `test_the_retired_module_path_does_not_exist`. This proves the tests exist, not that they pass; the replacement text says the test "is written to fail" and does not claim a run.

These are static checked-in facts. They do not prove runtime behavior, test passage or deployment, and the replacement text says so.

## 4. Change and disposition ledger

Assigned rows:

| Row | Source content | Disposition | Location or destination |
| :---- | :---- | :---- | :---- |
| C-13 | 2.4 DELTA-001: HDE Architecture §1.1 "Non-BodyGraph chart loader classification" describes `engine/charts/loader.py` as current "until separately remediated"; it is removed (l.707, l.723, l.729) | Actionable: RL-01 | PF02 §1.1, line 198 |
| C-13 | 2.4 DELTA-002: HDE Mechanics Guide §1.1 | Out of this target's ownership | T-05 (HDE Mechanics Guide) |
| C-13 | 2.4 approval, review, CI, attribution and status record of WU-PR-02 | Out of this target's ownership: Epic history | T-10 (HDE Phased Epics) |
| C-14 | 2.5 DELTA-001: "after delivery and acceptance, replace 'remains current repository reality until separately remediated' with the delivered boundary" (l.853) | Actionable: RL-01 (the same edit; one coherent operation) | PF02 §1.1, line 198 |
| C-14 | 2.5 DELTA-002 (l.854) | Out of this target's ownership | T-05 |
| C-14 | 2.5 DELTA-003, HDE State of the Repository §2.2 | Held: H-03 (§5) | None in this task |
| C-14 | 2.5 CCR-5 close-pack ordering | Held: H-06 (ledger §5) | Not a PF02 point |
| C-14 | 2.5 PF09 row-closure record | Held: H-01 (ledger §5) | Not a PF02 point |
| C-14 | 2.5 PF23 rows #19 to #27 | Held: H-04 (ledger §5) | Not a PF02 point |
| C-14 | 2.5 remaining triage record (coverage rows, CCR-1 to CCR-4, Specification carry-forward) | Out of this target's ownership: Epic history | T-10 |

Supporting rows (read for meaning only; no drainage from them):

| Row | Use in this task |
| :---- | :---- |
| C-12 | 2.3 names the delivered modules and their roles. Used to describe the delivered boundary, confirmed by §3 inspection. |
| C-16 | 2.7 restates the DELTAs and l.1027 says they drain "after all QA tasks; never a close blocker". QA-120 records PASS. |
| C-21 | 2.10 records the closure and, at l.1313–1320, gives DELTA-001 the home "HDE Architecture §1.1 'Non-BodyGraph chart loader classification'", the posture "still describes the removed loader as current" and the action "text drain only", with no status change. |

Equivalence check. Before RL-01 the target did not already state the delivered boundary: line 198 is the only occurrence of `engine/charts/loader.py`, `chart_orchestration` or `engine/charts` in PF02, and it calls the loader current. No other PF02 text describes the chart path, so no other location needs an edit.

## 5. Held items

| ID | Item | What it waits for |
| :---- | :---- | :---- |
| H-03 | DELTA-003, HDE State of the Repository §2.2 | It is not a target of this task. PF10 2.5 calls it a candidate that is not adopted, owned by the Product Owner, and the ledger records no eligible Technical Writing home (a Reference document other than PF03 and PF20). It waits for the Product Owner's decision to adopt it and the Product Owner's own update of that reference document. |

No change in the selected units belongs to an Epic or CRD that is not closed. HDE-EPIC041 is closed (`CLOSE / CHANGE_CLOSED`, 2026-11-01T16:39Z), and QA-120 recorded PASS before it, so DELTA-001 is eligible to drain.

## 6. Substantive change and its basis

RL-01 replaces the single paragraph at line 198 with three paragraphs:

1. The normative classification, kept as `[Required-Now]`: non-BodyGraph chart loading is not a sanctioned Engine I/O seam; operational concerns belong to Adapter-owned orchestration and use the BodyGraph resolver/ingest boundary where vendor or database acquisition is required; pure validation and normalization may stay in the Engine. The four obligations of the original paragraph are kept word for word. Removed: the commit-pinned statement that the loader is current, "The checked-in loader remains current repository reality until separately remediated" (the phrase DELTA-001 names), and "this classification does not claim that relocation, caller migration, or removal has occurred", which is no longer true.
2. A `[Implemented]` current-repository statement at commit `e2b7427`, the delivered boundary DELTA-001 asks for: the Adapter entry and what it owns, the pure Engine module as the only tracked file under `engine/charts/`, the removed loader with no shim (keeping the commit `5ef911fe` at which the classification called it drift, as history), the import-guard test, and the fact that the supported path acquires only a fixture chart and so does not engage the BodyGraph resolver/ingest boundary (PF10 2.5 QA10-OBS-01; §3 inspection).
3. A "Static inspection cannot establish" statement, in the form PF02 already uses in §3.

Classification: CANON_UPDATE.

## 7. Constraints, assumptions and interpretations

- PF02 rules applied: claim-level status labels (front matter "Section labels"), so the normative rule and the inspected state are separate labelled paragraphs; the `[Implemented]` "At repository commit" form used in §2.1 and §3; HDE Build Notes cited by title only ("Supersession rule"); guard mechanics routed by title to HDE-Mechanics Guide ("Routing (titles-only)" in §1.1); no ellipsis forms (change control "Ellipsis prohibition").
- PF03 rules applied: §3 claim-state separation (a test definition is not a passing test; static inspection proves checked-in bytes only); §4 one repository snapshot for every repository-dependent claim; §7 smallest structural change and no change to document-control values; §8 and §15.2 redline fields. PF03 §8 says not to fence paste text unless the operator asks; TW-DRAIN-10, the operator contract here, requires literal fenced payloads, and PF03 §8 and §15 defer to an operator-supplied format.
- The bold label "Non-BodyGraph chart loader classification" is kept, because PF10 2.5 and 2.10 name that label as the drain home. Renaming it was not authorized.
- The heading structure of §1.1 is unchanged; RL-01 adds no heading.
- Header: not edited by RL-01. TW-APPLY-10 derives the document-control values. Native header schema, in order: Title `PF02-Canon-HDE-Architecture`; Version `v2.4.7`; Status `Canon`; Effective date `2026-10-26`; Last Update Gate `BN 13.8.8`; Invocation tag `INV-f2ac55d77ce9aacc`. Version scheme `v<major>.<minor>.<patch>`; the expected bump is v2.4.8. Source for the header, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, version v14.0.5. PF02 has no change log or Doc-Delta entry format, so no history redline is prepared.
- Hygiene: PF02 carries no `Draft` status language, placeholder, TODO or drafting note to remove. Lines 181 and 1225 mention placeholders as canon rules. No hygiene redline is prepared.

## 8. Validation

Producer validation ran in a scratch directory with a script that parses the saved redlines file (not the in-memory draft), then simulates one-pass application against the unchanged baseline bytes:

| Check | Expected | Observed |
| :---- | :---- | :---- |
| Redline IDs | RL-01 | RL-01 |
| Operation dialect | `REPLACE`, exact old block | `REPLACE` |
| Section path `# 1\. Architectural Principles \[Required-Now\]` > `## 1.1 Single homes` | each heading once | 1 and 1 |
| Old block occurrences, whole document | 1 | 1 |
| Old block span | inside §1.1 (lines 190 to 237) | line 198; characters 18,747–19,812; bytes 18,782–19,847; LF on both sides |
| Replacement contains the old block | no | no |
| Replacement contains U+2026 or three full stops | no | no |
| Payload present and complete | yes | yes; END OF REDLINES present |
| Overlap and conflicts | none possible with one operation | none |
| Bytes outside the span after simulation | unchanged | unchanged |
| Phrase "remains current repository reality until separately remediated" after simulation | absent | absent |
| Simulated result (content only, before header derivation) | — | 143,457 bytes; 1,628 LF; SHA-256 `fe2318226d18be55a15c0ae1c6494a2ec65ea3ea1655146e1672af09137fe2d4` |

Save verification: both files were read back in full from the working tree after writing. Before writing, `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF02/` did not exist, so no output collided.

Not run: product tests, QA and CI. They are outside this task.

## 9. Unresolved issues, limitations and deviations

- None blocks application.
- Line count: the handoff and ledger give 1,624 lines (`wc -l`); the file has 1,624 LF characters and a final line without LF. This is a counting convention, not a difference in the bytes.

## 10. Next step

TW-APPLY-10 — Apply Validated Redlines — 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`) runs next in this session, as the handoff authorizes, with this redlines file, this proof log, the unchanged original, ledger rows C-13 and C-14, branch `claude/gtwpe-triage-authoring-j94ewf`, final output under `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF02/` (expected `PF02-Canon-HDE-Architecture-v2.4.8.md`) and diagnostic path `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF02/PF02-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`.
