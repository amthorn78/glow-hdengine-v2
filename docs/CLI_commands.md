docs/CLI_commands.md  

Title: Glow CLI — “hdctl showcompat” (CORE-CLI-A3)
Version: 2.0
Owner: Cyrano (Technical Writer)
Status: Canon
Cards: CORE-CLI-A3

1. Purpose

Define the canonical CLI surface for “hdctl showcompat,” including: public stdout contract (keys, order, trailing newline rule), idempotence preimage, strict sidecar gate, exit codes, determinism checks, and the minimal evidence required for A3 acceptance. Transport and caching live in Environment & Integration Plan v2.0. The public body example lives in docs/contracts/reader_v1_public_bytes.md.

2. Invocation (canonical)

Command accepts two people (A and B). Time zones are per person unless present in the chart files. Argument parser MUST disallow abbreviated flags.

Required

“--a <path-to-A.json>” and “--b <path-to-B.json>”


Optional

“--a-tz <IANA>” and “--b-tz <IANA>” when tz is not embedded in charts

“--score” to include a top-level numeric score (see §5)

“--showmath” and “--admin-out <path>” (admin sidecar; see §6)

“--admin” or environment “HD_ADMIN=1” (admin gate; see §6)


Acceptance runs SHOULD set SAFE_MODE to 1 (no vendor network).

3. Public stdout contract (A3)

Public stdout is numeric-free, bands-only, and is the only thing written to stdout on success. It MUST be:

UTF-8 JSON using the canonical serializer, exactly one trailing newline

BOM-free and ANSI-free

Top-level keys (canonical set; order induced by sorted keys):
categories, eligible, idempotence_hash, meta, release_id

Categories rule: the array contains exactly one object, with only id="harmony" and band in {Cool, Open, Warm, Glow}.


Source of truth for the body example: docs/contracts/reader_v1_public_bytes.md.

4. Idempotence preimage rule

The idempotence hash couples stdout to its canonical preimage.

Build the preimage by omitting the idempotence_hash field.

Serialize the preimage with the canonical serializer, including the single trailing newline.

Compute a lowercase 64-hex sha256 over those bytes and insert it as idempotence_hash.

The final stdout remains canonically serialized with exactly one trailing newline.

Acceptance recomputes and asserts equality between the recomputed hash and idempotence_hash.


5. Numeric policy (compatibility)

Reader is numeric-free (bands only).

CLI stdout shows bands by default.

Only when “--score” is present, stdout MAY include a top-level score_pct number in the inclusive range 0.00–100.00, rounded half-up to two decimals.

The presence or absence of score_pct MUST NOT change any other fields, order, or bytes besides the addition or removal of that field. AB↔BA parity and two-run identity still hold.


6. Admin sidecar gate (TS-v0 minimal schema)

The admin sidecar is private and excluded from the preimage. It is written only when the strict gate is satisfied.

Gate MUST be satisfied by all of: “--showmath” and “--admin-out <path>” and either “--admin” or environment “HD_ADMIN=1”.

If the gate is not satisfied, the command MUST exit with code 2, stdout empty, and no sidecar created.

Sidecar write MUST be atomic, LF-terminated, and file mode 0600.

TS-v0 minimal schema keys: type, strategy, features, decision, pair_order, correlation_id, rule_version, timestamp, warning.

Exact strategy strings:
Generator / Manifesting Generator → “Wait to respond”; Projector → “Wait for the invitation”; Manifestor → “Inform”; Reflector → “Wait a lunar cycle”.

Features: strategy_match (bool), sacral_pair (bool; true only when both are Generator/MG), projector_to_generator (bool).


7. Exit codes

0 success
2 gate misuse (strict sidecar gate not satisfied)
3 missing or invalid per-person time zone (A or B)
4 invalid path or missing required file

> 4 unexpected error



8. Determinism and parity

AB↔BA parity: swapping A and B MUST NOT change public stdout bytes.

Two-run identity: repeating the same run MUST produce identical bytes for the same release.


9. Minimal acceptance evidence (A3)

Produce the following evidence files and PASS markers (names are exact). No command snippets are provided here.

Artifacts (paths are exact)

artifacts/cards/A3/cli_stdout_AB.json

artifacts/cards/A3/cli_stdout_BA.json

artifacts/cards/A3/release_id.txt

artifacts/cards/A3/validation.log

Optional (only if gate is exercised): artifacts/cards/A3/admin/sidecar.json


PASS markers (each as a separate line in validation.log)

CLI_STDOUT_CANON_OK (UTF-8, BOM-free, ANSI-free, one trailing newline)

CLI_PREIMAGE_OK (recomputed sha256 over canonical preimage equals idempotence_hash)

CLI_AB_BA_IDENTITY_OK (byte-identical AB vs BA)

CLI_TWO_RUN_IDENTITY_OK (byte-identical across two runs in the same release)

CLI_KEYS_CANON_OK (top-level keys match the canonical set and induced order)

CLI_CATEGORIES_RULE_OK (exactly one category; id “harmony”; band in {Cool, Open, Warm, Glow})

CLI_RELEASE_ID_MATCH_OK (release_id in stdout matches the 64-hex in release_id.txt)

SIDECAR_GATE_NEGATIVE_OK (gate not satisfied → exit 2, stdout empty, no file)

SIDECAR_MODE_0600_OK (when present)

SIDECAR_LF_OK (when present)


10. Release identity

The release_id is the 64-hex sha256 of release/manifest.sorted.json and MUST match the value present in stdout. The same value MUST be present in artifacts/cards/A3/release_id.txt.

11. References

Environment & Integration Plan v2.0 (A7 transport; conditional GET; caching validators)

docs/contracts/reader_v1_public_bytes.md (canonical public body example and worked preimage)

Glow HD Engine — CLI, API & Vendor Ingest Spec v0.1.5 (normative definitions and invariants)


Supersedes v1.2 and de-duplicates any transport details to Environment & Integration Plan v2.0.