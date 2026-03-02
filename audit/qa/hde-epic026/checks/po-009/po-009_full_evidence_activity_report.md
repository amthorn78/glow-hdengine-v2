# HDE-EPIC026 — CHECK po-009 Full Evidence and Activity Report

## Report metadata
- generated_utc: 2026-03-01T02:38:00Z
- scope: Remedial CHECK po-009 execution + EPIC026 close-pack and gate run
- repo: glow-hdengine-v2
- branch: main

## Activity timeline (executed)
- Captured showcompat help and derived conjunction commands from help-supported flags.
- Corrected conjunction invocation to use pair input mode for no-real-user execution.
- Resolved local tooling blocker by installing psycopg[binary] in the workspace Python environment.
- Re-ran po-009 under deterministic pins and rails matrix (closed/open).
- Ran EPIC026 close-pack generator and evidence gates under closed rails.

## Determinism and rails posture
- LC_ALL=C
- LANG=C
- TZ=UTC
- Closed rails run: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev
- Open rails runs: SAFE_MODE=0, ALLOW_NETWORK=1, APP_ENV=dev

## Command evidence (po-009)
- HELP_RC=0
- AB command: /workspaces/glow-hdengine-v2/.venv/bin/python -m engine.cli showcompat --conjunction --pair-file audit/qa/hde-epic026/checks/po-009/_pair_ab.json
- BA command: /workspaces/glow-hdengine-v2/.venv/bin/python -m engine.cli showcompat --conjunction --pair-file audit/qa/hde-epic026/checks/po-009/_pair_ba.json

## CHECK po-009 results
- closed_rails_rc=1
- closed_rails_classification=REFUSED_TYPED
- open_rails_ab_rc=0
- open_rails_ba_rc=0
- open_rails_ab_sha256=2b5b684c246ebce8e8b7df05ec868f3d7ffd6d4f8ef8139fbad95adfae0e211c
- open_rails_ba_sha256=2b5b684c246ebce8e8b7df05ec868f3d7ffd6d4f8ef8139fbad95adfae0e211c
- open_rails_ab_canonical=OK canonical-json
- open_rails_ba_canonical=OK canonical-json
- abba_identity=SAME sha256_match

## EPIC026 close-pack and gate run results
- epic026_close_pack_rc=0
- gate_evidence_paths_validation_rc=0
- gate_lf_endings_rc=0
- close_pack_captured_at_utc=2026-03-01T02:35:26Z
- close_pack_run_id=epic026-close
- close_pack_key_output_count=159
- qa_step_manifest_generated_utc=2026-03-01T02:35:26Z
- qa_step_manifest_check_count=12

## Required/primary evidence files for this run
- audit/qa/hde-epic026/checks/po-009/primary.log
- audit/qa/hde-epic026/checks/po-009/showcompat_help.txt
- audit/qa/hde-epic026/checks/po-009/command_used.txt
- audit/qa/hde-epic026/checks/po-009/closed_rails_stdout.log
- audit/qa/hde-epic026/checks/po-009/closed_rails_stderr.log
- audit/qa/hde-epic026/checks/po-009/closed_rails_rc.txt
- audit/qa/hde-epic026/checks/po-009/closed_rails_classification.txt
- audit/qa/hde-epic026/checks/po-009/open_rails_ab_stdout.log
- audit/qa/hde-epic026/checks/po-009/open_rails_ab_stderr.log
- audit/qa/hde-epic026/checks/po-009/open_rails_ab_rc.txt
- audit/qa/hde-epic026/checks/po-009/open_rails_ab_sha256.txt
- audit/qa/hde-epic026/checks/po-009/open_rails_ab_canonical_json_check.txt
- audit/qa/hde-epic026/checks/po-009/open_rails_ba_stdout.log
- audit/qa/hde-epic026/checks/po-009/open_rails_ba_stderr.log
- audit/qa/hde-epic026/checks/po-009/open_rails_ba_rc.txt
- audit/qa/hde-epic026/checks/po-009/open_rails_ba_sha256.txt
- audit/qa/hde-epic026/checks/po-009/open_rails_ba_canonical_json_check.txt
- audit/qa/hde-epic026/checks/po-009/abba_identity_check.txt
- audit/qa/hde-epic026/checks/po-009/epic026_close_pack_stdout.log
- audit/qa/hde-epic026/checks/po-009/epic026_close_pack_stderr.log
- audit/qa/hde-epic026/checks/po-009/epic026_close_pack_rc.txt
- audit/qa/hde-epic026/checks/po-009/gate_evidence_paths_validation_stdout.log
- audit/qa/hde-epic026/checks/po-009/gate_evidence_paths_validation_stderr.log
- audit/qa/hde-epic026/checks/po-009/gate_evidence_paths_validation_rc.txt
- audit/qa/hde-epic026/checks/po-009/gate_lf_endings_stdout.log
- audit/qa/hde-epic026/checks/po-009/gate_lf_endings_stderr.log
- audit/qa/hde-epic026/checks/po-009/gate_lf_endings_rc.txt
- audit/EPIC-026_MANIFEST.json
- audit/EPIC-026_close_report.md
- audit/qa/hde-epic026/qa_step_logs_manifest.json
- audit/docdeltas/hde-epic026_doc_deltas.md
- audit/qa/hde-epic026/00_meta/doc_deltas.md

