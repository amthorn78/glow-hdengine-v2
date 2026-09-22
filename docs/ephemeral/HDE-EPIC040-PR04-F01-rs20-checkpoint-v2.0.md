---
artifact_type: RS20_CHECKPOINT
artifact_id: HDE-EPIC040-PR04-F01-RS20-CHECKPOINT
artifact_version: "2.0"
predecessor_version: "1.0"
predecessor_path: docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-checkpoint-v1.0.md
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR04 / RS-20 (GCF-17.RESCOPE), second decision
actor: Isis-50 — continuing independent Lead Developer reviewer for HDE-EPIC040
session_disposition: RETAIN_EXISTING
execution_posture: MANUAL_PROMPT_EXECUTION
decision: APPROVE
addendum_created: docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md
captured_at_utc: 2026-09-22T07:27:55Z
---

# HDE-EPIC040-PR04-F01 — RS-20 Working-State Checkpoint v2.0

One compact working-state note for the second RS-20 invocation on this finding. It introduces no registry, approval object or additional deliverable, and it carries no authority.

## Invocation state

| Field | Value |
| --- | --- |
| Stage | `RS-20 — Review Bounded Work-Unit Rescope — 091426.1`, second decision |
| Reviewed input | `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL` v1.1, read complete, SHA-256 verified |
| Companion read | `HDE-EPIC040-PR04-F01-RS30-REDLINE-APPLICATION-REPORT` v1.0, read complete, SHA-256 verified |
| Decision | `APPROVE` |
| Addendum | **one**, at `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` |
| Prior decision on this finding | `REVISION_REQUIRED`, this same session, 2026-09-22T06:48:06Z, no addendum |
| `context_conflict` | `NONE` |
| Interruption or compaction during this invocation | none |

## Repository observation window

| Field | Value |
| --- | --- |
| `main` head observed | `0f47079f24834424c4a4cfaba6a8d44d94286ad2` |
| Tree | `0865ef1814d238910b7da1e935d04124980aba34` |
| Working tree | clean before and after every observation |
| Repository mutation by this invocation | none, other than the four `docs/ephemeral/` artifacts this stage produces |
| Scratch worktree | created under the session scratchpad for the simulation, then removed; `git worktree prune` run; `git worktree list` shows only the primary checkout |
| Storage state correction | PR #463 has merged since the handoff was written; v1.1 and its companion were read from `main` |

## Executed observations

All under `LC_ALL=C LANG=C TZ=UTC`, closed rails except where a job definition declares otherwise. Dev test dependencies installed from `requirements.txt` and `requirements-dev.txt`; `python -m pytest --version` reported `pytest 8.4.2` as readiness proof. No network vendor call, no database operation, no governed-artifact write.

The simulation applies a PR04-shaped change inside the removed scratch worktree only: `engine/runtime/public.py::_compute_harmony_band` routed through the admission owner instead of `ts_v0`, and `adapter/http_reader.py::reader_v1_post` implementing the instruction §6.5 success path at its existing declared route.

| ID | Check | Result |
| --- | --- | --- |
| W-01 | `main` head, tree, clean status; non-documentation diff from `6ecacafb` | head `0f47079`; diff empty; no commit since `332fa4c` touches a non-`docs/` path |
| W-02 | SHA-256 of proposal v1.1, companion report, proposal v1.0, review v1.0 | all four match |
| W-03 | PF10 resolution and hash from `docs/pfcanon/` | unique PF10 Markdown; `1421e4d6…` matches; read complete |
| W-04 | `adapter/http_reader.py` membership in `catalog/manifest.json` | **member**, first of the fifteen entries |
| W-05 | Rails chain under simulation: `run_rails_job_definitions.py` over all three job files | rc=1; 18 failures in `tests/evidence/test_open_rails_abba_proof.py`; `tests/bodygraph/test_vendor_client.py` passed |
| W-06 | Rails chain: `pytest tests/evidence/test_rails_ci_workflow_integration.py` | 1 failed, 123 passed; the failure is `test_open_rails_producer_check_mode_has_no_repo_residue` on `INCOMPLETE_RELEASE_ROSTER` |
| W-07 | Release chain: the lane's four-file pytest set | 2 failed, 50 passed — `tests/runtime/test_identity.py` and `tests/evidence/test_release_manifest_content_binding.py`; `tests/evidence/test_release_attestation.py` fully green |
| W-08 | Full-validation chain: the complete 40-member supplemental roster | 14 failed, 1,207 passed, across five files, every one inside the enumeration or inside loci PR04 already owns |
| W-09 | `tools/evidence/run_canonical_json_gate.py --check-only` under simulation | rc=1 |
| W-10 | `generate_determinism_gate_proofs.py` declared outputs | six, not the five the proposal lists; the sixth is `artifacts/cards/a3/IDENTITY_OK.txt` |

## Sources resolved

- PF10: `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`, read complete. No non-Markdown, export, archive or search-hit variant was opened, compared or cited. `docs/pfcanon/` was read only and never written.
- Active overlays read at their repository paths; §2.8, §2.10, §2.12 and §2.13 read in full as load-bearing.
- Google Drive was not used as a source, store or authority at any point in this invocation.

## Artifacts produced by this stage

| Artifact | Repository path |
| --- | --- |
| Decision | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` |
| PF10 addendum overlay | `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` |
| Checkpoint | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-checkpoint-v2.0.md` |
| Handoff | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs20-handoff-v2.0.md` |

## Not performed

No implementation, product branch or pull request for PR04; no Proceed requested, minted or fabricated; no merge or auto-merge; no rerun of accepted-final PR01, PR02 or PR03; no IA-30 or IA-40 restart; no rewrite of the immutable Plan; no PF10 edit, number allocation, addendum drainage or canonical-adoption claim; no empty addendum drafted; no `PR-50` invocation or routing; no QA, Ops, deployment, release promotion, PF09 movement, acceptance or closure; no decision on the separately recorded `HDE-EPIC040-PR04-F02` candidate; no write outside `docs/ephemeral/`.
