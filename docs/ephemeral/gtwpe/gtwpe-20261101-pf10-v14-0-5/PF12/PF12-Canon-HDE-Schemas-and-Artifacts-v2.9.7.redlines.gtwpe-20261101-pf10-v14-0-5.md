# PF12 redlines — HDE Schemas and Artifacts — gtwpe-20261101-pf10-v14-0-5 (T-04)

## Package identity

| Field | Value |
| :---- | :---- |
| Package | `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Proof log | `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, in the same directory |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-04 / preparation revision r3. It supersedes r2 (commit `2a2325b`), which TW-APPLY-10 returned with the diagnostic `PF12-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` (commit `5716f60`), and r1 (commit `324de26`). The proof log records each correction. |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live in this session) |
| Preparer | One Claude Code session started by Nathan for T-04; no subagent, reviewer or other session took part |
| Preparation outcome | `READY` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at commit `142feb35144d8795f927e0c78b665ace52279064`; task T-04; rows C-04, C-05, C-10, C-17, C-18; uncertain C-07, C-29; supporting C-06, C-20 |

## Original baseline (the only text these redlines bind to)

| Field | Value |
| :---- | :---- |
| In-document title | PF12-Canon-HDE-Schemas-and-Artifacts |
| Path | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md` |
| Version | v2.9.7 |
| Commit | `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56` (unchanged on `origin/main` `84d6d1c` when this package was prepared) |
| Git blob | `d5bc01f83078bebe04f0854385317b47c1cd2de3` |
| SHA-256 | `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc` |
| Size | 640,642 bytes; 6,264 LF characters; the last line is empty, so the file ends with two LF bytes |

## Change source

| Field | Value |
| :---- | :---- |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` (HDE Build Notes), version v14.0.5 |
| Identity | Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 1,976 lines; read at `origin/main` `e2b7427` |
| Selected units | 2.1 D-4 (lines 397–450), D-5 (451–490) and context (205–224, 491–516); 2.2 (517–561); 2.8 decisions and drainage table (1063–1106, 1111–1127); 2.16 status, R-1 and R-2 (1869–1939) |
| Supporting reading only | 2.2 (562–588); 2.8 (1048–1062, 1107–1110, 1128–1145); 2.9 (1146–1229); 2.10 heading and first paragraph (1230–1232); 2.16 R-3 to end (1940–1976) |

## Document-control data for TW-APPLY-10

These redlines leave the header to TW-APPLY-10's derivation. The baseline header schema is the `## **0.1 Header**` block of six bold-labelled lines, each but the last ending in two spaces:

| Field | Baseline value |
| :---- | :---- |
| Title | PF12-Canon-HDE-Schemas-and-Artifacts |
| Version | v2.9.7 |
| Status | Canon |
| Effective date | 2026-10-26 |
| Last Update Gate | BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md |
| Invocation tag | INV-f2ac55d77ce9aacc |

- Version scheme: the third component increments once per revision (v2.9.5, v2.9.6, v2.9.7 in §§9.5 and 9.6). The expected derived version is v2.9.8.
- Sources that justified this update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, version v14.0.5. No other source changed the target.
- Revision-history entry: RL-11 adds §9.7 in PF12's own Doc-Delta record format, naming `document_version: "v2.9.8"` and `date: "2026-11-02"` (the preparation date). The record's `change_log_entry` also names `v2.9.8 / 2026-11-02`.
- No redline below touches the header, the title, the status or the invocation tag.

## Literal-block convention

Each literal block below is fenced with five backticks and the info string `text`. The literal is exactly the characters between the newline that ends the opening fence line and the newline that immediately precedes the closing fence line; that last newline is a delimiter, not part of the literal. Every other byte inside the fence, including trailing spaces, blank lines and inner fences, is literal.

## Operations and application

- Eleven redlines: nine `REPLACE` and two `INSERT`. No `DELETE` and no repeated-replacement operation.
- Each `REPLACE` old block occurs exactly once in the original. Each `INSERT` gap is the single place where its BEFORE anchor is immediately followed by its AFTER anchor.
- Resolve every locator against the unchanged original, then apply all eleven in one pass by original position. No redline's output is another redline's locator, and no two redlines touch or overlap.
- RL-01 to RL-11 are listed in original-document order.

## RL-01

