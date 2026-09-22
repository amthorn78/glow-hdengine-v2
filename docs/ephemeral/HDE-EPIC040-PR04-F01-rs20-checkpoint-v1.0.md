---
artifact_type: RS20_CHECKPOINT
artifact_id: HDE-EPIC040-PR04-F01-RS20-CHECKPOINT
artifact_version: "1.0"
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR04 / RS-20 (GCF-17.RESCOPE)
actor: Isis-50 — continuing independent Lead Developer reviewer for HDE-EPIC040
session_disposition: RETAIN_EXISTING
execution_posture: MANUAL_PROMPT_EXECUTION
decision: REVISION_REQUIRED
addendum_created: NONE
captured_at_utc: 2026-09-22T06:48:06Z
---

# HDE-EPIC040-PR04-F01 — RS-20 Working-State Checkpoint v1.0

One compact working-state note for this RS-20 invocation. It introduces no registry, approval object or additional deliverable, and it carries no authority.

## Invocation state

| Field | Value |
| --- | --- |
| Stage | `RS-20 — Review Bounded Work-Unit Rescope — 091426.1` |
| Reviewed input | `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL` v1.0, read complete, SHA-256 verified |
| Decision | `REVISION_REQUIRED` |
| Addendum | **NONE** — only `APPROVE` creates one |
| Prior RS-20 decision on this finding | NONE; this is the first review of `HDE-EPIC040-PR04-F01` |
| `context_conflict` | `NONE` |
| Interruption or compaction during this invocation | none |

## Repository observation window

| Field | Value |
| --- | --- |
| `main` head observed | `a07340965c1dabbe0205135e321ecd6e76687d68` |
| Tree | `9ab2c9a9c3ed1dfb9aba127ee19c87fce8d98702` |
| Committed | 2026-09-22T07:35:39+01:00 |
| Working tree | clean before and after every observation |
| Repository mutation by this invocation | none, other than the three `docs/ephemeral/` artifacts this stage produces |
| Scratch worktree | created under the session scratchpad for simulations V-05 to V-08, then removed; `git worktree prune` run; `git worktree list` shows only the primary checkout |

## Executed observations

All under `LC_ALL=C LANG=C TZ=UTC`. Closed rails (`SAFE_MODE=1 ALLOW_NETWORK=0`) except where the job definition itself declares open rails, which is noted per row. No network vendor call, no database operation, no governed-artifact write. Dev test dependencies were installed from `requirements.txt` and `requirements-dev.txt` before pytest-dependent checks; `python -m pytest --version` reported `pytest 8.4.2` as readiness proof.

| ID | Command or check | Rails | Result |
| --- | --- | --- | --- |
| V-01 | `load_active_mechanics_bundle()` | closed | `SchemaValidationError INCOMPLETE_RELEASE_ROSTER` |
| V-02 | `catalog/manifest.json` `files` vs. `ADMITTED_RELEASE_ROSTER` | read-only | 15 vs. 44; strict subset confirmed set-wise |
| V-03 | `generate_open_rails_abba_proof.py --check-current` at baseline | `SAFE_MODE=0 ALLOW_NETWORK=1`, as `ci/jobs/rails_open_conformance.yml` declares | exit 0, `top_level_pass: true` |
| V-04 | release-sanity stage 04 and stage 05 validators at baseline | closed | both OK |
| V-05 | simulation A, rails-lane gate | open, as declared | exit 1, `INCOMPLETE_RELEASE_ROSTER` |
| V-06 | simulation A, stage 04 validator | closed | FAIL, same refusal |
| V-07 | simulation B, stage 05 validator | closed | FAIL, `AssertionError: writer` |
| V-08 | simulation B, `tests/http/test_reader_a7_transport.py` and `tests/transport/test_a7_transport_proofs.py` | closed | 8 failed, 13 passed |
| V-09 | `classify_paths(("ci/checks/classify_ci_changes.py",))` | read-only | all seven lanes true, `reason='selected_lanes'` |
| V-10 | lane union over PR05's Plan §6.5 owned loci | read-only | `{evidence, product, release}` |

Simulation A routes `engine/runtime/public.py::_compute_harmony_band` through the admission owner instead of `ts_v0`. Simulation B implements the instruction §6.5 Reader `POST` success path at the existing declared route. Both were applied only inside the removed scratch worktree.

## Sources resolved

- PF10: `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`, SHA-256 `1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f`, unique in `docs/pfcanon/`, read complete. No non-Markdown, export, archive or search-hit variant was opened, compared or cited. `docs/pfcanon/` was read only and never written.
- Active overlays read at their repository paths per proposal §2; PF10 §2.8, §2.12 and §2.13 read in full as load-bearing.
- Google Drive was not used as a source, store or authority at any point in this invocation.

## Artifacts produced by this stage

| Artifact | Repository path |
| --- | --- |
| Decision | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md` |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-checkpoint-v1.0.md` |
| Handoff | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-handoff-v1.0.md` |
| PF10 addendum | **none created** |

## Not performed

No implementation, product branch or pull request for PR04; no Proceed requested, minted or fabricated; no merge or auto-merge; no rerun of accepted-final PR01, PR02 or PR03; no IA-30 or IA-40 restart; no rewrite of the immutable Plan; no PF10 edit, number allocation, addendum drainage or canonical-adoption claim; no empty addendum drafted; no `PR-50` invocation or routing; no QA, Ops, deployment, release promotion, PF09 movement, acceptance or closure; no write outside `docs/ephemeral/`.