## Full epic evidence index reference
- Complete key_outputs inventory is authoritative in audit/EPIC-026_MANIFEST.json (key_outputs object).
- This manifest currently enumerates 159 governed output paths.

## QA step manifest snapshot
- po-001: checks/po-001/primary.log | sha256=18cdf88824df9681a8e06442422cce06f0a8f110b3dbc46286609c6d3b1e0a07 | size_bytes=1363
- po-002: checks/po-002/primary.log | sha256=0547fa4ca7b730b12439aee264d481206f50541f0db7800b086cffd166ae9bfd | size_bytes=1006
- po-003: checks/po-003/primary.log | sha256=9fc6188660f8f6bd92e861953d234899d23aac287748f7c076f2dafafb700888 | size_bytes=1036
- po-004: checks/po-004/primary.log | sha256=cf545563f658a1c33e4adae763264212158e4b9d8667e9669c7241ef64a80542 | size_bytes=860
- po-005: checks/po-005/primary.log | sha256=b1a9d07d48fd33674034a39aee9c3f81aed2f04015a917fb89065de603e6dd29 | size_bytes=1419
- po-006: checks/po-006/primary.log | sha256=50ebdea390633ae36461f50b09306980ed696d996363c6439b396f81e6cca4b5 | size_bytes=1248
- po-007: checks/po-007/primary.log | sha256=58688bfedeaf1b2e4955c0a14468c26581aa592c3e0380f526233bb39e55d2d2 | size_bytes=1580
- po-008: checks/po-008/primary.log | sha256=ee5da4fb490ac1f651811ce0024efc60aef6707035ce0e014f9b0bed752eca57 | size_bytes=1323
- po-009: checks/po-009/primary.log | sha256=f6b6fae41b2a95cc4e602ffac447c38662771b54ff829930321cc8ea3960e3c0 | size_bytes=3145
- po-010: checks/po-010/primary.log | sha256=c42dc1684d02d48a20b095240ea4e5eb90011a82cc2f55867d73bd634fe988ad | size_bytes=4672
- po-011: checks/po-011/primary.log | sha256=d78ec8902e79cf74971c6e2197f676e95152b43fce2c1e777eb2801fcebed74a | size_bytes=1318
- po-012: checks/po-012/primary.log | sha256=7f402e26085b7063d643520ef0cd91b58330cb37553483933087a7f30aefab93 | size_bytes=1377

## Outcome
- CHECK po-009 status: PASS (closed rails typed refusal + open rails canonical AB/BA success + ABBA identity SAME).
- EPIC026 close-pack generator: PASS (rc=0).
- Evidence paths gate: PASS (rc=0).
- LF endings gate: PASS (rc=0).