- Source rows: C-05
- Change type: CANON_UPDATE
- Operation: `INSERT`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
- Location within that section: run-in block "Canonical JSON gate artifacts (primary family plus legacy coexistence)": after its closing paragraph "Acceptance bindings MUST cite", before the run-in block "Evidence index snapshot artifacts (single home; remove EPIC-local variant)"
- Gap location: immediately before original line 551 (informative only; the anchors below are the locator)
- Expected occurrences of BEFORE immediately followed by AFTER in the original: 1 (observed: 1)
- The gap is the boundary between the end of BEFORE and the start of AFTER. Neither anchor is changed.

BEFORE anchor (it ends with 2 newline characters):

`````text
Acceptance bindings MUST cite audit/gates/json\_gate/canonical/ as the authoritative family. The legacy family under audit/gates/canonical\_json/ and the optional legacy artifact audit/gates/canonical\_json\_gate.json MAY be present and tracked during migration, but they MUST NOT be treated as independent acceptance bindings.


`````

AFTER anchor (it ends with 1 newline character):

`````text
Evidence index snapshot artifacts (single home; remove EPIC-local variant)

`````

Inserted text (it ends with 2 newline characters):

`````text
Governed gate check row content (normative).

* Scope. This rule applies to each row of `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` and of `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, and to each check row of any other PF12-governed gate family. HDE-Governance governs these rows as keys-only governed logs.  
* Issue entries. Each issue entry MUST be a closed token. An exception contributes at most its type name, as `validation_error:<ExceptionType>`. No row carries exception message text, library message text, or a stack trace.  
* Paths. Every path a row records MUST be repository-relative. No row carries an absolute or machine-local path.  
* Diagnostics. Detail for diagnosing a failing run goes to the gate tool's stderr, which is not governed evidence.

This rule states the required row content; this section does not assert that the current gate tool already enforces it. Frozen gate captures retain their recorded bytes.


`````

## RL-02

- Source rows: C-10, C-18, C-17
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
- Location within that section: run-in block "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", run-in list "Generic close-pack writer (normative)."
- Original location: line 603 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
* A source whose `schema_version` is `close_candidate_source.v2` is read against `schemas/close_candidate_source.v2.json`, a closed schema for exactly one Epic (`HDE-EPICNNN`) or CRD (`HDE-CRD-NNNN`, four or more digits) identity.  
`````

Replacement block:

`````text
* A source whose `schema_version` is `close_candidate_source.v2` is read against `schemas/close_candidate_source.v2.json`, a closed schema for exactly one Epic (`HDE-EPICNNN`) or CRD (`HDE-CRD-NNNN`, four or more digits) identity. Its tracked-issue IDs are `TI-NNN` or the Epic's own `ISSUE-EPIC<NNN>-TI-<nn>`, and the writer refuses a tracked-issue ID that names another Epic (`TRACKED_ISSUE_UNBOUND`). A tracked issue maps only through an ADR status; the v2 schema refuses the register-pointer form for it.  
* A v2 source records the planning facts the writer checks and binds no planning document: `planning_records` holds the identity and SHA-256 of the Specification, the implementation plan, the QA plan, and the final QA report, each as a record text; `requirement_ids` holds the approved Specification's requirement IDs; `qa_checks` holds the QA plan's checks in plan order with the criteria each maps; and `qa_verdict` holds the final QA report's verdict. It has no plan path and no requirements, QA plan, or QA report binding. The writer checks the form of these records, not their agreement with the documents they name.  
`````

## RL-03

