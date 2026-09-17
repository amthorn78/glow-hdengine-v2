---
artifact_type: RESCOPE_REQUEST
artifact_id: HDE-EPIC040-PR02-F03-RESCOPE-REQUEST
artifact_version: 1.0
state: RESCOPE_PENDING
status: RESCOPE_PENDING
decision: NOT_YET_REVIEWED
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR02
finding_ref: HDE-EPIC040-PR02-F03
originating_stage: RS-40 continuation of proceeded PR-30
producer_role: dedicated PR02 engineer
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: PR-02 HDE-EPIC040
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR02 / RS-40 / approved F01 and F02 overlays / PR404 / F03 manifest binding
context_conflict: NONE
ecosystem_release: GCFPE-20260913.1
prompt_version: 091326.2
selected_membership_count: 54
created_at_utc: 2026-09-13T19:10:19Z
---

# HDE-EPIC040-PR02 — F03 Existing Manifest Binding Rescope Request v1.0

## 1. Requested decision and exact material finding

State: **RESCOPE_PENDING**. Submit exactly one new formal request to the same continuing whole-change HDE-EPIC040 IA through [RS-20 — Review Bounded Work-Unit Rescope — 091326.2](https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb?pvs=204). F01 and F02 remain approved and drained. Their local correction is preserved. F03 is not approved, and no manifest/evidence exception has been applied.

F02/PF10 §2.9 requires each of four named modules—including `engine/serializer/canon.py`—to retain the actual top-level executing code object. The prepared local implementation of that approved predicate changes the wrapper from 485 to 795 bytes while retaining the shared serializer behavior; the code itself has not received independent approval. The same F02 overlay expressly freezes the actual 15-member manifest in PR02. That manifest already lists this wrapper with the old exact hash and size.

The unchanged owning gate `scripts/release_id_recompute.py::manifest_only_problems` audits actual bytes of every listed member. It reports exactly one mismatch: the wrapper. The other 14 member bindings still match. The existing canonical JSON gate's `_validate_release_manifest_snapshot` independently refuses `release_manifest_member_integrity_mismatch`, causing the one targeted fixture-proof failure. The CI release lane runs `python scripts/release_id_recompute.py --check-manifest-only`, so publishing this known state cannot satisfy required CI.

This conflict is now established from actual code and local gate results. It was not identified in the approved F02 request/review's feasibility treatment; those documents required both provenance-bearing modules and an unchanged 15-member manifest. It is separate from F01's Gate-schema closure, from the restored `.bytes` evidence file, and from the user-authorized archive removals.

Two bounded diagnostics test the ordinary alternatives without changing the repository manifest. Passing an in-memory one-row refreshed manifest to the existing snapshot validator succeeds using its own temporary fixture/canonical check. Restoring the exact old wrapper bytes only in an isolated 44-member test fixture makes active admission refuse `EXECUTION_PROVENANCE_UNAVAILABLE`. Thus simply restoring the old wrapper does not implement the approved F02 predicate. No captured source was executed by the production admission comparison; fixture imports are ordinary isolated test execution.

Removing provenance, substituting function-only/source-hash proof, weakening the integrity check, retaining unmanifested old source or introducing import/deployment machinery would change or evade the approved boundary. Deferring PR02 acceptance until PR06 would conflict with their dependency order. The smallest proposed correction is an explicit source-row maintenance exception with bounded owning evidence convergence. It requires the same IA's decision because the engineer cannot change the explicit current-manifest prohibition.

## 2. Immutable bases and approval lineage

