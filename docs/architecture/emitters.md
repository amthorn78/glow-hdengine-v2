docs/architecture/emitters.md  

Title: Single Emitter Canon — public JSON emission for CLI and Reader
Version: 2.0
Owner: Cyrano (Technical Writer)
Status: Canon (A3–A7 scope)
Cards: CORE-CLI-A3, CORE-READER-A5 (public body), A7 (transport lives outside this doc)

1. Purpose

Establish one canonical emitter used by both the CLI and the Reader dev harness. This prevents drift, locks the serializer/idempotence rules, and guarantees that the same inputs produce the same public bytes across tools. Transport (ETag/INM/304/HEAD) is documented in the Environment & Integration Plan v2.0; do not restate it here.

2. Canonical module (no alternatives)

Path: engine/emit_public.py

Entrypoint name: emit_public_envelope

Return type: LF-terminated UTF-8 bytes representing the minimal public JSON envelope.

Single source of truth: CLI and Reader MUST both call this emitter for public output. No duplicate serializer or preimage logic is permitted elsewhere.


3. Public envelope (contract reference)

Contract home: docs/contracts/reader_v1_public_bytes.md. This architecture page does not duplicate the example.

Canonical set of top-level keys (sorted): categories, eligible, idempotence_hash, meta, release_id.

Categories rule: categories contains exactly one object with only id:"harmony" and band ∈ {Cool, Open, Warm, Glow}.

Numeric policy: public envelope is numeric-free (bands only).

Determinism: AB↔BA parity and two-run identity MUST hold.


4. Canonical serializer (rules)

UTF-8; no BOM; ANSI-free.

Sorted keys (lexicographic).

Compact separators; parameters equivalent to separators=(',',':'), ensure_ascii=False.

Exactly one trailing newline (\n) on the final public JSON.


5. Idempotence preimage (rules)

1. Build the envelope omitting the idempotence_hash.


2. Canonically serialize that preimage (rules in §4), including the single trailing \n.


3. Compute sha256(preimage_bytes) to produce a lowercase 64-hex idempotence_hash.


4. Insert idempotence_hash, serialize canonically again, and return the final bytes.



6. AB↔BA parity (bytes)

Swapping inputs A and B MUST NOT change the public bytes. This requirement applies equally to CLI and Reader outputs.

7. Purity and safety

No import-time I/O or environment reads.

No network access; function is a pure transformation of validated inputs.

No file writes.

Any logs are keys-only and never include secrets or payloads.


8. Tooling usage (binding requirements)

CLI (hdctl showcompat): MUST call emit_public_envelope for stdout bytes.

Reader v1: MUST call the same emitter and place those bytes in the HTTP 200 body. (Transport headers/validators are governed by Environment & Integration Plan v2.0.)


9. Provenance and evidence (names only)

Closeouts MUST capture emitter provenance and absence of drift via artifact names (no commands here):

artifacts/cards/<CARD>/EMITTER_SHA256.txt — sha256 over the file bytes of engine/emit_public.py.

artifacts/cards/<CARD>/validation.log includes lines such as:

EMITTER_SHA256=<64hex>

NO_DUPLICATE_SERIALIZER_OK (no other public-serialization code paths)

EMITTER_IMPORT_OK (both CLI and Reader bind to the canonical emitter)

READER_EQ_CLI_AB_OK and READER_EQ_CLI_BA_OK (byte equality)



10. Unit checks and goldens (acceptance indicators)

Two-run identity on the same inputs.

AB↔BA byte identity.

Preimage recompute equals embedded idempotence_hash.

Final text ends with a single LF and is BOM-free.

Minimal envelope shape present and numeric-free.

Reader bytes == CLI bytes for identical inputs.


11. Change control

The public envelope remains frozen for A3–A5. Any change requires a lead-approved card and refreshed acceptance evidence.

New internal fields belong in the admin sidecar, not in the public envelope.

When the emitter changes, update provenance markers and re-run A3/A5 evidence.


12. Cross-references

Public body contract: docs/contracts/reader_v1_public_bytes.md.

Reader transport and validators (A7): Environment & Integration Plan v2.0.

CLI behavior and admin sidecar rules: docs/CLI_commands.md.