- Source rows: C-10, C-17
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
- Location within that section: run-in block "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", run-in list "Generic close-pack writer (normative)."
- Original location: line 605 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
* The v2 close report and manifest are rendered only from tracked inputs. Requirement and acceptance text is bound by reference, never copied into a causal field. The feedback-dependency refusal is kept, and the writer refuses as causal inputs the Human Evidence Index, the Machine Evidence Mirror, their hash and checksum sentinels, every `.path_proof.txt`, the orientation output, the close-run family, and `catalog/manifest.json`. Check mode writes nothing and validates the exact committed bytes.  
`````

Replacement block:

`````text
* The v2 close report and manifest are rendered only from tracked inputs. Requirement and acceptance text is bound by reference, never copied into a causal field. The feedback-dependency refusal is kept, and the writer refuses as causal inputs the Human Evidence Index, the Machine Evidence Mirror, their hash and checksum sentinels, every `.path_proof.txt`, the orientation output, the close-run family, and `catalog/manifest.json`. In either schema version, no path under `docs/ephemeral/` or `docs/pfcanon/` is a causal input, pointer, or key output: the writer refuses one with `PLANNING_OR_CANON_INPUT_PROHIBITED`, and the v2 schema refuses one too. A later-drain statement's evidence basis and a superseded artifact MAY name a planning document by a record text instead of a binding. A deferral's drain target names its register by PF title and gives the full text of one of its headings. PF titles and register headings are resolved at write time only, by title, against the PF-Canon files tracked at HEAD. Check mode writes nothing, reads no PF-Canon file, and validates the exact committed bytes.  
`````

## RL-04

- Source rows: C-18, C-17
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
- Location within that section: run-in block "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", run-in list "Generic close-pack writer (normative)."
- Original location: line 607 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
* The canonical updater registers a CRD close pack's report and manifest as Human Evidence Index and Machine Evidence Mirror rows `hde_crd_nnnn.close_report` and `hde_crd_nnnn.manifest`, each carrying `crd_id`. The rows are absent-tolerant: when neither file is present there are no rows, and when both are present there is one row each. One file present without the other, or a row whose file is absent, is refused.
`````

Replacement block:

`````text
* The canonical updater registers a CRD close pack's report and manifest as Human Evidence Index and Machine Evidence Mirror rows `hde_crd_nnnn.close_report` and `hde_crd_nnnn.manifest`, each carrying `crd_id`. For an Epic admitted in the canonical updater's Epic close admission table, `ADMITTED_EPIC_CLOSE` in `tools/evidence/update_evidence_index.py`, it registers the writer close pack's report and manifest as rows `epicNNN.close_report` and `epicNNN.manifest`, each carrying `epic_id`, the key form of earlier Epic close packs. The rows are absent-tolerant: when neither file is present there are no rows, and when both are present there is one row each. One file present without the other, or a row whose file is absent, is refused. Another Epic's v2 close pack is written and checked by the writer, but its rows need that Epic's own row in `ADMITTED_EPIC_CLOSE`.
`````

## RL-05

- Source rows: C-18, C-17
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **1\. Purpose & Single-Home Rule \[Required-Now\]**` > `## **1.2 Titles-only routing \[Required-Now\]**`
- Location within that section: run-in block "Close-pack artifacts (deterministic path-of-record; baseline artifacts)", paragraph "Same-run close evidence for a CRD (normative)."
- Original location: line 668 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
Same-run close evidence for a CRD (normative). For a CRD admitted in the canonical updater's CRD admission table, the same-run evidence of the close workflow is its post-verdict close-run family under `audit/qa/<change-id>/close/`, where `<change-id>` is the CRD's lower-case directory form: one `primary.log` per close-run check at `audit/qa/<change-id>/close/<check_id>/primary.log`, each with its sibling `primary.log.path_proof.txt`. The family is written after the final QA verdict. It neither reopens nor adds to the approved `audit/qa/<change-id>/qa_step_logs_manifest.json` or any `checks/` primary, and it is not a close-pack baseline artifact. §8.17 owns its writer, membership, and indexing. No Epic close-run family is admitted.
`````

Replacement block:

`````text
Same-run close evidence for an admitted CRD or Epic (normative). For a CRD admitted in the canonical updater's CRD admission table, or an Epic admitted in its Epic close admission table, the same-run evidence of the close workflow is its post-verdict close-run family under `audit/qa/<change-id>/close/`, where `<change-id>` is the change's lower-case directory form: one `primary.log` per close-run check at `audit/qa/<change-id>/close/<check_id>/primary.log`, each with its sibling `primary.log.path_proof.txt`. The family is written after the final QA verdict and after the close pack. It neither reopens nor adds to the approved `audit/qa/<change-id>/qa_step_logs_manifest.json` or any `checks/` primary, and it is not a close-pack baseline artifact. In a v2 source, every pointer names a tracked file or a directory holding one, except the change's own close-run directory, which the close run writes after the close pack: a CRD's source MUST point to its own close-run directory, and an admitted Epic's source MAY. Any other pointer that does not resolve is refused (`POINTER_UNRESOLVED`). §8.17 owns the family's writer, membership, indexing, and admission.
`````

## RL-06

- Source rows: C-04
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **6\. Freeze-Pack Manifest → release\_id \[Required-Now\]**` > `## **6.2 release\_id computation**` > `### **6.2.1 External release attestation**`
- Location within that section: the builder-refusal paragraph that follows the successful-attestation paragraph
- Original location: line 2049 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
The builder MUST refuse a symlinked output root, an output inside the source repository, a non-directory destination, a non-empty destination, or overwrite of existing output. Success and failure outputs remain external. They are not checked-in release primaries and do not create Human Evidence Index, Machine Evidence Mirror, QA PASS, acceptance-token, PF09, deployment, migration, or OPS claims by implication.
`````

Replacement block:

`````text
The builder MUST refuse a symlinked output root, an output inside the source repository, a non-directory destination, a non-empty destination, or overwrite of existing output. An absent output root is created by the builder, and an existing, empty, non-symlinked directory outside the source repository is accepted. Success and failure outputs remain external. They are not checked-in release primaries and do not create Human Evidence Index, Machine Evidence Mirror, QA PASS, acceptance-token, PF09, deployment, migration, or OPS claims by implication.

