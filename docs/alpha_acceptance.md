docs/alpha_acceptance.md 

Title: Glow Alpha Acceptance — A3 (CLI) and A5 (Reader v1 dev harness)
Version: 1.4
Owner: Cyrano (Technical Writer)
Status: Canon
Cards: CORE-CLI-A3, CORE-READER-A5

1. Purpose

Provide a single, prescriptive acceptance gate for Alpha. This verifies public stdout invariants, AB↔BA byte identity, idempotence preimage coupling, strict sidecar gating for CLI, and byte equivalence between Reader v1 and CLI.

2. Governance

Work on main. Deliver one revert-friendly commit with the evidence bundle under artifacts/cards/<CARD>/. PO performs acceptance. No PRs for final approval.

Acceptance uses SAFE rails. Default SAFE_MODE=1. Vendor HTTP is allowed only when SAFE_MODE=0 and ALLOW_NETWORK=1.


3. Canon pins

Canonical serializer: UTF-8, no BOM, sorted keys, compact separators, ensure_ascii=False, exactly one trailing \n.

Idempotence preimage: idempotence_hash = sha256(canonical_preimage_bytes) where the preimage omits idempotence_hash and is LF-terminated.

Public envelope keys (sorted): categories, eligible, idempotence_hash, meta, release_id.

Categories rule: categories has exactly one object with only {"id":"harmony","band":"Cool|Open|Warm|Glow"}. Public payload is numeric free.

A5 transport guard: Reader v1 in A5 does not emit ETag or Cache-Control. Conditional GET and caching appear in A7 and are covered by the Environment and Integration Plan v2.0.


4. A3 — CLI acceptance

4.1 Command surface

hdctl showcompat accepts two people (A and B). Per person time zones are required unless embedded in charts. The parser uses no flag abbreviation. Fetch commands are out of scope for Alpha.

4.2 Sidecar gate (TS-v0 minimal schema only)

Gate must be satisfied by all of: --showmath, --admin-out <path>, and either --admin or environment HD_ADMIN=1.

Negative gate: exit 2, stdout empty, no file created.

Positive gate: sidecar write is atomic, LF-terminated, mode 0600.

TS-v0 minimal keys only: type, strategy, features, decision, pair_order, correlation_id, rule_version, timestamp, warning.

Strategy strings: Generator or Manifesting Generator → Wait to respond; Projector → Wait for the invitation; Manifestor → Inform; Reflector → Wait a lunar cycle.


4.3 Required artifacts (exact paths)

artifacts/cards/A3/cli_stdout_AB.json
artifacts/cards/A3/cli_stdout_BA.json
artifacts/cards/A3/release_id.txt
artifacts/cards/A3/validation.log
# Optional when gate used:
artifacts/cards/A3/admin/sidecar.json

4.4 Required PASS markers (each as its own line in validation.log)

CLI_STDOUT_CANON_OK (UTF-8, BOM-free, ANSI-free, one trailing LF)

CLI_PREIMAGE_OK (recomputed hash equals idempotence_hash)

CLI_AB_BA_IDENTITY_OK (byte identical AB vs BA)

CLI_TWO_RUN_IDENTITY_OK (two runs produce identical bytes in the same release)

CLI_KEYS_CANON_OK (top level keys match the canonical set)

CLI_CATEGORIES_RULE_OK (single harmony category and allowed band)

CLI_RELEASE_ID_MATCH_OK (stdout release_id matches release_id.txt)

SIDECAR_GATE_NEGATIVE_OK (exit 2, no file)

SIDECAR_MODE_0600_OK and SIDECAR_LF_OK when the sidecar is present


5. A5 — Reader v1 acceptance

5.1 Scope

Reader v1 is a developer harness. It returns bytes identical to CLI for the same inputs. It is not production traffic.

5.2 Endpoint surface

GET /health returns ok\n.

GET /api/reader?v=1&a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA> returns LF-terminated public bytes identical to CLI.


5.3 Gating and path safety

If APP_ENV != dev, return 403 and do not access the filesystem. Body: {"error":"forbidden"}\n.

If APP_ENV == dev, allow reads only from fixtures/charts/*. Deny traversal and symlinks.


5.4 Transport policy for A5

Content-Type: application/json; charset=utf-8 for success and error bodies.

No ETag and no Cache-Control in A5. No conditional 304. These appear in A7.


5.5 Required artifacts (exact paths)

artifacts/cards/A5/reader_AB.json
artifacts/cards/A5/reader_BA.json
artifacts/cards/A5/headers_AB.txt
artifacts/cards/A5/headers_BA.txt
artifacts/cards/A5/validation.log

5.6 Required PASS markers (each as its own line in validation.log)

READER_EQ_CLI_AB_OK and READER_EQ_CLI_BA_OK (body bytes equal CLI)

READER_PREIMAGE_OK (recomputed hash equals idempotence_hash)

READER_CT_JSON_OK (Content-Type correct)

READER_NO_ETAG_OK and READER_NO_CACHECTL_OK (no transport headers in A5)

READER_APP_ENV_GATING_OK and READER_PATH_SAFETY_OK


6. A7 note

A7 transport acceptance for Reader and Aux Narrative is defined in the Environment and Integration Plan v2.0. This Alpha document does not restate HTTP transport.

7. PO signoff template

[ALPHA ACCEPTANCE — PO SIGNOFF]
Cards: CORE-CLI-A3, CORE-READER-A5
Result: ACCEPTED
Release ID (64-hex): <value from artifacts/cards/A3/release_id.txt>
Verifier: Full Stack Guru
PO: Nathan
Date: <ISO 8601>
Notes: CLI and Reader bytes, preimage, invariants, sidecar gate, and minimal evidence verified on main.

8. Rollback

Revert the single acceptance commit on main. No migrations or global edits. Re-run the checks to confirm a clean state.

9. References

Glow Environment and Integration Plan v2.0

docs/contracts/reader_v1_public_bytes.md

docs/server/reader_v1.md

Glow HD Engine — CLI, API and Vendor Ingest Spec v0.1.5


