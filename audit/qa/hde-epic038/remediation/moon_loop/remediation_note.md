# HDE-EPIC038 PO-005 Artifact-Only Moon Loop

## Authorization

- On 2026-07-27, the Product Owner explicitly authorized a Moon Loop outside the governed QA loop only if it touches artifacts and does not change functional code.
- Scope is limited to the canonical A7 evidence producer, canonical evidence-graph maintenance, coherence validation, and an unchanged PO-005 rerun.

## Preserved failure

- Original receipt: `audit/qa/hde-epic038/remediation/moon_loop/qa-05-po-005.pre-remediation.log`
- Original receipt SHA-256: `ede383e356069e5c60a9b61cee8e443eb2791260c65c95664b0c1258432327ef`
- Failure signature: `DRIFT:artifacts/proofs/success_get.txt,artifacts/proofs/success_head.txt,artifacts/proofs/success_304.txt,artifacts/proofs/success_encoding_invariance.txt,artifacts/proofs/reader_success_get_head_304.json`
- Recorded pre-remediation verdict: `FAIL_BEHAVIOR`, exit code `1`.

## Root cause

- The five capture-time proofs retain the pre-seal Reader body SHA/ETag `fc98b90ac806180fb3b26503952be59be803bf661f42e05975bd0dd7404921a6`.
- Current in-memory A7 evaluation produces body SHA/ETag `68173614f2de96ecb445d2ff2ef17574d72b72dad7acca6482dbe84279f431e1`.
- Comparing the last matching capture source with current behavior changes only `release_id` and its derived `idempotence_hash`; status, header, length, encoding, and pass predicates remain unchanged.

## Boundaries

- No functional code, tests, schemas, release manifest, configuration, PF-Canon, acceptance map, manifest, close report, OPS evidence, token, public contract, or deployment change is authorized.
- Governed artifacts must be regenerated only by repository canonical tools; no governed artifact may be hand-edited.
- The original FAIL receipt remains preserved and must not be relabeled.
- A final PO-005 PASS is bounded to the unchanged check after the canonical evidence graph is coherent.

## Canonical remediation

- The A7 producer ran under `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, and `TZ=UTC`, with ambient vendor credential variables removed.
- `HDE_WRITE_A7_PROOFS=1 python tools/evidence/generate_a7_transport_proofs.py` changed only the five drifted A7 primaries.
- `python tools/evidence/update_evidence_index.py` refreshed their path proofs and the Machine Mirror family.
- `python tools/evidence/orientation_demo.py` completed without changing orientation bytes.
- The tracked delta is exactly 14 artifact files recorded in `changed_files.txt` and `patch.diff`.

## Tooling-only correction

- The first mirror-schema verification attempt incorrectly invoked the Python-shebang `ci/checks/check_mirror_schema.sh` through Bash.
- Failure signature: `ci/checks/check_mirror_schema.sh: line 2: import: command not found`.
- Minimal correction: invoke `ci/checks/check_mirror_schema.sh` directly so its declared Python interpreter is used.
- The incorrect attempt changed no files; the corrected direct invocation passed.

## Verification and rerun

- A7 check mode, Evidence Index check mode, orientation check mode, evidence-path validation, mirror schema, Evidence Index hash, final-LF, manifest-only identity validation, canonical JSON, and both Endpoint Catalog checksum checks passed.
- The unchanged PO-005 invocation then reported `a7 transport proofs check ok`, `6 passed`, and `BEHAVIOR_EXIT_CODE=0`.
- Final receipt: `audit/qa/hde-epic038/checks/qa-05-po-005/primary.log`
- Final receipt SHA-256: `eedce113352005d8dc4c30d754ef3ddca2b5ab30f357794248180702cf4b9ef7`
- Final recorded verdict: `PASS`, exit code `0`.

## Nonclaims

- This remediation does not claim public Reader expansion, deployment, production operation, OPS completion, QA-plan provenance repair, token satisfaction, PF09 movement, close-pack completion, or epic closeout.
- The A7 target remains the repo-classified dev-harness surface (`classification=dev_harness`, `internal=true`, `APP_ENV=dev`).
