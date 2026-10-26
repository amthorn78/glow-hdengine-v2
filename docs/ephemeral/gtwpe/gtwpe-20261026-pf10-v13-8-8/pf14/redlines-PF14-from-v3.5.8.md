# T-PF14 — exact redlines from PF14 v3.5.8

Run: `gtwpe-20261026-pf10-v13-8-8/T-PF14`. Preparation revision: `P1`.  
Originating preparer: TW-DRAIN-10 in the Nathan-started T-PF14 document session, Claude Code cloud session https://claude.ai/code/session_017fZuKCTMJn4EwZYu5ENvh1.  
Target: `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md` (`PF14-Canon-HDE-Mechanics-Guide` v3.5.8) at `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a`, byte-identical at `0838ba08254eaefc888019df49a06aa2ae99cc6c`: blob `3360a9eb1a5056274a31ad36739df8b04a4864c3`, 663,440 bytes, 7,722 LF characters (7,723 lines; the last line has no final LF), SHA-256 `0fb34a6534f685eb7abeeaab43e848f02e780d903507a597cee669678257b63a`.  
Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`, unchanged on `main`), task `T-PF14`, rows A06, A07, A10, A15, A26 and X07, with supporting cross-references X03, X04 and X06.  
Sources: PF10 v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter 1–223; addenda 2.6 (531–687), 2.7 (688–889), 2.10 (1102–1204), 2.15 (1620–1690) and 2.26 (2900–2986). Supporting cross-references at their ledger boundaries: X03, X04, X06 and X07. The proof log records every supporting read.  
Prompt: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.  
Preparation outcome: `READY` after whole-batch producer validation. Save completeness is recorded in the separate proof log.

These are 11 independent original-bound operations: 9 `REPLACE` and 2 `INSERT`. Header control fields are reserved for TW-APPLY-10. Payloads are literal: the single LF immediately before a closing fence is presentation only and is not part of the payload. Every other payload newline and every trailing space is exact. Fences are four backticks, longer than any backtick run in a payload. Each `REPLACE` OLD block consists of complete original lines, and RL-011's OLD block ends at the document-end boundary. Each `INSERT` defines its gap by adjacent BEFORE and AFTER anchors; the gap lies between the last byte of BEFORE and the first byte of AFTER, and both anchors stay unchanged. Every OLD block, BEFORE anchor, AFTER anchor and BEFORE+AFTER pair occurs exactly once in the whole original. The original line numbers are context only, not locators.

Document-control inputs for TW-APPLY-10. The header (original lines 5–10) carries `**Title:**`, `**Version:**` (`v3.5.8`, a dotted numeric version), `**Status:**` (`Canon`), `**Effective date:**` (`2026-10-09`, `YYYY-MM-DD`), `**Last Update Gate:**` (sources separated by `; `) and `**Invocation tag:**`, each line but the last ending in two spaces. The one source that justified this update is PF10 file `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, version 13.8.8 (gate form `BN 13.8.8`). The supporting cross-references X03, X04, X06 and X07 are read at the ledger's boundaries as supporting reading, not as change sources in their own right (ledger "Source register"). PF14 has no change log or revision-history section and no rule that requires one, so no change-history entry is prepared. No package redline touches the header, and no other line restates the document's version or effective date.

## RL-001

Redline number: RL-001  
Findings or source items: A26 (PF10 v13.8.8 addendum 2.26, FND-040; Required canon drainage, first bullet)  
Change type: CANON_UPDATE  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > `## **1.6 QA tooling bootstrap & Live QA harness (mechanics)**` > `### **1.6.3 Generic Epic/CRD QA harness (local records, governed publication, legacy viability)**`  
Original-bound location: the "Current-family validation and publication" list, the bullet that begins "* Source-owned updater admission"  

Original line (context only): 913  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: Addendum 2.26 FND-040 finds that this bullet limits updater admission to HDE-CRD-0001 while the code admits HDE-CRD-0001 and HDE-CRD-0002 through the source-owned `ADMITTED_CRD_QA` table, and directs the drainage: state admission as the CRDs in that table, with their roots and Index keys, beside the close-run API. 2.26 records it as canon lagging approved, delivered behaviour, not a conflict: admission stays source-owned and explicit. Verified read-only on `main` `0838ba0`: `tools/evidence/update_evidence_index.py` lines 48-54 (the table and its comment), `_load_crd_qa_entries`, `publish_crd_check_family` and `publish_crd_close_run_family`, which refuse every ID outside the table.

