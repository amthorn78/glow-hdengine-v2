# HDE-EPIC040-PR02 PR Implementation Plan v1.0

## 0. Control block

| Field | Value |
| --- | --- |
| `ARTIFACT_TYPE` | `PR_IMPLEMENTATION_PLAN` |
| `PR_IMPLEMENTATION_PLAN_ID` | `HDE-EPIC040-PR02-PRIP-v1.0` |
| `VERSION` | `1.0` |
| `STATE` | `AWAITING_PO_PROCEED` |
| `CHANGE_CLASS` | `EPIC` |
| `CHANGE_ID` | `HDE-EPIC040` |
| `CHANGE_NAME` | `Separation Pass 3` |
| `WORK_UNIT_ID` | `HDE-EPIC040-PR02` |
| `WORK_UNIT_NAME` | `Strict immutable input and admission boundary` |
| `DESTINATION_PROMPT` | `PR-20 — Create Detailed PR Implementation Plan — 091226.1` |
| `EXECUTION_POSTURE` | `MANUAL_PROMPT_EXECUTION` |
| `session_disposition` | `INITIAL_DEDICATED_ASSIGNMENT` |
| `role_session_ref` | `This current user-assigned dedicated HDE-EPIC040-PR02 engineering/planning session; no platform session ID is asserted` |
| `invocation_binding` | `EPIC / HDE-EPIC040 / HDE-EPIC040-PR02 / PR-20 / sole substantive input libfile_40f6b1d402808191b484e5929a6afcca` |
| `context_conflict` | `NONE` |
| `CREATED_AT_UTC` | `2026-09-12T16:25:32Z` |
| `NEXT_CONTROL_PROMPT` | `PR-30 — PR Implementation Proceed — 091226.1` |

The Library-assigned file identity is bound by the verified save/read-back handoff for this exact body. The semantic plan identity and version above are stable. This plan authorizes no repository mutation; only a later Product Owner invocation of the exact PR-30 prompt for this exact saved plan supplies Proceed.

## 1. Decision and bounded outcome

PR02 is executable as one coherent pull request within the approved scope. It will provide:

1. one strict shared Gate normalizer that accepts only a non-empty list of canonical Gate values and returns one immutable normalized representation;
2. one production admission entry point rooted only at the fixed repository root, with no caller-selected root, config ID, fallback, alias, skip flag, environment selector or remote schema resolution;
3. exact byte capture, duplicate-aware canonical JSON validation, safe-path/symlink protection, complete manifest-roster/hash/size/member-format validation, schema and relational closure, separate identities and recursive immutability before any active handle is returned; and
4. exhaustive positive/adverse tests plus explicit CI changed-path ownership.

The pull request does **not** implement Magic10 scoring, compatibility/application wiring, golden comparison, readiness, release promotion, repository documentation, live operations, QA acceptance or Epic closure. It does not change `catalog/manifest.json`. On the current accepted 15-member baseline, the new production entry point must fail closed because the final release roster is not yet present. A labeled, isolated synthetic complete-release fixture proves the complete path without claiming that the repository is a promoted release.

No material source conflict, missing decision, dependency gap or out-of-scope prerequisite prevents execution. Therefore the correct plan state is `AWAITING_PO_PROCEED`.

## 2. Exact controlling lineage

| Role | Exact identity / disposition |
| --- | --- |
| Sole PR02 instruction | `libfile_40f6b1d402808191b484e5929a6afcca`, HDE-EPIC040-PR02 PR Work-Unit Instruction v1.0, `INSTRUCTION_READY` |
| Approved Specification | `libfile_12bab860949c8191881510875f051460`, v1.1 |
| Whole-change Implementation Audit | `libfile_823ee8e9ecb0819185181ec7695265fb`, v2.0 |
| Approved whole-change Implementation Plan | `libfile_11c992cda3f0819199827e86584e41f1`, v2.1 |
| Approving Plan review | `libfile_b85b81651a508191abdfd8f81803caf8`, Review v2.1 / Isis-50 `APPROVE` |
| Accepted predecessor review | `libfile_47bf2e063d208191bf57f93c71f96821`, HDE-EPIC040-PR01 lineage review v1.1 / `ACCEPT` |
| Predecessor repository delivery | GitHub PR `#403`, merged; attributable accepted main commit `3828d4b3454259841a3e48d13039dd1475754f2f`, tree `529306a74268f2a46765bf40defdae49026d103e` |

Controlled Product Framework Canon was resolved through the exact Markdown files selected from `Glow / Core Docs / PFCanon` by the canonical Drive path/content predicate, not by modification time:

- PF01 v1.3.7: §4 Gate normalization and §5.2–5.3 identity/model constraints;
- PF02 v2.4.5: §§2.1–2.2 pure-engine and normalized immutable input boundaries;
- PF04 v2.8.6;
- PF10 v13.1.8, including published Addendum 2.5;
- PF12 v2.9.6: §2.9 active config, §§5–6 manifest/release identity, §§8.14–8.15 candidate and FE/BE boundaries; and
- PF27 v2.0.5: §12 per-PR planning and approval handoff.