The builder owns its output root for the run:

* Exclusive claim. Before any other write, the builder MUST claim the output root exclusively for the run, by an atomic create that fails if another run holds the root. A root it cannot claim MUST be refused with a typed failure code before any write. The claim adds no member to a successful bundle beyond the `hde.release_attestation.v1` contract.  
* No writes through symlinks. Every write below the output root MUST go to a path the run created. A pre-existing or substituted symlink anywhere below the root MUST be refused, not followed.  
* Scoped cleanup. On failure, the builder MUST remove only the files and directories the run created, and then write its failure receipt. It never removes a path it did not create.

These rules state the required contract. They do not fix the mechanism of the exclusive claim, and this section does not assert that the current builder already enforces them.
`````

## RL-07

- Source rows: C-07, C-10
- Change type: CLARIFY
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.3 Machine Evidence Index — JSONL mirror (records-only) \[Required-Now\]**` > `### **Single home and path**` > `#### **Governed locations only.**`
- Location within that section: the paragraph under this heading
- Original location: line 2262 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
Every evidence file referenced by the mirror MUST live under governed repo paths (for example, artifacts/, docs/). Transient generator paths (scratch/temp) are disallowed; mirror entries pointing to non-governed paths fail CI.
`````

Replacement block:

`````text
Every evidence file referenced by the mirror MUST live under governed repo paths (for example, artifacts/, docs/). Transient generator paths (scratch/temp) are disallowed; mirror entries pointing to non-governed paths fail CI. No Machine Evidence Mirror record, Human Evidence Index row, or path proof binds a path under `docs/ephemeral/` or `docs/pfcanon/`: planning documents serve planning only, and a PF-Canon file's name and version may change at any time.
`````

## RL-08

- Source rows: C-05
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.6 Evidence Index entries (titles/paths only) \[Required-Now\]**` > `### **8.6.3 Entries (authoritative list; titles/paths only)**` > `#### **8.6.3.2 Core pack, canonical JSON, topology, and deterministic order**` > `##### **Canonical JSON and topology**`
- Location within that section: the artifact list under this heading
- Original location: line 2971–2972 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`  
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`  
`````

Replacement block:

`````text
* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`: its rows follow §1.2 "Governed gate check row content".  
* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`: its rows follow §1.2 "Governed gate check row content".  
`````

## RL-09

- Source rows: C-18, C-17
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.17 Live QA evidence layout (audit/qa/\\/) \[Required-Now\]**`
- Location within that section: run-in block "Close-run family exception (normative; admitted CRDs only).", after the run-in block "Current-state evidence (normative)."
- Original location: line 5399–5408 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
Close-run family exception (normative; admitted CRDs only).

