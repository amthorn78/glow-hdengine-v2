> **Note (EPIC-009):** The canonical human Evidence Index lives at `docs/evidence/INDEX.json`.
> Add new entries there first, then mirror key pointers here for quick navigation.

# Appendix-D — Evidence Index (EPIC-009)

## Ops rails refusal
* `artifacts/ops/rails_refusal_proof.txt`
* `artifacts/ops/no_io_guard.txt`

## Env-matrix (selection-only)
* `artifacts/runtime/env_matrix.snapshot.json`
* `artifacts/runtime/env_matrix.failure.json`

## Database (EPIC-009)
* `artifacts/db/ddl_applied.sql`
* `artifacts/db/check_schema.txt`
* `artifacts/db/check_constraints.txt`
* `artifacts/db/partition_plan.txt`
* `artifacts/db/grants.txt`
* `artifacts/db/ddl_fingerprint.json`
* `artifacts/db/migration_runner.log`

## QA Runs
* `artifacts/qa/epic009_precommit_report.json`

## PF12 parity (human + machine)
* `docs/evidence/INDEX.json`
* `docs/evidence/INDEX.sha256`
* `artifacts/evidence_index.jsonl`

## Aux Narrative (EPIC-010) — Evidence
* `audit/gates/narratives/keys_10x4.table.json`
* `tests/transport/headers/aux_text_200.snap`
* `tests/transport/headers/aux_suppression_200.snap`

---

# Appendix-D — Evidence Index (EPIC-007)
## Step6
* `artifacts/epic007/ACCEPTANCE_NOTE.txt` — bytes: 79, sha256: 29567dac1cba71373a9eaa3125e4bce8118b4e62f8e94469317fecc229c6d2a0, added_in: EPIC007/Step6
* `artifacts/epic007/CLOSE_NOTE.txt` — bytes: 295, sha256: 911e6bfe3618a427f9602f34f75c9539b2aa15fc17d02642be7a41b3725d18a3, added_in: EPIC007/Step6