No controlled source is copied to Drive and no output is stored there. Runtime source IDs remain evidence only; reusable selection rules remain predicate-based.

## 3. Repository baseline and action-time preflight

The read-only GitHub planning baseline is `amthorn78/glow-hdengine-v2`, default branch `main`, commit `3828d4b3454259841a3e48d13039dd1475754f2f`, tree `529306a74268f2a46765bf40defdae49026d103e`. That SHA is both the current remote `main` head observed during planning and the accepted PR01 merge result. No later remote divergence and no existing branch matching HDE-EPIC040-PR02 were found. Branch protection was not present at planning time; manual-merge and review controls still govern.

PR-30 must begin with a read-only action-time capture before editing:

1. read the complete current root `AGENTS.md` and any narrower instruction file applicable to each affected path;
2. record current remote `main` head/tree and compare them to the baseline above;
3. record the selected local checkout path, current branch, full `HEAD`, upstream and `git status --short --untracked-files=all`;
4. preserve every pre-existing tracked/untracked user change; do not stash, reset, overwrite, clean or incorporate unrelated work;
5. if the accepted base has advanced, attribute the divergence and re-run this plan's source/ownership assumptions before editing; stop for rescope if it changes the approved boundary;
6. create one PR02 branch from the accepted current base only after the worktree is safe, with a descriptive name such as `hde-epic040-pr02-immutable-admission`; and
7. record the actual base SHA/tree in engineering evidence and the eventual PR body.

The repository's closed validation rails apply throughout: `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`. Install the repository-declared development dependencies and prove `python -m pytest --version` before claiming test execution. No vendor, database or production access is needed.

## 4. Current implementation facts and seams

### 4.1 Existing owners to preserve

`engine/config/registry_loader.py` already owns typed config records, safe source paths, owned byte reads, duplicate-aware JSON parsing, local schema execution, candidate registry/mechanics capture and unchanged-source verification. It deliberately does not yet own complete release admission. Several dataclasses are frozen only shallowly because nested dictionaries remain mutable. `_LocalCapture` is JSON-oriented and keeps a mutable source map. `load_manifest` validates the current generic manifest shape but not the approved exact final roster.

`engine/config/bundles.py` and `tools/config/artifacts.py` use candidate validation for bounded FE/BE/config projections. `tools/config/generate_config_artifacts.py` explicitly produces candidate/non-active outputs. These are not active-release selectors and must remain so.

`engine/bodygraph/gates.py` does not exist at the baseline. Gate parsing is therefore not yet centralized under the approved contract.

`catalog/manifest.json` is a canonical 15-member baseline at manifest version `1.0.0`, timestamp `2025-12-26T00:00:00Z`. It is structurally valid for its current release but intentionally incomplete for EPIC040's final active release. `scripts/release_id_recompute.py` already defines release identity as SHA-256 of exact canonical manifest bytes; engine code must implement the same rule locally rather than importing a script module.

`.github/workflows/ci.yml` has one exact-head workflow with product, compatibility, database, rails, evidence, QA and release lanes plus a final applicability guard. `ci/checks/classify_ci_changes.py` fails closed for new product source lacking explicit test ownership. Its current registry-loader ownership map does not include the new admission tests, and it has no entry for `engine/bodygraph/gates.py`. The classifier's behavioral tests live in `tests/evidence/test_rails_ci_workflow_integration.py`.

### 4.2 Stable PR03-facing interface

PR02 will establish these internal interfaces in their owning modules:

```python
# engine/bodygraph/gates.py
@dataclass(frozen=True, slots=True)
class NormalizedGates:
    gates: tuple[int, ...]
    mask: int
    mask_hex: str

class GateNormalizationError(ValueError):
    code: str

def normalize_gates(value: object) -> NormalizedGates: ...

# engine/config/registry_loader.py
@dataclass(frozen=True, slots=True)
class SourceIdentity:
    path: str
    sha256: str
    size: int

@dataclass(frozen=True, slots=True)
class AdmittedMechanicsBundle:
    registry: RegistryConfig
    mechanics: Mapping[str, object]
    manifest: Manifest
    config_sha256: str
    source_identities: tuple[SourceIdentity, ...]
    manifest_sha256: str
    release_id: str

def load_active_mechanics_bundle() -> AdmittedMechanicsBundle: ...
```

Names may change only if code review finds an existing repository naming convention that materially improves compatibility; the properties, one-way admission boundary and tests may not weaken. PR03 imports from the owning modules directly. PR02 need not expand package `__init__.py` surfaces merely for convenience.

`GateNormalizationError` and existing/config-specific `RegistryConfigError` subclasses carry stable, value-free codes. Diagnostics may contain an allowed source-relative path and rule identity, never raw JSON, Gate payloads, secrets, birth data or chart records.

### 4.3 Exact Gate contract

`normalize_gates` accepts only a built-in/non-string list that is non-empty. Each element is either:

- an integer from 1 through 64, excluding `bool`; or
- an exact canonical decimal string from `"1"` through `"64"`.

It rejects tuples, mappings, sets, iterators and all scalar top-level values; empty input; duplicates after numeric normalization, including `[1, "1"]`; `0`, `65`, negative values; floats; booleans; signed, whitespace-padded, zero-padded, decimal-point, exponential, Unicode-digit or nondecimal strings.

Success returns a sorted tuple of unique integers, a uint64-compatible integer mask with bit `gate - 1`, and exactly sixteen lowercase hexadecimal characters with leading zeroes. It performs no I/O and retains no caller-owned collection.

## 5. Production admission design

### 5.1 One capture, validation and identity pipeline

Refactor the loader's capture primitive so one immutable owned byte capture per path feeds all parsing, canonical-byte comparison, size/hash identity and later unchanged verification. Preserve the existing duplicate-aware JSON parser. A JSON file must be exact UTF-8 without BOM and equal the canonical serializer output plus exactly one terminal LF. CRLF, extra LF, noncanonical key/order/number/spacing form and normalized-hash laundering fail.

Member validation is extension-specific and local:

- `.json`: duplicate-aware parse plus exact canonical JSON bytes and one LF;
- `.py`: exact UTF-8, no BOM, one LF, non-empty, syntactically compilable/AST-parseable bytes;
- `.sql`: exact UTF-8, no BOM, one LF and non-empty bytes.

The exact roster admits no other extension. Byte validation never rewrites a member or hashes normalized substitutes.

The capture map is private, source-relative, copy-owned and not exposed in the returned bundle. It rejects duplicate capture requests with inconsistent identity and verifies every captured file is unchanged before return. Replacement, truncation, symlink substitution or identity change at any stage yields no active handle.

### 5.2 Fixed root and safe paths

`load_active_mechanics_bundle()` accepts no arguments and resolves exactly the repository root derived from the installed owning module. It does not inspect CWD, environment variables, a caller config/release ID or a global mutable selector. A private test-only worker may accept an explicit `Path` so isolated synthetic fixtures can exercise the real admission algorithm; it is not exported or reachable from production consumers.

Every member path is non-empty canonical POSIX-relative text: no absolute path, backslash, `.`/`..` segment, duplicate separator or escape. Each ancestor and target must remain within the selected root and be a regular non-symlink file. Local schema references must resolve only to captured, roster-authorized local schemas; remote `$ref` or network resolution fails.

### 5.3 Exact complete release roster

Admission requires the sorted unique union of the legitimate 15 baseline members and the approved 31 promoted members: exactly **41** paths. The manifest does not list itself.

Current-only legitimate members retained by the union:

```text
catalog/gates_v1.json
catalog/magic10_seeds.json
catalog/narratives/keys.json
catalog/narratives/manifest.json
catalog/narratives/palettes.json
catalog/narratives/suppression_map.json
catalog/narratives/templates.json
engine/presenter/emitter.py
engine/serializer/canon.py
migrations/005_identity.sql
```

Exact promoted set:

```text
adapter/http_reader.py
adapter/schemas/error_v1.schema.json
catalog/channels_v1.json
catalog/magic10.json
catalog/magic10_caps.json
catalog/magic10_mechanics_v1.json
engine/bodygraph/gates.py
engine/bodygraph/mapped_cache.py
engine/bodygraph/projection.py
engine/bodygraph/resolver.py
engine/bodygraph/v2_adapter.py
engine/cli/main.py
engine/compat/compute.py
engine/compat/error_tokens.py
engine/config/registry_loader.py
engine/core/core.py
engine/http/compat_handler.py
engine/magic10/calculators.py
engine/magic10/composite.py
engine/magic10/signals.py
engine/narratives/router.py
engine/runtime/public.py
errors/token_map/token_map.json
math/thresholds.json
presenter/reader_v1/emitter.py
schemas/channels_v1.schema.json
schemas/magic10_compat_result_v1.schema.json
schemas/magic10_mechanics_v1.schema.json
schemas/magic10_result_v1.schema.json
schemas/reader.v1.schema.json
tools/bodygraph/check_magic10_gate_readiness.py
```

The five paths common to the current and promoted sets appear once: `adapter/http_reader.py`, `catalog/channels_v1.json`, `catalog/magic10.json`, `catalog/magic10_caps.json`, and `math/thresholds.json`.

The admitted manifest must also have exact adopted `version: "1.1.0"` and `built_at_utc: "2026-08-24T18:04:49Z"`, strict top/entry key sets, sorted unique entries and correct exact byte hash/size for every member. Missing, extra or malformed members fail before an active bundle exists.

PR02 does not edit the actual 15-member manifest. PR06 owns final roster materialization, exact member-byte refresh and release promotion after PR03–PR05 deliver their files.

### 5.4 Schema and relational closure

Use the loader's existing schema and shared-relation implementations rather than duplicate validators. Full admission runs all applicable PR01 validations over the captured release graph, including:

- exact 64 Gate facts and 36 Channel assignments;
- Gate/Channel/Center topology and all cross-file IDs;
- Magic10 classes, profiles, signals, categories, operations, scales, caps and defaults;
- required config/result-schema identity and local reference closure;
- every required source declaration and roster member binding; and
- exact list/order/default constraints from the adopted schemas and approved decisions.

Result schemas are validation dependencies only. PR02 does not construct result payloads or manufacture PR03/PR04 expected outputs.

### 5.5 Separate identities and immutable return

Keep these identities separate and explicitly tested:

- `config_sha256`: digest of the exact canonical admitted mechanics/config object under its governed construction;
- per-member `SourceIdentity(path, sha256, size)` from exact captured bytes;
- `manifest_sha256`: SHA-256 of exact canonical manifest bytes; and
- `release_id`: equal to the manifest-byte SHA-256 under the existing release rule, never substituted by config/source/pair identity.

Only after capture, format, manifest, schema, relational, identity and unchanged-source checks all succeed does the loader recursively copy/freeze the admitted graph. Mappings become read-only copied mappings; lists/tuples become copied tuples; records are frozen; nested profile responses, Channel structures, caps, categories, signals and source declarations are unreachable as mutable aliases. Freeze follows validation and cannot sanitize invalid input.

No global success cache is introduced. A valid first load followed by corrupt source must make the second load fail; a stale prior bundle cannot be returned. Existing candidate APIs may continue to support bounded projections but never receive `release_id` or active-bundle status.

## 6. Exact per-file implementation plan

| Order | File | Planned change | Decisive proof / reason |
| --- | --- | --- | --- |
| 1 | `engine/bodygraph/gates.py` (new) | Add frozen `NormalizedGates`, typed value-free error codes and the pure exact normalizer. No chart fingerprint, UUID, provider, DB or scoring logic. | `tests/bodygraph/test_gates.py` exhaustive equivalence, bounds, duplicate and prohibited-form matrix; purity and caller-alias tests. |
| 2 | `engine/config/registry_loader.py` | Generalize one owned capture to JSON/Python/SQL bytes; add exact release constants/roster; fixed-root public admission and private explicit-root worker; member format, manifest completeness, local-schema, relation, source-change, identity and deep-freeze gates; preserve candidate APIs. | New production-admission suite plus all existing config/bundle/schema regressions. Current repository entry point must fail with typed incomplete-roster error. |
| 3 | `tests/config/helpers.py` | Add a clearly named synthetic complete-release-root builder. Copy actual source bytes where the fixture intentionally represents current owners; create minimal format-valid, nonfunctional placeholders only for later-owned absent paths; compute exact hashes/sizes and a canonical 41-row manifest in a temp root. Never touch repository files. | Fixture self-checks exact roster/version/timestamp, labels and isolation. Helpers do not calculate expected Gate outcomes or silently repair invalid cases. |
| 4 | `tests/bodygraph/test_gates.py` (new) | Table-driven success cases for integers/strings/order/mask/hex plus exhaustive adverse contract and no-input-retention checks. | Proves PF01 §4 exact shared boundary independently from admission. |
| 5 | `tests/config/test_production_admission.py` (new) | Exercise the real private admission pipeline against valid and one-fault-at-a-time synthetic roots. Cover complete success, actual-root refusal, bytes, manifest, path/symlink, root isolation, schema/relation, identity, mutation and stale-fallback behavior. | Primary PR02 acceptance proof. It must assert fixture success is synthetic and actual current root yields no active handle. |
| 6 | `tests/config/test_manifest_schema.py` | Extend generic manifest-shape/path/version/member-format assertions only where the new exact admission contract reuses this owner; avoid turning current manifest validity into a false full-release claim. | Separates generic 15-member manifest integrity from full 41-member active admission. |
| 7 | `ci/checks/classify_ci_changes.py` | Register `engine/bodygraph/gates.py` to `tests/bodygraph/test_gates.py`; extend registry-loader ownership to `tests/config/test_production_admission.py`; register new support/test paths in the existing explicit ownership/full-validation structures. Because this classifier source changes, all seven workflow lanes remain applicable. | Prevent `CI_PRODUCT_OWNER_TEST_MISSING`, ensure changed implementation executes its behavioral owners, and preserve fail-closed handling of unknown product sources/support files. |
| 8 | `tests/evidence/test_rails_ci_workflow_integration.py` | Update classifier expectation fixtures for the new source/test/support mappings and assert exact changed-test targets/lane behavior. No rails policy change. | Existing canonical classifier test home at the baseline; proves no ownership waiver or accidental lane reduction. |

Expected unchanged-but-regression-tested files include `engine/config/bundles.py`, `engine/config/__init__.py`, `tools/config/artifacts.py`, `tools/config/generate_config_artifacts.py`, `tools/config/generate_bundles.py`, `scripts/release_id_recompute.py`, all PR01 catalog/schema inputs and `catalog/manifest.json`. If implementation requires editing one of these, the engineer must document the exact necessity, update ownership/tests and confirm it remains within PR02; otherwise stop for rescope.