* A CRD admitted in the canonical updater's source-owned CRD admission table, `ADMITTED_CRD_QA` in `tools/evidence/update_evidence_index.py`, has a post-verdict close-run family at `audit/qa/<change-id>/close/<check_id>/primary.log`, each primary with its sibling `primary.log.path_proof.txt`. Each row of that table maps a CRD ID to its QA root and Index key prefix; another CRD needs its own row.  
* The family holds the same-run mechanical evidence of the change's close workflow: one primary per close-run check, rendered from that check's captured command, exit code, and output with a `pf27.step_log_header.v2` header as Plan Templates defines it. Its posture is `PASS`, `FAIL`, or `BLOCKED`, as Glow QA Guide "Close-pack truthfulness and same-run execution" requires.  
* The family is written after the final QA verdict. It neither reopens nor adds to the change's approved `qa_step_logs_manifest.json` or any `checks/` primary, and that manifest never lists it.  
* Only the canonical updater writes the family, through its close-run publication entrypoint `publish_crd_close_run_family`, inside one recoverable write transaction. The given results replace the whole family. The entrypoint requires the change's recorded QA family to exist.  
* The family's members are its validated primaries and their path proofs under `close/`, in a closed shape: each member is a directory, not a symlink, named by a valid lower-case check ID, and it holds only `primary.log` and `primary.log.path_proof.txt`. Anything else under `close/`, an aliased `close/` root, or a `close/` root without a primary is refused.  
* This is a scoped exception, for `close/` only, to the rule above that tools MUST NOT infer run state by enumerating subdirectories: the canonical updater discovers the family's members by enumerating `close/`. That rule continues to govern `checks/` and every other part of a QA root, where `qa_step_logs_manifest.json` stays the authoritative index.  
* Each primary has one Human Evidence Index row and one Machine Evidence Mirror record with artifact key `<key_prefix>.close.<check_id>.primary.log`, where `<key_prefix>` is the CRD's Index key prefix in the admission table, and Mirror role `log`. HDE Build Notes introduced this family under the rule for new standardized evidence families above.  
* No Epic close-run family is admitted. An Epic close run needs its own explicit admission later, as each CRD needs its admission row.
`````

Replacement block:

`````text
Close-run family exception (normative; admitted CRDs and Epics only).

* A CRD admitted in the canonical updater's source-owned CRD admission table, `ADMITTED_CRD_QA` in `tools/evidence/update_evidence_index.py`, has a post-verdict close-run family at `audit/qa/<change-id>/close/<check_id>/primary.log`, each primary with its sibling `primary.log.path_proof.txt`. Each row of that table maps a CRD ID to its QA root and Index key prefix; another CRD needs its own row.  
* An Epic admitted in the canonical updater's source-owned Epic close admission table, `ADMITTED_EPIC_CLOSE` in the same file, has the same family at `audit/qa/<epic-id>/close/<check_id>/primary.log`, each primary with its sibling `primary.log.path_proof.txt`. Each row of that table maps an Epic ID to its QA root and Index key prefix. The table admits HDE-EPIC041 only; another Epic close run needs its own row and its own explicit Product Owner admission.  
* The family holds the same-run mechanical evidence of the change's close workflow: one primary per close-run check, rendered from that check's captured command, exit code, and output with a `pf27.step_log_header.v2` header as Plan Templates defines it. Its posture is `PASS`, `FAIL`, or `BLOCKED`, as Glow QA Guide "Close-pack truthfulness and same-run execution" requires.  
* The family is written after the final QA verdict. It neither reopens nor adds to the change's approved `qa_step_logs_manifest.json` or any `checks/` primary, and that manifest never lists it.  
* Only the canonical updater writes the family, inside one recoverable write transaction, through its close-run publication entrypoint: `publish_crd_close_run_family` for an admitted CRD and `publish_epic_close_run_family` for an admitted Epic. The given results replace the whole family. The entrypoint requires the change's recorded QA family to exist. For an Epic, it renders each primary through the canonical QA harness's own renderer, writes neither the Epic's QA step-logs manifest nor any of its `checks/` primaries, and refuses if either changes during publication.  
* The family's members are its validated primaries and their path proofs under `close/`, in a closed shape: each member is a directory, not a symlink, named by a valid lower-case check ID, and it holds only `primary.log` and `primary.log.path_proof.txt`. Anything else under `close/`, an aliased `close/` root, or a `close/` root without a primary is refused.  
* This is a scoped exception, for `close/` only, to the rule above that tools MUST NOT infer run state by enumerating subdirectories: the canonical updater discovers the family's members by enumerating `close/`. That rule continues to govern `checks/` and every other part of a QA root, where `qa_step_logs_manifest.json` stays the authoritative index.  
* Each primary has one Human Evidence Index row and one Machine Evidence Mirror record with artifact key `<key_prefix>.close.<check_id>.primary.log`, where `<key_prefix>` is the change's Index key prefix in its admission table, and Mirror role `log`. An Epic's rows also carry `epic_id`. HDE Build Notes introduced this family, and its extension to admitted Epics, under the rule for new standardized evidence families above.
`````

## RL-10

- Source rows: C-18, C-17
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **8\. CI & Evidence \[Required-Now\]**` > `## **8.17 Live QA evidence layout (audit/qa/\\/) \[Required-Now\]**` > `### **8.17.1 Root and step directories**`
- Location within that section: run-in list "EPIC_QA_ROOT MAY contain:" under the run-in label "Epic QA root (per epic)."
- Original location: line 5424 (informative only; the exact old block below is the locator)
- Expected occurrences of the exact old block in the original: 1 (observed: 1)