OLD (415 bytes, SHA-256 `d930f162f445e1a83d9fa3aab05b63e31a59fa6315340f8b173965f5d2527053`)

````text
* Source-owned updater admission in `_load_crd_qa_entries` is limited to `HDE-CRD-0001`'s validated current manifest and selected primary logs. Optional absence on an unrelated fresh operation is different from a present, selected or indexed family that is incomplete. Validate selected retained rows before generic deduplication, including aliases and collisions. Other CRDs and unlisted files gain no admission.  
````

NEW (726 bytes, SHA-256 `b240e4bd5285b3b0c85663cf843fa613231138956f1cba5dd7733c9f5dac03eb`)

````text
* Source-owned updater admission is the `ADMITTED_CRD_QA` table in `tools/evidence/update_evidence_index.py`; `_load_crd_qa_entries` and both CRD publication entrypoints read it. It admits `HDE-CRD-0001` and `HDE-CRD-0002`, each limited to its validated current manifest, its selected primary logs and its close-run family below. Each admitted CRD has its own explicit row; the table is neither a check roster nor a directory-discovery rule. Optional absence on an unrelated fresh operation is different from a present, selected or indexed family that is incomplete. Validate selected retained rows before generic deduplication, including aliases and collisions. A CRD outside the table and unlisted files gain no admission.  
````

## RL-002

Redline number: RL-002  
Findings or source items: A26 (PF10 v13.8.8 addendum 2.26, FND-040)  
Change type: CANON_UPDATE  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > `## **1.6 QA tooling bootstrap & Live QA harness (mechanics)**` > `### **1.6.3 Generic Epic/CRD QA harness (local records, governed publication, legacy viability)**`  
Original-bound location: the "Current-family validation and publication" list, the bullet that begins "* The admitted root is"  

Original line (context only): 915  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: 2.26 FND-040 cites this line with the admission line and asks for the admitted CRDs' roots and Index keys. On `main` `0838ba0` the table maps `HDE-CRD-0001` to `audit/qa/hde-crd-0001` and `audit.qa.hde_crd_0001`, and `HDE-CRD-0002` to `audit/qa/hde-crd-0002` and `audit.qa.hde_crd_0002`; `_crd_qa_entry` builds the keys `<prefix>.qa_step_logs_manifest` and `<prefix>.checks.<check_id>.primary.log`. The bullet keeps the existing HDE-CRD-0001 keys as examples and its last sentence unchanged.

OLD (423 bytes, SHA-256 `a8d5a982a740a4af8d8d3b8cfc4544d3a42ea5ddc5bd5c57d3757a4308b9898a`)

````text
* The admitted root is `audit/qa/hde-crd-0001/`. Primary logs use `checks/<check_id>/primary.log`; the root manifest is `qa_step_logs_manifest.json`. Human Index keys are `audit.qa.hde_crd_0001.qa_step_logs_manifest` and `audit.qa.hde_crd_0001.checks.<check_id>.primary.log`. The existing source rows carry `artifact_key`, `discovered_physical_path` and their existing role; the canonical writer derives integrity fields.  
````

NEW (704 bytes, SHA-256 `49b233ab7d2f606b1478ad4247c57bb839855cd5e03b299b19c62f4705d1d216`)

````text
* The admitted roots, with their Human Index key prefixes, are `audit/qa/hde-crd-0001/` (`audit.qa.hde_crd_0001`) and `audit/qa/hde-crd-0002/` (`audit.qa.hde_crd_0002`). In each admitted root, primary logs use `checks/<check_id>/primary.log` and the root manifest is `qa_step_logs_manifest.json`. Human Index keys are `<prefix>.qa_step_logs_manifest` and `<prefix>.checks.<check_id>.primary.log`, where `<prefix>` is the root's key prefix, for example `audit.qa.hde_crd_0001.qa_step_logs_manifest` and `audit.qa.hde_crd_0001.checks.<check_id>.primary.log`. The existing source rows carry `artifact_key`, `discovered_physical_path` and their existing role; the canonical writer derives integrity fields.  
````

## RL-003