No generated evidence file is expected to change. If a legitimately changed primary source makes an existing projection stale, run only its owning generator from the same selected root, inspect the primary delta first, then update required companions through their governed sole writers. Never hand-edit evidence index, path proof, mirror, checksum, manifest or acceptance artifacts.

## 7. Ordered engineering sequence after Proceed

1. Perform §3 preflight and record the exact safe baseline.
2. Create the branch; set closed rails; install declared dev requirements; prove pytest readiness.
3. Write failing Gate tests, then implement the pure normalizer and make only that suite pass.
4. Add the synthetic complete-root helper with explicit placeholder inventory and self-validation.
5. Write admission tests for the successful complete synthetic root and for current-root incomplete refusal.
6. Refactor capture internals without changing candidate behavior; run existing config tests immediately.
7. Add exact roster/manifest/member-format checks, then schema/relational closure and identity checks, one tested layer at a time.
8. Add deep recursive freezing, source-change detection and stale-fallback tests; verify no partial handle is observable on every failure.
9. Update CI ownership maps and their existing tests; verify exact changed-test targets and selected lanes against the real branch diff.
10. Run targeted PR02 suites, all affected regressions, owner/writer checks and the full applicable local validation set in the closed environment.
11. Inspect the entire diff for scope, generated residue, secrets/private data and actual manifest changes. `catalog/manifest.json` must be byte-identical to base.
12. Commit coherent changes, push, open one PR targeting `main`, and record base/head/tree and exact changed paths.
13. Obtain an actual code review and a security-focused review of the exact PR head. Read every finding; disposition with evidence; repair in scope; re-run affected and full tests; obtain corrected-code re-review where code changed.
14. Require all applicable exact-head CI lanes and final guard to pass. Record run/check/job/log identities, not just green counts.
15. Return `Ready to merge` with the PR reference and complete attribution to the Product Owner. Do not merge.

## 8. Test and adverse matrix

| Proof group | Positive case | Required refusal / no-success cases | Primary home |
| --- | --- | --- | --- |
| Gate normalization | Canonical ints and strings in arbitrary order yield identical sorted tuple, mask and 16-lower-hex | missing/non-list/empty; bool; 0/65; float; signs; whitespace; leading zero; decimal/exponent/nondecimal/Unicode digit; direct and numeric-equivalent duplicates | `tests/bodygraph/test_gates.py` |
| Complete synthetic admission | Labeled exact 41-member temp root returns `AdmittedMechanicsBundle` through real worker | Success is never described as actual release/deploy/readiness; placeholder files cannot be executed as mechanics | `tests/config/test_production_admission.py` |
| Actual baseline separation | Existing candidate loaders/projections retain bounded success where already valid | `load_active_mechanics_bundle()` on actual 15-member baseline yields typed incomplete-roster refusal and no handle | production-admission plus existing config suites |
| Canonical bytes | Exact canonical local JSON with one LF; exact valid Python/SQL member bytes | duplicate keys at governed depths, BOM, CRLF, extra LF, spacing/order/numeric noncanonicality, normalized-hash laundering, empty/invalid Python or SQL | production-admission / manifest tests |
| Schema/relations | Local schemas and complete Gate/Channel/profile/signal/category/default/source joins succeed | remote `$ref`; wrong IDs, operations, scales, defaults, order, type or closure; schema-valid but relationally incoherent graph | production-admission / existing contract tests |
| Root/capture | Two deliberately different valid roots yield internally consistent distinct identities and no cross-read | absolute/escape/backslash/dot/duplicate-separator path; file or ancestor symlink; missing/nonregular member; substitution/change between capture and verify; global-root leakage | production-admission |
| Manifest | Exact keys, `1.1.0`, adopted timestamp, sorted unique 41 roster and exact bytes/hash/size | missing/extra/duplicate/unsorted/unsafe member; wrong top/entry key; bad date/version/hash/size; self-list; unsupported format | production-admission / manifest tests |
| Candidate/admitted | Candidate APIs return only bounded candidate objects; full admission alone returns release-bearing bundle | generated snapshot, alias, config ID, direct selector, environment/CWD, skip/strictness flag, legacy success path or prior bundle cannot activate | production-admission / typed bundles / artifact tests |
| Identity | Config, source, manifest and release identities each equal their exact independent oracle | equality substitution or hash of rewritten bytes; release ID from config/pair/source rather than manifest bytes | production-admission |
| Deep immutability | Read all nested values after admission without mutation | mutate every mapping/list/record/profile/source/caps/category/signal/Channel level; caller/parser alias mutation; shallow freeze | production-admission |
| Failure/fallback | Every typed failure returns no object; a repaired fresh load can later succeed | stale cached success after corruption, partial object, exception suppression, legacy fallback | production-admission |
| CI ownership | Real diff resolves exact test targets and all classifier-selected lanes; classifier change selects seven lanes | missing owner/support map, nonexistent/symlink owner test, stale head, skipped lane or waiver | classifier + workflow integration tests |

