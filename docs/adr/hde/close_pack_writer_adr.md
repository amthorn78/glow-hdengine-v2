# Close-pack writer for Epic and CRD identities

Status: Approved with changes by the Product Owner on 2026-10-20 (AQ-1; HDE Build Notes addendum 2.15; review docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md).

Amended by the Product Owner on 2026-10-21 (PO-35-7 to PO-35-9; result record docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.9.md): R-2 is reworded to match HDE Build Notes addendum 2.15's summary, so the drain-targets ledger names every deferral's ID in both forms; a tracked-issue pointer names a heading in the change kind's register; the plan is the change's current implementation plan. The HDE Schemas & Artifacts §1.2 basis is the drain-targets ledger plus the single-posture rule; for the pointer form this is stricter than §1.2 requires.

## Problem

An ordinary Close Gate needs a close report and manifest that canon can accept, written from tracked inputs, plus same-run evidence of the close workflow. HDE-EPIC040 showed that neither existed (closure evidence record CLOSE01, findings B-1 and B-2):

- B-1. The generic writer `tools/qa/generate_epic_close_pack.py` was made neutral on purpose by HDE-EPIC039: a closed vocabulary of four headings and ten fixed body lines, five fixed nonclaims, Epic identities only. It cannot write the required heading `QA Rails — Open/Close (Final PR)`, the acceptance pointers, a binary decision, deferrals, later-drain statements or a manifest `key_outputs` map, and one of its fixed nonclaims ("No QA PASS, acceptance, or token satisfaction is claimed.") contradicts a `SATISFIED` close.
- B-2. Every admitted evidence home under a change's QA root is a check listed in `qa_step_logs_manifest.json`. Recording the close run there reopens an approved QA manifest after the verdict.

HDE-EPIC040 then closed by Product Owner-authorized exceptional closure, as HDE-EPIC038 had before it.

## Decision

