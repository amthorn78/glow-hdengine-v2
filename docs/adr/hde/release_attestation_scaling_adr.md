# Release-attestation scaling decision

Status: implemented and superseded by HDE-EPIC038 final external-attestation admission; permanent PF-Canon drainage remains downstream.

## Problem

The release ID is the hash of `catalog/manifest.json`. A release input change therefore changes every current artifact that embeds that ID. Keeping those derivatives in Git made a release cut look recursive: the manifest changed, a source constant changed, many evidence files changed, their companions changed, and validation could repair the checkout while it was checking it.

The content hash was not the defect. The defect was making generated attestations part of the mutable source graph.

## Decision

1. `catalog/manifest.json` remains the only release identity input in Git.
2. Runtime identity derives its release ID once from that packaged canonical file. No generated release-ID source constant exists.
3. `scripts/cut_release_manifest.py` is the only normal release-cut writer. It requires an explicit version and UTC build time, refreshes the declared file hashes, and changes only the manifest.
4. Source validation is read-only: `scripts/release_id_recompute.py --check-manifest-only`.
5. `tools/evidence/build_release_attestation.py` copies the tracked source into a temporary Git repository, runs the release-attestation closure there, proves a read-only fixed point, and verifies the final nineteen-stage release-sanity gate for exact-source admission.
6. The strict `hde.release_attestation.v1` bundle is written only to an explicitly external empty directory. CI verifies it and publishes it with `actions/upload-artifact`.
7. Direct execution of `regenerate_identity_closure.py` in the source checkout is refused.
8. Existing checked-in EPIC022 release artifacts remain frozen capture-time records. They are not current runtime identity inputs and are not rewritten for later releases.
9. Git does not preserve filesystem mtimes, so clone-local `stat().st_mtime` is not evidence. Path-proof validity is determined by exact path, SHA-256, size, required companion fields, and UTC timestamp shape. `mtime_utc` remains capture-time provenance and seeds newly written proofs, but a later clone or cache restore cannot invalidate content-bound evidence or trigger a proof rewrite.
10. Non-identity artifacts must not embed the release manifest merely as incidental provenance. The registry report remains strict configuration evidence: its loader validates the manifest and catalog contract, but its emitted bytes bind only the registry catalogs. Release/source provenance belongs to the external attestation. This one-time separation prevents an otherwise unchanged config report and its bundles/index companions from churning on every release cut.

The resulting dependency direction is acyclic:

`tracked source -> canonical manifest -> release ID -> external attestation`

No edge points from the external attestation back into tracked source.

## Safety and compatibility

- The isolated child environment is allowlisted, closed-rails, and excludes database, bridge, vendor, and credential values.
- Host-specific virtual-environment files are not source inputs. The legacy tracked `.venv` entries are removed from Git (the ignored local environment remains on disk), and future tracked environment roots fail source inventory.
- The external output path must be outside the source tree and empty; existing output is never overwritten.
- The bundle binds the exact commit, a deterministic tracked-tree digest, manifest/release digest, sorted file inventory, hashes, sizes, build transcript, and final release admission.
- Success transcripts retain only stage, command, and exit-code facts; subprocess bytes and timing are not persisted, so repeated builds for one exact source produce an identical content tree.
- Unknown schema fields, mutation, missing or extra files, checksum drift, noncanonical bytes, a failure receipt, and a non-exact source in CI fail closed.
- Generated material that fails the retained secret-safety contract is omitted with names-only reason codes; its companions are omitted with it. A failed build removes partial output and emits only a names-only failure receipt.
- Frozen bridge-era roots and all OPS roots are explicit isolated-write refusals. The bundle verifier recomputes the current clean Git commit and tracked-tree digest when exact-source verification is required.
- `catalog` is package data, so installed wheels and source checkouts consume byte-identical manifest content.
- Public Reader/CLI identity bytes remain unchanged for the current manifest.

## Final HDE-EPIC038 attestation boundary

The current external attestation records final admission as `PR06R_B_FINAL_PASS` only when the source commit is exact, the tracked-tree and manifest-derived release identity verify, the wheel-installed entry point is exercised, and all nineteen release-sanity stages pass with no pipeline stop. It validates committed evidence and admitted OPS packets; it does not rerun OPS, perform Railway discovery, write a database, deploy production, move PF09 status, claim QA PASS, or close HDE-EPIC038.

The earlier PR-A stage-14 stop remains historical implementation context only. Current documentation and release validation should refer to the final exact-source nineteen-stage attestation rather than treating PR-A or downstream PR-06R-B wording as current workflow.

Permanent PF04/PF09/PF12 release-evidence wording and historical EPIC022 canonical-path semantics require later human drainage. This implementation does not edit PF-Canon or move any status.

For this exact portability defect, the authorized repo decision `SUPERSEDES` the clone-local mtime comparison clauses in PF12 — HDE Schemas and Artifacts (path-proof mtime semantics), PF14 — HDE Mechanics Guide (path-proof checks), and PF19 — Glow QA Guide (path-proof QA checks). It preserves their timestamp-format, hash, size, path, producer-ownership, and no-hand-edit requirements. Permanent wording drainage remains human-owned and downstream.

## Rollback

Revert the isolated builder, runtime manifest derivation, release-cut command, workflow publication, and this repo ADR together. Do not restore CI that repairs the source checkout. If external publication is unavailable, fail the release attestation job while leaving the manifest and source immutable.