Redline number: RL-003  
Findings or source items: A15 with X03 (PF10 v13.8.8 addendum 2.15, "The close-run evidence family (introduced)"; S21 ADR "Affected canon and drainage consequences", HDE Mechanics Guide row: "§1.6.3 gains the close-run publication API"; Decision item 7); X07 (QA-70 review v1.0 §5, "CR-11 — decided"; listed by PF10 v13.8.8 addendum 2.35 among canon drainage items)  
Change type: NEW_CANON  
Operation: `INSERT`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > `## **1.6 QA tooling bootstrap & Live QA harness (mechanics)**` > `### **1.6.3 Generic Epic/CRD QA harness (local records, governed publication, legacy viability)**`  
Original-bound location: the gap between the bullet that begins "* The recovery guarantee is bounded" and the bullet that begins "* An authorized verification/check publication"  

Expected occurrence count: `1` for BEFORE, for AFTER and for the adjacent BEFORE+AFTER pair (whole original).  
Action: insert the complete INSERTED TEXT once at the gap between BEFORE and AFTER.  

Controlling basis and rationale: 2.15 introduces the post-verdict close-run family (path, content, status, single writer through the updater's close-run publication entrypoint, `close/`-only membership exception, no Epic family) and leaves drainage of the ADR's canon table to the Product Owner's canon maintenance; the ADR table names §1.6.3 for the close-run publication API, and ADR Decision item 7 gives its exact signature. 2.17 (supporting reading) supersedes 2.15 C-3 for pointer items only and extends C-1 and the approved design by its table; under "Does not change" it keeps the close-run family and its membership exception. CR-11 is decided `APPROVED_AS_CHANGED`, alternative (a), with HDE Mechanics Guide §1.6.3 as a drainage target: for a CRD, Step-0B's `00_meta` capture cannot be indexed by the governed writer, Step-0B's substance goes into an indexed check primary, and the draft ledger is a close-stage causal input another owner authors. Plan Templates owns Step-0B's own rules, so the bullet routes to it by title instead of restating them. Verified on `main` `0838ba0`: `publish_crd_close_run_family` (signature, `validate_crd_check_family` and `_run_once(check=True)` before any write, stale-member removal and whole-family replacement in one `_WriteTransaction`, no manifest or `checks/` write), `_crd_close_run_check_ids` (only `primary.log` and `primary.log.path_proof.txt` per member), `_crd_close_run_entry` (`<prefix>.close.<check_id>.primary.log`); `_load_crd_qa_entries` refuses an Index row under a CRD root other than the manifest and `checks/` or `close/` primaries; `audit/qa/hde-crd-0002/` holds no `00_meta/`.

BEFORE (299 bytes, SHA-256 `18613844059bdedfbe8a73a222109d1ba87aa2ab239e4cc5d4b88bc215456961`)

````text
* The recovery guarantee is bounded to handled exceptions and a single writer. It is not process-crash durability, cross-process locking, a global freeze, or simultaneous atomic visibility of all files to readers. Stable reads detect observed changes; they do not supply those stronger guarantees.  
````

AFTER (84 bytes, SHA-256 `a0062f2f77d9133da7cbaecec1f5795ed2da42206cd7188356ebaf4440f4c16e`)

````text

* An authorized verification/check publication must not claim a future final graph.
````

INSERTED TEXT (2045 bytes, SHA-256 `4bb6a69154e116e20fb2064732535ebd5801f0371efd1ae68f50c39f489e0351`)

````text

* The post-verdict close-run family of an admitted CRD is published only through `tools.evidence.update_evidence_index.publish_crd_close_run_family(config, results, *, captured_at_utc=None, coherence_verifier=None)`, a Python API in the same updater module as `publish_crd_check_family`; HDE-Build Notes introduces the family. Each member directory holds `audit/qa/<change-dir>/close/<check_id>/primary.log` and its sibling `primary.log.path_proof.txt`, and each primary is a full-v2 step-log header rendered from the captured command, exit code and output of one close-run check. The entrypoint requires a nonempty result family. Before writing, it refuses when the CRD's recorded QA family is absent or fails validation, or when the existing integrity graph is incoherent. It replaces the whole family inside one outer recovery transaction, with the bounds stated for `publish_crd_check_family`. It writes neither `qa_step_logs_manifest.json` nor any `checks/` primary, and that manifest never lists the family. The family's members are its validated primaries and their path proofs; anything else under `close/` is refused. This `close/`-only exception to manifest-listed membership leaves the current manifest the authoritative index of `checks/`. Human Index keys are `<prefix>.close.<check_id>.primary.log`. No Epic close-run family is admitted.  
* Step-0B for a CRD: the canonical writer indexes no `00_meta/` capture under a CRD root. A CRD's Step-0B capture is therefore recorded in the indexed primary of the QA plan check that performs it. That capture applies Step-0B's rules from Plan Templates in full, including its no-deltas determination and preservation rules, to both doc-delta surfaces: the draft ledger `audit/docdeltas/<change-dir>_doc_deltas.md` and any `00_meta/doc_deltas.md` surface. The draft ledger is a close-stage causal input of the CRD's close pack that another owner authors; the QA run does not write it. A `00_meta/doc_deltas.md` file left beside the family stays unindexed and is not admitted as evidence.  
````

## RL-004

Redline number: RL-004  
Findings or source items: A26 (PF10 v13.8.8 addendum 2.26, FND-040)  
Change type: CONSISTENCY  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > `## **1.6 QA tooling bootstrap & Live QA harness (mechanics)**` > `### **1.6.3 Generic Epic/CRD QA harness (local records, governed publication, legacy viability)**`  
Original-bound location: the "Closed-rails regression responsibilities" list, the bullet that begins "* Cover both existing Epic behavior and CRD local recording"  

Original line (context only): 1158  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: The same §1.6.3 admission rule that FND-040 corrects is restated here as a regression responsibility ("governed admission limited to 0001"). On `main` `0838ba0`, `tests/evidence/test_evidence_index_missing_state.py` asserts `admits only HDE-CRD-0001, HDE-CRD-0002; refused HDE-CRD-0003` for check-family publication and refuses unadmitted close-run publication. Only the bullet's last clause changes.

OLD (376 bytes, SHA-256 `db8c9154bdd1bb1279b569606683958f7492ba6d6bb6431b979a6b7dec011769`)

````text
* Cover both existing Epic behavior and CRD local recording; valid CRD widths at 9999, 10000 and 123456; all five statuses and tokenless full-v2 output; explicit-claim shape/subset safety; strict current-family byte/path/identity/status/own-log checks; optional absence versus selected incompleteness; rejection before deduplication; and governed admission limited to 0001\.  
````

NEW (503 bytes, SHA-256 `29748a3f9991dd31600cfe706668115fe21923eb0737efff42dc060b2497008e`)

````text
* Cover both existing Epic behavior and CRD local recording; valid CRD widths at 9999, 10000 and 123456; all five statuses and tokenless full-v2 output; explicit-claim shape/subset safety; strict current-family byte/path/identity/status/own-log checks; optional absence versus selected incompleteness; rejection before deduplication; and governed admission limited to the `ADMITTED_CRD_QA` set, with an unadmitted CRD refused by name by both the check-family and the close-run publication entrypoints.  
````

## RL-005

Redline number: RL-005  
Findings or source items: A07 (PF10 v13.8.8 addendum 2.7, Affected surfaces, canon doc-delta candidates: "its route table's /api/reader alias row"); X04 (WU-PR-03 plan v2.0 §18, first stale-document row)  
Change type: CANON_UPDATE  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **34\) Dev HTTP Harness (single home)**`  
Original-bound location: the "Routes in the bounded capture context" table, the row for `/api/reader?v=1`  

Original line (context only): 4915  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: 2.7 names this row a canon doc-delta candidate; X04 records it as stale. On `main` `0838ba0`, `get_reader_api_bp` is mounted under `/api` by every app factory (`adapter/http_reader.py::create_app`, `adapter/factory.py`, `adapter/wsgi.py`) and serves only `POST /api/reader` for `v=1` and `v=2`; every other method gets the governed `405` with `Allow: POST`. HDE-CLI-API-Vendor-Ref §5.4 "Production mount" (supporting reading) states that this mount "is not an alias of the dev GET surface". The row now states the production surface by reference to §9.2 and keeps the method and contract detail with the owning document, as the table's following sentence already routes it.

OLD (168 bytes, SHA-256 `0ae953d9adb4d6202f44e65c0ad8acdc0adbc348f83731c40d62fd8823333688`)

````text
| `/api/reader?v=1` | `GET`, `HEAD` only when the Reader blueprint is mounted under `/api` | Conditional alias of `/reader`, never a second contract or proof surface. |
````

NEW (336 bytes, SHA-256 `dcab4da6419bbf9ec7da7883b11ad07ba5ec3a9d44f1c1d8a3e4c704914395b4`)

````text
| `/api/reader?v=1`, `/api/reader?v=2` | `POST` only; every other method gets the governed `405` | Production Reader v1 and v2 surface (§9.2). Every app factory, the dev runner's included, mounts it under `/api`. It is not an alias of `/reader` and not a dev capture surface; the development-only `GET /reader?v=1` does not prove it. |
````

## RL-006

Redline number: RL-006  
Findings or source items: A07 (PF10 v13.8.8 addendum 2.7, AD-3; Affected surfaces: HDE Mechanics Guide §34 "Current repository posture" bind); A10 (PF10 v13.8.8 addendum 2.10, HDE Mechanics Guide §34 among the stale canon passages)  
Change type: CONSISTENCY  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **34\) Dev HTTP Harness (single home)**`  
Original-bound location: the paragraph that begins "**Required start and local examples.**"  