Tests must mutate one property at a time and assert the owning typed failure code where stable. They must not compute expected output by calling the function under test. Temporary fixtures contain no real user, chart, credential, vendor or production data.

## 9. Validation commands and evidence contract

The engineer records exact commands, exit codes, test counts and UTC timestamps. Adapt only for action-time repository instructions; record any justified command delta.

```bash
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0
python -m pip install -r requirements-dev.txt
python -m pytest --version

python -m pytest -q -p no:cacheprovider -- \
  tests/bodygraph/test_gates.py \
  tests/config/test_production_admission.py \
  tests/config/test_manifest_schema.py \
  tests/config/test_magic10_contracts.py \
  tests/config/test_registry_catalog_contract.py \
  tests/config/test_typed_bundles.py \
  tests/config/test_config_artifacts.py \
  tests/config/test_config_loader_unknown_ids_fail_closed.py \
  tests/config/test_alias_policy_enforcement.py \
  tests/evidence/test_rails_ci_workflow_integration.py

python tools/config/generate_config_artifacts.py --check
python tools/config/generate_bundles.py --check
python scripts/release_id_recompute.py --check-manifest-only
python tools/evidence/update_evidence_index.py --check
python tools/evidence/orientation_demo.py --check
ci/checks/check_evidence_index_hash.sh
python tools/evidence/validate_evidence_paths.py
ci/checks/check_mirror_schema.sh
ci/checks/check_final_lf.sh

python -m pytest -q -p no:cacheprovider
git diff --check
git status --short --untracked-files=all
```

`release_id_recompute.py --check-manifest-only` proves only the current manifest's generic internal identity; it does **not** prove the 41-member active release. The separate actual-root admission test must prove typed incomplete-release refusal until PR06.

Run the classifier CLI with the real PR base/head and its documented `--event-name pull_request`, `--base`, `--head`, repository root and temporary output files. Confirm the changed-test output includes the Gate, admission and classifier owners and that the classifier change makes all seven lanes applicable. Do not invent placeholder SHAs in evidence.

Required native engineering evidence:

- exact base/head/tree, branch, PR URL/number and changed-path list;
- per-file/behavior attribution to this plan and PR01 dependency;
- exact local commands/results and tested commit;
- proof `catalog/manifest.json` and unrelated generated families did not change;
- code-review and security-review mechanism, reviewer/head, every finding and disposition;
- repair commits, corrected-code tests and re-review;
- exact current CI run, check, job and relevant log identities for all applicable lanes/final guard; and
- truthful remaining limits: synthetic full release only, actual promotion/runtime mechanics/consumer/QA/Ops incomplete.

Historical PR01 results or a green-count summary cannot substitute for PR02 evidence.

## 10. Requirement-to-change/test/evidence mapping

| Requirement | PR02 change | Test/evidence | Retained later owner / nonclaim |
| --- | --- | --- | --- |
| `K040-REQ-001` | Deliver ordered unit 2 as one bounded PR | dependency/base attribution, PR diff and acceptance record | No Epic completion; PR03–PR07/OPS01 remain |
| `K040-REQ-002` | Preserve PF01/PF02/PF12 homes and all C040 decisions | source ledger, conflict register, no alternative behavior | No Canon decision/publication |
| `K040-REQ-003` | Full admission executes PR01 Gate/Channel/Center/schema contracts | positive graph plus one-fault relation/schema cases | Data ownership remains PR01; mechanics PR03 |
| `K040-REQ-004` | Preserve Product metadata and existing candidate/public shapes while adding separate active interface | existing registry/bundle/artifact regressions | Application use PR04 |
| `K040-REQ-005` | Validate config/default and result-schema dependencies | local-schema/default/operation/scale refusal tests | Signal/category results PR03/04 |
| `K040-REQ-006` | Only complete exact roster returns immutable manifest-bound bundle; no fallback | synthetic success, actual-root refusal, missing/extra/stale cases | Actual complete promotion PR06; partial AC040-05 only |
| `K040-REQ-007` | Shared Gate normalizer and strict schema-loaded immutable bundle | exhaustive Gate and deep-freeze tests | PR03/04 consume interfaces |
| `K040-REQ-008` | Own Gate, raw bytes, schema, path, hash, immutability and admission refusal | adverse matrix with typed failures/no handle | Runtime/application refusal PR03–PR06 |
| `K040-REQ-009` | Separate config/source/manifest/release identities | independent exact hash oracles and substitution failures | Pair identity PR03; final proof PR06/OPS01 |
| `K040-REQ-010` | Provide stable inputs needed by all eight later goldens | interface-shape tests only | No golden computation; PR03–PR05 |
| `K040-REQ-011` | Complete PR02 adverse coverage | Gate/admission/immutability/fallback matrix | Identity/application/readiness coverage PR03–PR06 |
| `K040-REQ-012` | Preserve owning writers and same-root companion rules; no expected generation | check-mode outputs, clean diff | Final convergence PR06; external proof OPS01 |
| `K040-REQ-013` | Preserve instruction/Plan/dependency/commit/decision/prompt-use lineage | PR body, engineering evidence and final handoff | Repository prompt-use persistence separately authorized |

