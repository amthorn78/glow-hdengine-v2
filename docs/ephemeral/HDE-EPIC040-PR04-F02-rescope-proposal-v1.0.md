# HDE-EPIC040-PR04-F02 — Bounded Work-Unit Rescope Proposal v1.0

```yaml
artifact_type: RESCOPE_PROPOSAL
RESCOPE_PROPOSAL_ID: HDE-EPIC040-PR04-F02-RESCOPE-PROPOSAL
version: v1.0
state: RESCOPE_PROPOSAL_PENDING_REVIEW
repository_path: docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F02
finding_title: Manifest content binding refresh for adapter/http_reader.py
producer: dedicated PR04 PR-development session PR04-HDE-EPIC040-1, as the explicitly assigned finding author (RS-10 role; no approval authority)
receiver: RS-20 — Review Bounded Work-Unit Rescope — 091426.1, in the continuing whole-change HDE-EPIC040 IA session (Isis-50)
originating_stage: PR-20 planning (plan v1.1 issued alongside); no Proceed, workspace, worktree, branch, commit, open PR or CI run exists
PR_RETURN_PHASE: NOT_APPLICABLE
session_disposition: RETAIN_EXISTING
role_session_ref: PR04-HDE-EPIC040-1
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR04 / RS-10 (GCF-17.RESCOPE)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
prior_proposal_or_review_for_this_finding: NONE
recorded_by: HDE-EPIC040-PR04-F01-RESCOPE-REVIEW v2.0 §5 (candidate finding, undecided) and PF10 §2.15 "Separate boundary recorded and not decided"
repository: amthorn78/glow-hdengine-v2
target: main
baseline_main_head: 3b8084d09e974f15c2b71112e5a596af01b1a371
baseline_tree: 11e81c99b9194c38471b494c59b149d4f4553659
executable_baseline: 9cda1b49a972da874021e8820997fab1ebaff153
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md — sha256 abcf86b82e6de7a0103534bf1deff140f5da273cb67412fd6e0a2c5838590afa — 1760 lines / 194329 bytes
authoring_time_utc: 2026-09-22T08:05:00Z (approximate start; storage commit time recorded by git)
```

## 1. Decision requested

RS-20 is asked to classify `HDE-EPIC040-PR04-F02` and, if it is a real bounded delta, to approve the smallest Specification-compatible overlay in §5: for HDE-EPIC040-PR04 only, permit one existing-row rebind of `adapter/http_reader.py` in `catalog/manifest.json` through the canonical manifest writer, with the roster held at fifteen and release identity recomputed from the actual bytes, plus the owner-generated evidence convergence that follows — the same remedy class PF10 §2.10 approved for HDE-EPIC040-PR02 and `engine/serializer/canon.py`.

This proposal approves nothing, authorizes no implementation, creates no addendum, requests no Proceed, and does not alter the approved F01 overlay (PF10 §2.15). It ends `ASK OK?`.

## 2. Controlling authority and exact source package