| Native input / direct Drive link | Bytes | Verified SHA-256 |
| --- | ---: | --- |
| [Current controlled PF10 v13.2.2](https://drive.google.com/file/d/1suxrnM-g96R3tqThIpND3ll9s1qKaopK/view?usp=drivesdk) | 116473 | `d1db160a6a10aac25ed034e820f7026537cc9d178f22e8e978ed1620a61b0bec` |
| [F02 RESCOPE_REVIEW v1.0 — APPROVE](https://drive.google.com/file/d/18JGk0EwtaA5_ZD3WWZHJmacK139utjWa/view?usp=drivesdk) | 23615 | `b6b9c1c21976fd19f2a9fe5c5f802042a08b41d70fb3fef6a33d10afda3216c2` |
| [F02 PF10_BUILD_NOTES_ADDENDUM v1.0](https://drive.google.com/file/d/1I1O6_r4FVrE29m902lUqndR9uMXBiove/view?usp=drivesdk) | 19592 | `1c952386cd84eaf8a8aefbb33054b6a902d49ea73aa6f68239f099ad700a25fd` |
| [Reviewed F02 RESCOPE_REQUEST v1.0](https://drive.google.com/file/d/1nlCOzR3y9QvyynxFIFt9KU6U3urdUpCW/view?usp=drivesdk) | 53772 | `cbfe94dd0530a6dbc052de5e9c9e67ddce8f1a878a9d16d1726cd53234d11b38` |
| [Predecessor resumed PR_IMPLEMENTATION_RESULT v2.0](https://drive.google.com/file/d/16uYvir9dGnz8rp8fzoj1v_y67cQ_Wyc1/view?usp=drivesdk) | 25961 | `33061285197b364a85d742a8faab36e839233df149be3859956d2d42bf06ebd2` |
| [F01 RESCOPE_REVIEW v2.0 — APPROVE](https://drive.google.com/file/d/1rNSVietXHUCA8OG2xUWHeOHcQbFsUmKK/view?usp=drivesdk) | 22830 | `86509f67869c0a95e8b9e1035dc0dbebe4ca19f9d3ea8005127426bed075ffc8` |
| [F01 PF10_BUILD_NOTES_ADDENDUM v2.0](https://drive.google.com/file/d/17-TV-9KeP0c0KmHuhogik_uyYXyBqNPV/view?usp=drivesdk) | 16206 | `5ecc9850dc9f4368868ad1e4de15e249193e2bb81421e41095e4aed686c2874d` |
| [Pre-F02-drain PF10 v13.2.1 — lineage only](https://drive.google.com/file/d/1zCDNwfUjs9sqVZWK-nY2rGFmnpMg4RF1/view?usp=drivesdk) | 96335 | `5c0f6f96a52b8821cb7826d492b0066322bf5eb12b48eff5b390eee002e5a7c9` |
| [Approved Specification v1.1](https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk) | 64553 | `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| [Immutable whole-change Implementation Plan v2.1](https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk) | 146624 | `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| [Approving Implementation Plan Review v2.1](https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk) | 32843 | `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| [PR02 Instruction v1.0](https://drive.google.com/file/d/15XLW2D-E3Ke_dXKAtxIdytYErhIBz_Ki/view?usp=drivesdk) | 37078 | `429cda8e7f00bedc0509e9d00a16c72b37a49f5592054b2b8e069308e812047c` |
| [PR02 Detailed Implementation Plan v1.0](https://drive.google.com/file/d/1iOcCUsOMNuofrPboOyry7c-FDJWASvHQ/view?usp=drivesdk) | 42560 | `496488109e3fc080dd238145f28edf0a0824b5bb1ff068432e209813df9998e0` |
| [Original PR02 Implementation Result v1.0 — original Proceed](https://drive.google.com/file/d/1QfM27EepUYN3kZuqv_3-SgEk8VLph43d/view?usp=drivesdk) | 42408 | `779c425ba72c7df142f7ba1806ad1489785eb90de46493dac408e31bf53004e0` |
| [Governing operating procedure v3.1.0](https://drive.google.com/file/d/1KvX86E4yP4sGHC17tlcfCPRNavnhckEm/view?usp=drivesdk) | 22782 | `c62dde03425b09e1b8bc51b6cc5d870392075e8a0e0cd21ad961c7ecdc6d8e7c` |

The Specification approval remains Thoth-17 APPROVE, 2026-09-08T13:23:24Z. The whole-change Plan review remains Isis-50 APPROVE, 2026-09-09T13:36:43Z. No approved base is rewritten. F01's original proposal v1.0 remains available at https://drive.google.com/file/d/1nbkt7F4td7keMifg582PFiscWna5oRkH/view?usp=drivesdk as historical source; it is not substituted for the later decisions.

## 3. Verified manual drain and current Canon

Current authoritative source: [PF10-HDE-Build-Notes-v13.2.2.md](https://drive.google.com/file/d/1suxrnM-g96R3tqThIpND3ll9s1qKaopK/view?usp=drivesdk), 116,473 bytes, SHA-256 `d1db160a6a10aac25ed034e820f7026537cc9d178f22e8e978ed1620a61b0bec`. It was independently resolved through Glow / Core Docs / PFCanon, with direct parent `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3`; only one current controlled PF10 Markdown was selected. Native Google Docs and repository PF copies were not substituted.

Nathan's invocation asserts his completed manual drain. The engineer independently compared the complete body beginning `## 2.9 HDE-EPIC040-PR02-F02 — Executing-Code Coherence Rescope` with the approved F02 addendum. Substantive content matches. Raw Markdown is not byte-identical: emphasis, escaped punctuation, self-label links, table alignment, list markers and whitespace differ. The terminal PF10 `<eof>` marker is outside the addendum and excluded. No substantive clause is waived; the standalone YAML transport envelope is not treated as page body. F01 §2.7 remains byte-identical to its section in pre-F02 PF10 v13.2.1; §2.8's form rule remains present.

The review's historical state `APPROVED_PENDING_MANUAL_PF10_DRAIN` and the standalone addendum's `READY_FOR_MANUAL_DRAIN` / `NON_CANONICAL_PENDING_MANUAL_DRAIN` labels remain source metadata. The current PF10 body and independent comparison establish the effective overlay. F01 and F02 are approved and drained; F03 is new and unapproved. No PF10 edit or addendum was made by this engineer.

## 4. Repository, authority and recovery continuity

- Continuing engineer/session: `PR-02 HDE-EPIC040`; `RETAIN_EXISTING`; `MANUAL_PROMPT_EXECUTION`; `context_conflict: NONE`.
- Same whole-change IA: the continuing Product Owner-assigned HDE-EPIC040 Implementation Agent that issued the linked F01/F02 reviews. No replacement session or fabricated platform identifier is assigned.
- Repository: `amthorn78/glow-hdengine-v2`; [existing PR404](https://github.com/amthorn78/glow-hdengine-v2/pull/404), open, draft and unmerged at the fresh read `2026-09-13T18:59:04.678Z`.
- Existing branch: `hde-epic040-pr02-immutable-admission`; current local and remote head `eed8a63807f573abc29de6f6d5ceac54f0c8da85`; tree `b0cc12ae82b597bd4f7f226b4812a8cf7dfa7a8d`.
- Immutable accepted base: `3828d4b3454259841a3e48d13039dd1475754f2f`; base tree `529306a74268f2a46765bf40defdae49026d103e`.
- Ordered attributable commits remain `3dda87853466fa18247654ffe5bb67561364b0f4` (tree `083a787c16a06328622cde0ca93f22508f16146b`) then `eed8a63807f573abc29de6f6d5ceac54f0c8da85`. No new commit, push or PR was created.
- Same recovery directory/worktree: `/workspace/scratch/b736cdb96988/pr02-recovery`. Missing files and Git metadata were restored around the four preserved files. Exact original commit and tree identities were reconstructed and verified, not replaced with newly authored materialization commits. The local Git history is shallow at the accepted base.
- Original earlier workspace `/workspace/scratch/8d666e9ba95b/glow-hdengine-v2` remains inaccessible/absent here and unchanged. No replacement workspace was created.
- The original Product Owner Proceed preserved in Implementation Result v1.0 remains the implementation authority. No replacement instruction, detailed Plan, whole-change Plan/review or Proceed was authored or requested.

Recovery restored 5,282 missing nonbinary working files. The only remaining unavailable historical blob objects are the five user-authorized retired archives; their originals remain in remote Git history. Their deletions are in the current index. The previously missing ordering digest was restored by its canonical generator and exactly matches both its recorded Git blob and SHA-256. Repository implementation and validation now run in the same recovered directory. Native Git authentication was unavailable; connected GitHub reads recovered exact objects. This is no longer a missing-working-file recovery blocker, but it is not a claim of complete local pre-base or archive history.

## 5. Exact proposed bounded delta — decision pending

The requested decision is a narrowly bounded exception to the actual-manifest freeze, not a replacement Plan or a new source/execution design. The following is **proposed and not implemented**:

1. Permit PR02 to rebind only the existing `engine/serializer/canon.py` row in `catalog/manifest.json` to the exact final reviewed provenance-bearing wrapper bytes, using the existing canonical manifest writer. Change only that row's `sha256` and `size`. Keep the actual roster at 15, preserve its other 14 rows, ordering, `root`, `version` and `built_at_utc`, and add no F01/F02/future member to the actual manifest in PR02.
2. Keep `release_id = sha256(exact manifest bytes)` and all separate source/config/manifest identities. A source-row refresh necessarily changes the manifest/release identity value; do not keep a stale release identifier or mislabel this as byte-unchanged. On the present preserved candidate, the old row is `f56cdacfb90b7d9cb467d7e6005ad62e62e83d4b04c022c53e9f9b190e7777c3:485` and the proposed row is `2a077c957c7526f9c0fe9c482d299b6912df05b084fa5fc9c5f63b555e23eec5:795`. The unchanged actual manifest is `c0f5f24fbbcbb04d01d1613be386c26fddbfb37d53cbb0f9c65d5cf55e97c2a4` (1,981 bytes). An in-memory one-row refresh has proposed manifest/release SHA-256 `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856` (1,981 bytes). These candidate values are evidence, not a fixed future hash independent of final review corrections.
3. Permit only the corresponding existing canonical JSON gate/evidence maintenance required by this source-row refresh. The gate owner is `tools/evidence/run_canonical_json_gate.py`; its six current outputs are `audit/gates/canonical_json/json_canonical_check.log`, `audit/gates/canonical_json/json_canon_compare.log`, `audit/gates/canonical_json/canonical_json.gate.json`, `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, and `audit/gates/json_gate/canonical/json_gate_structured_record.json`, with their owned `.path_proof.txt` companions. The sole evidence updater owns any resulting INDEX/Mirror/checksum/orientation/path-proof convergence in its existing families. Do not hand-edit evidence, recapture historical vendor/QA/Ops/CLI inputs, rewrite capture-time identity claims, introduce a new evidence family, or refresh unrelated artifacts. An additional required identity/evidence family outside this explicit closure requires its owning decision rather than an open-ended cascade.
4. Preserve all strict manifest content, canonical JSON, ownership and CI checks. No special-case waiver, ignored serializer row, xfail, narrowed assertion, fake hash, unmanifested old-source authority, import hook, loader/reload scheme, `sys.modules` mutation, duplicate serializer or altered deployment protocol is proposed.
5. PR02 remains responsible for its F01/F02 implementation, this one existing-row maintenance exception, corresponding local tests and exact-head review/CI. PR06 retains the final complete **44-member** actual-manifest materialization, complete member refresh, final identity recomputation/convergence and eventual promotion after PR03–PR05. The proposed exception does not move final 44-member promotion to PR02 or change unit order. PR03–PR05 and PR07 retain their existing owners and scope.
6. Keep Specification intent, requirement wording, mathematics, taxonomy, public/API/CLI contracts and identity formulas unchanged. K040-REQ-007/008/009 and existing K040-REQ-011/012 evidence/ownership duties require reconciliation of the actual maintained source and manifest; AC040-04/05 retain their existing PR02 versus PR06 completion split. No PR01 rerun, QA/Ops, live vendor/database work, release activation, deployment, merge, PF10 edit or Epic closure is authorized.
7. If the same IA approves this exact bounded exception, it produces one native RESCOPE_REVIEW and exactly one separate page-ready PF10_BUILD_NOTES_ADDENDUM under the current form rule. Nathan alone manually drains and verifies it. Only then may the same PR02 session resume via selected RS-40 under the original Proceed and apply that explicit exception.

The IA must decide whether this is a permissible bounded implementation/evidence-maintenance overlay within the approved Specification, and expressly reconcile the existing unchanged-manifest clause. This engineer does not self-approve it. If the proposed closure is insufficient or conflicts with a remaining owning rule, return precise bounded redlines or the actual Product Owner/Specification question through the native selected result; do not approve an unspecified integrity mechanism or assume permission to rewrite historical evidence.

## 6. Prepared implementation and retained limits

The coherent local correction is prepared, uncommitted and preserved; independent corrected-candidate review and merge readiness are not claimed.

- F01: `schemas/gates_v1.schema.json` is a manifest-bound required member; `_load_gates` executes the existing owning schema validator on captured Gate bytes before active admission. Captured schema identity, canonical bytes, local references and relational checks remain enforced. Missing, rejecting, malformed and unbound schema/member cases remain covered.
- F02: the synthetic complete roster is exactly 44. It adds `engine/stable/sercanon.py` and `engine/categories/registry.py` to F01's 42. All four named modules retain their actual top-level execution code and origin/compilation provenance. Admission validates the four actual owners, safe common origin and matching interpreter/optimization semantics, then compares retained code with compilation of exact captured manifest-bound bytes using `dont_inherit=True`. Captured source is not executed or reimported.
- The shared serializer wrapper, underlying serializer and category registry remain their owners. The prior duplicate serializer, copied category order and import-time disk hash attempt were removed from the current correction. Their complete prior state remains recoverable in the predecessor F02 request and the original four-file snapshot.
- Ordinary repair 3997351895: the packaged manifest is captured once and final verification uses its retained metadata instead of physically rereading it. A descriptor-level `os.open` observation checks one physical manifest open on success, malformed manifest, member hash failure and manifest change after capture. Other members retain rereads and the complete final identity pass.
- Existing symlink refusal, inter-read mutation detection, recursive freezing, no fallback and the explicit non-atomicity limit remain. Public admission fixes the verified execution root. The existing private fixture seam can use copied identical implementation bytes, still requiring all four executable comparisons.
- Tests cover fresh public imports at optimization levels 0/1/2; materially changed captured source for each module; source replaced after import; timestamp-valid stale bytecode A versus source B, with actual A/B behavior and fresh B separately checked; unsupported provenance, live origin disagreement and real deployment symlinks; 42/43/45 roster refusal; helper absence/format/hash/size/change/symlink refusal; unavailable captured members; actual shared consumers; and physical manifest read counts.
- The existing CI classifier registers exact ownership for the added tests/owners and the exact five retired archives; `.gitignore` conservatively selects full validation. It does not change workflow triggers, suppress required tests, or exempt the manifest check.

The claim remains executable-code equivalence for four modules, distinct from exact source/config/manifest/release identities. It is not exact historical imported-source byte identity, universal runtime integrity, arbitrary in-process tamper resistance, process-death atomicity, multi-file atomic visibility, cross-process locking or stronger deployment portability. The actual 15-member manifest is still byte-for-byte unchanged and production active admission remains incomplete until PR06.

## 7. Local validation and exact failure evidence

Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Python 3.12.14 and pytest 8.4.2; repository runtime/dev dependencies and the editable project were installed. Isolated child interpreters have their dependencies installed in the local virtual environment. These are development checks, not QA/Ops execution or live vendor/database testing.

| Local check | Result | Log SHA-256 |
| --- | --- | --- |
| targeted | 562 passed; 1 failed (manifest-dependent canonical gate) | `549701d29259c8ff33caf2f0712afc3481e99757c1ddd861244f94e312ba297f` |
| regression | 1,800 passed; 3 existing closed-rails vendor skips | `401b72383c47111e9fef335bbbcdb2f7c3556bcc7637b6d7785f70841061b46f` |
| config-artifacts | PASS | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| bundles | PASS | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| manifest-integrity | FAIL — exact existing-member hash/size mismatch | `11dc56dc123902dc4c6dc666f07601c991d3e6fb8c88183de70b27daf445cd40` |
| evidence-index | PASS | `82ea36a3eb90ae8477d61e1c51eeb918e8c5139890885823dd52b6f4c3add06d` |
| orientation | PASS | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| index-hash | PASS | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| evidence-paths | PASS | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| mirror-schema | PASS | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| final-lf | PASS | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |


Targeted execution: 2026-09-13T18:58:12.932179+00:00 to 2026-09-13T18:59:04.613911+00:00; 51.681 seconds. Default regression: 2026-09-13T18:59:04.614293+00:00 to 2026-09-13T19:00:35.222621+00:00; 90.608 seconds. JUnit records corroborate 563 targeted test cases (one failure), and 1,803 regression cases (three skipped, zero failures/errors). The skipped cases are `test_two_run_identity_and_reemit`, `test_ab_ba_identity_and_artifacts`, and `test_reader_dump_matches_runtime` in `tests/cli/test_showcompat_parity_and_identity.py`; they require open rails and were not run live.

The sole targeted failure is `tests/evidence/test_rails_ci_workflow_integration.py::test_open_rails_producer_check_mode_has_no_repo_residue`, which reaches the existing canonical JSON gate. Its fixture-backed validation makes no live vendor call. The exact direct writer failure is:

```text
MANIFEST_ERROR:manifest_file_audit:BAD engine/serializer/canon.py expected f56cdacfb90b7d9cb467d7e6005ad62e62e83d4b04c022c53e9f9b190e7777c3:485 got 2a077c957c7526f9c0fe9c482d299b6912df05b084fa5fc9c5f63b555e23eec5:795
```

No failing test was skipped, xfailed, weakened or relabeled passing. Earlier diagnostic runs had dependency isolation, observation-path and test expectation errors; those ordinary test defects were corrected before this recorded batch. The results above supersede those attempts only for the exact preserved local file hashes. They are not exact-new-commit evidence because no new commit exists.

Changed-path classification passes for all 16 local paths and the 20-path cumulative base-to-candidate set, selecting all seven lanes. The owning test-target mapping resolves. `git diff --check` and staged text whitespace checks pass. Worktree status is intentionally dirty: five staged archive deletions, ten modified tracked text files and one new test file. The expected changed set was checked; it is not reported as a clean committed worktree. Historical archive deletion checks use exact index/tree metadata because those five old binary objects are unavailable locally. No full-history fsck or binary patch validation is claimed.

Exact commands and log references:

- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python -m pytest -q -p no:cacheprovider --tb=short --junitxml /workspace/scratch/2cc1d0be2240/rs40-f02-checks/targeted.junit.xml -- tests/bodygraph/test_gates.py tests/config/test_production_admission.py tests/config/test_execution_coherence.py tests/config/test_manifest_schema.py tests/config/test_magic10_contracts.py tests/config/test_registry_catalog_contract.py tests/config/test_typed_bundles.py tests/config/test_config_artifacts.py tests/config/test_config_loader_unknown_ids_fail_closed.py tests/config/test_alias_policy_enforcement.py tests/evidence/test_rails_ci_workflow_integration.py tests/cli/test_serializer_guards.py tests/categories/test_registry_and_purity.py tests/order/test_ordering_artifacts_stability.py`
- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python -m pytest -q -p no:cacheprovider --tb=short --junitxml /workspace/scratch/2cc1d0be2240/rs40-f02-checks/regression.junit.xml`
- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python tools/config/generate_config_artifacts.py --check`
- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python tools/config/generate_bundles.py --check`
- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python scripts/release_id_recompute.py --check-manifest-only`
- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python tools/evidence/update_evidence_index.py --check`
- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python tools/evidence/orientation_demo.py --check`
- `bash ci/checks/check_evidence_index_hash.sh`
- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python tools/evidence/validate_evidence_paths.py`
- `/workspace/scratch/b736cdb96988/pr02-recovery/.venv/bin/python ci/checks/check_mirror_schema.sh`
- `bash ci/checks/check_final_lf.sh`

Scratch evidence lives at `/workspace/scratch/2cc1d0be2240/rs40-f02-checks`. The native result/request carries its hashes, outcomes, failure text and the complete current textual correction so these conclusions do not depend on an unlinked scratch directory.

## 8. Reviews, CI and unresolved owners

Fresh repository read `2026-09-13T18:59:04.678Z` confirms all seven original review threads remain unresolved. Their historical comments are not rewritten as current-candidate acceptance.

| Finding / thread | Current classification and owner |
| --- | --- |
| 3997320377 / 3997320916 | F01 authority approved/drained; local owning-schema implementation and focused proof prepared. PR02 engineer still owns completion; repository reviewer owns final disposition. |
| 3997320380 | Existing symlink correction preserved, with actual public import-origin tests added. Repository reviewer owns final disposition. |
| 3997320917 | Bounded inter-read correction and explicit non-atomicity limit preserved. Repository reviewer owns final disposition. |
| 3997351895 | Ordinary one-physical-manifest-read repair and success/adverse proof prepared locally; final reviewer disposition remains pending. |
| 3997351898 | F02 authority approved/drained; four-module code-equivalence and 44-member implementation prepared and focused tests pass. New F03 manifest/evidence conflict prevents publication. |
| 3997351903 | `CONFLICTS_WITH_EXPLICIT_APPROVED_LIMITATION`; no expanded atomicity, cross-process lock, immutable deployment or stronger portability was implemented. Repository review owner retains final disposition. |
| HDE-EPIC040-PR02-F03 | Newly established local manifest/provenance contradiction. No GitHub discussion ID is invented. Same whole-change IA owns the bounded RS-20 decision. |

Historical security comment [5648272341](https://github.com/amthorn78/glow-hdengine-v2/pull/404#issuecomment-5648272341) reports no findings for `eed8a63807f573abc29de6f6d5ceac54f0c8da85` only. Historical CI [34715034846](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34715034846), workflow 192291018, run number 3565, remains completed/success for that same head. All seven historical CI lanes, 472 targeted passes, 1,724 regression passes and three existing skips remain attributed solely to that published head.

No new candidate was pushed, no substantive code/security review against new source was requested, no thread was self-resolved and no new CI run was started. The fresh commit-run read returns only the completed historical run; no active PR02 run needed cancellation. Current working-source tests cannot turn old security/CI evidence into final-head evidence. After a permitted complete correction, current-head substantive review and actual owner dispositions must precede final-candidate CI. No merge-readiness or waiver is inferred.

## 9. Separate Product Owner archive cleanup and preserved binary evidence

Nathan's later request, “can you remove the archives, or at least untrack them?”, explicitly authorizes this separate housekeeping change. Exactly these five paths were untracked locally and receive exact ignore entries. Deletions are staged; no remote deletion or history rewrite has occurred. These are archive removals, not deletion of current primary evidence. Historical inventory references remain historical and were not edited.

| Retired archive | Historical bytes | Recorded Git blob |
| --- | ---: | --- |
| `.backup_epic004/changelog_20251024121758.tgz` | 3377 | `8a42139545e06ced6540fb749755bc334d2b583b` |
| `_backup_1761350008.tgz` | 82375 | `fea562083cb704e60a00f634b3022919aeb9c413` |
| `_backup_corrupted_1761349750.tgz` | 94584 | `14fb708b5ee17627f4025a05083444eb36244716` |
| `_backup_corrupted_1761349780.tgz` | 96598 | `2f0a423cd24e736749a89c3bae7e12157a14910b` |
| `handoff/epic004_live_evidence_20251022T202304Z.tar.gz` | 368739 | `49977f3d57d9a6d7df04d0697902f8bd159a52b6` |

`artifacts/engine/order/abba_identity.bytes` is not an archive. It is the generated 32-byte SHA-256 digest used by the AB↔BA ordering-evidence family, its index/path proofs and `tests/order/test_ordering_artifacts_stability.py`. It is not loaded by active mechanics admission. It was kept and restored through `tools/order/generate_ordering_artifacts.py`, after proving the other owning outputs already matched. Its SHA-256 is `5dd560e80a411b3e428d4f8190740f269c1020b401410129b28d55ab803e2ae2`; its Git blob is `0949b8e6d0ee5fc2e50fcace9decb7cda74964e0`. It has no tracked diff. This restoration supplies required evidence bytes; it does not create new acceptance evidence.

## 10. Carried Canon-conflict register

| Entry | Preserved disposition / owning source |
| --- | --- |
| C040-01 | CANON_RECONCILIATION / APPROVED by Thoth-17, 2026-09-08T13:23:24Z; PF10 §§2.2/2.4 retained. |
| C040-02 | Same Thoth-17 approval; PF12 identity history and PF10 §§2.2/2.4 retained. |
| C040-03 | Same Thoth-17 approval; PF14 identity history and PF10 §§2.2/2.4 retained. |
| C040-04 | Same Thoth-17 approval; PF19 identity history and PF10 §§2.2/2.4 retained. |
| C040-05 | CANON_RECONCILIATION / APPROVED, alternative A, by Isis-49, 2026-09-09T03:57:16Z; PF10 §2.3 retained. |
| C040-06 | NEW_CANON / APPROVED, alternative A, by Isis-50, 2026-09-09T11:48:08Z; PF10 §2.5 retained. |
| HDE-EPIC040-PR02-F01 | BOUNDED_WORK_UNIT_RESCOPE / APPROVED by linked RESCOPE_REVIEW v2.0; effective PF10 §2.7, owning Gate schema/member 42 only. |
| HDE-EPIC040-PR02-F02 | BOUNDED_WORK_UNIT_RESCOPE / APPROVED by linked RESCOPE_REVIEW v1.0; effective PF10 §2.9, four-module executable equivalence and complete synthetic roster 44 only. |
| HDE-EPIC040-PR02-F03 | BOUNDED_WORK_UNIT_RESCOPE / REQUESTED, NOT_YET_REVIEWED. Existing serializer-source binding versus unchanged actual 15-member manifest and mandatory integrity/evidence checks. No approval or Canon adoption is claimed. |

## 11. Native return and required next action

The same continuing whole-change HDE-EPIC040 IA reviews this exact request under selected RS-20 and returns one complete RESCOPE_REVIEW with the actual native classification. The requested scope is solely the existing serializer row and explicitly bounded owning evidence maintenance. F01/F02 decisions, original Proceed and all accepted earlier work remain effective within their existing scope. No new decision owner, replacement Plan or instruction, renewed Proceed, PR01 rerun, RS-10 insertion, IA Plan restart or PR-50 route is created.

If APPROVE, the IA produces exactly one separate read-back PF10_BUILD_NOTES_ADDENDUM and a conditional return to this same PR02 session via RS-40 after Nathan's manual drain and verification. The engineer must then independently verify the drain, recover the exact preserved directory/head/delta, apply only the approved exception, resolve ordinary findings, rerun required local checks before a coherent push, obtain substantive code/security review on the actual corrected head, obtain repository-owner dispositions, and run final CI once on the exact candidate. No merge is authorized. No post-merge PR-40 handoff is applicable now.

## 12. Prompt-use evidence

Usage `GCFPE-USE-HDE-EPIC040-PR02-RS40-F02-20260913-02`: RS-40 / 091326.2, [exact selected page](https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3?pvs=204), retrieved page revision 2026-09-13T11:35:51.889Z. Role/stage: continuing PR02 engineer, approved F01/F02 implementation, local validation and F03 boundary return. Exact Specification v1.1 and work-unit/component/requirement references are carried above. Capture/result time `2026-09-13T19:10:19Z`; selected release GCFPE-20260913.1, 54 members, [selection register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1?pvs=204). Runtime model configuration is not a routing or approval field. Prior uses remain retrievable in linked Results v1.0/v2.0 and reviews; none are overwritten.

RS-20 / 091326.2 was fetched for receiver compatibility only (page revision 2026-09-13T11:33:42.699Z), not executed and no other session was messaged. Repository prompt-use persistence remains pending/non-gating: no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` writer/procedure was found. The next authorized repository writer must use an actually installed supported schema; no new process file or fabricated record was committed.

## 13. Complete preserved recovery delta

The complete four-file pre-recovery delta was copied byte-for-byte to `/workspace/scratch/2cc1d0be2240/rs40-f02-sources/preserved-before-recovery` before restoring repository files or changing source. The predecessor F02 request also durably carries it. Its initial identities are:

| Preserved file | Bytes | SHA-256 |
| --- | ---: | --- |
| `engine/config/registry_loader.py` | 68380 | `79fa00ca3dcb5c9b311ae1174aa8b1d7f9ddac4d72a786d42fbb4f995369a556` |
| `tests/artifacts/test_cli_text_artifacts_bom_lf.py` | 858 | `c3279c6654e58d1b2c6fd6ef9f298c553ff74ef9056784885fc179f12b137d59` |
| `tests/config/helpers.py` | 4668 | `cea929551e632fd85428219092a66a19b038f5c6ef739cd770a0e7323fcd7335` |
| `tests/config/test_production_admission.py` | 27750 | `fbfed8cfce48e6024296fc765d5aea5dfd46a5ec3962d24896dd659545084262` |

The pre-existing `tests/artifacts/test_cli_text_artifacts_bom_lf.py` terminal-LF-only change remains preserved, with the same hash as on entry. It is not relabeled as new F01/F02 behavior. Current local path identities are:

| Current local path | State / bytes | SHA-256 |
| --- | --- | --- |
| `.backup_epic004/changelog_20251024121758.tgz` | staged deletion | `not applicable — archive deletion` |
| `.gitignore` | 779 | `faa44479e92b9c7b379875a0fb8faecbda421836a4f1c1f8b16cdf2b6e074d8c` |
| `_backup_1761350008.tgz` | staged deletion | `not applicable — archive deletion` |
| `_backup_corrupted_1761349750.tgz` | staged deletion | `not applicable — archive deletion` |
| `_backup_corrupted_1761349780.tgz` | staged deletion | `not applicable — archive deletion` |
| `ci/checks/classify_ci_changes.py` | 59775 | `20626dfd2f957236dee6f7f3140c6e95614520275225ec6507b3ef6dfbc8f21b` |
| `engine/categories/registry.py` | 878 | `9a2dbee668d45d0ba43eb9ccc03830862b75e97faf66ccc983ff00c3981d6e87` |
| `engine/config/registry_loader.py` | 72173 | `7be9af94867d9b7218848e6c17deebaacdba1b3dbc9863f51905450f7e8a0dc3` |
| `engine/serializer/canon.py` | 795 | `2a077c957c7526f9c0fe9c482d299b6912df05b084fa5fc9c5f63b555e23eec5` |
| `engine/stable/sercanon.py` | 862 | `8280ff1148b367824ab450abf5ba35b3799ec9175c633bd975407179c0226f38` |
| `handoff/epic004_live_evidence_20251022T202304Z.tar.gz` | staged deletion | `not applicable — archive deletion` |
| `tests/artifacts/test_cli_text_artifacts_bom_lf.py` | 858 | `c3279c6654e58d1b2c6fd6ef9f298c553ff74ef9056784885fc179f12b137d59` |
| `tests/config/helpers.py` | 4668 | `5da509830ae35c4cbf6f8bb7a86bcd917ef13329c27b00580d66bf1981ddbc4f` |
| `tests/config/test_execution_coherence.py` | 16038 | `900df0f1b67129b9ba214841576ce77d7587a10408f318c1ddac5cba55cb6702` |
| `tests/config/test_production_admission.py` | 27868 | `e7d0061ff8d12d8666b6106bc8be28469a76cc2017e9802ac6672a3ddcb0cb88` |
| `tests/evidence/test_rails_ci_workflow_integration.py` | 74401 | `2c5879d6a26ebdfd1ba733d3ae2f6dac1073d25706a3cd10a150db2ebe6bcae8` |

Exact current Git status:

```text
D  .backup_epic004/changelog_20251024121758.tgz
 M .gitignore
D  _backup_1761350008.tgz
D  _backup_corrupted_1761349750.tgz
D  _backup_corrupted_1761349780.tgz
 M ci/checks/classify_ci_changes.py
 M engine/categories/registry.py
 M engine/config/registry_loader.py
 M engine/serializer/canon.py
 M engine/stable/sercanon.py
D  handoff/epic004_live_evidence_20251022T202304Z.tar.gz
 M tests/artifacts/test_cli_text_artifacts_bom_lf.py
 M tests/config/helpers.py
 M tests/config/test_production_admission.py
 M tests/evidence/test_rails_ci_workflow_integration.py
?? tests/config/test_execution_coherence.py
```

The complete current textual delta relative to `eed8a63807f573abc29de6f6d5ceac54f0c8da85` is embedded below (47,076 bytes; SHA-256 `a2644c0e7c8b802c274e46c8074db569e1e02e7c339f9188ac73a5690bae8af2`). The five binary archive removals are separately identified by exact path/blob above; no unavailable archive bytes are invented. Preserve the existing directory/index/delta. On later recovery compare hashes and restore only genuinely missing content around the preserved work; do not overwrite it, create another implementation, or replay this patch blindly over an already changed tree.

```diff
diff --git a/.gitignore b/.gitignore
index b08e679..a939784 100644
--- a/.gitignore
+++ b/.gitignore
@@ -17,6 +17,11 @@ VERIFY.out
 # Backups/temps
 *.bak
 server_backup.tar
+/.backup_epic004/changelog_20251024121758.tgz
+/_backup_1761350008.tgz
+/_backup_corrupted_1761349750.tgz
+/_backup_corrupted_1761349780.tgz
+/handoff/epic004_live_evidence_20251022T202304Z.tar.gz
 EPIC1_PATCH_PACKET_*/
 artifacts/bodygraph/refresh_state.json
 
diff --git a/ci/checks/classify_ci_changes.py b/ci/checks/classify_ci_changes.py
index 0533797..f50f763 100644
--- a/ci/checks/classify_ci_changes.py
+++ b/ci/checks/classify_ci_changes.py
@@ -29,6 +29,7 @@ _FULL_VALIDATION_PREFIXES = (
     ".github/",
 )
 _FULL_VALIDATION_PATHS = {
+    ".gitignore",
     "ci/checks/classify_ci_changes.py",
     "pyproject.toml",
     "pytest.ini",
@@ -48,6 +49,7 @@ _FULL_VALIDATION_SUPPLEMENTAL_TESTS = (
     "tests/config/test_alias_policy_enforcement.py",
     "tests/config/test_config_artifacts.py",
     "tests/config/test_config_loader_unknown_ids_fail_closed.py",
+    "tests/config/test_execution_coherence.py",
     "tests/config/test_manifest_schema.py",
     "tests/config/test_magic10_contracts.py",
     "tests/config/test_production_admission.py",
@@ -97,6 +99,11 @@ _HISTORICAL_PREFIXES = (
     "audit/historical/",
     "audit/ops/",
 )
+_HISTORICAL_PATHS = {
+    # Exact legacy archives retired by the Product Owner during PR02 recovery.
+    ".backup_epic004/changelog_20251024121758.tgz",
+    "handoff/epic004_live_evidence_20251022T202304Z.tar.gz",
+}
 _DOCUMENTATION_PREFIXES = (
     "docs/crd/",
     "docs/pfcanon/",
@@ -317,8 +324,21 @@ _PRODUCT_TEST_OWNER_PATHS = {
         "tests/config/test_alias_policy_enforcement.py",
         "tests/config/test_manifest_schema.py",
         "tests/config/test_production_admission.py",
+        "tests/config/test_execution_coherence.py",
         "tests/config/test_typed_bundles.py",
     ),
+    "engine/serializer/canon.py": (
+        "tests/cli/test_serializer_guards.py",
+        "tests/config/test_execution_coherence.py",
+    ),
+    "engine/stable/sercanon.py": (
+        "tests/cli/test_serializer_guards.py",
+        "tests/config/test_execution_coherence.py",
+    ),
+    "engine/categories/registry.py": (
+        "tests/categories/test_registry_and_purity.py",
+        "tests/config/test_execution_coherence.py",
+    ),
     "engine/config/bundles.py": ("tests/config/test_typed_bundles.py",),
     "catalog/manifest.json": (
         "tests/runtime/test_identity.py",
@@ -551,6 +571,7 @@ _CONFIG_WRITER_TEST_OWNERS = {
 }
 _TEST_SUPPORT_OWNER_PATHS = {
     "tests/config/helpers.py": (
+        "tests/config/test_execution_coherence.py",
         "tests/config/test_registry_catalog_contract.py",
         "tests/config/test_magic10_contracts.py",
         "tests/config/test_alias_policy_enforcement.py",
@@ -1315,7 +1336,7 @@ def _lanes_for_path(path: str) -> set[str] | None:
         return set()
 
     historical_namespace = path.startswith(("audit/", "artifacts/", "docs/", "reports/"))
-    if path.startswith(_HISTORICAL_PREFIXES) or (
+    if path in _HISTORICAL_PATHS or path.startswith(_HISTORICAL_PREFIXES) or (
         historical_namespace
         and any(
             _contains_component(path, component)
diff --git a/engine/categories/registry.py b/engine/categories/registry.py
index 3e974aa..680287e 100644
--- a/engine/categories/registry.py
+++ b/engine/categories/registry.py
@@ -1,6 +1,16 @@
 """Category registry with frozen Magic-10 order (EPIC006)."""
+import sys as _sys
 from typing import Callable, Dict, Tuple
 
+# Passive, immutable top-level execution provenance for active admission.
+try:
+    _MODULE_EXECUTION = (
+        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
+        _sys.flags.optimize, _sys.implementation.cache_tag,
+    )
+except Exception:
+    _MODULE_EXECUTION = None
+
 FROZEN_MAGIC10_ORDER = ("harmony","heat","communication","alignment","comfort","consistency","expansion","creativity","drive","balance")
 _REG: Dict[str, Callable] = {}
 
diff --git a/engine/config/registry_loader.py b/engine/config/registry_loader.py
index 880357c..4b906a1 100644
--- a/engine/config/registry_loader.py
+++ b/engine/config/registry_loader.py
@@ -7,10 +7,11 @@ import math
 import os
 import re
 import stat
+import sys as _sys
 from dataclasses import dataclass, field
 from datetime import datetime
 from pathlib import Path
-from types import MappingProxyType
+from types import CodeType, MappingProxyType, ModuleType
 from typing import Iterable, Mapping
 
 import jsonschema
@@ -18,9 +19,20 @@ from jsonschema import validators
 from referencing import Registry, Resource
 from referencing.exceptions import NoSuchResource
 
+from engine.categories import registry as category_registry
+from engine.categories.registry import FROZEN_MAGIC10_ORDER
 from engine.serializer import canon
 
-from engine.categories.registry import FROZEN_MAGIC10_ORDER
+
+# Retain actual execution provenance without reading or executing source bytes.
+# Unsupported provenance leaves candidate APIs usable; active admission refuses.
+try:
+    _MODULE_EXECUTION = (
+        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
+        _sys.flags.optimize, _sys.implementation.cache_tag,
+    )
+except Exception:
+    _MODULE_EXECUTION = None
 
 
 # PF12 — HDE Schemas & Artifacts, §2.1 owns the closed Gate domain 1..64,
@@ -405,6 +417,7 @@ ADMITTED_RELEASE_ROSTER = tuple(sorted({
     "engine/bodygraph/resolver.py",
     "engine/bodygraph/v2_adapter.py",
     "engine/cli/main.py",
+    "engine/categories/registry.py",
     "engine/compat/compute.py",
     "engine/compat/error_tokens.py",
     "engine/config/registry_loader.py",
@@ -421,15 +434,17 @@ ADMITTED_RELEASE_ROSTER = tuple(sorted({
     "migrations/005_identity.sql",
     "presenter/reader_v1/emitter.py",
     "schemas/channels_v1.schema.json",
+    "schemas/gates_v1.schema.json",
     "schemas/magic10_compat_result_v1.schema.json",
     "schemas/magic10_mechanics_v1.schema.json",
     "schemas/magic10_result_v1.schema.json",
     "schemas/reader.v1.schema.json",
     "tools/bodygraph/check_magic10_gate_readiness.py",
     "engine/serializer/canon.py",
+    "engine/stable/sercanon.py",
 }))
 
-if len(ADMITTED_RELEASE_ROSTER) != 41:  # pragma: no cover - import-time invariant
+if len(ADMITTED_RELEASE_ROSTER) != 44:  # pragma: no cover - import-time invariant
     raise RuntimeError("ADMITTED_RELEASE_ROSTER_INVALID")
 
 @dataclass(frozen=True)
@@ -624,8 +639,18 @@ class _LocalCapture:
         self.sources[relative_path] = source
         return source
 
-    def verify_unchanged(self) -> None:
+    def verify_unchanged(
+        self,
+        *,
+        identity_only: frozenset[str] = frozenset(),
+    ) -> None:
+        if not identity_only.issubset(self.sources):
+            raise SchemaValidationError(
+                'UNBOUND_SOURCE', 'identity-only verification requires a captured source'
+            )
         for name, source in self.sources.items():
+            if name in identity_only:
+                continue
             raw, identity = _read_captured_file(self.root, name)
             if identity != source.identity or raw != source.raw:
                 raise SchemaValidationError('SOURCE_CHANGED', f'captured source changed: {name}')
@@ -1236,10 +1261,102 @@ def _capture_admitted_members(
     return tuple(identities)
 
 
+def _admission_execution_provenance(
+) -> tuple[Path, tuple[tuple[str, CodeType, int], ...]]:
+    """Validate the four actual consumers' passive import provenance.
+
+    This proves neither historical imported bytes nor arbitrary in-process
+    tamper resistance. It establishes safe common origin and compilation
+    semantics for the bounded executable-equivalence comparison below.
+    """
+    owners = (
+        ('engine/config/registry_loader.py', 'engine.config.registry_loader', globals()),
+        ('engine/serializer/canon.py', 'engine.serializer.canon', canon),
+        ('engine/stable/sercanon.py', 'engine.stable.sercanon', getattr(canon, 'stable_sercanon', None)),
+        ('engine/categories/registry.py', 'engine.categories.registry', category_registry),
+    )
+    root: Path | None = None
+    executions: list[tuple[str, CodeType, int]] = []
+    for relative_path, expected_name, owner in owners:
+        if isinstance(owner, ModuleType):
+            namespace = vars(owner)
+        elif owner is globals():
+            namespace = owner
+        else:
+            raise SchemaValidationError('EXECUTION_PROVENANCE_UNAVAILABLE', 'covered admission module is unavailable')
+        provenance = namespace.get('_MODULE_EXECUTION')
+        if type(provenance) is not tuple or len(provenance) != 6:
+            raise SchemaValidationError('EXECUTION_PROVENANCE_UNAVAILABLE', 'module execution provenance is unavailable')
+        code, name, filename, origin, optimization, cache_tag = provenance
+        if not isinstance(code, CodeType) or code.co_name != '<module>':
+            raise SchemaValidationError('EXECUTION_PROVENANCE_UNAVAILABLE', 'top-level execution code is unavailable')
+        if (
+            type(optimization) is not int or optimization not in (0, 1, 2)
+            or optimization != _sys.flags.optimize
+            or not isinstance(cache_tag, str) or not cache_tag
+            or cache_tag != _sys.implementation.cache_tag
+        ):
+            raise SchemaValidationError('EXECUTION_SEMANTICS_MISMATCH', 'module compilation semantics are incompatible')
+        spec = namespace.get('__spec__')
+        if (
+            name != expected_name or namespace.get('__name__') != expected_name
+            or getattr(spec, 'name', None) != expected_name
+            or not isinstance(filename, str) or not isinstance(origin, str)
+            or filename != origin or namespace.get('__file__') != filename
+            or getattr(spec, 'origin', None) != origin
+            or code.co_filename != filename
+        ):
+            raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'module origin does not match retained execution provenance')
+        path = Path(filename)
+        relative = Path(relative_path)
+        if (
+            not path.is_absolute() or str(path) != filename
+            or '..' in path.parts or path.parts[-len(relative.parts):] != relative.parts
+        ):
+            raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'module origin is not the owning absolute source path')
+        module_root = path.parents[len(relative.parts) - 1]
+        if root is None:
+            root = module_root
+        elif module_root != root:
+            raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'covered admission modules have different roots')
+        _safe_source_path(module_root, relative_path)
+        executions.append((relative_path, code, optimization))
+    assert root is not None  # the fixed four-owner set is nonempty
+    return root, tuple(executions)
+
+
+def _validate_executing_admission_sources(
+    capture: _MechanicsCapture,
+    executions: tuple[tuple[str, CodeType, int], ...],
+) -> None:
+    """Compare actual executed code with compilation of manifest-owned bytes.
+
+    Compilation is passive: no captured source is executed or imported. Code
+    equality is deliberately separate from exact source and release identities.
+    """
+    for relative_path, executed, optimization in executions:
+        source = capture.sources.get(relative_path)
+        if source is None or relative_path not in ADMITTED_RELEASE_ROSTER:
+            raise SchemaValidationError('UNBOUND_SOURCE', 'executing module source is not captured and manifest-bound')
+        try:
+            compiled = compile(
+                source.raw, executed.co_filename, 'exec',
+                dont_inherit=True, optimize=optimization,
+            )
+        except Exception as exc:
+            raise SchemaValidationError('EXECUTION_COMPILATION_FAILED', 'captured admission source cannot be compiled') from exc
+        if compiled != executed:
+            raise SchemaValidationError(
+                'EXECUTING_SOURCE_MISMATCH',
+                f'executing code differs from captured source: {relative_path}',
+            )
+
+
 def _validate_admitted_schema_documents(capture: _MechanicsCapture) -> None:
     draft_2020 = 'https://json-schema.org/draft/2020-12/schema'
     for path in (
         'schemas/channels_v1.schema.json',
+        'schemas/gates_v1.schema.json',
         'schemas/magic10_mechanics_v1.schema.json',
         'schemas/magic10_result_v1.schema.json',
         'schemas/magic10_compat_result_v1.schema.json',
@@ -1316,17 +1433,20 @@ def _freeze_registry(registry: RegistryConfig, manifest: Manifest) -> RegistryCo
 
 
 def _load_active_mechanics_bundle_from_root(root: Path) -> AdmittedMechanicsBundle:
-    """Test seam for the fixed-root production admission algorithm."""
+    """Private fixture seam; public admission fixes the verified execution root.
+
+    Isolated fixtures may copy the identical implementation to a different
+    directory. They still undergo the complete executable-equivalence check.
+    """
+    _, executions = _admission_execution_provenance()
     capture = _MechanicsCapture(Path(root))
     manifest_source = capture.read('catalog/manifest.json')
     manifest = _parse_manifest(manifest_source.data)
     _validate_admitted_manifest(manifest)
     source_identities = _capture_admitted_members(capture, manifest)
+    _validate_executing_admission_sources(capture, executions)
 
-    # schemas/gates_v1.schema.json is intentionally outside the exact release
-    # roster.  The gate domain is therefore checked by the closed loader rules
-    # below, while every roster-authorized schema is executed from this capture.
-    gates, centers = _load_gates(capture, validate_schema=False)
+    gates, centers = _load_gates(capture)
     channels, aliases, domains = _load_channels(
         capture,
         gate_map=gates,
@@ -1352,7 +1472,9 @@ def _load_active_mechanics_bundle_from_root(root: Path) -> AdmittedMechanicsBund
     if not isinstance(frozen_mechanics, Mapping):  # guarded by mechanics schema
         raise SchemaValidationError('INVALID_MECHANICS', 'mechanics config must be an object')
     manifest_sha256 = manifest_source.sha256
-    capture.verify_unchanged()
+    capture.verify_unchanged(
+        identity_only=frozenset({'catalog/manifest.json'}),
+    )
     return AdmittedMechanicsBundle(
         registry=frozen_registry,
         mechanics=frozen_mechanics,
@@ -1366,12 +1488,9 @@ def _load_active_mechanics_bundle_from_root(root: Path) -> AdmittedMechanicsBund
 
 def load_active_mechanics_bundle() -> AdmittedMechanicsBundle:
     """Admit the exact installed complete mechanics release, or fail closed."""
-    module_path = Path(__file__)
-    if not module_path.is_absolute():
-        raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'owning module path must be absolute')
-    # Keep the lexical import path: resolving it would hide deployment aliases
-    # from _LocalCapture's symlink-ancestor refusal.
-    repository_root = module_path.parents[2]
+    # Derive the lexical root from retained actual execution provenance and
+    # corroborate all four live origins. Patching __file__ cannot select a root.
+    repository_root, _ = _admission_execution_provenance()
     return _load_active_mechanics_bundle_from_root(repository_root)
 
 
diff --git a/engine/serializer/canon.py b/engine/serializer/canon.py
index 05508f3..0cb0847 100644
--- a/engine/serializer/canon.py
+++ b/engine/serializer/canon.py
@@ -1,8 +1,20 @@
 from __future__ import annotations
 
+import sys as _sys
+
 from engine.stable import sercanon as stable_sercanon
 
 
+# Passive, immutable top-level execution provenance for active admission.
+try:
+    _MODULE_EXECUTION = (
+        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
+        _sys.flags.optimize, _sys.implementation.cache_tag,
+    )
+except Exception:
+    _MODULE_EXECUTION = None
+
+
 def sercanon(obj, *, sort_keys: bool = True) -> bytes:
     """
     Canonical JSON serializer for public envelopes.
diff --git a/engine/stable/sercanon.py b/engine/stable/sercanon.py
index d0375b5..7cfb57a 100644
--- a/engine/stable/sercanon.py
+++ b/engine/stable/sercanon.py
@@ -3,8 +3,18 @@
 from __future__ import annotations
 
 import json
+import sys as _sys
 from typing import Any
 
+# Passive, immutable top-level execution provenance for active admission.
+try:
+    _MODULE_EXECUTION = (
+        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
+        _sys.flags.optimize, _sys.implementation.cache_tag,
+    )
+except Exception:
+    _MODULE_EXECUTION = None
+
 _COMPACT_SEPS = (",", ":")
 
 
diff --git a/tests/artifacts/test_cli_text_artifacts_bom_lf.py b/tests/artifacts/test_cli_text_artifacts_bom_lf.py
index 42a0477..02ea1e4 100644
--- a/tests/artifacts/test_cli_text_artifacts_bom_lf.py
+++ b/tests/artifacts/test_cli_text_artifacts_bom_lf.py
@@ -22,4 +22,4 @@ def test_cli_text_artifacts_are_bom_free_and_single_lf():
 
     rc2, out_ba, err2 = _run(B, A)
     assert rc2 == 0 and err2 == b""
-    _assert_text_bytes_ok(out_ba)
\ No newline at end of file
+    _assert_text_bytes_ok(out_ba)
diff --git a/tests/config/helpers.py b/tests/config/helpers.py
index 9f78b7b..55cfb02 100644
--- a/tests/config/helpers.py
+++ b/tests/config/helpers.py
@@ -102,7 +102,7 @@ def synthetic_complete_release_root(
     *,
     source_root: Path | None = None,
 ) -> Path:
-    """Build a labeled, non-production 41-member admission fixture."""
+    """Build a labeled, non-production 44-member admission fixture."""
     from engine.config.registry_loader import (
         ADMITTED_RELEASE_BUILT_AT_UTC,
         ADMITTED_RELEASE_ROSTER,
diff --git a/tests/config/test_production_admission.py b/tests/config/test_production_admission.py
index 60b7609..6b450a8 100644
--- a/tests/config/test_production_admission.py
+++ b/tests/config/test_production_admission.py
@@ -58,6 +58,10 @@ def test_synthetic_complete_release_is_labeled_and_admits_exact_identities(relea
     assert isinstance(bundle, AdmittedMechanicsBundle)
     assert bundle.manifest.version == ADMITTED_RELEASE_VERSION
     assert bundle.manifest.built_at_utc == ADMITTED_RELEASE_BUILT_AT_UTC
+    assert len(ADMITTED_RELEASE_ROSTER) == 44
+    assert "schemas/gates_v1.schema.json" in ADMITTED_RELEASE_ROSTER
+    assert "engine/stable/sercanon.py" in ADMITTED_RELEASE_ROSTER
+    assert "engine/categories/registry.py" in ADMITTED_RELEASE_ROSTER
     assert tuple(row.path for row in bundle.manifest.files) == ADMITTED_RELEASE_ROSTER
     assert tuple(row.path for row in bundle.source_identities) == ADMITTED_RELEASE_ROSTER
     assert bundle.config_sha256 == hashlib.sha256(mechanics_raw).hexdigest()
@@ -116,26 +120,58 @@ def test_public_admission_never_resolves_relative_module_path_from_cwd(monkeypat
     assert caught.value.code == "UNSAFE_SOURCE_PATH"
 
 
+def test_public_admission_refuses_file_only_root_substitution(
+    release_root: Path, monkeypatch
+) -> None:
+    module_path = release_root / "engine/config/registry_loader.py"
+    module_path.write_bytes(module_path.read_bytes().rstrip(b"\n") + b"\n# changed after import\n")
+    write_synthetic_release_manifest(release_root)
+    monkeypatch.setattr(registry_loader, "__file__", str(module_path))
+
+    with pytest.raises(RegistryConfigError) as caught:
+        load_active_mechanics_bundle()
+    assert caught.value.code == "UNSAFE_SOURCE_PATH"
+
+
 def test_source_changed_after_its_verification_read_is_refused(release_root: Path, monkeypatch) -> None:
     original = registry_loader._read_captured_file
     reads = 0
+    target = "adapter/http_reader.py"
 
-    def replace_verified_manifest(root, relative_path):
+    def replace_verified_source(root, relative_path):
         nonlocal reads
         result = original(root, relative_path)
-        if relative_path == "catalog/manifest.json":
+        if relative_path == target:
             reads += 1
             if reads == 2:
                 # Initial capture was read 1. Change a source after read 2
                 # returned its old verified bytes, while other reads remain.
-                (root / relative_path).write_bytes(b"{}\n")
+                (root / relative_path).write_bytes(b'"""Changed after verification."""\n')
         return result
 
-    monkeypatch.setattr(registry_loader, "_read_captured_file", replace_verified_manifest)
+    monkeypatch.setattr(registry_loader, "_read_captured_file", replace_verified_source)
     _expect_code(release_root, "SOURCE_CHANGED")
     assert reads == 2
 
 
+def test_packaged_manifest_is_physically_read_once_per_admission(
+    release_root: Path, monkeypatch
+) -> None:
+    original = registry_loader._read_captured_file
+    reads = 0
+
+    def count_manifest_reads(root, relative_path):
+        nonlocal reads
+        if relative_path == "catalog/manifest.json":
+            reads += 1
+        return original(root, relative_path)
+
+    monkeypatch.setattr(registry_loader, "_read_captured_file", count_manifest_reads)
+    bundle = _load_active_mechanics_bundle_from_root(release_root)
+    assert isinstance(bundle, AdmittedMechanicsBundle)
+    assert reads == 1
+
+
 def test_source_removed_during_final_identity_check_has_typed_refusal(release_root: Path, monkeypatch) -> None:
     capture = _LocalCapture(release_root)
     capture.read("catalog/gates_v1.json")
@@ -256,6 +292,57 @@ def test_manifest_requires_exact_roster_version_and_timestamp(release_root: Path
     _expect_code(release_root, "RELEASE_TIMESTAMP_MISMATCH")
 
 
+def test_gate_schema_is_required_and_an_unlisted_43_member_release_is_incomplete(
+    release_root: Path,
+) -> None:
+    manifest = _manifest(release_root)
+    manifest["files"] = [
+        row for row in manifest["files"] if row["path"] != "schemas/gates_v1.schema.json"
+    ]
+    assert len(manifest["files"]) == 43
+    _write_manifest(release_root, manifest)
+    _expect_code(release_root, "INCOMPLETE_RELEASE_ROSTER")
+
+
+def test_missing_gate_schema_member_is_refused(release_root: Path) -> None:
+    (release_root / "schemas/gates_v1.schema.json").unlink()
+    _expect_code(release_root, "MISSING_FILE")
+
+
+@pytest.mark.parametrize(
+    ("raw", "code"),
+    [
+        (b'{"broken":\n', "INVALID_JSON"),
+        (b'{ "$id": "schemas/gates_v1.schema.json" }\n', "NONCANONICAL_JSON"),
+    ],
+)
+def test_gate_schema_member_bytes_must_be_valid_and_canonical(
+    release_root: Path, raw: bytes, code: str
+) -> None:
+    (release_root / "schemas/gates_v1.schema.json").write_bytes(raw)
+    write_synthetic_release_manifest(release_root)
+    _expect_code(release_root, code)
+
+
+def test_gate_schema_hash_and_size_are_manifest_bound(release_root: Path) -> None:
+    manifest = _manifest(release_root)
+    row = next(
+        item for item in manifest["files"] if item["path"] == "schemas/gates_v1.schema.json"
+    )
+    row["sha256"] = "0" * 64
+    _write_manifest(release_root, manifest)
+    _expect_code(release_root, "MANIFEST_MEMBER_HASH_MISMATCH")
+
+    write_synthetic_release_manifest(release_root)
+    manifest = _manifest(release_root)
+    row = next(
+        item for item in manifest["files"] if item["path"] == "schemas/gates_v1.schema.json"
+    )
+    row["size"] += 1
+    _write_manifest(release_root, manifest)
+    _expect_code(release_root, "MANIFEST_MEMBER_SIZE_MISMATCH")
+
+
 @pytest.mark.parametrize("unsafe", ["/absolute.json", "../escape.json", "a\\b.json", "a/./b.json", "a//b.json"])
 def test_manifest_member_paths_remain_canonical(release_root: Path, unsafe: str) -> None:
     manifest = _manifest(release_root)
@@ -339,6 +426,50 @@ def test_schema_identity_remote_reference_and_relation_fail_closed(release_root:
     _expect_code(release_root, "GATE_CENTER_COUNTS_MISMATCH")
 
 
+def test_manifest_bound_gate_schema_is_executed(release_root: Path) -> None:
+    schema_path = release_root / "schemas/gates_v1.schema.json"
+    write_canonical(
+        schema_path,
+        {
+            "$id": "schemas/gates_v1.schema.json",
+            "$schema": "https://json-schema.org/draft/2020-12/schema",
+            "not": {},
+        },
+    )
+    write_synthetic_release_manifest(release_root)
+    _expect_code(release_root, "SCHEMA_VALIDATION_FAILED")
+
+
+def test_gate_schema_remote_reference_and_source_change_fail_closed(
+    release_root: Path, monkeypatch
+) -> None:
+    schema_path = release_root / "schemas/gates_v1.schema.json"
+    schema = json.loads(schema_path.read_bytes())
+    schema["$ref"] = "https://example.invalid/gates.json"
+    write_canonical(schema_path, schema)
+    write_synthetic_release_manifest(release_root)
+    _expect_code(release_root, "NONLOCAL_SCHEMA_REFERENCE")
+
+    source_schema = Path(__file__).resolve().parents[2] / "schemas/gates_v1.schema.json"
+    schema_path.write_bytes(source_schema.read_bytes())
+    write_synthetic_release_manifest(release_root)
+    original = registry_loader._read_captured_file
+    reads = 0
+
+    def change_gate_schema_on_verify(root, relative_path):
+        nonlocal reads
+        result = original(root, relative_path)
+        if relative_path == "schemas/gates_v1.schema.json":
+            reads += 1
+            if reads == 2:
+                (root / relative_path).write_bytes(b"{}\n")
+        return result
+
+    monkeypatch.setattr(registry_loader, "_read_captured_file", change_gate_schema_on_verify)
+    _expect_code(release_root, "SOURCE_CHANGED")
+    assert reads == 2
+
+
 def test_mechanics_defaults_and_source_bindings_remain_closed(release_root: Path) -> None:
     path = release_root / "catalog/magic10_mechanics_v1.json"
     mechanics = json.loads(path.read_bytes())
@@ -491,8 +622,8 @@ def test_parser_and_registry_aliases_cannot_mutate_admitted_values(release_root:
     captures = []
     original = registry_loader._MechanicsCapture.verify_unchanged
 
-    def retain_capture(capture):
-        original(capture)
+    def retain_capture(capture, **kwargs):
+        original(capture, **kwargs)
         captures.append(capture)
 
     monkeypatch.setattr(registry_loader._MechanicsCapture, "verify_unchanged", retain_capture)
diff --git a/tests/evidence/test_rails_ci_workflow_integration.py b/tests/evidence/test_rails_ci_workflow_integration.py
index 1a74c71..67b86f7 100644
--- a/tests/evidence/test_rails_ci_workflow_integration.py
+++ b/tests/evidence/test_rails_ci_workflow_integration.py
@@ -456,6 +456,7 @@ def test_pr02_loader_gate_and_bundle_have_exact_behavioral_owners() -> None:
     assert classifier.changed_test_targets(ROOT, ("engine/config/registry_loader.py",)) == (
         "tests/config/test_alias_policy_enforcement.py",
         "tests/config/test_config_loader_unknown_ids_fail_closed.py",
+        "tests/config/test_execution_coherence.py",
         "tests/config/test_magic10_contracts.py",
         "tests/config/test_manifest_schema.py",
         "tests/config/test_production_admission.py",
@@ -467,6 +468,31 @@ def test_pr02_loader_gate_and_bundle_have_exact_behavioral_owners() -> None:
     )
 
 
+@pytest.mark.parametrize("source", [
+    "engine/serializer/canon.py",
+    "engine/stable/sercanon.py",
+    "engine/categories/registry.py",
+])
+def test_pr02_executing_module_changes_select_coherence_proof(source: str) -> None:
+    assert "tests/config/test_execution_coherence.py" in classifier.changed_test_targets(ROOT, (source,))
+
+
+@pytest.mark.parametrize("path", [
+    ".backup_epic004/changelog_20251024121758.tgz",
+    "_backup_1761350008.tgz",
+    "_backup_corrupted_1761349750.tgz",
+    "_backup_corrupted_1761349780.tgz",
+    "handoff/epic004_live_evidence_20251022T202304Z.tar.gz",
+])
+def test_retired_archive_paths_keep_evidence_validation(path: str) -> None:
+    assert classifier._lanes_for_path(path) == {"evidence"}
+
+
+def test_archive_retirement_does_not_open_a_new_unclassified_namespace() -> None:
+    assert classifier._lanes_for_path("handoff/new_runtime.py") is None
+    assert classifier._lanes_for_path(".backup_epic004/new_runtime.py") is None
+
+
 @pytest.mark.parametrize("source", [
     "tools/config/artifacts.py", "tools/config/generate_config_artifacts.py",
     "tools/config/generate_bundles.py",
@@ -536,6 +562,7 @@ def test_pr01_support_mapping_is_exact_and_new_modules_join_full_validation(tmp_
         "tests/config/test_manifest_schema.py", "tests/config/test_production_admission.py", "tests/config/test_registry_report.py",
         "tests/config/test_registry_report_determinism.py", "tests/config/test_registry_report_indexing.py",
         "tests/config/test_config_artifacts.py", "tests/config/test_typed_bundles.py",
+        "tests/config/test_execution_coherence.py",
     }
     for unknown in ("tests/config/unowned_helper.py", "tools/config/unowned_writer.py", "catalog/unowned.json"):
         p = tmp_path / unknown
@@ -548,6 +575,7 @@ def test_pr01_support_mapping_is_exact_and_new_modules_join_full_validation(tmp_
         "tests/config/test_registry_catalog_contract.py",
         "tests/config/test_magic10_contracts.py",
         "tests/config/test_production_admission.py",
+        "tests/config/test_execution_coherence.py",
     ):
         assert new_test in classifier._FULL_VALIDATION_SUPPLEMENTAL_TESTS
         assert new_test in classifier._full_validation_test_targets()
@@ -571,6 +599,7 @@ def test_pr02_changed_paths_keep_all_lanes_and_exact_new_test_targets() -> None:
         "tests/bodygraph/test_gates.py",
         "tests/config/test_alias_policy_enforcement.py",
         "tests/config/test_config_loader_unknown_ids_fail_closed.py",
+        "tests/config/test_execution_coherence.py",
         "tests/config/test_magic10_contracts.py",
         "tests/config/test_manifest_schema.py",
         "tests/config/test_production_admission.py",
@@ -906,7 +935,7 @@ def test_behavioral_owner_examples_cover_router_and_epic037_generator(
     ) == ("tests/ops/test_http_logging.py",)
     assert classifier.changed_test_targets(
         ROOT, ("engine/serializer/canon.py",)
-    ) == ()
+    ) == ("tests/config/test_execution_coherence.py",)
     assert classifier.changed_test_targets(
         ROOT, ("catalog/manifest.json",)
     ) == ()
diff --git a/tests/config/test_execution_coherence.py b/tests/config/test_execution_coherence.py
new file mode 100644
--- /dev/null
+++ b/tests/config/test_execution_coherence.py
@@ -0,0 +1,394 @@
+from __future__ import annotations
+
+import hashlib
+import json
+import os
+import py_compile
+import subprocess
+import sys
+from pathlib import Path
+
+import pytest
+
+from engine.categories import registry as category_registry
+from engine.config import registry_loader as loader
+from engine.serializer import canon
+from tests.config.helpers import (
+    closed_rails_env,
+    synthetic_complete_release_root,
+    write_canonical,
+    write_synthetic_release_manifest,
+)
+
+
+ROOT = Path(__file__).resolve().parents[2]
+COVERED = (
+    ("engine/config/registry_loader.py", loader),
+    ("engine/serializer/canon.py", canon),
+    ("engine/stable/sercanon.py", canon.stable_sercanon),
+    ("engine/categories/registry.py", category_registry),
+)
+HELPERS = ("engine/stable/sercanon.py", "engine/categories/registry.py")
+
+
+@pytest.fixture
+def release_root(tmp_path: Path) -> Path:
+    return synthetic_complete_release_root(tmp_path)
+
+
+def _refuses(root: Path, code: str) -> None:
+    with pytest.raises(loader.RegistryConfigError) as caught:
+        loader._load_active_mechanics_bundle_from_root(root)
+    assert caught.value.code == code
+
+
+def _importable(root: Path) -> None:
+    # Empty package scaffolding isolates the four real source modules from the
+    # installed checkout; it is not added to the synthetic release manifest.
+    for package in ("engine", "engine/config", "engine/serializer", "engine/stable", "engine/categories"):
+        (root / package / "__init__.py").write_bytes(b"")
+
+
+def _child(root: Path, script: str, *, optimization: int = 0) -> dict:
+    options = ["-I"] + (["-" + "O" * optimization] if optimization else [])
+    result = subprocess.run(
+        [sys.executable, *options, "-c", script, str(root)],
+        cwd=root, env=closed_rails_env(), text=True, capture_output=True,
+        check=False, timeout=30,
+    )
+    assert result.returncode == 0, result.stderr
+    assert result.stderr == ""
+    return json.loads(result.stdout)
+
+
+_IMPORT = """
+import hashlib, json, sys
+from pathlib import Path
+root = Path(sys.argv[1])
+sys.path.insert(0, str(root))
+from engine.config import registry_loader as loader
+from engine.serializer import canon
+from engine.categories import registry as category_registry
+owners = {
+    'engine/config/registry_loader.py': loader,
+    'engine/serializer/canon.py': canon,
+    'engine/stable/sercanon.py': canon.stable_sercanon,
+    'engine/categories/registry.py': category_registry,
+}
+def refresh_manifest():
+    path = root / 'catalog/manifest.json'
+    manifest = json.loads(path.read_bytes())
+    for row in manifest['files']:
+        raw = (root / row['path']).read_bytes()
+        row.update(sha256=hashlib.sha256(raw).hexdigest(), size=len(raw))
+    path.write_bytes(canon.sercanon(manifest))
+def admit():
+    try:
+        bundle = loader.load_active_mechanics_bundle()
+    except loader.RegistryConfigError as exc:
+        return {'state': 'refused', 'code': exc.code}
+    return {'state': 'admitted', 'members': len(bundle.source_identities),
+            'release_id': bundle.release_id,
+            'sources': {row.path: row.sha256 for row in bundle.source_identities}}
+"""
+
+
+@pytest.mark.parametrize("optimization", [0, 1, 2])
+def test_public_fresh_execution_admits_all_four_modules_under_matching_semantics(
+    release_root: Path, optimization: int,
+) -> None:
+    _importable(release_root)
+    result = _child(release_root, _IMPORT + "print(json.dumps(admit()))\n", optimization=optimization)
+    assert result["state"] == "admitted"
+    assert result["members"] == 44
+    assert result["release_id"] == hashlib.sha256((release_root / "catalog/manifest.json").read_bytes()).hexdigest()
+    for path, _ in COVERED:
+        assert result["sources"][path] == hashlib.sha256((release_root / path).read_bytes()).hexdigest()
+
+
+@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
+def test_each_materially_different_captured_module_refuses_without_execution(
+    release_root: Path, path: str, owner,
+) -> None:
+    source = release_root / path
+    source.write_bytes(source.read_bytes() + b"raise RuntimeError('captured source must never execute')\n")
+    write_synthetic_release_manifest(release_root)
+    _refuses(release_root, "EXECUTING_SOURCE_MISMATCH")
+
+
+@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
+def test_public_execution_refuses_source_replaced_after_import(
+    release_root: Path, path: str, owner,
+) -> None:
+    _importable(release_root)
+    script = _IMPORT + f"""
+path = root / {path!r}
+path.write_bytes(path.read_bytes() + b"raise RuntimeError('not executed')\\n")
+refresh_manifest()
+print(json.dumps(admit()))
+"""
+    assert _child(release_root, script) == {"state": "refused", "code": "EXECUTING_SOURCE_MISMATCH"}
+
+
+@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
+def test_timestamp_valid_stale_bytecode_refuses_but_fresh_b_admits(
+    release_root: Path, path: str, owner,
+) -> None:
+    _importable(release_root)
+    source = release_root / path
+    raw_a = source.read_bytes() + b"\ndef _f02_behavior():\n    return 'A'\n"
+    source.write_bytes(raw_a)
+    before = source.stat()
+    cached = Path(py_compile.compile(
+        str(source), doraise=True, invalidation_mode=py_compile.PycInvalidationMode.TIMESTAMP,
+    ))
+    raw_b = raw_a.replace(b"return 'A'", b"return 'B'")
+    assert raw_a != raw_b and len(raw_a) == len(raw_b)
+    source.write_bytes(raw_b)
+    os.utime(source, ns=(before.st_atime_ns, before.st_mtime_ns))
+    assert source.stat().st_mtime_ns == before.st_mtime_ns
+    write_synthetic_release_manifest(release_root)
+    script = _IMPORT + f"""
+result = admit()
+result['behavior'] = owners[{path!r}]._f02_behavior()
+print(json.dumps(result))
+"""
+    stale = _child(release_root, script)
+    assert stale == {"state": "refused", "code": "EXECUTING_SOURCE_MISMATCH", "behavior": "A"}
+    cached.unlink()
+    fresh = _child(release_root, script)
+    assert fresh["state"] == "admitted"
+    assert fresh["members"] == 44
+    assert fresh["behavior"] == "B"
+    assert fresh["sources"][path] == hashlib.sha256(raw_b).hexdigest()
+
+
+def test_code_equivalence_does_not_claim_historical_raw_source_identity(release_root: Path) -> None:
+    path = "engine/config/registry_loader.py"
+    source = release_root / path
+    old_digest = hashlib.sha256(source.read_bytes()).hexdigest()
+    source.write_bytes(source.read_bytes() + b"# Nonexecuting trailing source comment.\n")
+    write_synthetic_release_manifest(release_root)
+    bundle = loader._load_active_mechanics_bundle_from_root(release_root)
+    identity = next(row for row in bundle.source_identities if row.path == path)
+    assert identity.sha256 != old_digest
+    assert identity.sha256 == hashlib.sha256(source.read_bytes()).hexdigest()
+
+
+@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
+@pytest.mark.parametrize("defect", ["missing", "nonmodule_code", "optimization", "cache_tag", "origin"])
+def test_unusable_provenance_fails_closed_and_candidate_apis_remain_usable(
+    release_root: Path, monkeypatch, path: str, owner, defect: str,
+) -> None:
+    provenance = list(owner._MODULE_EXECUTION)
+    code = "EXECUTION_PROVENANCE_UNAVAILABLE"
+    if defect == "missing":
+        value = None
+    elif defect == "nonmodule_code":
+        provenance[0] = test_unusable_provenance_fails_closed_and_candidate_apis_remain_usable.__code__
+        value = tuple(provenance)
+    elif defect == "optimization":
+        provenance[4] = (sys.flags.optimize + 1) % 3
+        value = tuple(provenance)
+        code = "EXECUTION_SEMANTICS_MISMATCH"
+    elif defect == "cache_tag":
+        provenance[5] = "unsupported-interpreter-semantics"
+        value = tuple(provenance)
+        code = "EXECUTION_SEMANTICS_MISMATCH"
+    else:
+        provenance[3] = "relative/source.py"
+        value = tuple(provenance)
+        code = "UNSAFE_SOURCE_PATH"
+    monkeypatch.setattr(owner, "_MODULE_EXECUTION", value)
+    _refuses(release_root, code)
+    assert loader.load_registry_config(ROOT).magic10_order == category_registry.FROZEN_MAGIC10_ORDER
+
+
+@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
+def test_live_origin_must_agree_with_retained_actual_origin(
+    release_root: Path, monkeypatch, path: str, owner,
+) -> None:
+    monkeypatch.setattr(owner.__spec__, "origin", str(release_root / path))
+    _refuses(release_root, "UNSAFE_SOURCE_PATH")
+
+
+def test_unavailable_frame_capture_does_not_break_candidate_imports(release_root: Path) -> None:
+    _importable(release_root)
+    script = """
+import json, sys, jsonschema
+from pathlib import Path
+root = Path(sys.argv[1])
+sys.path.insert(0, str(root))
+original = sys._getframe
+covered = {
+    'engine.config.registry_loader', 'engine.serializer.canon',
+    'engine.stable.sercanon', 'engine.categories.registry',
+}
+def unavailable(depth=0):
+    frame = original(depth + 1)
+    if depth == 0 and frame.f_globals.get('__name__') in covered:
+        raise RuntimeError('frame provenance unavailable')
+    return frame
+sys._getframe = unavailable
+from engine.config import registry_loader as loader
+sys._getframe = original
+candidate = loader.load_registry_config(root)
+try:
+    loader.load_active_mechanics_bundle()
+except loader.RegistryConfigError as exc:
+    print(json.dumps({'candidate_gates': len(candidate.gates), 'code': exc.code}))
+"""
+    assert _child(release_root, script) == {"candidate_gates": 64, "code": "EXECUTION_PROVENANCE_UNAVAILABLE"}
+
+
+@pytest.mark.parametrize("retarget", [False, True])
+def test_real_public_import_through_deployment_symlink_refuses(
+    tmp_path: Path, release_root: Path, retarget: bool,
+) -> None:
+    _importable(release_root)
+    alias = tmp_path / "current"
+    alias.symlink_to(release_root, target_is_directory=True)
+    script = _IMPORT
+    if retarget:
+        parent = tmp_path / "replacement"
+        parent.mkdir()
+        replacement = synthetic_complete_release_root(parent)
+        _importable(replacement)
+        script += f"root.unlink(); root.symlink_to({str(replacement)!r}, target_is_directory=True)\n"
+    assert _child(alias, script + "print(json.dumps(admit()))\n") == {"state": "refused", "code": "UNSAFE_SOURCE_PATH"}
+
+
+@pytest.mark.parametrize("count", [42, 43, 45])
+def test_only_the_exact_44_member_roster_admits(release_root: Path, count: int) -> None:
+    path = release_root / "catalog/manifest.json"
+    manifest = json.loads(path.read_bytes())
+    if count < 44:
+        omitted = HELPERS[:44 - count]
+        manifest["files"] = [row for row in manifest["files"] if row["path"] not in omitted]
+        expected = "INCOMPLETE_RELEASE_ROSTER"
+    else:
+        manifest["files"].append({"path": "engine/unapproved.py", "sha256": "0" * 64, "size": 1})
+        manifest["files"].sort(key=lambda row: row["path"])
+        expected = "RELEASE_ROSTER_MISMATCH"
+    assert len(manifest["files"]) == count
+    write_canonical(path, manifest)
+    _refuses(release_root, expected)
+
+
+@pytest.mark.parametrize("path", HELPERS)
+@pytest.mark.parametrize("defect,expected", [
+    ("missing", "MISSING_FILE"),
+    ("malformed", "INVALID_PYTHON_MEMBER"),
+    ("noncanonical", "INVALID_MEMBER_FINAL_LF"),
+    ("hash", "MANIFEST_MEMBER_HASH_MISMATCH"),
+    ("size", "MANIFEST_MEMBER_SIZE_MISMATCH"),
+    ("symlink", "UNSAFE_SOURCE_PATH"),
+])
+def test_both_added_helper_sources_have_full_member_protection(
+    release_root: Path, path: str, defect: str, expected: str,
+) -> None:
+    source = release_root / path
+    if defect == "missing":
+        source.unlink()
+    elif defect == "malformed":
+        source.write_bytes(b"def broken(:\n")
+    elif defect == "noncanonical":
+        source.write_bytes(source.read_bytes() + b"\n")
+    elif defect in ("hash", "size"):
+        manifest_path = release_root / "catalog/manifest.json"
+        manifest = json.loads(manifest_path.read_bytes())
+        row = next(row for row in manifest["files"] if row["path"] == path)
+        if defect == "hash":
+            row["sha256"] = "0" * 64
+        else:
+            row["size"] += 1
+        write_canonical(manifest_path, manifest)
+    else:
+        target = source.with_suffix(".outside.py")
+        source.rename(target)
+        source.symlink_to(target)
+    _refuses(release_root, expected)
+
+
+@pytest.mark.parametrize("path", HELPERS)
+def test_added_helper_changed_after_capture_is_refused(release_root: Path, monkeypatch, path: str) -> None:
+    original = loader._read_captured_file
+    changed = False
+    def mutate_after_capture(root, relative):
+        nonlocal changed
+        result = original(root, relative)
+        if relative == path and not changed:
+            changed = True
+            (root / path).write_bytes(b"raise RuntimeError('changed after capture')\n")
+        return result
+    monkeypatch.setattr(loader, "_read_captured_file", mutate_after_capture)
+    _refuses(release_root, "SOURCE_CHANGED")
+
+
+@pytest.mark.parametrize("path", HELPERS)
+def test_execution_check_cannot_read_an_uncaptured_helper(release_root: Path, monkeypatch, path: str) -> None:
+    original = loader._validate_executing_admission_sources
+    def omit_captured_source(capture, executions):
+        capture.sources.pop(path)
+        return original(capture, executions)
+    monkeypatch.setattr(loader, "_validate_executing_admission_sources", omit_captured_source)
+    _refuses(release_root, "UNBOUND_SOURCE")
+
+
+def test_admission_exercises_the_existing_serializer_and_category_owners(release_root: Path, monkeypatch) -> None:
+    calls = 0
+    original = canon.stable_sercanon.serialize
+    def observe(value, *, sort_keys=True):
+        nonlocal calls
+        calls += 1
+        return original(value, sort_keys=sort_keys)
+    monkeypatch.setattr(canon.stable_sercanon, "serialize", observe)
+    bundle = loader._load_active_mechanics_bundle_from_root(release_root)
+    assert calls > 0
+    assert loader.FROZEN_MAGIC10_ORDER is category_registry.FROZEN_MAGIC10_ORDER
+    assert bundle.registry.magic10_order == category_registry.all_ids()
+
+
+@pytest.mark.parametrize("outcome", ["success", "malformed_manifest", "member_hash", "manifest_changed"])
+def test_packaged_manifest_has_one_physical_open_on_success_and_adverse_paths(
+    release_root: Path, monkeypatch, outcome: str,
+) -> None:
+    manifest_path = release_root / "catalog/manifest.json"
+    if outcome == "malformed_manifest":
+        manifest_path.write_bytes(b"{invalid\n")
+    elif outcome == "member_hash":
+        manifest = json.loads(manifest_path.read_bytes())
+        manifest["files"][0]["sha256"] = "0" * 64
+        write_canonical(manifest_path, manifest)
+    original_open = os.open
+    original_read = loader._read_captured_file
+    manifest_directory = manifest_path.parent.stat()
+    opens = 0
+    def observe_open(path, flags, *args, **kwargs):
+        nonlocal opens
+        directory = kwargs.get("dir_fd")
+        parent = os.fstat(directory) if directory is not None else None
+        if Path(path) == manifest_path or (
+            path == manifest_path.name and parent is not None
+            and (parent.st_dev, parent.st_ino)
+            == (manifest_directory.st_dev, manifest_directory.st_ino)
+        ):
+            opens += 1
+        return original_open(path, flags, *args, **kwargs)
+    def change_manifest_after_capture(root, relative):
+        result = original_read(root, relative)
+        if relative == "catalog/manifest.json":
+            manifest_path.write_bytes(b"{}\n")
+        return result
+    monkeypatch.setattr(os, "open", observe_open)
+    if outcome == "manifest_changed":
+        monkeypatch.setattr(loader, "_read_captured_file", change_manifest_after_capture)
+    if outcome == "success":
+        assert isinstance(loader._load_active_mechanics_bundle_from_root(release_root), loader.AdmittedMechanicsBundle)
+    else:
+        _refuses(release_root, {
+            "malformed_manifest": "INVALID_JSON",
+            "member_hash": "MANIFEST_MEMBER_HASH_MISMATCH",
+            "manifest_changed": "SOURCE_CHANGED",
+        }[outcome])
+    assert opens == 1
```