This produces PR02 contributions to AC040-01/02/03/04/07/08/09 and only the explicitly partial contribution to AC040-05. It does not complete AC040-05/06 or whole-chain acceptance.

## 11. Review, security, migration and release posture

### Code review

Review the entire exact-head diff for interface stability, validation order, exception boundaries, absence of duplicate authorities, candidate/admitted separation, test independence and changed-path ownership. Any repair invalidates earlier corrected-code coverage until affected tests and re-review are complete.

### Security review

Explicitly inspect:

- traversal, alternate separators, symlink ancestors/targets, TOCTOU detection and root mixing;
- duplicate JSON keys, canonical byte laundering, remote schema/network attempts and unsupported member types;
- argument/signature/environment/CWD selectors, bypass flags, hidden fallback/cache and exception suppression;
- raw payload or path leakage beyond allowed source-relative diagnostics;
- recursive immutability and caller/parser alias retention; and
- any accidental secret, birth/chart data, database/vendor call, settings mutation or live network access.

### Migration and compatibility

There is no data migration, database schema change, backfill, account mutation or public API change. Existing candidate loaders and FE/BE generators remain compatible. The new production entry point is additive and intentionally unavailable on the partial actual release. PR03 is the first consumer after PR02 acceptance.

### Release and deployment

There is no deployment, release cut, active config promotion, manifest rewrite or external attestation. The repository may merge PR02 while active admission continues to refuse the incomplete release. PR06 later assembles and validates the actual 41-member manifest after intervening owners land. Manual merge remains solely with the Product Owner.

## 12. Failure recovery and rollback

Before each write, preserve the action-time worktree capture and conflicting external changes. If implementation is interrupted, resume only after revalidating branch/head/status and attribution.

In-scope rollback restores the Gate module, registry-loader changes, test helpers/tests and CI ownership updates as one compatible set. Do not leave a production entry point that can return a shallow/partial bundle, and do not leave a new product source without a registered behavioral owner. Do not change or regenerate the actual manifest to make tests pass. A failed derived-generation or companion step restores its entire affected family through the owning mechanism; no partial success is claimed.

No promise is made for process-death atomicity, multi-file atomic visibility or cross-process locking beyond the mechanism actually reviewed and evidenced. The previously active complete release, if one exists at execution time, must remain untouched; a failed candidate never replaces it and no stale fallback is added.

Material boundary triggers requiring stop and rescope include: current repository instructions contradicting this plan; a changed approved final roster/manifest identity; need for a public API, DB/vendor/network/live setting, new schema semantics or actual manifest promotion; inability to preserve user work; or an upstream dependency no longer attributable to accepted PR01. Return the exact observed boundary to the Product Owner for the governed RS-10/RS-20 route rather than stretching PR02.

## 13. Dependency and PR ordering

```text
PR01 ACCEPT / merged #403
  -> PR02 this plan: normalizer + strict immutable admission
    -> PR03 pure Gate mechanics and intrinsic identity
      -> PR04 application/identity/consumer integration
        -> PR05 goldens and read-only readiness
          -> PR06 actual complete release admission/evidence convergence
            -> PR07 final repository documentation
              -> OPS01 authorized final clean-candidate external verification
```

PR02 should remain one PR because its normalizer, active-interface contract, admission machinery, adverse suite and CI ownership form one inseparable boundary. Splitting them would temporarily create either an unowned product source or an unproved active interface. If action-time constraints force multiple commits, they remain within one reviewed PR and one terminal PR02 acceptance result.

PR03 must not start from this plan alone. It consumes the merged/accepted PR02 interface only after PR02 engineering completion, merge by the Product Owner and later acceptance control.

## 14. Preserved Canon-conflict register and unresolved facts

| Entry | Preserved decision/current status |
| --- | --- |
| `C040-01 CANON_RECONCILIATION` | Thoth-17 `APPROVED` exactly at `2026-09-08T13:23:24Z`; current PF09.3 aligns; selected/excluded inventory and published Addenda 2.2/2.4 history retained. |
| `C040-02 CANON_RECONCILIATION` | Same Thoth decision; PF12 filename/body resolved at v2.9.6; discrepancy is history. |
| `C040-03 CANON_RECONCILIATION` | Same Thoth decision; PF14 filename/body resolved at v3.5.7; C040-05 legacy content remains separate. |
| `C040-04 CANON_RECONCILIATION` | Same Thoth decision; PF19 filename/body resolved at v3.0.5; no QA authority inferred. |
| `C040-05 CANON_RECONCILIATION` | Isis-49 `APPROVED` alternative A exactly at `2026-09-09T03:57:16Z`; four-argument Gate core, no optional scoring config/second calculator. PF14 §6.7 drainage pending/non-gating; Addendum 2.3 published; HDE-DIST008.1 separate. |
| `C040-06 NEW_CANON` | Isis-50 `APPROVED` alternative A exactly at `2026-09-09T11:48:08Z`; exact 36 assignments, 64 Gate facts and 16 states. PF10 Addendum 2.5 publication verified; permanent PF12/PF01 drainage and stale preparation wording pending/non-gating. |