Exact old block:

`````text
* close/ — for a CRD in the canonical updater's CRD admission table only, the post-verdict close-run family; written only by the canonical updater, never plan-owned (§8.17 "Close-run family exception").  
`````

Replacement block:

`````text
* close/ — only for a CRD in the canonical updater's CRD admission table or an Epic in its Epic close admission table, the post-verdict close-run family; written only by the canonical updater, never plan-owned (§8.17 "Close-run family exception").  
`````

## RL-11

- Source rows: C-04, C-05, C-07, C-10, C-17, C-18
- Change type: NEW_CANON
- Operation: `INSERT`
- Target document: PF12-Canon-HDE-Schemas-and-Artifacts (v2.9.7 original baseline)
- Complete authored heading path (raw original heading lines, outermost first): `# **9\) Change Log & Doc-Delta Hooks \[Required-Now\]**` > `## 9.6 Documentary drainage record — 2026-10-26`
- Location within that section: the end of "## 9.6 Documentary drainage record — 2026-10-26", immediately before the heading "# **Appendix A: UMS Schemas**"
- Gap location: immediately before original line 6165 (informative only; the anchors below are the locator)
- Expected occurrences of BEFORE immediately followed by AFTER in the original: 1 (observed: 1)
- The gap is the boundary between the end of BEFORE and the start of AFTER. Neither anchor is changed.

BEFORE anchor (it ends with 2 newline characters):

`````text
    proof logs.
```


`````

AFTER anchor (it ends with 1 newline character):

`````text
# **Appendix A: UMS Schemas**

`````

Inserted text (it ends with 2 newline characters):

`````text
## 9.7 Documentary drainage record — 2026-11-02

This record drains into PF12 the Product Owner decisions on evidence-tool output roots and governed gate check rows; the rules that planning documents and PF-Canon file identities are never inputs, as they bear on the close-pack writer and on Human Evidence Index, Machine Evidence Mirror and path-proof records; and the close-pack writer decisions as amended for HDE-EPIC041's admitted close run, all recorded in HDE Build Notes. It changes PF text only. HDE-CRD-0002 and HDE-EPIC041 are closed; neither those closures nor this record establishes a QA verdict, acceptance, Ops, deployment, register movement, or implementation of a rule this record states as required.