Original line (context only): 4930  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: AD-3 hardened the canonical runner to the required local capture profile (loopback bind, debugger and reloader off), and the code on `main` `0838ba0` carries it (see RL-008); the Addendum Index entry 2.8 records WU-PR-03's lineage acceptance, which 2.10 applies as an overlay. The conditional "After the runner is hardened to the required profile" is now satisfied and would contradict the updated repository posture; the requirement itself is unchanged.

OLD (131 bytes, SHA-256 `ed13136d7289387044e35f40481d521d6751fa57782d3ce94ad8d16cf08ed0de`)

````text
**Required start and local examples.** After the runner is hardened to the required profile, start the ordinary local capture with:
````

NEW (77 bytes, SHA-256 `1786f1493b28139c943a765b977413ff2d0522f8d784198a79dd19b9366b94a4`)

````text
**Required start and local examples.** Start the ordinary local capture with:
````

## RL-007

Redline number: RL-007  
Findings or source items: A07 (PF10 v13.8.8 addendum 2.7, AD-3); A10 (PF10 v13.8.8 addendum 2.10)  
Change type: CONSISTENCY  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **34\) Dev HTTP Harness (single home)**`  
Original-bound location: the paragraph that begins "This command is a documentation contract"  

Original line (context only): 4936  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: The sentence's caution that the command is not a claim that the current bind satisfies the loopback posture is stale once AD-3's loopback bind is delivered. The command stays a documentation contract, and the observed posture stays a separate static observation; the `PORT` override sentence is unchanged.

OLD (219 bytes, SHA-256 `3d05c807fc1a0abec3bf4f219ac402fc44e607d2619cce10bb4410959909e151`)

````text
This command is a documentation contract, not a claim that the current server bind satisfies the required loopback posture. For an explicit `PORT` override, replace `8000` in each local base URL with the effective port.
````

NEW (208 bytes, SHA-256 `31925d3a1eac286e8f263cea8dd9730b0de0d77e5bd62c931bccd7543d4fcfbf`)

````text
This command is a documentation contract; the current repository posture below is a separate static observation. For an explicit `PORT` override, replace `8000` in each local base URL with the effective port.
````

## RL-008

Redline number: RL-008  
Findings or source items: A06 (PF10 v13.8.8 addendum 2.6, Affected surfaces: the "Current repository posture" statement that the Reader handler treats missing APP_ENV as dev); A07 with X04 (addendum 2.7: "Current repository posture" bind, flags, CORS, APP_ENV default; WU-PR-03 plan v2.0 §18); A10 with X06 (addendum 2.10: HDE Mechanics Guide §34 among the stale canon passages of result v1.0 §10)  
Change type: CANON_UPDATE  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **34\) Dev HTTP Harness (single home)**`  
Original-bound location: the paragraph "**Current repository posture at `d7e8b4e7f07a844fd976dcd68a8cabe983891e75` (static inspection only).**" through the `docs/ENDPOINTS_CATALOG.json` bullet; the `.devcontainer/devcontainer.json` bullet that follows is unchanged  