None is `REJECTED` or `APPROVED_AS_CHANGED`. PR02 may enforce approved data/structure but cannot reopen or decide Canon.

Other non-gating facts:

- permanent C040-05/C040-06 Canon drainage stays with existing governed owners;
- `docs/changes/GCFPE_PROMPT_PROVENANCE.md` was absent at the verified baseline, so repository prompt-use persistence remains pending until an installed procedure and authorized writer exist; PR02 checks action-time state but does not invent the file;
- no platform Custom Agent session ID is available or invented; the user assignment establishes the dedicated role binding; and
- PR02 branch, implementation, tests, review, CI, PR and merge remain not produced by PR-20.

## 15. GCFPE prompt-use record

Inherited exact instruction-generation record:

```text
GCFPE-USE-HDE-EPIC040-PR-10-20260912-PR02-REV21-01
captured_at_utc: 2026-09-12T16:04:04Z
```

Current detailed-planning record:

```text
GCFPE_USE_ID: GCFPE-USE-HDE-EPIC040-PR-20-20260912-PR02-01
ecosystem_version: GCFPE-20260912.1
prompt_name: PR-20 — Create Detailed PR Implementation Plan — 091226.1
prompt_revision_retrieved_at: 2026-09-12T13:41:41.142Z
capture_at_utc: 2026-09-12T16:25:32Z
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR02
input: libfile_40f6b1d402808191b484e5929a6afcca
output: HDE-EPIC040-PR02-PRIP-v1.0
repository_persistence: NOT_PERFORMED — governed procedure absent at verified baseline; non-gating
```

## 16. Completion predicates for this plan

This implementation plan is complete and executable because it supplies exact lineage, current repository baseline, actual affected files and owners, stable interfaces, ordered changes, exact 41-member admission contract, adverse proofs, requirement/acceptance mapping, dependencies, review/CI evidence, security, migration, release and recovery treatment, continuing session identity and the direct next-control package.

Implementation completion later requires every item below:

- all eight planned file changes (or an explicitly justified in-scope refined set) are attributable on one PR head;
- all positive and adverse PR02 proofs pass on that same head;
- candidate behavior remains bounded and the actual partial release fails active admission;
- actual manifest and unrelated generated/evidence families remain unchanged;
- code/security review findings are fully dispositioned, repaired code is retested/re-reviewed and no unresolved blocking finding remains;
- all seven classifier-applicable CI lanes and final exact-head guard pass with retained identities; and
- the engineer returns `Ready to merge`, PR reference and truthful limits without merging.

## 17. Direct handoff to PR-30

`NEXT_PROMPT_HANDOFF`

**Destination:** [PR-30 — PR Implementation Proceed — 091226.1](https://app.notion.com/p/3d94590a05eb81bf8bc7d19de0c9b76f?pvs=204), verified path `AI Prompts / HDE IA`, retrieved revision `2026-09-12T13:41:46.491Z`.

**Receiving role/session:** continue this same dedicated HDE-EPIC040-PR02 engineering/planning session. Do not create or substitute another role session. `session_disposition: INITIAL_DEDICATED_ASSIGNMENT`; `context_conflict: NONE`.

**Exact required inputs:** this complete saved `PR_IMPLEMENTATION_PLAN` v1.0 plus sole instruction `libfile_40f6b1d402808191b484e5929a6afcca`, `CHANGE_ID: HDE-EPIC040`, `WORK_UNIT_ID: HDE-EPIC040-PR02`, complete lineage above, and a Product Owner invocation that explicitly supplies **Proceed** for this exact plan.

**Authorized on Proceed:** action-time preflight, in-scope implementation, local tests/checks, branch/commit/push/PR publication, actual code and security review, finding disposition, in-scope repairs, corrected-code re-review/retest, exact-head CI interpretation and engineering completion return.

**Not authorized by Proceed:** merge, QA/Ops, deployment, release/promotion, live vendor or DB action, Canon publication, scope expansion, Epic closure or repository prompt-provenance invention.

**Expected PR-30 terminal return:** `Ready to merge` only after all §16 engineering predicates pass, with exact PR/base/head/tree, changed paths, tests, review/security dispositions, CI identities and remaining limits. Otherwise return the precise blocked/rescope state; do not claim partial completion.

**Current handoff status:** `READY_FOR_PO_PROCEED`

## 18. Approval sentinel

**ASK OK? — PR IMPLEMENTATION PLAN**

`STATE: AWAITING_PO_PROCEED`

**END — HDE-EPIC040-PR02 PR IMPLEMENTATION PLAN v1.0**