```yaml
doc_delta:
  id: "DOCDELTA-20261102-pf12-evidence-rules-and-epic-close-run-drain"
  date: "2026-11-02"
  author: "Claude Code — T-04 document worker"
  document_version: "v2.9.8"
  scope:
    catalogs: "false"
    schemas: "true"
    manifest_checksums: "false"
    validation: "true"
    evidence_index: "true"
    routing_only: "false"
    operation_boundary: "documented contracts and status only; no governed payload writes"
  targets:
    catalogs_changed: []
    schemas_changed: []
    other_artifacts_changed: []
    documented_contracts:
      - title: "Release attestation builder"
        path: "tools/evidence/build_release_attestation.py"
      - title: "Canonical JSON gate check log"
        path: "audit/gates/json_gate/canonical/json_gate_check_log.ndjson"
      - title: "Canonical JSON gate compare log"
        path: "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson"
      - title: "Canonical JSON gate tool"
        path: "tools/evidence/run_canonical_json_gate.py"
      - title: "Close candidate source v2 schema"
        path: "schemas/close_candidate_source.v2.json"
      - title: "Generic close-pack writer"
        path: "tools/qa/generate_epic_close_pack.py"
      - title: "Evidence Index updater"
        path: "tools/evidence/update_evidence_index.py"
      - title: "Epic close-run family"
        path: "audit/qa/<epic-id>/close/<check_id>/primary.log"
  summary: |
    Add to the release attestation builder's contract the exclusive claim of
    its output root, the refusal of writes through symlinks, and cleanup
    scoped to what the run created. Add the governed gate check row content
    rule for the canonical JSON gate logs and point their Evidence Catalog
    entries to it. State that no Machine Evidence Mirror record, Human
    Evidence Index row or path proof binds a planning-document or PF-Canon
    path. Record the v2 close-candidate source's planning records,
    requirement IDs, QA checks and QA verdict, the refusal of planning and
    PF-Canon paths as inputs, write-time-only PF title resolution, and the
    Epic tracked-issue ID form with its ADR-status-only mapping. Extend the
    absent-tolerant close-pack Index rows, the close-run pointer exception,
    and the post-verdict close-run family to an Epic admitted in the
    canonical updater's Epic close admission table, which admits HDE-EPIC041
    only.
  domain_impact:
    current_domains_changed: []
    future_promotions: []
    mathematical_or_public_numeric_change: "none"
  release_identity:
    frozen_input_changed: "false"
    manifest_changed: "false"
    release_id_expected_change: "false"
    prior_release_id: "77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e"
    computed_release_id: "77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e"
    disposition: "prior release_id remains valid; static SHA-256 of the unchanged catalog/manifest.json bytes at the source baseline commit"
  acceptance_impact:
    tokens_added: []
    tokens_removed: []
    tokens_unchanged: []
    decision_boundary: "no new QA, OPS, acceptance, deployment, register movement, or closure claim"
  validation:
    - behavior: "exclusive output-root claim, no writes through symlinks, and scoped cleanup by the release attestation builder"
      entrypoint: "python tools/evidence/build_release_attestation.py --output <external-empty-directory> --require-clean"
      result: "not-run by this documentary revision; the rules are required and their implementation is not asserted"
      evidence_path: "tools/evidence/build_release_attestation.py"
    - behavior: "closed issue tokens and repository-relative paths in governed gate check rows"
      entrypoint: "python tools/evidence/run_canonical_json_gate.py --check-only"
      result: "not-run by this documentary revision; the rule is required and its implementation is not asserted"
      evidence_path: "tools/evidence/run_canonical_json_gate.py"
    - behavior: "v2 source planning records, planning and PF-Canon input refusal, tracked-issue ID form and ADR-status-only mapping"
      entrypoint: "python tools/qa/generate_epic_close_pack.py --source <candidate-source> --check"
      result: "not-run by this documentary revision; schema and writer statically inspected"
      evidence_path: "schemas/close_candidate_source.v2.json"
    - behavior: "Epic close-pack rows and Epic close-run family for the admitted Epic"
      entrypoint: "python tools/evidence/update_evidence_index.py --check"
      result: "not-run by this documentary revision; implementation statically inspected"
      evidence_path: "tools/evidence/update_evidence_index.py"
    - behavior: "complete exact original-bound PF redline preparation and application"
      entrypoint: "TW-DRAIN-10 then TW-APPLY-10, both 100926.1"
      result: "recorded in the evidence path; this record states no outcome in advance"
      evidence_path: "docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md"
  evidence_updates: []
  index_and_mirror:
    human_index: "docs/evidence/INDEX.json"
    human_index_sentinel: "docs/evidence/INDEX.sha256"
    machine_mirror: "artifacts/evidence_index.jsonl"
    machine_mirror_checksum: "artifacts/evidence_index.jsonl.sha256"
    parity_status: "not-run; no governed evidence bytes, paths, records, sidecars, sentinels, or companions changed"
    required_updates: "none for this PF-text-only drainage; original owner rules continue to govern future payload changes"
  routing_titles_only:
    math: "HDE-Math-Spec"
    governance: "HDE-Governance"
    cli_api_vendor: "HDE-CLI-API-Vendor-Ref"
    architecture: "HDE Architecture"
  open_decisions: []
  traceability:
    pull_request: "https://github.com/amthorn78/glow-hdengine-v2/pull/826"
    source_baseline_commit: "e2b7427ff418ca8f08f05587c4a541308a76da56"
    publication: "document output only; canonical source publication remains separately governed"
  change_log_entry: |
    v2.9.8 / 2026-11-02 — Documentary drainage of the Product Owner decisions
    on evidence-tool output roots and governed gate check rows, and of the
    close-pack writer decisions as amended for HDE-EPIC041's admitted close
    run, into the release attestation, canonical JSON gate, close-pack,
    Machine Evidence Mirror, and Live QA evidence layout homes above.
    Canonical runtime and evidence bytes remain unchanged; the prior
    release_id remains valid. Exact preparation and application evidence is
    retained in the document output proof logs.
```


`````

END OF REDLINES