Original lines (context only): 4944–4951  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: The posture block was a static inspection at `d7e8b4e`. 2.6, 2.7 and 2.10 record its bind, flags, CORS, APP_ENV-default and production-mount statements as stale after S10 (exact explicit-dev gate), AD-2 (exact comparison), AD-3 (loopback bind, explicit `debug`/`use_debugger`/`use_reloader`, test-backed absence of CORS headers) and S19-F02/S19-F03 (WU-PR-05: production-like posture refuses the dev-harness and retired routes). The block is re-inspected at `main` `0838ba0` and every bullet is restated from that inspection: `scripts/dev_start_reader.sh`; `adapter/http_reader.py` `__main__` run call and `_reader_dev_env_explicit`; `_mount_for_production`, `_PRODUCTION_DEV_WRITER_ROUTES`, `_PRODUCTION_RETIRED` and `adapter/env_guard.py::_compute_env_mode`; the registration of the root blueprint in `adapter/factory.py`, `adapter/wsgi.py` and `create_app`; `tests/http/test_reader_a7_transport.py::test_dev_runner_emits_no_cors_headers` and `::test_dev_runner_binds_loopback_with_debugger_and_reloader_off`; a bounded search finding no CORS reference in `adapter/` or `engine/http/` Python modules; and `docs/ENDPOINTS_CATALOG.json` (18 records). The catalog bullet keeps its nonclaim and drops the unverified negative about the complete PF05/PF12 projection, which this inspection did not re-establish. The production-posture bullet states only requests dispatched to the routes' handlers and does not characterize router-level answers (held item H-03, LR5-O1, is not drafted).