## Admin-QA
* `artifacts/admin/qa/M10_AB.json` — bytes: 1672, sha256: 2a6d96226a71c600b1d7eb38f4830d114fc6580f36cd41724576bcd2b7b84f09, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/M10_BA.json` — bytes: 1672, sha256: d5f9955ad726086e469d9c5bc4fb086edf11e0016ad568c0054a5e8f68a0ca02, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/Composite_AB.json` — bytes: 1348, sha256: 361211e377e35e5d1257b99fc3692dbe9aa0186226839b356fd32dfa82266695, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/M10_scores.csv` — bytes: 662, sha256: cbe5f03db6a914ecf2d6cd597a530fb4ffc7eb330826019ea3e207f705ea5c5e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/public_reader_AB.json` — bytes: 314, sha256: cd9c054901e6dec7b8d92ad9a03ab8f4c9ee8f0220c4b4d191eca6ca50b2864e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/public_reader_BA.json` — bytes: 314, sha256: cd9c054901e6dec7b8d92ad9a03ab8f4c9ee8f0220c4b4d191eca6ca50b2864e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/public_cli_AB.json` — bytes: 314, sha256: cd9c054901e6dec7b8d92ad9a03ab8f4c9ee8f0220c4b4d191eca6ca50b2864e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/public_cli_BA.json` — bytes: 314, sha256: cd9c054901e6dec7b8d92ad9a03ab8f4c9ee8f0220c4b4d191eca6ca50b2864e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/M10_AB.idempotence.sha256` — bytes: 65, sha256: f3c76a76460bcea5145fe3bf09b224a5c9257912cdb5e0f8bae97e13845cc1ef, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/M10_BA.idempotence.sha256` — bytes: 65, sha256: f3c76a76460bcea5145fe3bf09b224a5c9257912cdb5e0f8bae97e13845cc1ef, added_in: EPIC007/Admin-QA

## Step5
* `proofs/AB_BA_PARITY.txt` — bytes: 16, sha256: 7a7771ab8f5279a3bcde8b103d6ecaddd01a342b1c7dc870f5479aee894a00dd, added_in: EPIC007/Step5
* `proofs/TWO_RUN_IDENTITY.txt` — bytes: 20, sha256: b171a2d116394deebe5518f5f22c56b9073e681ae02dea22d3962f0873d408de, added_in: EPIC007/Step5

## Step3
* `artifacts/m10/thresholds_edge_cases.txt` — bytes: 471, sha256: 4279a194ff980dd90a95aff371fff26b0ce518e28bb53292972fc7d6b16a3fe2, added_in: EPIC007/Step3

## Step4
* `proofs/HELP_OK.txt` — bytes: 37, sha256: 644df560f3493b7f39888a6736f1b2a4592c55242c90da98d2be8b9a726adbd7, added_in: EPIC007/Step4
* `proofs/SERIALIZER_GUARD.txt` — bytes: 18, sha256: eaaa46f94c37817dc93a7d6e831c0a9bb32227053b6d67fd69344e5bf7a2a636, added_in: EPIC007/Step4
* `proofs/SUCCESS_SHAPE.txt` — bytes: 28, sha256: 1f3e4ca57e3515506702dfdad8610a406f7a33d39abbacb3c1067fe659056676, added_in: EPIC007/Step4
* `proofs/READER_CLI_PARITY.txt` — bytes: 28, sha256: de5004f9eaceae9f195410efbc3dcb70f5a4711a702afda7876adc649c4b231a, added_in: EPIC007/Step4

## Step2B
* `catalog/magic10_caps.json` — bytes: 900, sha256: ecd1f536717fc8ff32cd30cde7a2e6164a58effdd1c63ba67429985cba61b05b, added_in: EPIC007/Step2B
* `catalog/magic10_seeds.json` — bytes: 357, sha256: 446ca6dcbe3d25286e40f9acbac6f492d36eb7416280f0c29a3ff43cacac5b45, added_in: EPIC007/Step2B
* `catalog/manifest.json` — bytes: 1000, sha256: 47f42d29fb4e1196691f3dae28cfc0fa04ce5504e2511cd27eca9e325fe88921, added_in: EPIC007/Step2B
* `artifacts/math/release_id.txt` — bytes: 65, sha256: 7810de3f2201a8f30874af3dc2ac226a1ef13f2a75b64c3a1a2c7c97a72c867e, added_in: EPIC007/Step2B

## Step2A
* `catalog/magic10.json` — bytes: 124, sha256: ef4ec8dd591294f15ca870f038678116b7932782023301fd8885b1a870b07e64, added_in: EPIC007/Step2A
* `math/thresholds.json` — bytes: 82, sha256: 2148630897b32d037ce244a8602a5d8c811441d21c0ad47be9ebb1379d1d9185, added_in: EPIC007/Step2A

# Appendix-D — Evidence Index (EPIC-006)
**Transport — `/internal/version` (headers-only proofs)**
* `artifacts/proofs/internal_version_headers.json`
* `artifacts/proofs/internal_version_headers.txt`
**CLI proofs**
* `artifacts/proofs/cli_install.txt`
* `artifacts/proofs/cli_implemented_set.txt`
* `artifacts/proofs/cli_grep_guard.txt`
* `artifacts/proofs/cli_reader_parity.txt`
**QA artifacts**
* `artifacts/qa/cli/pair.reader.json`
* `artifacts/qa/cli/pair.reader.json.sha256`
* `artifacts/admin/qa/pair.left.bodygraph.json`
* `artifacts/admin/qa/pair.left.bodygraph.json.sha256`
* `artifacts/admin/qa/pair.right.bodygraph.json`
* `artifacts/admin/qa/pair.right.bodygraph.json.sha256`
* `artifacts/admin/qa/pair.composite.bodygraph.json`
* `artifacts/admin/qa/pair.composite.bodygraph.json.sha256`
* `artifacts/admin/qa/pair.compat.proof.json`
* `artifacts/admin/qa/pair.compat.proof.json.sha256`
**Mechanics**
* `artifacts/mech/constants_snapshot.json`
* `artifacts/mech/ordering_examples.jsonl`
* `artifacts/mech/identity_hash.txt`
**Identity & Math**
* `artifacts/identity/service_identity.json`
* `artifacts/math/release_id.txt`
* `artifacts/math/release_id_recompute.log`
* `artifacts/identity/emitter_sha256.txt`
**Database (present but out of scope)**
* `artifacts/db/conn_env.txt`
* `artifacts/db/attempts.json`
* `artifacts/db/check_schema.txt`
* `artifacts/db/grants.txt`
* `artifacts/db/rw_smoke.txt`
* `artifacts/db/read_guards.txt`
* `artifacts/db/check_constraints.txt`
* `artifacts/db/partition_plan.txt`
* `artifacts/db/ddl_applied.sql`
* `artifacts/ddl/DDL_BASELINE.sql`
**Ops pins**
* `artifacts/validation/service_cmd.txt`
* `artifacts/prod/exposure_note.md`

---

# Appendix-D — Evidence Index (EPIC-005, historical)

**Transport — `/internal/version`**

* `artifacts/headers/internal_version_200.txt`
* `artifacts/headers/internal_version_head.txt`
* `artifacts/headers/internal_version_if_none_match.txt`
* `artifacts/headers/internal_version_override_denied.txt`

**Identity & Math**

* `artifacts/identity/service_identity.json`
* `artifacts/math/release_id.txt`
* `artifacts/math/release_id_recompute.log`
* `artifacts/identity/emitter_sha256.txt`

**Database**

* `artifacts/db/ddl_applied.sql`
* `artifacts/db/check_schema.txt`
* `artifacts/db/check_constraints.txt`
* `artifacts/db/partition_plan.txt`
* `artifacts/db/grants.txt`

**Ops pins**

* `artifacts/validation/service_cmd.txt`
* `artifacts/prod/exposure_note.md`
