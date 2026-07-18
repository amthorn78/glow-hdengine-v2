# Rescoping CRD - HDE-EPIC038 - POST-PR359-REMEDIATION

## 1. Document Control

| Field | Value |
| --- | --- |
| CRD ID | `CRD-HDE-EPIC038-POST-PR359-REMEDIATION` |
| Version | `v1.3` |
| Supersedes | `CRD-HDE-EPIC038-POST-PR359-REMEDIATION` `v1.2` |
| Epic | `HDE-EPIC038`, Distillation Pass 3 |
| Slice | `POST-PR359-REMEDIATION` |
| Preceding PR | [PR 359](https://github.com/amthorn78/glow-hdengine-v2/pull/359), `HDE-EPIC038 PR-06: orchestrate fail-closed release sanity pipeline and bind OPS evidence` |
| Author role | Sekhmet |
| PO authorization | `APPROVED` for bounded rescoping and CRD creation |
| IA review status | `READY FOR IA RE-REVIEW` |
| Creation date | `2026-07-18` |
| Revised date | `2026-07-18` |
| ADR inventory | `ADR-CANON-004` - `PROPOSED - PENDING IA TECHNICAL APPROVAL` - canon effect `AMENDS` |
| Repository | `amthorn78/glow-hdengine-v2` |
| Product repository root | `/workspaces/glow-hdengine-v2` in the authorized OPS environment |
| Local diagnostic checkout | `/workspace/scratch/c481b522cc4c/glow-hdengine-v2` |
| Local checkout branch/head | `codex/implement-pr-04-for-hde-epic038@87206b284bb53b651e9b8dee015127401abd6bf7`; not detached; unrelated to the merged-state target |
| Local worktree before/after | Pre-existing dirty state was unchanged; `git status --porcelain=v1` had 59 entries before and after, with final output SHA-256 `aa80a920df693e3f64e6acea9c85d9bac97eef269929ae79a0c2f0642c7fceea` |
| Reviewed merged baseline | `main@78756e776f7fa598370235de6a72aa29fe045af9` |
| PR head incorporated by the merge | `codex/implement-pr-06-for-hde-epic038@c6e689edefdac1f832faed6ad19f504eefbda696` |
| Branch posture | PR head merged and PR closed; the CRD targets a new post-merge remediation slice, not PR 359 |
| Confirmed rescope IDs | `BUG-001`, `BUG-002`, `BUG-003` |
| Unverified historical-report IDs | `BLK-001`, `ACT-002`; retained only as non-operative provenance with every unsupported field marked `UNVERIFIED` |
| Superseded finding IDs retained for regression | `STALE-001`, `STALE-002` |
| PF-Canon baseline | `PF07-Canon-Glow-Infrastructure v2.2.4`; `PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2`; `PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8`; `PF14-Canon-HDE-Mechanics-Guide v3.4.3`; `PF27-Canon-Plan-Templates v1.9.5` |
| PF-Canon source | Complete current session-provided canonical documents, checked against the merged repository topic loci used by PR 359 |
| Current PF10 | `PF10-HDE-Build-Notes v12.2.7` |
| Planning posture | `r1 Epic Plan HDE-EPIC038.md` remains the approved epic-scope baseline; `r6 Implementation Plan HDE-EPIC038.md` is the current Implementation Plan lineage and must receive a separately authorized next-version revision before implementation relies on this CRD |

### Source units used

- Baseline `CRD-HDE-EPIC038-POST-PR359-REMEDIATION v1.2` and IA review v1.2 are the complete revision contract for this version.
- The earlier Current Debugging Context is provenance only and is not required to review or execute this CRD. Its failed-run assertions are represented in the self-contained claim-disposition record in §4 and are not treated as confirmed evidence.
- GitHub PR metadata for PR 359 and the exact merged files at merge commit `78756e776f7fa598370235de6a72aa29fe045af9`.
- `tools/evidence/run_sanity_pipeline.py`, including `SAFE_ENV_REFERENCE`, `_validate_secret_safety`, `_normalize_ddl_provider_value`, `_validate_bodygraph_selection_snapshot`, and the OPS-01 schema and corpus constants.
- `scripts/db/capture_epic011_posture.py`, including `_ddl_projection` and `_parity_match`.
- `tools/qa/run_hde_epic024_harness.py`, including `_write_token_matrix`, `_write_acceptance_map`, and `_check_specs`.
- `docs/acceptance_map_epic024.json` and `audit/qa/hde-epic024/token_evidence_matrix.md`.
- `audit/ops/hde-epic038/ops-01/commands.txt`, `provider_parity.proof.json`, `result_summary.json`, and `env_presence.json`.
- `tools/evidence/update_evidence_index.py`, including `EPIC038_PR06_PRIMARY_ARTIFACTS` and the current PR-06 artifact-key derivation.
- `tests/evidence/test_hde_epic038_release_sanity.py`.
- IA review v1.2 `REV-001`. No external Railway documentation is treated as proof of the installed CLI or target contract.
- Reviewer-directed current canon proof from `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.7.8.md` section 8.6.3.4 and `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.4.3.md` section 20.3 at merged `main@78756e776f7fa598370235de6a72aa29fe045af9`.
- The PF10, PF07, PF27, PF09.6, PF12, PF14, r1, r6, and failed-run search facts already grounded in v1.2 are preserved as baseline content and were not re-inspected for this revision because current `REV-001` required no PF or plan consultation.
- The only conditional current-Repo inspection for this revision was the reviewer-directed ignored-cache posture check recorded in the Conditional Source Record; no product source, plan, PF document, unrelated evidence, QA, or OPS surface was inspected or executed.

Evidence pointer: Repo | PR 359 metadata | "merged=true; merge_commit_sha=78756e776f7fa598370235de6a72aa29fe045af9; head_sha=c6e689edefdac1f832faed6ad19f504eefbda696."

Evidence pointer: Repo | `/workspace/scratch/c481b522cc4c/glow-hdengine-v2`, `git status --porcelain=v1`, `git branch --show-current`, `git rev-parse HEAD` before/after | "The unrelated PR-04 checkout remained on codex/implement-pr-04-for-hde-epic038@87206b284bb53b651e9b8dee015127401abd6bf7 with the same 59 pre-existing status entries; no product file was modified for this CRD."

This CRD is stored outside the product repository. No product, plan, PF-Canon, ADR, PF09, PF10, deployment, database, or external service state was changed during its creation.

## 2. Executive Summary

PR 359 is merged. The post-merge review established four distinct conditions:

1. The EPIC024 generator now emits the canonical sanity path, but two checked-in historical outputs still retain the old path. This is a live generated-output coherence bug.
2. The retained-evidence scanner detects raw-payload markers only when written as double-quoted JSON keys followed by a colon. This is a live evidence-admission security bug.
3. The OPS-01 DDL comparison is duplicated in two functions, is not versioned, compares only object identity and column name/type, and is labeled merely `match`. This is a bounded Glow evidence-architecture conflict because the label can be read as full DDL semantic parity even though nullability, defaults, constraints, and view definitions are not compared.
4. An earlier external report alleged that a temporary OPS recapture runner encountered `ModuleNotFoundError`, but the exact traceback, runner and candidate-ledger provenance, call counters, provider-construction boundary, and no-I/O methods are unavailable from the permitted sources. `BLK-001` and `ACT-002` are therefore `UNVERIFIED` and non-operative. The mandatory runner qualification below is justified prospectively by the one-attempt safety boundary: an immutable runner must prove source imports, component identity, exact `-I -B` Python execution, no Python environment override, no detached-source mutation or bytecode-cache residue, a closed per-mode write set, and zero-I/O orchestration before any bounded external discovery or live launch.

The selected architecture uses two narrow PRs separated by one operational lane:

- PR-A is a closed-rails remediation PR. It lands the two independently releasable P1/P2 repairs, the shared DDL projector, and a tracked, testable OPS-01R runner. It leaves the committed OPS packet and default release-sanity admission at v4. No live execution occurs in PR-A.
- OPS-01R is one separately authorized, one-attempt, Glow-only recapture from an immutable detached source worktree at the exact PR-A merge commit. Before live authorization, `hde_epic038.ops01r.preflight.v1` proves deterministic zero-I/O execution under the exact ordered Python prefix `-I -B`, an empty `PYTHON*` child environment, byte-identical full-source manifests, no `__pycache__` or `.pyc` residue, and an authenticated pre-staging baseline/post delta limited to the exact mode-owned control path. A separately PO-authorized `hde_epic038.ops01r.discovery_authorization.v1` plus `hde_epic038.ops01r.discovery_policy.v1` constrain at most six non-mutating Railway discovery stages and bind the same exact target-probe and supporting-entry-point isolation contract. The tracked launcher consumes only independently validated preflight and discovery identities; a separately invoked independent live-authorization validator must then pass before marker, Railway, credential, or provider activity. The live authorization binds the same isolation contract and an independently captured live pre-staging baseline to the validator, launcher, live child, and capture-time validator, requires exact equality to the authorization-owned call vector, and stages a v5 candidate only. Capture-time admission recomputes the actual temporary source/staging trees while they exist; later PR-C and release validation check only retained canonical proof and externally reviewed identities and do not claim to recapture those temporary trees. OPS-01R does not write tracked files or change Railway, PostgreSQL, or `pg-bridge`.
- PR-C is a separate closed-rails integration PR. It integrates the reviewed candidate atomically, switches default release-sanity admission to v5, regenerates updater-owned companions, and leaves a v5-only final state. It contains no OPS rerun.

The minimum rescope is therefore:

- selectively regenerate exactly the two stale EPIC024 acceptance-binding primaries and their updater-owned companions without rerunning historical QA;
- harden the raw-payload marker scanner while preserving the already-correct shell-default credential and provider-selection provenance controls;
- extract one strict, versioned Glow-owned DDL identity projector and update the OPS-01 proof contract so a projection match cannot claim full DDL semantic parity;
- require an offline, zero-I/O import and full-flow preflight under exact `-I -B` execution, with independent source-manifest, cache-residue, environment, authenticated pre-staging/delta, and per-mode write-set validation; carry that identical isolation contract through the Railway target probe, bounded supporting entry points, launcher, and live child; then perform separately authorized bounded Railway contract discovery before a new live OPS authorization is requested;
- require the live result to equal the complete preflight-derived call vector field by field, with any unexplained extra call rejected before delegation;
- execute at most one newly authorized OPS-01R attempt and stage, review, then integrate the candidate through a separate PR-C and the canonical updater.

Deferral is unsafe because the merged release-sanity validator can currently admit checksum-consistent retained evidence containing raw payload in non-JSON forms, checked-in EPIC024 outputs disagree with their generator, and the DDL result is semantically overbroad. A one-attempt live lane without independently valid source/import/write-isolation, preflight-record, discovery-policy, and exact-call identities could consume authority or mutate ignored source residue before producing admissible evidence even though the earlier external failed-run occurrence remains unverified.

The DDL contract decision has canon effect `AMENDS` and is fully specified in `ADR-CANON-004`. All other requested work has `NO CANON CHANGE`: it repairs implementation and evidence to the existing canonical path, safety, and OPS boundaries.

This CRD and `ADR-CANON-004` do not themselves edit either plan. `r1` remains the approved epic-scope baseline. If IA technically approves this CRD, it becomes the authoritative input for a separately authorized next-version revision of the Current Implementation Plan in the `r6` lineage; implementation may not rely on `RSC-001` through `RSC-005` or `ADR-CANON-004` until that revision is approved, unless a newer explicit PO instruction changes the current PF10 posture. A separately authorized PF10 section 2.9 and permanent PF drainage remain non-gating documentation work. No PF09 status moves.

Preserved boundaries are explicit: no PR 359 reopening; no `pg-bridge` repository or service change; no SQL write, migration, grant, role, schema, deployment, restart, relink, vendor call, production write, raw BodyGraph persistence, QA rerun, token claim, PF09 movement, acceptance, closeout, or epic completion.

## 3. Authority and Decision Posture

### PO rescoping authority

The PO has approved bounded rescoping and directed Sekhmet to produce this CRD. That authority establishes that the post-merge defects and the proposed one-attempt operational lane may be scoped together. It does not establish technical correctness and does not authorize implementation or live execution.

### Sekhmet technical decisions

Sekhmet selects the exact architecture in this CRD: closed-rails PR-A, selective EPIC024 rendering, exact-marker scanner hardening, one shared DDL projector, a tracked OPS runner, the closed `hde_epic038.ops01r.preflight.v1` zero-I/O record, one exact `-I -B` Python import/write-isolation contract reused by preflight, target probe, launcher, live child, and their bounded source-loading validators/producers, authenticated per-mode staging baselines/deltas, the closed discovery-authorization and policy contracts, one exact-vector OPS-01R attempt, and separate atomic integration PR-C. IA is not asked to design any of those mechanisms.

### Pending IA review

IA must approve or return this CRD for revision based on technical accuracy, causal completeness, minimum scope, implementation feasibility, evidence-schema completeness, migration safety, and boundary preservation. Sekhmet does not self-approve the CRD.

### Plan posture

This CRD and `ADR-CANON-004` do not directly edit either plan. `r1 Epic Plan HDE-EPIC038.md` remains the approved epic-scope baseline. Upon IA technical approval, this CRD becomes the authoritative input for a separately authorized next-version revision of the Current Implementation Plan in the `r6 Implementation Plan HDE-EPIC038.md` lineage. Implementation may not rely on `RSC-001` through `RSC-005` or `ADR-CANON-004` until that plan revision is approved, unless a newer explicit PO instruction changes the current PF10 posture. PF10 living-context recording and permanent PF drainage remain separate and non-gating.

### Later authorities remain separate

- IA technical approval of this CRD is required before the plan-revision lane.
- A separately authorized next-version Current Implementation Plan revision must incorporate every approved consequence and be approved before implementation relies on this CRD.
- A separately authorized implementation action is then required before opening or changing PR-A or PR-C.
- A separate bounded discovery authorization is required after the tracked PR-A runner and independent validator pass offline preflight from an immutable detached source worktree, including exact `-I -B` producer/validator argv, empty `PYTHON*` child environment, full-source manifest equality, cache-residue absence, authenticated pre-staging delta, and exact write-set proof. Discovery does not authorize the live attempt. A new exact live OPS authorization is required only after the discovery authorization, static policy, and discovery output pass fail-closed validation and bind the target, CLI, every bounded source-loading argv, identity-field contract, source-manifest identity, authenticated live pre-staging identity/write contract, and preflight call vector. An independently invoked live-authorization validator must then PASS before marker, Railway, credential, or provider activity. This CRD makes no verified claim about whether any earlier external authority was consumed.
- Candidate integration requires review of the staged packet and an explicit implementation/integration action. OPS authorization does not authorize integration.
- Permanent PF-Canon and ADR drainage is later documentation work. CRD approval does not edit PF files.

### Prohibited completion claims

CRD approval is not implementation, QA PASS, OPS completion, evidence integration, PF09 movement, acceptance-token satisfaction, release readiness, deployment readiness, slice completion, PR closure, epic closeout, or approval to merge PR-A or PR-C.

Evidence pointer: PF10 - PF10-HDE-Build-Notes v12.2.7 | section 2.6 | "OPS-01 contributes evidence only; HDE-DIST001.4 and HDE-DIST001.9 remain Partial; QA, acceptance, PF09 movement, and closeout are not claimed."

Evidence pointer: Implementation Plan | r6 Implementation Plan HDE-EPIC038, OPS-01 and PR-06 ownership | "OPS-01 produces read-only evidence; PR-06 validates and binds it without rerunning OPS."

## 4. Debugging Flow Basis

### Complete finding and action disposition ledger

| ID | Submitted or derived condition | Classification | CRD disposition |
| --- | --- | --- | --- |
| `BUG-001` | EPIC024 generator emits `audit/gates/sanity_pipeline/sanity_pipeline.log`, while `docs/acceptance_map_epic024.json` and `audit/qa/hde-epic024/token_evidence_matrix.md` still bind `SANITY_PIPELINE_OK` to `artifacts/sanity/sanity.log`. | Confirmed retained-scope repair | Mandatory `RSC-001`; selectively regenerate only the two historical binding primaries, then updater-owned companions. |
| `BUG-002` | Raw-payload detection recognizes only double-quoted JSON keys followed by `:` and misses unquoted YAML, single-quoted, and assignment forms. | Confirmed rescoping premise | Mandatory `RSC-002`; exact marker recognition across `:` and `=` forms with a closed safe-scalar set. |
| `STALE-001` | Shell default expressions such as `${HD_API_KEY:-live-secret}` could be treated as safe credential references. | Stale or superseded | No new production fix. Merged `SAFE_ENV_REFERENCE.fullmatch` accepts only `$NAME` and `${NAME}`. Existing negative tests remain mandatory regression coverage under `RSC-002`. |
| `STALE-002` | BodyGraph direct/bridge labels could be literal rather than bound to retained provider-selection output. | Stale or superseded | No new architecture. Merged v4 evidence retains content, path, hash, attempts, selection order, flags, and distinct providers; mutation tests reject drift. The same controls must survive the v5 migration under `RSC-003`. |
| `BUG-003` | DDL parity is implemented twice, silently treats different rich provider structures as the same narrow projection, has no versioned comparison contract, and reports plain `match`. | Confirmed architectural conflict | Mandatory `RSC-003` and `ADR-CANON-004`; one strict shared projector and explicit projection-only evidence semantics. |
| `BLK-001` | An external report alleged that a temporary recapture runner encountered `ModuleNotFoundError` before provider construction. | `UNVERIFIED` historical report; non-operative | Retained only in the claim-disposition record below. `RSC-004` is justified prospectively by the approved one-attempt boundary and the need to qualify source/import and external-command contracts before execution. |
| `ACT-001` | PR 359 was manually merged to stop further scope growth. | Completed external action observed from GitHub | Freeze PR 359. All remediation moves to a new slice and new PR. |
| `ACT-002` | An external report alleged a candidate at `/tmp/hde-epic038-ops01-recapture.051XSWvs/candidate`, a verified ledger, and no tracked integration. | `UNVERIFIED` historical report; non-operative | The alleged candidate is not governed Repo evidence and is never an integration input. Any future candidate must be produced and admitted independently under `RSC-004` and `RSC-005`. |
| `ACT-003` | Earlier reasoning treated `pg-bridge` compatibility as though it could imply repository work. | Ruled-out scope | `pg-bridge` is a separate repository/service. No inspection, patch, deploy, service selection, or defect claim is in scope. |

### Confirmed RCA conclusions

1. `BUG-001` is generator/output sequencing drift. The writers already contain the canonical path, but the governed checked-in outputs were not regenerated. A full EPIC024 harness run is unsafe because it would rewrite historical QA, close-pack, viability, log, and status surfaces that are not being reopened.
2. `BUG-002` is an admission-pattern defect. Checksum consistency does not mitigate it because a malicious or accidental retained value can be added and the ledger refreshed. The validator must inspect semantic marker forms, not only strict JSON syntax.
3. `BUG-003` is not a database-schema defect. Direct introspection contains nullability, defaults, constraints, and view definitions; the bridge side exposes a reduced shape. The current comparison intentionally uses shared identity fields, but the implementation and evidence do not version or label that limitation clearly.
4. No failed-run RCA is confirmed from the permitted sources. The external report's exact traceback, import order, provider-construction boundary, and no-I/O methods are unavailable. The supportable engineering limitation is prospective: a one-attempt external runner needs a closed source/import/write-isolation qualification contract before any CLI or provider boundary. V1.2 defined the preflight record but invoked Python from a writable detached source with `-I` only, so it did not suppress bytecode/cache writes or prove the complete source and staging write invariants. This limitation does not establish a Railway, PostgreSQL, or `pg-bridge` defect.

### Relevant observed actions

- PR 359 was merged and closed at `78756e776f7fa598370235de6a72aa29fe045af9`; this is the confirmed scope-separation action.
- Current Repo searches return zero hits for the alleged failed runner hash, alleged candidate-ledger hash, staging suffix, and `ModuleNotFoundError`. Those results do not disprove an external run; they prove only that current Repo cannot verify it.
- The previously successful committed OPS runner uses `/workspaces/glow-hdengine-v2`, an absolute repository `.venv` Python, `cd` into the repository, `python -m` for package entry points, exact branch/head pins, a clean-worktree check, unique staging, and retained provider-selection snapshots.

Evidence pointer: Repo | `audit/ops/hde-epic038/ops-01/commands.txt` | "REPO=/workspaces/glow-hdengine-v2; PYTHON=/workspaces/glow-hdengine-v2/.venv/bin/python; cd \"$REPO\"; exact branch, head, runner hash, and clean-worktree checks precede capture."

#### Minimal failed-run evidence record and verification disposition

This record is the complete retained treatment of the earlier external report. `UNVERIFIED` means the value is a provenance claim, not an observed fact, causal proof, authorization input, acceptance predicate, or implementation dependency.

| Required element | Reported value | Provenance available in this CRD | Verification method and result | Status | Operative consequence |
| --- | --- | --- | --- | --- | --- |
| Sanitized traceback/import excerpt | Only the term `ModuleNotFoundError` and the paraphrase "before provider construction" were reported; no exact traceback excerpt is available. | Baseline v1.1 claim, preserved only for provenance. | Case-sensitive GitHub code search of current `amthorn78/glow-hdengine-v2` returned 0 hits for `ModuleNotFoundError`; no external log is available. | `UNVERIFIED` | None. `CAUSE-004` does not assert occurrence, traceback location, or provider boundary. |
| Executed runner identity and SHA-256 | Temporary runner; alleged SHA-256 `aca1f0e09810cc7a451c07bd6660015e3d071ac50d930116177e60aa8aa8f15f`. | Baseline v1.1 claim only; no bytes or path-to-bytes proof. | Exact case-sensitive current-Repo search returned 0 hits; hash cannot be recomputed. | `UNVERIFIED` | Never reused, trusted, or bound. Future execution uses the tracked PR-A runner and independently validated hashes. |
| Candidate ledger identity and SHA-256 | Alleged `checksums.sha256` beneath the candidate; alleged hash `4dff85b6e55571ca49fae25f06dd9a19c23234d0c46c5c4a37225380fc21b8d6`. | Baseline v1.1 claim only; ledger bytes unavailable. | Exact case-sensitive current-Repo search returned 0 hits; hash and entries cannot be recomputed. | `UNVERIFIED` | Not an integration input. `RSC-005` accepts only a new externally reviewed candidate-ledger identity. |
| Staging/candidate relationship | Alleged staging root `/tmp/hde-epic038-ops01-recapture.051XSWvs` and child `candidate`. | Baseline v1.1 claim only. | Case-sensitive current-Repo search for `051XSWvs` returned 0 hits; filesystem state is unavailable. | `UNVERIFIED` | No path or artifact is reused. The new path contract is defined independently in `RSC-004.A`. |
| Exact call-counter record | Alleged logical observations `0`, direct SQL statements `0`, bridge HTTP requests `0`, BodyGraph reads `0`, retries `0`, and fallbacks `0`; no complete counter object or instrumentation output is available. | Baseline v1.1 narrative only. | No counter artifact, schema, capture method, or independently recomputable bytes are available. | `UNVERIFIED` | No no-I/O or consumed-attempt claim. Future zero-I/O is proven only by the closed preflight record. |
| Method proving pre-provider failure | None available. | Baseline paraphrase only. | Traceback and instrumentation ordering unavailable. | `UNVERIFIED` | No provider-construction conclusion is retained as fact. |
| Method proving no DB, bridge, vendor, deployment, or tracked write | None available. | Baseline paraphrase only. | No complete command manifest, process trace, provider counters, deployment trace, or tracked-write comparison is available. | `UNVERIFIED` | No external-I/O or write conclusion is retained as fact. |

The four Repo searches above are negative claim-scoping evidence only. They do not prove that the external report was false or that a run did not occur. No mandatory mechanism in this CRD depends on the alleged hash, path, count, traceback, provider boundary, no-I/O conclusion, or attempt-consumption claim.

### Rejected alternatives

- Reopen or continue adding commits to PR 359: rejected because the PR is merged and the PO explicitly stopped its growth.
- Update the `pg-bridge` repository or service: rejected because the confirmed defects are Glow-owned and no permitted source establishes a bridge defect. The unverified external report supplies no bridge evidence.
- Rerun the full EPIC024 QA harness: rejected because it would reopen historical execution and rewrite unrelated governed outputs.
- Keep the raw scanner JSON-only: rejected because retained logs and command transcripts are not restricted to JSON.
- Claim full DDL semantic parity: rejected because the bridge observation lacks fields present in direct introspection.
- Remove the DDL row: rejected because the active plan and OPS evidence require a DDL posture comparison; the safe correction is to version and bound the claim.
- Duplicate the projection a third time in the new runner: rejected because it would deepen the architectural conflict.
- Reuse the alleged temporary runner or staging root: rejected because neither identity is verifiable or governed and neither can satisfy the closed source/preflight contracts.
- Allow permanent v4/v5 dual acceptance: rejected because ambiguous final evidence admission would prevent a decisive migration.
- Treat the v1.0 Railway UUIDs, `--no-local` flag, or six injected-variable names as settled: rejected because the permitted current sources do not establish them.
- Make the v1.0 journal, recovery, `/proc`, dependency-manifest, code-contract, output-cap, and multi-receipt systems mandatory: rejected because they lack independent causal necessity for this one-attempt remediation. They are removed; any reusable OPS platform is `Follow-up (out of scope)`.

### Residual concerns and unknowns

The external failed-run occurrence, traceback, hashes, counters, provider boundary, no-I/O result, and attempt-consumption state remain Unknown and are non-operative. Separately, the candidate Railway executable path, resolved path, and byte hash are `UNKNOWN PENDING PREFLIGHT`. Its version and supported explicit-target argv, nonlinked behavior, exact project/environment/service IDs, and injected target-identity fields are `UNKNOWN PENDING DISCOVERY`. These execution-blocking operational unknowns are resolved only by the closed records in `RSC-004.A` and `.B`; live authorization is forbidden until both validate. Future PR-A/PR-C identities, run ID, and candidate checksums are later derived identities, not architecture unknowns.

## 5. Current Contract and Observed Conflict

### Implemented contract

- PR 359 establishes `audit/gates/sanity_pipeline/sanity_pipeline.log` as the canonical sanity primary and validates committed OPS packages in `tools/evidence/run_sanity_pipeline.py`.
- The current secret-safety validator accepts only bare shell environment references for credential values but recognizes raw-payload keys only as double-quoted JSON followed by a colon.
- OPS-01 provider proof v4 binds five ordered rows: `grants`, `search_path`, `select_one`, `ddl_fingerprint`, and `bodygraph_payload_row`.
- BodyGraph direct and bridge rows retain selection snapshots with content, path, SHA-256, attempts, selection order, force flags, and provider identity.
- DDL equality is calculated by `scripts/db/capture_epic011_posture.py::_ddl_projection` and reinterpreted by `tools/evidence/run_sanity_pipeline.py::_normalize_ddl_provider_value`.
- The current DDL evidence retains the richer direct and reduced bridge values, but the row result is simply `parity: "match"`.

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py::_validate_secret_safety` | "raw_payload_key matches only a double-quoted governed key followed by a colon."

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py::SAFE_ENV_REFERENCE` and test suite | "Only `$NAME` and `${NAME}` full-match; shell default and command-substitution values are rejected."

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py::_validate_bodygraph_selection_snapshot` | "The validator recomputes snapshot canonical bytes and SHA-256, checks path, provider, attempts, order, and force flags."

Evidence pointer: Repo | `scripts/db/capture_epic011_posture.py::_ddl_projection` | "Provider parity compares only object kind/name and column name/type."

Evidence pointer: Repo | `audit/ops/hde-epic038/ops-01/provider_parity.proof.json` | "Direct DDL includes nullable/default/constraints/view definition, bridge DDL is reduced, and the retained row says parity=match."

### Current canonical contract

- PF12 makes the canonical sanity path, evidence index, mirror, checksums, and path proofs governed surfaces and requires the canonical updater to own their companions.
- PF14 requires secret-safe, scope-rationalized, row-level provider evidence and prohibits overclaiming beyond observed evidence.
- PF09.6 keeps `HDE-DIST001.4`, `HDE-DIST001.6`, and `HDE-DIST001.9` `Partial`, keeps `HDE-DIST001.11` `Optional`, and keeps `HDE-DIST005.2` `Partial`. OPS evidence remains contributory, not independently completion-conferring. `.4` governs DDL/read-only posture, `.6` governs one-button release-sanity and retained-evidence admission, `.9` governs direct/bridge parity and provenance, `.11` preserves mapped-cache/vendor safety posture, and `DIST005.2` governs global Human Index/Machine Mirror and updater discipline.
- PF07 identifies `glow-hdengine-v2` and `pg-bridge` as separate service/repository boundaries. The HD engine may observe the bridge endpoint, but this slice does not own bridge implementation.

### Current plan contract

- The r6 plan assigns OPS-01 read-only observation and PR-06 validation/binding without an OPS rerun.
- The plan maps `HDE-DIST001.4` and `HDE-DIST001.9` across PR-04, OPS-01, and PR-06. The current canonical release-sanity and updater surfaces also engage `HDE-DIST001.6` and `HDE-DIST005.2`; the retained safety repair preserves `HDE-DIST001.11` without changing its optional posture.
- The merged PR-06 is the original release-sanity integration owner. Post-merge defects require a new remediation owner, but the original outcomes and exclusions remain authoritative historical constraints.

### Exact conflicts

1. Canonical generator output and checked-in historical EPIC024 outputs disagree.
2. The validator's raw-payload safety intent is broader than its syntax recognition.
3. DDL projection behavior is duplicated, not versioned, not strict in the producer, and not described in the retained proof. A plain `match` is semantically wider than the data supports.
4. The one-attempt recapture architecture requires source/import/write qualification and exact external-command admission before authority can be consumed. V1.2 closed the preflight record, discovery-authorization/static-policy input, and expected-vector identity chain, but its Python invocations used `-I` without `-B` and its clean-worktree claims could not detect ignored `__pycache__` or `.pyc` residue. A newly authorized attempt is blocked until exact `-I -B` execution, source-manifest equality, cache-residue absence, and per-mode write-set validation are hash-bound across preflight, target probe, and live child, and bounded discovery replaces unknown Railway target, CLI, and injection facts.

### Dependency preventing isolated fixes

The issues cannot safely be reduced to a one-line regex or one-off OPS retry. EPIC024 primaries drive updater-owned index and proof companions. DDL projection changes both the producer and release-sanity consumer and requires new retained evidence bytes. New live bytes require a tracked producer bound to immutable PR-A source, zero-I/O full-flow preflight, exact `-I -B` import execution and source/write proof in all three Python modes, validated Railway discovery output, exact PO live authorization, exact expected/actual call equality, independent candidate validation, and PR-C integration without mixed v4/v5 default admission.

### Consequence of deferral

- A checksum-consistent retained packet can pass Stage 12 while containing raw request, response, or vendor data in a non-JSON marker form.
- Consumers of checked-in EPIC024 outputs continue to observe the retired sanity path.
- Operators and reviewers can misconstrue `match` as full DDL parity.
- A one-attempt OPS authorization can be consumed before evidence exists if source/import/write, CLI, policy, target, and call-vector identities are not independently closed and validated; ignored bytecode residue can also escape an ordinary clean-worktree assertion.
- Integrating partial source changes without matching evidence would create a validator/evidence version split.

### Selected resolution posture

Use a closed-rails PR-A for independent repairs and the reduced tracked runner, one exact `-I -B` and source/write-isolation contract across offline full-flow preflight, Railway target probe, and live child, one separately authorized bounded Railway discovery, one separately authorized exact-vector OPS-01R capture against the exact merged head, and a closed-rails PR-C for v5-only updater-coherent integration. No other repository or service enters scope.

## 6. Causal Map

### CAUSE-001 - EPIC024 generated-output drift

- Linked finding: `BUG-001`.
- Current contract: the harness writers are the source for the EPIC024 token matrix and acceptance map, and the canonical sanity primary is `audit/gates/sanity_pipeline/sanity_pipeline.log`.
- Repo reality: both writers emit the canonical path, but both checked-in outputs still emit `artifacts/sanity/sanity.log`.
- Conflict: governed primaries do not equal the bytes their current producer would render.
- Consequence: rerunning the producer is nondeterministic relative to the repository, while consumers see a retired path.
- Selected technical decision: add pure renderers and a selective refresh/check mode that touches exactly the two primaries, derives the historical bootstrap classification from the mutually consistent status pair already retained in those two primaries, and preserves all historical statuses.
- Affected dependency graph: harness renderer -> two governed primaries -> canonical updater -> Human Index, Machine Mirror, checksums, path proofs, orientation checks.
- Current and retained owners: `tools/qa/run_hde_epic024_harness.py` remains sole primary producer; `tools/evidence/update_evidence_index.py` remains sole companion producer. Historical EPIC024 QA remains closed.
- Historical plan boundary and proposed exception: r6 PR-06 owns the canonical sanity-path migration, not the EPIC024 acceptance-map or token-matrix primaries, and its historical boundary prohibits writes under the EPIC024 QA outputs. This CRD proposes that one narrow post-merge exception be incorporated into the separately authorized next-version Current Implementation Plan. Only after that plan revision is approved may separately authorized PR-A work use the HDE-EPIC024 harness's selective mode to rewrite exactly `docs/acceptance_map_epic024.json` and `audit/qa/hde-epic024/token_evidence_matrix.md`. The exception does not permit `_check_specs`, a QA rerun, status reevaluation, or any other EPIC024 primary write. This CRD does not itself revise either plan or authorize the write.
- Validation: byte-identity check mode; canonical path present; old path absent; `QA_BOOTSTRAP_OK=token_incomplete` and `QA_BOOTSTRAP_TOOLING_FAIL=implemented` unchanged; updater and orientation checks pass.
- Rollback: revert the two primary bytes and the same updater-owned companion refresh as one unit. Do not rerun QA to roll back.
- Plan consequence: this CRD does not edit either plan; after IA approval, `RSC-001` must be incorporated into and approved through the separately authorized next-version Current Implementation Plan before implementation relies on it. `r1` remains the epic-scope baseline and historical QA is not reopened.
- Canon/ADR consequence: `NO CANON CHANGE`; this restores existing canonical path ownership.

Evidence pointer: Repo | `tools/qa/run_hde_epic024_harness.py::_write_token_matrix` and `_write_acceptance_map` | "SANITY_PIPELINE_OK evidence is audit/gates/sanity_pipeline/sanity_pipeline.log."

Evidence pointer: Repo | `docs/acceptance_map_epic024.json`; `audit/qa/hde-epic024/token_evidence_matrix.md` | "Both checked-in primaries still bind SANITY_PIPELINE_OK to artifacts/sanity/sanity.log."

### CAUSE-002 - Raw-payload syntax blind spot

- Linked finding: `BUG-002`.
- Current contract: retained OPS evidence must contain no raw request, response, vendor payload, or vendor envelope.
- Repo reality: exact governed markers are scanned only in double-quoted JSON key form with `:`.
- Conflict: equivalent YAML, single-quoted, or assignment syntax bypasses the safety predicate.
- Consequence: unsafe retained bytes can be indexed after their checksum ledger is refreshed.
- Selected technical decision: detect the four exact governed markers with balanced optional quotes and either `:` or `=`, then allow only an exact closed set of redaction/null scalars.
- Affected dependency graph: OPS retained files -> checksum validation -> semantic secret/raw scanner -> Stage 12 admission -> updater/index/release sanity.
- Current and retained owners: `_validate_secret_safety` remains the validator owner; no generalized DLP subsystem is introduced.
- Validation: checksum-consistent mutation tests for unsafe JSON, YAML, single-quoted, assignment, empty, collection, block-scalar, and shell-expansion values plus exact safe-scalar tests.
- Rollback: revert scanner and its tests together. Previously admitted packets remain unmodified; validation fails closed on any newly recognized unsafe marker.
- Plan consequence: this CRD does not edit either plan; after IA approval, `RSC-002` must be incorporated into and approved through the separately authorized next-version Current Implementation Plan before implementation relies on it. `r1` remains the epic-scope baseline.
- Canon/ADR consequence: `NO CANON CHANGE`; enforcement is brought into line with the existing no-raw-payload contract.

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py`, raw marker detector | "The detector is `(?i)\"(?:raw_vendor_(?:payload|envelope)|raw_(?:request|response)_body)\"\\s*:`."

### CAUSE-003 - Unversioned and duplicated DDL projection

- Linked finding: `BUG-003`.
- Current contract: OPS-01 compares direct and bridge DDL posture as one ordered provider-parity row and must not claim beyond observed data.
- Repo reality: the producer silently projects shared identity fields while skipping malformed objects/columns; the consumer independently normalizes similar fields but raises on malformed data. Neither identifies a schema or excluded fields, and the retained result is plain `match`.
- Conflict: two implementations can drift, malformed data can be treated differently, and the result label overstates the comparison surface.
- Consequence: a release gate can certify ambiguous DDL parity and future changes can produce producer/consumer disagreement.
- Selected technical decision: extract `engine/db/ddl_identity_projection.py`, make both producer and validator call the same strict function, version the comparison contract, label only `projection_match`, and retain an explicit false full-semantic-parity claim.
- Affected dependency graph: direct/bridge DDL captures -> shared projector -> OPS packet producer -> `provider_parity.proof.json` v5 -> result summary v4 -> release-sanity validator -> updater/index/mirror.
- Current and retained owners: Glow owns projection and evidence semantics. PostgreSQL and `pg-bridge` remain observed providers and are not modified.
- Validation: exhaustive unit tests for valid direct/bridge shapes, malformed inputs, duplicates, conflicting type aliases, deterministic ordering, and excluded-field differences; packet mutation tests for contract/schema/label/false-claim drift.
- Rollback: before OPS, a projector defect blocks execution and is repaired or reverted through PR-A. On OPS failure, tracked state is unchanged. After PR-C, revert PR-C atomically to the matching v4 packet/default constants while retaining independent PR-A repairs; never mix versions.
- Plan consequence: this CRD does not edit either plan; after IA approval, `RSC-003` and `ADR-CANON-004` must be incorporated into and approved through the separately authorized next-version Current Implementation Plan before implementation relies on them. `r1` remains the epic-scope baseline and PF09 status does not move.
- Canon/ADR consequence: `AMENDS` under `ADR-CANON-004`.

Evidence pointer: Repo | `scripts/db/capture_epic011_posture.py::_ddl_projection` and `tools/evidence/run_sanity_pipeline.py::_normalize_ddl_provider_value` | "Two separate functions implement the same shared object-kind/name and column-name/type comparison with different malformed-input behavior."

### CAUSE-004 - OPS source/import qualification and unresolved launch contract

- Historical context: `BLK-001` and `ACT-002` are `UNVERIFIED` and non-operative; their alleged values do not establish this cause.
- Linked revisions: IA review v1.1 `REV-002`, `REV-003`, `REV-004`, and `REV-005`; IA review v1.2 `REV-001`.
- Governing contract: OPS-01R permits one bounded read-only observation from an exact clean Glow commit, with no retry, fallback, tracked write, Railway mutation, database mutation, vendor request, or `pg-bridge` work.
- Supportable engineering limitation: before a one-attempt external lane can be authorized, the exact tracked runner must prove importability and module origin from immutable source, deterministic production orchestration with zero external I/O, and the identities of every component used by discovery and live execution. V1.2 closed those fields but used `-I` without `-B`; Python could therefore create ignored bytecode/cache residue in the writable detached source while ordinary Git-clean assertions remained true. It also lacked a complete before/after source manifest, exact cache-residue scan, and explicit staging write-set proof.
- Execution-blocking operational unknowns: permitted current sources do not establish the candidate Railway executable path/resolved path/hash; its version; exact project, environment, and service IDs; supported explicit-target argv; nonlinked behavior; or injected target-identity fields. The local byte identity is `UNKNOWN PENDING PREFLIGHT`; the remaining facts are `UNKNOWN PENDING DISCOVERY`. None is a current fact or operator-selectable placeholder.
- Additional contract defects corrected by prior revisions remain closed: discovery authorization/static policy constrains all CLI calls and the expected-call-vector hash has one non-circular derived-only home. Current `REV-001` changes only the missing Python bytecode and filesystem-write isolation across preflight, target probe, and live child, plus the bounded source-loading producers, validators, and launcher necessary to prevent those controls from creating the same residue themselves.
- Consequence: without the current correction, an apparently clean and internally hash-consistent run could create or retain ignored source artifacts, or write outside the explicit control/candidate set, without violating the v1.2 Git-clean predicate.
- Selected technical decision: retain four necessary controls and close the current gap within them: `RSC-004.A` binds exact ordered `-I -B` preflight producer/validator execution, an empty `PYTHON*` child environment, full-source manifest equality, cache-residue absence, and an authenticated pre-staging delta limited to exact preflight writes; `RSC-004.B` binds the identical discovery producer/validator/target-probe rule and discovery write proof; `RSC-004.C` binds an independently invoked live-authorization validator plus identical live-launcher/live-child execution, an authenticated live pre-staging baseline, and exact live success/failure write sets; and `RSC-004.D` uses a capture-time validator to recompute all actual temporary source, residue, argv, environment, and staging predicates before candidate admission, while the distinct permanent validator later checks only retained proof and externally reviewed identities.
- Affected dependency graph: approved next-version Current Implementation Plan -> merged PR-A source -> independently validated offline `-I -B` preflight/source-write proof -> independently validated PO discovery authorization/policy -> bounded discovery with exact `-I -B` producer/validator/target probe -> validated discovery source/write proof -> exact PO live authorization -> independent exact `-I -B` live-authorization PASS -> one exact `-I -B` launcher/child OPS-01R launch -> isolated candidate -> exact `-I -B` capture-time actual-tree validation plus nested permanent packet validation -> later PR-C permanent packet review without an ephemeral-tree recapture claim.
- Owners: the approved plan allocates implementation; PR-A owns runner, validators, and tests; the PO separately authorizes discovery and the live attempt; the operator executes only exact validated commands; PR-C retains tracked integration ownership.
- Validation: exact argv order and environment in all three Python modes and their bounded supporting source-loading entry points; independently supplied baseline source-manifest and pre-staging identities; before/after full-source equality; no `__pycache__` component or `.pyc` file in either snapshot; authenticated complete staging deltas and exact mode-owned write sets; outside-source import resolution; closed preflight bytes and module origins; zero external preflight I/O; pre-CLI and immediate pre-dispatch discovery-policy validation; six-stage bounds; one launch; exact call-vector identity and equality; one-extra-call rejection; candidate isolation; and independent admission.
- Rollback: any missing, duplicated, substituted, reordered, or environment-replaced Python control, source-manifest mismatch, cache residue, or unauthorized write stops at the current boundary. Preflight or discovery failure ends before live authorization. A local identity/write mismatch before marker creation stops without launch; successful exclusive marker creation, any started or indeterminate subprocess state, or any later failure consumes the new authority, produces no admissible packet, and stops without retry. No recovery launch or reconstructed success is authorized.
- Plan consequence: this CRD does not edit either plan; after IA approval, `RSC-004` must be incorporated into and approved through the separately authorized next-version Current Implementation Plan before implementation relies on it. `r1` remains the epic-scope baseline.
- Documentation consequence: PF10 may later receive factual append-only discovery, preflight, authorization, count, and outcome facts. Recording is not a prerequisite or authority source.
- Canon/ADR consequence: `NO CANON CHANGE`; this operationally qualifies an existing bounded task.

Evidence pointer: CRD | §4 minimal failed-run record | "Every unsupported failed-run element is UNVERIFIED and no mandatory mechanism depends on it."

Evidence pointer: PF27 - PF27-Canon-Plan-Templates v1.9.5 | `Repository locus validation and file minting posture` | "Validated references only. Plans MUST NOT include any repository path, module home, command, or uniqueness claim ... that cannot be confirmed via canon or repo inspection."

Evidence pointer: PF07 - PF07-Canon-Glow-Infrastructure v2.2.4 | Front Matter `Change control`, bounded discovery posture | "When a PF07-owned fact ... is missing but can be safely discovered by the PO through bounded OPS discovery ... the artifact MUST route the unknown to that discovery work."
### CAUSE-005 - Evidence migration must be atomic

- Linked finding: `BUG-003`.
- Current contract: the release-sanity validator, retained packet, checksums, path proofs, Human Index, and Machine Mirror must describe one evidence version.
- Repo reality: merged evidence uses provider-proof v4, corpus v3, and result-summary v3; the selected projection contract requires provider-proof v5, corpus v4, and result-summary v4 bytes produced from an immutable checkout of the exact PR-A merge commit and admitted by a separate validator.
- Conflict: source-first or evidence-first merge would leave a version split, while permanent dual acceptance would make the final gate ambiguous.
- Consequence: CI may fail or, worse, admit the wrong evidence generation.
- Selected technical decision: PR-A leaves default release admission on the committed v4 packet and adds a tracked producer plus an independent candidate-only v5 validator. OPS runs from an immutable detached worktree at the exact PR-A merge commit. PR-C atomically integrates the full independently validated candidate and switches default release admission directly from v4 to v5. No default dual-version admission exists at any merged state.
- Affected dependency graph: merged PR-A closed rails -> OPS-01R candidate -> candidate validation -> PR-C primaries and v5 validator -> updater companions -> final closed rails -> separate merge action.
- Current and retained owners: PR-A owns independent repairs, the shared projector, and runner; the OPS lane owns candidate creation only; PR-C owns tracked evidence integration; the canonical updater owns all companions.
- Validation: explicit final test that v4 schema/corpus/constants and prior staging root are rejected; all updater, mirror, path, LF, and release-sanity checks pass.
- Rollback: no tracked change on OPS failure. Revert PR-C as one unit if integration fails; that restores the coherent v4 packet/default validator while retaining the independently valid PR-A scanner, EPIC024, shared-projector, and runner changes. If the shared projector itself is defective, revert its PR-A source/test subset separately and suspend OPS until a replacement PR is reviewed.
- Plan consequence: this CRD does not edit either plan; after IA approval, `RSC-005` must be incorporated into and approved through the separately authorized next-version Current Implementation Plan before implementation relies on it. The revision supersedes the original PR-06 integration sequence only for this bounded repair; `r1` remains the epic-scope baseline.
- Canon/ADR consequence: migration mechanics are part of `ADR-CANON-004`; no second canon decision is required.

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py` constants | "Current merged constants bind provider proof v4, corpus v3, and the prior literal staging root."

## 7. Requested Rescope

### RSC-001 - Selective EPIC024 acceptance-binding regeneration

- Requested addition: add a non-QA selective render/check mode to the existing EPIC024 harness and regenerate exactly two historical primaries.
- Canon effect: `NO CANON CHANGE`.
- Linked cause: `CAUSE-001`.
- Reason required now: PR 359 changed the canonical sanity path but left producer-owned historical outputs stale.
- Exact existing implementation locus: `tools/qa/run_hde_epic024_harness.py`.
- Ownership and narrow historical-plan exception: `tools/qa/run_hde_epic024_harness.py` is the historical primary owner. Current r6 PR-06 owns only the canonical sanity-path migration and historically prohibits writes to `docs/acceptance_map_epic024.json`, `audit/qa/hde-epic024/token_evidence_matrix.md`, and other EPIC024 QA outputs. This CRD proposes one narrow post-merge exception to that no-EPIC024-write boundary: after the required Current Implementation Plan revision is separately authorized and approved, PR-A may use only the HDE-EPIC024 harness selective mode to rewrite exactly those two named primaries. The exception does not permit `_check_specs`, a QA rerun, status reevaluation, or any other EPIC024 primary write. `r1` remains unchanged as the epic-scope baseline.
- Proposed CRD decision:
  - Extract pure functions `_render_token_matrix(*, bootstrap_status: str) -> bytes` and `_render_acceptance_map(*, bootstrap_status: str) -> bytes` from the existing writers. Their output remains canonical LF-terminated UTF-8, and both map the same validated bootstrap classification to their format-specific status spelling.
  - Add `_derive_retained_bootstrap_status(acceptance_map: object, token_matrix: str) -> str`. It requires the current primaries to agree on exactly one of two pairs: acceptance-map `QA_BOOTSTRAP_OK=implemented` plus `QA_BOOTSTRAP_TOOLING_FAIL=token_incomplete` and matrix `Implemented` plus `Token-incomplete` maps to `PASS`; acceptance-map `QA_BOOTSTRAP_OK=token_incomplete` plus `QA_BOOTSTRAP_TOOLING_FAIL=implemented` and the inverse matrix statuses maps to `TOOLING_BLOCKED`. Any missing, duplicated, differently cased, or conflicting status is an error.
  - Add `--refresh-acceptance-bindings-only`. It reads only the current two governed primaries, derives the already-retained bootstrap classification with `_derive_retained_bootstrap_status`, renders exactly `audit/qa/hde-epic024/token_evidence_matrix.md` and `docs/acceptance_map_epic024.json`, and exits without running `_check_specs` or writing any other EPIC024 file.
  - Add `--check-acceptance-bindings`. It renders expected bytes in memory and exits nonzero on either mismatch. It performs no writes.
  - Reject the selective mode if the two retained historical classifications are ambiguous or disagree. It must never inspect current tooling to infer PASS.
  - Preserve the existing acceptance-map statuses `QA_BOOTSTRAP_OK=token_incomplete` and `QA_BOOTSTRAP_TOOLING_FAIL=implemented` and the corresponding matrix wording. Only the `SANITY_PIPELINE_OK` path changes.
  - Before writing, calculate a semantic diff against both current primaries. The acceptance-map diff must be exactly one `SANITY_PIPELINE_OK.evidence_titles` element changing from `artifacts/sanity/sanity.log` to `audit/gates/sanity_pipeline/sanity_pipeline.log`. The matrix diff must be exactly that same old-to-new substring in the `SANITY_PIPELINE_OK` evidence cell. Every other JSON value, token row, column, ordering position, status, note, and line must remain unchanged. Any broader diff fails before write.
- Governed paths and keys:
  - Existing primary `docs/acceptance_map_epic024.json`; retain artifact key `epic024.acceptance_map` and its current producer.
  - Existing primary `audit/qa/hde-epic024/token_evidence_matrix.md`; retain artifact key `epic024.token_matrix` and its current producer.
  - No new primary, schema ID, artifact key, QA log, close-pack file, viability record, or historical manifest is introduced.
- Contract impact: generator and checked-in bytes become deterministic and agree on `audit/gates/sanity_pipeline/sanity_pipeline.log`.
- Compatibility and migration: one selective refresh changes only the two primaries. After those bytes are final, run the canonical updater and orientation generation/check sequence so proofs, index, mirror, and hashes follow the final primary bytes.
- Validation and evidence:
  - add focused tests for pure-renderer byte identity, exact one-path semantic diff per primary, selective touched-file set, retained two-primary classification preservation, conflicting-status refusal, and no call to `_check_specs`;
  - assert both primaries contain the canonical path and do not contain `artifacts/sanity/sanity.log`;
  - assert check mode is no-write;
  - run updater check, orientation check, evidence-path validation, mirror schema, evidence-index hash, and final-LF checks.
- Rollback: revert the exact two primaries and every updater-owned companion changed because of them as one commit unit.
- Downstream effect: EPIC024 consumers see the canonical path. Historical QA status, acceptance posture, and closeout remain exactly as recorded.
- Plan consequence: this CRD does not edit either plan. After IA approval, the separately authorized next-version Current Implementation Plan must allocate `RSC-001` to PR-A and be approved before implementation relies on it; `r1` remains the epic-scope baseline.
- PF09 relationship: no EPIC024 PF09 row is reopened. `HDE-DIST001.6` and `HDE-DIST005.2` constrain only the current epic's canonical-path admission and updater mechanics; their statuses do not move.
- Documentation consequence: PF10 section 2.9 may later or in parallel record this exact exception and nonclaim under separate documentation authority, and may later receive the verified selective-repair fact without claiming a QA rerun. PF10 is not an implementation gate.
- Nonclaims: no EPIC024 QA run, reapproval, status reopening, token satisfaction, PF09 movement, or historical closeout change.

### RSC-002 - Exact multi-syntax raw-payload marker enforcement

- Requested addition: close the retained-evidence marker syntax gap and preserve two already-resolved P1 controls.
- Canon effect: `NO CANON CHANGE`.
- Linked cause: `CAUSE-002`.
- Reason required now: merged Stage 12 can admit unsafe checksum-consistent bytes in ordinary log, YAML, or shell-assignment forms.
- Exact existing implementation locus: `tools/evidence/run_sanity_pipeline.py::_validate_secret_safety`.
- Proposed CRD decision:
  - extract the pure retained-text rules into proposed shared module `tools/evidence/retained_evidence_safety.py`, owning `SAFE_ENV_REFERENCE`, `RAW_PAYLOAD_MARKERS`, `_iter_raw_marker_assignments`, `_raw_marker_value_is_safe`, and `validate_retained_text_safety(path: Path, payload: bytes) -> tuple[str, ...]`. The function performs strict UTF-8 decoding and returns a deduplicated lexically sorted subset of the exact non-secret reason-code roster `NON_UTF8_RETAINED_TEXT`, `FORBIDDEN_SERVICE_URI`, `UNREDACTED_BEARER_VALUE`, `UNREDACTED_VENDOR_HEADER_VALUE`, `UNREDACTED_CREDENTIAL_VALUE`, `UNREDACTED_BIRTH_INPUT_VALUE`, and `UNSAFE_RAW_PAYLOAD_MARKER_VALUE`; an empty tuple is PASS. No code contains the retained value. `run_sanity_pipeline.py` and the independent v5 candidate validator both import this module; neither duplicates or weakens it;
  - Define `RAW_PAYLOAD_MARKERS = frozenset({"raw_vendor_payload", "raw_vendor_envelope", "raw_request_body", "raw_response_body"})` beside the current safety regexes.
  - Add `_iter_raw_marker_assignments(text: str) -> Iterator[tuple[str, str]]`. It recognizes only those exact case-insensitive marker names with either no quotes, balanced single quotes, or balanced double quotes, followed by `:` or `=`. Both sides of an unquoted marker require identifier boundaries, so names such as `not_raw_vendor_payload` and `raw_vendor_payload_copy` do not match. It does not broaden to fuzzy `raw_*` names.
  - Add `_raw_marker_value_is_safe(raw: str) -> bool`. It preserves the current safe-value contract exactly: only unquoted case-insensitive JSON literals `false` and `null`, or double-quoted case-insensitive JSON strings `"none"` and `"redacted"`, are safe. It does not newly admit unquoted redaction words, single-quoted values, the angle-bracketed `redacted` token, environment references, or shell syntax. It rejects empty values, mappings, sequences, block scalars `|` and `>`, shell expansions, command substitution, and every other value.
  - A recognized marker with no complete same-line scalar is unsafe. Multiline continuation cannot convert an unsafe first token into a safe value.
  - Keep `SAFE_ENV_REFERENCE` unchanged. It must continue to full-match only `$NAME` and `${NAME}`.
  - Keep `_validate_bodygraph_selection_snapshot` and all provider-provenance predicates unchanged except for schema-version migration required by `RSC-003`.
- Contract and unknown-key posture: the scanner is a text safety gate, not a parser. It has a closed marker roster and closed safe-scalar roster. Unrecognized keys are outside this marker rule but remain subject to existing URI, credential, birth-input, bearer, and header checks.
- Compatibility and migration: the exact four previously accepted safe RHS forms remain accepted and no new safe RHS spelling is introduced. Any retained packet using an unsafe marker form becomes invalid and must be rewritten to one of those existing safe forms, not grandfathered.
- Validation and evidence:
  - checksum-consistent failures for `raw_vendor_payload: {private: value}`, `'raw_vendor_payload': {'private':'value'}`, `raw_vendor_payload={'private':'value'}`, `raw_request_body = secret`, `raw_response_body: |`, empty RHS, arrays, shell defaults, and command substitution;
  - positive tests for `false`, `null`, `"none"`, and `"redacted"` across each marker-key quote style and both delimiters, plus negative tests proving unquoted/single-quoted redaction words and marker-name substrings are rejected or not misclassified;
  - retain the existing negative tests for `${HD_API_KEY:-live-secret}`, `${GEO_API_KEY:=live-secret}`, command substitution, and the full provider-selection snapshot mutation matrix.
- Proposed test locus: add focused pure tests in `tests/evidence/test_retained_evidence_safety.py`; retain pipeline-level packet mutation tests in `tests/evidence/test_hde_epic038_release_sanity.py` so extraction cannot bypass Stage 12.
- Rollback: revert scanner and tests together. There is no data migration.
- Downstream effect: release-sanity admission becomes syntax-neutral for the four governed markers; other evidence semantics do not change.
- Plan consequence: this CRD does not edit either plan. After IA approval, the separately authorized next-version Current Implementation Plan must allocate `RSC-002` to PR-A and be approved before implementation relies on it; `r1` remains the epic-scope baseline. This affects `HDE-DIST001.6` and preserves the existing `HDE-DIST001.11` safety posture without status movement.
- Documentation consequence: PF10 section 2.9 may later or in parallel record the approved predicate and finding disposition and may receive verified implementation facts after they exist. PF10 is not an implementation gate.
- Nonclaims: no generalized DLP engine, no raw-payload content inspection outside the exact markers, no modification of existing evidence bytes solely to demonstrate the test, and no claim that every possible secret form is detected.

### RSC-003 - Shared versioned DDL identity projection and OPS evidence v5

- Requested addition: replace duplicate implicit DDL projection logic with one strict Glow-owned contract and migrate the retained OPS-01 proof.
- Canon effect: `AMENDS` under `ADR-CANON-004`.
- Linked causes: `CAUSE-003`, `CAUSE-005`.
- Reason required now: the current plain `match` claim and duplicate implementations are ambiguous at the exact release gate that consumes the OPS packet.
- Proposed CRD decision: add `engine/db/ddl_identity_projection.py` as the sole DDL identity-projection implementation, use it in the existing posture producer and validator in PR-A, and migrate retained evidence in PR-C.
- Proposed API and constants:

```python
DDL_IDENTITY_PROJECTION_SCHEMA = "hde.ddl_identity_projection.v1"
DDL_IDENTITY_PROJECTION_FIELDS = (
    "projection[].kind",
    "projection[].name",
    "projection[].columns[].name",
    "projection[].columns[].type",
)
DDL_IDENTITY_UNEXAMINED_FIELDS = (
    "source[].columns[].nullable",
    "source[].columns[].default",
    "source[].constraints",
    "source[kind=view].definition",
)

def project_ddl_identity(value: object) -> list[dict[str, object]]:
    ...
```

- Proposed function contract:
  - input must be a nonempty list;
  - every object must be a mapping with exact nonempty, already-trimmed string `kind` and `name` fields;
  - governed kinds are exactly `table` and `view`;
  - duplicate `(kind, name)` objects are rejected;
  - a table must have a nonempty `columns` list;
  - a view may omit `columns` or use an empty list; both inputs normalize to an output `"columns": []`; if nonempty columns are present, each is validated normally;
  - every column must be a mapping with exact nonempty, already-trimmed string `name`;
  - type is read from `type` or `data_type`; if both exist they must be identical nonempty strings, otherwise reject;
  - duplicate column names within an object are rejected;
  - type strings are preserved exactly; the projector performs no alias normalization;
  - malformed objects and columns are rejected and never skipped;
  - objects sort by `(kind, name)` and columns by `(name, type)`;
  - provider-specific fields outside the included roster may be present in input but are never compared or represented as examined;
  - every output object contains exactly `kind`, `name`, and `columns`; output columns contain only `name` and `type`;
  - `source` in the unexamined roster is the logical root of each direct or bridge provider row's retained `value` member. `projection` in the included roster is the canonical output of `project_ddl_identity(source)`. The direct input alias `data_type` and bridge input alias `type` both populate the exact projected field `projection[].columns[].type`; neither alias is silently preferred when both are present and unequal.
- Existing consumers changed:
  - `scripts/db/capture_epic011_posture.py` deletes `_ddl_projection` and imports `project_ddl_identity` for producer comparison.
  - `tools/evidence/run_sanity_pipeline.py` deletes `_normalize_ddl_provider_value` and imports the same function for retained-evidence validation.
- Proposed test locus: new `tests/db/test_ddl_identity_projection.py`; extend `tests/evidence/test_hde_epic038_release_sanity.py`.
- Proposed evidence versions:
  - `OPS01_PROVIDER_PROOF_SCHEMA = "hde_epic038.ops01.provider_parity.v5"`;
  - `OPS01_CORPUS_NAME = "hde_epic038_ops01_live_bodygraph_parity_v4"`;
  - `result_summary.json` schema `hde_epic038.ops01.result_summary.v4`.
- Exact success-packet primary inventory, paths, and retained artifact keys:

| Filename under `audit/ops/hde-epic038/ops-01/` | Artifact key |
| --- | --- |
| `commands.txt` | `epic038.pr06.ops01.commands_txt` |
| `stdout.log` | `epic038.pr06.ops01.stdout_log` |
| `stderr.log` | `epic038.pr06.ops01.stderr_log` |
| `exit_code.txt` | `epic038.pr06.ops01.exit_code_txt` |
| `env_presence.json` | `epic038.pr06.ops01.env_presence_json` |
| `db_posture_summary.json` | `epic038.pr06.ops01.db_posture_summary_json` |
| `provider_parity.proof.json` | `epic038.pr06.ops01.provider_parity_proof_json` |
| `bridge_consistency.result.json` | `epic038.pr06.ops01.bridge_consistency_result_json` |
| `nonclaims.json` | `epic038.pr06.ops01.nonclaims_json` |
| `result_summary.json` | `epic038.pr06.ops01.result_summary_json` |
| `checksums.sha256` | `epic038.pr06.ops01.checksums_sha256` |

  No success primary may be added, omitted, renamed, or substituted. `checksums.sha256` contains exactly one lowercase SHA-256 and filename entry for each of the other ten primaries, sorted by filename, and excludes itself.
- Proposed DDL row contract:

```json
{
  "name": "ddl_fingerprint",
  "parity": "projection_match",
  "comparison_contract": {
    "schema": "hde.ddl_identity_projection.v1",
    "mode": "shared_identity_projection",
    "included_fields": [
      "projection[].kind",
      "projection[].name",
      "projection[].columns[].name",
      "projection[].columns[].type"
    ],
    "unexamined_fields": [
      "source[].columns[].nullable",
      "source[].columns[].default",
      "source[].constraints",
      "source[kind=view].definition"
    ],
    "ordering": "objects_by_kind_name_columns_by_name_type"
  }
}
```

- Required provider-proof v5 fields and unknown-key posture:
  - the exact top-level key set is `active_parity_corpus`, `attempts`, `capabilities`, `captured_at_utc`, `environment`, `full_ddl_semantic_parity_claimed`, `live_provider_parity`, `payload_posture`, `provider_observations`, `rails_open`, `rails_posture`, `remediation_marker`, `schema`, `selected`, and `status`;
  - `schema` is v5, `status` is `PASS`, `selected` is `psycopg`, `environment` is `dev`, `rails_open` is false, `full_ddl_semantic_parity_claimed` is false, and `remediation_marker` is exactly `F-009_DDL_IDENTITY_PROJECTION_CONTRACT`;
  - `active_parity_corpus` has exactly `name`, `ordered_rows`, and `selector`; `selector` has exactly `alias`, `identity_source`, `non_pii`, and `uuid`; the name is `hde_epic038_ops01_live_bodygraph_parity_v4` and the ordered rows are exactly `grants`, `search_path`, `select_one`, `ddl_fingerprint`, `bodygraph_payload_row`;
  - top-level `attempts` is exactly one `{provider: "psycopg", status: "ok"}` object;
  - `capabilities` is exactly five rows in corpus order. `grants`, `search_path`, and `select_one` rows have exactly `name`, `direct`, `bridge`, and `parity`; each provider object has exactly `status` and `value`; parity is `match`;
  - the DDL row has exactly `name`, `direct`, `bridge`, `parity`, and `comparison_contract`; each provider object has exactly `status` and `value`; parity and contract are exactly the projection contract below;
  - the BodyGraph row has exactly `name`, `direct`, `bridge`, `parity`, `comparison`, `payload_fetch_implementation`, `read_surface`, and `selector`. Each side has exactly `canonical_sha256`, `provider`, `raw_bodygraph_payload_recorded`, `selection_snapshot`, `staged_output`, and `status`. Each selection snapshot has exactly `content`, `path`, and `sha256`; content has exactly `attempts`, `flags`, `schema`, `selected`, and `selection_order`; flags has exactly `allow_bridge_prod`, `env`, `force_bridge`, and `force_pg`;
  - `live_provider_parity` has exactly `bridge_provider_rows`, `claimed_row_count`, `direct_provider_rows`, `matched_row_count`, and `parity_status`; `payload_posture` has exactly `raw_bodygraph_payload_persisted`, `raw_user_data_persisted`, and `secret_values_persisted`; `provider_observations` has exactly `bridge` and `direct`; `rails_posture` has exactly `ALLOW_DB_WRITE`, `ALLOW_NETWORK`, `APP_ENV`, `SAFE_MODE`, and `all_actions`;
  - both provider-row availability values are `available`, both provider observations are `ok`, both row counts are integer `5`, parity status is `pass`, every payload-posture boolean is false, and rails posture is the exact closed-rails `ALLOW_DB_WRITE=0`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `SAFE_MODE=1`, `all_actions=closed` tuple;
  - unknown keys are rejected at every proof object listed above. Provider `value` members may retain provider-specific metadata, but only `project_ddl_identity` output participates in the DDL predicate and no extra metadata may be described as examined.
- Required result-summary v4 fields and unknown-key posture:
  - the exact top-level key set is `acceptance_tokens`, `active_parity_corpus`, `active_parity_rows`, `actual_call_counts`, `authorization`, `authorization_sha256`, `bodygraph_selector`, `captured_at_utc`, `checksum_policy`, `discovery_identity_sha256`, `epic_closeout`, `execution`, `expected_call_counts`, `full_ddl_semantic_parity_claimed`, `literal_staging_root`, `observations`, `ops_observation_status`, `packaged_at_utc`, `pf09_status_movement`, `preflight_identity_sha256`, `qa_status`, `remediation_findings_resolved`, `repository`, `runner_sha256`, `schema`, and `scope`;
  - `bodygraph_selector` has exactly `alias`, `identity_source`, `non_pii`, and `uuid`; `checksum_policy` has exactly `algorithm` and `ledger_excludes_itself`; `repository` has exactly `branch`, `head`, `post_execution_worktree`, `pre_execution_worktree`, and `root`;
  - `observations` has exactly `bodygraph_row_parity`, `bridge_consistency`, `bridge_provider`, `claimed_rows`, `db_posture`, `ddl_identity_projection`, `direct_provider`, `matched_rows`, and `search_path`;
  - `authorization` is the complete closed non-secret authorization object defined in `RSC-004.C`, including the validated discovery contract and exact expected-call vector, with no additional member. The validator canonicalizes the object as key-sorted compact JSON plus LF and requires its SHA-256 to equal `authorization_sha256`; `preflight_identity_sha256` and `discovery_identity_sha256` must equal the corresponding identities embedded in that authorized object;
  - `literal_staging_root` equals `authorization.run.staging_root`; `authorization.run.candidate_root` is exactly its `candidate` child; every retained staged path resolves beneath that candidate root;
  - `execution` has exactly `candidate_validator_argv`, `commands_sha256`, `launch_executions`, `source_checkout_state`, and `source_write_validation`. `launch_executions` is integer `1`, source state is `DETACHED`, and `commands_sha256` is the checksum of retained `commands.txt`. `candidate_validator_argv` is exactly `[authorization.interpreter.path, "-I", "-B", authorization.validator.path, "--validate-candidate", "--expected-identity-stdin", authorization.run.candidate_root]`; it is the only authoritative permanent packet-validator CLI vector, receives the exact external `Ops01V5ExpectedIdentity` through the canonical stdin contract below, and rejects omission, substitution, duplication, reordering, environment replacement, or alternate expected-input transport. `source_write_validation` is the complete live-mode object defined in `RSC-004.A` and `.C`; its exact `python_argv` is the authorization-bound live child argv, its pre/post source hashes equal the authorization and external expected source-manifest identity, its authenticated pre-staging hash equals both the authorization write contract and `Ops01V5ExpectedIdentity.live_pre_staging_manifest_sha256`, its post-staging hash equals `Ops01V5ExpectedIdentity.live_post_staging_manifest_sha256`, its cache and unauthorized-path lists are empty, and its status is `PASS`. Capture-time validation recomputes the actual ephemeral source/staging trees; permanent packet validation later checks retained canonical proof identities and semantics without claiming that those temporary trees still exist. Independent validation proves target identity by comparing retained environment-presence facts with the hash-bound authorization's discovered target contract; the summary does not repeat those facts as a second mutable contract;
  - `expected_call_counts` and `actual_call_counts` each have exactly the ten fields defined in `RSC-004.A`. Every value is a nonnegative integer, not a boolean. The known exact values are `logical_observations=10`, `bodygraph_reads=2`, `direct_provider_selections=1`, `bridge_provider_selections=1`, `vendor_requests=0`, `retries=0`, and `fallbacks=0`; exact values for direct connections, direct SQL statements, and bridge HTTP requests are supplied by the independently validated deterministic preflight and copied field by field into the live authorization;
  - `expected_call_counts_sha256` is deliberately absent from the exact preflight, live-authorization, and result-summary serialized key rosters. It is a derived-only independent identity. Its sole authoritative source is `result_summary.authorization.expected_call_counts`, equivalently the authorization object before embedding. Canonical bytes are key-sorted compact ASCII-escaped UTF-8 JSON plus exactly one LF, and the derived identity is the lowercase SHA-256 of those bytes;
  - admission requires, in order: independently validated `preflight.expected_call_counts == authorization.expected_call_counts`; the embedded canonical authorization hash equals `authorization_sha256`; `result_summary.expected_call_counts == result_summary.authorization.expected_call_counts`; the independently supplied `Ops01V5ExpectedIdentity.expected_call_counts_sha256` equals the validator's recomputation from that embedded authorization vector; and `result_summary.actual_call_counts == result_summary.authorization.expected_call_counts`, all field by field. There is no producer-supplied vector-hash field and no successful range or less-than-or-equal predicate. Adding `expected_call_counts_sha256` to any serialized preflight, authorization, or result-summary object is an unknown-key failure;
  - `active_parity_corpus` and `active_parity_rows` exactly match the proof; `checksum_policy` is `sha256` with ledger self-exclusion true; `ops_observation_status` is `PASS`; both provider availability values are `available`; both row counts are integer `5`; `db_posture` and `bridge_consistency` are `PASS`; `bodygraph_row_parity` is `match`; `ddl_identity_projection` is `projection_match`; and `search_path` is `hde, public`;
  - `remediation_findings_resolved` is exactly the ordered current roster `F-004_LITERAL_COMMANDS`, `F-005_RAW_STREAM_AND_CHECKER_BINDING`, `F-006_BODYGRAPH_ROW_PARITY`, `F-007_OPS01_SCOPE`, `F-008_BODYGRAPH_PROVIDER_SELECTION_PROVENANCE`, followed by `F-009_DDL_IDENTITY_PROJECTION_CONTRACT`;
  - `acceptance_tokens=NOT_CLAIMED`, `epic_closeout=NOT_CLAIMED`, `pf09_status_movement=NONE`, and `qa_status=NOT_CLAIMED`; repository branch is `DETACHED`, root is the unique immutable source worktree, head is the exact PR-A merge SHA, both pre/post worktree values are `clean`, `authorization_sha256` is the exact recomputed canonical authorization-object hash, and `runner_sha256` equals the exact executed tracked-runner hash; unknown keys are rejected at every summary object listed above.
- Unchanged success-primary schemas and formats:
  - `env_presence.json` remains `hde_epic038.ops01.env_presence.v3`, `db_posture_summary.json` remains `hde_epic038.ops01.db_posture_summary.v3`, `bridge_consistency.result.json` remains `hde_epic038.ops01.bridge_consistency.v3`, and `nonclaims.json` remains `hde_epic038.ops01.nonclaims.v3`;
  - `env_presence.json` has exactly top-level `captured_at_utc`, `environment_presence`, `execution_rails`, `operator_console`, `repository`, `schema`, `secret_posture`, and `target`. `environment_presence` has exactly `ALLOW_DB_WRITE`, `ALLOW_NETWORK`, `APP_ENV`, `DATABASE_URL`, `DB_BRIDGE_URL`, `ENGINE_ENV`, `LANG`, `LC_ALL`, `SAFE_MODE`, and `TZ`. `execution_rails` has exactly `bridge_bodygraph_read`, `canonical_comparison`, `db_posture_capture`, `direct_bodygraph_read`, and `governed_checker`. `bridge_bodygraph_read` is exactly `{ALLOW_DB_WRITE: "0", ALLOW_NETWORK: "0", DB_FORCE_BRIDGE: "1", DB_FORCE_PG: "UNSET", SAFE_MODE: "1"}`; `direct_bodygraph_read` is exactly `{ALLOW_DB_WRITE: "0", ALLOW_NETWORK: "0", DB_FORCE_BRIDGE: "UNSET", DB_FORCE_PG: "1", SAFE_MODE: "1"}`; and each of `canonical_comparison`, `db_posture_capture`, and `governed_checker` is exactly `{ALLOW_DB_WRITE: "0", ALLOW_NETWORK: "0", SAFE_MODE: "1"}`. `repository` has exactly `branch`, `head`, `pre_execution_worktree`, and `root`; `target` has exactly `bridge_service`, `db_instance`, `db_schema`, `project`, and `provider`. Required values are presence-only credentials, `operator_console=github_codespaces`, `secret_posture=presence_only`, `branch=DETACHED`, the authorized commit/root, `pre_execution_worktree=clean`, `project=ample-illumination`, `provider=Railway`, and `db_schema=hde`;
  - `db_posture_summary.json` has exactly top-level `bodygraph_unique_constraints`, `boundary_views`, `boundary_views_readonly`, `captured_at_utc`, `database_schema`, `default_privileges`, `fingerprint_objects`, `grants`, `observation_mode`, `partition_plan`, `partition_plan_status`, `schema`, `search_path`, `search_path_exact`, `source_capture_root`, and `status`. Unique-constraint rows have exactly `definition` and `name`; boundary-view rows exactly `is_insertable_into`, `is_trigger_updatable`, `is_updatable`, `name`, and `readonly`; fingerprint rows exactly `kind` and `name`; grant rows exactly `grantees`, `object`, and `privileges`; partition rows exactly `key`, `strategy`, and `table`. Decisive values are `database_schema=hde`, `observation_mode=read_only`, `search_path="hde, public"`, `search_path_exact=true`, `boundary_views_readonly=true`, `default_privileges=none_observed`, `partition_plan_status=PASS`, and `status=PASS`. The exact v3 rosters are: one unique constraint named `body_graphs_user_id_vendor_vendor_version_input_fingerprint_key` with definition `UNIQUE (user_id, vendor, vendor_version, input_fingerprint)`; boundary views `hde.body_graphs_current` and `public.hde_body_graphs_current`, each with `is_insertable_into="NO"`, `is_trigger_updatable="NO"`, `is_updatable="NO"`, and `readonly=true`; fingerprint objects `{kind: "table", name: "hde.body_graphs"}`, `{kind: "view", name: "hde.body_graphs_current"}`, and `{kind: "view", name: "public.hde_body_graphs_current"}`; grants for exactly those same three object names, each with `grantees=["postgres"]` and `privileges=["DELETE", "INSERT", "REFERENCES", "SELECT", "TRIGGER", "TRUNCATE", "UPDATE"]`; and partition rows `{key: "(evaluated_at)", strategy: "RANGE", table: "hde.pair_evaluation"}` and `{key: "(created_at)", strategy: "RANGE", table: "hde.public_results"}`. `source_capture_root` must be contained beneath the authorized literal staging root;
  - `bridge_consistency.result.json` has exactly top-level `bodygraph_comparator`, `captured_at_utc`, `command_exit_codes`, `governed_checker`, `predicates`, `schema`, and `status`. `bodygraph_comparator` has exactly `bridge_input`, `canonical_sha256`, `direct_input`, `exit_code`, `identity`, `literal_invocation`, and `result`; each input has exactly `path` and `sha256`. `command_exit_codes` has exactly `bridge_bodygraph_read`, `canonical_comparison`, `db_posture_capture`, `direct_bodygraph_read`, and `governed_checker`. `governed_checker` has exactly `exit_code`, `inputs`, `literal_invocation`, `repo_identity`, `repo_sha256`, `result`, `staged_executable`, and `staged_sha256`; its `inputs` has exactly `adapter_selection`, `env_connectivity`, and `provider_parity`, each with exactly `path` and `sha256`. `predicates` has exactly `all_actions_closed_rails`, `bodygraph_bridge_available`, `bodygraph_direct_available`, `bodygraph_provider_selection_provenance`, `bodygraph_row_match`, `bodygraph_selector_approved`, `four_row_corpus_exact`, `provider_selection_consistent`, and `search_path_exact`. Every command exit is integer zero, every predicate is true, both checker identities and hashes agree with the staged reviewed executable, comparator identity is `presenter.json_canon_compare`, comparator result is `FILE_EQ_CANON_BYTES_OK`, checker result and top-level status are `PASS`, and every retained path is contained beneath the literal staging root;
  - `nonclaims.json` has exactly top-level `captured_at_utc`, `nonclaims`, `pf09_posture`, and `schema`. `nonclaims` is exactly the ordered roster `no_sql_write`, `no_migration`, `no_grant_change`, `no_schema_change`, `no_vendor_call`, `no_deployment_change`, `no_raw_secret_persistence`, `no_raw_user_data_persistence`, `no_raw_bodygraph_payload_persistence`, `no_qa_pass_claim`, `no_acceptance_token_claim`, `no_pf09_status_movement`, and `no_epic_closeout_claim`. `pf09_posture` has exactly `HDE-DIST001`, `HDE-DIST001.4`, `HDE-DIST001.9`, and `status_change`, with the first three `Partial` and the last `none`;
  - unknown keys are rejected at every object roster stated above. Only capture identity, detached worktree root, staging paths, hashes, and timestamps may vary where explicitly identified; all other predicates and literal values are closed;
  - `exit_code.txt` is exactly `0` plus LF for a success packet; `stdout.log` and `stderr.log` are UTF-8, LF-terminated, checksum-bound, and must pass every secret/raw scanner. `commands.txt` is canonical UTF-8/LF with one sanitized JSON argv array per executed live subprocess; a success packet has exactly one line because `launch_executions=1`. The validator reconstructs that exact line only as `authorization.discovery.run_contract.argv_prefix + authorization.run.child_argv`, requires `authorization.discovery.run_contract.child_argv_start_index == len(argv_prefix)`, and requires the suffix at that index to equal the exact five-token live child `[interpreter.path, "-I", "-B", runner.path, "--live-child"]`. It rejects every boundary, omission, duplication, substitution, reordering, secret, or endpoint-value drift and requires the complete line checksum to equal `commands_sha256`. CLI authentication is launcher-only and excluded from the child; DB endpoint values are child-environment-only; neither appears in argv or retained evidence except endpoint presence. Runner-source identity is retained separately by `runner_sha256`; the checksum ledger format is defined by the inventory rule above.

  Evidence pointer: Repo | `audit/ops/hde-epic038/ops-01/env_presence.json` | "Current retained v3 execution-rail key sets and values are the exact direct, bridge, comparison, posture, and checker tuples enumerated above."

  Evidence pointer: Repo | `audit/ops/hde-epic038/ops-01/db_posture_summary.json` | "Current retained v3 unique constraint, boundary-view, fingerprint-object, grants, and partition rosters are the exact literals enumerated above."
- Required DDL and summary predicates:
  - provider proof top level requires `full_ddl_semantic_parity_claimed: false`;
  - the DDL row requires the exact closed `comparison_contract` object and `parity: "projection_match"`;
  - result summary requires `scope: "bounded_read_only_db_posture_and_declared_provider_contract_comparison"`, `observations.ddl_identity_projection: "projection_match"`, and `full_ddl_semantic_parity_claimed: false`;
  - plain DDL `parity: "match"`, missing contract metadata, reordered or changed field rosters, additional contract keys, or a true/missing full-parity flag are rejected;
  - all existing provider-selection snapshot, attempts, order, force-flag, bodygraph hash, selector, no-raw-persistence, rails, and nonclaim predicates remain required.
- Serialization: retained JSON remains canonical UTF-8, ASCII-escaped, key-sorted, compact, and LF-terminated. Checksums remain SHA-256 and exclude the ledger itself.
- Sole producer and consumers:
  - tracked `scripts/ops/hde_epic038_ops01r.py`, executed at the exact authorized merged PR-A blob, is the sole producer of candidate OPS-01 primary bytes;
  - proposed independent module `tools/evidence/hde_epic038_ops01_v5.py` owns two distinct read-only validation boundaries. Permanent packet API `validate_ops01_v5_package(root: Path, *, expected: Ops01V5ExpectedIdentity) -> Ops01V5ValidationResult` validates candidate or integrated retained bytes and never requires the temporary source, control, or non-candidate staging tree. Its standalone CLI receives `expected` only through the exact retained `candidate_validator_argv` and canonical expected-identity stdin contract; direct PR-C/release callers may instead pass only the checked-in `OPS01_V5_EXPECTED` object to the Python API. Frozen dataclass `Ops01V5ExpectedIdentity` has exactly `authorization_sha256`, `candidate_ledger_sha256`, `commands_sha256`, `discovery_identity_sha256`, `expected_call_counts_sha256`, `literal_staging_root`, `live_post_staging_manifest_sha256`, `live_pre_staging_manifest_sha256`, `preflight_identity_sha256`, `projector_sha256`, `runner_sha256`, `source_commit`, `source_manifest_sha256`, and `validator_sha256`. `source_manifest_sha256` is captured independently before preflight and must equal every retained pre/post source-manifest identity in the hash-bound preflight, discovery, authorization, and result chain. `live_pre_staging_manifest_sha256` is captured independently after the live-authorization placeholder and required empty candidate root exist, is embedded in the canonical authorization, is recaptured under identical exclusions after in-place authorization finalization, and is frozen only when both captures are byte-identical and before PO authorization or launcher execution. `live_post_staging_manifest_sha256` is independently computed from the actual post-run non-candidate staging tree at capture time. Both staging identities must equal the live result's retained proof and are never accepted solely from producer output. `expected_call_counts_sha256` remains external and derived only by independent recomputation over the reviewed authorization vector; it is never read from a packet field. The permanent API recomputes canonical retained authorization/discovery/summary/command/ledger identities, validates the closed source/write proof schemas, exclusions, delta/path semantics, and expected identities, and rejects any claim that it recaptured an ephemeral tree after integration;
  - capture-time API `validate_ops01r_live_capture(staging_root: Path, *, expected: Ops01V5ExpectedIdentity) -> Ops01V5ValidationResult` runs only after the runner exits and before candidate admission while the exact detached source and complete staging tree still exist. Its CLI entry point receives the independently reviewed exact `Ops01V5ExpectedIdentity` bytes only through `authorization.run.live_capture_validator_argv` and canonical stdin. It invokes the permanent packet function in-process with that same parsed immutable object for candidate semantics, independently recomputes the actual source manifest, cache scan, non-candidate post-staging manifest and complete delta under the authorization-bound exclusions, validates the excluded candidate subtree through its inventory/ledger/semantic result, and requires equality to `expected.source_manifest_sha256`, `.live_pre_staging_manifest_sha256`, and `.live_post_staging_manifest_sha256`. Its PASS plus the nested permanent packet PASS is the capture-time candidate-admission result. It emits no governed receipt and writes nothing;
  - frozen dataclass `Ops01V5ValidationResult` has exactly `valid: bool` and `errors: tuple[str, ...]`; errors are unique stable non-secret reason codes sorted lexically. The module imports the shared projector and has no producer or write path. PR-A tests both APIs independently against frozen positive and mutation fixtures. The producer may call either only as a non-authoritative self-check. The operator constructs `Ops01V5ExpectedIdentity` from independently reviewed capture facts, including all three external manifest identities, the candidate-ledger hash, and the independently derived expected-vector hash, then supplies its canonical bytes to the authorization-bound capture-time validator vector. Standalone candidate review supplies the same bytes to the exact retained candidate-validator vector. PR-C repeats only the permanent packet validation against the untouched candidate before copy and against copied retained bytes after copy, using either that exact canonical-stdin CLI boundary or a direct Python call with the checked-in `OPS01_V5_EXPECTED`; `tools/evidence/run_sanity_pipeline.py` imports that same permanent function when PR-C switches default admission to v5;
  - for IA review v1.2 `REV-001`, the complete exact v5 isolation/write admission-code subset is `OPS01_V5_BYTECODE_CONTROL_MISMATCH`, `OPS01_V5_PYTHON_ARGV_MISMATCH`, `OPS01_V5_PYTHON_ENVIRONMENT_INVALID`, `OPS01_V5_SOURCE_MANIFEST_MISMATCH`, `OPS01_V5_SOURCE_RESIDUE_DETECTED`, and `OPS01_V5_WRITE_SET_MISMATCH`. The separate exact external-input transport code is `OPS01_V5_EXPECTED_INPUT_INVALID`. The six isolation/write codes and one transport code are the exhaustive v5 additions made by this revision, are unique, non-secret, and each blocks admission; the isolation/write subset remains lexically sorted as listed. Non-isolation v5 validation behavior preserved from v1.2 is unchanged; this revision neither renames those errors nor claims a newly enumerated complete pre-existing non-isolation roster;
  - no failure packet or negative receipt is admissible under this API. A failed or incomplete run produces no success package for integration; any separately retained operator failure summary is temporary, sanitized, and outside governed success evidence;
  - `tools/evidence/run_sanity_pipeline.py` remains the default release-sanity consumer. PR-A does not route default admission to v5; PR-C changes only the default dispatch and expected retained identity to the independently tested v5 validator;
  - `tools/evidence/update_evidence_index.py` remains sole producer of path proofs, Human Index, Machine Mirror, and related checksums;
  - no other generator may synthesize v5 provider proof bytes.
- Compatibility and migration:
  - PR-A merges the strict shared projector, tracked runner, and independent `tools/evidence/hde_epic038_ops01_v5.py` validator while default release sanity continues to validate only the committed v4 packet. The independent validator is callable for candidate roots but has no default release-admission path;
  - OPS-01R produces only provider-proof v5, corpus v4, and result-summary v4 candidate evidence from the exact detached PR-A source commit and independent validator contract;
  - PR-C replaces the complete v4 packet with the reviewed candidate, updates default release-sanity schema, runner-hash, and staging-root constants directly to v5, and introduces no default dual-version admission;
  - the PR-C final state must reject v4 proof schema, result-summary v3, corpus v3, the prior runner hash, and the prior staging root.
- Exact companion and release-binding inventory: for each of the eleven indexed primary filenames, the canonical updater owns the sibling produced by appending `.path_proof.txt`, plus `docs/evidence/INDEX.json`, `docs/evidence/INDEX.json.path_proof.txt`, `docs/evidence/INDEX.sha256`, `docs/evidence/INDEX.sha256.path_proof.txt`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.path_proof.txt`, `artifacts/evidence_index.jsonl.sha256`, and `artifacts/evidence_index.jsonl.sha256.path_proof.txt`. Current orientation ownership remains with `tools/evidence/orientation_demo.py` for `docs/EVIDENCE_INDEX.md` and `docs/INDEX.md`. Artifact keys and primary paths remain stable; all listed companions and orientation surfaces are regenerated only after final primary bytes are copied. The canonical sanity gate runs only after those companions are current.
- Validation and evidence:
  - projector unit tests cover both retained provider shapes, deterministic ordering, omitted-versus-empty view-column equivalence, always-present output columns, duplicates, malformed mappings, absent/empty/conflicting types, skipped-item prohibition, and differences only in unexamined fields;
  - release-sanity mutation tests cover schema, corpus, field roster, ordering label, full-parity false flag, DDL result label, direct/bridge values, and inherited selection snapshot provenance;
  - independent `validate_ops01_v5_package` candidate-root validation passes before any tracked copy, and producer-side self-assertions cannot substitute for that result;
  - final updater check, orientation check, evidence-path validation, mirror schema, index hash, LF, focused tests, full closed-rails CI, and release-sanity gate pass in v5-only state.
- Rollback: before OPS, a defective shared projector or independent v5 validator blocks OPS and is reverted through a focused PR-A follow-up or full PR-A revert. On OPS failure, tracked state is unchanged. After PR-C integration, reverting PR-C restores the coherent v4 packet and default v4 constants while retaining PR-A's independently tested shared projector, independent candidate validator, scanner, EPIC024 repair, and dormant runner. Never restore individual evidence files manually.
- Downstream effect: consumers receive an honest projection-only DDL result. Full semantic DDL parity remains unproven and unclaimed.
- Plan consequence: this CRD does not edit either plan. After IA approval, the separately authorized next-version Current Implementation Plan must allocate PR-A shared semantics/tooling and PR-C evidence migration, and be approved before implementation relies on `RSC-003` or `ADR-CANON-004`; `r1` remains the epic-scope baseline. PF09 status does not move.
- Documentation consequence: PF12 and PF14 permanent drainage under `ADR-CANON-004`; later PF09.6 wording clarification without status change; PF10 section 2.9 may separately record the approved ADR lineage, historical v4 qualification, and later verified facts. Neither PF10 nor permanent drainage gates implementation.
- Nonclaims: no full DDL semantic parity, no database migration, no provider API change, no bridge contract change, no `pg-bridge` code change, and no runtime BodyGraph behavior change.

### RSC-004 - Qualified one-attempt OPS-01R recapture

- Requested addition: one Glow-only operational recapture after PR-A is merged, subject first to separate bounded discovery authority and then to a separate exact live authorization.
- Canon effect: `NO CANON CHANGE`.
- Linked cause: `CAUSE-004`.
- Linked revisions: IA review v1.1 `REV-002`, `REV-003`, `REV-004`, and `REV-005`; IA review v1.2 `REV-001`.
- Reason required now: the approved one-attempt lane has no tolerance for unqualified source/import/write or command-admission behavior. V1.2 closed the preflight and discovery contracts but used `-I` alone from a writable detached source and relied on Git-clean posture that can hide ignored Python cache artifacts. The Railway execution contract remains `UNKNOWN PENDING DISCOVERY`, and the unverified external failed-run report remains non-causal.

#### Independently reviewable mandatory sub-decisions

| Sub-decision | Governing contract, observed risk, and consequence | Minimum necessary control | Dependency and owner | Validation | Rollback and documentation consequence |
| --- | --- | --- | --- | --- | --- |
| `RSC-004.A` Source and import qualification | OPS-01R requires exact immutable Glow source, but `-I` alone does not suppress bytecode writes and Git-clean checks can omit ignored cache residue. | Track `scripts/ops/hde_epic038_ops01r.py`; invoke preflight with exact ordered `[interpreter, "-I", "-B", runner, "--preflight"]`; pass no `PYTHON*` child variable; bind independent full-source before/after manifests, cache scans, and the exact sole write `control/preflight.json` in `hde_epic038.ops01r.preflight.v1`. | Approved Current Implementation Plan, then PR-A source and tests; Glow implementation owner. | Independent validation rejects every schema, argv, environment, path, identity, origin, source-manifest, cache-residue, staging-write, nondeterminism, count, canonical-byte, nonclaim, or zero-I/O mismatch. | Failure blocks discovery and live authorization and requires a reviewed source correction. PF10 may later record only the factual outcome. |
| `RSC-004.B` Railway contract discovery | Current permitted sources do not establish exact target IDs, CLI identity, supported explicit-target argv, nonlinked behavior, or injected target fields; the target probe also executes the tracked runner script from the writable detached source even though its closed contract performs no Glow-package import. | One separately PO-authorized discovery object binds the preflight-resolved CLI bytes, tracked discovery code, static read-only policy, unlinked working directory, at most six subprocesses, and exact ordered target-probe argv `[interpreter, "-I", "-B", runner, "--target-identity-probe"]`; the probe writes nothing and the producer writes only `control/discovery.json`. | Installed Railway CLI and Railway control-plane metadata; PO authorizes, operator executes, tracked discovery code validates. | Closed schema, manifest/hash agreement, exact Python argv/environment, source/cache/write proof, secret scan, exact command counts, unambiguous target resolution, explicit-target and nonlinked proof, and one exact identity field per target dimension. | Any missing, ambiguous, unsupported, unsafe, source-mutating, or write-set-violating result is `DISCOVERY_FAILURE`; no live authorization is requested. |
| `RSC-004.C` One launch and exact call graph | The task permits one attempt with no retry or fallback; the live child must not create ignored source residue or write outside explicit control/candidate paths. | PO live authorization binds source and baseline manifest, runner, validator, projector, interpreter, preflight, discovery, target, CLI, exact independent-validator/launcher/child/capture-validator `-I -B` argv, empty `PYTHON*` child environment, exact success/failure write sets, and complete expected-call vector. | PO authorization; operator invokes the independent validator and, only after PASS, the tracked launcher. | Independent live-authorization validation and redundant launcher checks reject isolation/write drift before marker or Railway. A second launch is impossible; one extra operation fails; successful evidence also requires unchanged source, no cache residue, exact write set, and field-by-field call equality. | A pre-marker mismatch blocks launch; marker creation, a started/indeterminate launch, or any later failure consumes authority, invalidates admission, and stops without retry. |
| `RSC-004.D` Candidate isolation and independent admission | OPS must not write tracked evidence, ignored source residue, or unlisted staging paths, and a producer cannot self-certify governed evidence. | Retain exact source/write proof in the result summary; write only the consumed marker and candidate descendants on success, or the marker, sanitized failure summary, and inadmissible candidate descendants on failure; run capture-time actual-tree validation before review and retain only self-contained proof for later permanent validation. | OPS owns temporary production; the capture-time and permanent validators own distinct read-only admission boundaries; PR-C alone owns later tracked integration. | While temporary state exists, capture-time validation recomputes exact argv/environment, full-source manifest equality, no cache residue, complete staging enumeration, candidate ledger, and semantic predicates and requires nested permanent packet PASS. PR-C/release later repeat only permanent retained-packet validation. | Any failure leaves no admissible packet and causes no tracked change. Permanent validation never claims to recapture absent temporary trees. Integration, QA, PF09 movement, acceptance, and closeout remain separate. |

#### `RSC-004.A` source and offline preflight contract

- Proposed CRD decision: the tracked runner derives `ROOT = Path(__file__).resolve().parents[2]` and prepends that exact path before importing Glow code. The source is a clean detached worktree at the exact reviewed PR-A merge commit. The preflight control record is a closed, independently validatable artifact, not narrative output.

- **Path and run identity contract.** One `run_id` is generated as `uuid.uuid4().hex` and must full-match `[0-9a-f]{32}`. Paths are derived only as follows: `staging_root = Path("/tmp/hde-epic038-ops01r") / run_id`; `source_root = staging_root / "source"`; `control_root = staging_root / "control"`; `working_directory = staging_root / "preflight-work"`; and `preflight_path = control_root / "preflight.json"`. The staging, source, control, and empty working directories exist before the preflight baseline snapshot; no alternate root or filename is valid. The exact sole producer argv is `[interpreter.lexical_path, "-I", "-B", components.runner.lexical_path, "--preflight"]` in that order. `control/preflight.json` is its only permitted file output; only its direct-parent `ctime_ns`/`mtime_ns` consequence defined below is additionally authorized. `preflight-work` remains empty, and candidate, failure-summary, source, cache, sibling, and tracked writes are forbidden.

- **Schema and exact top-level roster.** The schema literal is `hde_epic038.ops01r.preflight.v1`; `status` is exactly `PASS`. The exact top-level key set is `actual_external_io_counts`, `components`, `expected_call_counts`, `interpreter`, `module_origins`, `nonclaims`, `orchestration`, `preflight_identity_sha256`, `railway_executable`, `run`, `schema`, `source`, `source_write_validation`, and `status`. Unknown keys are rejected recursively at every listed object and entry.

- **`run` object.** Exact keys are `control_root`, `preflight_path`, `run_id`, `source_root`, `staging_root`, and `working_directory`; each value must equal the path-composition rule above.

- **`source` object.** Exact keys are `checkout_state`, `commit`, `repository`, `root`, `source_manifest_sha256`, and `worktree_state`. Required values are `repository="amthorn78/glow-hdengine-v2"`, `root=run.source_root`, `checkout_state="DETACHED"`, `worktree_state="clean"`, the exact PR-A merge commit, and the independently captured pre-import manifest identity defined below. Git status is corroborating evidence only and cannot substitute for the full manifest.

- **`components` object.** Exact keys are `projector`, `runner`, and `validator`. Each component has exactly `lexical_path`, `resolved_path`, and `sha256`. The exact lexical paths are `source_root/engine/db/ddl_identity_projection.py`, `source_root/scripts/ops/hde_epic038_ops01r.py`, and `source_root/tools/evidence/hde_epic038_ops01_v5.py`, respectively. Every resolved path is a regular file beneath `source_root`; each SHA-256 is lowercase over resolved bytes.

- **`interpreter` and module origins.** `interpreter` has exactly `bytecode_flag`, `bytecode_write_control`, `isolated_flag`, `lexical_path`, `preflight_argv`, `preflight_validator_argv`, `python_environment_names`, `resolved_path`, and `sha256`. Required values are `isolated_flag="-I"`, `bytecode_flag="-B"`, `bytecode_write_control="python_flag_-B"`, the exact five-token preflight argv above, `preflight_validator_argv=[interpreter.lexical_path, "-I", "-B", components.validator.lexical_path, "--validate-preflight", "--expected-identity-stdin", run.preflight_path]`, and `python_environment_names=[]`; the hash is over the resolved regular executable. Omission, duplication, substitution, or reordering of either flag or the expected-input selector is invalid. `PYTHONDONTWRITEBYTECODE`, `PYTHONPYCACHEPREFIX`, and every other case-folded `PYTHON*` name are absent, and no environment value may substitute for `-B`. `module_origins` is exactly four entries sorted by `module`; every entry has exactly `lexical_origin`, `module`, `resolved_origin`, and `sha256`. The exact module roster is `engine.db.ddl_identity_projection`, `scripts.db.capture_epic011_posture`, `scripts.ops.hde_epic038_ops01r`, and `tools.evidence.hde_epic038_ops01_v5`. Every origin resolves beneath `source_root`, and every hash is over resolved bytes.

- **Exact OPS-01R source-loading Python entry-point rule.** Every Python process in this bounded OPS-01R preflight, discovery, live-launch, and candidate-admission chain whose script resides beneath or imports from `source_root` must use the same authorization-bound interpreter followed immediately and exactly by `"-I"`, `"-B"`; must execute one bound regular script beneath `source_root` by lexical path; and must receive no environment name whose case-folded form begins `python`. The closed vectors are: preflight producer `interpreter.preflight_argv`; preflight validator `interpreter.preflight_validator_argv`; discovery producer and both discovery validators in `RSC-004.B policy.python_execution`; live authorization validator `RSC-004.C authorization.run.live_authorization_validator_argv`; live launcher `authorization.run.launcher_argv`; live child `authorization.run.child_argv`; capture-time validator `authorization.run.live_capture_validator_argv`; and permanent candidate validator `result_summary.execution.candidate_validator_argv`. No module-mode, console-script, shell, wrapper, environment-only suppression, or alternate Python entry point is authorized in that chain. Each enclosing preflight, discovery-authorization, live-authorization, or result-summary hash binds its applicable vector, and the independent validator reconstructs it before that process may cross its applicable Railway/provider boundary. This rule does not create a repository-wide Python-launch policy.

- **Exact external expected-identity transport for validator CLI modes.** Every validator CLI vector whose Python API requires an independently constructed `expected` object contains the literal `--expected-identity-stdin` exactly once at the position specified by that vector. The operator serializes only the applicable frozen dataclass as ASCII-only UTF-8 JSON with `ensure_ascii=True`, key-sorted keys, compact separators `(',', ':')`, no duplicate key, and exactly one trailing LF. The stream is nonempty, at most 16,384 bytes including LF, supplied only through a newly created anonymous OS pipe connected to file descriptor 0, and followed immediately by writer close/EOF. Before reading, the validator requires `os.isatty(0) == false` and `stat.S_ISFIFO(os.fstat(0).st_mode) == true`; regular-file redirection, named sidecar paths, sockets, terminals, inherited descriptors, and interactive input are invalid. The validator reads the stream once before validation, requires the exact dataclass key roster and string value types, recomputes the canonical bytes, and rejects any byte mismatch, extra byte, second JSON value, CR, BOM, non-ASCII byte, missing/extra/duplicate key, non-string value, unreadable/wrong-type stdin, or early/late EOF. No expected identity may come from argv values other than the literal selector and target path, an environment variable, a file or sidecar, the producer packet, a default, or interactive input. The operator constructs and reviews these bytes independently of the producer; the validator compares their fields to the canonical packet and actual state. Stdin bytes are not retained and create no file or hash cycle. The bounded transport applies exactly to preflight validation, discovery-authorization validation, discovery-result validation, live-authorization validation, live-capture validation, and standalone permanent candidate validation. Discovery dispatch is an in-process pure call and accepts no stdin channel. Later PR-C/release code may call the permanent Python API directly with the checked-in `OPS01_V5_EXPECTED` constant; it may not silently substitute a different CLI transport.

- **Common source/import/write-isolation object.** `source_write_validation` is reused without field drift for preflight, the discovery target probe/result, and the live child/result. Its exact keys are `authorized_directory_metadata_paths`, `authorized_exact_write_paths`, `authorized_recursive_write_roots`, `bytecode_write_control`, `manifest_algorithm`, `mode`, `observed_staging_changes`, `post_source_manifest_sha256`, `post_staging_manifest_sha256`, `pre_source_manifest_sha256`, `pre_staging_manifest`, `pre_staging_manifest_sha256`, `prohibited_cache_paths`, `python_argv`, `python_environment_names`, `self_bound_excluded_paths`, `self_bound_excluded_recursive_roots`, `source_root`, `source_tree_unchanged`, `staging_manifest_algorithm`, `staging_write_set_valid`, `status`, and `unauthorized_staging_paths`. The fixed values are `bytecode_write_control="python_flag_-B"`, `manifest_algorithm="hde_epic038.source_tree_manifest.v1"`, `staging_manifest_algorithm="hde_epic038.non_source_staging_manifest.v1"`, `python_environment_names=[]`, `source_tree_unchanged=true`, `staging_write_set_valid=true`, `status="PASS"`, `prohibited_cache_paths=[]`, and `unauthorized_staging_paths=[]`. For preflight, `mode="preflight"`, `python_argv=interpreter.preflight_argv`, `authorized_exact_write_paths=[run.preflight_path]`, `authorized_recursive_write_roots=[]`, `authorized_directory_metadata_paths=[run.control_root]`, `self_bound_excluded_paths=[run.preflight_path]`, and `self_bound_excluded_recursive_roots=[]`. The self-reporting preflight file is omitted only from the staging manifest to avoid hashing its own `post_staging_manifest_sha256`; its path/type, canonical bytes, and `preflight_identity_sha256` are independently revalidated and the file remains subject to the normalized write guard. Both source-manifest hashes equal `source.source_manifest_sha256` and the independently supplied expected identity.

- **Exact source-manifest algorithm and residue predicate.** Take the pre-snapshot immediately after the entry point establishes `source_root` and before any repository-local import or mode work; for preflight and live this precedes the first Glow import, and for the no-Glow-import target probe it precedes probe logic. Take the post-snapshot after the mode's work but before process exit. Recursively inspect `source_root` with `lstat` without following symlinks; include `.` and every descendant as a relative POSIX path. Each entry has exactly `ctime_ns`, `kind`, `mode`, `mtime_ns`, `path`, `sha256`, `size`, and `target`; allowed kinds are `directory`, `regular_file`, and `symlink`; inapplicable values are JSON null. Regular files alone bind byte SHA-256 and integer size; symlinks alone bind exact `readlink` target; directory and symlink `size` and every non-regular `sha256` are null; and all entries bind integer `st_ctime_ns`, integer `st_mtime_ns`, and `stat.S_IMODE`. Other filesystem kinds fail. Access time is intentionally excluded because reading/importing may change it. Sort by UTF-8 path bytes, serialize the entry list as ASCII-escaped, key-sorted compact JSON plus one LF, and hash those bytes. Independently scan both snapshots case-sensitively; any path component exactly `__pycache__` or regular filename ending `.pyc` fails even when the two manifests match. Pre-existing residue is not grandfathered.

- **Exact non-source staging baseline and delta.** The pre-staging snapshot is taken after all mode inputs, parent directories, and any required empty candidate root exist, but before the mode process starts. It recursively applies the same entry schema, `lstat`, metadata, sorting, canonicalization, and no-symlink-following rules as the source manifest to `staging_root` while excluding the complete `source_root` subtree, exact `self_bound_excluded_paths`, and equal-or-descendant paths under exact `self_bound_excluded_recursive_roots`. An exact-file exclusion is allowed only for the current authorization file, a self-reporting canonical result, or the non-governed failure summary; a recursive exclusion is allowed only for the precreated live candidate root. The current authorization is revalidated by its canonical authorization hash; preflight and discovery results are revalidated by their canonical self-hashes; the failure summary can never support PASS; and the candidate subtree is separately contained, enumerated, checksum-ledger-bound, and semantically validated on success. Every excluded path remains subject to the normalized write guard and exact authorized write set; no exclusion is a general ignored path. `pre_staging_manifest` retains the complete canonical entry list; `pre_staging_manifest_sha256` is independently computed before execution and binds those bytes; `post_staging_manifest_sha256` is recomputed from the actual post-mode tree under the same exclusions.
- **Non-circular self-report finalization.** When an exact preflight, discovery-result, or failure-summary file must report its own post-staging identity, the producer first creates one zero-length regular non-symlink placeholder at that exact authorized path through the normalized guard, after every other mode write but before the post snapshot. It computes `post_staging_manifest_sha256` while excluding that placeholder, finalizes the same file in place without rename, replacement, unlink, or alternate path, and independently recaptures the post manifest under identical exclusions. The recapture must equal the reported post hash; any parent metadata drift or placeholder substitution fails. Canonical preflight/discovery bytes and their self-hashes are then revalidated. A success result summary beneath the recursively excluded candidate root instead participates in the candidate's closed inventory, checksum ledger, external ledger hash, and semantic validation, so neither it nor the ledger is hashed through itself.
- `observed_staging_changes` is the complete path-sorted delta from the authenticated pre list to the actual post list under those exact exclusions. Every entry has exactly `change_kinds` and `path`; `change_kinds` is a sorted nonempty subset of `created`, `deleted`, `ctime_ns`, `kind`, `mode`, `mtime_ns`, `sha256`, `size`, and `target`. Created/deleted paths use only that change kind. Content or symlink-target mutation names the corresponding exact changed fields. A change is authorized only when its path equals one `authorized_exact_write_paths` member, is that member's listed parent-directory metadata-only change, or is equal to/beneath an `authorized_recursive_write_roots` member. Because directory `size` is null, `authorized_directory_metadata_paths` permits only `ctime_ns` and `mtime_ns` changes caused by an authorized direct-child create/replace/delete; it never permits directory content, kind, mode, target, or other-child drift. No non-excluded pre-existing input may be deleted or modified unless it is itself an authorized output path.
- **Exact staging-write predicate.** All runner-owned writes pass through one normalized-containment guard that rejects symlink ancestors and permits only the applicable exact path or recursive root. The independent validator authenticates the retained pre-staging list against the external or authorization-bound pre hash, recomputes the complete actual post tree and delta, revalidates every exact-file exclusion, separately validates every recursive candidate exclusion, requires every working directory to be empty where specified, and requires exact equality between its delta and `observed_staging_changes`. Every unauthorized path list must be empty. This is a bounded OPS-01R source/staging guard, not a host-wide filesystem-immutability claim or generalized sandbox.

- **Unexecuted Railway identity.** `railway_executable` has exactly `lexical_path`, `resolved_path`, and `sha256`. The symlink chain must resolve stably to one regular executable and the hash is over resolved bytes. The executable is not launched in preflight. CLI version, flags, target identifiers, and injected fields remain Unknown until `RSC-004.B`.

- **Exact call-vector contract.** `expected_call_counts` has exactly `bodygraph_reads`, `bridge_http_requests`, `bridge_provider_selections`, `direct_connection_attempts`, `direct_provider_selections`, `direct_sql_statements`, `fallbacks`, `logical_observations`, `retries`, and `vendor_requests`. Every value is a nonnegative integer, not a boolean. Exact invariants are `logical_observations=10`, `bodygraph_reads=2`, `direct_provider_selections=1`, `bridge_provider_selections=1`, `vendor_requests=0`, `retries=0`, and `fallbacks=0`; the other three are exact deterministic fake-run results, not ceilings. `direct_connection_attempts` increments immediately before each connector call attempt; `direct_sql_statements` increments immediately before each `execute`, `executemany`, or `copy` attempt; `bridge_http_requests` increments immediately before each bridge transport-send attempt. Counters advance before delegation even if delegation raises; retries and redirects are disabled.

- **Exact zero-I/O structure.** `actual_external_io_counts` has exactly `bridge_transport_delegations`, `candidate_writes`, `credential_reads`, `direct_connector_delegations`, `failure_summary_writes`, `provider_constructions`, `railway_subprocesses`, `sql_driver_delegations`, and `vendor_transport_delegations`; every value is integer zero.

- **Deterministic two-run structure.** `orchestration` has exactly `fake_boundary_mode`, `run_1`, `run_2`, `run_count`, and `vectors_equal`. Required literals are `fake_boundary_mode="count_before_fail_on_touch_delegate"`, `run_count=2`, and `vectors_equal=true`. `run_1` and `run_2` each have exactly `actual_external_io_counts` and `expected_call_counts`, using the exact rosters above. Both expected vectors equal each other and the top-level vector field by field; both actual objects equal the top-level actual object and are all zero. Fakes are injected only after the counted boundaries.

- **Nonclaims.** `nonclaims` is exactly the ordered list `no_railway_subprocess`, `no_credential_read`, `no_provider_construction`, `no_direct_connector_delegation`, `no_sql_driver_delegation`, `no_bridge_transport_delegation`, `no_vendor_transport_delegation`, `no_candidate_write`, `no_failure_summary_write`, `no_source_tree_write`, `no_bytecode_cache_write`, `no_unauthorized_staging_write`.

- **Canonical bytes and identity.** JSON is UTF-8 with `ensure_ascii=True`, key-sorted, compact separators `(',', ':')`, and exactly one trailing LF. `preflight_identity_sha256` is the lowercase SHA-256 of that canonical object with only `preflight_identity_sha256` omitted. The stored file is canonicalized again with the hash field included and one LF. No `expected_call_counts_sha256` key exists in this record.

- **Independent validator and API.** `tools/evidence/hde_epic038_ops01_v5.py` owns frozen `Ops01RPreflightExpectedIdentity` with exactly `source_commit`, `source_manifest_sha256`, `pre_staging_manifest_sha256`, `literal_staging_root`, `runner_sha256`, `validator_sha256`, `projector_sha256`, `interpreter_sha256`, `railway_executable_sha256`, and `preflight_identity_sha256`. Both manifest values are computed independently before the producer runs. It owns `validate_ops01r_preflight(path: Path, *, expected: Ops01RPreflightExpectedIdentity) -> Ops01V5ValidationResult`. The CLI entry point receives those independently reviewed exact bytes only through `interpreter.preflight_validator_argv` and the canonical expected-identity stdin contract. Validation is local and read-only; it authenticates the retained pre-staging manifest, recomputes the post-run source manifest and complete staging delta, compares the record's identities and observed delta to the external values and actual tree, and has no producer or write path. The result object remains exactly `valid` and `errors`, with unique non-secret errors sorted lexically.

- **Exact failure-code roster.** The only preflight codes are `PREFLIGHT_ACTUAL_IO_NONZERO`, `PREFLIGHT_BYTECODE_CONTROL_MISMATCH`, `PREFLIGHT_BYTES_NONCANONICAL`, `PREFLIGHT_COMPONENT_IDENTITY_MISMATCH`, `PREFLIGHT_EXPECTED_COUNTS_INVALID`, `PREFLIGHT_EXPECTED_IDENTITY_MISMATCH`, `PREFLIGHT_EXPECTED_INPUT_INVALID`, `PREFLIGHT_FILE_UNREADABLE`, `PREFLIGHT_IDENTITY_MISMATCH`, `PREFLIGHT_INTERPRETER_IDENTITY_MISMATCH`, `PREFLIGHT_JSON_INVALID`, `PREFLIGHT_MODULE_ORIGIN_MISMATCH`, `PREFLIGHT_NONCLAIMS_INVALID`, `PREFLIGHT_ORCHESTRATION_MISMATCH`, `PREFLIGHT_PATH_MISMATCH`, `PREFLIGHT_PYTHON_ARGV_MISMATCH`, `PREFLIGHT_PYTHON_ENVIRONMENT_INVALID`, `PREFLIGHT_RAILWAY_EXECUTABLE_IDENTITY_MISMATCH`, `PREFLIGHT_SCHEMA_INVALID`, `PREFLIGHT_SOURCE_IDENTITY_MISMATCH`, `PREFLIGHT_SOURCE_MANIFEST_MISMATCH`, `PREFLIGHT_SOURCE_RESIDUE_DETECTED`, `PREFLIGHT_STATUS_INVALID`, `PREFLIGHT_UNKNOWN_KEY`, and `PREFLIGHT_WRITE_SET_MISMATCH`. `PREFLIGHT_EXPECTED_INPUT_INVALID` covers every canonical-stdin transport failure before any source-dependent validation result can be accepted.

- **Binding rule.** Live authorization preserves the exact top-level `preflight_identity_sha256` key. That hash cryptographically binds the complete independently validated preflight record, including exact `-I -B` argv, empty Python environment-name roster, both source-manifest identities, authenticated pre-staging manifest/hash, actual post-staging hash/delta, cache-residue predicate, and preflight write set, because it covers every record member except itself. Discovery authorization has a `preflight` object with exactly `path`, `preflight_identity_sha256`, and `source_manifest_sha256`; all values must identify the independently validated PASS record. Result-summary top-level `preflight_identity_sha256` must equal the live-authorization value. Any omission, duplication, substitution, reordering, environment replacement, manifest/residue/write drift, or hash mismatch blocks discovery or live authorization before external I/O. The validated preflight vector must equal the later authorization vector field by field; no vector hash is serialized here.

#### `RSC-004.B` bounded Railway discovery gate

- Proposed CRD decision: after successful independent preflight validation, the PO may authorize one closed discovery object. No CLI subprocess may start until the complete authorization and static policy pass the independent validator.

- **Schemas and paths.** The authorization schema is `hde_epic038.ops01r.discovery_authorization.v1`; the policy schema is `hde_epic038.ops01r.discovery_policy.v1`. The same preflight `run_id` is used. Exact paths are `staging_root/control/discovery_authorization.json`, `staging_root/control/discovery.json`, and `staging_root/discovery-work`, where `staging_root` is the `RSC-004.A` path. No alternate authorization, result, or working-directory path is valid.

- **Authorization top-level roster.** Exact recursively closed keys are `discovery_authorization_sha256`, `discovery_entry_point`, `nonclaims`, `output_contract`, `policy`, `preflight`, `railway_cli`, `requested_target`, `run_id`, `schema`, `source`, `subprocess_limit`, `working_directory`, and `write_contract`.

- **Bound identities.** `source` has exactly `commit`, `repository`, `root`, `source_manifest_sha256`, and `state`, and must equal the validated preflight source with `state="DETACHED"`. `discovery_entry_point` has exactly `lexical_path`, `resolved_path`, and `sha256`; the lexical path is the bound runner `scripts/ops/hde_epic038_ops01r.py` beneath the source and its resolved bytes equal the preflight runner. `preflight` has exactly `path`, `preflight_identity_sha256`, and `source_manifest_sha256`, all identifying the independently validated PASS record. `railway_cli` has exactly `lexical_path`, `resolved_path`, and `sha256`, all equal to preflight.

- **Working directory, target, limit, output, and write set.** `working_directory` has exactly `linked_context_required`, `must_be_empty`, and `path`, with values false, true, and the exact `discovery-work` path. The validator requires a real empty directory with no Railway link, config, selection material, or post-run residue. `requested_target` has exactly `environment_name`, `project_name`, and `service_name`; the PO supplies exact non-secret names, while IDs remain discovery results. Every inventory must yield exactly one case-sensitive name match. `subprocess_limit` is integer `6`. `output_contract` has exactly `canonical_json`, `path`, `raw_cli_output_retained`, `schema`, and `trailing_lf`, with values true, the exact result path, false, `hde_epic038.ops01r.discovery.v1`, and true. The target-probe child may write nothing; the discovery producer may write only the exact result file plus its separately listed direct-parent `ctime_ns`/`mtime_ns` consequence. Pre-existing preflight and discovery-authorization inputs remain byte-identical.
- `write_contract` has exactly `authorized_directory_metadata_paths`, `authorized_exact_write_paths`, `authorized_recursive_write_roots`, `pre_staging_manifest`, `pre_staging_manifest_sha256`, `self_bound_excluded_paths`, `self_bound_excluded_recursive_roots`, and `source_root_writes_authorized`. Required values are the complete independently captured non-source staging baseline; `authorized_exact_write_paths=[output_contract.path]`; `authorized_recursive_write_roots=[]`; `authorized_directory_metadata_paths=[staging_root/control]`; `self_bound_excluded_paths=[staging_root/control/discovery_authorization.json, output_contract.path]` sorted by UTF-8 path bytes; `self_bound_excluded_recursive_roots=[]`; and `source_root_writes_authorized=false`. The authorization exclusion is revalidated through `discovery_authorization_sha256`; the result exclusion is revalidated through `discovery_identity_sha256`; no other path is excluded.
- **Non-circular discovery-authorization construction.** After every immutable input and directory exists, create one zero-length regular non-symlink placeholder at the exact discovery-authorization path; this placeholder conveys no authority. Capture `pre_staging_manifest` and its external hash under the exact exclusions above, construct the canonical authorization embedding that list/hash, and finalize the existing placeholder in place without rename, replacement, unlink, or alternate path. Recompute and verify `discovery_authorization_sha256`, then independently recapture the staging manifest under the same exclusions and require byte-for-byte equality with the embedded baseline before the PO authorizes the final exact bytes/hash. Any parent metadata drift, placeholder substitution, recapture mismatch, or authorization mutation invalidates the object before any CLI subprocess; the authorization file is never created or replaced after the authenticated baseline.

- **Authorization nonclaims.** `nonclaims` is exactly the ordered list `no_glow_import`, `no_provider_construction`, `no_db_call`, `no_bridge_call`, `no_vendor_call`, `no_deployment`, `no_restart`, `no_relink`, `no_selection_change`, `no_variable_mutation`, `no_tracked_write`.

- **Policy top-level roster.** `policy` has exactly `argv_rules`, `permitted_command_families`, `prohibited_command_families`, `python_execution`, `sanitization`, `schema`, `stages`, and `template_selection`. Its schema is the exact policy literal above.

- **Command families.** `permitted_command_families` is exactly the ordered list `cli_version`, `cli_help`, `project_inventory`, `environment_inventory`, `service_inventory`, `target_identity_probe`. `prohibited_command_families` is exactly `arbitrary_child_execution`, `database_connect`, `deployment`, `environment_mutation`, `linked_context_change`, `log_stream`, `project_mutation`, `redeployment`, `remote_shell`, `restart`, `selection_change`, `service_mutation`, `variable_read`, `variable_write`.

- **Argv rules.** `argv_rules` has exactly `allow_control_characters`, `allow_empty_tokens`, `allow_endpoint_or_secret_values`, `allow_shell`, `executable_token_source`, and `forbidden_casefolded_tokens`. The four booleans are false; source is `authorized_railway_cli_lexical_path`; and the exact forbidden token list is `add`, `connect`, `delete`, `deploy`, `disconnect`, `down`, `link`, `logs`, `redeploy`, `remove`, `restart`, `set`, `shell`, `ssh`, `unlink`, `unset`, `up`, `variables`. Comparison strips leading hyphens and casefolds. Every rendered argv begins with the exact bound Railway lexical path and executes with `shell=false`.

- **Python discovery and target-probe execution.** `python_execution` has exactly `authorization_validator_argv`, `bytecode_flag`, `bytecode_write_control`, `discovery_producer_argv`, `environment_name_rule`, `interpreter_argv_prefix`, `python_environment_names`, `result_validator_argv`, and `target_probe_argv`. Required values are `bytecode_flag="-B"`, `bytecode_write_control="python_flag_-B"`, `environment_name_rule="no_casefolded_python_prefix"`, and `python_environment_names=[]`. `interpreter_argv_prefix` is an exact three-string array: its first member equals the exact `lexical_path` from the independently validated preflight interpreter object, its second is `-I`, and its third is `-B`. `target_probe_argv` is an exact five-string array: those same first three members, followed by `discovery_entry_point.lexical_path` and `--target-identity-probe`. `discovery_producer_argv` is exactly that prefix followed by `discovery_entry_point.lexical_path`, `--discovery`, and the exact discovery-authorization path. `authorization_validator_argv` is exactly that prefix followed by the preflight-bound validator lexical path, `--validate-discovery-authorization`, `--expected-identity-stdin`, and the same authorization path. `result_validator_argv` is exactly that prefix followed by the same validator path, `--validate-discovery-result`, `--expected-identity-stdin`, `output_contract.path`, and the authorization path. Both validators receive the same independently reviewed `Ops01RDiscoveryAuthorizationExpectedIdentity` bytes only through the common canonical stdin contract; this proves the result still derives from the PO-authorized discovery object rather than a mutually rewritten authorization/result pair. Canonical authorization bytes contain every resolved literal string and the authorization self-hash therefore binds all four vectors. Omission, duplication, substitution, reordering, environment-only bytecode suppression, alternate expected-input transport, module/console-script invocation, and every other Python entry point are invalid.

- **Template selection.** `template_selection` has exactly `cardinality`, `help_match`, `tie_break`, and `version_match`, with values `exactly_one`, `every_required_help_token_present_as_case_sensitive_exact_token`, `none_fail_on_zero_or_multiple`, and `python_re_fullmatch_on_normalized_version`. Version output is strict UTF-8, CRLF/CR normalized to LF, ASCII-whitespace trimmed, and exactly one nonempty line. Help is strict UTF-8, newline-normalized, split on ASCII whitespace, and case-preserved. Raw version/help bytes are ephemeral and not retained.

- **Sanitization.** `sanitization` has exactly `allowed_value_classes`, `endpoint_values_retained`, `forbidden_field_name_regex`, `raw_stderr_retained`, `raw_stdout_retained`, and `secret_like_output_action`. Allowed classes are exactly `boolean`, `cli_version`, `identity_field_name`, `integer_count`, `sanitized_argv`, `schema_literal`, `sha256`, `target_id`, `target_name`; all three retention booleans are false; action is `fail`; and the regex is exactly `(?i)(secret|token|password|passwd|api[_-]?key|database_url|db_bridge_url|authorization|cookie)`. No environment value or CLI-auth value may be retained.

- **Six-stage matrix.** `policy.stages` contains exactly six entries in this order. Every entry has exactly `max_invocations`, `ordinal`, `predecessors`, `selection_mode`, `stage`, and `templates`; `max_invocations` is `1` for each.

| Ordinal | Stage | Predecessors | Selection mode |
| --- | --- | --- | --- |
| 1 | `cli_version` | empty list | `single` |
| 2 | `cli_help` | `cli_version` | `version` |
| 3 | `project_inventory` | `cli_version`, `cli_help` | `version_and_help` |
| 4 | `environment_inventory` | `cli_version`, `cli_help`, `project_inventory` | `version_and_help` |
| 5 | `service_inventory` | `cli_version`, `cli_help`, `project_inventory`, `environment_inventory` | `version_and_help` |
| 6 | `target_identity_probe` | `cli_version`, `cli_help`, `project_inventory`, `environment_inventory`, `service_inventory` | `version_and_help` |

- **Template-entry contract.** Each `templates` value is a nonempty PO-authorized list. Every template has exactly `argv`, `required_help_tokens`, `template_id`, and `version_regex`; IDs are unique per stage, regexes compile and use full-match. `single` has exactly one template with empty version regex and help-token list. `version` has an empty help-token list. `version_and_help` applies both selectors. Exactly one template may be eligible; zero or multiple matches stop without improvisation. Version-specific concrete templates are authorized input data, not implementation choices.

- **Structured argv tokens and child boundary.** `argv` contains arguments after the bound executable and is a nonempty list of descriptors. A literal descriptor has exactly `kind` and `value`, with `kind="literal"`. A binding descriptor has exactly `field`, `kind`, and `source_stage`, with `kind="prior_result"`. Bindings may name only a declared predecessor and these exact fields: `project_inventory` supplies `project_id` and `project_name`; `environment_inventory` supplies `environment_id` and `environment_name`; `service_inventory` supplies `service_id` and `service_name`. A Python-child descriptor has exactly `kind`, with `kind="python_child"`; it is permitted exactly once, only as the final descriptor of every `target_identity_probe` template, and in no other stage. No version/help raw value becomes a target argument.
- Rendering a target-probe template produces one exact full vector: `[railway_cli.lexical_path]`, followed by every literal/prior-result token before the terminal child descriptor, followed by the exact five strings in `policy.python_execution.target_probe_argv`. Any Railway child delimiter such as `--` is an ordinary explicit literal descriptor before `python_child`; no delimiter is assumed or injected. The prefix is every rendered token before the five-string child suffix, begins with the exact Railway executable, and contains the complete CLI subcommand, explicit-target tokens, and delimiter. Omitted, duplicated, substituted, reordered, environment-replaced, nonterminal, or different child tokens are `arbitrary_child_execution` and fail pre-dispatch validation.

- **Authorization identity.** `discovery_authorization_sha256` is the lowercase SHA-256 of canonical authorization JSON with only that field omitted. Canonicalization is ASCII-escaped, key-sorted, compact UTF-8 JSON plus exactly one LF. Stored authorization bytes include the hash field and one LF. The PO authorizes those exact bytes and hash. Unsupported or ambiguous templates fail; none may be invented or appended.

- **Independent APIs.** `tools/evidence/hde_epic038_ops01_v5.py` owns frozen `Ops01RDiscoveryAuthorizationExpectedIdentity` with exactly `discovery_authorization_sha256`, `discovery_entry_point_sha256`, `literal_staging_root`, `pre_staging_manifest_sha256`, `preflight_identity_sha256`, `railway_executable_sha256`, `source_commit`, and `source_manifest_sha256`. The staging value is independently captured before discovery. It owns `validate_ops01r_discovery_authorization(path: Path, *, expected: Ops01RDiscoveryAuthorizationExpectedIdentity) -> Ops01V5ValidationResult`, which is invoked only through `policy.python_execution.authorization_validator_argv`, receives `expected` only through the canonical expected-identity stdin contract, runs locally and read-only before any CLI call, and rejects every Python-policy, source-manifest, authenticated staging-baseline, or write-set mismatch. It also owns `validate_ops01r_discovery_dispatch(authorization_path: Path, *, stage: str, prior_results: object, rendered_argv: tuple[str, ...]) -> Ops01V5ValidationResult`; the discovery producer, invoked only through `policy.python_execution.discovery_producer_argv`, must obtain PASS from this pure independent function immediately before each subprocess, and the function reconstructs the full argv from validated policy and prior results. It owns `validate_ops01r_discovery_result(path: Path, *, authorization_path: Path, expected: Ops01RDiscoveryAuthorizationExpectedIdentity) -> Ops01V5ValidationResult`, invoked only through `policy.python_execution.result_validator_argv`, which receives the same independently reviewed expected bytes through canonical stdin, revalidates current authorization bytes against `expected.discovery_authorization_sha256`, proves output authorization-hash equality, derives selected templates, reconstructs every full argv, authenticates the retained pre-staging manifest, recomputes source and actual staging predicates, and checks manifest, counts, target, nonlinked context, identity, sanitization, nonclaims, canonical bytes, and result self-hash. The bound runner discovery mode is the sole result producer; the validator has no producer/write path. Every API invocation revalidates its own exact bound argv and empty Python-environment-name roster before doing source-dependent work.

- **Authorization failure codes.** The exact roster is `DISCOVERY_AUTH_BYTECODE_CONTROL_MISMATCH`, `DISCOVERY_AUTH_BYTES_NONCANONICAL`, `DISCOVERY_AUTH_CLI_IDENTITY_MISMATCH`, `DISCOVERY_AUTH_ENTRY_POINT_IDENTITY_MISMATCH`, `DISCOVERY_AUTH_EXPECTED_IDENTITY_MISMATCH`, `DISCOVERY_AUTH_EXPECTED_INPUT_INVALID`, `DISCOVERY_AUTH_FILE_UNREADABLE`, `DISCOVERY_AUTH_IDENTITY_MISMATCH`, `DISCOVERY_AUTH_JSON_INVALID`, `DISCOVERY_AUTH_NONCLAIMS_INVALID`, `DISCOVERY_AUTH_OUTPUT_CONTRACT_INVALID`, `DISCOVERY_AUTH_PATH_MISMATCH`, `DISCOVERY_AUTH_POLICY_INVALID`, `DISCOVERY_AUTH_PREFLIGHT_IDENTITY_MISMATCH`, `DISCOVERY_AUTH_PROHIBITED_COMMAND`, `DISCOVERY_AUTH_PYTHON_ARGV_MISMATCH`, `DISCOVERY_AUTH_PYTHON_ENVIRONMENT_INVALID`, `DISCOVERY_AUTH_REQUESTED_TARGET_INVALID`, `DISCOVERY_AUTH_SANITIZATION_INVALID`, `DISCOVERY_AUTH_SCHEMA_INVALID`, `DISCOVERY_AUTH_SOURCE_IDENTITY_MISMATCH`, `DISCOVERY_AUTH_SOURCE_MANIFEST_MISMATCH`, `DISCOVERY_AUTH_SUBPROCESS_LIMIT_INVALID`, `DISCOVERY_AUTH_UNKNOWN_KEY`, `DISCOVERY_AUTH_WORKING_DIRECTORY_INVALID`, and `DISCOVERY_AUTH_WRITE_SET_INVALID`. `DISCOVERY_AUTH_EXPECTED_INPUT_INVALID` covers every missing, malformed, noncanonical, oversized, trailing, alternate-channel, or wrong-roster expected-input stream before any CLI call.
- `validate_ops01r_discovery_dispatch` uses `DISCOVERY_AUTH_PYTHON_ARGV_MISMATCH` for any target-probe suffix or child-boundary drift and `DISCOVERY_AUTH_PROHIBITED_COMMAND` for any other unauthorized rendered token. Either code is emitted before that stage's Railway subprocess. Tests inject renderer drift after authorization PASS and prove the target-probe Railway call count remains zero.

- **Result failure codes.** The exact roster is `DISCOVERY_RESULT_ARGV_MISMATCH`, `DISCOVERY_RESULT_AUTHORIZATION_MISMATCH`, `DISCOVERY_RESULT_BYTECODE_CONTROL_MISMATCH`, `DISCOVERY_RESULT_BYTES_NONCANONICAL`, `DISCOVERY_RESULT_CLI_IDENTITY_MISMATCH`, `DISCOVERY_RESULT_COUNT_MISMATCH`, `DISCOVERY_RESULT_EXPECTED_INPUT_INVALID`, `DISCOVERY_RESULT_FILE_UNREADABLE`, `DISCOVERY_RESULT_IDENTITY_CONTRACT_INVALID`, `DISCOVERY_RESULT_IDENTITY_MISMATCH`, `DISCOVERY_RESULT_JSON_INVALID`, `DISCOVERY_RESULT_LINKED_CONTEXT_DETECTED`, `DISCOVERY_RESULT_NONCLAIMS_INVALID`, `DISCOVERY_RESULT_PYTHON_ARGV_MISMATCH`, `DISCOVERY_RESULT_PYTHON_ENVIRONMENT_INVALID`, `DISCOVERY_RESULT_SCHEMA_INVALID`, `DISCOVERY_RESULT_SECRET_LIKE_OUTPUT`, `DISCOVERY_RESULT_SOURCE_MANIFEST_MISMATCH`, `DISCOVERY_RESULT_SOURCE_RESIDUE_DETECTED`, `DISCOVERY_RESULT_STAGE_COUNT_INVALID`, `DISCOVERY_RESULT_STAGE_FAILED`, `DISCOVERY_RESULT_STAGE_ORDER_INVALID`, `DISCOVERY_RESULT_TARGET_AMBIGUOUS`, `DISCOVERY_RESULT_TEMPLATE_SELECTION_AMBIGUOUS`, `DISCOVERY_RESULT_TEMPLATE_SELECTION_NONE`, `DISCOVERY_RESULT_UNKNOWN_KEY`, and `DISCOVERY_RESULT_WRITE_SET_MISMATCH`. `DISCOVERY_RESULT_EXPECTED_INPUT_INVALID` covers the canonical stdin transport; a valid input whose authorization hash differs uses `DISCOVERY_RESULT_AUTHORIZATION_MISMATCH`. Errors are unique, lexically sorted, and non-secret. Any code yields sanitized overall `DISCOVERY_FAILURE` and never live authority.

- **Successful discovery output.** The sole result producer emits canonical `hde_epic038.ops01r.discovery.v1` JSON with exactly `schema`, `status`, `discovery_run_id`, `discovery_authorization_sha256`, `command_manifest`, `command_manifest_sha256`, `railway_cli`, `target`, `run_contract`, `identity_contract`, `counts`, `nonclaims`, `source_write_validation`, and `discovery_identity_sha256`. `status` is `PASS`; the authorization hash equals the independently validated input; any failed, interrupted, unauthorized, incomplete, source-mutating, residue-bearing, or write-set-violating discovery is invalid.

- `command_manifest` is the complete ordered list of the exact sanitized full JSON string argv arrays actually executed, one array per selected stage in stage order. Each array begins with the exact bound Railway executable lexical path and contains only the deterministically rendered authorized template tokens; the target-probe entry is exactly `run_contract.argv_prefix + run_contract.python_execution.target_probe_argv`, split at `run_contract.child_argv_start_index`. There is at most one command per named stage and at most six total. `command_manifest_sha256` is the lowercase SHA-256 of the manifest's ASCII-escaped, key-sorted, compact UTF-8 canonical JSON bytes plus exactly one LF; `counts.discovery_subprocesses` equals the manifest length; no unrecorded invocation is permitted. `railway_cli` has exactly `path`, `resolved_path`, `sha256`, and `version`. `target` has exactly `project_name`, `project_id`, `environment_name`, `environment_id`, `service_name`, and `service_id`.

- `run_contract` has exactly `argv_prefix`, `child_argv_start_index`, `child_environment_contract`, `linked_context_required`, `python_execution`, and `target_dimensions`. `argv_prefix` is the exact sanitized full Railway outer prefix derived from the selected target-probe template, begins with the exact Railway executable, contains every CLI subcommand/target/delimiter token, and excludes the five child strings. `child_argv_start_index` is the integer length of `argv_prefix`; `linked_context_required` is false; `python_execution` equals the authorization policy object exactly; `target_dimensions` is exactly `project`, `environment`, `service` in the order proven by discovery. This CRD does not assume `--no-local` or `--`; any required literal is policy data, and failure to prove nonlinked execution is fatal. `identity_contract` is a sorted closed list whose entries have exactly `field_name`, `target_dimension`, `value_kind`, and `expected_value`, with at least one unambiguous field for every target dimension. `child_environment_contract` is a sorted closed list whose entries have exactly `name`, `source`, and `value_policy`; endpoints are presence-only, CLI-auth variables remain launcher-only, and no case-folded name beginning `python` is present.

- `source_write_validation` uses the common exact object in `RSC-004.A` with `mode="discovery"`, `python_argv=run_contract.python_execution.target_probe_argv`, and every baseline/write member equal to validated `authorization.write_contract`: the sole exact output is `authorization.output_contract.path`, the sole allowed parent-metadata path is `staging_root/control`, recursive write and exclusion roots are empty, and the exact-file exclusions are the canonical discovery authorization and self-reporting discovery result. Its pre/post source hashes equal the independently validated preflight source-manifest identity; its retained pre-staging list/hash equal the independently supplied authorization expectation; the target-probe child writes nothing; the discovery producer writes only `control/discovery.json`; the result bytes and `discovery_identity_sha256` validate independently of the staging manifest; `discovery-work` is empty; preflight and discovery-authorization bytes are unchanged; and both prohibited/unauthorized lists are empty.

- `counts` has exactly `command_manifest_entries`, `discovery_subprocesses`, `provider_constructions`, `db_connections`, `direct_sql_statements`, `bridge_http_requests`, and `vendor_requests`. The first two equal manifest length and are at most six; every other count is zero. Result `nonclaims` equals the authorization roster. `discovery_identity_sha256` hashes the canonical result with only itself omitted. Unknown keys are recursively rejected. Live authorization embeds the complete validated discovery result; its embedded authorization hash cryptographically binds the complete validated policy input.

#### `RSC-004.C` authorization and live equality contract

- The PO live authorization is a closed canonical object and SHA-256. It embeds the complete validated discovery result, which includes the independently validated `discovery_authorization_sha256` and therefore binds the closed policy input. It also binds repository identity; detached source commit/root/state and full-manifest identity; unique run, control, and candidate roots; runner, independent-validator, shared-projector, and interpreter identities; the complete validated preflight record by `preflight_identity_sha256`; discovery identity; CLI identity; target; exact run argv prefix; exact injected-identity contract; exact `-I -B` live-child argv and empty `PYTHON*` environment-name roster; success/failure write sets; launch limit `1`; the complete ten-field `expected_call_counts`; and zero tracked writes, vendor requests, retries, and fallbacks.
- The authorization object schema is `hde_epic038.ops01r.authorization.v1` and its exact top-level keys are `schema`, `source`, `run`, `runner`, `validator`, `projector`, `interpreter`, `preflight_identity_sha256`, `discovery`, `launch_limit`, `expected_call_counts`, `tracked_writes_authorized`, and `write_contract`. `source` has exactly `repository`, `commit`, `root`, `source_manifest_sha256`, and `state`; the manifest identity equals validated preflight and discovery. `run` has exactly `authorization_path`, `candidate_root`, `child_argv`, `launcher_argv`, `live_authorization_validator_argv`, `live_capture_validator_argv`, `run_id`, and `staging_root`; `authorization_path` is exactly `staging_root/control/live_authorization.json`; `candidate_root` is exactly the `candidate` child beneath `staging_root`; `live_authorization_validator_argv` is exactly `[interpreter.path, "-I", "-B", validator.path, "--validate-live-authorization", "--expected-identity-stdin", authorization_path]`; `launcher_argv` is exactly `[interpreter.path, "-I", "-B", runner.path, "--live-launch", authorization_path]`; `child_argv` is exactly `[interpreter.path, "-I", "-B", runner.path, "--live-child"]`; and `live_capture_validator_argv` is exactly `[interpreter.path, "-I", "-B", validator.path, "--validate-live-capture", "--expected-identity-stdin", staging_root]`. Each validator vector receives only its exact frozen expected identity through canonical stdin. Each of `runner`, `validator`, and `projector` has exactly `path` and `sha256`. `interpreter` has exactly `bytecode_flag`, `bytecode_write_control`, `isolated_flag`, `path`, `python_environment_names`, `resolved_path`, and `sha256`, with `isolated_flag="-I"`, `bytecode_flag="-B"`, `bytecode_write_control="python_flag_-B"`, and `python_environment_names=[]`; both validators, launcher, and child receive that empty Python-environment-name roster. `launch_limit` is integer `1`; `tracked_writes_authorized` is false. `preflight_identity_sha256` must equal the independent PASS record; `discovery` must equal the independent PASS result and its authorization hash must equal the validated discovery-authorization object. Unknown keys are rejected at every listed object. The authorization SHA-256 is computed over ASCII-escaped, key-sorted, compact UTF-8 JSON plus exactly one LF. It contains no endpoint or CLI-auth value and no `expected_call_counts_sha256` key.
- `write_contract` has exactly `consumed_marker_path`, `failure_authorized_directory_metadata_paths`, `failure_authorized_exact_paths`, `failure_authorized_recursive_write_roots`, `failure_summary_path`, `pre_staging_manifest`, `pre_staging_manifest_sha256`, `self_bound_excluded_paths`, `self_bound_excluded_recursive_roots`, `source_root_writes_authorized`, `success_authorized_directory_metadata_paths`, `success_authorized_exact_paths`, and `success_authorized_recursive_write_roots`. Required paths are `consumed_marker_path=staging_root/control/live_authority_consumed.json` and `failure_summary_path=staging_root/control/failure.json`; success exact paths contain only the consumed marker and success recursive roots contain only `candidate_root`; failure exact paths contain only the consumed marker and failure summary and failure recursive roots contain only `candidate_root`; both directory-metadata lists contain only `staging_root/control`; `self_bound_excluded_paths=[run.authorization_path, failure_summary_path]` sorted by UTF-8 path bytes; `self_bound_excluded_recursive_roots=[run.candidate_root]`; and `source_root_writes_authorized=false`. The excluded live authorization is revalidated through `authorization_sha256`; any failure summary is non-governed, independently constrained to its exact path/canonical sanitized form, and can never support PASS; and the candidate subtree is independently contained, enumerated, ledger-bound, and semantically validated on success. Preflight, discovery authorization/result, and every other non-excluded pre-existing input remain byte-identical.
- **Non-circular live-authorization construction.** After every immutable input, parent directory, and the verified real empty non-symlink candidate root exists, create one zero-length regular non-symlink placeholder at `run.authorization_path`; the placeholder is not live authority. Capture the external live `pre_staging_manifest` under the exact file/root exclusions above, construct the canonical live authorization embedding that list/hash, and finalize the same placeholder in place without rename, replacement, unlink, or alternate path. Recompute `authorization_sha256`, independently recapture the staging manifest under the same exclusions, and require byte-for-byte equality with the embedded baseline; only then freeze `Ops01V5ExpectedIdentity.live_pre_staging_manifest_sha256` and permit the PO to authorize those final exact bytes/hash. Any parent metadata drift, candidate non-emptiness, placeholder substitution, recapture mismatch, or later authorization mutation invalidates the object before marker, Railway, credential, or provider activity.
- No placeholder identity or authorization content, guessed UUID, assumed flag, or hard-coded injected field is valid. The only permitted placeholders are the exact zero-length regular non-symlink filesystem files required by the non-circular finalization rules in `RSC-004.A` through `.C`; they convey no identity, authority, PASS, or executable value and must be finalized and recaptured exactly as specified.
- **Independent live-authorization validator.** `tools/evidence/hde_epic038_ops01_v5.py` owns frozen `Ops01RLiveAuthorizationExpectedIdentity` with exactly `authorization_sha256`, `discovery_identity_sha256`, `interpreter_sha256`, `live_pre_staging_manifest_sha256`, `literal_staging_root`, `preflight_identity_sha256`, `projector_sha256`, `railway_executable_sha256`, `runner_sha256`, `source_commit`, `source_manifest_sha256`, and `validator_sha256`, plus pure API `validate_ops01r_live_authorization(path: Path, *, expected: Ops01RLiveAuthorizationExpectedIdentity) -> Ops01V5ValidationResult`. The operator constructs `expected` from independently reviewed facts and invokes the API only through `authorization.run.live_authorization_validator_argv`, supplying those exact canonical bytes on stdin under the common transport contract; the entry point validates its own exact `-I -B` argv/empty Python environment, canonical expected input, canonical authorization bytes/hash/schema, placeholder-finalization recapture, actual prelaunch source/cache/staging state, every bound component/preflight/discovery/CLI identity, expected-call equality, child/launcher/capture-validator vectors, write sets, and one-launch posture, and writes nothing. PASS is a mandatory operational gate before the operator may start the launcher; no new receipt artifact is created, and the launcher performs the redundant local rechecks below. Any failure uses the exact `OPS01_AUTH_*` code roster and stops before authority consumption.
- After independent live-authorization PASS and before consuming authority, the runner rechecks the exact source commit and clean detached state, recomputes the complete source manifest and requires equality to the independently reviewed, preflight, discovery, and authorization values, rejects any `__pycache__` or `.pyc` residue, then re-resolves and rehashes runner, validator, projector, interpreter lexical/resolved paths and bytes, preflight, discovery, authorization, and CLI identities. It validates the exact `-I -B` validator/launcher/child argv, empty `PYTHON*` roster, normalized write contract, and staging inputs. Any mismatch stops before Railway, provider, launch, or marker creation.
- After every local check passes and immediately before the only Railway subprocess, the runner atomically creates a consumed marker bound to run ID and authorization hash. Successful marker creation consumes authority. An existing, ambiguous, or unreadable marker blocks launch. Any subprocess start, indeterminate launch state, OS launch error after marker creation, or child outcome leaves authority consumed. The marker is never deleted to restore authority.
- The launcher itself starts only through the authorization-bound `run.launcher_argv`, revalidates that vector and its empty Python-environment-name roster, then uses the exact discovered CLI and run contract, appends only the exact authorized five-token live child argv, and uses neither shell execution nor linked-context fallback. Omission, duplication, substitution, reordering, module/console-script substitution, or environment-only replacement of `-I` or `-B` in either vector is fatal before the Railway/provider boundary.
- Under exact `-I -B` execution, the child derives and prepends the same resolved runner root, verifies the authorization-bound interpreter and repository-local module origins, then validates every discovered mandatory identity field against the authorized target. All checks occur before credential reads or provider construction. Any missing or mismatched identity fails with zero DB, bridge, and vendor calls.
- The child uses exactly the authorization-bound `child_environment_contract`. The contract must include the two required DB endpoint names, discovered target-identity fields, exact closed read-only rails, and only explicitly enumerated locale/TLS/proxy names with closed or presence-only value policies. Caller Railway authentication, vendor, birth-input, provider-force, permissive production, every unlisted variable, and every variable whose name case-folds to a `python` prefix do not enter the capture environment. `PYTHONDONTWRITEBYTECODE` or `PYTHONPYCACHEPREFIX` cannot replace the required `-B` token.
- Before authorization is accepted, its complete `expected_call_counts` must equal the independently validated preflight vector field by field. After that point, the authorization vector is the sole authoritative serialized expected vector. `expected_call_counts_sha256` is derived only as `SHA256(CANONICAL_LF(authorization.expected_call_counts))`; it is not serialized in preflight, authorization, or result summary.
- Each call wrapper computes `attempted_next = actual + 1` before delegation and rejects when `attempted_next > authorization.expected_call_counts[field]`. A success candidate is valid only when `actual_call_counts == authorization.expected_call_counts` field by field. A failure may retain only a strict prefix as sanitized failure information and can never satisfy admission.
- The former `direct_connection_attempt_ceiling`, `direct_sql_statement_ceiling`, and `bridge_http_request_ceiling` keys and every less-than-or-equal PASS predicate are removed.

- **Prelaunch failure codes.** The exact isolation/write roster is `OPS01_AUTH_BYTECODE_CONTROL_MISMATCH`, `OPS01_AUTH_PYTHON_ARGV_MISMATCH`, `OPS01_AUTH_PYTHON_ENVIRONMENT_INVALID`, `OPS01_AUTH_SOURCE_MANIFEST_MISMATCH`, and `OPS01_AUTH_WRITE_SET_INVALID`. The additional exact transport code is `OPS01_AUTH_EXPECTED_INPUT_INVALID`. Each is unique and non-secret. A missing, malformed, noncanonical, oversized, trailing, alternate-channel, or wrong-roster expected stream uses the transport code; every listed code is raised before marker creation, Railway subprocess, credential read, or provider construction.

#### `RSC-004.D` candidate admission and failure posture

- Success writes are limited to the exact consumed marker plus descendants of the unique temporary candidate root and only the listed direct-parent directory-metadata consequences; failure writes are limited to that marker, exact sanitized failure summary, inadmissible candidate descendants, and only the listed direct-parent consequences. The source worktree remains clean only as corroboration: admission also requires independently recomputed full-source manifest equality and empty cache-residue results.
- The result summary retains the complete authorization object, preflight and discovery hashes, exact invocation provenance, `expected_call_counts`, `actual_call_counts`, provider-selection provenance, existing v5 DDL and BodyGraph nonclaims, and `execution.source_write_validation`. The live object uses the exact common roster from `RSC-004.A` with `mode="live"`, `python_argv=authorization.run.child_argv`, the applicable authorization success write set, authenticated pre-staging list/hash, exact-file exclusions, and candidate-root recursive exclusion from `authorization.write_contract`, pre/post source hashes equal to `authorization.source.source_manifest_sha256`, independently recomputed post-staging hash/delta over every non-excluded staging path, independent closed-inventory/checksum/semantic validation of the excluded candidate subtree, and empty prohibited-cache and unauthorized-staging lists. Its expected vector must equal the embedded authorization vector field by field, and its actual vector must equal that same authorization vector for PASS. On failure, the same non-governed diagnostic object uses the exact failure write set, validates containment outside the excluded failure/candidate outputs, and remains inadmissible.
- After the runner exits and while the ephemeral source/control tree still exists, the operator supplies `Ops01V5ExpectedIdentity` from independently reviewed facts, including independent pre/post staging and source-manifest identities, exact candidate-ledger hash, and independently derived `expected_call_counts_sha256`, then invokes `authorization.run.live_capture_validator_argv`. Capture-time validation recomputes the actual source manifest and complete non-candidate staging layout, rejects any `__pycache__`, `.pyc`, symlink escape, unlisted create/modify/delete/metadata change, or source-manifest drift, validates the excluded candidate subtree, recomputes the expected-vector hash only from `result_summary.authorization.expected_call_counts`, rejects any serialized vector-hash key, requires summary-expected equality and terminal actual equality, and reconstructs target, CLI, source, and invocation identity from retained governed content. The nested permanent packet validator must also PASS. A producer self-check cannot satisfy admission. Later PR-C and release sanity repeat only permanent retained-packet validation and expressly do not claim ephemeral-tree recapture.
- On any failure or interruption, no success packet is admitted and no second or recovery launch is allowed. If outcome reconstruction is incomplete, report only sanitized `OPS_FAILURE` and stop.
- Discovery artifacts, consumed markers, and failure summaries are temporary control material, not governed success evidence or integration inputs. PR-C may integrate only an independently valid success candidate under separate authority.

- **Focused isolation, residue, and write-set tests.** Positive tests execute every exact source-loading vector: preflight producer/validator, discovery authorization validator/producer/result validator, target probe, live-authorization validator, live launcher/child, live-capture validator, and permanent candidate validator. Mutation tests remove, duplicate, substitute, and reorder `-I` or `-B`; remove, duplicate, move, or replace `--expected-identity-stdin`; substitute module, console-script, shell, or wrapper entry points; attempt environment-only suppression; seed `PYTHONDONTWRITEBYTECODE`, `PYTHONPYCACHEPREFIX`, `PYTHONPATH`, and arbitrary case variants of `PYTHON*`; recompute producer self-hashes after policy/argv mutation; and force disagreements among discovery policy, rendered target-probe argv, command manifest, live authorization, every validator vector, `commands.txt`, result summary, and candidate-validator argv. Expected-input tests cover empty, TTY, unreadable, oversized, non-ASCII, BOM, CRLF, missing LF, extra bytes, second JSON value, duplicate/missing/extra keys, wrong types, noncanonical ordering/spacing/escaping, valid-but-wrong identity values, file/env/argv fallback attempts, and exact canonical PASS for every applicable expected dataclass; discovery-result tests also prove a mutually rewritten authorization/result pair fails against the independently reviewed authorization identity. Import/execution tests cover the exact four preflight modules, the no-Glow-import target-probe execution, live-child imports, and every supporting source-loading process and prove that no `__pycache__` component or `.pyc` file exists before or after any phase.
- Filesystem mutation tests create pre-existing and new cache residue; add or modify ignored and ordinary source files; delete, chmod, touch, or replace a source entry or symlink; forge or alter a retained pre-staging list/hash; delete or modify a pre-existing staging input; substitute, rename, replace, or mutate either authorization placeholder; force parent metadata drift between baseline and in-place authorization finalization; tamper with any exact-file exclusion; escape or leave unledgered content under the recursively excluded candidate root; add files to `preflight-work`, `discovery-work`, `control`, staging siblings, or source; create an unlisted parent-directory metadata change; and attempt a symlink escape. Mode tests authenticate the non-circular pre-staging baseline before accepting the post delta and prove preflight writes only `control/preflight.json`, the target-probe child writes nothing, the discovery producer writes only `control/discovery.json`, live success writes only the consumed marker and candidate descendants, and live failure writes only the marker, sanitized failure summary, and inadmissible candidate descendants; self-reporting outputs validate through their canonical identities, the candidate validates through its closed inventory/ledger/semantic gate, and only the explicitly listed direct-parent `ctime_ns`/`mtime_ns` consequences of authorized file operations are accepted. Spies prove every preflight or discovery-authorization mismatch occurs with zero Railway subprocesses, credential reads, provider constructions, DB calls, bridge calls, or vendor calls; renderer/target-probe drift fails the immediate pre-dispatch gate with zero target-probe Railway calls; discovery-result failure blocks live authorization; pre-marker live failure performs no Railway/provider call; and post-marker failure consumes authority without retry.
- **Non-circular hash-binding chain.** Each self-reporting output is excluded from the staging manifest that its own bytes report, while its canonical self-hash, exact authorized path/type, and parent-directory delta are validated independently; the live candidate root is excluded from that staging manifest only because its complete subtree is independently contained, inventoried, ledger-bound, and semantically validated. `preflight_identity_sha256` binds the preflight producer/validator interpreter vectors, full argv/environment, source/write object, and source-manifest identities. `discovery_authorization_sha256` binds the validated preflight/source identity, authenticated placeholder-derived staging baseline, discovery producer/validator vectors, and exact target-probe policy; `command_manifest_sha256` and `discovery_identity_sha256` bind the rendered/executed target-probe argv and discovery source/write result without hashing the result through itself. The live `authorization_sha256` binds the complete discovery result, exact live authorization-validator/launcher/child/capture-validator argv and environment, placeholder-derived authenticated baseline manifest, and write contract. Capture-time validation freezes the external `Ops01V5ExpectedIdentity.live_post_staging_manifest_sha256` from the actual ephemeral tree; `commands_sha256`, result-summary canonical bytes including exact permanent candidate-validator argv, primary checksums, external candidate-ledger identity, and all three external manifest identities then bind the retained result without a result-summary or ledger self-cycle. Permanent candidate/PR-C/release validation checks those retained identities and semantics but does not recapture temporary state. No producer-supplied isolation or baseline hash can replace any enclosing or external identity.

#### Removed mandatory mechanisms

The v1.0 multi-state attempt journal, child-outcome protocol, launch-manifest protocol, governed negative-receipt schema, file-and-directory `fsync` choreography, `/proc` process discovery, recovery launcher, output-cap subsystem, installed-distribution manifest, repository-wide code-contract map, and generalized four-mode recovery state machine are removed from implementation obligations because they are not necessary to resolve the approved one-attempt recapture.

`Follow-up (out of scope):` a reusable multi-run OPS execution platform, crash-recovery framework, generalized durable journal protocol, or generalized operational receipt architecture requires a separate causal case and authority.

- Exact operational locus: repository identity remains `amthorn78/glow-hdengine-v2`. For a runtime-generated `run_id`, the detached source path is formed by joining `/tmp/hde-epic038-ops01r`, `run_id`, and `source`; the runner is `scripts/ops/hde_epic038_ops01r.py` beneath that source; and the success candidate path is formed by joining `/tmp/hde-epic038-ops01r`, the same `run_id`, and `candidate`. The run ID and later hashes are derived only after the responsible source or record exists.
- Candidate admission: require the exact success inventory in `RSC-003`, canonical serialization, checksum ledger, secret/raw scan, provider-selection snapshots, exact `-I -B` and empty-Python-environment provenance for all three modes, independent full-source manifest equality, empty cache-residue and unauthorized-write lists, one-attempt provenance, DDL comparison contract, false full-parity claim, nonclaims, result-summary agreement, and independent `validate_ops01r_live_capture` PASS with nested `validate_ops01_v5_package` PASS while the temporary source/staging trees still exist. Preserve the admitted candidate for review but do not copy, index, or merge it during OPS. Later review repeats only permanent packet validation and does not claim temporary-tree recapture.
- Plan consequence: this CRD does not edit either plan. After IA approval, the separately authorized next-version Current Implementation Plan must encode PR-A merge -> exact `-I -B` offline preflight and source/write PASS -> validated discovery authorization/policy -> bounded discovery and target-probe source/write PASS -> discovery-result validation -> exact PO live authorization and prelaunch source/write PASS -> one launch -> independent candidate source/write admission -> later PR-C review, and must be approved before implementation relies on `RSC-004`. `r1` remains the epic-scope baseline.
- Documentation consequence: PF10 may later receive factual append-only discovery/preflight hashes, authorization identity, expected/actual counts, outcome, and nonclaims. PF10 recording is not an implementation prerequisite or authority source.
- Nonclaims: no read-only mount, cache-redirection directory, environment-variable substitute, host-wide immutability claim, generalized filesystem sandbox, extra Railway subprocess, `pg-bridge` repository/service/deployment work, SQL write, migration, schema/grant/role change, vendor call, deployment, restart, relink, Railway selection or variable mutation, tracked evidence integration, QA, PF09 movement, token satisfaction, acceptance, merge readiness, or epic closeout.
### RSC-005 - Atomic candidate integration and v5-only release binding

- Requested addition: integrate a reviewed successful OPS-01R candidate in a separate PR-C and converge all governed companions.
- Canon effect: `NO CANON CHANGE` beyond the bounded `ADR-CANON-004` contract adopted by `RSC-003`.
- Linked cause: `CAUSE-005`.
- Reason required now: live candidate evidence has no effect until tracked bytes, validator constants, proofs, index, mirror, and sanity binding agree.
- Exact existing implementation loci:
  - `audit/ops/hde-epic038/ops-01/` for retained primaries;
  - `tools/evidence/run_sanity_pipeline.py` for v5-only constants and validation;
  - `tools/evidence/update_evidence_index.py` for primary inventory, stable artifact keys, and updater-owned companions;
  - `tools/evidence/orientation_demo.py` and existing evidence/path/LF checks for orientation and closure validation.
- Proposed CRD decision:
  - require a successful, capture-time-admitted, reviewed candidate with unchanged authorization, invocation, externally reviewed candidate-ledger hash, source-commit, runner, validator, projector, preflight, discovery, and expected-call identities before PR-C is created; the earlier capture-time PASS and nested permanent PASS are prerequisite reviewed facts, while PR-C repeats only permanent retained-packet validation;
  - require the candidate's exact `repository.head` source commit to be an ancestor of the proposed PR-C base. Before any PR-C edit, require the base copies of `tools/evidence/hde_epic038_ops01_v5.py` and `engine/db/ddl_identity_projection.py` to match the independently reviewed validator and projector hashes bound by authorization. Unrelated main advancement is allowed; a changed validator, projector, or incompatible evidence-admission surface blocks integration and requires a separately reviewed compatibility decision. It does not authorize moving main backward or automatically authorize recapture;
  - immediately before validation and copy, hash the untouched `checksums.sha256` bytes and require equality with externally reviewed `candidate_ledger_sha256`; then run independent `validate_ops01_v5_package` against the untouched candidate and recomputed expected identity. The producer cannot waive or replace this check;
  - copy the full candidate packet atomically, never individual files selected by hand;
  - before updater convergence, require the copied `checksums.sha256` bytes to hash to the same external `candidate_ledger_sha256`, then recompute every copied primary checksum and require exact equality with its ledger entry; any copy-time mismatch removes the partial PR-C change and blocks integration;
  - replace the current v4 identity constants with one closed `OPS01_V5_EXPECTED = Ops01V5ExpectedIdentity(...)` instance whose source commit, independently captured source-manifest hash, independently captured live pre- and post-staging-manifest hashes, runner hash, validator hash, projector hash, authorization hash, staging root, preflight identity, discovery identity, commands hash, derived expected-call-vector hash, and external candidate-ledger hash come from independently reviewed authorization and candidate facts, never solely from producer-supplied packet fields. `OPS01_V5_EXPECTED.live_pre_staging_manifest_sha256` must equal the canonical live authorization and retained live result but originates from the independent pre-launch baseline; `.live_post_staging_manifest_sha256` originates from capture-time recomputation of the actual ephemeral tree; and `.expected_call_counts_sha256` is computed independently from reviewed authorization bytes and is never copied from a serialized packet key. The permanent validator revalidates its exact `-I -B` candidate-validator argv, recomputes canonical retained proof/authorization/command/ledger identities and closed delta/write-set semantics, and matches the three external manifest identities without requiring the temporary source/control tree. Capture-time recomputation remains a prerequisite fact, not a CI claim;
  - switch default release admission directly from v4/corpus-v3/result-v3 to v5/corpus-v4/result-v4 in the same PR by importing the unchanged independent v5 validator, without a dual-default state;
  - retain all current OPS-01 primary paths and artifact keys;
  - run the canonical updater only after all primary bytes are final;
  - regenerate every changed path proof, Human Index row, Machine Mirror row, checksum, and orientation output through its current owner;
  - run release sanity after companion convergence;
  - prohibit a second OPS execution during integration.
- Compatibility and migration: main remains coherently v4 after PR-A and during OPS. An unrelated later main commit does not invalidate the candidate when the PR-A source commit remains an ancestor, the exact authorized validator and projector hashes remain current, and independent validation passes. Repository history retains the old v4 packet; merged PR-C contains only v5 current evidence. No dual-version default admission exists.
- Validation and evidence: source-ancestor check, exact validator/projector hash checks, external candidate-ledger hash before validation and after copy, reviewed capture-time actual-tree PASS as an immutable prerequisite fact, independent permanent full-candidate validation before and after copy, retained and externally reviewed source/live-pre/live-post manifest identity agreement without a permanent ephemeral-tree claim, exact `-I -B` command reconstruction, empty `PYTHON*` child environment, preflight-to-authorization expected-vector equality, summary-to-authorization expected-vector equality, independently derived expected-vector-hash equality, authorization-to-actual call equality, unknown-key rejection for any serialized vector hash, full required inventory, updater no-diff check, orientation no-diff check, evidence-path validation, mirror schema, index hash, LF, schema-negative tests, focused tests, and all required CI checks.
- Rollback: revert PR-C as an atomic unit, restoring the coherent v4 packet/default constants while leaving PR-A's independent repairs and shared projector in place. If PR-C has not merged, correct it through normal non-destructive branch commits; do not manually edit governed companion files. Any new live recapture after rollback requires new authority.
- Downstream effect: PR-06's release-sanity surface consumes the new bounded contract without reopening PR 359.
- Plan consequence: this CRD does not edit either plan. After IA approval, the separately authorized next-version Current Implementation Plan must allocate `RSC-005` to a separate post-merge PR-C and be approved before implementation relies on it; `r1` remains the epic-scope baseline.
- Documentation consequence: after those facts exist, a separately authorized PF10 section 2.9 update may record the integrated commit, current schemas, validation results, and nonclaims. That recording is not an integration prerequisite or acceptance condition.
- Nonclaims: integration does not by itself establish QA PASS, PF09 movement, token satisfaction, deployment readiness, acceptance, slice closeout, or epic closeout.

## 8. Ownership and Boundary Effects

### Work moved into the new remediation slice

- The two EPIC024 generated-output repairs that PR 359 left inconsistent.
- The raw-marker safety gap in the merged release-sanity validator.
- The strict shared DDL projection and explicit projection-only evidence contract.
- The preflight-qualified OPS-01R recapture with exact Python import/write isolation and conditional candidate integration.

This work is not moved back into PR 359. PR 359 remains merged and closed.

### Retained current-slice work

- After the approved Current Implementation Plan revision, PR-A owns independent closed-rails repairs, the shared projector, tracked runner, closed preflight/discovery contracts, the exact `-I -B` and source/write guard, independent validators, and tests.
- OPS-01R owns one candidate capture only and may write only the authorization-listed temporary control paths and candidate root; it may not write tracked evidence or detached-source bytes.
- PR-C owns candidate integration, default v5 release admission, and final v5-only CI.
- The canonical updater retains sole ownership of path proofs, index, mirror, and checksums.

### Historical work reused without reopening

- EPIC024's mutually consistent bootstrap status pair in the two current primaries supplies migration input only. No historical command is rerun and no status is reevaluated.
- The merged v4 OPS packet supplies migration baseline and test fixtures only. It remains current until a reviewed v5 packet is atomically integrated.
- PR 359 source and evidence remain the reviewed baseline. No new commit is added to the merged PR.

### Downstream work retained elsewhere

- QA execution and acceptance remain in their existing downstream governance lanes.
- PF-Canon and ADR file drainage remains later documentation work.
- PF09 status review remains a separate authorized action and is not triggered by this CRD.
- Deployment, migration, production-write validation, and any bridge-service maintenance remain outside this slice.

### Producer and consumer ownership

| Surface | Sole owner after adoption | Consumers | Boundary effect |
| --- | --- | --- | --- |
| EPIC024 acceptance map and token matrix primary bytes | `tools/qa/run_hde_epic024_harness.py` selective render mode | acceptance and evidence tooling | Same owners and paths; current bytes repaired without QA rerun. |
| DDL identity projection | `engine/db/ddl_identity_projection.py` | posture producer and sanity validator | Replaces two duplicate implementations. |
| OPS-01R control and candidate records | Exact authorized PR-A runner from the detached source worktree is sole preflight/discovery-result/candidate producer; PO supplies exact discovery/live authorization | independent `tools/evidence/hde_epic038_ops01_v5.py`, then integration review | PR-A owns exact `-I -B`, empty `PYTHON*` environment, source-manifest/cache scan, path guard, schemas, validator, and tests. Preflight and discovery authorization validate before external calls; the independent validator owns admission; candidate remains temporary until approved PR-C integration. |
| Retained OPS-01 primaries | PR-C | release-sanity validator and updater | Stable paths/keys, new schema bytes. |
| Path proofs, Human Index, Machine Mirror, hashes | `tools/evidence/update_evidence_index.py` | CI and release sanity | No manual companion writes. |
| Bridge implementation | Separate `pg-bridge` owner | Glow bridge adapter is a read-only client | No change, inspection, deployment, or defect assignment. |

### PF09 status posture

The complete PF09 relationship is: `HDE-DIST001.4` `Partial` for DDL posture and read-only OPS evidence; `HDE-DIST001.6` `Partial` for one-button release-sanity and retained-evidence admission; `HDE-DIST001.9` `Partial` for direct/bridge parity and provider provenance; `HDE-DIST001.11` `Optional` for the existing mapped-cache/vendor safety posture preserved by `RSC-002`; and `HDE-DIST005.2` `Partial` for global Human Index/Machine Mirror and updater discipline. This CRD makes no status change.

`RSC-001` reopens no EPIC024 PF09 row; `.6` and `DIST005.2` constrain only this epic's canonical-path and updater mechanics. `RSC-002` affects `.6` and preserves `.11`. `RSC-003` and `RSC-004` affect `.4` and `.9`. `RSC-005` constrains `.4`, `.6`, `.9`, and `DIST005.2`. No additional PF09 status is inferred.

### Prohibited boundary crossings

- no `pg-bridge` repository, code, environment, service selection, deployment, or issue creation;
- no Railway relink, deploy, restart, variable mutation, or service switch;
- no PostgreSQL write, migration, DDL, grant, role, or schema mutation;
- no vendor network call or birth-data use;
- no raw request, response, vendor payload, vendor envelope, or BodyGraph payload retention;
- no detached-source write, `__pycache__` or `.pyc` residue, environment substitute for `-B`, unlisted staging write, cache-redirection directory, read-only mount requirement, or generalized filesystem sandbox;
- no direct plan edit by this CRD; `r1` remains the epic-scope baseline, while the separately authorized next-version Current Implementation Plan revision is required before implementation reliance;
- no PF09 status movement;
- no QA rerun or completion claim.

## 9. Implementation Requirements and Plan Consequences

### Source-grounded technical requirements

1. Obtain IA technical approval of this CRD and `ADR-CANON-004`. Approval makes the CRD the authoritative input to the plan-revision lane; it is not implementation authorization.
2. Obtain separate authority to create a next-version revision of the Current Implementation Plan in the `r6` lineage. Preserve `r1` as the approved epic-scope baseline. The plan revision must incorporate every approved `RSC-001` through `RSC-005` consequence, the corrected `ADR-CANON-004` adoption rule, exact closed preflight/discovery/hash/import/write contracts, ownership, validation, rollback, and nonclaims.
3. Obtain approval of that Current Implementation Plan revision. No implementation may rely on this CRD or ADR before this gate, unless a newer explicit PO instruction changes the current PF10 posture.
4. Start PR-A only under separate implementation authority, from reviewed current main containing merge commit `78756e776f7fa598370235de6a72aa29fe045af9`. Do not reuse the merged PR branch.
5. Preserve unrelated user changes and use a clean worktree for all committed implementation and OPS execution.
6. Implement `RSC-001`, `RSC-002`, the shared-projector and independent-validator portions of `RSC-003`, and reduced runner controls `RSC-004.A` through `RSC-004.D` in PR-A under closed rails, including one exact ordered `-I -B` prefix, no case-folded `PYTHON*` child environment, the full-source manifest/cache algorithm, exact per-mode write sets, path guard, failure codes, and focused tests. No external I/O is permitted during implementation or CI.
7. Keep default release-sanity admission on the current v4 packet in PR-A. Candidate-v5 validation remains an independent read-only path until PR-C.
8. Merge PR-A only through a separate user action. Materialize the exact `RSC-004.A` source and control roots at a clean immutable detached PR-A merge commit.
9. Independently capture the exact full-source manifest and authenticated preflight staging baseline after required inputs/directories exist, then run the detached runner's zero-I/O full-flow preflight from `preflight-work` as `[interpreter, "-I", "-B", runner, "--preflight"]` with no `PYTHON*` child variable. Invoke the independent validator only as its hash-bound exact `-I -B` vector and supply the independently reviewed `Ops01RPreflightExpectedIdentity` only through canonical stdin. Independently validate canonical `hde_epic038.ops01r.preflight.v1` bytes, exact paths, identities, module origins, two equal vectors, all-zero external I/O, source-manifest equality, cache absence, authenticated pre/post staging delta, and the sole permitted write. Any failure blocks discovery.
10. Only after preflight PASS, construct the exact `hde_epic038.ops01r.discovery_authorization.v1` bytes through the zero-length-placeholder, excluded-baseline, in-place-finalization, identical-recapture sequence; then obtain PO authorization for those final bytes containing the closed `hde_epic038.ops01r.discovery_policy.v1`. Supply the same independently reviewed `Ops01RDiscoveryAuthorizationExpectedIdentity` canonical stdin bytes to both exact authorization- and result-validator vectors. Independently validate authorization identity and later result continuity with those authorized bytes, source-manifest binding, authenticated non-circular discovery staging baseline, exact `-I -B` authorization-validator, producer, result-validator, and target-probe argv/environment, six-stage roster, templates, prohibited families, unlinked empty working directory, write set, sanitization, and subprocess limit before their applicable boundary.
11. Execute only the selected authorized discovery templates, at most once per stage and six total, with the target probe exactly `[interpreter, "-I", "-B", runner, "--target-identity-probe"]`, then independently validate `hde_epic038.ops01r.discovery.v1`. Any missing or ambiguous target, CLI, argv, environment, source manifest, cache scan, write set, nonlinked, identity-field, command manifest, count, checksum, canonical-byte, or secret-safety fact stops before live authorization.
12. Construct the live authorization through the exact zero-length-placeholder, excluded-baseline, in-place-finalization, identical-recapture sequence; then obtain separate PO authorization for those final exact bytes binding source and independent manifest identity, runner, validator, projector, interpreter, preflight identity, complete validated discovery result and its authorization hash, target, CLI, exact `-I -B` live-authorization-validator, launcher, child, and capture-validator argv, empty `PYTHON*` roster, authenticated non-circular live pre-staging baseline, exact success/failure write contract, identity contract, one launch, and complete expected-call vector copied field by field from validated preflight.
13. Invoke `validate_ops01r_live_authorization` through the authorization-bound exact vector, supply only the independently reviewed `Ops01RLiveAuthorizationExpectedIdentity` canonical stdin bytes, and require independent PASS; then redundantly revalidate source, cache, validator/launcher/child argv, environment, authenticated staging inputs, and authorization before marker creation. Independently derive `expected_call_counts_sha256` only from canonical live-authorization `expected_call_counts`, then execute the tracked launcher once. On any launch, source/write, identity, count, candidate, or independent-validation failure, stop without retry, PR-C, or tracked evidence change.
14. On success only and while the ephemeral tree exists, construct the externally reviewed `Ops01V5ExpectedIdentity`, including source, live pre-staging, live post-staging, and ledger identities; invoke `validate_ops01r_live_capture` through the authorization-bound exact `-I -B` vector with those exact canonical stdin bytes; and require both capture-time and nested permanent packet PASS. Review the complete candidate, embedded authorization/discovery/preflight identities, exact invocation/environment provenance, authenticated source/cache/staging-delta proof, preflight-to-authorization vector equality, summary-to-authorization vector equality, derived-hash equality, actual-to-authorization equality, provider provenance, and runner/validator/projector lineage. Later PR-C/release validation uses only the permanent packet API with the same reviewed object or checked-in `OPS01_V5_EXPECTED` and does not claim temporary-tree recapture.
15. Create PR-C from current main only after proving PR-A ancestry and candidate compatibility. Implement `RSC-005`, copy the whole candidate, switch directly to v5 admission, regenerate updater-owned companions after final primary bytes, and run the full closed-rails validation set.
16. PF10 section 2.9 may later or in parallel record living context under separate documentation authority and may receive factual append-only updates after facts exist. PF10 creation/update and permanent PF drainage are not plan-revision prerequisites, implementation prerequisites, deliverables, acceptance conditions, or substitute decision records. This CRD does not itself edit either plan.

### Plan-consequence matrix

| Affected deliverable | Current plan owner | PF09 relationship/status | Current plan baseline | CRD decision and new owner | Components | Evidence outputs | Validation changes | Dependency and execution order | Updater and release-binding order | Retained downstream owner | Exclusions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPIC024 canonical binding coherence | Historical HDE-EPIC024 harness owner; current r6 PR-06 owns only sanity-path migration | No EPIC024 row reopened; `.6` and `DIST005.2` remain `Partial` | current r6 PR-06 historically prohibits EPIC024 primary writes | `RSC-001` directs the next-version Current Implementation Plan to allocate PR-A one narrow two-primary exception through the harness selective mode | harness selective renderer; exact two primaries | existing acceptance map, token matrix, proofs/index/mirror | exact one-path diff; no-write check; touched-set test | IA approval -> separately authorized and approved plan revision -> separate PR-A authority; independent of discovery/OPS | two primaries; canonical updater; orientation; default gate remains v4 | HDE-EPIC024 harness remains primary owner | no `_check_specs`, QA rerun, status reinterpretation, other EPIC024 write, or closeout change |
| Retained raw/secret safety | PR-06 historical OPS admission | `.6` remains `Partial`; `.11` remains `Optional` | current r6 PR-06 validates retained OPS; PF14 requires secret-safe evidence | `RSC-002`, allocated to PR-A by the approved next-version plan | shared safety validator and mutation tests | no new primary | new key/delimiter negatives; existing shell-default/provider-provenance regressions | IA approval -> separately authorized and approved plan revision -> separate PR-A authority; independent of discovery/OPS | updater only for changed primaries; release gate validates current v4 packet | QA and acceptance remain downstream | no generalized DLP or evidence rewrite |
| DDL comparison semantics | PR-04 + OPS-01 + PR-06 | `.4` and `.9` remain `Partial` | current r6 direct/bridge observation plus PR-06 binding; PF10 §2.6 evidence-only posture | `RSC-003`, allocated by the approved next-version plan to PR-A then OPS-01R then PR-C | shared projector, posture producer, current v4 validator, independent v5 validator | no tracked v5 primary in PR-A; temporary v5 candidate in OPS | projector tests; independent fixtures; projection-only and false-full-parity mutations | approved plan -> PR-A merge -> preflight -> discovery authorization validation -> discovery -> exact authorization -> one attempt | no release-binding change until PR-C | PR-C retains integration ownership | no DB/bridge change or full DDL parity |
| OPS-01R live recapture | Historical OPS-01 evidence lane | `.4` and `.9` remain `Partial` | current r6 OPS-01 is read-only evidence only | `RSC-004.A` through `.D`; allocation by approved next-version plan; PR-A/PO/operator/validator owners | tracked runner; exact `-I -B` in every source-loading producer, validator, launcher, target probe, and live child; canonical-stdin external expected identities for every applicable validator CLI; empty `PYTHON*` child environment; full-source manifest/cache scan; authenticated pre-staging baselines and exact mode deltas/write sets; closed preflight and discovery contracts; independent live-authorization gate; one exact-vector launch; capture-time actual-tree validator; permanent packet validator; isolated candidate | preflight/discovery controls are temporary; success candidate or sanitized failure outcome only | independent source and pre/post staging identities; exact argv/environment/stdin; source equality; no cache residue; complete staging enumeration/delta authentication; preflight zero-I/O; discovery authorization and result continuity before live authority; per-stage dispatch before CLI; independent prelaunch authorization validation; derived expected hash; exact actual equality; capture-time plus permanent admission | approved plan -> PR-A merge -> preflight isolation PASS -> discovery-policy isolation PASS -> discovery-result source/write/authorized-identity PASS -> live-authorization independent PASS -> one launch -> capture-time actual-tree and permanent candidate PASS -> PR-C permanent packet PASS | no updater or release binding during discovery/OPS | PR-C only after independent success review | no guessed UUID/flag/field, alternate expected-input channel, env substitute, source/cache/unlisted write, read-only mount, generalized sandbox, tracked write, retry, mutation, QA, status movement, or bridge work |
| V5 evidence integration | PR-06 historical binding owner | `.4`, `.6`, `.9`, and `DIST005.2` remain `Partial` | current r6 PR-06 consumes OPS without rerun | `RSC-005`, allocated to PR-C by the approved next-version plan | full packet, independent v5 validator, default dispatcher, updater, orientation | exact eleven primaries plus exact companions | ancestry/compatibility, candidate identities, derived-vector identity, v5-only negatives, updater/mirror/path/hash/LF/full CI | approved plan -> success candidate review -> separate PR-C authority | primaries; updater companions; orientation; release sanity | QA, PF09, acceptance, deployment, and closeout remain separate | no second OPS run or dual default admission |

### Dependency and adoption order

1. IA technically approves this CRD and `ADR-CANON-004` for their exact bounded decisions.
2. A separately authorized next-version revision of the Current Implementation Plan incorporates every approved consequence while retaining `r1` as the epic-scope baseline.
3. That Current Implementation Plan revision is approved. Implementation reliance before this gate is prohibited unless a newer explicit PO instruction changes current PF10 posture.
4. A separate implementation authority creates PR-A.
5. PR-A closed-rails tests and CI pass; PR-A is reviewed and merged by separate user action.
6. The independent pre-run source manifest and preflight staging-baseline hash are frozen; the exact merged runner emits canonical `hde_epic038.ops01r.preflight.v1` under exact `-I -B`; the independent validator runs through its bound exact vector with only the canonical-stdin `Ops01RPreflightExpectedIdentity` and proves source, components, interpreter, argv/environment, module origins, Railway executable identity, source equality, cache absence, authenticated staging delta and exact preflight write set, two equal vectors, canonical identity, and zero external I/O.
7. The discovery authorization is built through the exact placeholder/baseline/in-place-finalization/identical-recapture sequence; the PO authorizes the resulting canonical `hde_epic038.ops01r.discovery_authorization.v1` bytes containing the closed policy and exact `-I -B` target-probe/write contract; the independent authorization validator passes before any CLI call, and the result validator later receives the same canonical-stdin expected object and proves continuity with that PO-authorized identity.
8. Discovery executes at most the selected six-stage policy; the exact target probe writes nothing; and `hde_epic038.ops01r.discovery.v1` passes independent argv/environment/source/cache/write result validation.
9. The live authorization is built through the exact placeholder/baseline/in-place-finalization/identical-recapture sequence; the PO then issues separate exact authority over those bytes, bound to source and baseline manifest, runner, validator, projector, interpreter, preflight, discovery authorization/result, target, CLI, exact `-I -B` live-authorization-validator/launcher/child/capture-validator argv, empty `PYTHON*` roster, authenticated live pre-staging baseline, write contract, identity contract, and field-identical preflight vector.
10. Independent `validate_ops01r_live_authorization` PASS using only the canonical-stdin expected object and redundant prelaunch source/cache/argv/environment/authenticated-write validation pass; the expected vector hash is independently derived only from canonical authorization counts; then the operator invokes the tracked launcher once. Any uncertainty or failure stops and consumes no further authority.
11. On success only while temporary state exists, `validate_ops01r_live_capture` receives only the canonical-stdin `Ops01V5ExpectedIdentity`, and it and its nested permanent packet validation pass, including external source and live pre/post-staging identities, full source equality, no cache residue, exact authenticated staging delta/writes, candidate inventory/ledger semantics, and the complete expected-vector identity/equality chain.
12. Separate implementation authority creates PR-C; ancestry and compatibility gates pass; the complete candidate is integrated and default admission switches to v5.
13. The canonical updater regenerates companions from final primary bytes; orientation, path, mirror, hash, LF, focused, full CI, and release-sanity checks pass.
14. PR-C review and merge remain separate user actions.
15. PF10 living-context recording and permanent PF drainage, if separately authorized, occur on independent documentation axes and do not gate plan revision or engineering actions.

### Validation order

- Unit and mutation tests before selective output generation.
- Selective EPIC024 primaries before updater generation.
- PR-A updater/orientation checks before merge.
- Approved next-version Current Implementation Plan before any implementation relies on this CRD.
- Independent source-manifest and authenticated preflight-staging-baseline capture, then exact `-I -B` offline import/full-flow producer and validator execution with the canonical-stdin expected identity and independent argv/environment/source/cache/delta/write validation before discovery authority.
- Non-circular placeholder/baseline/in-place-finalization/identical-recapture construction of discovery authorization, then static-policy isolation validation through the bound `-I -B` validator vector and canonical-stdin expected identity before the first CLI subprocess; then bounded execution through the bound discovery-producer vector, immediate pre-dispatch validation, an exact `-I -B` no-write target probe, command-manifest capture, and bound result-validator validation against the same expected authorization identity before live authority.
- Non-circular placeholder/baseline/in-place-finalization/identical-recapture construction of exact live authorization; independent exact-argv `validate_ops01r_live_authorization` PASS with canonical expected-identity stdin; authenticated live pre-staging baseline, `-I -B` launcher/child argv, environment/source/write prelaunch validation, and independently derived expected-vector identity before one live launch.
- Prospective per-field call denial and terminal exact expected/actual equality during live capture.
- Capture-time actual-tree validation through the authorization-bound exact vector and canonical `Ops01V5ExpectedIdentity` stdin while temporary state exists, including external source/live-pre/live-post identities, followed by permanent candidate semantics through the exact retained candidate-validator argv with the same canonical stdin (or direct API with checked-in `OPS01_V5_EXPECTED`) and checksum/identity validation before tracked copy; only permanent packet validation repeats after integration.
- PR-C primary copy before updater/orientation convergence and release sanity.
- Final v5-only negatives before PR review.

### Rollback stops

- Missing or unapproved Current Implementation Plan revision: no PR-A implementation reliance.
- Any PR-A test failure: no merge, discovery, or OPS request.
- Any preflight schema, `-I -B` argv, canonical expected-identity stdin, Python-environment, identity, path, origin, source-manifest, cache-residue, write-set, deterministic-vector, canonical-byte, nonclaim, or zero-I/O failure: reviewed source correction; no discovery or live authorization.
- Any discovery-authorization/policy isolation or expected-input failure: no CLI call. Any discovery-result expected-authorization continuity, argv/environment/source/cache/write, or other failure: no live authorization; no retry without a new exact discovery authority.
- Any independent live-authorization-validator expected-input or prelaunch argv/environment/source/cache/write failure: do not create the marker or execute.
- Any post-marker launch, child-identity, source/write, call-count, capture-time actual-tree, permanent candidate, or other validation failure: authority is consumed; stop without retry or PR-C. A pre-marker mismatch stops without consuming or launching.
- Any PR-C integration or companion failure: revert PR-C as a unit; do not rerun OPS automatically.
- Any PR-C final v4 acceptance or dual default admission: return PR-C to non-mergeable state.

### Exclusions

This CRD does not itself rewrite either implementation plan; it requires a separately authorized and approved next-version Current Implementation Plan before implementation relies on its decisions. It does not create a new epic, alter the `r1` epic-scope baseline, add unrelated evidence cleanup, refactor the general provider architecture, change database or bridge APIs, reopen EPIC024 QA, run production writes, or perform PF documentation work. It requires no read-only source mount, cache-redirection directory, environment-variable bytecode substitute, host-wide immutability monitor, or generalized filesystem sandbox. The v1.0 multi-state journal, child protocol, launch manifest, governed negative-receipt schema, `fsync` choreography, `/proc` recovery, recovery launcher, output-cap subsystem, installed-distribution manifest, repository-wide code-contract map, and generalized four-mode state machine remain removed from obligations. `Follow-up (out of scope):` any reusable OPS platform, generalized filesystem sandbox, or crash-recovery framework requires a separate causal case and authority.

## 10. PF-Canon, ADR, PF09.x, and PF10 Consequences

### ADR-CANON-004

**ADR ID:** `ADR-CANON-004`

**Title:** Versioned Glow-Owned DDL Identity Projection for OPS Provider Evidence

**Status:** `PROPOSED - PENDING IA TECHNICAL APPROVAL`

**Linked IDs:** `BUG-003`, `CAUSE-003`, `CAUSE-005`, `RSC-003`, `RSC-005`, IA review v1.1 `REV-001`, IA review v1.1 `REV-005`

**Canon effect:** `AMENDS`

**Current canon baseline with exact proof:**

- `PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8`, exact locator `§8.6.3.4 Gates, runtime, DB, and ops evidence` (complete unit lines 4877-4991 at merged main). Relied-on line copied verbatim:

  > * `artifacts/db/ddl_fingerprint.json`  

- `PF14-Canon-HDE-Mechanics-Guide v3.4.3`, exact locator `§20.3 Bridge parity mechanics`, including `§20.3.1` (complete unit lines 4561-4621 at merged main). Relied-on lines copied verbatim:

  > Provider-parity false-PASS guard (required). The checker MUST reject provider-parity PASS conditions when direct rows are missing, skipped, unavailable, or errored. A truth-preserving skip or unavailable posture MAY be accepted only when the artifact does not present live provider parity as passing.

  > OPS provider-parity closure packet mechanics (required when OPS evidence is used to close a provider-parity loop). The OPS packet MUST keep provider-parity closure evidence machine-readable, secret-safe, and non-overclaiming. When the packet claims closure, it MUST record the active parity corpus, row-level direct and bridge provider availability, row-level parity values, closure status, bridge consistency result, parity scope rationale, non-claims, command transcript, stdout, stderr, exit code, redacted or presence-only environment posture, final report, and checksum ledger. If an active row such as `ddl_fingerprint` remains in the corpus, closure MUST be based on row-level match evidence, not on silent exclusion. OPS closure evidence MUST NOT claim QA PASS, PF09 status movement, epic closure, or acceptance-token satisfaction for DB proof labels.

**Exact current rule or limitation being amended:**

Current canon catalogs `artifacts/db/ddl_fingerprint.json`, requires truth-preserving row-level direct/bridge match evidence for an active `ddl_fingerprint` row, and requires the closure packet to remain machine-readable, secret-safe, non-overclaiming, and bounded by explicit nonclaims. It does not define a versioned DDL comparison schema, the exact shared projection fields, deterministic ordering, strict malformed-input behavior, an explicit projection-only result label, the unexamined fields, or a required false full-semantic-parity claim.

**Complete negative-search proof for the limitation:**

- PF12 scope: the complete `PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8` §8.6.3.4 unit, lines 4877-4991. Method: case-insensitive exact text search followed by semantic reading of the complete unit. Terms `projection`, `provider`, `column`, `nullable`, and `schema_version` returned zero hits; `ddl` and `fingerprint` returned only the `artifacts/db/ddl_fingerprint.json` catalog row. Case variants were included by case-insensitive matching.
- PF14 scope: the complete `PF14-Canon-HDE-Mechanics-Guide v3.4.3` §20.3 unit including §20.3.1, lines 4561-4621. Method: case-insensitive exact text search followed by semantic reading of the complete unit. Terms `projection`, `nullable`, `default`, `comparison_contract`, and `full_ddl_semantic_parity_claimed` returned zero hits; `ddl_fingerprint` occurred once in the quoted row-level closure rule. Case variants were included by case-insensitive matching.

**Observed current Repo reality:**

- `scripts/db/capture_epic011_posture.py::_ddl_projection` and `tools/evidence/run_sanity_pipeline.py::_normalize_ddl_provider_value` independently implement the same narrow concept with different malformed-input behavior.
- The current v4 proof stores rich direct metadata and reduced bridge metadata but labels the DDL row simply `match`.
- Current stable primary paths and artifact keys already exist and can be retained.

**Engineering problem or limitation:**

The retained evidence cannot distinguish equality of a shared identity projection from full DDL semantic parity. Duplicate producer/consumer logic can drift and already differs in fail-closed behavior.

**Alternatives considered and rejection rationale:**

1. Compare full nullability, defaults, constraints, and view definitions now. Rejected because the bridge observation does not expose equivalent fields and cross-repository/service expansion is not justified by a proven bridge defect.
2. Preserve duplicate projections and improve wording only. Rejected because wording does not prevent drift or silent malformed-row skipping.
3. Remove `ddl_fingerprint` from the corpus. Rejected because current mechanics require active-row evidence rather than silent exclusion.
4. Add a third projection to the runner. Rejected because it multiplies ownership and weakens independent validation.
5. Selected: one strict shared Glow-owned projector, exact version/field roster/exclusions, projection-specific result label, and an explicit false full-semantic-parity claim.

**Selected decision and exact bounded amended rule:**

Adopt `engine/db/ddl_identity_projection.py` and the exact API, invariants, field rosters, result labels, and evidence versions specified in `RSC-003`. For the HDE-EPIC038 OPS provider-parity `ddl_fingerprint` row only, a passing result proves equality only of object kind/name and column name/type after strict deterministic projection. The result label is `projection_match`; proof and summary must set `full_ddl_semantic_parity_claimed` to false; included and unexamined fields must be explicit; malformed included identity fields fail closed; producer and validator must import the same function.

**Changed meaning:**

The prior row-level `match` requirement is narrowed for this exact DDL row from an unlabeled match to an explicitly versioned identity-projection match. It cannot be interpreted as equality of nullability, defaults, constraints, view definitions, or any other unexamined field.

**Canon that remains unchanged:**

PF12 evidence paths, primary/companion ownership, Human Index, Machine Mirror, checksums, and path proofs remain unchanged. PF14 provider availability, row-level truthfulness, secret safety, parity-scope rationale, no-silent-exclusion rule, DBAccess/provider provenance, and all QA/PF09/token/closeout nonclaims remain unchanged. The amendment does not change PostgreSQL, bridge, provider, BodyGraph, public CLI/Reader, vendor, Railway, or durable-data contracts.

**Exact affected topic and bounded scope:**

Glow-owned DDL identity projection and projection-only semantics for the HDE-EPIC038 OPS-01 provider-parity evidence family and its release-sanity admission. No other parity row or evidence family is amended.

**Exact proposed implementation owner and locus:**

- API owner: `engine/db/ddl_identity_projection.py`.
- Producer adapter: `scripts/db/capture_epic011_posture.py` imports the API.
- Consumer/admission validator: `tools/evidence/run_sanity_pipeline.py` imports the same API.
- Independent candidate validator: `tools/evidence/hde_epic038_ops01_v5.py` imports the same API.
- Unit validation: `tests/db/test_ddl_identity_projection.py`.
- Packet validation: `tests/evidence/test_hde_epic038_release_sanity.py`.

**API, schema, path, key, producer, and consumer decisions:**

- API and constants are exactly those in `RSC-003`.
- DDL contract schema is `hde.ddl_identity_projection.v1`.
- Provider proof schema is `hde_epic038.ops01.provider_parity.v5`.
- Active corpus is `hde_epic038_ops01_live_bodygraph_parity_v4`.
- Result summary schema is `hde_epic038.ops01.result_summary.v4`.
- DDL result label is only `projection_match`.
- `full_ddl_semantic_parity_claimed` is exactly false in proof and summary.
- Existing paths and artifact keys remain stable, including `epic038.pr06.ops01.provider_parity_proof_json` and `epic038.pr06.ops01.result_summary_json`.
- The exact authorized runner produces candidate primaries once; the independent v5 module validates candidate semantics; release sanity owns default dispatch; the canonical updater owns companions.

**Source-adapter, persistence, and durable-data effects:**

The exact source adapters are the existing direct `psycopg` observation and Glow bridge-adapter observation. No adapter, fallback, provider API, database schema, data, migration, or durable runtime persistence changes. The projector is pure; only secret-safe governed evidence JSON and existing companions change after separately authorized OPS and PR-C actions.

**Compatibility and migration consequences:**

The function accepts current rich direct and reduced bridge inputs while strictly validating included fields. Extra provider metadata is retained as unexamined and cannot support parity. PR-A merges the shared API and independent candidate-v5 validator while default release admission remains v4. OPS-01R produces v5/v4/v4 candidate bytes from exact PR-A source. PR-C independently validates the candidate, checks source compatibility, atomically replaces the packet, and switches default admission directly to v5. No merged state has dual default admission.

**Dependency, adoption order, and plan consequences:**

IA technical approval makes this CRD and proposed ADR the authoritative inputs for the separately authorized next-version Current Implementation Plan revision. `r1` remains the approved epic-scope baseline. The plan revision must incorporate this ADR's exact DDL-projection architecture, PR-A/OPS-01R/PR-C allocation, compatibility, validation, rollback, and nonclaims, and must be approved before implementation relies on the ADR unless a newer explicit PO instruction changes the current PF10 posture. Separate implementation authority then permits PR-A; PR-A review/merge precedes `RSC-004` preflight, validated discovery authorization/policy, exact live authorization, and one attempt; independent candidate review precedes PR-C; updater convergence and v5-only validation precede separate PR-C merge action. PF10 living-context recording and permanent PF drainage are separate documentation axes and do not gate plan revision or implementation. PF09 status does not move.

**Validation and evidence requirements:**

Strict projector unit tests; malformed-input, duplicate, alias-conflict, ordering, and excluded-field tests; packet schema/corpus/result mutations; inherited provider-selection tests; closed preflight and discovery authorization/result validation; exact `-I -B` and source/write qualification as a non-canon operational prerequisite; candidate-root validation; the non-circular derived expected-vector identity chain and exact actual equality; updater/orientation/mirror/path/hash/LF checks; and final v5-only CI.

**Risks and safeguards:**

- Reject rather than skip malformed identity fields.
- Preserve exact type strings and deterministic ordering.
- Enumerate included and unexamined fields.
- Reject plain DDL `match`, missing/true full-parity flags, duplicate projection implementations, and permanent dual-version admission.
- Prohibit cross-repository repair absent a separately proven bridge defect and rescope.

**Rollback or fail-closed posture:**

Before integration, no candidate is copied on any failure. After integration, revert PR-C as one unit to the coherent v4 packet/default validator while retaining independent PR-A repairs. A mixed validator/packet state is invalid. Another live attempt requires new authority.

**Permanent PF-Canon or ADR drainage targets:**

| Target | Exact locator | Required later drainage | Order | Unchanged canon |
| --- | --- | --- | --- | --- |
| `PF12-Canon-HDE-Schemas-and-Artifacts` | §8.6.3.4, provider-parity DB/ops evidence family | Add v5 proof, v4 corpus, v4 summary, `hde.ddl_identity_projection.v1`, stable paths/keys, projection label, false-full-parity rule, and v4-to-v5 migration posture. | After IA approval and successful implementation/integration evidence; never an execution gate. | Canonical sanity path, updater ownership, index, mirror, hashes, and path-proof rules remain unchanged. |
| `PF14-Canon-HDE-Mechanics-Guide` | §20.3 Bridge parity mechanics | Define shared-identity DDL scope and prohibit interpreting `projection_match` as full semantic parity. | After PF12 schema drainage; never an execution gate. | Existing read-only, secret-safe, fail-closed, scope-rationale, provider-provenance, and no-overclaim mechanics remain unchanged. |
| `PF09.6-Canon-HDE-Build-Checklist-Distillation` | `HDE-DIST001.4`, `.6`, `.9`, `.11`; `HDE-DIST005.2` | Later wording clarification for projection/provenance, release admission, preserved safety, and updater discipline without reopening EPIC024 or moving status. | After PF12/PF14 drainage; never an execution gate. | `.4`, `.6`, `.9`, and `DIST005.2` remain `Partial`; `.11` remains `Optional`; unrelated rows remain unchanged. |

PF10 section 2.9 is not permanent canon and is not an ADR substitute. If separately authorized, it may record living context and later facts only.

**Downstream effects:**

Future consumers can distinguish projection parity from full DDL parity. A future full-semantic contract requires a separate finding, capability proof, CRD/ADR, migration, and authorization.

**Explicit nonclaims:**

No full DDL semantic parity, bridge defect, bridge conformance change, SQL/schema/data change, deployment, QA PASS, PF09 movement, token satisfaction, acceptance, PR readiness, or closeout. No PF file has been edited or drained by this CRD.
### Other canon effects

- `RSC-001`: `NO CANON CHANGE`; it restores current canonical sanity-path bindings.
- `RSC-002`: `NO CANON CHANGE`; it enforces the existing no-raw-payload rule across retained text forms.
- `RSC-004`: `NO CANON CHANGE`; it adds bounded operational qualification and does not alter the task's read-only meaning.
- `RSC-005`: `NO CANON CHANGE` beyond adopting `ADR-CANON-004`; it is the required atomic migration mechanism.

### PF09 consequences

| PF09 row | Current status | CRD relationship | Status movement |
| --- | --- | --- | --- |
| `HDE-DIST001.4` | `Partial` | `RSC-003`, `RSC-004`, and `RSC-005` add honest versioned DDL posture and preserve read-only OPS boundaries. | None |
| `HDE-DIST001.6` | `Partial` | `RSC-001` uses its canonical-path constraint without reopening EPIC024; `RSC-002` hardens retained-evidence admission; `RSC-005` preserves one-button/release-sanity closure. | None |
| `HDE-DIST001.9` | `Partial` | `RSC-003`, `RSC-004`, and `RSC-005` preserve distinct direct/bridge provenance and migrate the DDL row without a bridge-service change. | None |
| `HDE-DIST001.11` | `Optional` | `RSC-002` preserves the existing mapped-cache/vendor safety posture and already-merged shell-reference protection. | None |
| `HDE-DIST005.2` | `Partial` | `RSC-001` and `RSC-005` obey global Human Index/Machine Mirror and updater discipline. | None |

No EPIC024 PF09 row is reopened. No additional PF09 status is inferred or moved.

### PF10 consequence

Current PF10 §2.4 `Governing posture` controls the plan-adoption topic for this revision:

> The approved CRD may govern revision of the current HDE-EPIC038 Implementation Plan. The Implementation Plan must be revised before implementation relies on these decisions.

Accordingly, this CRD and `ADR-CANON-004` do not themselves edit either plan. `r1` remains the approved epic-scope baseline. After IA technical approval, this CRD is the authoritative input for a separately authorized next-version Current Implementation Plan revision, and implementation may not rely on `RSC-001` through `RSC-005` or `ADR-CANON-004` until that revision is approved unless a newer explicit PO instruction changes the current PF10 posture.

PF10 section `2.9) PR-06 Post-Merge Remediation and OPS-01R HDE-EPIC038` remains only a proposed living-context record. Under separate documentation authority it may be created later or in parallel and may record:

- PR 359 merge commit and frozen scope boundary;
- this CRD and IA disposition;
- confirmed `BUG-001`, `BUG-002`, and `BUG-003` remediation scope;
- `BLK-001` and `ACT-002` only as `UNVERIFIED` historical provenance, without repeating alleged hashes, counts, traceback, no-I/O, provider-boundary, or consumed-attempt claims as facts;
- `STALE-001` and `STALE-002` superseded dispositions and retained regression coverage;
- approved `ADR-CANON-004` lineage, exact scope, and permanent PF12/PF14 drainage targets;
- the narrow post-merge EPIC024 exception and its strict two-primary/no-QA bounds after the approved plan revision allocates it;
- the approved-plan -> PR-A -> exact `-I -B` closed preflight/source-write PASS -> validated discovery authorization/policy -> bounded discovery/target-probe source-write PASS -> exact OPS-01R -> candidate source-write PASS -> PR-C lineage;
- explicit `pg-bridge` exclusion;
- unchanged PF09 posture and all QA, token, acceptance, deployment, and closeout nonclaims;
- exactly: "For this exact post-merge slice, r1 remains the approved epic-scope baseline. This CRD does not edit either plan. Before implementation relies on the approved rescope, a separately authorized next-version Current Implementation Plan revision must be approved unless a newer explicit PO instruction changes this posture.";
- exactly: "PF10 §2.6's historical v4 `ddl_fingerprint` result labeled `match` records an unversioned shared-field comparison only. It does not prove full semantic DDL parity. Until PR-C integrates a valid v5 packet, v4 remains the current retained packet. After PR-C, record the current v5 result as `projection_match`. Every other §2.6 provider-parity row, evidence-only posture, `Partial` status, and QA, acceptance, PF09-movement, deployment, and closeout nonclaim remains unchanged."

The phrase "After PR-C, record" is prospective. Only after facts exist may separately authorized factual updates append approved-plan identity, PR-A commit/tests, preflight identity and expected vector, discovery-authorization and result identities, live authorization, actual counts, outcome, candidate identity, PR-C schemas, and validation results.

PF10 living-context recording is not the Current Implementation Plan revision, implementation authorization, required implementation deliverable, required check, acceptance condition, closeout gate, or substitute decision record. Permanent PF12/PF14/PF09.6 drainage remains later documentation work and does not gate the plan revision or execution. This CRD does not edit PF10 or any plan.

## 11. Evidence, Risks, and Residual Unknowns

### Factual evidence and Repo validation

- PR 359 is merged and closed at the exact merge commit recorded in section 1.
- The merged generator/output path mismatch was verified by comparing both writer functions with both governed checked-in outputs.
- The raw-marker gap was verified in the merged scanner source. The shell-default credential issue was tested and is already rejected by exact full-match behavior.
- The provider-selection finding was verified stale by inspecting both the retained v4 proof and the mutation tests for path, hash, selected provider, attempts, selection order, force flags, and row-provider drift.
- The DDL ambiguity was verified by comparing both implementation functions and the retained direct/bridge DDL values.
- The external failed-run report does not prove occurrence, traceback location, provider boundary, hashes, counters, no external I/O, or consumed authority from the permitted sources; every such value is `UNVERIFIED` in §4 and non-operative. The current successful retained runner demonstrates only a current Glow-root/interpreter/module pattern.

Evidence pointer: Repo | `tests/evidence/test_hde_epic038_release_sanity.py` | "Shell defaults, assignment operators, command substitution, provider snapshot path/hash/content/attempt/order/flag drift, and provider substitution are rejected."

Evidence pointer: Repo | `audit/ops/hde-epic038/ops-01/result_summary.json` | "schema=hde_epic038.ops01.result_summary.v3; active corpus v3; runner and staging identities are pinned; QA, PF09 movement, acceptance, and closeout are not claimed."

### Diagnostics

- Read-only GitHub inspection fixed the merged baseline, PR lifecycle, exact merge/head SHAs, current source functions, current packet schemas, exact packet bytes, and updater artifact keys.
- The local diagnostic checkout's branch, head, status-entry count, and complete porcelain output were captured before and after inspection. The before/after outputs were identical; the checkout was not used as merged-state authority.
- No test, harness, updater, OPS runner, provider, database, bridge, vendor, Railway, deployment, or migration command was executed while authoring this CRD.
- The external failed-run assertions were converted into the self-contained §4 claim-disposition record. No unavailable source is required, no alleged candidate is an integration input, and no operative conclusion depends on it.

Evidence pointer: Repo | case-sensitive exact GitHub searches of current `amthorn78/glow-hdengine-v2` | "0 hits for the alleged runner hash, alleged ledger hash, `051XSWvs`, and `ModuleNotFoundError`; zero hits limit verification and do not disprove an external run."

Evidence pointer: Repo | `tools/evidence/update_evidence_index.py::EPIC038_PR06_PRIMARY_ARTIFACTS` | "The exact OPS-01 primary inventory is eleven files and artifact keys are derived as epic038.pr06.ops01 plus the normalized filename."

### Rejected alternatives

- Continue PR 359 or reuse its merged branch: rejected because PR 359 is closed and the PO ordered scope separation.
- Keep one unmergeable PR across OPS: rejected because it would delay independent P1/P2 fixes and couple closed-rails review to live success.
- Use an untracked ad hoc `/tmp` runner: rejected prospectively because its exact source, imports, identities, orchestration, and zero-I/O preconditions cannot satisfy the closed preflight contract.
- Add default v4/v5 dual admission: rejected because every merged main state must have one current evidence version.
- Expand safe raw-marker RHS values: rejected because the finding concerns key syntax, not a broader redaction-value contract.
- Rerun historical EPIC024 QA, claim full DDL parity, remove the DDL row, or modify `pg-bridge`: rejected for the causal and ownership reasons in sections 4 through 7.

### Plan and PF validation

- The baseline r6 plan gives OPS-01 an evidence-only role and assigns validation/binding to PR-06 without rerunning OPS. It remains the current plan lineage until a separately authorized next-version revision is approved.
- Current PF10 §2.4 requires the Current Implementation Plan revision before implementation relies on approved HDE-EPIC038 rescoping decisions. PF10 §2.6 preserves the evidence-only posture and does not elevate OPS evidence into acceptance or QA. Its historical v4 DDL `match` wording remains qualified by the bounded `ADR-CANON-004` decision. A later or parallel PF10 section 2.9 may record living context, but it is not the required plan revision or an authority substitute.
- PF12 §8.6.3.4 and PF14 §20.3 govern the evidence family, truth-preserving row parity, scope rationale, and non-overclaim posture but do not define the exact DDL projection contract. `ADR-CANON-004` supplies the bounded amendment upon IA technical approval.
- PF07 supports the separate `glow-hdengine-v2` and `pg-bridge` ownership boundary.

Evidence pointer: PF12 - PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8 | section 8.6 | "Canonical sanity evidence, provider-parity primaries, Human Index, Machine Mirror, checksums, and path proofs are governed; the canonical updater owns companions."

Evidence pointer: PF14 - PF14-Canon-HDE-Mechanics-Guide v3.4.3 | sections 1.1 and 20.3 | "Retained operational evidence is secret-safe and fail-closed; row-level provider parity requires an explicit scope rationale."

Evidence pointer: PF07 - PF07-Canon-Glow-Infrastructure v2.2.4 | production HD Engine and bridge service inventory | "amthorn78/glow-hdengine-v2 and glow-hdengine-v2 are the HD Engine repository/service; pg-bridge is a separate service and repository boundary."

Evidence pointer: PF27 - PF27-Canon-Plan-Templates v1.9.5 | ADR and documentation-home discipline | "A durable decision has one owning record and later topic-owning drainage; duplicate decision homes are prohibited."

Evidence pointer: PF09.6 - PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2 | `HDE-DIST001.4`, `HDE-DIST001.6`, `HDE-DIST001.9`, `HDE-DIST001.11` | "DDL/read-only posture, one-button release-sanity admission, and direct/bridge provenance remain Partial; mapped-cache/vendor safety remains Optional."

Evidence pointer: PF09.6 - PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.2 | `HDE-DIST005.2` | "Global Human Index and Machine Mirror discipline remains Partial and constrains updater-owned convergence."

Evidence pointer: PF10 - PF10-HDE-Build-Notes v12.2.7 | §2.4 `Governing posture` | "The approved CRD may govern revision of the current HDE-EPIC038 Implementation Plan. The Implementation Plan must be revised before implementation relies on these decisions."

Evidence pointer: Implementation Plan | `r6 Implementation Plan HDE-EPIC038.md`, PR-06/OPS-01 mapping | "HDE-DIST001.4 and HDE-DIST001.9 span PR-04, OPS-01, and PR-06; PR-06 validates and binds OPS evidence without rerunning OPS."

Evidence pointer: Implementation Plan | `r1 Epic Plan HDE-EPIC038.md`, document control | "HDE-EPIC038 is Distillation Pass 3 and the reviewed historical plan status is Planned."

Evidence pointer: IA review v1.1 | `REV-001` | "implementation may not rely on RSC-001 through RSC-005 or ADR-CANON-004 until that revision is approved, unless a newer explicit PO instruction changes the PF10 posture."

### Negative-search methods

1. **Shared DDL projector absence at the merged baseline.** Searched terms: `_ddl_projection`, `_normalize_ddl_provider_value`, `ddl_fingerprint`, `project_ddl`, `nullable`, `default`, `constraints`, and `definition`. Scope: merged `engine/db`, `scripts/db/capture_epic011_posture.py`, `tools/evidence/run_sanity_pipeline.py`, and focused tests. Method: case-sensitive repository symbol search followed by semantic comparison of complete function bodies; equivalent behavior was considered even where names differed. Result: two local projection implementations were found and no shared `engine/db` projector existed.
2. **Exact PF DDL projection contract absence.** PF12 scope: complete `PF12-Canon-HDE-Schemas-and-Artifacts v2.7.8` §8.6.3.4, lines 4877-4991. Case-insensitive exact searches for `projection`, `provider`, `column`, `nullable`, and `schema_version` returned zero hits; `ddl` and `fingerprint` returned only the artifact catalog row. PF14 scope: complete `PF14-Canon-HDE-Mechanics-Guide v3.4.3` §20.3 including §20.3.1, lines 4561-4621. Case-insensitive exact searches for `projection`, `nullable`, `default`, `comparison_contract`, and `full_ddl_semantic_parity_claimed` returned zero hits; `ddl_fingerprint` occurred once in the row-level closure rule. Each complete unit was then read semantically. Result: current canon requires row-level truthful closure and scope rationale but does not define the exact projection roster, version, label, or false-full-parity rule.
3. **No demonstrated `pg-bridge` defect.** Scope: the three confirmed Glow Repo defects, PF07 repository/service ownership boundary, and the self-contained failed-run claim-disposition record. Method: causal and ownership review, not inference from the unverified external report. Case handling: not applicable. Result: the confirmed repairs are Glow-owned; no permitted source establishes a bridge defect, so no bridge task is imported.
4. **Failed-run verification boundary.** Search terms: exact alleged runner hash `aca1f0e09810cc7a451c07bd6660015e3d071ac50d930116177e60aa8aa8f15f`, exact alleged ledger hash `4dff85b6e55571ca49fae25f06dd9a19c23234d0c46c5c4a37225380fc21b8d6`, `051XSWvs`, and `ModuleNotFoundError`. Scope: current indexed `amthorn78/glow-hdengine-v2`. Method: four case-sensitive exact GitHub code searches. Result: zero hits for each. Negative result means current Repo cannot verify those external claims; it does not prove absence or falsity. Every element remains `UNVERIFIED` and non-operative.
5. **ADR-CANON-004 lineage-ID availability.** Carried from the v1.1 baseline: PF10 section 2.4 contains ADR-CANON-001 through ADR-CANON-003 and no ADR-CANON-004, making `ADR-CANON-004` the next proven HDE-EPIC038 lineage ID. No new lineage search was required for the v1.2 revision.

### Selected architecture rationale

The selected solution reuses current provider captures, paths, keys, updater ownership, and evidence corpus. It adds one shared pure module, one tracked operational runner, and four independently justified OPS sub-decisions: closed exact `-I -B` import/source/write preflight, closed bounded Railway discovery authorization/policy with the same target-probe control, one authorization-owned exact-call live launch with the same child control, and isolated independent source/write candidate admission. `-B` is the smallest direct bytecode-suppression mechanism and is hash-bound rather than replaced by environment or platform machinery. Mandatory controls are justified by the prospective one-attempt safety contract and independently validatable identities, not the unverified external report. The v1.0 platform-hardening mechanisms listed as removed in `RSC-004` and §9 are not obligations. The solution does not introduce a cross-service contract, full DDL parity program, generalized secret scanner, reusable OPS platform, host-wide filesystem monitor, crash-recovery framework, or new evidence home.

### Material risks and safeguards

| Risk | Safeguard |
| --- | --- |
| Selective EPIC024 repair accidentally rewrites historical QA or statuses | Pure renderers, exact two-file touched-set assertion, strict cross-check of the two retained status representations, and prohibition on `_check_specs`. |
| Raw scanner creates broad false positives | Exact four-marker roster, balanced optional quotes, exact delimiters, closed safe-scalar set, and focused positive/negative tests. |
| Raw scanner remains bypassable through multiline or empty syntax | Recognized marker with absent/structured/block-scalar RHS fails closed; checksum-consistent tests cover each form. |
| Shared projection hides rich-field differences | Explicit unexamined roster, `projection_match` label, and required false full-semantic-parity field. |
| Producer and validator drift | Both import one strict pure function; duplicate functions are deleted. |
| Candidate-only v5 validation accidentally becomes default before integration | PR-A tests prove default release sanity accepts only the current v4 packet; the independent v5 module is callable for candidate review but not default dispatch. PR-C switches the single default directly to that same validator. |
| A one-attempt lane reaches CLI or provider boundaries before source/import qualification | Produce only the closed `hde_epic038.ops01r.preflight.v1` record from the tracked runner, independently validate exact source/component/interpreter/module/Railway identities, exact `-I -B` execution, source/write proof, two equal vectors, canonical self-hash, and all-zero external I/O, and withhold discovery until PASS. |
| Python imports create ignored bytecode/cache residue or a mode writes outside its explicit control/candidate set | Require exact ordered `-I -B` and no `PYTHON*` child variable in preflight, target probe, live child, and every supporting OPS-01R source-loading producer/validator/launcher; bind an independently captured full-source manifest, two residue scans, authenticated pre-staging baseline and complete post delta, normalized path guard, and exact mode write set in every authorization/result hash; independently enumerate source and staging state; and run positive and mutation tests for all bounded entry points. |
| A validator cannot receive its independently reviewed expected identity without inventing a sidecar, wrapper, environment variable, or circular hash input | Bind `--expected-identity-stdin` in every applicable exact validator vector; accept only one bounded canonical ASCII JSON dataclass object plus LF and EOF on non-TTY stdin; reject every alternate channel and malformed stream with a stable code; retain no stdin bytes; use the same externally reviewed discovery object for authorization and result continuity and the same `Ops01V5ExpectedIdentity` for capture-time and permanent semantics. |
| A self-reporting result or authorization creates a direct or temporal manifest/hash cycle | Exclude only the exact authorization/self-reporting file or live candidate root from its own staging manifest; retain path-guard enforcement; validate canonical self-hashes or candidate inventory/ledger semantics separately; and build discovery/live authorization through an exact precreated-placeholder, baseline, in-place-finalization, identical-recapture sequence before PO authorization. |
| Source or executable identity drifts after preflight | Bind the detached source commit/root/state/full manifest and runner, validator, projector, exact `-I -B` launcher/child interpreter/argv/environment, preflight, discovery, and CLI identities in the exact live authorization; recheck source, residue, authenticated staging baseline/write set, and executable identities before the sole launch and stop on mismatch. |
| Caller or Railway-injected variables override intended rails or credentials | Rebuild the child environment from a minimal allowlist, exclude caller auth/vendor/birth/Python/provider-force/permissive variables, require only the discovery-proven target identity fields, preserve closed read-only rails, and test seeded conflicts. |
| Discovery policy admits a mutating, seventh, improvised, or linked-context command | Independently validate exact `hde_epic038.ops01r.discovery_authorization.v1` and embedded `hde_epic038.ops01r.discovery_policy.v1` bytes before any CLI call; require the exact six-stage roster, one selected template per stage, prohibited-family and argv rules, unlinked empty working directory, six-process limit, sanitization, and stable failure codes. |
| Railway selection reaches the wrong target or depends on linked context | The validated discovery result must prove installed CLI identity, exact explicit-target nonlinked argv, exact target, and at least one identity field for each target dimension. No `--no-local` flag or injected field name is assumed by this CRD. |
| Producer, authorization, summary, and validator bind different expected vectors | Authorization counts are the sole authoritative serialized vector. Independently validated preflight must equal it; summary expected must equal it; `Ops01V5ExpectedIdentity.expected_call_counts_sha256` is independently recomputed only from canonical authorization counts; and summary actual must equal it. Any serialized vector-hash key is rejected. |
| Live attempt exceeds its preflighted graph while an adapter hides multiple operations | One launch, prospective denial before every counted operation, zero vendor/retry/fallback values, and terminal field-by-field equality to the authorization-owned ten-field vector. Focused tests add one to each nonzero field and attempt the first call for every zero field. |
| Candidate is partially integrated | Full-inventory copy, candidate-root validation, atomic PR-C, then updater-owned companions. |
| Post-integration validation depends on temporary control files or claims to recapture absent temporary state | Capture-time validation recomputes the actual source and staging trees while they exist. The success summary embeds the complete hash-bound non-secret authorization and exact preflight/discovery/count/source-write identities; the independent expected identity is copied from reviewed capture facts, not inferred solely from the packet. Permanent PR-C/release validation checks only retained canonical proof and those external identities. Failure material is never an integration input. |
| Main advances between capture and integration | Require candidate-source ancestry, exact authorized validator/projector hashes on the PR-C base, and independent full candidate validation. Unrelated advancement is allowed; relevant incompatibility blocks integration for separate review. |
| Scope drifts into `pg-bridge` | Explicit repository/service prohibition and no demonstrated bridge defect. |
| Evidence change is mistaken for completion | Required nonclaims in packet, PF10, PR description, and CRD approval boundary. |

### Rollback and fail-closed behavior

- Missing or unapproved Current Implementation Plan revision stops before implementation reliance.
- Development failures stop before OPS.
- Preflight record, exact producer/validator Python argv/environment, source-manifest/cache, authenticated staging baseline/delta, write-set, or independent-validation failures stop before discovery authorization.
- Discovery-authorization or static-policy isolation failures stop before the first CLI subprocess; immediate dispatch, target-probe, supporting entry-point, or discovery-result argv/environment/source/cache/authenticated-staging/write failures stop before live authorization.
- Independent live-authorization-validator failure or any redundant prelaunch validator/launcher/child argv, environment, source, cache, authenticated-staging, or write-contract mismatch stops before marker creation or execution.
- A pre-marker validation failure stops without launch. Successful exclusive marker creation, a started or indeterminate subprocess state, or any later live failure consumes authority and stops without retry.
- Capture-time-validator argv, external source/live-pre/live-post-staging identity, actual source/cache/staging-write, candidate-ledger, nested permanent-packet, or semantic validation failure leaves no admissible candidate. Later permanent-validator argv, retained-proof, external-identity, or semantic failure stops before tracked changes without claiming temporary-tree recapture.
- PR-C failures revert the complete integration unit while independent PR-A fixes remain.
- Mixed schema/evidence/companion states are invalid.
- No rollback path authorizes a fresh live attempt, environment substitution for `-B`, cache redirection, source mount, or broader platform mechanism.

### Residual operational unknowns and gates

The following values are deliberately unresolved and execution-blocking until their named gate supplies exact evidence:

- `UNVERIFIED HISTORICAL REPORT`: external failed-run occurrence, traceback, runner/ledger bytes, staging state, counters, provider boundary, no-I/O result, and attempt consumption. These remain non-operative and are never execution inputs.
- `UNKNOWN PENDING PREFLIGHT`: exact direct-connection, direct-SQL, and bridge-HTTP counts for the deterministic full success path, plus the independently captured source-manifest and preflight-staging-baseline identities and resulting preflight identity hash.
- `UNKNOWN PENDING PREFLIGHT`: candidate Railway CLI path, resolved path, and executable hash.
- `UNKNOWN PENDING DISCOVERY`: Railway CLI version.
- `UNKNOWN PENDING DISCOVERY`: exact explicit-target, nonlinked run argv and supported flag/value ordering.
- `UNKNOWN PENDING DISCOVERY`: exact project, environment, and service identifiers and the closed injected target-identity field contract.
- `UNKNOWN UNTIL APPROVED PLAN/PR-A MERGE/PREFLIGHT`: approved next-version Current Implementation Plan identity; exact PR-A merge commit; immutable detached source root; runner/validator/projector hashes; and preflight hash.
- `UNKNOWN UNTIL LIVE AUTHORIZATION/ARTIFACT CREATION`: independently captured live pre-staging-manifest identity; capture-time live post-staging-manifest identity; run ID; candidate root; authorization hash; candidate checksums; capture-time admission outcome; and any PR-C commit.

These are not treated as verified current facts and do not block CRD review or closed-rails PR-A work. Preflight unknowns block discovery authority; discovery unknowns block live authorization; later artifact identities block any action that consumes them until exact-pinned. Failure to derive or match any value is a stop condition, not a delegated architecture choice.

## 12. Approval Limitations and Nonclaims

This CRD:

- does not implement any fix;
- does not edit the product repository;
- does not edit `r1` or the current `r6` planning file;
- does not itself authorize or complete the separately authorized next-version Current Implementation Plan revision required before implementation reliance;
- does not edit PF10;
- does not edit PF-Canon, an ADR file, or PF09;
- does not move PF09 status;
- does not create QA PASS or rerun historical QA;
- does not execute OPS or authorize the new OPS attempt;
- does not claim a completed source-manifest capture, authenticated pre-staging baseline/delta, cache-residue scan, write-set validation, read-only mount, cache-redirection setup, generalized filesystem sandbox, or host-wide filesystem immutability;
- does not authorize an expected-identity sidecar, wrapper, environment, interactive, or retained-stdin evidence channel; the proposed canonical stdin transport is read-only, ephemeral, and bounded to the exact validator CLI modes;
- does not claim that permanent PR-C or release validation can recapture temporary source, control, or non-candidate staging trees after they no longer exist;
- does not authorize deployment, restart, relink, variable mutation, database write, migration, grant, role, schema change, or vendor call;
- does not inspect, update, deploy, or assign a defect to the `pg-bridge` repository or service;
- does not integrate the failed or future candidate packet;
- does not satisfy an acceptance token;
- does not accept provisional implementation;
- does not declare PR readiness or authorize merge;
- does not reopen or alter PR 359;
- does not close the remediation slice; and
- does not close HDE-EPIC038.

IA approval means only that the technical decisions, causal coverage, minimum scope, schemas, ownership, compatibility, migration, validation, rollback, plan consequences, canon consequences, and boundaries in this CRD are technically approved as authoritative inputs to a separately authorized next-version Current Implementation Plan revision. That plan revision must be approved before implementation relies on `RSC-001` through `RSC-005` or `ADR-CANON-004`, unless a newer explicit PO instruction changes current PF10 posture. Approval does not itself revise a plan or authorize implementation. PF10 living-context recording and permanent PF12/PF14/PF09.6 drainage remain separate, non-gating documentation axes and are neither completed nor authorized by this CRD.

## 13. Questions for the Implementation Agent

None.

## 14. Implementation Agent Review Gate

### APPROVE

IA should return `APPROVE` only if all of the following are true:

1. Every submitted finding and material action is classified exactly once; `BLK-001` and `ACT-002` are explicitly `UNVERIFIED`, the §4 record is self-contained, and no operative cause or control depends on unavailable failed-run evidence.
2. `BUG-001`, `BUG-002`, and `BUG-003` have complete causal chains, while `STALE-001` and `STALE-002` create regression coverage but no redundant production scope.
3. The CRD and ADR do not themselves edit plans; `r1` remains the epic-scope baseline; the CRD is the authoritative input to a separately authorized next-version Current Implementation Plan revision; and implementation reliance is prohibited until that revision is approved unless a newer explicit PO instruction changes current PF10 posture.
4. The approved-plan -> PR-A -> OPS-01R -> PR-C sequence is the minimum coherent migration, lets independent P1/P2 repairs land before OPS, and prevents additional PR 359 growth.
5. `RSC-001` can regenerate exactly two EPIC024 primaries without executing or reopening historical QA and preserves historical statuses byte-semantically.
6. `RSC-002` closes the reported raw-marker forms with an exact, testable, fail-closed contract while preserving the merged credential and provider-provenance controls.
7. `RSC-003` supplies a complete implementable shared projection API, strict invariants, exact schema versions, exact paths and keys, explicit exclusions, stable ownership, compatibility, migration, validation, and rollback.
8. `ADR-CANON-004` is independently reviewable, remains `PROPOSED - PENDING IA TECHNICAL APPROVAL`, correctly classifies `AMENDS`, and has the corrected plan-adoption sequence and exact permanent drainage targets.
9. `RSC-004.A` defines one complete `hde_epic038.ops01r.preflight.v1` record with exact recursive rosters, paths, source/component/interpreter/module/Railway identities, exact ordered `-I -B` producer and validator argv, canonical external expected-identity stdin, empty `PYTHON*` environment-name roster, independent full-source and authenticated pre-staging identities, no cache residue, exact pre/post staging delta and sole preflight write, two-run determinism, zero-I/O counts, canonical self-hash, sole producer, independent validator/API, failure codes, and authorization binding.
10. `RSC-004.B` defines one complete `hde_epic038.ops01r.discovery_authorization.v1` and `hde_epic038.ops01r.discovery_policy.v1`, independently valid before any CLI call, with exact non-circular placeholder/finalization construction, exact `-I -B` authorization-validator, producer, result-validator, and no-write target-probe vectors, canonical expected-identity stdin proving continuity from PO-authorized discovery bytes through result validation, authenticated staging baseline/delta and source/cache/write result proof, narrowly excluded self-report validation, immediate pre-dispatch enforcement, six-stage/templates/prohibited-family/unlinked/sanitization/hash/path/API/failure contracts; successful output closes every runtime CLI/target/argv/environment/identity fact.
11. `RSC-004.C` and `.D` define non-circular live-authorization construction; bind exact `-I -B` live-authorization-validator, launcher, child, capture-time-validator, and permanent candidate-validator vectors plus their applicable canonical expected-identity stdin; require independent live-authorization PASS before marker/provider boundaries; bind empty `PYTHON*` environment names, independent source-manifest and live pre/post-staging-manifest identities, narrowly excluded candidate/failure outputs with independent containment/ledger/semantic validation, and exact authenticated live success/failure deltas/write sets; define one launch, no retry/fallback, authorization-owned expected counts, a derived-only external expected-vector hash, exact summary/actual equality, capture-time actual-tree admission, and later permanent packet validation without an ephemeral-tree claim.
12. `RSC-005` independently validates the self-contained packet against every closed expected identity and prevents partial integration or permanent dual-version admission.
13. The `pg-bridge` repository and service are unambiguously outside implementation scope.
14. PF09 `HDE-DIST001.4`, `.6`, `.9`, and `HDE-DIST005.2` remain `Partial`; `HDE-DIST001.11` remains `Optional`; no EPIC024 row is reopened and no status moves.
15. PF10 living-context recording and permanent PF drainage remain non-gating, and all nonclaims and rollback stops prevent evidence, QA, acceptance, deployment, or closeout overclaiming.

### RETURN FOR REVISION

IA should return `RETURN FOR REVISION` if any of the following is true:

- a live finding is incorrectly treated as stale, a stale finding creates redundant production scope, or an unverified external failed-run claim is represented as confirmed or made operative;
- the EPIC024 proposal can run `_check_specs` or change any historical output beyond the exact two primaries and updater-owned companions;
- the raw scanner remains JSON-only, accepts shell expansions, or broadens into an unbounded content scanner;
- DDL projection behavior remains duplicated, silently skips malformed included fields, normalizes type aliases, or claims full semantic parity;
- evidence, preflight, discovery-authorization, discovery-policy, discovery-result, or identity schemas, paths, keys, producer/consumer owners, unknown-key posture, failure codes, or migration are incomplete;
- PR-A makes candidate-v5 validation a default release-admission path or PR-C permits default v4/v5 dual admission;
- the preflight record leaves any field, nested roster, path, owner, module origin, exact `-I -B` producer/validator argv, canonical expected-input transport, environment rule, source-manifest/cache predicate, authenticated pre-staging baseline/delta, write set, canonicalization, self-hash, zero-I/O structure, validator decision, or failure code to implementation inference, or the runner/validator can reach credentials, provider construction, candidate writes, source/cache writes, unlisted staging writes, or external I/O in preflight mode;
- the discovery authorization or policy can add a seventh stage, mutating command family, linked-context fallback, unapproved flag/template, shell/module/console-script execution, secret-like output, target probe or supporting source-loading process without exact `-I -B`, target-probe write, self-referential result hash, authorization baseline captured through a temporal cycle, unauthenticated staging baseline, alternate expected-input channel, result validation without continuity to the independently PO-authorized discovery hash, source/cache residue, unlisted discovery write, or CLI call before independent authorization and immediate dispatch PASS;
- the OPS design guesses or leaves unvalidated any mandatory target, CLI, argv, nonlinked behavior, injected identity field, or external expected identity; omits, duplicates, substitutes, reorders, or environment-replaces `-I` or `-B` or the required `--expected-identity-stdin` selector in any applicable bound vector; accepts expected identity from a producer, file, sidecar, argv value, environment, default, interactive input, noncanonical stdin, or any channel outside the exact direct-API exception for checked-in `OPS01_V5_EXPECTED`; lacks independent live-authorization PASS before marker/Railway/provider boundaries; permits any self-reporting output or authorization to hash itself directly or temporally; uses an unbounded staging exclusion; fails to authenticate the applicable pre-staging baseline/delta or independently validate every excluded output/root; fails to perform capture-time actual-tree validation while temporary state exists or later claims permanent validation recaptured that absent state; fails to detect source mutation, `__pycache__`, `.pyc`, symlink escape, or any write outside the exact mode set; exceeds the authorized policy or six-command maximum; permits mutable or unbound source/runner/validator/projector/interpreter identity, inherited caller credentials, unlisted child variables, reuse, retry, fallback, tracked writes, Railway mutation, database mutation, vendor calls, or `pg-bridge` work;
- live admission uses a ceiling, range, or less-than-or-equal predicate; serializes `expected_call_counts_sha256`; derives it from anything other than canonical authorization counts; permits preflight, authorization, summary expected, external derived hash, or actual counts to disagree; or lacks required mutation tests;
- success evidence depends on temporary control files after integration, failure material can become governed success evidence, copied primaries can diverge from the reviewed candidate ledger, or candidate integration can occur before independent review or without full updater convergence;
- PF10 section 2.9 or permanent PF drainage is made a prerequisite, sole authority, acceptance condition, closeout gate, or substitute plan revision, or factual updates are represented as complete before their facts exist;
- the CRD itself edits a plan, bypasses the required approved Current Implementation Plan revision, alters the `r1` epic-scope baseline, or implies PF09 movement, QA PASS, acceptance, deployment, merge, slice closure, or epic closure; or
- any material technical decision is deferred to IA.

## Revision Response Ledger

The current IA review v1.2 contains exactly one item, `REV-001`, handled exactly once below. Prior-review responses are not part of this ledger; they are preserved separately in the Historical Revision Response Archive.

### Revision item 1

- **REV ID:** `REV-001`
- **IA-required change:** Select and specify one exact import/write-isolation mechanism for every PR-A preflight, Railway target-identity probe, and live-child Python invocation; bind it in exact interpreter, argv, environment, filesystem, identity, and authorization contracts; make independent validators reject omission, substitution, or drift; add focused no-source-write/no-unlisted-write tests; and propagate the invariant through the plan-consequence matrix and validation sequence without new product, OPS, QA, PF09, or canon scope.
- **Disposition:** `RESOLVED`
- **Revised CRD section or item:** §1 source/version control; §2 Executive Summary; §3 authority gates; §4 RCA; §5 conflict and resolution posture; `CAUSE-004`; `RSC-003` result-summary execution/expected identity; complete `RSC-004.A` through `.D`; `RSC-005`; §8 ownership and boundaries; §9 technical requirements, matrix, adoption, validation, rollback, and exclusions; `ADR-CANON-004` linkage qualification and dependent validation; §10 PF10 prospective lineage; §11 architecture, risks, rollback, and unknowns; §12 nonclaims; §14 IA gates.
- **Affected `ADR-CANON-###` ID(s), or `None`:** None
- **Canon effect:** `none`
- **Change made or reason unresolved:** The revised CRD selects exact ordered `-I -B` execution as the sole bytecode/cache write control for preflight, target probe, and live child and applies the same rule to every supporting source-loading producer, validator, and launcher. It rejects every environment substitute and every case-folded `PYTHON*` child variable; binds exact argv, interpreter, canonical-stdin external expected identities, independently captured full-source manifests, authenticated pre-staging baselines and post deltas, two cache scans, normalized path guarding, and mode-specific write sets through preflight, discovery-authorization/result, live-authorization/result, and external expected identities; proves discovery-result continuity with the independently authorized discovery hash; supplies exact pre-boundary gates, including an independently invoked live-authorization validator before marker/Railway/provider activity; separates capture-time actual-tree admission from later permanent retained-packet validation so CI makes no ephemeral-tree recapture claim; and defines positive and mutation tests for all three modes and their supporting entry points. The bounded source/staging guard and read-only stdin transport create no sidecar, read-only-mount, cache-redirection, generalized sandbox, host-wide immutability, new operational attempt, QA, PF09, product, or canon scope.
- **Baseline, review, or permitted conditional-source evidence pointer:** IA Review v1.2 | `FND-001` and `REV-001`; Baseline v1.2 | `RSC-004.A` through `.D`, exact `-I` invocations and clean-source/sole-write claims; Repo evidence: Repo | GitHub read-only fetch of `.gitignore` at `main@78756e776f7fa598370235de6a72aa29fe045af9` | "The ignore policy contains exact `__pycache__/` and `*.pyc` entries, so Git-clean posture cannot independently prove cache-residue absence."
- **Permanent canon drainage target(s), or `None`:** None
- **IA acceptance condition:**
  1. The CRD names one exact bytecode/cache write-control mechanism and applies it consistently to preflight, discovery target probe, and live child.
  2. Exact interpreter/argv/environment/filesystem contracts and all corresponding authorization hashes bind that mechanism.
  3. Independent validators reject omission, substitution, or drift of the selected mechanism before any Railway or provider boundary.
  4. Focused tests prove that each mode creates or modifies no file beneath the detached source root and no path outside its explicitly authorized control or candidate write set, including no `__pycache__` directory or `.pyc` file when bytecode suppression is the selected control.
  5. The plan-consequence matrix and validation order state the same invariant without introducing new product, OPS, QA, PF09, or canon scope.
- **Acceptance condition satisfied:** Yes

## Conditional Source Record

### Repo ignored Python-cache posture

- **Triggering `REV-###` item:** `REV-001`
- **Affected `ADR-CANON-###` ID:** None
- **Source:** Repo
- **Exact locator or inspection method:** GitHub read-only file fetch, repository `amthorn78/glow-hdengine-v2`, path `.gitignore`, ref `78756e776f7fa598370235de6a72aa29fe045af9`.
- **Observed fact:** The file contains exact ignore entries `__pycache__/` and `*.pyc`.
- **Revision use:** Confirmed the IA review's bounded engineering concern that ordinary worktree-clean validation can omit Python cache residue; supported the independently captured full-source manifest and explicit residue scan. This Repo fact does not establish canon, implementation, QA, OPS, acceptance, or completion.

## Historical Revision Response Archive

The following five version-qualified responses preserve the complete resolved IA review v1.1 lineage carried by baseline v1.2. They are not current IA review v1.2 items, are excluded from the current Revision Response Ledger and current status calculation, and remain historical even where current v1.2 review numbering reuses `REV-001`.

### Revision item 1

- **Historical REV ID:** IA review v1.1 `REV-001`
- **IA-required change:** Replace every absolute no-plan-revision clause with the current PF10 posture: this CRD and ADR do not themselves edit plans; `r1` remains the approved epic-scope baseline; after technical approval this CRD is the authoritative input to a separately authorized next-version Current Implementation Plan revision; and implementation may not rely on `RSC-001` through `RSC-005` or `ADR-CANON-004` until that revision is approved unless a newer explicit PO instruction changes the PF10 posture.
- **Disposition:** `RESOLVED` in v1.2; preserved historical lineage, not a current-review item.
- **Revised CRD section or item:** §1 planning posture; §2; §3 Plan posture and Later authorities; every CAUSE/RSC plan consequence; §8 boundaries; complete §9 plan/adoption lifecycle; `ADR-CANON-004` adoption and validation; §10 PF10 consequence; §11 plan/PF validation; §12; §14.
- **Affected `ADR-CANON-###` ID(s), or `None`:** `ADR-CANON-004`
- **Canon effect:** `none`
- **Change made or reason unresolved:** The complete CRD distinguishes direct document mutation from the required later plan-revision lane. IA approval precedes a separately authorized and approved next-version Current Implementation Plan; only then may separate implementation authority be used. `r1` remains the epic-scope baseline. PF10 living notes and permanent PF drainage remain non-gating.
- **Baseline, review, or permitted conditional-source evidence pointer:** IA Review v1.1 | `REV-001`; PF10 - PF10-HDE-Build-Notes v12.2.7 | §2.4 `Governing posture` | "The Implementation Plan must be revised before implementation relies on these decisions."
- **Permanent canon drainage target(s), or `None`:** Existing `ADR-CANON-004` targets remain exact and unchanged: PF12 §8.6.3.4; PF14 §20.3; PF09.6 rows `HDE-DIST001.4`, `.6`, `.9`, `.11`, and `HDE-DIST005.2`.
- **IA acceptance condition:** Every plan-consequence and adoption clause consistently permits and requires the separately authorized Current Implementation Plan revision before implementation reliance; no clause states that no revision is authorized or required; later PF drainage remains explicitly non-gating.
- **Acceptance condition satisfied:** Yes in v1.2; preserved unchanged.

### Revision item 2

- **Historical REV ID:** IA review v1.1 `REV-002`
- **IA-required change:** Make the failed-run treatment self-contained; include or classify the traceback, runner/ledger identities, staging relationship, counters, provider-boundary method, no-action method, and provenance; mark unsupported elements `UNVERIFIED`; narrow `CAUSE-004`; and ensure no mandatory control depends solely on unavailable material.
- **Disposition:** `RESOLVED` in v1.2; preserved historical lineage, not a current-review item.
- **Revised CRD section or item:** §1 source posture; §2 item 4; §3 Later authorities; §4 `BLK-001`, `ACT-002`, RCA, observed actions, and complete minimal evidence record; §5 conflict/deferral; `CAUSE-004`; `CAUSE-005`; `RSC-004`; §10 PF10 consequence; §11 evidence, diagnostics, searches, rationale, risks, unknowns; §14.
- **Affected `ADR-CANON-###` ID(s), or `None`:** None
- **Canon effect:** `none`
- **Change made or reason unresolved:** Every alleged failed-run datum is preserved only in one self-contained table with its provenance, available verification method, `UNVERIFIED` status, and zero operative consequence. The exact traceback and methods are stated unavailable. Four current-Repo searches are recorded as zero-hit verification limits, not proof of non-occurrence. `CAUSE-004` is the prospective one-attempt source/import and launch-contract limitation.
- **Baseline, review, or permitted conditional-source evidence pointer:** IA Review v1.1 | `REV-002`, FND-002, and Material `UNVERIFIED` claims; Repo | four case-sensitive exact searches of current `amthorn78/glow-hdengine-v2` | zero hits for the alleged runner hash, alleged ledger hash, `051XSWvs`, and `ModuleNotFoundError`.
- **Permanent canon drainage target(s), or `None`:** None
- **IA acceptance condition:** A reviewer using only the next CRD, plans, current PF-Canon, and scoped Repo inspection can verify every retained `BLK-001` premise and distinguish confirmed facts from Unknowns; no operative claim depends on an unavailable source.
- **Acceptance condition satisfied:** Yes in v1.2; preserved unchanged.

### Revision item 3

- **Historical REV ID:** IA review v1.1 `REV-003`
- **IA-required change:** Define the complete preflight control-record contract, including exact schema and recursive rosters, expected and actual count structures, source/component/interpreter/module/Railway identities, deterministic two-run fields, path, sole producer, independent validator/API, canonical bytes, self-hash omission, failure codes, and live-authorization binding.
- **Disposition:** `RESOLVED` in v1.2; preserved historical lineage, not a current-review item.
- **Revised CRD section or item:** `CAUSE-004`; `RSC-003` result-summary/expected identity; complete `RSC-004.A`; `RSC-004.C` and `.D`; `RSC-005`; §8 ownership; §9 requirements, matrix, adoption, validation, stops; §11 rationale, safeguards, rollback, unknowns; §14.
- **Affected `ADR-CANON-###` ID(s), or `None`:** None
- **Canon effect:** `none`
- **Change made or reason unresolved:** `hde_epic038.ops01r.preflight.v1` received one exact path convention, closed top-level and nested rosters, exact ten-field vector, exact nine-field zero-I/O object, deterministic two-run structure, source/component/interpreter/module/Railway identities, nonclaims, canonical self-hash, sole producer, independent expected-identity dataclass and validator API, exact failure codes, and cryptographic authorization binding. V1.3 preserves that decision and adds only the current `REV-001` isolation/write and expected-input details.
- **Baseline, review, or permitted conditional-source evidence pointer:** IA Review v1.1 | `REV-003`; PF27 - PF27-Canon-Plan-Templates v1.9.5 | `Repository locus validation and file minting posture` | "Plans MUST NOT include any repository path, module home, command, or uniqueness claim ... that cannot be confirmed via canon or repo inspection."
- **Permanent canon drainage target(s), or `None`:** None
- **IA acceptance condition:** One implementation can be written without choosing any new preflight field, schema, identity, path, ownership, or validation decision; mutation tests can independently reject every unknown or mismatched preflight fact.
- **Acceptance condition satisfied:** Yes in v1.2; preserved and extended consistently in v1.3.

### Revision item 4

- **Historical REV ID:** IA review v1.1 `REV-004`
- **IA-required change:** Define a complete discovery-authorization and static-policy input contract with exact schema/key sets, policy entries, six stages, deterministic template selection, prohibited families, source/executable/preflight/unlinked-workdir bindings, subprocess limit, sanitization, identity, independent APIs, paths, and stable failure codes before any CLI call.
- **Disposition:** `RESOLVED` in v1.2; preserved historical lineage, not a current-review item.
- **Revised CRD section or item:** `CAUSE-004`; `RSC-003` identities; complete `RSC-004.B`; `RSC-004.C` and `.D`; `RSC-005`; §8 ownership; §9 requirements, matrix, adoption, validation, stops; §10 PF10 lineage; §11 rationale, safeguards, rollback, unknowns; §14.
- **Affected `ADR-CANON-###` ID(s), or `None`:** None
- **Canon effect:** `none`
- **Change made or reason unresolved:** The CRD defines exact `hde_epic038.ops01r.discovery_authorization.v1` and `hde_epic038.ops01r.discovery_policy.v1` contracts, recursively closed input objects, a six-entry stage matrix, structured argv token grammar, one-template selection, permitted/prohibited families, sanitization, canonical self-hash, unlinked empty workdir, six-process cap, independent pre-CLI authorization and post-run result APIs, exact paths, and exact authorization/result failure-code rosters. Runtime version, IDs, argv, and identity fields remain bounded discovery results. V1.3 preserves that decision and adds exact `-I -B`, source/write, and external expected-input continuity.
- **Baseline, review, or permitted conditional-source evidence pointer:** IA Review v1.1 | `REV-004`; PF07 - PF07-Canon-Glow-Infrastructure v2.2.4 | Front Matter `Change control`, `PS discovery for discoverable infrastructure facts`; PF27 - PF27-Canon-Plan-Templates v1.9.5 | `Operational unknowns, deferral, OPS discovery, and open-rails posture`.
- **Permanent canon drainage target(s), or `None`:** None
- **IA acceptance condition:** A reviewer can validate the discovery authorization and policy before any CLI subprocess; an implementer cannot add a seventh stage, mutating argv, linked-context fallback, or unapproved flag without violating an exact closed rule.
- **Acceptance condition satisfied:** Yes in v1.2; preserved and extended consistently in v1.3.

### Revision item 5

- **Historical REV ID:** IA review v1.1 `REV-005`
- **IA-required change:** Select one non-circular home and equality chain for `expected_call_counts_sha256`; the safest bounded choice is a derived-only independent identity over canonical `authorization.expected_call_counts`, with exact summary and actual equality and no serialized hash key.
- **Disposition:** `RESOLVED` in v1.2; preserved historical lineage, not a current-review item.
- **Revised CRD section or item:** `RSC-003` result-summary and `Ops01V5ExpectedIdentity`; `RSC-004.A`, `.C`, and `.D`; `RSC-005`; §9 requirements, matrix, adoption, validation; `ADR-CANON-004` validation; §11 safeguards; §14.
- **Affected `ADR-CANON-###` ID(s), or `None`:** `ADR-CANON-004`
- **Canon effect:** `none`
- **Change made or reason unresolved:** Authorization counts are the sole authoritative serialized vector. Validated preflight must equal authorization; summary expected must equal embedded authorization; the validator independently recomputes the derived hash only from canonical authorization counts and compares the external expected identity; summary actual must equal authorization. The hash is absent from preflight, authorization, and result-summary rosters, and any added key fails recursively.
- **Baseline, review, or permitted conditional-source evidence pointer:** IA Review v1.1 | `REV-005`; Baseline v1.1 | result-summary roster, authorization roster, and `Ops01V5ExpectedIdentity`.
- **Permanent canon drainage target(s), or `None`:** Existing `ADR-CANON-004` targets remain exact and unchanged: PF12 §8.6.3.4; PF14 §20.3; PF09.6 rows `HDE-DIST001.4`, `.6`, `.9`, `.11`, and `HDE-DIST005.2`.
- **IA acceptance condition:** The next CRD defines one non-circular source of truth and one exact recomputation/equality chain for the expected vector and its hash; every positive and mutation test can determine the authoritative value without inference.
- **Acceptance condition satisfied:** Yes in v1.2; preserved unchanged.

## Historical Conditional Source Record

The following headings and records preserve valid baseline v1.2 provenance for IA review v1.1. They are not current v1.3 conditional-source consultations, are excluded from the current `Conditional Source Record`, and do not imply that Sekhmet re-inspected those sources for current `REV-001`.

### PF10 plan-adoption posture

- **Historical triggering item:** IA review v1.1 `REV-001`
- **Affected `ADR-CANON-###` ID:** `ADR-CANON-004`
- **Source:** `PF10-HDE-Build-Notes v12.2.7`
- **Exact locator:** §2.4 `PR-04 HDE-EPIC038 — Approved Rescope and Canon Decisions`, subsection `Governing posture`; historical Library path `/Glow HDE 3.0/PF10-HDE-Build-Notes-v12.2.7.md`.
- **Relied-on lines copied verbatim:**

  > * The approved CRD may govern revision of the current HDE-EPIC038 Implementation Plan. The Implementation Plan must be revised before implementation relies on these decisions.  
  > * Approval of the CRD and these ADRs is not implementation authorization, implementation acceptance, PR merge approval, QA PASS, OPS completion, PF09 movement, token satisfaction, deployment authorization, persistence authorization, slice acceptance, or epic closeout.  

- **Historical revision use:** Corrected every plan-consequence and adoption clause, including `ADR-CANON-004`, without making PF10 or permanent drainage an execution substitute.

### Repo failed-run verification boundary

- **Historical triggering item:** IA review v1.1 `REV-002`
- **Affected `ADR-CANON-###` ID:** None
- **Source:** Repo
- **Exact locator or inspection method:** Historical GitHub code search, current indexed `amthorn78/glow-hdengine-v2`; four independent case-sensitive exact searches for `aca1f0e09810cc7a451c07bd6660015e3d071ac50d930116177e60aa8aa8f15f`, `4dff85b6e55571ca49fae25f06dd9a19c23234d0c46c5c4a37225380fc21b8d6`, `051XSWvs`, and `ModuleNotFoundError`.
- **Observed fact:** Each historical search returned zero current-Repo hits. This proves only that current Repo could not validate the alleged external-run identity or traceback term; it does not prove that no external run occurred.
- **Historical revision use:** Marked every unsupported `BLK-001` and `ACT-002` element `UNVERIFIED`, created the self-contained claim-disposition record, and removed failed-run provenance from operative causality.

### PF27 preflight reproducibility posture

- **Historical triggering item:** IA review v1.1 `REV-003`
- **Affected `ADR-CANON-###` ID:** None
- **Source:** `PF27-Canon-Plan-Templates v1.9.5`
- **Exact locator:** `Purpose & scope`, subsection `Repository locus validation and file minting posture (hard)`; historical Repo path `docs/pfcanon/PF27-Canon-Plan-Templates-v1.9.5.md` at `78756e776f7fa598370235de6a72aa29fe045af9`.
- **Relied-on lines copied verbatim:**

  > * Validated references only. Plans MUST NOT include any repository path, module home, command, or uniqueness claim (for example, “only create_app factory”) that cannot be confirmed via canon or repo inspection.
  > * File minting is allowed. When a plan mints new files or new evidence outputs, it MUST name the exact repository paths and filenames that will be created and the exact primary evidence files that will be produced.

- **Historical revision use:** Closed the preflight schema, path, owner, identity, canonicalization, validation API, and mutation/failure contract so a later plan need not invent a repository locus or control record.

### PF07 and PF27 bounded discovery posture

- **Historical triggering item:** IA review v1.1 `REV-004`
- **Affected `ADR-CANON-###` ID:** None
- **Source:** `PF07-Canon-Glow-Infrastructure v2.2.4`
- **Exact locator:** Front Matter, `Change control (titles-only cross-refs)`, bullet `PS discovery for discoverable infrastructure facts`; historical Repo path `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.2.4.md` at `78756e776f7fa598370235de6a72aa29fe045af9`.
- **Relied-on lines copied verbatim:**

  > * **PS discovery for discoverable infrastructure facts.** When a PF07-owned fact needed by a plan, implementation guide, QA plan, OPS task, or remediation guide is missing but can be safely discovered by the PO through bounded OPS discovery or a bounded PO-authorized open-rails check, the artifact MUST route the unknown to that discovery work rather than treating the missing fact as automatic deferral.
  > This does not authorize guessing, secret exposure, uncontrolled external action, or agent-performed OPS.

- **Source:** `PF27-Canon-Plan-Templates v1.9.5`
- **Exact locator:** `Purpose & scope`, subsection `Operational unknowns, deferral, OPS discovery, and open-rails posture (hard)`; historical Repo path `docs/pfcanon/PF27-Canon-Plan-Templates-v1.9.5.md` at the same commit.
- **Relied-on lines copied verbatim:**

  > * If a missing operational fact can be safely discovered, confirmed, or recorded by the PO, the plan MUST route a bounded OPS discovery task instead of deferring.
  > * Open-rails work must be bounded, PO-authorized, secret-safe, and evidence-recorded.

- **Historical revision use:** Defined the exact pre-execution discovery authorization, static policy, six stages, template-selection and prohibited-command rules, unlinked workdir, sanitization, independent APIs, canonical identities, and failure codes while leaving installed CLI and target facts as bounded runtime results.

## 15. Revision History

| Version | Date | Author | State | Summary |
| --- | --- | --- | --- | --- |
| `v1.0` | `2026-07-18` | Sekhmet | Pending IA technical review | Initial post-PR359 rescoping CRD derived from the complete active debugging flow, the four submitted findings, the DDL architectural analysis, the failed OPS recapture RCA, merged PR 359 at `78756e776f7fa598370235de6a72aa29fe045af9`, current Repo loci, current PF-Canon, PF10 v12.2.7, and the r1/r6 historical execution baselines. |
| `v1.1` | `2026-07-18` | Sekhmet | Ready for IA re-review | Resolved IA review v1.0 `REV-001` through `REV-005`: corrected PF10/ADR authority, replaced unverified Railway facts with bounded discovery, reduced OPS to four causally justified controls, required exact call-vector equality, and completed `ADR-CANON-004` (`AMENDS`) for the HDE-EPIC038 DDL identity-projection topic with permanent drainage to PF12 §8.6.3.4, PF14 §20.3, and PF09.6. |
| `v1.2` | `2026-07-18` | Sekhmet | Ready for IA re-review | Resolved IA review v1.1 `REV-001` through `REV-005`: required the separately authorized and approved Current Implementation Plan revision before implementation reliance; made failed-run provenance self-contained and non-operative where `UNVERIFIED`; closed preflight and discovery-authorization/policy contracts; and made the expected-vector hash derived-only. Materially revised `ADR-CANON-004` (`AMENDS`) adoption and validation for the HDE-EPIC038 DDL identity-projection topic while retaining exact permanent drainage to PF12 §8.6.3.4, PF14 §20.3, and PF09.6 rows `HDE-DIST001.4`, `.6`, `.9`, `.11`, and `HDE-DIST005.2`. |
| `v1.3` | `2026-07-18` | Sekhmet | Ready for IA re-review | Resolved IA review v1.2 `REV-001`: selected exact ordered `-I -B` bytecode/write isolation for preflight, Railway target probe, and live child; applied the same rule to supporting source-loading producers, validators, and launcher; bound argv, environment, canonical-stdin external expected identities, independent source manifests, authenticated pre-staging baselines/deltas, cache scans, and exact per-mode write sets through every affected hash/schema; added independent pre-boundary gates, including discovery-result continuity and live-authorization validation before authority consumption; separated capture-time actual-tree admission from permanent retained-packet validation; added focused tests; and propagated the invariant through ownership, plan consequences, validation, rollback, and nonclaims. Current `REV-001` has no canon effect. `ADR-CANON-004` remains `PROPOSED - PENDING IA TECHNICAL APPROVAL`, effect `AMENDS`, for the exact affected topic “Glow-owned DDL identity projection and projection-only semantics for the HDE-EPIC038 OPS-01 provider-parity evidence family”; its decision/effect are unchanged, its dependent operational-validation cross-reference now names the source/write qualification, and its permanent drainage targets remain exactly PF12 §8.6.3.4, PF14 §20.3, and PF09.6 rows `HDE-DIST001.4`, `.6`, `.9`, `.11`, and `HDE-DIST005.2`. |

STATUS: Approved

# Approval notes:

# Rescoping CRD Review - HDE-EPIC038 - POST-PR359-REMEDIATION

## 1. Document Control

- **Review version:** `v1.3`
- **Reviewed CRD ID and version:** `CRD-HDE-EPIC038-POST-PR359-REMEDIATION`, `v1.3`
- **Epic ID and name:** `HDE-EPIC038`, Distillation Pass 3
- **PR or slice ID:** `POST-PR359-REMEDIATION`
- **Reviewer role:** Glow Implementation Agent
- **PO approval posture:** PO authorization to rescope is established. This review assesses technical correctness and execution readiness only.
- **CRD_FILE:** `rescoping-crd-hde-epic038-post-pr359-remediation-v1.3.md`
- **APPROVED_IMPLEMENTATION_GUIDE_FILE:** `r1 Epic Plan HDE-EPIC038.md`
- **CURRENT_IMPLEMENTATION_PLAN_FILE:** `r6 Implementation Plan HDE-EPIC038.md`
- **REPO_ROOT_OR_GITHUB:** `glow-hdengine-v2`
- **Repo inspection mode:** Connected GitHub repository, read-only
- **Observed Repo revision:** `amthorn78/glow-hdengine-v2`, default branch `main`, current reviewed HEAD `78756e776f7fa598370235de6a72aa29fe045af9`
- **Preceding merged PR:** PR 359, merged into `main` as `78756e776f7fa598370235de6a72aa29fe045af9`; PR head `c6e689edefdac1f832faed6ad19f504eefbda696`; base `fbb1639890a89858c17ba8ac1f09af410df15d8f`
- **Current PF-Canon consulted:**
  - `PF10-HDE-Build-Notes`, current `v12.2.7`, Addendum 2.4 `PR-04 HDE-EPIC038 — Approved Rescope and Canon Decisions`, subsection `Governing posture`, plus bounded exact-topic searches for this post-PR359 rescope
  - `PF06-Canon-Epic-Process-Guide`, current `v2.3.5`, `0.2 Policy and principles`, `# 1) EPIC PLAN → CRD`, and `# 2) IMPLEMENTATION GUIDE`
  - `PF07-Canon-Glow-Infrastructure`, current `v2.2.4`, Front Matter `Change control`, `PS discovery for discoverable infrastructure facts`
  - `PF09.6-Canon-HDE-Build-Checklist-Distillation`, current `v1.1.2`, `HDE-DIST001.4`, `HDE-DIST001.6`, `HDE-DIST001.9`, `HDE-DIST001.11`, and `HDE-DIST005.2`
  - `PF12-Canon-HDE-Schemas-and-Artifacts`, current `v2.7.8`, `§8.6.3.4 Gates, runtime, DB, and ops evidence`
  - `PF14-Canon-HDE-Mechanics-Guide`, current `v3.4.3`, `§20.3 Bridge parity mechanics` and `§20.3.1 Bridge-consistency checker fallback contract`
  - `PF27-Canon-Plan-Templates`, current `v1.9.5`, `Repository locus validation and file minting posture (hard)` and `Operational unknowns, deferral, OPS discovery, and open-rails posture (hard)`
- **Reviewed canon-changing ADR:** `ADR-CANON-004 — Versioned Glow-Owned DDL Identity Projection for OPS Provider Evidence`
- **ADR result:** `APPROVED`, canon effect `AMENDS`, limited to the exact DDL identity-projection and projection-only evidence semantics stated in the CRD

Evidence pointer: Repo | repository metadata | "repository_full_name=amthorn78/glow-hdengine-v2; default_branch=main".

Evidence pointer: Repo | PR 359 metadata | "merged=true; merge_commit_sha=78756e776f7fa598370235de6a72aa29fe045af9; head_sha=c6e689edefdac1f832faed6ad19f504eefbda696; base_sha=fbb1639890a89858c17ba8ac1f09af410df15d8f".

Evidence pointer: Repo | compare `78756e776f7fa598370235de6a72aa29fe045af9...main` | "status=identical; ahead_by=0; behind_by=0; total_commits=0".

Evidence pointer: CRD | §1 `Document Control` | "Version v1.3"; "Epic HDE-EPIC038, Distillation Pass 3"; "Slice POST-PR359-REMEDIATION"; "ADR-CANON-004 - PROPOSED - PENDING IA TECHNICAL APPROVAL - canon effect AMENDS".

## 2. Review Decision

Decision: APPROVED

The CRD is technically complete and execution-ready as the authoritative input to a later, separately authorized revision of the Current Implementation Plan. It establishes three confirmed current-repository defects, keeps two historical external-run claims explicitly unverified and non-operative, provides complete causal chains for all mandatory additions, and requests a bounded PR-A → qualified one-attempt OPS-01R → PR-C migration rather than reopening PR 359 or expanding product scope.

The v1.3 source and write-isolation revision closes the remaining execution-readiness risk: every source-loading Python entry point in the bounded OPS-01R chain is pinned to the exact ordered `-I -B` prefix, receives no case-folded `PYTHON*` environment variable, is bound to independently captured source and staging identities, and is checked against explicit cache-residue and per-mode write-set contracts. The CRD also separates capture-time actual-tree admission from later permanent packet validation, so later CI does not falsely claim it can recapture temporary state.

`ADR-CANON-004` is technically sound and complete. It amends only the exact semantics of the active `ddl_fingerprint` evidence row: the new result proves equality of a strict, versioned Glow-owned identity projection and explicitly does not prove full DDL semantic parity. Existing provider availability, secret safety, evidence ownership, path, index, mirror, PF09, QA, acceptance, deployment, and closeout boundaries remain unchanged.

Evidence pointer: CRD | §2 `Executive Summary` | "OPS-01R is one separately authorized, one-attempt, Glow-only recapture"; "exact ordered Python prefix -I -B"; "Capture-time admission recomputes the actual temporary source/staging trees while they exist; later PR-C and release validation check only retained canonical proof and externally reviewed identities".

Evidence pointer: CRD | §14 `Revision Response Ledger`, `REV-001` | "Disposition: RESOLVED"; "Acceptance condition satisfied: Yes".

Evidence pointer: CRD | §10 `ADR-CANON-004` | "Canon effect: AMENDS"; "The result label is projection_match"; "full_ddl_semantic_parity_claimed is exactly false".

## 3. Source Coverage and Conflicts

### Complete-source coverage

The Rescoping CRD, Approved Implementation Guide, and Current Implementation Plan were read end-to-end. Current PF sources were resolved from their complete document-control units and the current session designation. `PF10-HDE-Build-Notes v12.2.7` was used as the sole current PF10 source; older PF10 copies were not combined with it. The CRD contains a complete material-item inventory: `BUG-001` through `BUG-003`; `STALE-001` and `STALE-002`; `BLK-001`; `ACT-001` through `ACT-003`; `CAUSE-001` through `CAUSE-005`; `RSC-001` through `RSC-005`; and `ADR-CANON-004`. The current Revision Response Ledger contains one active review item, `REV-001`, and treats the older review responses only as historical lineage.

Material-item coverage is allocated once as follows:

- Gate 1: authority, source roles, plan posture, and nonclaims in §§1, 3, 10, 12, and 14.
- Gate 2: the complete finding/action ledger, `BUG-001` through `BUG-003`, `STALE-001`, `STALE-002`, `BLK-001`, `ACT-001` through `ACT-003`, and `CAUSE-001` through `CAUSE-005`.
- Gate 3: `RSC-001` through `RSC-005` and the selected minimum migration.
- Gate 4: §8 ownership and boundary effects, plus the sequencing boundaries in §§7 and 9.
- Gate 5: §9 implementation requirements, the plan-consequence matrix, adoption order, exact implementation loci, and current `REV-001` resolution.
- Gate 6: §11 evidence, risks, safeguards, rollback, source/write qualification, and the independent validation contracts in `RSC-002` through `RSC-005`.
- Gate 7: `ADR-CANON-004`, PF09/PF10 consequences, permanent drainage targets, and §12 nonclaims.

Evidence pointer: CRD | §4 `Complete finding and action disposition ledger` | "BUG-001"; "BUG-002"; "BUG-003"; "BLK-001"; "ACT-001"; "ACT-002"; "ACT-003".

Evidence pointer: CRD | §6 `Causal Map` | "CAUSE-001" through "CAUSE-005".

Evidence pointer: CRD | §7 `Requested Rescope` | "RSC-001" through "RSC-005".

### Repo validation posture

Current GitHub inspection confirms the merged baseline and all three operative defect premises:

1. **EPIC024 generated-output drift is present.** The current generator emits the canonical sanity path, while both checked-in historical acceptance surfaces still point to the legacy path.
2. **The retained-evidence raw-payload scan has the reported syntax limitation.** The current scanner detects only double-quoted JSON-style keys followed by `:`.
3. **DDL projection logic is duplicated and semantically narrower than the plain `match` label suggests.** The current OPS producer projects object kind/name and column name/type, while the release-sanity validator independently normalizes the same narrow field set with different malformed-input behavior.
4. **Git-clean posture cannot prove Python-cache absence.** The current `.gitignore` ignores both `__pycache__/` and `*.pyc`, validating the CRD's need for explicit full-source manifests and residue scans rather than status-only checks.

Evidence pointer: Repo | `tools/qa/run_hde_epic024_harness.py`, `_write_acceptance_map` | "SANITY_PIPELINE_OK" binds `audit/gates/sanity_pipeline/sanity_pipeline.log`.

Evidence pointer: Repo | `docs/acceptance_map_epic024.json` | `SANITY_PIPELINE_OK` currently binds `artifacts/sanity/sanity.log`.

Evidence pointer: Repo | `audit/qa/hde-epic024/token_evidence_matrix.md` | `SANITY_PIPELINE_OK` currently binds `artifacts/sanity/sanity.log`.

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py`, `_validate_secret_safety` | `raw_payload_key = re.compile(r'(?i)"(?:raw_vendor_(?:payload|envelope)|raw_(?:request|response)_body)"\s*:')`.

Evidence pointer: Repo | `scripts/db/capture_epic011_posture.py`, `_ddl_projection` and `_parity_match` | "Provider parity compares only the shared schema identity surface: object kind/name and column name/type"; `ddl_fingerprint` parity compares canonicalized projections.

Evidence pointer: Repo | `tools/evidence/run_sanity_pipeline.py`, `_normalize_ddl_provider_value` | DDL admission independently retains only item `name`, `kind`, and sorted column `name` plus `data_type` or `type`.

Evidence pointer: Repo | `.gitignore` | "__pycache__/"; "*.pyc".

### CRD evidence sufficiency and material unverified claims

The CRD does not use the unavailable failed-run report as a technical premise. `BLK-001` and `ACT-002` remain explicitly `UNVERIFIED`, non-operative provenance. Their alleged traceback, hashes, staging location, counters, provider boundary, and no-I/O conclusions are excluded from implementation identity, authorization, validation, or acceptance. The selected source/import/write qualification is justified prospectively by the one-attempt boundary and by current Repo facts, not by the unverified report.

The remaining operational facts—Railway CLI identity, explicit-target argv, target identifiers, injected identity fields, run ID, live authorization identity, candidate identity, and PR-C identity—are not represented as known. Each is assigned to a named preflight, bounded discovery, authorization, capture, or integration gate with a fail-closed stop condition. These are staged execution inputs, not unresolved CRD design decisions.

Evidence pointer: CRD | §4 `Minimal failed-run evidence record and verification disposition` | every historical failed-run field is marked `UNVERIFIED`; "No mandatory mechanism in this CRD depends on the alleged hash, path, count, traceback, provider boundary, no-I/O conclusion, or attempt-consumption claim."

Evidence pointer: CRD | §11 `Residual operational unknowns and gates` | "UNKNOWN PENDING PREFLIGHT"; "UNKNOWN PENDING DISCOVERY"; "UNKNOWN UNTIL LIVE AUTHORIZATION/ARTIFACT CREATION"; "Failure to derive or match any value is a stop condition, not a delegated architecture choice."

### Plan and PF-Canon conflicts

No unresolved product-scope conflict remains. The Approved Implementation Guide already makes release sanity, DB/bridge posture, governed evidence, controlled OPS support, and no-public-scope boundaries part of HDE-EPIC038. The Current Implementation Plan remains the current execution baseline but does not yet allocate this post-merge remediation. The CRD correctly preserves both plans, requires a separately authorized next-version Current Implementation Plan revision before implementation relies on the rescope, and does not treat the CRD as an implementation authorization.

Current PF10 explicitly governs that adoption sequence and is otherwise silent on `POST-PR359-REMEDIATION`, `ADR-CANON-004`, and `ddl_identity_projection`. Permanent PF12/PF14 canon currently requires truthful active-row parity evidence but does not define the versioned projection contract. That is a real bounded canon gap, not a contradiction invalidating the proposal.

Evidence pointer: Implementation Guide | `Business Case`, `Scope boundaries` | HDE-EPIC038 includes governed evidence discipline, DB posture, DB-bridge parity, mapped-cache hardening, a one-button release sanity pipeline, and PO-only OPS support where external confirmation is required; new public Reader behavior, new public routes, broad vendor-platform scope, QA execution, and PF status movement are excluded.

Evidence pointer: Implementation Plan | `Brief recap of scope` | the epic consolidates DB and BodyGraph posture, DB-bridge parity, governed evidence, and a single release sanity pipeline; it does not add public behavior, public routes, app-side vendor ownership, production authorization, PF09 movement, QA PASS, OPS completion, or closeout.

Evidence pointer: PF10 - PF10-HDE-Build-Notes | Addendum 2.4, `Governing posture` | "The approved CRD may govern revision of the current HDE-EPIC038 Implementation Plan. The Implementation Plan must be revised before implementation relies on these decisions."

Search method: searched PF10 - PF10-HDE-Build-Notes `v12.2.7` for `POST-PR359-REMEDIATION`, `ADR-CANON-004`, `ddl_identity_projection`, and `projection_match` (case: insensitive); scope: complete current PF10; method: exact text search plus complete relevant-addendum reading; result: 0 hits.

Evidence pointer: PF12 - PF12-Canon-HDE-Schemas-and-Artifacts | `§8.6.3.4 Gates, runtime, DB, and ops evidence` | `artifacts/db/ddl_fingerprint.json` is the current governed DDL evidence identity.

Evidence pointer: PF14 - PF14-Canon-HDE-Mechanics-Guide | `§20.3 Bridge parity mechanics` | "If an active row such as ddl_fingerprint remains in the corpus, closure MUST be based on row-level match evidence, not on silent exclusion."

Search method: searched PF12 - PF12-Canon-HDE-Schemas-and-Artifacts `§8.6.3.4` and PF14 - PF14-Canon-HDE-Mechanics-Guide `§20.3` for `hde.ddl_identity_projection.v1`, `project_ddl_identity`, `projection_match`, and `full_ddl_semantic_parity_claimed` (case: insensitive); scope: the complete topic-owning units; method: exact text search plus complete-unit reading; result: 0 hits.

## 4. Review Gate Results

### Gate 1: Authority and source fidelity — PASS

The CRD stays within the already approved product and rescoping boundary. It treats the Approved Implementation Guide as the epic-scope baseline, the Current Implementation Plan as the current execution baseline requiring later revision, Repo as current-state proof, PF-Canon as the architectural baseline, and PF10 only where PF10 explicitly speaks. It neither treats PO rescoping authority as technical proof nor converts approval into implementation, plan revision, PF09 movement, QA PASS, OPS completion, deployment, token satisfaction, acceptance, or closeout.

**Covered CRD items:** §§1, 3, 10, 12, and 14; `ACT-001`; `ACT-003`; plan-adoption posture; all explicit nonclaims.

Evidence pointer: CRD | §3 `Authority and Decision Posture` | "The PO has approved bounded rescoping"; "Sekhmet technical decisions" remain subject to IA technical review; "Plan posture" preserves `r1` and requires a separately authorized next-version Current Implementation Plan revision.

Evidence pointer: CRD | §12 `Approval Limitations and Nonclaims` | no implementation, Repo edit, plan edit, PF edit, PF09 movement, QA PASS, OPS execution, deployment, acceptance, merge authorization, slice closure, or epic closure is claimed.

Evidence pointer: PF06 - PF06-Canon-Epic-Process-Guide | `0.2 Policy and principles` | PF-Canon editing, PF09 drainage, QA evidence, OPS state, merge provenance, and PO closeout remain separate axes.

Evidence pointer: PF10 - PF10-HDE-Build-Notes | Addendum 2.4 `Governing posture` | the approved CRD may govern a later Implementation Plan revision, but the plan must be revised before implementation relies on the decisions.

### Gate 2: Conflict and causal accuracy — PASS

The CRD accurately identifies three current conflicts and validates each against current Repo state. `BUG-001` is a selective generated-output binding drift, `BUG-002` is a retained-text admission blind spot, and `BUG-003` is an ambiguous and duplicated DDL comparison contract. `CAUSE-001` through `CAUSE-005` connect governing contract, observed reality, conflict, consequence, minimum change, ownership, validation, and documentation consequence. Suspected historical-run facts are separately classified as `UNVERIFIED` and are not used to justify any mandatory addition.

**Covered CRD items:** `BUG-001`, `BUG-002`, `BUG-003`, `STALE-001`, `STALE-002`, `BLK-001`, `ACT-001`, `ACT-002`, `ACT-003`, and `CAUSE-001` through `CAUSE-005`.

Evidence pointer: CRD | §4 `Confirmed RCA conclusions` | `BUG-001` is generator/output sequencing drift; `BUG-002` is an admission-pattern defect; `BUG-003` is a versioning and truth-label defect rather than a database-schema defect; no failed-run RCA is claimed.

Evidence pointer: Repo | current EPIC024 generator and checked-in acceptance surfaces | canonical generator path is `audit/gates/sanity_pipeline/sanity_pipeline.log`; both checked-in historical primaries still use `artifacts/sanity/sanity.log`.

Evidence pointer: Repo | current retained-evidence scanner | the raw-payload marker regex requires a double-quoted key and `:` delimiter.

Evidence pointer: Repo | current DDL producer and release-sanity consumer | both compare only object kind/name and column name/type, but own separate implementations and plain match semantics.

Evidence pointer: Repo | `.gitignore` | ignored Python cache families make an ordinary clean-worktree result insufficient to prove no cache residue.

### Gate 3: Minimum coherent rescope — PASS

Each requested addition is causally necessary and bounded:

- `RSC-001` repairs exactly two stale EPIC024 primaries and their updater-owned companions without rerunning or reopening historical QA.
- `RSC-002` centralizes the existing secret/raw-payload safety rule across the retained text forms actually consumed by the release gate.
- `RSC-003` removes duplicated DDL semantics, makes the proof scope explicit, and introduces only the shared pure projector and independent v5 validator needed for truthful admission.
- `RSC-004` adds one qualified, separately authorized, no-retry OPS recapture with bounded discovery rather than guessing external CLI or target facts.
- `RSC-005` makes integration atomic and switches directly from coherent v4 to coherent v5 without a permanent dual-default state.

The broader PR-A → OPS-01R → PR-C shape is the minimum coherent migration because independent code and validation must exist before the one live attempt, while governed retained bytes and release admission cannot change until a candidate exists and passes independent review. No unrelated cleanup, platform redesign, public behavior, bridge-service repair, or speculative product scope is imported.

**Covered CRD items:** `RSC-001` through `RSC-005`; selected architecture; rejected alternatives; scope classifications `NO CANON CHANGE` and `AMENDS`.

Evidence pointer: CRD | §7 `RSC-001` | exactly `docs/acceptance_map_epic024.json` and `audit/qa/hde-epic024/token_evidence_matrix.md` are regenerated; the full historical harness is not rerun.

Evidence pointer: CRD | §7 `RSC-002` | one shared retained-evidence safety module, exact marker forms, closed safe-scalar roster, strict UTF-8, and fail-closed reason codes.

Evidence pointer: CRD | §7 `RSC-003` | one pure `engine/db/ddl_identity_projection.py` owner, strict deterministic invariants, projection-only label, false full-parity flag, stable existing evidence paths and keys, and v5-only final admission.

Evidence pointer: CRD | §7 `RSC-004` | one Glow-only recapture, separate bounded discovery authority, separate exact live authorization, one launch, no retry or fallback, no tracked write, and no `pg-bridge` work.

Evidence pointer: CRD | §7 `RSC-005` | whole-packet candidate validation and copy, external candidate-ledger identity, direct v4-to-v5 default switch, canonical updater convergence, and atomic rollback.

### Gate 4: Epic and slice boundaries — PASS

The CRD preserves the epic and slice boundaries. PR 359 is frozen as merged. The remediation is a new post-merge slice divided into implementation-owned PR-A, PO/operator-owned OPS-01R, and integration-owned PR-C. Historical EPIC024 maintenance is limited to two stale generated bindings and does not create historical reapproval, rerun QA, or reopen PF09. Existing direct and bridge provider ownership is preserved; the separate `pg-bridge` repository/service is explicitly excluded. Downstream QA, acceptance, PF09 drainage, deployment, merge, and closeout remain separate.

**Covered CRD items:** §8 `Ownership and Boundary Effects`; `ACT-001`; `ACT-003`; PR-A/OPS-01R/PR-C allocation; EPIC024 limitation; PF09 status posture.

Evidence pointer: CRD | §8 `Work moved into the new remediation slice` | PR-A owns code and validators, OPS-01R owns temporary operational production, and PR-C alone owns later tracked integration.

Evidence pointer: CRD | §8 `Historical work reused without reopening` | EPIC024 is used only for exact generated-binding repair and retains its historical execution/status posture.

Evidence pointer: CRD | §8 `Downstream work retained elsewhere` | QA, acceptance, PF09 status movement, deployment, merge, and closeout remain outside the remediation slice.

Evidence pointer: CRD | §8 `Prohibited boundary crossings` | no `pg-bridge` inspection, patch, deploy, provider-service mutation, or inferred defect.

Evidence pointer: Implementation Guide | `Scope boundaries` | the epic is an internal reliability and evidence slice, not a public-product expansion or Coagulation deployment-hardening effort.

### Gate 5: Implementation Plan executability — PASS

The CRD provides enough exact, Repo-grounded technical direction to revise the Current Implementation Plan without inventing material paths, APIs, schemas, commands, tests, evidence identities, dependency order, or ownership. It identifies the confirmed current loci and separates new files from retained files. Every external operational fact that cannot be proved from Repo or PF authority is routed through an explicit, bounded PO-authorized discovery contract rather than guessed.

The v1.3 revision resolves the only remaining source/write-isolation concern. The CRD now pins exact interpreter and argv order for the preflight producer, preflight validator, discovery producer, both discovery validators, target-identity probe, live-authorization validator, launcher, live child, capture-time validator, and permanent candidate validator. It prohibits every environment substitute, binds canonical stdin expected identities, requires independently captured full-source manifests and authenticated staging baselines/deltas, rejects `__pycache__`, `.pyc`, symlink escape, and all unlisted writes, and propagates those invariants into the plan-consequence matrix, adoption order, validation order, rollback, and tests.

**Covered CRD items:** §9; `RSC-001` through `RSC-005` implementation loci and owners; `RSC-004.A` through `.D`; current `REV-001`.

Evidence pointer: CRD | §9 `Source-grounded technical requirements` | exact existing and proposed modules, artifact families, producer/consumer ownership, and plan consequences are enumerated.

Evidence pointer: CRD | §9 `Plan-consequence matrix` | each work unit has current baseline, PF09 posture, exact CRD allocation, implementation owner, proof contract, evidence output, validation, sequence, updater boundary, and nonclaims.

Evidence pointer: CRD | `RSC-004.A` | exact preflight producer argv `[interpreter.lexical_path, "-I", "-B", components.runner.lexical_path, "--preflight"]`; exact validator argv; `python_environment_names=[]`; full-source manifest; cache scans; and exact sole write.

Evidence pointer: CRD | `RSC-004.B` through `.D` | exact `-I -B` target probe, discovery producer and validators, live validator/launcher/child/capture validator, permanent candidate validator, per-mode write sets, and independent pre-boundary PASS requirements.

Evidence pointer: CRD | §14 `Revision Response Ledger`, `REV-001` | all five IA acceptance conditions are marked satisfied, including exact isolation mechanism, bound identities, independent drift rejection, focused no-source-write/no-unlisted-write tests, and plan-sequence propagation.

Evidence pointer: PF27 - PF27-Canon-Plan-Templates | `Repository locus validation and file minting posture (hard)` | "Validated references only. Plans MUST NOT include any repository path, module home, command, or uniqueness claim (for example, only create_app factory) that cannot be confirmed via canon or repo inspection."

Evidence pointer: PF07 - PF07-Canon-Glow-Infrastructure | `PS discovery for discoverable infrastructure facts` | when a missing infrastructure fact can be safely discovered by bounded PO OPS discovery, the artifact must route it to that discovery rather than guess or automatically defer it.

### Gate 6: Validation, evidence, and safeguards — PASS

Validation follows the dependency graph and independently checks the decisive claims before each irreversible boundary. PR-A tests and validates the shared scanner, projector, preflight, discovery policy, independent v5 APIs, exact argv/environment rules, and mutation cases under closed rails. Discovery cannot call the CLI until its authorization and per-stage dispatch validators pass. Live authority cannot be consumed until the independent live-authorization validator passes. Candidate admission occurs while temporary source and staging trees still exist, with a separate capture-time actual-tree validator and nested permanent packet validation. PR-C later repeats only permanent retained-packet validation and explicitly does not claim to recapture temporary state.

Evidence production and ownership are correctly governed: the task-specific producers own only primary outputs, the independent validators are read-only, `tools/evidence/update_evidence_index.py` remains the sole path-proof/index/mirror owner, and `tools/evidence/orientation_demo.py` retains orientation ownership. Mixed packet/validator/companion states fail closed. Rollback is atomic at PR-A or PR-C boundaries, and a failed or indeterminate live attempt cannot be retried under the same authority.

**Covered CRD items:** §11; `RSC-002` validation; `RSC-003` independent v5 validation; `RSC-004.A` through `.D`; `RSC-005`; risks, safeguards, rollback, and residual gates.

Evidence pointer: CRD | §11 `Material risks and safeguards` | exact controls cover historical-QA overreach, raw-marker bypass, projection overclaim, source/import/cache/write drift, unknown Railway facts, expected-identity transport, one-attempt consumption, candidate self-certification, temporary-state loss, and main advancement.

Evidence pointer: CRD | §11 `Rollback and fail-closed behavior` | preflight, discovery, live authorization, post-marker execution, capture-time validation, permanent candidate validation, and PR-C each have explicit stop or atomic-revert behavior.

Evidence pointer: CRD | `RSC-003` | strict projector tests, packet schema/corpus/result mutations, independent `validate_ops01_v5_package`, `validate_ops01r_live_capture`, and stable sorted non-secret error codes.

Evidence pointer: CRD | `RSC-004.A` | source manifest entries use `lstat`-derived metadata and hashes; pre/post scans reject every `__pycache__` path component and `.pyc` file; exact staging deltas and writes are authenticated.

Evidence pointer: CRD | `RSC-005` | independent candidate validation before and after copy; candidate ledger hash preserved; updater/orientation/path/mirror/hash/LF checks; v5-only release admission; no second OPS execution.

Evidence pointer: PF12 - PF12-Canon-HDE-Schemas-and-Artifacts | `§8.6.3.4 Gates, runtime, DB, and ops evidence` | current DDL and OPS evidence identities remain governed under the existing evidence/index/path-proof discipline.

Evidence pointer: PF14 - PF14-Canon-HDE-Mechanics-Guide | `§20.3 Bridge parity mechanics` | provider-parity PASS must fail when direct rows are missing, skipped, unavailable, or errored; closure evidence must remain machine-readable, secret-safe, row-level, and non-overclaiming.

### Gate 7: Canon-changing ADRs, documentation consequences, and nonclaims — PASS

`ADR-CANON-004` is complete and technically sound. It identifies the exact PF12/PF14 baseline and proof excerpts, provides negative-search proof for the missing contract, states the engineering limitation, evaluates and rejects alternatives, selects one strict shared projector, classifies the change as `AMENDS`, defines the exact topic and boundary affected, preserves unchanged canon, specifies compatibility and migration, identifies all implementation dependencies and plan consequences, defines validation/evidence and safeguards, supplies atomic rollback, lists permanent PF12/PF14/PF09.6 drainage targets, defines adoption order, and includes explicit nonclaims.

The amendment is causally necessary: without it, the active DDL row continues to report an unqualified `match` while producer and release validator implement separate narrow comparisons with different malformed-input behavior. The decision strengthens truthfulness and fail-closed behavior; it does not weaken provider evidence, broaden runtime behavior, or hide product scope.

PF09 mapping is exact and no status movement is proposed. The CRD retains `HDE-DIST001.4`, `.6`, `.9`, and `HDE-DIST005.2` as `Partial`, retains `HDE-DIST001.11` as `Optional`, and reopens no EPIC024 row. Permanent PF drainage remains later documentation work and is not represented as complete or as an implementation gate.

**Covered CRD items:** `ADR-CANON-004`; §10 other canon effects; PF09 consequences; PF10 consequence; permanent drainage order; §12 nonclaims.

**ADR-CANON-004 assessment:** `APPROVED` — `AMENDS`.

Evidence pointer: CRD | `ADR-CANON-004`, `Current canon baseline with exact proof` | exact PF12 §8.6.3.4 and PF14 §20.3 excerpts are supplied.

Evidence pointer: CRD | `ADR-CANON-004`, `Selected decision and exact bounded amended rule` | the change is limited to the HDE-EPIC038 OPS `ddl_fingerprint` row; `projection_match` proves only object kind/name and column name/type equality; `full_ddl_semantic_parity_claimed=false`.

Evidence pointer: CRD | `ADR-CANON-004`, `Canon that remains unchanged` | paths, evidence ownership, provider availability, row-level truthfulness, secret safety, parity-scope rationale, DBAccess provenance, and all QA/PF09/token/closeout nonclaims remain unchanged.

Evidence pointer: CRD | `ADR-CANON-004`, `Permanent PF-Canon or ADR drainage targets` | exact later targets are PF12 §8.6.3.4, PF14 §20.3, and the listed PF09.6 rows, in a bounded order and never as an execution gate.

Evidence pointer: PF09.6 - PF09.6-Canon-HDE-Build-Checklist-Distillation | `HDE-DIST001.4`, `HDE-DIST001.6`, `HDE-DIST001.9`, `HDE-DIST001.11`, and `HDE-DIST005.2` | current statuses are respectively `Partial`, `Partial`, `Partial`, `Optional`, and `Partial`.

Evidence pointer: CRD | §10 `PF09 consequences` | every mapped row has `Status movement: None`; no EPIC024 PF09 row is reopened.

## 5. Findings

None.

## 7. Nonblocking Notes

1. Permanent PF12, PF14, and PF09.6 documentation drainage remains pending. It is not a CRD correction, implementation prerequisite, QA result, or closeout condition.
2. The current `r6` Implementation Plan does not yet allocate this post-merge remediation. A separately authorized next-version Current Implementation Plan revision must be approved before implementation relies on `RSC-001` through `RSC-005` or `ADR-CANON-004`, unless a newer explicit PO instruction changes the current PF10 posture.
3. Railway CLI identity, explicit-target syntax, target identifiers, injected target fields, run identities, and later candidate/integration hashes remain intentionally unknown until their named preflight, bounded discovery, authorization, capture, or integration gates. The CRD defines safe failure posture for each unknown and does not delegate an architectural decision to the implementer.

## 8. Approval Scope and Nonclaims

This IA approval technically approves `CRD-HDE-EPIC038-POST-PR359-REMEDIATION v1.3` and `ADR-CANON-004` for their exact stated scopes. `ADR-CANON-004` now governs the exact architectural topic it defines: a strict, shared, versioned Glow-owned DDL identity projection and projection-only semantics for the HDE-EPIC038 OPS-01 provider-parity evidence family. It does not establish full DDL semantic parity, change provider or database behavior, or apply beyond the bounded supersession/amendment boundary stated in the ADR.

The approved ADR governs that exact scope pending permanent PF-Canon drainage. No PF document was edited by this review, and the absence of later drainage does not invalidate the approved engineering decision. The drainage targets remain documentation consequences, not execution gates.

This approval authorizes neither implementation nor plan mutation. Before implementation relies on the approved decisions, the Current Implementation Plan must receive the separately authorized next-version revision required by current PF10, unless the PO later changes that posture explicitly. Separate authority remains required for PR-A implementation, bounded Railway discovery, the one-attempt live OPS-01R action, PR-C integration, any merge, and every later QA, acceptance, PF09, deployment, board, or closeout action.

This review did not implement code, edit either plan, edit PF10 or PF-Canon, modify Repo state, execute QA, execute OPS, open rails, call Railway, access a database or bridge, deploy, migrate, move PF09 status, satisfy a token, accept implementation, merge a PR, close the remediation slice, or close HDE-EPIC038.

## 9. Re-review Instructions

No re-review required.

DECISION: APPROVED