OLD (1207 bytes, SHA-256 `bbb5c8c5af4ad232b9e94cd3b8c3b11433c502f6f30df1aad6f0310ebbd20449`)

````text
**Current repository posture at `d7e8b4e7f07a844fd976dcd68a8cabe983891e75` (static inspection only).**

* `scripts/dev_start_reader.sh` invokes `python -m adapter.http_reader`, defaults `PORT=8000`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`, and propagates `APP_ENV` only when the caller supplies it.  
* `adapter/http_reader.py` binds `0.0.0.0`, not the required ordinary-local `127.0.0.1`; the loopback requirement is not currently satisfied.  
* The module invocation does not explicitly bind `debug=False`, `use_debugger=False`, or `use_reloader=False`; explicit capture controls remain required.  
* The selected factory contains no explicit CORS binding or test-backed disabled-CORS declaration; the disabled posture remains a requirement.  
* The Reader handler treats missing `APP_ENV` as dev; that behavior does not satisfy the explicit caller-supplied `APP_ENV=dev` requirement.  
* `docs/ENDPOINTS_CATALOG.json` includes the Reader `GET`/`HEAD` rows and `POST /internal/dev/sampler`, but it does not express the complete current PF05-Canon-HDE-CLI-API-Vendor-Ref and PF12-Canon-HDE-Schemas-and-Artifacts route-and-alias projection. Catalog conformance is not claimed.  
````

NEW (2441 bytes, SHA-256 `9a30b628f7229065fc938373f13a9860e23ca00a7eb1aa92e719517022f00177`)

````text
**Current repository posture at `0838ba08254eaefc888019df49a06aa2ae99cc6c` (static inspection only).**

* `scripts/dev_start_reader.sh` invokes `python -m adapter.http_reader`, defaults `PORT=8000`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`, and propagates `APP_ENV` only when the caller supplies it. Its banner shows `APP_ENV=<UNSET>` for an unset value and names host `127.0.0.1`.  
* `adapter/http_reader.py` runs `create_app()` on host `127.0.0.1`, with no host override, and on the effective `PORT` (default `8000`), and passes `debug=False`, `use_debugger=False`, and `use_reloader=False` explicitly. The checked-in run call meets the loopback requirement and sets the explicit capture controls.  
* No Python module under `adapter/` or `engine/http/` references CORS. `tests/http/test_reader_a7_transport.py` declares the disabled posture as tests: they assert that the dev runner's application emits no `Access-Control-*` header on `GET` or `HEAD /reader`, on a cross-origin `OPTIONS` preflight, or on an error response. This inspection does not establish that the tests pass.  
* The dev `GET /reader` handler serves only when `APP_ENV` is exactly `dev`, with no trimming or case-folding. Unset, empty, `test`, `local`, any case or whitespace variant of `dev`, and every other value refuse with `403 ERR_READER_FORBIDDEN`; a missing value is not treated as dev.  
* A production-like posture is decided once, when an app factory registers the root Reader blueprint: `APP_ENV`, or `ENGINE_ENV` when `APP_ENV` is unset or blank, is `prod`, `production` or `live` after trimming and case-folding. In that posture, `adapter.factory.create_app`, `adapter.wsgi.create_app` and `adapter.http_reader.create_app` keep the dev-harness and canon-retired rules in their URL maps and add one `before_request` hook that refuses requests dispatched to those routes' handlers: `GET` and `HEAD /reader` with `403 ERR_READER_FORBIDDEN`; `POST /internal/dev/sampler` and the three `/dev/*/conjunction` routes with `403 ERR_WRITER_FORBIDDEN`; and `/ops/db/unavailable`, `/ops/probe/env` and `/ops/writer/diagnostic` with `404 ERR_NOT_FOUND`. Under `APP_ENV=dev` the dev runner keeps the full mount.  
* `docs/ENDPOINTS_CATALOG.json` has 18 records, among them the Reader `GET` and `HEAD` rows, `POST /api/reader` and `POST /internal/dev/sampler`, and no record for a canon-retired route. Catalog conformance is not claimed.  
````

