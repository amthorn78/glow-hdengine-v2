## A. Inputs reviewed (read-only)

- `audit/qa/hde-epic022/remediation/s1_host_matrix/host_matrix.md`
- `audit/qa/hde-epic022/remediation/s1_host_matrix/selected_base_url.txt`
- `audit/qa/hde-epic022/remediation/s1_host_matrix/selected_host_label.txt`
- `audit/qa/hde-epic022/remediation/s1_host_matrix/headers_internal_version_sample.json`
- Selected base URL: `https://glow-hdengine-v2-production.up.railway.app`
- Selected host label: `prod_railway`

## B. `/internal/version` governed artifacts — generators and validators

- Primary generator/validator: `tests/transport/test_internal_version_contract.py::test_internal_version_invariants_and_artifacts` issues GET/HEAD/conditional requests via `adapter.http_reader.app.test_client()`, asserts header/body invariants, couples payload fields to `artifacts/identity/service_identity.json`, `artifacts/invocation.json`, and `catalog/manifest.json`, and writes the governed artifacts into `artifacts/ops/internal_version/` (body, sha sidecar, header captures, and two-run identity log).
- Acceptance scaffolding coverage: `tests/qa/test_epic022_acceptance_scaffold.py` and `tests/qa/test_epic022_close_pack_ready.py` require the internal_version artifacts to exist and bind them to EPIC022 tokens (e.g., `INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK`, `TWO_RUN_IDENTITY_OK`) and the close-pack bundle set.
- Evidence index tooling coverage: `tools/evidence/update_evidence_index.py` includes `artifacts/ops/internal_version/*` through `docs/evidence/INDEX.json`; `tools/evidence/orientation_demo.py` and `ci/checks/check_mirror_schema.sh` validate that each indexed artifact has a matching proof and size/sha entries.
- Current files under `artifacts/ops/internal_version/`:
  - Payload and digest: `body_get.json`, `body_get.json.path_proof.txt`, `body_get.sha256`, `body_get.sha256.path_proof.txt`
  - Headers: `headers_get.txt`, `headers_get.txt.path_proof.txt`, `headers_head.txt`, `headers_head.txt.path_proof.txt`, `cond_if_none_match_headers.txt`, `cond_if_none_match_headers.txt.path_proof.txt`, `cond_if_modified_since_headers.txt`, `cond_if_modified_since_headers.txt.path_proof.txt`, plus legacy `headers_cond_if_none_match.txt`, `headers_cond_if_modified_since.txt`
  - Coupling log: `two_run_identity.log`, `two_run_identity.log.path_proof.txt`
  - Enforced by: the transport contract test (content + digest consistency), EPIC022 QA scaffold (presence of the main header/body/log artifacts), and mirror/schema checks (proof shape/sha/size).

## C. Request-chain manifest presence and intended location

- No `request_chain_manifest.json` file exists in the repo (no hits from ripgrep or evidence indices).
- Observed placement pattern for governed ops artifacts: `artifacts/ops/internal_version/*` (internal_version family, enforced by `tests/transport/test_internal_version_contract.py::test_internal_version_invariants_and_artifacts` and the EPIC022 QA scaffold) and other ops proofs like `artifacts/ops/rails_open_scope.txt` and `artifacts/ops/no_io_guard.txt` (both indexed via `docs/evidence/INDEX.json`). A request-chain manifest location is therefore **TBD**; the minimal constrained options are either co-locating with the internal_version family under `artifacts/ops/internal_version/` or a parallel ops-level file under `artifacts/ops/`. Follow-up should decide based on how the manifest is coupled to `/internal/version` evidence and update the index accordingly.

## D. Path-proof mechanism (production and validation)

- Generation/write path: `tools/evidence/update_evidence_index.py::_write_path_proof` writes `<rel>.path_proof.txt` siblings with `path`, `size_bytes`, `sha256`, `mtime_utc`, and `produced_at_utc` (plus optional extras such as `mirror_body_sha256` for the mirror self-record). It is invoked for every indexed artifact, including the mirror itself (self-record gets `mirror_body_sha256`).
- Validation paths:
  - `ci/checks/check_mirror_schema.sh` (Python entrypoint) re-parses `artifacts/evidence_index.jsonl`, loads each proof, re-computes sha/size, enforces required keys, ISO-8601 UTC timestamps (no microseconds), monotonic mtime vs filesystem, and checks that the self-record proof contains `mirror_body_sha256`.
  - `tools/evidence/orientation_demo.py` reloads the rendered mirror and proofs to ensure sha/size alignment and canonical mirror body sha consistency, raising `ORIENTATION_MISMATCH`/`ORIENTATION_DRIFT` in `--check` mode if discrepancies appear.
- Format requirements: path proofs are colon-delimited key/value lines; required fields include `path`, `size_bytes`, `sha256`, `mtime_utc`, and `produced_at_utc`; the mirror proof also records `mirror_body_sha256`. Missing or mismatched fields trigger `SystemExit` errors in both validators.

## E. Governed evidence index/mirror toolchain (update + validation entrypoints)

- Update (write): `env SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py` (default scope; add `--epic-id HDE-EPIC020` only when explicitly refreshing EPIC020 bundles). Regenerates `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and all `.path_proof.txt` siblings.
- Orientation check/write: `env SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py` (write) and `... --check` (fail on drift or missing proofs); must run after the index update because it consumes the refreshed skeleton.
- Mirror schema check: `env SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python ci/checks/check_mirror_schema.sh` (despite the `.sh` suffix, the shebang is Python); validates ordering, required fields, proof anchors, sha/size, and the mirror self-record.
- Recommended refresh order (per `docs/EVIDENCE_INDEX.md` and in-tool comments): `update_evidence_index.py` (write) → `orientation_demo.py` (write) → `update_evidence_index.py --check` → `orientation_demo.py --check` → `ci/checks/check_mirror_schema.sh`.

## F. Minimal loci to touch in follow-up PRs

- `tests/transport/test_internal_version_contract.py` — adjust the generator/validator and emitted artifact filenames/content if the internal_version evidence needs refresh or new fields.
- `artifacts/ops/internal_version/*` (and associated `.path_proof.txt` files) — regenerate the governed artifacts after any contract or endpoint change.
- `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `docs/evidence/INDEX*.path_proof.txt`, `artifacts/evidence_index.jsonl.path_proof.txt` — re-render via `tools/evidence/update_evidence_index.py` to keep the index/mirror and proofs aligned with refreshed artifacts.
- `tools/evidence/orientation_demo.py` output (`audit/gates/topology/orientation_demo.txt`) — re-render after index/mirror changes to satisfy orientation coherence checks.
- `ci/checks/check_mirror_schema.sh` (only if schema rules need tightening/loosening for new artifacts such as a request-chain manifest) — ensure validation expectations match any new index fields or artifact roles.