1. **A second source schema version.** `schemas/close_candidate_source.v2.json` is a closed schema for one Epic (`HDE-EPICNNN`) or CRD (`HDE-CRD-NNNN`, four or more digits). `schemas/epic_close_candidate_source.v1.json` stays, unchanged, for history; a v1 source keeps the v1 model, refusals and output bytes.
2. **One writer, kept at its registered path.** `tools/qa/generate_epic_close_pack.py` selects the model by the source's `schema_version`. Its CLI, closed-rails refusal, clean-tree and tracked-input rules, manifest-last publication, `manifest → report → manifest` reading and non-writing check mode are unchanged.
3. **Paths of record.** An Epic writes `audit/EPIC-NNN_close_report.md` and `audit/EPIC-NNN_MANIFEST.json`. A CRD uses its ID as the prefix (`audit/HDE-CRD-NNNN_close_report.md`, `audit/HDE-CRD-NNNN_MANIFEST.json`) and its lower-case ID as the directory form (`hde-crd-nnnn`). The candidate source for HDE-CRD-0002 is `audit/HDE-CRD-0002_close_candidate_source.json`.
4. **What the v2 report carries**, each part rendered from a structured source field: the verbatim `QA Rails — Open/Close (Final PR)` heading; the "Acceptance and evidence pointers" list; the binary `SATISFIED` / `NOT SATISFIED` closure decision with its posture; an exact-source acceptance section that binds each criterion ID to the change's current approved Specification, to tracked evidence and to a result and limitation. The current approved Specification is the tracked `docs/ephemeral/<change-id>-specification-v<N>.<N>-approved.md` of the source's own change at the highest version tracked; any other document is refused (`REQUIREMENTS_SOURCE_NOT_CURRENT`). The writer reads the requirement IDs from that Specification in the change kind's pinned format and refuses a document without it. Every criterion ID must be one of those IDs. `SATISFIED` needs an acceptance row for every ID read, every row met, no follow-up, and a bound QA step-logs manifest, in the pinned ledger format, whose every recorded status is `PASS` and agrees with its tracked primary's header; `NOT SATISFIED` needs at least one follow-up; delivered scope; deferrals, each with a drain target or with an ADR status and rationale, and in both forms the deferral's ID occurs in the drain-targets ledger; later-drain statements in the fixed vocabulary of HDE Schemas & Artifacts §1.2, stated as support records only; the tracked-issue mapping in HDE Governance's literal `TI-<id> pointers:` and `ADR status line:` fields, each item either a pointer to a Markdown heading in the change kind's bound register (a PF09 HDE Build Checklist file for an Epic, a PF30 HDE CRD Records file for a CRD) or an ADR status, in which case the item's ID occurs in the drain-targets ledger; the ADR block that Change Process Guide §3.5.4 requires; follow-ups; superseded artifacts; the QA RCA, embedded or bound; a "Key outputs" section; the close-pack verification statement; the source bindings; four nonclaims that are true of any close. Free text is limited to single neutral lines in named fields.
5. **What the v2 manifest carries.** A `key_outputs` JSON object whose values are repo-relative path strings: at least the close report, the close manifest, the doc-delta ledger, the drain-target ledger and the QA step-logs manifest. It points to the report by SHA-256 and size and carries no digest of the Index, a path proof, the orientation output or the close-run family. Every key output other than the close report and the close manifest is also a bound tracked evidence input, so its digest is recorded (`OUTPUT_BINDING_MISMATCH` otherwise).
6. **Feedback-freedom kept.** The v1 feedback-dependency refusal applies unchanged to every v2 causal value. Requirement and acceptance text is bound by reference (the requirements document's path and digest, and the criterion ID), never copied into a causal field. Two of HDE-CRD-0002's own requirement rows (S06, S11) contain words the refusal rejects; binding by reference lets the close record them without weakening the refusal. The v2 writer also refuses, as causal inputs, the Index trio and its sentinels, every `.path_proof.txt`, the orientation output, every path under `audit/qa/<change-id>/close/` and `catalog/manifest.json`.
7. **A post-verdict close-run family** for admitted CRDs: `audit/qa/<crd-id>/close/<check_id>/primary.log` with a path proof, published only by the canonical updater through `tools.evidence.update_evidence_index.publish_crd_close_run_family(config, results, *, captured_at_utc=None, coherence_verifier=None)`, a Python API like `publish_crd_check_family`. Each primary is a PF27 v2 step-log header rendered from the captured command, exit code and output of one close-run check. The family is never listed in `qa_step_logs_manifest.json`; the entrypoint writes neither that manifest nor any `checks/` primary. It requires the CRD's recorded QA family to exist. The given results replace the whole family inside one recovery transaction. HDE Build Notes addendum 2.15 introduces this family, with a membership exception for `close/` only.
8. **Absent-tolerant CRD close-pack rows** in the Human Index for every admitted CRD: neither file present, no rows; both present, one row each (`hde_crd_nnnn.close_report`, `hde_crd_nnnn.manifest`, with `crd_id`); one present, or a row whose file is gone, refused. Until a CRD closes, the Index is unchanged.
9. **The ADR block.** The v2 source carries a required, non-empty list of ADR-block decisions, each with a label, a statement, the decision point, the options considered when more than one was real, the bounding PF canon by title, the final decision, whether it becomes canonical or stays change-specific, and the Doc Delta targets by PF title. An optional closure-override entry enumerates each accepted gap with its bound evidence basis and drain targets. The report renders them as an "ADR block" section with titles-only canon references.

Dependency direction (no cycle):

`tracked causal inputs → close report and manifest → Index`; `close-run primaries → Index`

No byte the Index binds depends on the Index, and no hosted run writes a byte the final state needs.

## HDE-EPIC039's neutral writer, weighed

HDE-EPIC039 kept the writer ignorant of the evidence graph and of any claim, so that a candidate could never certify itself. S21 reverses only the second half of that choice: the v2 report states the closure decision and its posture because canon requires it, and it claims nothing its bound tracked inputs do not record. Kept from HDE-EPIC039: the single writer, its CLI and rails, tracked inputs at a clean HEAD, report first and manifest last, the manifest-to-report read, mixed-state refusal, symlink-byte verification, the non-writing check and the absence of hosted feedback. The v2 block names updater outputs and the close-run family only to refuse them as inputs, and binds the QA step-logs manifest as a tracked input and names it as a canonical pointer.

## Alternatives considered

- (a) Extend the generic writer and admit a post-verdict family: this decision.
- (b) A separate governed close-report writer beside the neutral one: two writers for one artifact family, and the same canon change.
- (c) Let the close PR add a manifest check after the verdict: reopens an approved QA manifest (CC-2), rejected.
- A canon change that drops the close-report requirement, or keeping exceptional closure for every change: weighed by the Product Owner on 2026-10-20 against the observed HDE-EPIC040 and HDE-EPIC038 closures; the Product Owner chose the writer (WU-PR-07 business case).

## Stated limits

- Closure-decision postures are exactly `review-trace-only`, `PO closeout` and `formal close-pack completion`; another posture needs a later schema version.
- Requirement coverage is checked against one pinned requirement-ID format per change kind: a CRD reads table rows whose first cell is `S` followed by two or more digits, as in HDE-CRD-0002's Specification; `HDE-EPIC<NNN>` reads its own requirement paragraphs `**K<NNN>-REQ-<NNN>.**` and acceptance rows `| AC<NNN>-<NN> — …`, as in HDE-EPIC040's. A bound requirements document without its change's format is refused (`REQUIREMENTS_TABLE_ABSENT`); another format needs a later pin.
- A tracked-issue pointer is a bound register file of the change's kind plus a Markdown heading that the file contains; the writer does not judge whether that section demonstrates closure.
- The plan is the change's own `docs/ephemeral/<change-id>-implementation-plan-v<N>.<N>.md` at the highest version tracked (`PLAN_SOURCE_NOT_CURRENT` otherwise). Every pointer names a tracked file or a directory holding one, except a CRD's close-run directory, which is written after the verdict (`POINTER_UNRESOLVED` otherwise).
- The QA step-logs manifest is read in one pinned format, the flat mapping the canonical QA harness writes (`check_id` to exactly `check_id`, `log_path` under `audit/qa/<change-dir>/checks/<check_id>/primary.log`, `status`); any other ledger, including an empty one, is refused (`QA_LEDGER_INVALID`), and `SATISFIED` needs every recorded status to be `PASS`. Each entry's `primary.log` must be tracked and open with a PF27 v2 step-log header whose `check_id` and `status` match the ledger (`QA_LEDGER_INVALID` otherwise); the primaries' digests are recorded in the manifest and under Source bindings. The writer reads the header line only; it does not judge the rest of a primary.
- No Epic close-run family is admitted. An Epic close run needs its own explicit admission later, as each CRD needs its row in `ADMITTED_CRD_QA`.
- A later Epic's v2 close pack is written and checked by the writer, but its Index rows need that Epic's own registration, as for earlier Epics.
- As in v1, an earlier commit's ID written without the refusal's trigger words is not refused; the current HEAD's ID is.

## Epic-only identity inventory (HDE Schemas & Artifacts §1.2)

Generic close-pack surfaces that accepted only Epic identities: the v1 schema's `epic_id` pattern and the writer's `EPIC_RE`. Both stay for v1; v2 accepts both identities. Epic-specific families stay epic-specific: `tools/qa/epic021_qa.py` and `tools/qa/generate_epic025_close_pack.py` to `generate_epic029_close_pack.py`. The read-only checks a close run uses carry no Epic or CRD identity rule; `ci/checks/check_mirror_schema.sh` already admits `crd_id`.

## Affected canon and drainage consequences

Drainage is unperformed. Each item below is a statement of what a later drain changes; none is a prerequisite, required check or blocker of any change or close.

| Canon home | Locator | Drainage consequence |
| :- | :- | :- |
| Change Process Guide | §3.5.2 "Close PR contents" and §3.5.2.1 "Close-pack files" | Name the CRD filename prefix beside `EPIC-NNN`, the v2 writer as the generic producer, and the close-run family as the same-run evidence home |
| HDE Schemas & Artifacts | §1.2 "Close-pack artifacts (deterministic path-of-record; baseline artifacts)" and "Change-container compatibility (normative)" | Record `close_candidate_source.v2`, the v2 manifest and its `key_outputs` minimum, the close-run family path and its post-verdict status, and the closed Epic-only inventory |
| Glow QA Guide | "Close-pack truthfulness and same-run execution (normative)" and "Close report requirements (validator-bound; mechanical)" | Name `audit/qa/<change-id>/close/` as the home of same-run close evidence for a CRD and the v2 writer's rendering of the verbatim heading and pointer list |
| HDE Mechanics Guide | §37.2 "Governance & homes", "Close-pack generator (mechanics; single-writer; normative)" | Name `tools/qa/generate_epic_close_pack.py` as the generic close-pack generator for v2 sources beside the EPIC-025 entrypoint; §1.6.3 gains the close-run publication API |
| HDE Governance | §2.0.19 "Close-pack baseline artifacts", "Close report minimal content (normative)" and "Close-pack manifest `key_outputs` shape (normative)"; Appendix D.0 | Name the CRD prefix beside `EPIC-###`, the v2 writer as the producer, and the literal `TI-<id> pointers:` and `ADR status line:` fields it renders |
| Change Process Guide | §3.5.4 "ADR block in the close-pack (all epics)" | Name the v2 report's ADR block, rendered from the source's ADR-block decisions and optional closure override |
| HDE Schemas & Artifacts | §8.17 "New standardized evidence families" and "Current-state evidence"; §8.17.1 | Record the close-run family as a post-verdict family whose membership is its validated primaries and path proofs, introduced by HDE Build Notes addendum 2.15 with its `close/`-only membership exception |
| Glow QA Guide | §3.4.3 "Evidence layout: current-state first" | Name `audit/qa/<change-dir>/close/` beside `checks/` as the post-verdict close-run family |
| HDE Mechanics Guide | §37.2 epic-scoped close-pack filename list; §37.3 `key_outputs` rule | Add the CRD filename form and the v2 `key_outputs` minimum |

## Nonclaims

This ADR produces no close pack, candidate source or close-run family for any change; HDE-EPIC040 gets no retroactive close pack. It changes no canon and drains nothing. It makes no QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement or closure decision.

## Rollback

Revert the change that carries this ADR. No existing close pack, Index row or QA record is rewritten by it, and no release member changes.