## RL-009

Redline number: RL-009  
Findings or source items: A15 with X03 (PF10 v13.8.8 addendum 2.15, What is approved: one writer with the v2 schema, CRD paths of record, directory form; S21 ADR "Affected canon and drainage consequences", HDE Mechanics Guide rows: "§37.2 'Governance & homes', 'Close-pack generator (mechanics; single-writer; normative)'" and "§37.2 epic-scoped close-pack filename list"; Decision items 2 and 3)  
Change type: CANON_UPDATE  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > `## **37.2 Governance & homes**`  
Original-bound location: the paragraph that begins "Where \\ is a zero-padded 3-digit epic number" through the paragraph that begins "Close-pack generator (mechanics; single-writer; normative):"; the first paragraph is unchanged  

Original lines (context only): 5029–5031  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: The ADR table directs two §37.2 changes: name `tools/qa/generate_epic_close_pack.py` as the generic close-pack generator for v2 sources beside the EPIC-025 entrypoint, and add the CRD filename form to the epic-scoped filename list. 2.15 approves the CRD paths of record and directory form. Combined into one REPLACE because both changes share the boundary between the two paragraphs. Verified on `main` `0838ba0`: `_derived_paths_v2` and `_supporting_paths_v2`, `CHANGE_RE` (four or more CRD digits), the CLI (`--source` required; `--write` and `--check` mutually exclusive and required), `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` and their `.path_proof.txt` siblings in the updater's path-proof format, and `audit/docdeltas/hde-crd-0002_doc_deltas.md`. The existing EPIC-025 sentence is kept verbatim.

OLD (446 bytes, SHA-256 `354e44897471aae5c1054d4aba217be2de21524532fd97c143070a67925a10b0`)

````text
Where \\ is a zero-padded 3-digit epic number (example: 022). These are governed artifacts and must not be duplicated under alternate spellings.

Close-pack generator (mechanics; single-writer; normative): A deterministic generator entrypoint MUST exist to write the close-pack artifacts above (and any required path proofs) at their canonical paths. For EPIC-025, the close-pack generator entrypoint is `tools/qa/generate_epic025_close_pack.py`.
````

NEW (1478 bytes, SHA-256 `d8313bedccd27e1827f639b55e3649cc343bcb28268975f462ff2a9469f4eb1e`)

````text
Where \\ is a zero-padded 3-digit epic number (example: 022). These are governed artifacts and must not be duplicated under alternate spellings.

CRD close-pack artifacts (canonical filenames): a CRD close pack uses the CRD ID as its prefix, `audit/HDE-CRD-<NNNN>_close_report.md` and `audit/HDE-CRD-<NNNN>_MANIFEST.json`, where `<NNNN>` is the CRD number of four or more digits. Each has a sibling `.path_proof.txt` transcript that the canonical updater writes. The CRD's lower-case ID is its directory form (for example `hde-crd-0002`), so its doc-delta ledger is `audit/docdeltas/hde-crd-<NNNN>_doc_deltas.md`. These are governed artifacts and must not be duplicated under alternate spellings.

Close-pack generator (mechanics; single-writer; normative): A deterministic generator entrypoint MUST exist to write the close-pack artifacts above (and any required path proofs) at their canonical paths. For EPIC-025, the close-pack generator entrypoint is `tools/qa/generate_epic025_close_pack.py`. For a `close_candidate_source.v2` source, Epic or CRD, the generic close-pack generator is `tools/qa/generate_epic_close_pack.py`. It takes exactly one `--source` and exactly one of `--write` or `--check`, renders the close report and manifest only from tracked inputs, publishes the manifest last and writes nothing in `--check` mode; a v1 source keeps the v1 model and output bytes. The canonical updater, not this generator, writes the pair's path proofs and Human Index rows.
````

## RL-010