| Role | Exact artifact |
| --- | --- |
| Approved Specification | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`; `HDE-EPIC040-SPECIFICATION` v1.1; Thoth-17 `APPROVE`; SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| Immutable whole-change Plan | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`; §6.4 (PR04), §6.6 (PR06 owns complete admission and convergence), §7.2 (Freeze-Pack Manifest writer `scripts/cut_release_manifest.py`; "full promoted admission only PR06") |
| Approving Plan review | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md`; Isis-50 `APPROVE`; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Whole-change Audit | `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md`; SHA-256 `9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b` |
| PR04 instruction | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md`; `INSTRUCTION_READY`; SHA-256 `8769d12f8e4df82eed9f4869e4a48ca53ae8a99d7a6b6497df526036f30ffdcf`; §6.5 requires the Reader `POST` success path in `adapter/http_reader.py`; §7.1 lists it as an owned locus; §9 excludes "release promotion, manifest expansion or activation" |
| PR04 detailed plan | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.1.md` (`AWAITING_PO_PROCEED`, this session, same storage PR) and predecessor `…-v1.0.md` (`DRAFT`, SHA-256 `40e1b904b0817c42609d6f6abecf1c53a382e2da1face7720caa9b05f126ee65`); plan §6.6 lists `catalog/**` including `catalog/manifest.json` as explicitly unchanged |
| F01 decision and overlay | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` (`APPROVE`, Isis-50, `2026-09-22T07:27:55Z`; §5 records this candidate finding); `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md`; drained as PF10 §2.15 |
| Current controlled PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`; SHA-256 `abcf86b82e6de7a0103534bf1deff140f5da273cb67412fd6e0a2c5838590afa`; applicable overlays §§2.2–2.13 and §2.15 per plan v1.1 §2.3; **§2.10** (PR02-F03) is the load-bearing precedent and is scoped "For HDE-EPIC040-PR02 only", reserving complete member refresh and final identity recomputation to PR06 (its item 8) |
| Accepted dependencies | PR01 lineage review v1.1 (`ACCEPT`), PR02 lineage review v1.0 (`ACCEPT`), PR03 lineage review v1.0 (`ACCEPTED_FINAL`; landed `9cda1b49a972da874021e8820997fab1ebaff153`) |

Every PF source was resolved only from `docs/pfcanon/` (read-only). Google Drive was not consulted and is not an authority.

## 3. Evidence-supported boundary

### 3.1 The collision

1. `catalog/manifest.json` (`root: catalog/`, `version: 1.0.0`, `built_at_utc: 2025-12-26T00:00:00Z`, fifteen `files` entries) contains as its first entry `{"path": "adapter/http_reader.py", "sha256": "9f0cde20055e7a94db50fb506bace9ddc51b3f9184fc1192a498c5b2fd243592", "size": 35655}`. The other members are `catalog/channels_v1.json`, `catalog/gates_v1.json`, `catalog/magic10.json`, `catalog/magic10_caps.json`, `catalog/magic10_seeds.json`, the five `catalog/narratives/*.json`, `engine/presenter/emitter.py`, `engine/serializer/canon.py`, `math/thresholds.json`, `migrations/005_identity.sql`.
2. `tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes` iterates every committed entry and asserts `entry["sha256"] == sha256(repository bytes)` and `entry["size"] == len(repository bytes)`. It runs in the release lane (`.github/workflows/ci.yml`, step "Build and verify exact-source release attestation", pytest list) inside the detached worktree at the candidate head. The release lane is selected for every product-prefix change (`ci/checks/classify_ci_changes.py::_lanes_for_path`), and a PR04 candidate selects all seven lanes.
3. Instruction §6.5 and Plan §6.4 require PR04 to change `adapter/http_reader.py` (Reader `POST` success path at the existing declared route, GET fixture route, dev conjunction routes, error mapping). Any byte change makes the committed row stale and the test fails — the RS-20 reviewer observed exactly this under a PR04-shaped change at `0f47079f…` (review v2.0 §4.1, "2 failed, 50 passed": this test and `tests/runtime/test_identity.py`).
4. PR04 may not refresh the manifest: instruction §9 excludes manifest expansion or activation; plan §6.6 lists `catalog/manifest.json` as unchanged; Plan §7.2 reserves full promoted admission to PR06.

### 3.2 Why it is not F01

F01 concerns gates that cannot express a truthful non-admitted outcome; its overlay keys on the admission state of the active release. This failure is a byte-binding mismatch that would occur with a fully admitted release too. Review v2.0 §5 and PF10 §2.15 both record it as outside F01 by the F01 proposal's own definition. The F01 overlay is complete on its own terms and is not reopened here.

### 3.3 Scope of the collision

Exactly one PR04 locus is a committed manifest member. `engine/presenter/emitter.py` (a member) is not changed by PR04; PR04's Reader emitter locus is `presenter/reader_v1/emitter.py`, which is not a committed member (it is a member of the 44-member `ADMITTED_RELEASE_ROSTER` that PR06 materializes). `engine/serializer/canon.py`, the catalog data files, `math/thresholds.json` and `migrations/005_identity.sql` are outside PR04's loci.

### 3.4 What the canonical writers do today (read-only inspection)

- `scripts/cut_release_manifest.py::cut_manifest(manifest_path, *, version, built_at_utc, check)` requires closed rails, validates the top-level key set `{root, version, built_at_utc, files}` and canonical bytes, sets `version` and `built_at_utc` from its arguments, recomputes `sha256`/`size` for **every** existing entry from repository bytes, sorts entries by path, and writes canonical bytes (or, with `--check`, returns 1 on any difference). It adds no member. Passing the current values `--version 1.0.0 --built-at-utc 2025-12-26T00:00:00Z` preserves both fields; with PR04's changes only the `adapter/http_reader.py` row's `sha256`/`size` change.
- `scripts/release_id_recompute.py --check-manifest-only` is the read-only validation posture (AGENTS.md release identity rules); `release_id = sha256(canonical_bytes(catalog/manifest.json))` and necessarily changes with any manifest byte change.
- `tools/evidence/run_canonical_json_gate.py` lists `catalog/manifest.json` among its targets and validates it through `scripts.cut_release_manifest.cut_manifest(check=True)`; its outputs under `audit/gates/canonical_json/` and `audit/gates/json_gate/canonical/` record manifest-derived values.
- Precedent evidence set: the PR02-F03 rebind landed in squash commit `5b2fb8d70924a6710b6261fc0c93d3869fed6380` (#404) changing `catalog/manifest.json` (2 lines), `audit/gates/canonical_json/json_canon_compare.log`, `audit/gates/canonical_json/json_canonical_check.log`, `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, their `.path_proof.txt` companions, and `artifacts/evidence_index.jsonl` with its `.sha256` and path proofs — all through owners. No tracked `release_id` derivative was hand-edited; release-bound derivatives are produced only inside the isolated attestation copy (`build_release_attestation.py` regenerates and cross-checks `artifacts/math/release_id.txt` there).

## 4. Classification

**A real bounded implementation delta, not an ordinary in-scope correction and not a Specification change.**

- Unchanged authority cannot address it: PR04's approved behavior requires changing a committed manifest member, and PR04's approved scope forbids touching the manifest. Both are binding on the same candidate; no implementation choice inside §7.1 loci reconciles them. Skipping or weakening the binding test is prohibited (AGENTS.md; F01 binding-condition posture). Leaving `adapter/http_reader.py` unchanged violates instruction §6.5. Deferring to PR06 leaves the release lane red for PR04 and PR05 and contradicts PR04's completion condition.
- Not a Specification change: no requirement text, exclusion, product objective, public contract, identity formula, taxonomy or work-unit order moves. The Specification already defines `release_id` as manifest-derived and distinct from source identity (`K040-REQ-009`, `AC040-05`); a truthful rebind keeps that contract.
- Not a defect in PR01–PR03: the manifest binding was correct for the bytes those units landed; PR02-F03 resolved the same class for its own member.
- Precedent: PF10 §2.10 (PR02-F03) — same class, same remedy shape, scoped to PR02 alone; this proposal asks for the same bounded permission scoped to PR04 alone.

## 5. Smallest complete bounded delta (proposed overlay text, for RS-20)

For HDE-EPIC040-PR04 only, apply all of the following together:

1. **One existing-row rebind.** Rebind only the existing `adapter/http_reader.py` row of `catalog/manifest.json` to the exact final, locally validated, substantively reviewed PR04 bytes, using the existing canonical manifest writer `python scripts/cut_release_manifest.py --version 1.0.0 --built-at-utc 2025-12-26T00:00:00Z` under closed rails. Change only that row's `sha256` and `size`. Preserve the other fourteen rows, their ordering, `root`, `version` and `built_at_utc`. Add no member.
2. **Identity recomputed, never described as unchanged.** `release_id = sha256(exact final manifest bytes)` changes with the row; validate with `python scripts/release_id_recompute.py --check-manifest-only`; record the final manifest SHA-256 and `release_id` in the PR04 result from the exact final reviewed bytes. Candidate identities computed at interim heads are reproduction evidence only.
3. **Re-cut on every byte change.** Each corrective push under PR-35 that changes `adapter/http_reader.py` re-runs the canonical writer so the binding test holds at every pushed head; the final cut is taken from the exact final reviewed bytes.
4. **Owner-generated evidence convergence only.** Regenerate only the canonical-JSON gate outputs actually affected (`tools/evidence/run_canonical_json_gate.py`: `audit/gates/canonical_json/json_canonical_check.log`, `json_canon_compare.log`, `canonical_json.gate.json`, `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `json_gate_compare_log.ndjson`, `json_gate_structured_record.json`, where their bytes change) and their `.path_proof.txt` companions, then the sole updater `python tools/evidence/update_evidence_index.py` for Index/Mirror/checksum/orientation convergence. No hand edit; no historical recapture; no new evidence family; no refresh of unrelated families.
5. **Loci effect.** PR04's owned loci extend by exactly `catalog/manifest.json` (one row) plus the owner-generated outputs in item 4. Plan v1.1 §6.6's "unchanged" entry for `catalog/manifest.json` is superseded only to that extent. Classifier: `catalog/manifest.json` is already a registered `_PRODUCT_TEST_OWNER_PATHS` entry and a `_RELEASE_IDENTITY_INPUT_PATHS` member; no classifier change is needed for this delta.
6. **Preserved checks.** `tests/evidence/test_release_manifest_content_binding.py` is unchanged and must pass; `scripts/release_id_recompute.py --check-manifest-only`, the canonical-JSON gate, the attestation's `release_identity_mismatch` check and every ownership/clean-tree check stay in force. No waiver, ignored row, xfail, narrowed assertion, fake hash or duplicate manifest.
7. **PR06 boundary preserved.** PR06 retains complete 44-member materialization, all-member refresh, final identity recomputation/convergence and promotion. Nothing here admits, activates or promotes a release; the actual release remains the incomplete 15-member manifest until PR06.

The delta is Specification-compatible: `K040-REQ-007` (admission stays bound to the actual manifest), `K040-REQ-008` (stale binding still fails closed), `K040-REQ-009` (identities recomputed from actual bytes, source/config/manifest/release identities distinct), `K040-REQ-011`/`K040-REQ-012` (owners regenerate only affected outputs), `AC040-04`/`AC040-05` (coherent bound candidate; PR06 retains promotion proof) — the same effect table PF10 §2.10 records for PR02, now for PR04.

## 6. Effects

| Dimension | Effect |
| --- | --- |
| Requirements / acceptance | None rewritten; see §5 effect list. PR04 completion condition (plan §4.2 item 4) becomes satisfiable together with the F01 overlay. |
| Work units | PR04 gains the one-row rebind; PR05 (which changes no manifest member — its loci are golden comparison and readiness) is unaffected unless it touches a member, which its Plan §6.5 loci do not; PR06 unchanged in ownership; PR07/OPS01 unchanged. Dependency order unchanged. |
| Tests | No test changes; the binding test is the acceptance check. PR04 result records the final manifest SHA-256 and `release_id`. |
| Ops / documentation | None. |
| Evidence | Items 4 of §5 through owners; frozen historical release evidence (EPIC022 captures) stays frozen with nonclaims. |
| Recovery | Rollback restores `adapter/http_reader.py` and the manifest row together (one coherent slice); a stale row is refused by the binding test and the canonical gate, never edited into equality. |
| Risk | Repeated re-cuts under PR-35 cost one writer run per corrective push; forgetting one turns the release lane red truthfully (the test catches it). |

## 7. Alternatives considered

| Alternative | Disposition proposed |
| --- | --- |
| One existing-row rebind through the canonical writer (this proposal) | Recommended: smallest complete correction; identical class and shape to PF10 §2.10; preserves roster size, writer ownership, strict checks and PR06 boundaries. |
| Defer the stale row to PR06 | Rejected: PR04 (and PR05 after it) cannot reach a green release lane; an internally inconsistent bound member would sit on `main`. |
| Do not change `adapter/http_reader.py` in PR04 | Rejected: instruction §6.5 requires the Reader `POST` success path there; moving it elsewhere would create a new route/home, which §9 excludes. |
| Waive, skip or narrow the binding test | Prohibited (AGENTS.md; Specification `K040-REQ-008`). |
| Add PR04's other loci to the manifest early / materialize 44 members | Rejected: manifest expansion is excluded; PR06-owned. |
| Product Owner CI waiver | Unnecessary if the bounded delta is approved; recorded as the fallback only if RS-20 rejects. |

## 8. Authority classification

Bounded implementation rescope decidable by RS-20 (the same whole-change IA reviewer that decided F01) with exactly one PF10 addendum overlay if approved. No PF12 wire value, schema or canon decision is involved (`release_id` derivation is unchanged; the manifest schema is unchanged). No Product Owner decision is required unless RS-20 rejects. RS-10 has no approval authority and this proposal is evidence for RS-20, not an addendum.

## 9. Carried `CANON_CONFLICT_REGISTER`

`C040-01` through `C040-06` are carried unchanged from Plan v2.1 §11.1, instruction §13, plan v1.1 §13.1 and review v2.0 §8 (classification, decision lineage, carried effects and remaining owners identical). Neither `HDE-EPIC040-PR04-F01` (approved overlay, PF10 §2.15) nor `HDE-EPIC040-PR04-F02` (this candidate) is a register entry. No entry is reopened, relabeled, omitted or newly decided.

## 10. Unresolved facts and owners

| Item | Owner | State |
| --- | --- | --- |
| This finding (F02) | RS-20 in the continuing whole-change IA session | `RESCOPE_PROPOSAL_PENDING_REVIEW` |
| Plan decision D-03 (valid self-pair carrier) | Session `PR04-HDE-EPIC040-1` | Carried, not raised |
| PF12 v2.9.5 vs register v2.9.6; C040-05/C040-06 permanent drainage; repository prompt-provenance persistence | Governed maintainers / authorized writer | Carried, non-gating |
| Sequencing of Nathan's PR-30 Proceed relative to this decision | Nathan / Product Owner | Plan v1.1 §9 preconditions and §17 record both orders |

## 11. Prompt-use provenance

`GCFPE_PROMPT_USE`:

- `usage_id`: `GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F02-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`; `work_unit_id` / `finding_ref`: `HDE-EPIC040-PR04` / `HDE-EPIC040-PR04-F02`; `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1
- `prompt`: `RS-10 — Create Bounded Work-Unit Rescope Proposal — 091426.1`, page `https://app.notion.com/p/3db4590a05eb811ca0cdc66e0d508ac4?pvs=204`, retrieved revision `2026-09-21T22:57:33.281Z`; ecosystem `GCFPE-20260914.1` / `091426.1` / 55
- `role_stage`: dedicated PR04 session `PR04-HDE-EPIC040-1` as explicitly assigned finding author / RS-10; `execution_posture`: `MANUAL_PROMPT_EXECUTION`; `session_disposition`: `RETAIN_EXISTING`
- `capture_time`: `2026-09-22T08:05:00Z` (approximate authoring start; storage commit time recorded by git)
- `result`: this `HDE-EPIC040-PR04-F02-RESCOPE-PROPOSAL v1.0`, `RESCOPE_PROPOSAL_PENDING_REVIEW`
- preserved earlier entries by exact reference: `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-02` (plan v1.1 §16), `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-02` (review v2.0 §11), `GCFPE-USE-HDE-EPIC040-RS-30-20260922-PR04-F01-01`, `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-01`, `GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01`, `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01`, `GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01`
- `repository_provenance`: `PENDING / NON_GATING` (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure)

## 12. Evidence index

| Evidence | Where |
| --- | --- |
| Manifest row and membership | `catalog/manifest.json` at `3b8084d0…` (`adapter/http_reader.py`: `9f0cde20055e7a94db50fb506bace9ddc51b3f9184fc1192a498c5b2fd243592`, 35655) |
| Binding test | `tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes` |
| Release-lane selection | `.github/workflows/ci.yml` release step pytest list; `ci/checks/classify_ci_changes.py::_lanes_for_path` (product prefix → `release`) |
| Observed failure under a PR04-shaped change | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` §4.1 and §5 (RS-20 execution at `0f47079f…`) |
| Canonical writer behavior | `scripts/cut_release_manifest.py::cut_manifest`; `scripts/release_id_recompute.py --check-manifest-only` |
| Precedent overlay and evidence set | PF10 §2.10; commit `5b2fb8d70924a6710b6261fc0c93d3869fed6380` (#404) file list |
| Requirement/exclusion texts | Instruction §§6.5, 7.1, 9; Plan v2.1 §§6.4, 6.6, 7.2; plan v1.1 §§4.3, 6.6, 14.3 |

## 13. Checkpoint

`RS-10 / HDE-EPIC040-PR04-F02`: proposal v1.0 authored and stored with plan v1.1 in one storage PR on branch `claude/peaceful-gauss-jhyezn` (restarted from `main` `3b8084d0…`); read back; no PF10 edit, no addendum, no Proceed, no product change; next: RS-20 in the continuing whole-change IA session; return point on any outcome: session `PR04-HDE-EPIC040-1` (plan v1.2 on `APPROVE`; PR-30 resumes directly if a Proceed already exists and the candidate is prepublication).

## 14. Handoff to RS-20 (complete native package)

```text
NEXT_PROMPT_HANDOFF
Run RS-20 — Review Bounded Work-Unit Rescope — 091426.1
https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204

=== RECEIVING ROLE AND SESSION ===
Actor: the continuing independent Lead Developer reviewer Isis-50 in the retained whole-change HDE-EPIC040 IA session — the same session that decided HDE-EPIC040-PR04-F01 (REVISION_REQUIRED 2026-09-22T06:48:06Z; APPROVE 2026-09-22T07:27:55Z). session_disposition: RETAIN_EXISTING; the operator selects it. Proposal author: dedicated PR04 session PR04-HDE-EPIC040-1 (retained, not replaced). invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR04 / RS-20 (GCF-17.RESCOPE), first decision on F02. context_conflict: NONE. EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION. AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS.

=== PROPOSAL UNDER REVIEW ===
RESCOPE_PROPOSAL_ID: HDE-EPIC040-PR04-F02-RESCOPE-PROPOSAL v1.0, RESCOPE_PROPOSAL_PENDING_REVIEW — docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md (amthorn78/glow-hdengine-v2; SHA-256 and storage PR recorded in the PR-20 return that carries this handoff). Finding: HDE-EPIC040-PR04-F02 — manifest content binding refresh for adapter/http_reader.py; recorded as a candidate by review v2.0 §5 and PF10 §2.15. Prior proposal/review for F02: NONE. Requested decision: §1; proposed overlay text: §5; classification: §4; alternatives: §7; authority: §8.

=== LINEAGE ===
CHANGE_CLASS EPIC; CHANGE_ID HDE-EPIC040; WORK_UNIT_ID HDE-EPIC040-PR04. PR_INSTRUCTION_ID HDE-EPIC040-PR04-PR-INSTRUCTION v1.0 (docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md, 8769d12f8e4df82eed9f4869e4a48ca53ae8a99d7a6b6497df526036f30ffdcf). SPECIFICATION_ID HDE-EPIC040-SPECIFICATION v1.1 (43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df). IMPLEMENTATION_AUDIT v2.0 (9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b). IMPLEMENTATION_PLAN v2.1 (10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be). PLAN_REVIEW v2.1 (47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3). PR04 plan v1.1 AWAITING_PO_PROCEED (docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.1.md) and v1.0 DRAFT preserved. F01: review v2.0 APPROVE and overlay drained as PF10 §2.15. Accepted-final PR01–PR03 unchanged.

=== PF10 AND OVERLAYS ===
Resolve and completely read docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md yourself (at proposal time sha256 abcf86b82e6de7a0103534bf1deff140f5da273cb67412fd6e0a2c5838590afa, 1760 lines / 194329 bytes; §2.15 present; index lists 2.14 and 2.15) and every applicable addendum by repository path (plan v1.1 §2.3). §2.10 is the load-bearing precedent, scoped to PR02 only. docs/pfcanon/ is read-only; Google Drive is not a source. RS-20 alone may create exactly one PF10 addendum overlay on APPROVE, page-ready under §2.8 with its number unallocated; RS-20 never edits PF10 or allocates numbering.

=== BASELINE AND SUSPENDED BOUNDARY ===
main 3b8084d09e974f15c2b71112e5a596af01b1a371 (tree 11e81c99b9194c38471b494c59b149d4f4553659); executable baseline 9cda1b49a972da874021e8820997fab1ebaff153; no PR04 product vehicle, Proceed, CI or merge exists; re-verify yourself. Boundary: adapter/http_reader.py is both a required PR04 locus (instruction §6.5) and the first committed member of catalog/manifest.json (sha256 9f0cde20055e7a94db50fb506bace9ddc51b3f9184fc1192a498c5b2fd243592, size 35655); tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes (release lane) fails on any PR04 candidate, independent of admission; PR04 may not refresh the manifest (instruction §9; plan §6.6; Plan §7.2 reserves promoted admission to PR06). Observed by RS-20 itself at 0f47079f (review v2.0 §4.1, §5).

=== COMPLETED WORK, EFFECTS AND UNRESOLVED ===
Preserved: plan v1.1 §§5–12 and F01 overlay; only plan §4.2 condition 4 and §6.6's catalog/manifest.json entry depend on this decision. Effects: §6 of the proposal. Unresolved: §10. CANON_CONFLICT_REGISTER C040-01..06 carried unchanged; F01/F02 are not register entries.

=== CONSTRAINTS ===
Do not implement, create a product branch or PR, request or fabricate a Proceed, edit PF10, allocate a PF10 number, rewrite the immutable Plan, restart IA-30/IA-40, rerun accepted PR01–PR03, merge, or invoke PR-50 (Nathan-only). Write the review, one addendum overlay on APPROVE, checkpoint and handoff under docs/ephemeral/, commit and push on a working branch, read back completely, open one PR; Nathan alone merges.

=== EXPECTED OUTPUT ===
One RESCOPE_REVIEW: APPROVE (exactly one PF10 addendum overlay; return to PR-20 in session PR04-HDE-EPIC040-1, which issues plan v1.2 in AWAITING_PO_PROCEED — or, if Nathan's Proceed already exists and PR-30 is prepublication, PR-30 resumes directly reading current PF10), REVISION_REQUIRED (exact redlines to RS-30, same author), REJECT (decision and evidence back to session PR04-HDE-EPIC040-1), or SPECIFICATION_CHANGE_REQUIRED (to Nathan and the Specification owners). No implementation authority, Proceed, merge permission, PF09 movement, QA verdict or closure is created.
```

ASK OK?