Redline number: RL-010  
Findings or source items: A15 with X03 (PF10 v13.8.8 addendum 2.15, What is approved: "a key_outputs map of path strings"; C-4 summary of R-3; S21 ADR "Affected canon and drainage consequences", HDE Mechanics Guide row "§37.3 key_outputs rule"; Decision item 5)  
Change type: NEW_CANON  
Operation: `INSERT`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > `## **37.3 Conventions**`  
Original-bound location: the gap between the bullet "* key\_outputs MUST NOT be a list." and the paragraph that begins "For EPIC023, key\_outputs MUST include these bindings"  

Expected occurrence count: `1` for BEFORE, for AFTER and for the adjacent BEFORE+AFTER pair (whole original).  
Action: insert the complete INSERTED TEXT once at the gap between BEFORE and AFTER.  

Controlling basis and rationale: The ADR table directs §37.3's `key_outputs` rule to gain the v2 minimum; ADR Decision item 5 lists it (close report, close manifest, doc-delta ledger, drain-target ledger, QA step-logs manifest) and 2.15 C-4 summarizes R-3 (every key output other than the report and manifest is also a bound tracked input). Verified on `main` `0838ba0`: `_require_v2_semantics` requires exactly these five keys with the derived path values and refuses an unbound extra value with `OUTPUT_BINDING_MISMATCH`; `audit/HDE-CRD-0002_MANIFEST.json` `key_outputs` holds these five bindings.

BEFORE (34 bytes, SHA-256 `c1b85dddb4a38a97a6d19722fd613baad1fa8e3ed6aeb11058c6284765d210e0`)

````text
* key\_outputs MUST NOT be a list.
````

AFTER (79 bytes, SHA-256 `54ec098da89c171500fec16a56ea9da5964b36bbda7769f7c5983e2c70d08495`)

````text


For EPIC023, key\_outputs MUST include these bindings (keys \+ exact values):
````

INSERTED TEXT (888 bytes, SHA-256 `c001542a877c1c605258f880159cd99138c4d4a17039cb634312a8a5faee758b`)

````text


For a `close_candidate_source.v2` close pack, Epic or CRD, `key_outputs` MUST include at least these bindings, each value a repo-relative path string. `<prefix>` is `EPIC-<NNN>` for an Epic and the CRD ID for a CRD, and `<change-dir>` is the change's lower-case ID:

* `close_report`: `audit/<prefix>_close_report.md`  
* `close_manifest`: `audit/<prefix>_MANIFEST.json`  
* `doc_deltas`: `audit/docdeltas/<change-dir>_doc_deltas.md`  
* `drain_targets`: `audit/docdeltas/<change-dir>_drain_targets.md`  
* `qa_step_logs_manifest`: `audit/qa/<change-dir>/qa_step_logs_manifest.json`

Every key output other than the close report and the close manifest MUST also be a bound tracked evidence input of the candidate source, so its digest is recorded; the generator refuses a mismatch with `OUTPUT_BINDING_MISMATCH`. Additional `key_outputs` entries are allowed under the same binding rule.
````

## RL-011

Redline number: RL-011  
Findings or source items: TW-DRAIN-10 100926.1, "Exact redline contract" (the revised PF carries no placeholder or unresolved drafting marker; this rule authorizes the removing redline as hygiene); PF03-Reference-Technical-Writing-Best-Practices §14 (no empty bullets)  
Change type: DOC_HYGIENE  
Operation: `REPLACE`  
Target document: `PF14-Canon-HDE-Mechanics-Guide`  
Section path: `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > `## **37.18 Index & synchronization**` > `### **37.18.3 EPIC029 close-pack baseline and OPS-01 dev-harness binding evidence**`  
Original-bound location: the end of the document: the "CI enforces:" list's last item and the two empty list items after it; the OLD block ends at the document-end boundary  

Original lines (context only): 7721–7723  

Expected non-overlapping occurrence count: `1` (whole original).  
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.  

Controlling basis and rationale: The document ends with two empty list items (`*   ` and `* `), unfilled placeholders after the final "CI enforces:" item. Removing them changes no requirement; the last real item loses its hard-break trailing spaces as the list's final item, matching the target's style, and the document keeps its original no-final-LF ending.

OLD (51 bytes, SHA-256 `879b0ba7040ba63094f471d0a90441ba1a46354cf9e3a80556080f774be8562e`)

````text
* presence and correctness of path-proofs  
*   
* 
````

NEW (41 bytes, SHA-256 `1bbb4a4783d4a5e73ff3035abf1e4c8bf4e312d9c6d0a39c41194c140d67b039`)

````text
* presence and correctness of path-proofs
````

END OF REDLINES
