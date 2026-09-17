# HDE-EPIC040-PR01 — PR-30 Engineering Verification Proof v1.0

Final audit-only verification proof for HDE-EPIC040-PR01 PR-30. This is not another approval object. The selected implementation Result v1.0 is MERGE_PENDING and all saved bytes, identity, state and next consumer have been verified. Embedded earlier observations retain their original timestamps and pending wording as history; the final evidence below records their completed outcomes.

## Actual local validation

The initial candidate tree 543ea921385410c6eda57404b8038b2d90f896e7 is native commit 924ae36a0bfe320f81fc9b6e4fd3891436096f27. The recorded combined affected-suite log is preserved below. Its 548 tests cover the allocated configuration contracts, root/writer/recovery, arrays, canonical gate, CI owners, updater and cutter modules. Supporting targeted runs overlap and are not added into a fabricated unique total. The exact local combined invocation and start/end timestamps were not retained in the working evidence; no reconstructed command or inferred timestamp is represented as observed. Its actual log SHA-256 is 709209273e21d75c2ecee93565f4274efb68e6b1845ecf21379dd4b9bd0186d4. Exact executed commands for the corrected owner run and actual native CI are preserved separately.

```text
........................................................................ [ 13%]
........................................................................ [ 26%]
........................................................................ [ 39%]
........................................................................ [ 52%]
........................................................................ [ 65%]
........................................................................ [ 78%]
........................................................................ [ 91%]
............................................                             [100%]
548 passed in 294.74s (0:04:54)
```

The token-reader correction tree 529306a74268f2a46765bf40defdae49026d103e is native commit 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950. Its exact affected test command and 149 passing tests are recorded in the full repair report below. No release source or generated artifact changed in that correction.

## Twelve read-only owner checks

Closed deterministic environment, repo virtualenv first on PATH, 2026-09-09T18:44:01.561589Z–18:44:04.275463Z. Every command exited 0.

| Command | Exit | Log SHA-256 |
| --- | --- | --- |
| `python tools/config/generate_config_artifacts.py --check` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `python tools/config/generate_bundles.py --check` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `python tools/evidence/generate_arrays_as_sets_report.py --check` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `python tools/evidence/run_canonical_json_gate.py --check-only` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `python tools/evidence/update_evidence_index.py --check` | 0 | 82ea36a3eb90ae8477d61e1c51eeb918e8c5139890885823dd52b6f4c3add06d |
| `python tools/evidence/orientation_demo.py --check` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `python tools/evidence/refresh_step_logs_manifest.py --check` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `python tools/evidence/validate_evidence_paths.py` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `ci/checks/check_evidence_index_hash.sh` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `ci/checks/check_mirror_schema.sh` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `ci/checks/check_final_lf.sh` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| `python scripts/release_id_recompute.py --check-manifest-only` | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

## Repeated output and unchanged source

First coordinated publication changed 31 output paths. The completed root had 5,862 files. The repeat, all owner checks and final combined tests each produced an empty bytes/mode/mtime delta. These are actual caught-operation observations, not crash atomicity or active production claims.

| Capture | SHA-256 | Delta |
| --- | --- | --- |
| publication-first-after.delta.json | 8d737b485f17e253e5bbddb7019c5a168530fd53e9e864a0ecebd4e832dacb55 | 31 paths |
| publication-repeat-after.delta.json | ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356 | 0 paths |
| owner-checks-after.delta.json | ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356 | 0 paths |
| candidate-after-tests.delta.json | ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356 | 0 paths |

## Complete bounded engineering evidence

The following reports preserve their actual producing helper and capture attribution. Root integrated the findings and alone owns native writes and the final result. They are not governed approvals or independent QA. Historical test failures inside an earlier report remain history and are read with the later corrections and 548-pass combined result.

### contract-review-findings.json

Original bytes: 4591; SHA-256 afd89b2d845c93a45fd48b8f8508037818e038aada873692be79a5e39f445a7b.

```json
{
  "actor": "bounded internal contract_review helper",
  "captured_at_utc": "2026-09-09T18:29:17.104235+00:00",
  "repository": "amthorn78/glow-hdengine-v2",
  "base_commit": "9065e6f0c01ad82a65c78687cd6c55e26ca33a1f",
  "reviewed_files": [
    {
      "path": "catalog/channels_v1.json",
      "size_bytes": 6481,
      "git_blob": "c5594c7cd196af592008ace4f3dda8c163ba084e",
      "sha256": "3a4ea9194121e48cc95848fd34a2903de413260b35bce9800b83f67a8bc3d3e9"
    },
    {
      "path": "schemas/channels_v1.schema.json",
      "size_bytes": 1396,
      "git_blob": "d68c9bdd7247f9054fccecd90b4d5c675239ff5b",
      "sha256": "33cd685e671b1ee44b93ce3b8ac5119a8d63ae18394f6b899e51f1e172107979"
    },
    {
      "path": "catalog/magic10_mechanics_v1.json",
      "size_bytes": 7279,
      "git_blob": "a3abe0cf473759aea31715106724a1eacc012b56",
      "sha256": "fff779980bdd6985dd0640d1b90ddc0e90046675a3b6cb7c17a08b9a70500eaf"
    },
    {
      "path": "schemas/magic10_mechanics_v1.schema.json",
      "size_bytes": 6061,
      "git_blob": "f7eb6fb8d86e4e88a90d3f0ce264bddca1c1363b",
      "sha256": "4d064366e9d3092127569aa4de328dd00938038ea7d2b790489fd6511f9cebe4"
    },
    {
      "path": "schemas/magic10_result_v1.schema.json",
      "size_bytes": 1631,
      "git_blob": "e3109864b44814eae04c34c3ec89f93323612c7d",
      "sha256": "67878786e7ec82ded8c1bad89103c4af57008582f1c6576aa7cd6ddb39825001"
    },
    {
      "path": "schemas/magic10_compat_result_v1.schema.json",
      "size_bytes": 1870,
      "git_blob": "aae6ec105a4f8619afd3efed2a5041e3a3ac6571",
      "sha256": "4c367bd1c819663344229ef03266c1c61f7d41053be953a04e5ea650bf2eb589"
    },
    {
      "path": "engine/config/registry_loader.py",
      "size_bytes": 50004,
      "git_blob": "df35e451c57ce97882d0b628c410cff975acf179",
      "sha256": "44919e56356a4d7597e04bf2cdaa73145ee2d66eead360b738f8cd7c0f22ed98"
    },
    {
      "path": "tests/config/helpers.py",
      "size_bytes": 1565,
      "git_blob": "6178e45aeef23350e674607dceda63ac146b46b2",
      "sha256": "b22a392ced2ba6765954f3f4e44f001f01873989eee2be3086b2eb5d619b468f"
    },
    {
      "path": "tests/config/test_registry_catalog_contract.py",
      "size_bytes": 16627,
      "git_blob": "52a76eb61a3d166c5b52f71abebce7e094a06a34",
      "sha256": "1a91e31b45830d12c35005b90dfef1994ab26ea670ff887095060a38f21f912b"
    },
    {
      "path": "tests/config/test_magic10_contracts.py",
      "size_bytes": 21024,
      "git_blob": "72a73c8160e4a1b34ce673d4037e6e3a223076f0",
      "sha256": "e4114c2271891ac3267c9245bbfeca047fe41d65b0627a44de6897039c71520c"
    }
  ],
  "source_comparison": {
    "taxonomy_rows": 36,
    "gate_center_facts": 64,
    "product_metadata_values": 108,
    "signals": 20,
    "memberships": 90,
    "profiles": 3,
    "responses": 15,
    "source_hashes": 4,
    "unchanged_source_and_consumer_documents": 8
  },
  "findings": [
    {
      "id": "R-CR01",
      "finding": "Unhashable result schema identity leaked TypeError",
      "root_fix": "Explicit string guard before fixed-set membership",
      "status": "FIX_REVIEWED"
    },
    {
      "id": "R-CR02",
      "finding": "Malformed consumer schema identity structure leaked AttributeError before typed schema check",
      "root_fix": "Explicit object guards for properties/schema identity extraction",
      "status": "FIX_REVIEWED"
    },
    {
      "id": "R-CR03",
      "finding": "Overdeep raw JSON leaked interpreter RecursionError instead of typed invalid JSON",
      "root_fix": "Convert RecursionError to INVALID_JSON without adding depth policy",
      "status": "FIX_REVIEWED"
    }
  ],
  "unresolved_findings": [],
  "limits": [
    "Internal bounded code/security review only, not a governed independent review or approval",
    "No tracked repository edits, publication, live product runtime, immutable admission or classifier/kernel proof performed by this helper; only bounded unit/adverse diagnostics and source comparisons.",
    "Current substantive file bytes identified individually; uncommitted source review does not assert a later PR head has been reviewed"
  ],
  "verification": {
    "completed_capture_utc": "2026-09-09T18:29:45.506556+00:00",
    "command": "LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m pytest -q -p no:cacheprovider -- tests/config/test_magic10_contracts.py tests/config/test_registry_catalog_contract.py",
    "exit_code": 0,
    "result": "171 passed in 18.06s",
    "reviewed_file_bytes_unchanged_through_test_completion": true
  }
}
```

### pr01-review-recovery-findings.json

Original bytes: 8956; SHA-256 d1998559326b81df5db83caa7e28001139ac07839d56ab37bbd603cd6fb91d9a.

```json
{
  "actor": "/root/finish_recovery; bounded internal helper under the responsible PR01 engineer",
  "authority": {
    "bounded_fixture_amendment": {
      "attribution": "Latest explicit PO instruction relayed by the responsible root engineer in this continuing session; no launch timestamp invented",
      "scope": "Correct the two baseline CRD test fixture assumptions. Supersedes the Plan preserve-tests clause only for this bounded repair; no waiver, removed test, CRD production change or retained evidence mutation.",
      "user_instruction_verbatim": "fix the crd ci issue too"
    },
    "original_operation": "Existing PO PR-30 Proceed for exact Plan v1.1 and Instruction v2.0"
  },
  "baseline": {
    "causal_checkout": "/workspace/scratch/545715ad0e8a/execution-preflight/recovery-baseline",
    "clean_after_causal_tests": true,
    "commit": "9065e6f0c01ad82a65c78687cd6c55e26ca33a1f",
    "transport": "Exact detached local Git worktree of the independently materialized native commit",
    "tree": "e07c4e4297c75fe83e0f286aa1cee46ffca6c62e"
  },
  "capture_utc": "2026-09-09T18:42:09.623261Z",
  "change_id": "HDE-EPIC040",
  "current_source_sha256": {
    "tests/evidence/test_evidence_index_missing_state.py": "c9c09e59452c358c123a22035e5b9b31e0b48972d7613621b25745a4657fbdb0",
    "tests/evidence/test_evidence_tool_ownership.py": "bd5f8cf7e6020a5e3e6ba45b33f6c4896cb1bdb0e6be4b0384aafd714de6766f",
    "tools/evidence/update_evidence_index.py": "538d18d3acac971a5bfa55e3581ff9b71553069b3dfdc7840f8c1d16a3fd0eb9",
    "tools/qa/qa_harness.py": "554066080cc4e9e06f261860fe3560ae0481ed0ce120212b18eaca798a69320c"
  },
  "execution_environment": {
    "pytest_options": "-q -p no:cacheprovider; distinct --basetemp outside repository; -k test_crd_ only for corrected group",
    "python": "/workspace/scratch/545715ad0e8a/glow-hdengine-v2/.venv/bin/python",
    "rails": {
      "ALLOW_NETWORK": "0",
      "APP_ENV": "dev",
      "LANG": "C",
      "LC_ALL": "C",
      "PYTHONDONTWRITEBYTECODE": "1",
      "SAFE_MODE": "1",
      "TZ": "UTC"
    }
  },
  "findings": [
    {
      "id": "PR01-RECOVERY-IDENTITY",
      "ownership_limit": "Original CRD transaction class and CRD adapter behavior unchanged; no immutable release admission or crash-atomic claim.",
      "problem": "Byte/mode/mtime equality did not identify an external same-byte inode replacement after an owner receipt. Rollback could attribute that replacement to the publisher.",
      "repair": "The config-only transaction state now binds dev/inode/ctime and verifies stable metadata around its read and preimage capture. Its receipt API remains the existing five-element dev/inode/mode/size/mtime tuple. Added an actual full config-family external-replacement proof that preserves the external inode and parent timestamp while restoring unrelated owned state.",
      "status": "REPAIRED_AND_TESTED"
    },
    {
      "baseline_failures": [
        "test_crd_governed_publication_binds_actual_records_and_is_repeatable",
        "test_crd_publication_refuses_incoherent_prior_state_before_writes[empty-root]"
      ],
      "id": "CRD-CI-FRESH-FIXTURE",
      "not_a_waiver": true,
      "problem": "Retained CRD QA evidence landed in baseline PR402, but the two existing tests assumed their copied CRD directory was absent. One failed the absence assertion; the other raised FileExistsError while constructing the empty-root adverse case.",
      "repair": "Only crd_repo fixture setup changes: remove the CRD family from the temporary copied root and its seed Index, then run the actual updater and its read-only check to construct a coherent pre-first-publication state. Original positive/adverse assertions, original production CRD adapter, and actual repository evidence remain intact.",
      "status": "REPAIRED_WITH_EXPLICIT_PO_AUTHORIZATION_AND_TESTED"
    },
    {
      "id": "RECOVERY-PRIOR-DIRECTORY-MTIME-OBSERVATION",
      "observation": "The inherited companion-True failure concerned directory mtimes after read-only checks. Isolated per-check snapshots showed zero changes, the exact focused case passed, and the full successor run did not repeat this failure. No causal explanation or production patch is claimed for that earlier observation.",
      "status": "NOT_REPRODUCED_IN_FOCUSED_AND_FULL_SUCCESSOR_TESTS"
    }
  ],
  "nonclaims": [
    "No governed review or approval",
    "No independent QA verdict",
    "No hosted CI result inferred from local pytest",
    "No PR publication or remote mutation by this helper",
    "No production activation, merge, Ops or Canon mutation",
    "No new governed artifact family"
  ],
  "pending": "Responsible root engineer will generate the actual coherent candidate after the separate writer callback repair stabilizes, then run combined required tests. No additional tests run for this evidence capture.",
  "record_kind": "BOUNDED_INTERNAL_ENGINEERING_REVIEW_AND_RECOVERY_EVIDENCE",
  "retained_crd_evidence": {
    "conclusion": "NO_DIFF; actual retained CRD evidence was not changed",
    "exit_code": 0,
    "path": "audit/qa/hde-crd-0001",
    "stdout": "",
    "verification_command": "git diff --name-only -- audit/qa/hde-crd-0001"
  },
  "selected_plan": {
    "library_file_id": "libfile_7960d01d117881919c0004545ae3a4d7",
    "sha256": "a77d453aa2a8b50b8e559cb8f6e5e2098f667760802366646f539a772769916e",
    "version": "1.1"
  },
  "validation": [
    {
      "log": {
        "bytes": 2884,
        "path": "/workspace/scratch/545715ad0e8a/execution-preflight/recovery-baseline-causal.log",
        "sha256": "c3a91a38013998f68c87f578d82364d27775296b8ca8efb3d7e48b575d67fb78"
      },
      "meaning": "Confirms both defects existed in the unchanged baseline, before fixture repair. Historical failure retained.",
      "result": "2 failed in 2.11s",
      "scope": "Exact original baseline causal tests"
    },
    {
      "log": {
        "bytes": 98,
        "path": "/workspace/scratch/545715ad0e8a/execution-preflight/recovery-targeted.log",
        "sha256": "9a78920f1b887894501c0e3832e3fb3db901ba1c9e81179dd8447c55cbbae8d5"
      },
      "result": "1 passed in 7.73s",
      "scope": "Original companion-True recovery reproduction"
    },
    {
      "log": {
        "bytes": 2892,
        "path": "/workspace/scratch/545715ad0e8a/execution-preflight/recovery-final.log",
        "sha256": "8abbcd366f40e79369f97a60175c053e5ecf046c5f82a71d5b9cc6d31783f906"
      },
      "meaning": "All then-current config publication/recovery/closure/concurrency/nonwriting and ownership cases passed. The two failures were the confirmed baseline CRD fixture cases, subsequently corrected. This run is not relabeled as all-pass.",
      "result": "70 passed, 2 failed in 252.00s",
      "scope": "Complete updater missing-state and evidence-tool ownership modules before PO fixture amendment",
      "source_manifest": {
        "bytes": 537,
        "path": "/workspace/scratch/545715ad0e8a/execution-preflight/recovery-final-source-sha256.txt",
        "sha256": "874d90298dc5b3614fd36a3812e94350cc91547a102ae21b5db0c014153a0906"
      }
    },
    {
      "log": {
        "bytes": 99,
        "path": "/workspace/scratch/545715ad0e8a/execution-preflight/recovery-final-success.log",
        "sha256": "d17bcf92691373d65b7e2b41ee1c67c760eb46286fe0f2251b42e2f71fb6617a"
      },
      "meaning": "Focused rerun covers the first success fixture whose earlier copy preceded the behavior-preserving helper relocation.",
      "result": "1 passed in 11.33s",
      "scope": "Current coordinator publication/repeatability after private receipt-helper relocation"
    },
    {
      "log": {
        "bytes": 99,
        "path": "/workspace/scratch/545715ad0e8a/execution-preflight/crd-repair-targeted.log",
        "sha256": "965d937afcf697eede3211c83e16d69a24f8752506baa52a174fdd3dda3ced26"
      },
      "result": "2 passed in 11.60s",
      "scope": "Two original CRD cases after fixture correction"
    },
    {
      "log": {
        "bytes": 125,
        "path": "/workspace/scratch/545715ad0e8a/execution-preflight/crd-repair-group.log",
        "sha256": "8d076db9d021110c0e7ee8f53813644ecc208249d1a4da232f830ebe6391a156"
      },
      "meaning": "All twenty original CRD cases passed. The twenty copied fixtures matched updater SHA538d18d3acac971a5bfa55e3581ff9b71553069b3dfdc7840f8c1d16a3fd0eb9, qa_harness SHA554066080cc4e9e06f261860fe3560ae0481ed0ce120212b18eaca798a69320c and corrected test SHA c9c09e59452c358c123a22035e5b9b31e0b48972d7613621b25745a4657fbdb0.",
      "result": "20 passed, 25 deselected in 89.49s",
      "scope": "Complete affected CRD group after correction",
      "source_manifest": {
        "bytes": 118,
        "path": "/workspace/scratch/545715ad0e8a/execution-preflight/crd-repair-source-sha256.txt",
        "sha256": "e4a24051c7591f76b86e6d8ad3780a3e5d0985d2f82b76c500d1f0afd7e1c595"
      }
    }
  ],
  "work_unit_id": "HDE-EPIC040-PR01"
}
```

### pr01-generated-review.json

Original bytes: 24432; SHA-256 d727fbd5962b951daa84797e24e1f183e3c5213b509a9890403f9d641ac91e05.

```json
{
  "kind": "bounded_read_only_generated_candidate_review",
  "captured_at_utc": "2026-09-09T18:49:49.476764+00:00",
  "actor": "internal contract_review helper",
  "base_commit": "9065e6f0c01ad82a65c78687cd6c55e26ca33a1f",
  "outcome": "NO_UNRESOLVED_FINDING_IN_REVIEWED_SCOPE",
  "generated_closure_count": 39,
  "changed_output_count": 31,
  "new_output_paths": [
    "artifacts/catalog/catalog_schema_validation.log",
    "artifacts/catalog/catalog_schema_validation.log.path_proof.txt",
    "artifacts/catalog/domain_closure_report.log",
    "artifacts/catalog/domain_closure_report.log.path_proof.txt"
  ],
  "changed_output_manifest": [
    {
      "path": "artifacts/canonical/arrays_as_sets_report.log",
      "size_bytes": 2010,
      "sha256": "92515fd8451bd2ebf4b0c0a5d731ee29c96f537451068621c2757b721614b5bf",
      "git_blob": "fa07a68b8d225ea40533b3ddf291ca6157bdb686"
    },
    {
      "path": "artifacts/canonical/arrays_as_sets_report.log.path_proof.txt",
      "size_bytes": 212,
      "sha256": "5e51482b46a3b39028f35a20c7ed327f0d32ac95bf764dafb572bdc69b7d5838",
      "git_blob": "a7d5cb58f4f0b5e2a0ae9c257ab9d88cc85affa8"
    },
    {
      "path": "artifacts/catalog/catalog_schema_validation.log",
      "size_bytes": 1537,
      "sha256": "6b96d1567de315409e076f0aff3aba6245a6278834a9234796f3faa0e0d5ff29",
      "git_blob": "a9cda4f70d626db4e2ab45428c639113523769d9"
    },
    {
      "path": "artifacts/catalog/catalog_schema_validation.log.path_proof.txt",
      "size_bytes": 214,
      "sha256": "199d2e15f3e24b00994c580f2be481937d3f2b066b26996d8209c2be58fe36e9",
      "git_blob": "f78939324577dafc8e7368f3d7a766034f8f6436"
    },
    {
      "path": "artifacts/catalog/domain_closure_report.log",
      "size_bytes": 1582,
      "sha256": "137ae49bc129ceabee100c72e535da71a4f40a822a1364e0caeb43d9f9c78660",
      "git_blob": "0dde4b8a0e8c406c517c292f87c081a8e4a61952"
    },
    {
      "path": "artifacts/catalog/domain_closure_report.log.path_proof.txt",
      "size_bytes": 210,
      "sha256": "5ec27fbaa1befebc01a749f32a618744d29fc0ae43211bb0e42bac3ddf8c2d50",
      "git_blob": "febd78f404097323a92d65822058e9d52badcf6b"
    },
    {
      "path": "artifacts/config_bundles/be_bundle.json",
      "size_bytes": 8822,
      "sha256": "b7524bde903a02a7d8ad70ba52ccdb9175210de06074c432379debf5fbbbdc4e",
      "git_blob": "d70e53809025e7b46fcdc6868986fac984ec752f"
    },
    {
      "path": "artifacts/config_bundles/be_bundle.json.path_proof.txt",
      "size_bytes": 206,
      "sha256": "c076016b4362aad31a0a0334d0727cc5b5b5a93ae0df7aea5d8b930867a7fbf3",
      "git_blob": "db7f046fdc55e52fee3b52a7b42136e60bb45cff"
    },
    {
      "path": "artifacts/config_bundles/fe_bundle.json",
      "size_bytes": 2201,
      "sha256": "ffce2dbb81f1cf7eedbe1a44f23d4bee4e8e05b051c087e7e676faac3f3a12a4",
      "git_blob": "4340f4ea8fde60bc6bef0e0e4f1fed7da9eb1b72"
    },
    {
      "path": "artifacts/config_bundles/fe_bundle.json.path_proof.txt",
      "size_bytes": 206,
      "sha256": "ffd35a7beabfa5fd0cf6df175c9bb367f1dc00b069954606c01079a095f7502f",
      "git_blob": "5093378bbc4851e904f58600d8eb7bad942c0565"
    },
    {
      "path": "artifacts/evidence_index.jsonl",
      "size_bytes": 289695,
      "sha256": "03255e812f78d37ae2988cf16dcaa7cee924b30b0588b88e7b91e6d2d22e2ce7",
      "git_blob": "c2fab4f2fbfb9189ec515b5185c6f57e6bfdccbd"
    },
    {
      "path": "artifacts/evidence_index.jsonl.path_proof.txt",
      "size_bytes": 284,
      "sha256": "1a86be072d4a14e4d81eedba07d7c1619362fc63c823331137ace62942d00289",
      "git_blob": "3baedd5e5e21940068d51b7d60f8d1777793ca18"
    },
    {
      "path": "artifacts/evidence_index.jsonl.sha256",
      "size_bytes": 97,
      "sha256": "078ceb52fda375f74ef3e7d47a739604324b159833ca1ed0855f067d4661fcf8",
      "git_blob": "28da589578630d62e0e682711460cf78cc3f4c64"
    },
    {
      "path": "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
      "size_bytes": 202,
      "sha256": "cc3bb9198984daf79244ea12101cf03eb404de1bb1d3a2cb0340367570df36f7",
      "git_blob": "d7ea87ab61bd3a8f13f9f0d59d22f40f33edceb5"
    },
    {
      "path": "artifacts/registry/registry_report.json",
      "size_bytes": 3832,
      "sha256": "270212323acf4af432e57af0c4611d706f4280e79fdb5d87a84c637a1197d940",
      "git_blob": "c677c8ca82459cdc2d9bec22fe7cd6488482f1f5"
    },
    {
      "path": "artifacts/registry/registry_report.json.path_proof.txt",
      "size_bytes": 206,
      "sha256": "18cb1c332308278805b3d4dc86777b78b460373e78885c8a1f606473c10445f9",
      "git_blob": "2ac16f5723c6595676c85479db76f5519313618e"
    },
    {
      "path": "audit/gates/canonical_json/json_canon_compare.log",
      "size_bytes": 12155,
      "sha256": "b4d36684ab5d086e139d65d768db6fddcb8d300825c79dc6287d7a5337a03749",
      "git_blob": "223a9c10555683a02dbb25cdac4f951fde3d491b"
    },
    {
      "path": "audit/gates/canonical_json/json_canon_compare.log.path_proof.txt",
      "size_bytes": 217,
      "sha256": "6a27cf14a00d1b22423c57dab9674e5f41bc64d8e7e6e18764e64c68327fea67",
      "git_blob": "f7faeb91b2ee0aac08a0d02789902c3c4349ae0e"
    },
    {
      "path": "audit/gates/canonical_json/json_canonical_check.log",
      "size_bytes": 12372,
      "sha256": "dbcd79eb5f144cf0a65b99501c6f878791747e469d2ae5272a53b3abf759edf1",
      "git_blob": "2e51c957c1460682237c646eabd83a06fdda4808"
    },
    {
      "path": "audit/gates/canonical_json/json_canonical_check.log.path_proof.txt",
      "size_bytes": 219,
      "sha256": "7b5cd8a1740503ea86498fe107bbf7f324e946042b596399f1d5e597a0f5773a",
      "git_blob": "51a24da1ec7bcf09f638f7ed1d29401a4ae11f56"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
      "size_bytes": 12372,
      "sha256": "dbcd79eb5f144cf0a65b99501c6f878791747e469d2ae5272a53b3abf759edf1",
      "git_blob": "2e51c957c1460682237c646eabd83a06fdda4808"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt",
      "size_bytes": 226,
      "sha256": "cf53d499576bfeb1889919b6ddc332d41d8de4bf5e1aac15099cb13cea099bde",
      "git_blob": "c9de8179d8b63081c3e59f85bce01c1ea8ccbd5c"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
      "size_bytes": 12155,
      "sha256": "b4d36684ab5d086e139d65d768db6fddcb8d300825c79dc6287d7a5337a03749",
      "git_blob": "223a9c10555683a02dbb25cdac4f951fde3d491b"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt",
      "size_bytes": 228,
      "sha256": "112fb22e56c934157d0ef6ca28f8845be2e822fed725f46b9d52180d199b0435",
      "git_blob": "d029a82c2b4582cd0be503dc99da8afacd7e6997"
    },
    {
      "path": "audit/gates/topology/orientation_demo.txt",
      "size_bytes": 115,
      "sha256": "147d62644f9251e675182f2130b1e2e5be0dff7018c39420d6b932fde50fb54a",
      "git_blob": "c2bfbad8d962b4507db9e250a4de3b14fa5818dc"
    },
    {
      "path": "audit/gates/topology/orientation_demo.txt.path_proof.txt",
      "size_bytes": 207,
      "sha256": "03aabacb55836aca525dfd837a6318b51a2eb0c5db8fa6cfa5e2e37104906166",
      "git_blob": "e43130c0a4ca284fc16771d53bdf34215a9ae81f"
    },
    {
      "path": "catalog/manifest.json",
      "size_bytes": 1981,
      "sha256": "c0f5f24fbbcbb04d01d1613be386c26fddbfb37d53cbb0f9c65d5cf55e97c2a4",
      "git_blob": "f551888892c2ff7448cb8c664611246379189aa6"
    },
    {
      "path": "docs/evidence/INDEX.json",
      "size_bytes": 160266,
      "sha256": "163fbc218ebb9c09621bac0a23ac52a5d8363618c0a56f5035efdc5f2687bdbc",
      "git_blob": "eeaefa037c5de7a5c1abfc3e9836afb9128510a3"
    },
    {
      "path": "docs/evidence/INDEX.json.path_proof.txt",
      "size_bytes": 193,
      "sha256": "15175766d49d05b50a433996437de8b2d0498e3a6de5af14c79903b536a74329",
      "git_blob": "8bd6c38e1b4b15c5d988f6ee640384ba7b35df80"
    },
    {
      "path": "docs/evidence/INDEX.sha256",
      "size_bytes": 91,
      "sha256": "af5c4d8b004d80ae66db54117e15407ce9e2e27b21da69b7bb07641c004f0e9e",
      "git_blob": "82bcc03e71b871ea3deb7a7548f837fe5acd9de5"
    },
    {
      "path": "docs/evidence/INDEX.sha256.path_proof.txt",
      "size_bytes": 191,
      "sha256": "3085237a5ccea00758e1457c9ace99370d3fa9cca54e5252d70e6c31314c5c43",
      "git_blob": "d34b360b12d80266ac3758e4f8678c7adaff35ca"
    }
  ],
  "all_required_closure_manifest": [
    {
      "path": "artifacts/canonical/arrays_as_sets_report.log",
      "size_bytes": 2010,
      "sha256": "92515fd8451bd2ebf4b0c0a5d731ee29c96f537451068621c2757b721614b5bf",
      "git_blob": "fa07a68b8d225ea40533b3ddf291ca6157bdb686"
    },
    {
      "path": "artifacts/canonical/arrays_as_sets_report.log.path_proof.txt",
      "size_bytes": 212,
      "sha256": "5e51482b46a3b39028f35a20c7ed327f0d32ac95bf764dafb572bdc69b7d5838",
      "git_blob": "a7d5cb58f4f0b5e2a0ae9c257ab9d88cc85affa8"
    },
    {
      "path": "artifacts/catalog/catalog_schema_validation.log",
      "size_bytes": 1537,
      "sha256": "6b96d1567de315409e076f0aff3aba6245a6278834a9234796f3faa0e0d5ff29",
      "git_blob": "a9cda4f70d626db4e2ab45428c639113523769d9"
    },
    {
      "path": "artifacts/catalog/catalog_schema_validation.log.path_proof.txt",
      "size_bytes": 214,
      "sha256": "199d2e15f3e24b00994c580f2be481937d3f2b066b26996d8209c2be58fe36e9",
      "git_blob": "f78939324577dafc8e7368f3d7a766034f8f6436"
    },
    {
      "path": "artifacts/catalog/domain_closure_report.log",
      "size_bytes": 1582,
      "sha256": "137ae49bc129ceabee100c72e535da71a4f40a822a1364e0caeb43d9f9c78660",
      "git_blob": "0dde4b8a0e8c406c517c292f87c081a8e4a61952"
    },
    {
      "path": "artifacts/catalog/domain_closure_report.log.path_proof.txt",
      "size_bytes": 210,
      "sha256": "5ec27fbaa1befebc01a749f32a618744d29fc0ae43211bb0e42bac3ddf8c2d50",
      "git_blob": "febd78f404097323a92d65822058e9d52badcf6b"
    },
    {
      "path": "artifacts/config_bundles/be_bundle.json",
      "size_bytes": 8822,
      "sha256": "b7524bde903a02a7d8ad70ba52ccdb9175210de06074c432379debf5fbbbdc4e",
      "git_blob": "d70e53809025e7b46fcdc6868986fac984ec752f"
    },
    {
      "path": "artifacts/config_bundles/be_bundle.json.path_proof.txt",
      "size_bytes": 206,
      "sha256": "c076016b4362aad31a0a0334d0727cc5b5b5a93ae0df7aea5d8b930867a7fbf3",
      "git_blob": "db7f046fdc55e52fee3b52a7b42136e60bb45cff"
    },
    {
      "path": "artifacts/config_bundles/fe_bundle.json",
      "size_bytes": 2201,
      "sha256": "ffce2dbb81f1cf7eedbe1a44f23d4bee4e8e05b051c087e7e676faac3f3a12a4",
      "git_blob": "4340f4ea8fde60bc6bef0e0e4f1fed7da9eb1b72"
    },
    {
      "path": "artifacts/config_bundles/fe_bundle.json.path_proof.txt",
      "size_bytes": 206,
      "sha256": "ffd35a7beabfa5fd0cf6df175c9bb367f1dc00b069954606c01079a095f7502f",
      "git_blob": "5093378bbc4851e904f58600d8eb7bad942c0565"
    },
    {
      "path": "artifacts/evidence_index.jsonl",
      "size_bytes": 289695,
      "sha256": "03255e812f78d37ae2988cf16dcaa7cee924b30b0588b88e7b91e6d2d22e2ce7",
      "git_blob": "c2fab4f2fbfb9189ec515b5185c6f57e6bfdccbd"
    },
    {
      "path": "artifacts/evidence_index.jsonl.path_proof.txt",
      "size_bytes": 284,
      "sha256": "1a86be072d4a14e4d81eedba07d7c1619362fc63c823331137ace62942d00289",
      "git_blob": "3baedd5e5e21940068d51b7d60f8d1777793ca18"
    },
    {
      "path": "artifacts/evidence_index.jsonl.sha256",
      "size_bytes": 97,
      "sha256": "078ceb52fda375f74ef3e7d47a739604324b159833ca1ed0855f067d4661fcf8",
      "git_blob": "28da589578630d62e0e682711460cf78cc3f4c64"
    },
    {
      "path": "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
      "size_bytes": 202,
      "sha256": "cc3bb9198984daf79244ea12101cf03eb404de1bb1d3a2cb0340367570df36f7",
      "git_blob": "d7ea87ab61bd3a8f13f9f0d59d22f40f33edceb5"
    },
    {
      "path": "artifacts/registry/registry_report.json",
      "size_bytes": 3832,
      "sha256": "270212323acf4af432e57af0c4611d706f4280e79fdb5d87a84c637a1197d940",
      "git_blob": "c677c8ca82459cdc2d9bec22fe7cd6488482f1f5"
    },
    {
      "path": "artifacts/registry/registry_report.json.path_proof.txt",
      "size_bytes": 206,
      "sha256": "18cb1c332308278805b3d4dc86777b78b460373e78885c8a1f606473c10445f9",
      "git_blob": "2ac16f5723c6595676c85479db76f5519313618e"
    },
    {
      "path": "artifacts/thresholds/band_edges.json",
      "size_bytes": 177,
      "sha256": "7e8931934b147e8a2069e3d2e5c5febada250fb889a1fd6d53405a6dd9986e49",
      "git_blob": "b1b9523c5ecd0c8a1cabb408b8483fc4f124dcdc"
    },
    {
      "path": "artifacts/thresholds/band_edges.json.path_proof.txt",
      "size_bytes": 202,
      "sha256": "ce4730b1bd7d7bf2344a31783f2f1a43cf1dd57ed67d92d872275f16175863dc",
      "git_blob": "73b75a74282c2c54ba46f39ff7cd90762bbfa915"
    },
    {
      "path": "artifacts/thresholds/magic10_config.json",
      "size_bytes": 1425,
      "sha256": "222af0fdfc8f87ee2fa2ee326c83bffa0ab9fa840eac7180d294883a7aeec71d",
      "git_blob": "44d1f579f172c9e3ebe7bcc1a5938a1d0ab47173"
    },
    {
      "path": "artifacts/thresholds/magic10_config.json.path_proof.txt",
      "size_bytes": 207,
      "sha256": "d1e5968bbdc60035a295ad276a9eb6155004e601264b51261c3e00669293aec8",
      "git_blob": "1722730baadab0e184154a68873174037f9aa46b"
    },
    {
      "path": "audit/gates/canonical_json/canonical_json.gate.json",
      "size_bytes": 4962,
      "sha256": "9e18dd68fcc90a550ad8f8edebde3f14af25e5237a624fe8bf18ed067fe814ec",
      "git_blob": "77c85b96a7822c6354e5e3ae3b0feb716eccce7b"
    },
    {
      "path": "audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt",
      "size_bytes": 218,
      "sha256": "d067bfa97f76e9d2d85c08b67e439546a116c00e5cae01ac8d60048c89961133",
      "git_blob": "1ba843ad43479a0501ee26247b3f459462a6ad96"
    },
    {
      "path": "audit/gates/canonical_json/json_canon_compare.log",
      "size_bytes": 12155,
      "sha256": "b4d36684ab5d086e139d65d768db6fddcb8d300825c79dc6287d7a5337a03749",
      "git_blob": "223a9c10555683a02dbb25cdac4f951fde3d491b"
    },
    {
      "path": "audit/gates/canonical_json/json_canon_compare.log.path_proof.txt",
      "size_bytes": 217,
      "sha256": "6a27cf14a00d1b22423c57dab9674e5f41bc64d8e7e6e18764e64c68327fea67",
      "git_blob": "f7faeb91b2ee0aac08a0d02789902c3c4349ae0e"
    },
    {
      "path": "audit/gates/canonical_json/json_canonical_check.log",
      "size_bytes": 12372,
      "sha256": "dbcd79eb5f144cf0a65b99501c6f878791747e469d2ae5272a53b3abf759edf1",
      "git_blob": "2e51c957c1460682237c646eabd83a06fdda4808"
    },
    {
      "path": "audit/gates/canonical_json/json_canonical_check.log.path_proof.txt",
      "size_bytes": 219,
      "sha256": "7b5cd8a1740503ea86498fe107bbf7f324e946042b596399f1d5e597a0f5773a",
      "git_blob": "51a24da1ec7bcf09f638f7ed1d29401a4ae11f56"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
      "size_bytes": 12372,
      "sha256": "dbcd79eb5f144cf0a65b99501c6f878791747e469d2ae5272a53b3abf759edf1",
      "git_blob": "2e51c957c1460682237c646eabd83a06fdda4808"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt",
      "size_bytes": 226,
      "sha256": "cf53d499576bfeb1889919b6ddc332d41d8de4bf5e1aac15099cb13cea099bde",
      "git_blob": "c9de8179d8b63081c3e59f85bce01c1ea8ccbd5c"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
      "size_bytes": 12155,
      "sha256": "b4d36684ab5d086e139d65d768db6fddcb8d300825c79dc6287d7a5337a03749",
      "git_blob": "223a9c10555683a02dbb25cdac4f951fde3d491b"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt",
      "size_bytes": 228,
      "sha256": "112fb22e56c934157d0ef6ca28f8845be2e822fed725f46b9d52180d199b0435",
      "git_blob": "d029a82c2b4582cd0be503dc99da8afacd7e6997"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_structured_record.json",
      "size_bytes": 4998,
      "sha256": "11dfa11308f8852d7927dd5bbf1686fd6c474f799887f792a3cd31849d85c0c7",
      "git_blob": "4b69f8c3aa887c86aa3859e08c03fae24b2af7bd"
    },
    {
      "path": "audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt",
      "size_bytes": 231,
      "sha256": "c54d8c42f9e495ec13165684c7d1dbec29302d06584815ed85a3ac5723b5baa2",
      "git_blob": "5fdebc402072387f769f3aad3f2f766917a22f83"
    },
    {
      "path": "audit/gates/topology/orientation_demo.txt",
      "size_bytes": 115,
      "sha256": "147d62644f9251e675182f2130b1e2e5be0dff7018c39420d6b932fde50fb54a",
      "git_blob": "c2bfbad8d962b4507db9e250a4de3b14fa5818dc"
    },
    {
      "path": "audit/gates/topology/orientation_demo.txt.path_proof.txt",
      "size_bytes": 207,
      "sha256": "03aabacb55836aca525dfd837a6318b51a2eb0c5db8fa6cfa5e2e37104906166",
      "git_blob": "e43130c0a4ca284fc16771d53bdf34215a9ae81f"
    },
    {
      "path": "catalog/manifest.json",
      "size_bytes": 1981,
      "sha256": "c0f5f24fbbcbb04d01d1613be386c26fddbfb37d53cbb0f9c65d5cf55e97c2a4",
      "git_blob": "f551888892c2ff7448cb8c664611246379189aa6"
    },
    {
      "path": "docs/evidence/INDEX.json",
      "size_bytes": 160266,
      "sha256": "163fbc218ebb9c09621bac0a23ac52a5d8363618c0a56f5035efdc5f2687bdbc",
      "git_blob": "eeaefa037c5de7a5c1abfc3e9836afb9128510a3"
    },
    {
      "path": "docs/evidence/INDEX.json.path_proof.txt",
      "size_bytes": 193,
      "sha256": "15175766d49d05b50a433996437de8b2d0498e3a6de5af14c79903b536a74329",
      "git_blob": "8bd6c38e1b4b15c5d988f6ee640384ba7b35df80"
    },
    {
      "path": "docs/evidence/INDEX.sha256",
      "size_bytes": 91,
      "sha256": "af5c4d8b004d80ae66db54117e15407ce9e2e27b21da69b7bb07641c004f0e9e",
      "git_blob": "82bcc03e71b871ea3deb7a7548f837fe5acd9de5"
    },
    {
      "path": "docs/evidence/INDEX.sha256.path_proof.txt",
      "size_bytes": 191,
      "sha256": "3085237a5ccea00758e1457c9ace99370d3fa9cca54e5252d70e6c31314c5c43",
      "git_blob": "d34b360b12d80266ac3758e4f8678c7adaff35ca"
    }
  ],
  "snapshot_files_compared": 5862,
  "snapshot_drift": [],
  "logical_deltas": {
    "docs/evidence/INDEX.json": {
      "before": 604,
      "after": 606,
      "added": [
        [
          "catalog.catalog_schema_validation",
          "artifacts/catalog/catalog_schema_validation.log"
        ],
        [
          "catalog.domain_closure_report",
          "artifacts/catalog/domain_closure_report.log"
        ]
      ],
      "changed": [],
      "removed": []
    },
    "artifacts/evidence_index.jsonl": {
      "before": 604,
      "after": 606,
      "added": [
        [
          "catalog.catalog_schema_validation",
          "artifacts/catalog/catalog_schema_validation.log"
        ],
        [
          "catalog.domain_closure_report",
          "artifacts/catalog/domain_closure_report.log"
        ]
      ],
      "changed": [
        {
          "identity": [
            "audit.gates.json_gate.canonical.json_gate_check_log.ndjson",
            "audit/gates/json_gate/canonical/json_gate_check_log.ndjson"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "audit.gates.json_gate.canonical.json_gate_compare_log.ndjson",
            "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "canonical_json.check_log",
            "audit/gates/canonical_json/json_canonical_check.log"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "canonical_json.compare_log",
            "audit/gates/canonical_json/json_canon_compare.log"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "config_bundle.be",
            "artifacts/config_bundles/be_bundle.json"
          ],
          "fields": [
            "sha256",
            "size_bytes"
          ]
        },
        {
          "identity": [
            "config_bundle.fe",
            "artifacts/config_bundles/fe_bundle.json"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "docs.evidence.INDEX.sha256",
            "docs/evidence/INDEX.sha256"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "epic039.pr01.arrays_as_sets_report",
            "artifacts/canonical/arrays_as_sets_report.log"
          ],
          "fields": [
            "sha256",
            "size_bytes"
          ]
        },
        {
          "identity": [
            "epic039.pr01.canonical_check",
            "audit/gates/json_gate/canonical/json_gate_check_log.ndjson"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "epic039.pr01.canonical_compare",
            "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "index.human_index",
            "docs/evidence/INDEX.json"
          ],
          "fields": [
            "sha256",
            "size_bytes"
          ]
        },
        {
          "identity": [
            "index.machine_mirror",
            "artifacts/evidence_index.jsonl"
          ],
          "fields": [
            "sha256",
            "size_bytes"
          ]
        },
        {
          "identity": [
            "registry.registry_report",
            "artifacts/registry/registry_report.json"
          ],
          "fields": [
            "sha256"
          ]
        },
        {
          "identity": [
            "topology.orientation_demo",
            "audit/gates/topology/orientation_demo.txt"
          ],
          "fields": [
            "produced_at_utc",
            "sha256"
          ]
        }
      ],
      "removed": []
    }
  },
  "manifest": {
    "member_count": 15,
    "roster_and_metadata_preserved": true,
    "changed_listed_member": [
      "catalog/channels_v1.json"
    ],
    "sha256": "c0f5f24fbbcbb04d01d1613be386c26fddbfb37d53cbb0f9c65d5cf55e97c2a4"
  },
  "consumer_schemas_preserved_and_validated": [
    {
      "path": "docs/schemas/config_bundle_be.json",
      "size_bytes": 4714,
      "sha256": "f1773e7ab36ab06336b26527a5e526561eb218629cb443fa4856f65d69414874",
      "git_blob": "e21687c7222572f6c7dcc07f08f9235e00547a6f"
    },
    {
      "path": "docs/schemas/config_bundle_fe.json",
      "size_bytes": 3369,
      "sha256": "287044da1517874462afad39936d8f3b51e986e42097b8161877343053259658",
      "git_blob": "a60e629e83553eca1191dde8ec089b762b4b1201"
    }
  ],
  "source_payload_parity": "registry/current catalogs; complete BE; trimmed FE; exact three primary source hashes and sizes; both catalog logs with all 11 actual captured source records",
  "canonical_gate": "all 26 owning target hash/size scopes match (25 complete files plus declared manifest root/files projection); 31 rows PASS in each paired log; six selector identities and both unchanged structured records retained; five endpoint rows inspected but not re-executed by reviewer",
  "crd_evidence_files_unchanged": 24,
  "timestamp_attribution": "Existing updater stable produced_default retained (2026-08-18T16:05:54Z on two new log proofs/mirror rows). Registry fixed-epoch and gate source timestamp remain owning deterministic metadata. Actual generation time is separately recorded by root publication capture; these metadata are not relabelled current run times.",
  "limitations": [
    "No tests, generators, repository mutations, remote writes, release activation, live vendor/DB or independent QA executed by reviewer",
    "The source snapshot and delta files were verified against actual current bytes and native baseline; no automatic approval or current PR head review verdict is supplied",
    "Publication order, rollback injections and runtime generation outcomes remain attributed to their actual executor, not re-performed here"
  ]
}
```

### token-roster-causality-review.json

Original bytes: 5269; SHA-256 282123fc0a88e0679cec2a5ae26d65efd2810a6ea5e919d874200cfee357f98f.

```json
{
  "kind": "bounded_internal_ci_causality_review",
  "captured_at_utc": "2026-09-09T19:02:18.711093+00:00",
  "candidate": "924ae36a0bfe320f81fc9b6e4fd3891436096f27",
  "baseline": "9065e6f0c01ad82a65c78687cd6c55e26ca33a1f",
  "ci_run": 34391523823,
  "ci_job": 102600719177,
  "test": "tests/qa/test_epic023_acceptance_alignment.py::test_epic023_acceptance_alignment_and_bindings",
  "finding": "Pre-existing Markdown escaped-underscore read bug. PF04 contains the legacy token at lines 852 and 865; raw token regex misses it. Export lacks this token. Identical failure occurs in isolated test processes on unchanged baseline and candidate. No preceding test mutation is necessary.",
  "scope": {
    "tests/qa/test_epic023_acceptance_alignment.py": {
      "candidate": {
        "git_blob": "d423943dab42e011a43f9c885dc9179c949aea6f",
        "sha256": "e2413b398cf162dc26c60c840007b4c54ef29569e15b446ae9d61005ee6ef3aa",
        "size": 9632
      },
      "baseline": {
        "git_blob": "d423943dab42e011a43f9c885dc9179c949aea6f",
        "sha256": "e2413b398cf162dc26c60c840007b4c54ef29569e15b446ae9d61005ee6ef3aa",
        "size": 9632
      }
    },
    "tools/qa/token_roster_validate.py": {
      "candidate": {
        "git_blob": "fe341add900a3a5b52e6d982663a96a7c25dc836",
        "sha256": "a6bd4ebe42945add6c1f22674877a3c9544bc123376a5817f1bf826223f37b76",
        "size": 2593
      },
      "baseline": {
        "git_blob": "fe341add900a3a5b52e6d982663a96a7c25dc836",
        "sha256": "a6bd4ebe42945add6c1f22674877a3c9544bc123376a5817f1bf826223f37b76",
        "size": 2593
      }
    },
    "docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.5.md": {
      "candidate": {
        "git_blob": "47767ec122e9d9d4b0c16b843e5069903cd10e5e",
        "sha256": "49def8b93c3f8fb658441361f3798a5f67419d6e50e58b6288b44874061f5408",
        "size": 522094
      },
      "baseline": {
        "git_blob": "47767ec122e9d9d4b0c16b843e5069903cd10e5e",
        "sha256": "49def8b93c3f8fb658441361f3798a5f67419d6e50e58b6288b44874061f5408",
        "size": 522094
      }
    },
    "reports/qa_acceptance_tokens.json": {
      "candidate": {
        "git_blob": "d35acae052b7da5998eb26b9c916a3d266872590",
        "sha256": "1d1630d811add116491d48d03d051770da8d711b37a1cf942b50aea603016265",
        "size": 35954
      },
      "baseline": {
        "git_blob": "d35acae052b7da5998eb26b9c916a3d266872590",
        "sha256": "1d1630d811add116491d48d03d051770da8d711b37a1cf942b50aea603016265",
        "size": 35954
      }
    },
    "audit/qa/hde-epic023/token_evidence_matrix.md": {
      "candidate": {
        "git_blob": "14eb7d06b55912d91362674b92c9ea17761fe6b4",
        "sha256": "11390a6d90b29fa71db3b1eba02339371f6c4b0b20ef07a2e32b74fd1aa44f88",
        "size": 3855
      },
      "baseline": {
        "git_blob": "14eb7d06b55912d91362674b92c9ea17761fe6b4",
        "sha256": "11390a6d90b29fa71db3b1eba02339371f6c4b0b20ef07a2e32b74fd1aa44f88",
        "size": 3855
      }
    },
    "docs/acceptance_map_epic023.json": {
      "candidate": {
        "git_blob": "090457199eb96771fef1a2118f503782998b9ed0",
        "sha256": "0e70390de1b1cecd7c4ee523032db5634b8ff0e061f45604590d30c3b1e6b2b1",
        "size": 3976
      },
      "baseline": {
        "git_blob": "090457199eb96771fef1a2118f503782998b9ed0",
        "sha256": "0e70390de1b1cecd7c4ee523032db5634b8ff0e061f45604590d30c3b1e6b2b1",
        "size": 3976
      }
    },
    "ci/checks/classify_ci_changes.py": {
      "candidate": {
        "git_blob": "bf759c9960eadaf3e751845eef3f93bbe1db5d61",
        "sha256": "0607d1ef7722c994de35863d1efdc9f2bfed27fdd077ea5cde84aad064626b29",
        "size": 58662
      },
      "baseline": {
        "git_blob": "64abae0c3a2ac820828d2f73de989614317ebd3a",
        "sha256": "eb624d952f21964947535e6027b9760e02edd26849cb5f861469f24c703d886c",
        "size": 55039
      }
    }
  },
  "results": [
    {
      "side": "candidate",
      "exit_code": 1,
      "summary": "same missing QA_ACCEPTANCE_MAP_VIABILITY_OK at line205",
      "log_path": "/workspace/scratch/545715ad0e8a/execution-preflight/token-roster-candidate-causality.log",
      "log_sha256": "b436f3da40e23ac0525cd7b6151a595fc761d20bc8189ee1d438cec5169d2ebe"
    },
    {
      "side": "baseline",
      "exit_code": 1,
      "summary": "same missing QA_ACCEPTANCE_MAP_VIABILITY_OK at line205",
      "log_path": "/workspace/scratch/545715ad0e8a/execution-preflight/token-roster-baseline-causality.log",
      "log_sha256": "095e4433743c22f6e84dde357b434ee6191803465d93dbf687d3073c90a3d63a"
    }
  ],
  "recommended_repair": "Normalize Markdown underscore escapes solely in existing extract_ok_tokens, retain token regex/sorted uniqueness, raw-source hashes, and missing/unknown refusal; add meaningful plain/escaped/mixed and unknown-token owner cases. Do not mutate Canon, registry or historic evidence.",
  "existing_owners": [
    "tests/qa/test_epic023_acceptance_alignment.py",
    "tests/qa/test_qa_tool_ownership.py"
  ],
  "lane": "qa",
  "limits": [
    "No product behavior, registry or Canon change performed.",
    "Root owns author integration and corrected-code review.",
    "This is internal source/test evidence, not QA acceptance, governed review or authority."
  ]
}
```

### token-roster-repair-report.json

Original bytes: 2179; SHA-256 ab2552a440787c951112610a139c3fdcd8c0b161b6ff985840ab6b47f9cb1a1a.

```json
{
  "kind": "bounded_reader_repair",
  "captured_at_utc": "2026-09-09T19:07:52.747497+00:00",
  "base_head": "924ae36a0bfe320f81fc9b6e4fd3891436096f27",
  "files": {
    "tools/qa/token_roster_validate.py": {
      "size": 2765,
      "sha256": "4f1126b276701c775b75fc888e9d8a96013252572997b0474213f20a3d719d65",
      "git_blob": "fe21ac527c6eba809aa3a41d8484754892c563ce"
    },
    "tests/qa/test_qa_tool_ownership.py": {
      "size": 21101,
      "sha256": "6a5f47144828b881002a6df6d4e1cdf10654b9af83eead830f13897250b93d49",
      "git_blob": "21d2170d3cb7b6d4fabb9f0b51472974600fc2f9"
    }
  },
  "behavior": "Normalize only literal Markdown underscore escapes before existing regex matching; retain raw source hashing and unknown-token refusal.",
  "proofs": [
    "plain/fully escaped/mixed spellings produce sorted unique original names",
    "Unicode/hex/newline escape spellings are not decoded",
    "CLI escaped unknown token returns10 with exact missing name",
    "CLI hashes preserve original raw source bytes and inputs remain unchanged",
    "Original historical EPIC023 alignment and binding check now passes"
  ],
  "test_command": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONDONTWRITEBYTECODE=1 /workspace/scratch/545715ad0e8a/execution-preflight/python-env/bin/python -m pytest -q -p no:cacheprovider --basetemp=/workspace/scratch/545715ad0e8a/execution-preflight/token-roster-repair-tmp tests/qa/test_epic023_acceptance_alignment.py tests/qa/test_qa_tool_ownership.py",
  "exit_code": 0,
  "summary": "149 passed in 0.30s",
  "test_log": "/workspace/scratch/545715ad0e8a/execution-preflight/token-roster-repair-owners.log",
  "test_log_sha256": "1b5eb7a176e8967ea2ddd587e91daf02039c387e8258bc4f4640e078b4dc8dcc",
  "diff": "/workspace/scratch/545715ad0e8a/execution-preflight/token-roster-repair.diff",
  "diff_sha256": "3ecdfd2cd894d86291dbe8f75ed190d5e9a3598b8ae9038b52862f7bd3c74974",
  "git_diff_check_exit_code": 0,
  "nonclaims": [
    "No registry, PF04, generated evidence, classifier, commit or publication mutation",
    "Internal implementation and tests only; root integrates and obtains corrected-code review"
  ]
}
```

### pr01-ci-command-map.json

Original bytes: 14572; SHA-256 a2f7dbbf35da19a00a9dab3183a9a95ba4819b296d1413d2d2f080e7164a7bb9.

```json
{
  "kind": "read_only_CI_command_preparation",
  "captured_at_utc": "2026-09-09T18:39:46.429416+00:00",
  "workflow": "ci",
  "job_check": "test",
  "lanes": [
    "product",
    "compat",
    "db",
    "rails",
    "evidence",
    "qa",
    "release"
  ],
  "source_records": [
    {
      "path": ".github/workflows/ci.yml",
      "sha256": "e1b63db426b4a62dedf16dd66fb46baf209384abda35135ee0693fd32db602d1",
      "git_blob": "a35e8670229c7b7b1a6549ba70b15322dc39e4ab"
    },
    {
      "path": "ci/checks/classify_ci_changes.py",
      "sha256": "0607d1ef7722c994de35863d1efdc9f2bfed27fdd077ea5cde84aad064626b29",
      "git_blob": "bf759c9960eadaf3e751845eef3f93bbe1db5d61"
    },
    {
      "path": "ci/checks/run_rails_job_definitions.py",
      "sha256": "835533f5b30a88557b0cd13b0ce02a498de19491a24814b1cbe2bf5ff0648d81",
      "git_blob": "f641d75d43ebcb1107fc05414ec55e4b47ca907c"
    },
    {
      "path": "ci/jobs/rails_closed_refusal.yml",
      "sha256": "323ea23c53973422f835ba1f83ea474e0f45fdabffb55d4b49786d6019d33c8b",
      "git_blob": "c159b502ee5b71655538c50f7af211e0564f871e"
    },
    {
      "path": "ci/jobs/rails_open_conformance.yml",
      "sha256": "d04763c03a128ba5031662ff60ebd35e3aaf04d9ecd50053d09f85ec0753fbeb",
      "git_blob": "c42301f90d425fae6f630ebbafea4b184d5fd67f"
    },
    {
      "path": "ci/jobs/logs_keys_only_redaction.yml",
      "sha256": "740d571a5e5ea23072f8c2392546ea856f3d4fc18651c32360fd09f7a94417bf",
      "git_blob": "015ea26b4f1520629b3c9e51643b07c276a4cf29"
    },
    {
      "path": "tools/evidence/build_release_attestation.py",
      "sha256": "b009c5ed934a29123c7d317b2ab1035b9c8fbbe7288bc2788a3f955b47a06fdb",
      "git_blob": "b98794da17e3a8a7284f292015883229093f3d30"
    },
    {
      "path": "tools/evidence/run_sanity_pipeline.py",
      "sha256": "43e5a454174e0cafcafc18edec56d864ac5fa1b8fb0b52de295f9c8623fe622f",
      "git_blob": "ab0f1cacc172ae7f6a5784e4466d3ec797b3c575"
    }
  ],
  "exact_workflow_steps": [
    {
      "id": "changed_tests",
      "name": "Run affected behavioral tests in isolation",
      "exact_workflow_run": "set -euo pipefail\nchanged_test_source=\"$RUNNER_TEMP/hde-changed-test-source\"\nchanged_test_manifest=\"$RUNNER_TEMP/ci-changed-test-targets.txt\"\ncleanup() {\n  git worktree remove --force \"$changed_test_source\" >/dev/null 2>&1 || true\n}\ntrap cleanup EXIT\ntest -f \"$changed_test_manifest\"\nmapfile -t changed_test_targets < \"$changed_test_manifest\"\n(( ${#changed_test_targets[@]} > 0 ))\ngit worktree add --detach \"$changed_test_source\" \"$(git rev-parse HEAD)\"\n(\n  cd \"$changed_test_source\"\n  unset GH_TOKEN\n  export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1\n  export PYTHONPATH=\"$changed_test_source\"\n  python -m pytest -q -p no:cacheprovider -- \"${changed_test_targets[@]}\"\n  git diff --exit-code\n  test -z \"$(git status --short --untracked-files=all)\"\n)\ncleanup\ntrap - EXIT\n"
    },
    {
      "id": "product_lane",
      "name": "Run product mechanics and ordering lane",
      "exact_workflow_run": "set -euo pipefail\npython tools/order/generate_ordering_artifacts.py --check\npython -m pytest -q \\\n  tests/order \\\n  tests/mech/test_order_properties.py \\\n  tests/evidence/test_architecture_snapshot.py\n"
    },
    {
      "id": "compat_lane",
      "name": "Run CLI and compatibility lane",
      "exact_workflow_run": "set -euo pipefail\nci/checks/check_cli_help.sh\npython tools/cli/serializer_grep_guard.py --output \"$RUNNER_TEMP/serializer_grep_guard.log\"\npython tools/cli/emitter_symbol_proof.py --output \"$RUNNER_TEMP/emitter_symbol_proof.txt\"\npython -m pytest -q \\\n  tests/adapter/test_jsonschema.py \\\n  tests/cli/test_cli_usage_and_errors.py \\\n  tests/cli/test_errors_parity.py \\\n  tests/cli/test_cli_canonical_bytes.py \\\n  tests/cli/test_showcompat_parity_and_identity.py \\\n  tests/cli/test_serializer_guards.py \\\n  tests/transport/test_internal_version_contract.py \\\n  tests/http/test_compat_endpoint_contract.py \\\n  tests/adapter/test_compat_http_dev.py \\\n  tests/adapter/test_compat_http_parity.py\n"
    },
    {
      "id": "db_lane",
      "name": "Run database and runtime-contract lane",
      "exact_workflow_run": "set -euo pipefail\npython ci/checks/check_direct_db_contract.py\npython -m pytest -q \\\n  tests/db \\\n  tests/unit/test_check_direct_db_contract.py \\\n  tests/bodygraph/test_bg_resolve_v2_mapped_cache.py \\\n  tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py \\\n  tests/bodygraph/test_ingest.py \\\n  tests/ops/test_capture_rails_open_scope.py \\\n  tests/ops/test_http_logging.py\n"
    },
    {
      "id": "rails_lane",
      "name": "Run rails policy and secret-safety lane",
      "exact_workflow_run": "set -euo pipefail\npython ci/checks/run_rails_job_definitions.py \\\n  ci/jobs/rails_closed_refusal.yml \\\n  ci/jobs/rails_open_conformance.yml \\\n  ci/jobs/logs_keys_only_redaction.yml\npython -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py\n"
    },
    {
      "id": "evidence_lane",
      "name": "Run governed evidence integrity lane",
      "exact_workflow_run": "set -euo pipefail\npython tools/evidence/update_evidence_index.py --check\npython tools/evidence/orientation_demo.py --check\npython tools/evidence/refresh_step_logs_manifest.py --check\nci/checks/check_evidence_index_hash.sh\npython tools/evidence/validate_evidence_paths.py\nci/checks/check_mirror_schema.sh\nci/checks/check_final_lf.sh\npython -m pytest -q \\\n  tests/evidence/test_evidence_index_missing_state.py \\\n  tests/evidence/test_evidence_skeleton.py \\\n  tests/evidence/test_machine_mirror_self_proof.py \\\n  tests/evidence/test_orientation_demo.py \\\n  tests/ops/test_evidence_index.py \\\n  tests/qa/test_epic020_qa_docs.py\n"
    },
    {
      "id": "qa_lane",
      "name": "Run approved generic QA subsystem lane in isolation",
      "exact_workflow_run": "set -euo pipefail\nqa_source=\"$RUNNER_TEMP/hde-generic-qa-tests\"\ncleanup() {\n  git worktree remove --force \"$qa_source\" >/dev/null 2>&1 || true\n}\ntrap cleanup EXIT\ngit worktree add --detach \"$qa_source\" \"$(git rev-parse HEAD)\"\n(\n  cd \"$qa_source\"\n  unset GH_TOKEN\n  export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1\n  export PYTHONPATH=\"$qa_source\"\n  python -m pytest -q \\\n    tests/qa/test_generic_qa_harness.py \\\n    tests/qa/test_qa_harness_followup.py \\\n    tests/qa/test_epic021_harness_entrypoint.py \\\n    tests/qa/test_epic021_acceptance_alignment.py \\\n    tests/qa/test_tooling_bootstrap.py \\\n    tests/qa/test_viability_generator_wrappers.py \\\n    tests/qa/test_epic029_requalification.py\n  git diff --exit-code\n  test -z \"$(git status --short --untracked-files=all)\"\n)\ncleanup\ntrap - EXIT\n"
    },
    {
      "id": "release_lane",
      "name": "Build and verify exact-source release attestation",
      "exact_workflow_run": "set -euo pipefail\nattestation_root=\"$RUNNER_TEMP/hde-release-attestation\"\nrelease_test_source=\"$RUNNER_TEMP/hde-release-regression-tests\"\ncleanup() {\n  git worktree remove --force \"$release_test_source\" >/dev/null 2>&1 || true\n}\ntrap cleanup EXIT\ntest ! -e \"$attestation_root\"\ntest ! -e \"$release_test_source\"\ngit diff --exit-code\npython scripts/release_id_recompute.py --check-manifest-only\ngit worktree add --detach \"$release_test_source\" \"$(git rev-parse HEAD)\"\n(\n  cd \"$release_test_source\"\n  export PYTHONPATH=\"$release_test_source\"\n  python -m pytest -q \\\n    tests/runtime/test_identity.py \\\n    tests/evidence/test_release_attestation.py \\\n    tests/evidence/test_release_manifest_content_binding.py \\\n    tests/evidence/test_sanity_pipeline.py\n  git diff --exit-code\n  test -z \"$(git status --short --untracked-files=all)\"\n)\ncleanup\ntrap - EXIT\ntest -z \"$(git status --short --untracked-files=all)\"\npython tools/evidence/build_release_attestation.py \\\n  --output \"$attestation_root\" \\\n  --require-clean\npython tools/evidence/build_release_attestation.py \\\n  --verify \"$attestation_root\" \\\n  --require-clean\n# No active release or deployment workflow consumes this bundle.\n# Keep it ephemeral instead of adding an unconsumed artifact transfer.\ngit diff --exit-code\ntest -z \"$(git status --short --untracked-files=all)\"\n"
    }
  ],
  "full_validation_changed_test_targets": [
    "tests/adapter/test_dev_sampler_http.py",
    "tests/adapter/test_diagnostic_writer.py",
    "tests/artifacts/test_env_guard_artifact_bytes.py",
    "tests/bodygraph/test_vendor_client.py",
    "tests/categories/test_registry_and_purity.py",
    "tests/cli/test_aux_preview.py",
    "tests/cli/test_bg_resolve.py",
    "tests/cli/test_cli_file_inputs.py",
    "tests/cli/test_cli_install_help.py",
    "tests/cli/test_dev_sampler_cli.py",
    "tests/cli/test_showcompat_sources.py",
    "tests/compare/test_arrays_as_sets.py",
    "tests/compat/test_abba_parity.py",
    "tests/compliance/test_logging_filter_keys_only_and_redactions.py",
    "tests/config/test_alias_policy_enforcement.py",
    "tests/config/test_config_artifacts.py",
    "tests/config/test_config_loader_unknown_ids_fail_closed.py",
    "tests/config/test_magic10_contracts.py",
    "tests/config/test_manifest_schema.py",
    "tests/config/test_registry_catalog_contract.py",
    "tests/config/test_registry_report.py",
    "tests/config/test_registry_report_determinism.py",
    "tests/config/test_registry_report_indexing.py",
    "tests/config/test_typed_bundles.py",
    "tests/evidence/test_canonical_json_gate_check_outputs.py",
    "tests/evidence/test_d23_evidence_index_snapshot_contract.py",
    "tests/evidence/test_epic024_acceptance_map_viability.py",
    "tests/evidence/test_epic024_evidence_path_binding_validation.py",
    "tests/evidence/test_evidence_tool_ownership.py",
    "tests/evidence/test_hde_epic037_v2_adapter.py",
    "tests/evidence/test_hde_epic038_direct_db_selection.py",
    "tests/evidence/test_http_reader_ci_ownership.py",
    "tests/evidence/test_po_006_token_registry_validity.py",
    "tests/evidence/test_refresh_epic024_step_logs_manifest.py",
    "tests/evidence/test_retained_evidence_safety.py",
    "tests/http/test_dev_conjunction_http.py",
    "tests/http/test_endpoint_catalog.py",
    "tests/http/test_reader_a7_transport.py",
    "tests/invariance/test_bytes_identity.py",
    "tests/invariance/test_determinism_env_helper.py",
    "tests/invariance/test_locale_tz.py",
    "tests/m10/test_defs_order.py",
    "tests/m10/test_m10_symmetry_identity.py",
    "tests/m10/test_thresholds_rounding.py",
    "tests/mech/test_arrays_as_sets.py",
    "tests/mech/test_constants.py",
    "tests/ops/test_hde_epic038_ops03.py",
    "tests/qa/test_cli_admin_dumps.py",
    "tests/qa/test_cli_admin_parity.py",
    "tests/qa/test_epic023_acceptance_alignment.py",
    "tests/qa/test_epic024_bootstrap_status.py",
    "tests/qa/test_generate_epic_close_pack.py",
    "tests/qa/test_qa_tool_ownership.py",
    "tests/scripts/test_cut_release_manifest.py",
    "tests/scripts/test_release_id_recompute.py",
    "tests/support/test_change_gates.py",
    "tests/tools/test_epic020_bundle_tool.py",
    "tests/transport/test_a7_transport_proofs.py",
    "tests/transport/test_aux_narrative.py",
    "tests/transport/test_ops_rails_refusal.py",
    "tests/transport/test_writers_errors_headers.py",
    "tests/unit/test_narratives_loader.py",
    "tests/unit/test_narratives_router.py"
  ],
  "full_validation_target_count": 63,
  "pr01_product_owner_targets": {
    "catalog/channels_v1.json": [
      "tests/config/test_registry_catalog_contract.py",
      "tests/config/test_typed_bundles.py",
      "tests/compare/test_arrays_as_sets.py",
      "tests/evidence/test_canonical_json_gate_check_outputs.py"
    ],
    "schemas/channels_v1.schema.json": [
      "tests/config/test_registry_catalog_contract.py",
      "tests/config/test_typed_bundles.py",
      "tests/compare/test_arrays_as_sets.py",
      "tests/evidence/test_canonical_json_gate_check_outputs.py"
    ],
    "catalog/magic10_mechanics_v1.json": [
      "tests/config/test_magic10_contracts.py"
    ],
    "schemas/magic10_mechanics_v1.schema.json": [
      "tests/config/test_magic10_contracts.py"
    ],
    "schemas/magic10_result_v1.schema.json": [
      "tests/config/test_magic10_contracts.py"
    ],
    "schemas/magic10_compat_result_v1.schema.json": [
      "tests/config/test_magic10_contracts.py"
    ],
    "engine/config/registry_loader.py": [
      "tests/config/test_registry_catalog_contract.py",
      "tests/config/test_magic10_contracts.py",
      "tests/config/test_config_loader_unknown_ids_fail_closed.py",
      "tests/config/test_alias_policy_enforcement.py",
      "tests/config/test_manifest_schema.py",
      "tests/config/test_typed_bundles.py"
    ],
    "engine/config/bundles.py": [
      "tests/config/test_typed_bundles.py"
    ],
    "catalog/manifest.json": [
      "tests/runtime/test_identity.py",
      "tests/evidence/test_release_manifest_content_binding.py"
    ]
  },
  "config_writer_owner_targets": {
    "tools/generate_registry_report.py": [
      "tests/config/test_registry_report.py",
      "tests/config/test_registry_report_determinism.py",
      "tests/config/test_registry_report_indexing.py"
    ],
    "tools/config/artifacts.py": [
      "tests/config/test_config_artifacts.py",
      "tests/config/test_typed_bundles.py"
    ],
    "tools/config/generate_config_artifacts.py": [
      "tests/config/test_config_artifacts.py",
      "tests/config/test_typed_bundles.py"
    ],
    "tools/config/generate_bundles.py": [
      "tests/config/test_config_artifacts.py",
      "tests/config/test_typed_bundles.py"
    ]
  },
  "updater_owner_targets": [
    "tests/evidence/test_evidence_index_missing_state.py",
    "tests/evidence/test_evidence_tool_ownership.py",
    "tests/config/test_config_artifacts.py"
  ],
  "config_helper_owner_targets": [
    "tests/config/test_registry_catalog_contract.py",
    "tests/config/test_magic10_contracts.py",
    "tests/config/test_alias_policy_enforcement.py",
    "tests/config/test_config_loader_unknown_ids_fail_closed.py",
    "tests/config/test_manifest_schema.py",
    "tests/config/test_registry_report.py",
    "tests/config/test_registry_report_determinism.py",
    "tests/config/test_registry_report_indexing.py",
    "tests/config/test_config_artifacts.py",
    "tests/config/test_typed_bundles.py"
  ],
  "execution_performed": false
}
```

## Final internal result/evidence audit

Root recorded the helper’s completed read-only audit and applied both reporting corrections. SHA-256 6556799a08a2527daf5b2c83b413210bbb4c640ca82f2829854d97827d0e20d5.

```json
{
  "captured_at": "2026-09-09T19:16:56.366Z",
  "kind": "internal_read_only_result_evidence_audit",
  "helper": "writer_review",
  "head": "75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950",
  "verified": [
    "67 paths/blob/SHA-256/size match current head",
    "Plan section9 and Canon section11 each carried unchanged exactly once",
    "Six embedded reports match original bytes and hashes",
    "39 required companion records match",
    "FE/BE schema bytes and retained CRD evidence unchanged"
  ],
  "reporting_findings": [
    {
      "finding": "Exact548-test command/timing not retained in proof",
      "disposition": "Removed unsupported retention statement; retained actual log/tree/scope/hash; exact later owner/CI commands remain available"
    },
    {
      "finding": "67-path table chronology includes2 repair paths afterPRcreation",
      "disposition": "Clarified initial65 versus successor2 commit publication chronology"
    }
  ],
  "result": "No unresolved finding in audited scope; actual review/CI outcomes still pending"
}
```

## Actual GitHub review, CI and final saved verification

Final integration is complete. The exact native Result and complete terminal review/CI evidence below establish the PR-30 engineering endpoint. Product Owner manual merge and the later PR-40 lineage review remain pending native actions.

## Complete actual terminal CI log

Run34393325625; job102606798665; head75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950. All seven selected lanes and final applicability/clean-tree predicate passed. Compatibility retains62 passed,3 skipped and2 xfailed; these are unchanged test predicates, not a supplied waiver. Decoded source bytes 65503; SHA-256 4d288f04fd71ed5fc5f7e791bd803baa2ba898aa65343afaa2cc88618ff93511.

```text
﻿2026-09-09T19:09:05.7074126Z Current runner version: '2.337.0'
2026-09-09T19:09:05.7110937Z ##[group]Runner Image Provisioner
2026-09-09T19:09:05.7112483Z Hosted Compute Agent
2026-09-09T19:09:05.7113554Z Version: 20260828.587
2026-09-09T19:09:05.7114591Z Commit: abac92662cab4cc7352de4f9f9d2e2419aad9c29
2026-09-09T19:09:05.7116009Z Build Date: 2026-08-28T16:44:25Z
2026-09-09T19:09:05.7117136Z Worker ID: {04836f78-54b2-4f3b-b42b-b6fb778340c7}
2026-09-09T19:09:05.7118425Z Azure Region: westus2
2026-09-09T19:09:05.7119446Z ##[endgroup]
2026-09-09T19:09:05.7122174Z ##[group]Operating System
2026-09-09T19:09:05.7123447Z Ubuntu
2026-09-09T19:09:05.7124522Z 24.04.4
2026-09-09T19:09:05.7125568Z LTS
2026-09-09T19:09:05.7126593Z ##[endgroup]
2026-09-09T19:09:05.7127547Z ##[group]Runner Image
2026-09-09T19:09:05.7128747Z Image: ubuntu-24.04
2026-09-09T19:09:05.7130213Z Version: 20260831.293.1
2026-09-09T19:09:05.7132587Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260831.293/images/ubuntu/Ubuntu2404-Readme.md
2026-09-09T19:09:05.7135379Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260831.293
2026-09-09T19:09:05.7137367Z ##[endgroup]
2026-09-09T19:09:05.7139327Z ##[group]GITHUB_TOKEN Permissions
2026-09-09T19:09:05.7142618Z Contents: read
2026-09-09T19:09:05.7143672Z Metadata: read
2026-09-09T19:09:05.7144770Z ##[endgroup]
2026-09-09T19:09:05.7148011Z Secret source: Actions
2026-09-09T19:09:05.7150145Z Cache mode: write
2026-09-09T19:09:05.7151452Z Prepare workflow directory
2026-09-09T19:09:05.7888849Z Prepare all required actions
2026-09-09T19:09:05.7962115Z Getting action download info
2026-09-09T19:09:06.2653832Z Download action repository 'actions/checkout@v4' (SHA:11d5960a326750d5838078e36cf38b85af677262)
2026-09-09T19:09:06.4059278Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-09-09T19:09:06.5825365Z Complete job name: test
2026-09-09T19:09:06.6672376Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-09-09T19:09:06.6687166Z ##[group]Run actions/checkout@v4
2026-09-09T19:09:06.6687905Z with:
2026-09-09T19:09:06.6688323Z   fetch-depth: 0
2026-09-09T19:09:06.6688786Z   persist-credentials: false
2026-09-09T19:09:06.6689342Z   ref: 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950
2026-09-09T19:09:06.6690522Z   repository: amthorn78/glow-hdengine-v2
2026-09-09T19:09:06.6697179Z   token: ***
2026-09-09T19:09:06.6697643Z   ssh-strict: true
2026-09-09T19:09:06.6698071Z   ssh-user: git
2026-09-09T19:09:06.6698502Z   clean: true
2026-09-09T19:09:06.6698941Z   sparse-checkout-cone-mode: true
2026-09-09T19:09:06.6699461Z   fetch-tags: false
2026-09-09T19:09:06.6700342Z   show-progress: true
2026-09-09T19:09:06.6700807Z   lfs: false
2026-09-09T19:09:06.6701213Z   submodules: false
2026-09-09T19:09:06.6701663Z   set-safe-directory: true
2026-09-09T19:09:06.6702167Z   allow-unsafe-pr-checkout: false
2026-09-09T19:09:06.6703070Z env:
2026-09-09T19:09:06.6703466Z   LC_ALL: C
2026-09-09T19:09:06.6703852Z   LANG: C
2026-09-09T19:09:06.6704230Z   TZ: UTC
2026-09-09T19:09:06.6704620Z   SAFE_MODE: 1
2026-09-09T19:09:06.6705023Z   ALLOW_NETWORK: 0
2026-09-09T19:09:06.6705437Z   APP_ENV: dev
2026-09-09T19:09:06.6705863Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:09:06.6706352Z ##[endgroup]
2026-09-09T19:09:06.8702668Z Syncing repository: amthorn78/glow-hdengine-v2
2026-09-09T19:09:06.8705517Z ##[group]Getting Git version info
2026-09-09T19:09:06.8706889Z Working directory is '/home/runner/work/glow-hdengine-v2/glow-hdengine-v2'
2026-09-09T19:09:06.8708771Z [command]/usr/bin/git version
2026-09-09T19:09:06.8709624Z git version 2.55.0
2026-09-09T19:09:06.8713075Z ##[endgroup]
2026-09-09T19:09:06.8717790Z Temporarily overriding HOME='/home/runner/work/_temp/76ad8d6f-26a0-45f4-80fb-439e2d970e1b' before making global git config changes
2026-09-09T19:09:06.8719590Z Adding repository directory to the temporary git global config as a safe directory
2026-09-09T19:09:06.8721653Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/glow-hdengine-v2/glow-hdengine-v2
2026-09-09T19:09:06.8723526Z Deleting the contents of '/home/runner/work/glow-hdengine-v2/glow-hdengine-v2'
2026-09-09T19:09:06.8724714Z ##[group]Initializing the repository
2026-09-09T19:09:06.8726260Z [command]/usr/bin/git init /home/runner/work/glow-hdengine-v2/glow-hdengine-v2
2026-09-09T19:09:06.8727621Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-09-09T19:09:06.8730007Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-09-09T19:09:06.8731783Z hint: to use in all of your new repositories, which will suppress this warning,
2026-09-09T19:09:06.8733258Z hint: call:
2026-09-09T19:09:06.8734154Z hint:
2026-09-09T19:09:06.8735368Z hint: 	git config --global init.defaultBranch <name>
2026-09-09T19:09:06.8736678Z hint:
2026-09-09T19:09:06.8737887Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-09-09T19:09:06.8740309Z hint: 'development'. The just-created branch can be renamed via this command:
2026-09-09T19:09:06.8741579Z hint:
2026-09-09T19:09:06.8743213Z hint: 	git branch -m <name>
2026-09-09T19:09:06.8744249Z hint:
2026-09-09T19:09:06.8748875Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-09-09T19:09:06.8751204Z Initialized empty Git repository in /home/runner/work/glow-hdengine-v2/glow-hdengine-v2/.git/
2026-09-09T19:09:06.8761373Z [command]/usr/bin/git remote add origin https://github.com/amthorn78/glow-hdengine-v2
2026-09-09T19:09:06.8766317Z ##[endgroup]
2026-09-09T19:09:06.8767990Z ##[group]Disabling automatic garbage collection
2026-09-09T19:09:06.8770673Z [command]/usr/bin/git config --local gc.auto 0
2026-09-09T19:09:06.8773740Z ##[endgroup]
2026-09-09T19:09:06.8774964Z ##[group]Setting up auth
2026-09-09T19:09:06.8776182Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-09-09T19:09:06.8781983Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-09-09T19:09:06.8862771Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-09-09T19:09:06.8899490Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-09-09T19:09:06.9120886Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-09-09T19:09:06.9150128Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-09-09T19:09:06.9391362Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-09-09T19:09:06.9405154Z ##[endgroup]
2026-09-09T19:09:06.9407065Z ##[group]Fetching the repository
2026-09-09T19:09:06.9416915Z [command]/usr/bin/git -c protocol.version=2 fetch --prune --no-recurse-submodules origin +refs/heads/*:refs/remotes/origin/* +refs/tags/*:refs/tags/*
2026-09-09T19:09:10.3085234Z From https://github.com/amthorn78/glow-hdengine-v2
2026-09-09T19:09:10.3108617Z  * [new branch]        agent/hde-epic039-pr04-ci-efficiency -> origin/agent/hde-epic039-pr04-ci-efficiency
2026-09-09T19:09:10.3110128Z  * [new branch]        codex/hde-crd-0001-pr-02 -> origin/codex/hde-crd-0001-pr-02
2026-09-09T19:09:10.3111264Z  * [new branch]        crd/hde-crd-0001-pr-01-token-claims -> origin/crd/hde-crd-0001-pr-01-token-claims
2026-09-09T19:09:10.3112559Z  * [new branch]        evidence/hde-crd-0001-qa-retention-20260907 -> origin/evidence/hde-crd-0001-qa-retention-20260907
2026-09-09T19:09:10.3114181Z  * [new branch]        gcfpe/prompt-provenance-20260905 -> origin/gcfpe/prompt-provenance-20260905
2026-09-09T19:09:10.3115292Z  * [new branch]        hde-epic040-pr01-source-contracts -> origin/hde-epic040-pr01-source-contracts
2026-09-09T19:09:10.3220527Z  * [new branch]        main       -> origin/main
2026-09-09T19:09:10.3224344Z [command]/usr/bin/git rev-parse --verify --quiet 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950^{object}
2026-09-09T19:09:10.3240621Z 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950
2026-09-09T19:09:10.3256898Z ##[endgroup]
2026-09-09T19:09:10.3257981Z ##[group]Determining the checkout info
2026-09-09T19:09:10.3259211Z ##[endgroup]
2026-09-09T19:09:10.3260409Z [command]/usr/bin/git sparse-checkout disable
2026-09-09T19:09:10.3263336Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-09-09T19:09:10.3282755Z ##[group]Checking out the ref
2026-09-09T19:09:10.3286380Z [command]/usr/bin/git checkout --progress --force 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950
2026-09-09T19:09:10.7005927Z Note: switching to '75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950'.
2026-09-09T19:09:10.7006586Z 
2026-09-09T19:09:10.7006947Z You are in 'detached HEAD' state. You can look around, make experimental
2026-09-09T19:09:10.7007910Z changes and commit them, and you can discard any commits you make in this
2026-09-09T19:09:10.7008945Z state without impacting any branches by switching back to a branch.
2026-09-09T19:09:10.7009551Z 
2026-09-09T19:09:10.7010227Z If you want to create a new branch to retain commits you create, you may
2026-09-09T19:09:10.7011178Z do so (now or later) by using -c with the switch command. Example:
2026-09-09T19:09:10.7011683Z 
2026-09-09T19:09:10.7011931Z   git switch -c <new-branch-name>
2026-09-09T19:09:10.7012301Z 
2026-09-09T19:09:10.7012520Z Or undo this operation with:
2026-09-09T19:09:10.7012880Z 
2026-09-09T19:09:10.7013083Z   git switch -
2026-09-09T19:09:10.7013680Z 
2026-09-09T19:09:10.7014183Z Turn off this advice by setting config variable advice.detachedHead to false
2026-09-09T19:09:10.7014845Z 
2026-09-09T19:09:10.7015285Z HEAD is now at 75ddaf2c Fix Markdown-escaped token reading in CI owner validation
2026-09-09T19:09:10.7042634Z ##[endgroup]
2026-09-09T19:09:10.7083010Z [command]/usr/bin/git log -1 --format=%H
2026-09-09T19:09:10.7107689Z 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950
2026-09-09T19:09:10.7126308Z ##[group]Removing auth
2026-09-09T19:09:10.7127436Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-09-09T19:09:10.7153687Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-09-09T19:09:10.7376811Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-09-09T19:09:10.7403895Z http.https://github.com/.extraheader
2026-09-09T19:09:10.7412556Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-09-09T19:09:10.7447499Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-09-09T19:09:10.7681483Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-09-09T19:09:10.7706358Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-09-09T19:09:10.7922123Z ##[endgroup]
2026-09-09T19:09:10.8209589Z ##[group]Run set -euo pipefail
2026-09-09T19:09:10.8210265Z [36;1mset -euo pipefail[0m
2026-09-09T19:09:10.8210632Z [36;1mpython3 ci/checks/classify_ci_changes.py \[0m
2026-09-09T19:09:10.8211008Z [36;1m  --base "$BASE_SHA" \[0m
2026-09-09T19:09:10.8211314Z [36;1m  --head "$HEAD_SHA" \[0m
2026-09-09T19:09:10.8211629Z [36;1m  --event-name "pull_request" \[0m
2026-09-09T19:09:10.8211993Z [36;1m  --github-output "$GITHUB_OUTPUT" \[0m
2026-09-09T19:09:10.8212684Z [36;1m  --changed-tests-output "$RUNNER_TEMP/ci-changed-test-targets.txt"[0m
2026-09-09T19:09:10.8253560Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:09:10.8253972Z env:
2026-09-09T19:09:10.8254202Z   LC_ALL: C
2026-09-09T19:09:10.8254424Z   LANG: C
2026-09-09T19:09:10.8254636Z   TZ: UTC
2026-09-09T19:09:10.8254850Z   SAFE_MODE: 1
2026-09-09T19:09:10.8255089Z   ALLOW_NETWORK: 0
2026-09-09T19:09:10.8255327Z   APP_ENV: dev
2026-09-09T19:09:10.8255577Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:09:10.8255958Z   BASE_SHA: 9065e6f0c01ad82a65c78687cd6c55e26ca33a1f
2026-09-09T19:09:10.8256352Z   HEAD_SHA: 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950
2026-09-09T19:09:10.8256684Z ##[endgroup]
2026-09-09T19:09:11.2751448Z CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=67;lanes=product,compat,db,rails,evidence,qa,release
2026-09-09T19:09:11.2954283Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-09-09T19:09:11.2955987Z ##[group]Run actions/setup-python@v5
2026-09-09T19:09:11.2956252Z with:
2026-09-09T19:09:11.2956457Z   python-version: 3.12
2026-09-09T19:09:11.2956676Z   check-latest: false
2026-09-09T19:09:11.2959045Z   token: ***
2026-09-09T19:09:11.2959253Z   update-environment: true
2026-09-09T19:09:11.2959491Z   allow-prereleases: false
2026-09-09T19:09:11.2960174Z   freethreaded: false
2026-09-09T19:09:11.2960435Z env:
2026-09-09T19:09:11.2960619Z   LC_ALL: C
2026-09-09T19:09:11.2960795Z   LANG: C
2026-09-09T19:09:11.2960976Z   TZ: UTC
2026-09-09T19:09:11.2961144Z   SAFE_MODE: 1
2026-09-09T19:09:11.2961332Z   ALLOW_NETWORK: 0
2026-09-09T19:09:11.2961568Z   APP_ENV: dev
2026-09-09T19:09:11.2961775Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:09:11.2962031Z ##[endgroup]
2026-09-09T19:09:11.4349347Z ##[group]Installed versions
2026-09-09T19:09:11.4450004Z (node:2169) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-09-09T19:09:11.4451670Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-09-09T19:09:11.4452934Z Successfully set up CPython (3.12.14)
2026-09-09T19:09:11.4453944Z ##[endgroup]
2026-09-09T19:09:11.4736243Z ##[group]Run python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .
2026-09-09T19:09:11.4737041Z [36;1mpython -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .[0m
2026-09-09T19:09:11.4788506Z shell: /usr/bin/bash -e {0}
2026-09-09T19:09:11.4788773Z env:
2026-09-09T19:09:11.4788962Z   LC_ALL: C
2026-09-09T19:09:11.4789174Z   LANG: C
2026-09-09T19:09:11.4789376Z   TZ: UTC
2026-09-09T19:09:11.4789549Z   SAFE_MODE: 1
2026-09-09T19:09:11.4789950Z   ALLOW_NETWORK: 0
2026-09-09T19:09:11.4790173Z   APP_ENV: dev
2026-09-09T19:09:11.4790384Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:09:11.4790708Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:11.4791170Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:09:11.4791611Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:11.4792035Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:11.4792416Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:11.4792796Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:09:11.4793121Z ##[endgroup]
2026-09-09T19:09:12.4236375Z Obtaining file:///home/runner/work/glow-hdengine-v2/glow-hdengine-v2
2026-09-09T19:09:12.4270748Z   Installing build dependencies: started
2026-09-09T19:09:13.3387496Z   Installing build dependencies: finished with status 'done'
2026-09-09T19:09:13.3400595Z   Checking if build backend supports build_editable: started
2026-09-09T19:09:13.6702419Z   Checking if build backend supports build_editable: finished with status 'done'
2026-09-09T19:09:13.6720630Z   Getting requirements to build editable: started
2026-09-09T19:09:14.2061765Z   Getting requirements to build editable: finished with status 'done'
2026-09-09T19:09:14.2065186Z   Preparing editable metadata (pyproject.toml): started
2026-09-09T19:09:14.7356978Z   Preparing editable metadata (pyproject.toml): finished with status 'done'
2026-09-09T19:09:14.8173149Z Collecting setuptools>=68
2026-09-09T19:09:14.8189239Z   Using cached setuptools-84.0.0-py3-none-any.whl.metadata (6.6 kB)
2026-09-09T19:09:14.8375322Z Collecting wheel
2026-09-09T19:09:14.8388989Z   Using cached wheel-0.48.0-py3-none-any.whl.metadata (2.3 kB)
2026-09-09T19:09:14.9224540Z Collecting psycopg<3.3,>=3.1 (from psycopg[binary]<3.3,>=3.1->-r requirements.txt (line 1))
2026-09-09T19:09:14.9803636Z   Downloading psycopg-3.2.13-py3-none-any.whl.metadata (4.5 kB)
2026-09-09T19:09:15.0037889Z Collecting Flask<3.0,>=2.3 (from -r requirements.txt (line 2))
2026-09-09T19:09:15.0116410Z   Downloading flask-2.3.3-py3-none-any.whl.metadata (3.6 kB)
2026-09-09T19:09:15.0345445Z Collecting gunicorn<22,>=21 (from -r requirements.txt (line 3))
2026-09-09T19:09:15.0431189Z   Downloading gunicorn-21.2.0-py3-none-any.whl.metadata (4.1 kB)
2026-09-09T19:09:15.0681008Z Collecting jsonschema==4.23.0 (from -r requirements.txt (line 4))
2026-09-09T19:09:15.0752604Z   Downloading jsonschema-4.23.0-py3-none-any.whl.metadata (7.9 kB)
2026-09-09T19:09:15.1090937Z Collecting pytest<9.0,>=7.4 (from -r requirements-dev.txt (line 5))
2026-09-09T19:09:15.1157463Z   Downloading pytest-8.4.2-py3-none-any.whl.metadata (7.7 kB)
2026-09-09T19:09:15.1371042Z Collecting pytest-cov<5.0,>=4.1 (from -r requirements-dev.txt (line 6))
2026-09-09T19:09:15.1456420Z   Downloading pytest_cov-4.1.0-py3-none-any.whl.metadata (26 kB)
2026-09-09T19:09:15.1720871Z Collecting pytest-mock<4.0,>=3.12 (from -r requirements-dev.txt (line 7))
2026-09-09T19:09:15.1784380Z   Downloading pytest_mock-3.15.1-py3-none-any.whl.metadata (3.9 kB)
2026-09-09T19:09:15.1974791Z Collecting attrs>=22.2.0 (from jsonschema==4.23.0->-r requirements.txt (line 4))
2026-09-09T19:09:15.2046882Z   Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
2026-09-09T19:09:15.2221075Z Collecting jsonschema-specifications>=2023.03.6 (from jsonschema==4.23.0->-r requirements.txt (line 4))
2026-09-09T19:09:15.2293331Z   Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
2026-09-09T19:09:15.2530851Z Collecting referencing>=0.28.4 (from jsonschema==4.23.0->-r requirements.txt (line 4))
2026-09-09T19:09:15.2601836Z   Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
2026-09-09T19:09:15.5192801Z Collecting rpds-py>=0.7.1 (from jsonschema==4.23.0->-r requirements.txt (line 4))
2026-09-09T19:09:15.5283905Z   Downloading rpds_py-2026.6.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
2026-09-09T19:09:15.5497502Z Collecting typing-extensions>=4.6 (from psycopg<3.3,>=3.1->psycopg[binary]<3.3,>=3.1->-r requirements.txt (line 1))
2026-09-09T19:09:15.5568913Z   Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
2026-09-09T19:09:15.5794917Z Collecting Werkzeug>=2.3.7 (from Flask<3.0,>=2.3->-r requirements.txt (line 2))
2026-09-09T19:09:15.5879347Z   Downloading werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
2026-09-09T19:09:15.6054430Z Collecting Jinja2>=3.1.2 (from Flask<3.0,>=2.3->-r requirements.txt (line 2))
2026-09-09T19:09:15.6123718Z   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
2026-09-09T19:09:15.6280452Z Collecting itsdangerous>=2.1.2 (from Flask<3.0,>=2.3->-r requirements.txt (line 2))
2026-09-09T19:09:15.6357576Z   Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
2026-09-09T19:09:15.6550657Z Collecting click>=8.1.3 (from Flask<3.0,>=2.3->-r requirements.txt (line 2))
2026-09-09T19:09:15.6623230Z   Downloading click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
2026-09-09T19:09:15.6789439Z Collecting blinker>=1.6.2 (from Flask<3.0,>=2.3->-r requirements.txt (line 2))
2026-09-09T19:09:15.6858926Z   Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
2026-09-09T19:09:15.6978557Z Collecting packaging (from gunicorn<22,>=21->-r requirements.txt (line 3))
2026-09-09T19:09:15.6992316Z   Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
2026-09-09T19:09:15.7120271Z Collecting iniconfig>=1 (from pytest<9.0,>=7.4->-r requirements-dev.txt (line 5))
2026-09-09T19:09:15.7192377Z   Downloading iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
2026-09-09T19:09:15.7365645Z Collecting pluggy<2,>=1.5 (from pytest<9.0,>=7.4->-r requirements-dev.txt (line 5))
2026-09-09T19:09:15.7437487Z   Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
2026-09-09T19:09:15.7657814Z Collecting pygments>=2.7.2 (from pytest<9.0,>=7.4->-r requirements-dev.txt (line 5))
2026-09-09T19:09:15.7729160Z   Downloading pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
2026-09-09T19:09:16.1786129Z Collecting coverage>=5.2.1 (from coverage[toml]>=5.2.1->pytest-cov<5.0,>=4.1->-r requirements-dev.txt (line 6))
2026-09-09T19:09:16.1858814Z   Downloading coverage-7.16.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (8.6 kB)
2026-09-09T19:09:16.3338937Z Collecting psycopg-binary==3.2.13 (from psycopg[binary]<3.3,>=3.1->-r requirements.txt (line 1))
2026-09-09T19:09:16.3410995Z   Downloading psycopg_binary-3.2.13-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.9 kB)
2026-09-09T19:09:16.3971710Z Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->Flask<3.0,>=2.3->-r requirements.txt (line 2))
2026-09-09T19:09:16.4042293Z   Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
2026-09-09T19:09:16.4251166Z Downloading jsonschema-4.23.0-py3-none-any.whl (88 kB)
2026-09-09T19:09:16.4444172Z Downloading psycopg-3.2.13-py3-none-any.whl (206 kB)
2026-09-09T19:09:16.4650769Z Downloading flask-2.3.3-py3-none-any.whl (96 kB)
2026-09-09T19:09:16.4760340Z Downloading gunicorn-21.2.0-py3-none-any.whl (80 kB)
2026-09-09T19:09:16.4854617Z Downloading pytest-8.4.2-py3-none-any.whl (365 kB)
2026-09-09T19:09:16.5086189Z Downloading pytest_cov-4.1.0-py3-none-any.whl (21 kB)
2026-09-09T19:09:16.5173855Z Downloading pytest_mock-3.15.1-py3-none-any.whl (10 kB)
2026-09-09T19:09:16.5270803Z Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
2026-09-09T19:09:16.5470821Z Downloading psycopg_binary-3.2.13-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (4.4 MB)
2026-09-09T19:09:16.5898675Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.4/4.4 MB 105.1 MB/s  0:00:00
2026-09-09T19:09:16.5916622Z Using cached setuptools-84.0.0-py3-none-any.whl (818 kB)
2026-09-09T19:09:16.5930538Z Using cached wheel-0.48.0-py3-none-any.whl (33 kB)
2026-09-09T19:09:16.6007299Z Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
2026-09-09T19:09:16.6108765Z Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
2026-09-09T19:09:16.6196120Z Downloading click-8.5.0-py3-none-any.whl (125 kB)
2026-09-09T19:09:16.6292128Z Downloading coverage-7.16.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (257 kB)
2026-09-09T19:09:16.6390001Z Downloading iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
2026-09-09T19:09:16.6478087Z Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
2026-09-09T19:09:16.6570456Z Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
2026-09-09T19:09:16.6667902Z Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
2026-09-09T19:09:16.6766056Z Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
2026-09-09T19:09:16.6801139Z Using cached packaging-26.3-py3-none-any.whl (129 kB)
2026-09-09T19:09:16.6876161Z Downloading pygments-2.21.0-py3-none-any.whl (1.3 MB)
2026-09-09T19:09:16.6989914Z    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 121.9 MB/s  0:00:00
2026-09-09T19:09:16.7057761Z Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
2026-09-09T19:09:16.7153176Z Downloading rpds_py-2026.6.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (366 kB)
2026-09-09T19:09:16.7266895Z Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
2026-09-09T19:09:16.7375541Z Downloading werkzeug-3.1.8-py3-none-any.whl (226 kB)
2026-09-09T19:09:16.8021015Z Building wheels for collected packages: glow-hdengine
2026-09-09T19:09:16.8033432Z   Building editable for glow-hdengine (pyproject.toml): started
2026-09-09T19:09:17.3814630Z   Building editable for glow-hdengine (pyproject.toml): finished with status 'done'
2026-09-09T19:09:17.3821189Z   Created wheel for glow-hdengine: filename=glow_hdengine-0.0.0-0.editable-py3-none-any.whl size=17974 sha256=305669b3978461bfbb1f584129da837d1eaf6df7f90d51603e250a74363bb4ff
2026-09-09T19:09:17.3823430Z   Stored in directory: /tmp/pip-ephem-wheel-cache-b4dqtzna/wheels/51/e3/d8/d35d8425d15176d06ccdae163b60c707de926d2b6963e1e576
2026-09-09T19:09:17.3849350Z Successfully built glow-hdengine
2026-09-09T19:09:17.4365926Z Installing collected packages: typing-extensions, setuptools, rpds-py, pygments, psycopg-binary, pluggy, packaging, MarkupSafe, itsdangerous, iniconfig, glow-hdengine, coverage, click, blinker, attrs, wheel, Werkzeug, referencing, pytest, psycopg, Jinja2, gunicorn, pytest-mock, pytest-cov, jsonschema-specifications, Flask, jsonschema
2026-09-09T19:09:20.0401723Z 
2026-09-09T19:09:20.0433206Z Successfully installed Flask-2.3.3 Jinja2-3.1.6 MarkupSafe-3.0.3 Werkzeug-3.1.8 attrs-26.1.0 blinker-1.9.0 click-8.5.0 coverage-7.16.0 glow-hdengine-0.0.0 gunicorn-21.2.0 iniconfig-2.3.0 itsdangerous-2.2.0 jsonschema-4.23.0 jsonschema-specifications-2025.9.1 packaging-26.3 pluggy-1.6.0 psycopg-3.2.13 psycopg-binary-3.2.13 pygments-2.21.0 pytest-8.4.2 pytest-cov-4.1.0 pytest-mock-3.15.1 referencing-0.37.0 rpds-py-2026.6.3 setuptools-84.0.0 typing-extensions-4.16.0 wheel-0.48.0
2026-09-09T19:09:20.1447087Z ##[group]Run python -m pytest --version
2026-09-09T19:09:20.1447466Z [36;1mpython -m pytest --version[0m
2026-09-09T19:09:20.1483883Z shell: /usr/bin/bash -e {0}
2026-09-09T19:09:20.1484138Z env:
2026-09-09T19:09:20.1484314Z   LC_ALL: C
2026-09-09T19:09:20.1484492Z   LANG: C
2026-09-09T19:09:20.1484664Z   TZ: UTC
2026-09-09T19:09:20.1484838Z   SAFE_MODE: 1
2026-09-09T19:09:20.1485027Z   ALLOW_NETWORK: 0
2026-09-09T19:09:20.1485219Z   APP_ENV: dev
2026-09-09T19:09:20.1485421Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:09:20.1485747Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.1486198Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:09:20.1486623Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.1486999Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.1487377Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.1487827Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:09:20.1488161Z ##[endgroup]
2026-09-09T19:09:20.7591441Z pytest 8.4.2
2026-09-09T19:09:20.7956188Z ##[group]Run ci/checks/check_env_pins.sh
2026-09-09T19:09:20.7956714Z [36;1mci/checks/check_env_pins.sh[0m
2026-09-09T19:09:20.7993315Z shell: /usr/bin/bash -e {0}
2026-09-09T19:09:20.7993569Z env:
2026-09-09T19:09:20.7993750Z   LC_ALL: C
2026-09-09T19:09:20.7993929Z   LANG: C
2026-09-09T19:09:20.7994093Z   TZ: UTC
2026-09-09T19:09:20.7994258Z   SAFE_MODE: 1
2026-09-09T19:09:20.7994447Z   ALLOW_NETWORK: 0
2026-09-09T19:09:20.7994639Z   APP_ENV: dev
2026-09-09T19:09:20.7994847Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:09:20.7995161Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.7995594Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:09:20.7996026Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.7996435Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.7996838Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.7997428Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:09:20.7997748Z ##[endgroup]
2026-09-09T19:09:20.8812323Z [env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC
2026-09-09T19:09:20.8846912Z ##[group]Run set -euo pipefail
2026-09-09T19:09:20.8847242Z [36;1mset -euo pipefail[0m
2026-09-09T19:09:20.8847572Z [36;1mchanged_test_source="$RUNNER_TEMP/hde-changed-test-source"[0m
2026-09-09T19:09:20.8848043Z [36;1mchanged_test_manifest="$RUNNER_TEMP/ci-changed-test-targets.txt"[0m
2026-09-09T19:09:20.8848422Z [36;1mcleanup() {[0m
2026-09-09T19:09:20.8848767Z [36;1m  git worktree remove --force "$changed_test_source" >/dev/null 2>&1 || true[0m
2026-09-09T19:09:20.8849222Z [36;1m}[0m
2026-09-09T19:09:20.8849413Z [36;1mtrap cleanup EXIT[0m
2026-09-09T19:09:20.8850006Z [36;1mtest -f "$changed_test_manifest"[0m
2026-09-09T19:09:20.8850432Z [36;1mmapfile -t changed_test_targets < "$changed_test_manifest"[0m
2026-09-09T19:09:20.8850815Z [36;1m(( ${#changed_test_targets[@]} > 0 ))[0m
2026-09-09T19:09:20.8851216Z [36;1mgit worktree add --detach "$changed_test_source" "$(git rev-parse HEAD)"[0m
2026-09-09T19:09:20.8851604Z [36;1m([0m
2026-09-09T19:09:20.8851840Z [36;1m  cd "$changed_test_source"[0m
2026-09-09T19:09:20.8852099Z [36;1m  unset GH_TOKEN[0m
2026-09-09T19:09:20.8852523Z [36;1m  export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1[0m
2026-09-09T19:09:20.8853031Z [36;1m  export PYTHONPATH="$changed_test_source"[0m
2026-09-09T19:09:20.8853473Z [36;1m  python -m pytest -q -p no:cacheprovider -- "${changed_test_targets[@]}"[0m
2026-09-09T19:09:20.8853882Z [36;1m  git diff --exit-code[0m
2026-09-09T19:09:20.8854200Z [36;1m  test -z "$(git status --short --untracked-files=all)"[0m
2026-09-09T19:09:20.8854533Z [36;1m)[0m
2026-09-09T19:09:20.8854714Z [36;1mcleanup[0m
2026-09-09T19:09:20.8854914Z [36;1mtrap - EXIT[0m
2026-09-09T19:09:20.8891516Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:09:20.8891869Z env:
2026-09-09T19:09:20.8892046Z   LC_ALL: C
2026-09-09T19:09:20.8892222Z   LANG: C
2026-09-09T19:09:20.8892393Z   TZ: UTC
2026-09-09T19:09:20.8892560Z   SAFE_MODE: 1
2026-09-09T19:09:20.8892760Z   ALLOW_NETWORK: 0
2026-09-09T19:09:20.8892955Z   APP_ENV: dev
2026-09-09T19:09:20.8893160Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:09:20.8893470Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.8893901Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:09:20.8894322Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.8894699Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.8895075Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:09:20.8895452Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:09:20.8895772Z ##[endgroup]
2026-09-09T19:09:20.8989203Z Preparing worktree (detached HEAD 75ddaf2c)
2026-09-09T19:09:21.3540978Z HEAD is now at 75ddaf2c Fix Markdown-escaped token reading in CI owner validation
2026-09-09T19:09:24.7274963Z ........................................................................ [  4%]
2026-09-09T19:09:28.0864931Z ........................................................................ [  9%]
2026-09-09T19:09:51.8932112Z ........................................................................ [ 13%]
2026-09-09T19:09:55.2393720Z ........................................................................ [ 18%]
2026-09-09T19:10:01.2147374Z ........................................................................ [ 23%]
2026-09-09T19:10:05.6425506Z ........................................................................ [ 27%]
2026-09-09T19:10:06.3653072Z ........................................................................ [ 32%]
2026-09-09T19:10:08.6065961Z ........................................................................ [ 37%]
2026-09-09T19:10:08.6598001Z ........................................................................ [ 41%]
2026-09-09T19:10:09.1093467Z ........................................................................ [ 46%]
2026-09-09T19:10:12.6765567Z ........................................................................ [ 51%]
2026-09-09T19:10:15.5304340Z ........................................................................ [ 55%]
2026-09-09T19:10:17.4172353Z ........................................................................ [ 60%]
2026-09-09T19:10:17.5426898Z ........................................................................ [ 65%]
2026-09-09T19:10:17.8159237Z ........................................................................ [ 69%]
2026-09-09T19:10:18.3554432Z ........................................................................ [ 74%]
2026-09-09T19:10:32.9332417Z ........................................................................ [ 79%]
2026-09-09T19:10:47.3373330Z ........................................................................ [ 83%]
2026-09-09T19:10:50.8339203Z ........................................................................ [ 88%]
2026-09-09T19:10:50.9660707Z ........................................................................ [ 93%]
2026-09-09T19:10:51.9876182Z ........................................................................ [ 97%]
2026-09-09T19:10:52.4091865Z ................................                                         [100%]
2026-09-09T19:10:52.4092999Z 1544 passed in 90.44s (0:01:30)
2026-09-09T19:10:52.9896909Z ##[group]Run set -euo pipefail
2026-09-09T19:10:52.9897234Z [36;1mset -euo pipefail[0m
2026-09-09T19:10:52.9897562Z [36;1mpython tools/order/generate_ordering_artifacts.py --check[0m
2026-09-09T19:10:52.9897934Z [36;1mpython -m pytest -q \[0m
2026-09-09T19:10:52.9898173Z [36;1m  tests/order \[0m
2026-09-09T19:10:52.9898427Z [36;1m  tests/mech/test_order_properties.py \[0m
2026-09-09T19:10:52.9898767Z [36;1m  tests/evidence/test_architecture_snapshot.py[0m
2026-09-09T19:10:52.9940139Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:10:52.9940500Z env:
2026-09-09T19:10:52.9940680Z   LC_ALL: C
2026-09-09T19:10:52.9940854Z   LANG: C
2026-09-09T19:10:52.9941024Z   TZ: UTC
2026-09-09T19:10:52.9941193Z   SAFE_MODE: 1
2026-09-09T19:10:52.9941375Z   ALLOW_NETWORK: 0
2026-09-09T19:10:52.9941566Z   APP_ENV: dev
2026-09-09T19:10:52.9941764Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:10:52.9942079Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:10:52.9942550Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:10:52.9942971Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:10:52.9943342Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:10:52.9943718Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:10:52.9944094Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:10:52.9944421Z ##[endgroup]
2026-09-09T19:11:03.7403212Z ....................                                                     [100%]
2026-09-09T19:11:03.7404034Z 20 passed in 9.94s
2026-09-09T19:11:03.7839207Z ##[group]Run set -euo pipefail
2026-09-09T19:11:03.7840032Z [36;1mset -euo pipefail[0m
2026-09-09T19:11:03.7840511Z [36;1mci/checks/check_cli_help.sh[0m
2026-09-09T19:11:03.7841376Z [36;1mpython tools/cli/serializer_grep_guard.py --output "$RUNNER_TEMP/serializer_grep_guard.log"[0m
2026-09-09T19:11:03.7842593Z [36;1mpython tools/cli/emitter_symbol_proof.py --output "$RUNNER_TEMP/emitter_symbol_proof.txt"[0m
2026-09-09T19:11:03.7843467Z [36;1mpython -m pytest -q \[0m
2026-09-09T19:11:03.7843956Z [36;1m  tests/adapter/test_jsonschema.py \[0m
2026-09-09T19:11:03.7844518Z [36;1m  tests/cli/test_cli_usage_and_errors.py \[0m
2026-09-09T19:11:03.7845080Z [36;1m  tests/cli/test_errors_parity.py \[0m
2026-09-09T19:11:03.7845630Z [36;1m  tests/cli/test_cli_canonical_bytes.py \[0m
2026-09-09T19:11:03.7846578Z [36;1m  tests/cli/test_showcompat_parity_and_identity.py \[0m
2026-09-09T19:11:03.7847253Z [36;1m  tests/cli/test_serializer_guards.py \[0m
2026-09-09T19:11:03.7847944Z [36;1m  tests/transport/test_internal_version_contract.py \[0m
2026-09-09T19:11:03.7848617Z [36;1m  tests/http/test_compat_endpoint_contract.py \[0m
2026-09-09T19:11:03.7849237Z [36;1m  tests/adapter/test_compat_http_dev.py \[0m
2026-09-09T19:11:03.7850193Z [36;1m  tests/adapter/test_compat_http_parity.py[0m
2026-09-09T19:11:03.7902785Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:11:03.7903369Z env:
2026-09-09T19:11:03.7903696Z   LC_ALL: C
2026-09-09T19:11:03.7904020Z   LANG: C
2026-09-09T19:11:03.7904330Z   TZ: UTC
2026-09-09T19:11:03.7904643Z   SAFE_MODE: 1
2026-09-09T19:11:03.7904989Z   ALLOW_NETWORK: 0
2026-09-09T19:11:03.7905342Z   APP_ENV: dev
2026-09-09T19:11:03.7905718Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:11:03.7906287Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:03.7907086Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:11:03.7907884Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:03.7908572Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:03.7909279Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:03.7910346Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:11:03.7910947Z ##[endgroup]
2026-09-09T19:11:09.2158028Z ..xx..................sss..........................................      [100%]
2026-09-09T19:11:09.2161074Z 62 passed, 3 skipped, 2 xfailed in 4.52s
2026-09-09T19:11:09.2704952Z ##[group]Run set -euo pipefail
2026-09-09T19:11:09.2705472Z [36;1mset -euo pipefail[0m
2026-09-09T19:11:09.2706089Z [36;1mpython ci/checks/check_direct_db_contract.py[0m
2026-09-09T19:11:09.2706702Z [36;1mpython -m pytest -q \[0m
2026-09-09T19:11:09.2707132Z [36;1m  tests/db \[0m
2026-09-09T19:11:09.2707670Z [36;1m  tests/unit/test_check_direct_db_contract.py \[0m
2026-09-09T19:11:09.2708584Z [36;1m  tests/bodygraph/test_bg_resolve_v2_mapped_cache.py \[0m
2026-09-09T19:11:09.2709595Z [36;1m  tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py \[0m
2026-09-09T19:11:09.2710893Z [36;1m  tests/bodygraph/test_ingest.py \[0m
2026-09-09T19:11:09.2711688Z [36;1m  tests/ops/test_capture_rails_open_scope.py \[0m
2026-09-09T19:11:09.2712512Z [36;1m  tests/ops/test_http_logging.py[0m
2026-09-09T19:11:09.2754898Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:11:09.2755768Z env:
2026-09-09T19:11:09.2810067Z   LC_ALL: C
2026-09-09T19:11:09.2810463Z   LANG: C
2026-09-09T19:11:09.2810749Z   TZ: UTC
2026-09-09T19:11:09.2811014Z   SAFE_MODE: 1
2026-09-09T19:11:09.2811313Z   ALLOW_NETWORK: 0
2026-09-09T19:11:09.2811664Z   APP_ENV: dev
2026-09-09T19:11:09.2812025Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:11:09.2812581Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:09.2813385Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:11:09.2814196Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:09.2814892Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:09.2815604Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:09.2816320Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:11:09.2816801Z ##[endgroup]
2026-09-09T19:11:18.8274893Z DIRECT_DB_CONTRACT_OK
2026-09-09T19:11:19.8648595Z ........................................................................ [ 28%]
2026-09-09T19:11:20.1750259Z ........................................................................ [ 57%]
2026-09-09T19:11:20.8026855Z ........................................................................ [ 86%]
2026-09-09T19:11:20.9038768Z .................................                                        [100%]
2026-09-09T19:11:20.9040414Z =============================== warnings summary ===============================
2026-09-09T19:11:20.9041846Z tests/ops/test_http_logging.py::test_log_http_call_keys_only
2026-09-09T19:11:20.9043076Z tests/ops/test_http_logging.py::test_log_override_rejects_symlink_target
2026-09-09T19:11:20.9045267Z tests/ops/test_http_logging.py::test_log_override_rejects_symlink_parent
2026-09-09T19:11:20.9046436Z tests/ops/test_http_logging.py::test_append_remains_anchored_when_checked_parent_name_is_swapped
2026-09-09T19:11:20.9047635Z tests/ops/test_http_logging.py::test_owned_capture_override_writes_only_fixed_subtree
2026-09-09T19:11:20.9050152Z   /home/runner/work/glow-hdengine-v2/glow-hdengine-v2/engine/ops/http_log.py:202: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
2026-09-09T19:11:20.9052297Z     "at": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
2026-09-09T19:11:20.9052950Z 
2026-09-09T19:11:20.9053483Z -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
2026-09-09T19:11:20.9054347Z 249 passed, 5 warnings in 1.60s
2026-09-09T19:11:20.9661539Z ##[group]Run set -euo pipefail
2026-09-09T19:11:20.9662051Z [36;1mset -euo pipefail[0m
2026-09-09T19:11:20.9662562Z [36;1mpython ci/checks/run_rails_job_definitions.py \[0m
2026-09-09T19:11:20.9663170Z [36;1m  ci/jobs/rails_closed_refusal.yml \[0m
2026-09-09T19:11:20.9663715Z [36;1m  ci/jobs/rails_open_conformance.yml \[0m
2026-09-09T19:11:20.9664259Z [36;1m  ci/jobs/logs_keys_only_redaction.yml[0m
2026-09-09T19:11:20.9664998Z [36;1mpython -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py[0m
2026-09-09T19:11:20.9745751Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:11:20.9746330Z env:
2026-09-09T19:11:20.9746635Z   LC_ALL: C
2026-09-09T19:11:20.9746946Z   LANG: C
2026-09-09T19:11:20.9747148Z   TZ: UTC
2026-09-09T19:11:20.9747322Z   SAFE_MODE: 1
2026-09-09T19:11:20.9747527Z   ALLOW_NETWORK: 0
2026-09-09T19:11:20.9747723Z   APP_ENV: dev
2026-09-09T19:11:20.9747926Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:11:20.9748271Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:20.9748725Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:11:20.9749183Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:20.9749565Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:20.9750285Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:20.9750793Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:11:20.9751350Z ##[endgroup]
2026-09-09T19:11:21.0281841Z RUN rails_closed_refusal: python -m pytest tests/bodygraph/test_resolver_vendor.py -q
2026-09-09T19:11:21.5927886Z ....                                                                     [100%]
2026-09-09T19:11:21.5928660Z 4 passed in 0.08s
2026-09-09T19:11:21.6231365Z RUN rails_open_conformance: python -m pytest tests/bodygraph/test_vendor_client.py tests/evidence/test_open_rails_abba_proof.py -q
2026-09-09T19:11:38.2751091Z ........................................................................ [ 66%]
2026-09-09T19:11:38.3813397Z ....................................                                     [100%]
2026-09-09T19:11:38.3814428Z 108 passed in 16.28s
2026-09-09T19:11:39.2020016Z RUN rails_open_conformance: python tools/evidence/generate_open_rails_abba_proof.py --check-current
2026-09-09T19:11:41.0551220Z {"path": "audit/gates/determinism/open_rails_abba.json", "result": "pass", "status": "OK", "top_level_pass": true}
2026-09-09T19:11:41.0689396Z RUN logs_keys_only_redaction: python tools/evidence/generate_rails_gate_evidence.py --check
2026-09-09T19:11:41.1783299Z RAILS_GATE_EVIDENCE_OK
2026-09-09T19:11:41.1891309Z RUN logs_keys_only_redaction: python -m pytest tests/bodygraph/test_vendor_client.py tests/bodygraph/test_resolver_vendor.py -q
2026-09-09T19:11:41.8331390Z .......................................                                  [100%]
2026-09-09T19:11:41.8332362Z 39 passed in 0.17s
2026-09-09T19:11:41.8700879Z RAILS_JOB_DEFINITIONS_OK
2026-09-09T19:11:43.0611939Z ........................................................................ [ 69%]
2026-09-09T19:11:53.1000969Z ................................                                         [100%]
2026-09-09T19:11:53.1001829Z 104 passed in 10.75s
2026-09-09T19:11:53.1420759Z ##[group]Run set -euo pipefail
2026-09-09T19:11:53.1421110Z [36;1mset -euo pipefail[0m
2026-09-09T19:11:53.1421449Z [36;1mpython tools/evidence/update_evidence_index.py --check[0m
2026-09-09T19:11:53.1421861Z [36;1mpython tools/evidence/orientation_demo.py --check[0m
2026-09-09T19:11:53.1422280Z [36;1mpython tools/evidence/refresh_step_logs_manifest.py --check[0m
2026-09-09T19:11:53.1422682Z [36;1mci/checks/check_evidence_index_hash.sh[0m
2026-09-09T19:11:53.1423032Z [36;1mpython tools/evidence/validate_evidence_paths.py[0m
2026-09-09T19:11:53.1423384Z [36;1mci/checks/check_mirror_schema.sh[0m
2026-09-09T19:11:53.1423664Z [36;1mci/checks/check_final_lf.sh[0m
2026-09-09T19:11:53.1423931Z [36;1mpython -m pytest -q \[0m
2026-09-09T19:11:53.1424246Z [36;1m  tests/evidence/test_evidence_index_missing_state.py \[0m
2026-09-09T19:11:53.1424623Z [36;1m  tests/evidence/test_evidence_skeleton.py \[0m
2026-09-09T19:11:53.1425007Z [36;1m  tests/evidence/test_machine_mirror_self_proof.py \[0m
2026-09-09T19:11:53.1425368Z [36;1m  tests/evidence/test_orientation_demo.py \[0m
2026-09-09T19:11:53.1425683Z [36;1m  tests/ops/test_evidence_index.py \[0m
2026-09-09T19:11:53.1425979Z [36;1m  tests/qa/test_epic020_qa_docs.py[0m
2026-09-09T19:11:53.1462396Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:11:53.1462739Z env:
2026-09-09T19:11:53.1462919Z   LC_ALL: C
2026-09-09T19:11:53.1463097Z   LANG: C
2026-09-09T19:11:53.1463261Z   TZ: UTC
2026-09-09T19:11:53.1463424Z   SAFE_MODE: 1
2026-09-09T19:11:53.1463621Z   ALLOW_NETWORK: 0
2026-09-09T19:11:53.1463815Z   APP_ENV: dev
2026-09-09T19:11:53.1464019Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:11:53.1464327Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:53.1464752Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:11:53.1465172Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:53.1465550Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:53.1465929Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:11:53.1466298Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:11:53.1466609Z ##[endgroup]
2026-09-09T19:11:53.8112405Z [evidence-index] env pins: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC
2026-09-09T19:18:19.4920652Z ........................................................................ [ 64%]
2026-09-09T19:18:20.4780817Z .......................................                                  [100%]
2026-09-09T19:18:20.4781852Z 111 passed in 385.40s (0:06:25)
2026-09-09T19:18:20.5170846Z ##[group]Run set -euo pipefail
2026-09-09T19:18:20.5171368Z [36;1mset -euo pipefail[0m
2026-09-09T19:18:20.5171853Z [36;1mqa_source="$RUNNER_TEMP/hde-generic-qa-tests"[0m
2026-09-09T19:18:20.5172370Z [36;1mcleanup() {[0m
2026-09-09T19:18:20.5172945Z [36;1m  git worktree remove --force "$qa_source" >/dev/null 2>&1 || true[0m
2026-09-09T19:18:20.5173628Z [36;1m}[0m
2026-09-09T19:18:20.5173995Z [36;1mtrap cleanup EXIT[0m
2026-09-09T19:18:20.5174613Z [36;1mgit worktree add --detach "$qa_source" "$(git rev-parse HEAD)"[0m
2026-09-09T19:18:20.5175264Z [36;1m([0m
2026-09-09T19:18:20.5175600Z [36;1m  cd "$qa_source"[0m
2026-09-09T19:18:20.5176004Z [36;1m  unset GH_TOKEN[0m
2026-09-09T19:18:20.5176785Z [36;1m  export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1[0m
2026-09-09T19:18:20.5177670Z [36;1m  export PYTHONPATH="$qa_source"[0m
2026-09-09T19:18:20.5178500Z [36;1m  python -m pytest -q \[0m
2026-09-09T19:18:20.5179046Z [36;1m    tests/qa/test_generic_qa_harness.py \[0m
2026-09-09T19:18:20.5185359Z [36;1m    tests/qa/test_qa_harness_followup.py \[0m
2026-09-09T19:18:20.5186240Z [36;1m    tests/qa/test_epic021_harness_entrypoint.py \[0m
2026-09-09T19:18:20.5186931Z [36;1m    tests/qa/test_epic021_acceptance_alignment.py \[0m
2026-09-09T19:18:20.5187571Z [36;1m    tests/qa/test_tooling_bootstrap.py \[0m
2026-09-09T19:18:20.5188193Z [36;1m    tests/qa/test_viability_generator_wrappers.py \[0m
2026-09-09T19:18:20.5188841Z [36;1m    tests/qa/test_epic029_requalification.py[0m
2026-09-09T19:18:20.5189385Z [36;1m  git diff --exit-code[0m
2026-09-09T19:18:20.5190265Z [36;1m  test -z "$(git status --short --untracked-files=all)"[0m
2026-09-09T19:18:20.5190836Z [36;1m)[0m
2026-09-09T19:18:20.5191166Z [36;1mcleanup[0m
2026-09-09T19:18:20.5191521Z [36;1mtrap - EXIT[0m
2026-09-09T19:18:20.5241230Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:18:20.5241597Z env:
2026-09-09T19:18:20.5241891Z   LC_ALL: C
2026-09-09T19:18:20.5242150Z   LANG: C
2026-09-09T19:18:20.5242317Z   TZ: UTC
2026-09-09T19:18:20.5242481Z   SAFE_MODE: 1
2026-09-09T19:18:20.5242669Z   ALLOW_NETWORK: 0
2026-09-09T19:18:20.5242858Z   APP_ENV: dev
2026-09-09T19:18:20.5243165Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:18:20.5243554Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:18:20.5243989Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:18:20.5244566Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:18:20.5244942Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:18:20.5245315Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:18:20.5245855Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:18:20.5246170Z ##[endgroup]
2026-09-09T19:18:20.5351643Z Preparing worktree (detached HEAD 75ddaf2c)
2026-09-09T19:18:21.0640517Z HEAD is now at 75ddaf2c Fix Markdown-escaped token reading in CI owner validation
2026-09-09T19:18:23.0111050Z ........................................................................ [ 14%]
2026-09-09T19:18:23.5074297Z ........................................................................ [ 29%]
2026-09-09T19:18:26.0407291Z ........................................................................ [ 44%]
2026-09-09T19:18:28.2871324Z ........................................................................ [ 59%]
2026-09-09T19:18:41.2321263Z ........................................................................ [ 73%]
2026-09-09T19:18:42.1924789Z ........................................................................ [ 88%]
2026-09-09T19:18:42.4400398Z ........................................................                 [100%]
2026-09-09T19:18:42.4401183Z 488 passed in 20.84s
2026-09-09T19:18:42.7946069Z ##[group]Run set -euo pipefail
2026-09-09T19:18:42.7946689Z [36;1mset -euo pipefail[0m
2026-09-09T19:18:42.7947291Z [36;1mattestation_root="$RUNNER_TEMP/hde-release-attestation"[0m
2026-09-09T19:18:42.7948152Z [36;1mrelease_test_source="$RUNNER_TEMP/hde-release-regression-tests"[0m
2026-09-09T19:18:42.7948842Z [36;1mcleanup() {[0m
2026-09-09T19:18:42.7949480Z [36;1m  git worktree remove --force "$release_test_source" >/dev/null 2>&1 || true[0m
2026-09-09T19:18:42.7950483Z [36;1m}[0m
2026-09-09T19:18:42.7950782Z [36;1mtrap cleanup EXIT[0m
2026-09-09T19:18:42.7951160Z [36;1mtest ! -e "$attestation_root"[0m
2026-09-09T19:18:42.7951598Z [36;1mtest ! -e "$release_test_source"[0m
2026-09-09T19:18:42.7952027Z [36;1mgit diff --exit-code[0m
2026-09-09T19:18:42.7952562Z [36;1mpython scripts/release_id_recompute.py --check-manifest-only[0m
2026-09-09T19:18:42.7953342Z [36;1mgit worktree add --detach "$release_test_source" "$(git rev-parse HEAD)"[0m
2026-09-09T19:18:42.7953988Z [36;1m([0m
2026-09-09T19:18:42.7954294Z [36;1m  cd "$release_test_source"[0m
2026-09-09T19:18:42.7955002Z [36;1m  export PYTHONPATH="$release_test_source"[0m
2026-09-09T19:18:42.7955475Z [36;1m  python -m pytest -q \[0m
2026-09-09T19:18:42.7955902Z [36;1m    tests/runtime/test_identity.py \[0m
2026-09-09T19:18:42.7956419Z [36;1m    tests/evidence/test_release_attestation.py \[0m
2026-09-09T19:18:42.7957044Z [36;1m    tests/evidence/test_release_manifest_content_binding.py \[0m
2026-09-09T19:18:42.7957659Z [36;1m    tests/evidence/test_sanity_pipeline.py[0m
2026-09-09T19:18:42.7958141Z [36;1m  git diff --exit-code[0m
2026-09-09T19:18:42.7958654Z [36;1m  test -z "$(git status --short --untracked-files=all)"[0m
2026-09-09T19:18:42.7959201Z [36;1m)[0m
2026-09-09T19:18:42.7959514Z [36;1mcleanup[0m
2026-09-09T19:18:42.7960193Z [36;1mtrap - EXIT[0m
2026-09-09T19:18:42.7960692Z [36;1mtest -z "$(git status --short --untracked-files=all)"[0m
2026-09-09T19:18:42.7961396Z [36;1mpython tools/evidence/build_release_attestation.py \[0m
2026-09-09T19:18:42.7962010Z [36;1m  --output "$attestation_root" \[0m
2026-09-09T19:18:42.7962486Z [36;1m  --require-clean[0m
2026-09-09T19:18:42.7962999Z [36;1mpython tools/evidence/build_release_attestation.py \[0m
2026-09-09T19:18:42.7963595Z [36;1m  --verify "$attestation_root" \[0m
2026-09-09T19:18:42.7964057Z [36;1m  --require-clean[0m
2026-09-09T19:18:42.7964618Z [36;1m# No active release or deployment workflow consumes this bundle.[0m
2026-09-09T19:18:42.7965431Z [36;1m# Keep it ephemeral instead of adding an unconsumed artifact transfer.[0m
2026-09-09T19:18:42.7966106Z [36;1mgit diff --exit-code[0m
2026-09-09T19:18:42.7966623Z [36;1mtest -z "$(git status --short --untracked-files=all)"[0m
2026-09-09T19:18:42.8017030Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:18:42.8017603Z env:
2026-09-09T19:18:42.8017898Z   LC_ALL: C
2026-09-09T19:18:42.8018199Z   LANG: C
2026-09-09T19:18:42.8018494Z   TZ: UTC
2026-09-09T19:18:42.8018796Z   SAFE_MODE: 1
2026-09-09T19:18:42.8019131Z   ALLOW_NETWORK: 0
2026-09-09T19:18:42.8019460Z   APP_ENV: dev
2026-09-09T19:18:42.8020003Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:18:42.8020539Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:18:42.8021276Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:18:42.8022014Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:18:42.8022665Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:18:42.8023324Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:18:42.8023993Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:18:42.8024552Z ##[endgroup]
2026-09-09T19:18:43.0493656Z Preparing worktree (detached HEAD 75ddaf2c)
2026-09-09T19:18:43.4007167Z HEAD is now at 75ddaf2c Fix Markdown-escaped token reading in CI owner validation
2026-09-09T19:18:44.4906865Z ....................................................                     [100%]
2026-09-09T19:18:44.4907926Z 52 passed in 0.60s
2026-09-09T19:20:13.7847034Z /home/runner/work/_temp/hde-release-attestation/attestation.json
2026-09-09T19:20:14.3955149Z /home/runner/work/_temp/hde-release-attestation/attestation.json
2026-09-09T19:20:14.4583390Z ##[group]Run set -uo pipefail
2026-09-09T19:20:14.4583746Z [36;1mset -uo pipefail[0m
2026-09-09T19:20:14.4583976Z [36;1mfailed=0[0m
2026-09-09T19:20:14.4584164Z [36;1m[0m
2026-09-09T19:20:14.4584350Z [36;1mrequire_outcome() {[0m
2026-09-09T19:20:14.4584577Z [36;1m  flag=$1[0m
2026-09-09T19:20:14.4584779Z [36;1m  outcome=$2[0m
2026-09-09T19:20:14.4584978Z [36;1m  label=$3[0m
2026-09-09T19:20:14.4585249Z [36;1m  if [[ "$flag" == "true" && "$outcome" != "success" ]]; then[0m
2026-09-09T19:20:14.4585683Z [36;1m    echo "APPLICABLE_CI_LANE_NOT_SUCCESSFUL:$label:$outcome" >&2[0m
2026-09-09T19:20:14.4586043Z [36;1m    failed=1[0m
2026-09-09T19:20:14.4586328Z [36;1m  elif [[ "$flag" == "false" && "$outcome" != "skipped" ]]; then[0m
2026-09-09T19:20:14.4586959Z [36;1m    echo "INAPPLICABLE_CI_LANE_NOT_SKIPPED:$label:$outcome" >&2[0m
2026-09-09T19:20:14.4587310Z [36;1m    failed=1[0m
2026-09-09T19:20:14.4587602Z [36;1m  elif [[ "$flag" != "true" && "$flag" != "false" ]]; then[0m
2026-09-09T19:20:14.4587988Z [36;1m    echo "CI_LANE_APPLICABILITY_INVALID:$label:$flag" >&2[0m
2026-09-09T19:20:14.4588307Z [36;1m    failed=1[0m
2026-09-09T19:20:14.4588503Z [36;1m  fi[0m
2026-09-09T19:20:14.4588682Z [36;1m}[0m
2026-09-09T19:20:14.4588854Z [36;1m[0m
2026-09-09T19:20:14.4589074Z [36;1mif [[ "$CLASSIFY_OUTCOME" != "success" ]]; then[0m
2026-09-09T19:20:14.4589492Z [36;1m  echo "CI_CHANGE_CLASSIFICATION_NOT_SUCCESSFUL:$CLASSIFY_OUTCOME" >&2[0m
2026-09-09T19:20:14.4590235Z [36;1m  failed=1[0m
2026-09-09T19:20:14.4590433Z [36;1mfi[0m
2026-09-09T19:20:14.4590739Z [36;1mrequire_outcome "$NEEDS_PYTHON" "$PYTHON_SETUP_OUTCOME" python-setup[0m
2026-09-09T19:20:14.4591227Z [36;1mrequire_outcome "$NEEDS_PYTHON" "$DEPENDENCIES_OUTCOME" dependencies[0m
2026-09-09T19:20:14.4591745Z [36;1mrequire_outcome "$NEEDS_PYTHON" "$PYTEST_READINESS_OUTCOME" pytest-readiness[0m
2026-09-09T19:20:14.4592257Z [36;1mrequire_outcome "$NEEDS_PYTHON" "$ENV_PINS_OUTCOME" environment-pins[0m
2026-09-09T19:20:14.4592742Z [36;1mrequire_outcome "$CHANGED_TESTS" "$CHANGED_TESTS_OUTCOME" changed-tests[0m
2026-09-09T19:20:14.4593195Z [36;1mrequire_outcome "$PRODUCT" "$PRODUCT_OUTCOME" product[0m
2026-09-09T19:20:14.4593621Z [36;1mrequire_outcome "$COMPAT" "$COMPAT_OUTCOME" compatibility[0m
2026-09-09T19:20:14.4594007Z [36;1mrequire_outcome "$DB" "$DB_OUTCOME" database[0m
2026-09-09T19:20:14.4594350Z [36;1mrequire_outcome "$RAILS" "$RAILS_OUTCOME" rails[0m
2026-09-09T19:20:14.4594727Z [36;1mrequire_outcome "$EVIDENCE" "$EVIDENCE_OUTCOME" evidence[0m
2026-09-09T19:20:14.4595087Z [36;1mrequire_outcome "$QA" "$QA_OUTCOME" qa[0m
2026-09-09T19:20:14.4595434Z [36;1mrequire_outcome "$RELEASE" "$RELEASE_OUTCOME" release[0m
2026-09-09T19:20:14.4595746Z [36;1m[0m
2026-09-09T19:20:14.4595949Z [36;1mgit diff --check || failed=1[0m
2026-09-09T19:20:14.4596216Z [36;1mgit diff --exit-code || failed=1[0m
2026-09-09T19:20:14.4596548Z [36;1mstatus=$(git status --short --untracked-files=all)[0m
2026-09-09T19:20:14.4596876Z [36;1mif [[ -n "$status" ]]; then[0m
2026-09-09T19:20:14.4597153Z [36;1m  echo "CI_CANDIDATE_TREE_NOT_CLEAN" >&2[0m
2026-09-09T19:20:14.4597437Z [36;1m  echo "$status" >&2[0m
2026-09-09T19:20:14.4597657Z [36;1m  failed=1[0m
2026-09-09T19:20:14.4597849Z [36;1mfi[0m
2026-09-09T19:20:14.4598035Z [36;1mif (( failed != 0 )); then[0m
2026-09-09T19:20:14.4598268Z [36;1m  exit 1[0m
2026-09-09T19:20:14.4598458Z [36;1mfi[0m
2026-09-09T19:20:14.4598677Z [36;1mecho "CI_APPLICABILITY_AND_EXACT_HEAD_OK"[0m
2026-09-09T19:20:14.4633919Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
2026-09-09T19:20:14.4634263Z env:
2026-09-09T19:20:14.4634443Z   LC_ALL: C
2026-09-09T19:20:14.4634615Z   LANG: C
2026-09-09T19:20:14.4634780Z   TZ: UTC
2026-09-09T19:20:14.4634953Z   SAFE_MODE: 1
2026-09-09T19:20:14.4635136Z   ALLOW_NETWORK: 0
2026-09-09T19:20:14.4635323Z   APP_ENV: dev
2026-09-09T19:20:14.4635532Z   PYTHONDONTWRITEBYTECODE: 1
2026-09-09T19:20:14.4636051Z   pythonLocation: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:20:14.4636506Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib/pkgconfig
2026-09-09T19:20:14.4636941Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:20:14.4637315Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:20:14.4637712Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.14/x64
2026-09-09T19:20:14.4638105Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.14/x64/lib
2026-09-09T19:20:14.4638506Z   CLASSIFY_OUTCOME: success
2026-09-09T19:20:14.4638748Z   NEEDS_PYTHON: true
2026-09-09T19:20:14.4638959Z   PYTHON_SETUP_OUTCOME: success
2026-09-09T19:20:14.4639198Z   DEPENDENCIES_OUTCOME: success
2026-09-09T19:20:14.4639437Z   PYTEST_READINESS_OUTCOME: success
2026-09-09T19:20:14.4640076Z   ENV_PINS_OUTCOME: success
2026-09-09T19:20:14.4640295Z   CHANGED_TESTS: true
2026-09-09T19:20:14.4640508Z   CHANGED_TESTS_OUTCOME: success
2026-09-09T19:20:14.4640734Z   PRODUCT: true
2026-09-09T19:20:14.4640933Z   PRODUCT_OUTCOME: success
2026-09-09T19:20:14.4641150Z   COMPAT: true
2026-09-09T19:20:14.4641336Z   COMPAT_OUTCOME: success
2026-09-09T19:20:14.4641540Z   DB: true
2026-09-09T19:20:14.4641714Z   DB_OUTCOME: success
2026-09-09T19:20:14.4641907Z   RAILS: true
2026-09-09T19:20:14.4642096Z   RAILS_OUTCOME: success
2026-09-09T19:20:14.4642302Z   EVIDENCE: true
2026-09-09T19:20:14.4642494Z   EVIDENCE_OUTCOME: success
2026-09-09T19:20:14.4642700Z   QA: true
2026-09-09T19:20:14.4642867Z   QA_OUTCOME: success
2026-09-09T19:20:14.4643056Z   RELEASE: true
2026-09-09T19:20:14.4643243Z   RELEASE_OUTCOME: success
2026-09-09T19:20:14.4643460Z ##[endgroup]
2026-09-09T19:20:14.5170087Z CI_APPLICABILITY_AND_EXACT_HEAD_OK
2026-09-09T19:20:14.5261541Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-09-09T19:20:14.5262816Z Post job cleanup.
2026-09-09T19:20:14.6507394Z (node:9398) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-09-09T19:20:14.6508955Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-09-09T19:20:14.6726994Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-09-09T19:20:14.6729310Z Post job cleanup.
2026-09-09T19:20:14.8351982Z [command]/usr/bin/git version
2026-09-09T19:20:14.8352459Z git version 2.55.0
2026-09-09T19:20:14.8356816Z Temporarily overriding HOME='/home/runner/work/_temp/39561d1b-f133-4725-b2de-522d63cc8e41' before making global git config changes
2026-09-09T19:20:14.8358120Z Adding repository directory to the temporary git global config as a safe directory
2026-09-09T19:20:14.8359283Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/glow-hdengine-v2/glow-hdengine-v2
2026-09-09T19:20:14.8374828Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-09-09T19:20:14.8411663Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-09-09T19:20:14.8636468Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-09-09T19:20:14.8671846Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-09-09T19:20:14.8894550Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-09-09T19:20:14.8930993Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-09-09T19:20:14.9283672Z Cleaning up orphan processes
2026-09-09T19:20:14.9551837Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

```

## Actual fsync finding and evidence-backed disposition

The corrected-head formal review5158828852 reported EIO on its own overlay. This is retained as an actual review-environment limitation; root compared the unchanged baseline flush/fsync/replace sequence, selected Plan§5.2step8, existing failure-injection proof, successful local scratch-only probes and actual CI. No code change or waiver follows. Complete posted disposition (source JSON SHA-256 7d210832c5b0252a3d9b383a41599900ddde94592750dc6b2cace4d5e7b9e65b):

```json
{
  "body": "Disposition of [review 5158828852](https://github.com/amthorn78/glow-hdengine-v2/pull/403#pullrequestreview-5158828852): **not accepted as a code defect; retain the reported EIO as a limitation of that review environment.** No source change or waiver.\n\nThe exact base commit already calls `handle.flush(); os.fsync(handle.fileno())` before `os.replace` in [`_publish_staged`](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/tools/evidence/update_evidence_index.py#L4063-L4074). This durability call was not introduced by PR403. Selected Detailed Plan v1.1 (`libfile_7960d01d117881919c0004545ae3a4d7`, §5.2 step8) expressly requires same-directory temporary files, flush/fsync and replacement; its recovery duty refuses partial success.\n\nAn EIO reports a synchronization/writeback error, not a safe signal to skip the operation ([Linux man-pages](https://man7.org/linux/man-pages/man2/fsync.2.html)). Silently falling through to replacement would conceal that error. The existing [failure-injection proof](https://github.com/amthorn78/glow-hdengine-v2/blob/75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950/tests/config/test_config_artifacts.py#L308-L378) verifies that fsync failure precedes replacement, preserves the same exception and restores bytes/mode/mtime.\n\nIndependent one-byte regular-file probes in this engineering environment succeeded in both `/tmp` and task scratch at2026-09-09T19:24:34.144941Z. This does not dispute the reviewer's distinct overlay failure. Actual coordinated publication, deterministic repeat and owner checks succeeded here; [current-head CI34393325625](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34393325625) passed all seven lanes, including1544 affected tests,111 evidence-lane tests and clean release-attestation build/verify. Recovery of the reported I/O inability belongs to that execution environment. The governed writer keeps its existing fail-closed behavior.",
  "capture": "2026-09-09T19:28:31.335Z",
  "id": 5607519817
}
```


## Final native Result save and complete readback

### pr30-result-native-save.json

```json
{
  "capture": "2026-09-09T19:54:36.069Z",
  "current_version_number": 0,
  "directory_id": "6a502af02b9c81918905db1026c9b0c4",
  "external_connectors_accessed": false,
  "file_id": "file_00000000427c81f4a2281be36da6e90a",
  "file_name": "HDE-EPIC040-PR01-pr-implementation-result-v1.0.md",
  "file_size_bytes": 74622,
  "library_file_id": "libfile_dbc2c204e99c8191a4179b022697bb00",
  "mime_type": "text/markdown",
  "operation": "create_library_file",
  "path": "/Glow HDE 3.0/HDE-EPIC040-PR01-pr-implementation-result-v1.0.md",
  "restored_from_version_number": null,
  "status": "succeeded",
  "xattrs": [
    {
      "name": "user.library-file-version",
      "value": "0"
    }
  ]
}
```

### pr30-result-saved-byte-verification.json

```json
{
  "verified_at": "2026-09-09T19:55:06.985370Z",
  "library_file_id": "libfile_dbc2c204e99c8191a4179b022697bb00",
  "logical_identity": "HDE-EPIC040-PR01-PR-IMPLEMENTATION-RESULT v1.0",
  "state": "MERGE_PENDING",
  "bytes": 74622,
  "lines": 402,
  "sha256": "5dc65f1a775f34fb92d9afa79b3d788258b2f6daedaf1df52657052f6f7b8551",
  "all_saved_bytes_match": true,
  "identity_state_next_consumer_verified": true,
  "materialized_path": "/workspace/scratch/545715ad0e8a/verified-pr30-result-v1/HDE-EPIC040-PR01-pr-implementation-result-v1.0.md"
}
```

The complete 74,622 saved bytes match the authored Result exactly. The Result carries its full requirement allocation, complete Canon register, 67-path attribution, actual engineering findings and test/review/CI outcomes. Its next consumer is the retained whole-change IA through conditional PR-40 after actual Product Owner manual merge; the intervening Analyzer is run only when manually invoked in the retained PR01 conversation. No merge, Analyzer or PR-40 was executed.

## Complete final native engineering evidence

Captured 2026-09-09T19:45:33.404Z. Terminal pages contain eight issue comments, one formal review, no inline comments/threads, two commits, one completed successful check and zero legacy status contexts. The empty legacy aggregate label `pending` is not an observed pending check. Code and security review summaries bind the current head. Both equivalent fsync disposition comments are retained as one finding history. The reviewer private task report was not opened; the native public PR security outcome explicitly reports no findings.

```json
{
  "capture": "2026-09-09T19:45:33.404Z",
  "checks": {
    "check_runs": [
      {
        "app": {
          "client_id": "Iv1.05c79e9ad1f6bdfa",
          "created_at": "2018-07-30T09:30:17Z",
          "description": "Automate your workflow from idea to production",
          "events": [
            "branch_protection_rule",
            "check_run",
            "check_suite",
            "create",
            "delete",
            "deployment",
            "deployment_status",
            "discussion",
            "discussion_comment",
            "fork",
            "gollum",
            "issues",
            "issue_comment",
            "label",
            "merge_group",
            "milestone",
            "page_build",
            "public",
            "pull_request",
            "pull_request_review",
            "pull_request_review_comment",
            "push",
            "registry_package",
            "release",
            "repository",
            "repository_dispatch",
            "status",
            "watch",
            "workflow_dispatch",
            "workflow_run"
          ],
          "external_url": "https://help.github.com/en/actions",
          "html_url": "https://github.com/apps/github-actions",
          "id": 15368,
          "name": "GitHub Actions",
          "node_id": "MDM6QXBwMTUzNjg=",
          "owner": {
            "avatar_url": "https://avatars.githubusercontent.com/u/9919?v=4",
            "events_url": "https://api.github.com/users/github/events{/privacy}",
            "followers_url": "https://api.github.com/users/github/followers",
            "following_url": "https://api.github.com/users/github/following{/other_user}",
            "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
            "gravatar_id": "",
            "html_url": "https://github.com/github",
            "id": 9919,
            "login": "github",
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjk5MTk=",
            "organizations_url": "https://api.github.com/users/github/orgs",
            "received_events_url": "https://api.github.com/users/github/received_events",
            "repos_url": "https://api.github.com/users/github/repos",
            "site_admin": false,
            "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/github/subscriptions",
            "type": "Organization",
            "url": "https://api.github.com/users/github",
            "user_view_type": "public"
          },
          "permissions": {
            "actions": "write",
            "administration": "read",
            "artifact_metadata": "write",
            "attestations": "write",
            "checks": "write",
            "code_quality": "write",
            "contents": "write",
            "copilot_requests": "write",
            "deployments": "write",
            "discussions": "write",
            "drives": "write",
            "issues": "write",
            "merge_queues": "write",
            "metadata": "read",
            "models": "read",
            "packages": "write",
            "pages": "write",
            "pull_requests": "write",
            "repository_hooks": "write",
            "repository_projects": "write",
            "security_events": "write",
            "statuses": "write",
            "vulnerability_alerts": "read"
          },
          "slug": "github-actions",
          "updated_at": "2026-06-18T16:17:48Z"
        },
        "check_suite": {
          "id": 93173457195
        },
        "completed_at": "2026-09-09T19:20:20Z",
        "conclusion": "success",
        "details_url": "https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34393325625/job/102606798665",
        "external_id": "4014ce0d-a6ca-5bfe-b414-fc7ad3dd0009",
        "head_sha": "75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950",
        "html_url": "https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34393325625/job/102606798665",
        "id": 102606798665,
        "name": "test",
        "node_id": "CR_kwDOP103ks8AAAAX49d_SQ",
        "output": {
          "annotations_count": 1,
          "annotations_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/check-runs/102606798665/annotations",
          "summary": null,
          "text": null,
          "title": null
        },
        "pull_requests": [
          {
            "base": {
              "ref": "main",
              "repo": {
                "id": 1063073682,
                "name": "glow-hdengine-v2",
                "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2"
              },
              "sha": "9065e6f0c01ad82a65c78687cd6c55e26ca33a1f"
            },
            "head": {
              "ref": "hde-epic040-pr01-source-contracts",
              "repo": {
                "id": 1063073682,
                "name": "glow-hdengine-v2",
                "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2"
              },
              "sha": "75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950"
            },
            "id": 4488310715,
            "number": 403,
            "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/pulls/403"
          }
        ],
        "started_at": "2026-09-09T19:09:04Z",
        "status": "completed",
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/check-runs/102606798665"
      }
    ],
    "total_count": 1
  },
  "comments": [
    {
      "author_association": "NONE",
      "body": "<!-- codex-pull-request-review-summary -->\n<!-- codex-security-review:v1 {\"blockingSeverityThreshold\":\"P0\",\"headSha\":\"75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950\",\"mergeGateEnabled\":false,\"pullRequestNumber\":403,\"repository\":\"amthorn78/glow-hdengine-v2\",\"status\":\"completed\"} -->\n## Codex Review Summary\n\nThis comment shows the latest Codex review activity on this pull request.\n\n| Review | Status | Commit | Review trigger |\n| --- | --- | --- | --- |\n| 📝 **Code Review** | ✅ **Completed** <relative-time datetime=\"2026-09-09T19:23:36.540273Z\">2026-09-09T19:23:36.540273Z</relative-time> | `75ddaf2` | Manual request |\n| 🔒 **Security Review** | ✅ **Completed** <relative-time datetime=\"2026-09-09T19:44:19.975498Z\">2026-09-09T19:44:19.975498Z</relative-time> | `75ddaf2` | Manual request |\n\n\n\n<details> <summary>ℹ️ About Codex in GitHub</summary>\n<br/>\n\n[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you\n- Open a pull request for review\n- Mark a draft as ready\n- Comment \"@codex review\" or \"@codex security review\".\n\nCodex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.\n\n</details>",
      "created_at": "2026-09-09T18:51:03Z",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607057536",
      "id": 5607057536,
      "issue_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/403",
      "minimized": null,
      "node_id": "IC_kwDOP103ks8AAAABTjTogA",
      "performed_via_github_app": {
        "client_id": "Iv23liVemv8A9if9v0F2",
        "created_at": "2025-02-14T01:37:05Z",
        "description": "Bring ChatGPT and Codex to your GitHub repositories.",
        "events": [
          "check_run",
          "check_suite",
          "commit_comment",
          "issues",
          "issue_comment",
          "pull_request",
          "pull_request_review",
          "pull_request_review_comment",
          "pull_request_review_thread",
          "repository",
          "status",
          "sub_issues"
        ],
        "external_url": "https://www.chatgpt.com",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 1144995,
        "name": "ChatGPT Codex Connector",
        "node_id": "A_kwHOAOQ6Gs4AEXij",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/14957082?v=4",
          "events_url": "https://api.github.com/users/openai/events{/privacy}",
          "followers_url": "https://api.github.com/users/openai/followers",
          "following_url": "https://api.github.com/users/openai/following{/other_user}",
          "gists_url": "https://api.github.com/users/openai/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/openai",
          "id": 14957082,
          "login": "openai",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0OTU3MDgy",
          "organizations_url": "https://api.github.com/users/openai/orgs",
          "received_events_url": "https://api.github.com/users/openai/received_events",
          "repos_url": "https://api.github.com/users/openai/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/openai/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/openai/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/openai",
          "user_view_type": "public"
        },
        "permissions": {
          "actions": "write",
          "checks": "read",
          "contents": "write",
          "emails": "read",
          "issues": "write",
          "metadata": "read",
          "pull_requests": "write",
          "statuses": "read",
          "workflows": "write"
        },
        "slug": "chatgpt-codex-connector",
        "updated_at": "2026-04-20T16:37:15Z"
      },
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607057536/reactions"
      },
      "updated_at": "2026-09-09T19:44:20Z",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607057536",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/in/1144995?v=4",
        "events_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/events{/privacy}",
        "followers_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 199175422,
        "login": "chatgpt-codex-connector[bot]",
        "node_id": "BOT_kgDOC98s_g",
        "organizations_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/orgs",
        "received_events_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/received_events",
        "repos_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/subscriptions",
        "type": "Bot",
        "url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D",
        "user_view_type": "public"
      }
    },
    {
      "author_association": "OWNER",
      "body": "@codex review\n\nPlease review the corrected current code at 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950. The correction recognizes Markdown-escaped underscores in the existing token reader and adds owner tests for plain/escaped/mixed names, unknown-token refusal and unchanged raw source hashes. The original CI failure reproduces independently on the base commit; the token is already present in the retained PF04 snapshot. Both mapped owner modules now pass (149 tests). No registry or Canon source changed.",
      "created_at": "2026-09-09T19:09:15Z",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607278348",
      "id": 5607278348,
      "issue_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/403",
      "minimized": null,
      "node_id": "IC_kwDOP103ks8AAAABTjhHDA",
      "performed_via_github_app": {
        "client_id": "Iv23liVemv8A9if9v0F2",
        "created_at": "2025-02-14T01:37:05Z",
        "description": "Bring ChatGPT and Codex to your GitHub repositories.",
        "events": [
          "check_run",
          "check_suite",
          "commit_comment",
          "issues",
          "issue_comment",
          "pull_request",
          "pull_request_review",
          "pull_request_review_comment",
          "pull_request_review_thread",
          "repository",
          "status",
          "sub_issues"
        ],
        "external_url": "https://www.chatgpt.com",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 1144995,
        "name": "ChatGPT Codex Connector",
        "node_id": "A_kwHOAOQ6Gs4AEXij",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/14957082?v=4",
          "events_url": "https://api.github.com/users/openai/events{/privacy}",
          "followers_url": "https://api.github.com/users/openai/followers",
          "following_url": "https://api.github.com/users/openai/following{/other_user}",
          "gists_url": "https://api.github.com/users/openai/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/openai",
          "id": 14957082,
          "login": "openai",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0OTU3MDgy",
          "organizations_url": "https://api.github.com/users/openai/orgs",
          "received_events_url": "https://api.github.com/users/openai/received_events",
          "repos_url": "https://api.github.com/users/openai/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/openai/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/openai/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/openai",
          "user_view_type": "public"
        },
        "permissions": {
          "actions": "write",
          "checks": "read",
          "contents": "write",
          "emails": "read",
          "issues": "write",
          "metadata": "read",
          "pull_requests": "write",
          "statuses": "read",
          "workflows": "write"
        },
        "slug": "chatgpt-codex-connector",
        "updated_at": "2026-04-20T16:37:15Z"
      },
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607278348/reactions"
      },
      "updated_at": "2026-09-09T19:09:15Z",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607278348",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/146120956?v=4",
        "events_url": "https://api.github.com/users/amthorn78/events{/privacy}",
        "followers_url": "https://api.github.com/users/amthorn78/followers",
        "following_url": "https://api.github.com/users/amthorn78/following{/other_user}",
        "gists_url": "https://api.github.com/users/amthorn78/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/amthorn78",
        "id": 146120956,
        "login": "amthorn78",
        "node_id": "U_kgDOCLWg_A",
        "organizations_url": "https://api.github.com/users/amthorn78/orgs",
        "received_events_url": "https://api.github.com/users/amthorn78/received_events",
        "repos_url": "https://api.github.com/users/amthorn78/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/amthorn78/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amthorn78/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/amthorn78",
        "user_view_type": "public"
      }
    },
    {
      "author_association": "OWNER",
      "body": "@codex security review\n\nPlease review the current substantive changes at 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950, including the token-reader correction following the completed initial security review. The reader decodes only Markdown underscore escapes; unknown-token refusal and hashes of the original source bytes remain enforced. No registry or Canon source changed.",
      "created_at": "2026-09-09T19:09:16Z",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607278497",
      "id": 5607278497,
      "issue_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/403",
      "minimized": null,
      "node_id": "IC_kwDOP103ks8AAAABTjhHoQ",
      "performed_via_github_app": {
        "client_id": "Iv23liVemv8A9if9v0F2",
        "created_at": "2025-02-14T01:37:05Z",
        "description": "Bring ChatGPT and Codex to your GitHub repositories.",
        "events": [
          "check_run",
          "check_suite",
          "commit_comment",
          "issues",
          "issue_comment",
          "pull_request",
          "pull_request_review",
          "pull_request_review_comment",
          "pull_request_review_thread",
          "repository",
          "status",
          "sub_issues"
        ],
        "external_url": "https://www.chatgpt.com",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 1144995,
        "name": "ChatGPT Codex Connector",
        "node_id": "A_kwHOAOQ6Gs4AEXij",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/14957082?v=4",
          "events_url": "https://api.github.com/users/openai/events{/privacy}",
          "followers_url": "https://api.github.com/users/openai/followers",
          "following_url": "https://api.github.com/users/openai/following{/other_user}",
          "gists_url": "https://api.github.com/users/openai/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/openai",
          "id": 14957082,
          "login": "openai",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0OTU3MDgy",
          "organizations_url": "https://api.github.com/users/openai/orgs",
          "received_events_url": "https://api.github.com/users/openai/received_events",
          "repos_url": "https://api.github.com/users/openai/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/openai/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/openai/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/openai",
          "user_view_type": "public"
        },
        "permissions": {
          "actions": "write",
          "checks": "read",
          "contents": "write",
          "emails": "read",
          "issues": "write",
          "metadata": "read",
          "pull_requests": "write",
          "statuses": "read",
          "workflows": "write"
        },
        "slug": "chatgpt-codex-connector",
        "updated_at": "2026-04-20T16:37:15Z"
      },
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607278497/reactions"
      },
      "updated_at": "2026-09-09T19:09:16Z",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607278497",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/146120956?v=4",
        "events_url": "https://api.github.com/users/amthorn78/events{/privacy}",
        "followers_url": "https://api.github.com/users/amthorn78/followers",
        "following_url": "https://api.github.com/users/amthorn78/following{/other_user}",
        "gists_url": "https://api.github.com/users/amthorn78/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/amthorn78",
        "id": 146120956,
        "login": "amthorn78",
        "node_id": "U_kgDOCLWg_A",
        "organizations_url": "https://api.github.com/users/amthorn78/orgs",
        "received_events_url": "https://api.github.com/users/amthorn78/received_events",
        "repos_url": "https://api.github.com/users/amthorn78/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/amthorn78/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amthorn78/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/amthorn78",
        "user_view_type": "public"
      }
    },
    {
      "author_association": "NONE",
      "body": "Codex Review: Didn't find any major issues. :tada:\n\n**Reviewed commit:** `75ddaf2c94`\n\n<details> <summary>ℹ️ About Codex in GitHub</summary>\n<br/>\n\n[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you\n- Open a pull request for review\n- Mark a draft as ready\n- Comment \"@codex review\".\n\nIf Codex has suggestions, it will comment; otherwise it will react with 👍.\n\n\n\n\nCodex can also answer questions or update the PR. Try commenting \"@codex address that feedback\".\n            \n</details>",
      "created_at": "2026-09-09T19:23:35Z",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607455190",
      "id": 5607455190,
      "issue_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/403",
      "minimized": null,
      "node_id": "IC_kwDOP103ks8AAAABTjr51g",
      "performed_via_github_app": {
        "client_id": "Iv23liVemv8A9if9v0F2",
        "created_at": "2025-02-14T01:37:05Z",
        "description": "Bring ChatGPT and Codex to your GitHub repositories.",
        "events": [
          "check_run",
          "check_suite",
          "commit_comment",
          "issues",
          "issue_comment",
          "pull_request",
          "pull_request_review",
          "pull_request_review_comment",
          "pull_request_review_thread",
          "repository",
          "status",
          "sub_issues"
        ],
        "external_url": "https://www.chatgpt.com",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 1144995,
        "name": "ChatGPT Codex Connector",
        "node_id": "A_kwHOAOQ6Gs4AEXij",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/14957082?v=4",
          "events_url": "https://api.github.com/users/openai/events{/privacy}",
          "followers_url": "https://api.github.com/users/openai/followers",
          "following_url": "https://api.github.com/users/openai/following{/other_user}",
          "gists_url": "https://api.github.com/users/openai/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/openai",
          "id": 14957082,
          "login": "openai",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0OTU3MDgy",
          "organizations_url": "https://api.github.com/users/openai/orgs",
          "received_events_url": "https://api.github.com/users/openai/received_events",
          "repos_url": "https://api.github.com/users/openai/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/openai/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/openai/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/openai",
          "user_view_type": "public"
        },
        "permissions": {
          "actions": "write",
          "checks": "read",
          "contents": "write",
          "emails": "read",
          "issues": "write",
          "metadata": "read",
          "pull_requests": "write",
          "statuses": "read",
          "workflows": "write"
        },
        "slug": "chatgpt-codex-connector",
        "updated_at": "2026-04-20T16:37:15Z"
      },
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607455190/reactions"
      },
      "updated_at": "2026-09-09T19:23:35Z",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607455190",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/in/1144995?v=4",
        "events_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/events{/privacy}",
        "followers_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 199175422,
        "login": "chatgpt-codex-connector[bot]",
        "node_id": "BOT_kgDOC98s_g",
        "organizations_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/orgs",
        "received_events_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/received_events",
        "repos_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/subscriptions",
        "type": "Bot",
        "url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D",
        "user_view_type": "public"
      }
    },
    {
      "author_association": "OWNER",
      "body": "@codex security review",
      "created_at": "2026-09-09T19:26:01Z",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607488213",
      "id": 5607488213,
      "issue_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/403",
      "minimized": null,
      "node_id": "IC_kwDOP103ks8AAAABTjt61Q",
      "performed_via_github_app": {
        "client_id": "Iv23liVemv8A9if9v0F2",
        "created_at": "2025-02-14T01:37:05Z",
        "description": "Bring ChatGPT and Codex to your GitHub repositories.",
        "events": [
          "check_run",
          "check_suite",
          "commit_comment",
          "issues",
          "issue_comment",
          "pull_request",
          "pull_request_review",
          "pull_request_review_comment",
          "pull_request_review_thread",
          "repository",
          "status",
          "sub_issues"
        ],
        "external_url": "https://www.chatgpt.com",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 1144995,
        "name": "ChatGPT Codex Connector",
        "node_id": "A_kwHOAOQ6Gs4AEXij",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/14957082?v=4",
          "events_url": "https://api.github.com/users/openai/events{/privacy}",
          "followers_url": "https://api.github.com/users/openai/followers",
          "following_url": "https://api.github.com/users/openai/following{/other_user}",
          "gists_url": "https://api.github.com/users/openai/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/openai",
          "id": 14957082,
          "login": "openai",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0OTU3MDgy",
          "organizations_url": "https://api.github.com/users/openai/orgs",
          "received_events_url": "https://api.github.com/users/openai/received_events",
          "repos_url": "https://api.github.com/users/openai/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/openai/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/openai/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/openai",
          "user_view_type": "public"
        },
        "permissions": {
          "actions": "write",
          "checks": "read",
          "contents": "write",
          "emails": "read",
          "issues": "write",
          "metadata": "read",
          "pull_requests": "write",
          "statuses": "read",
          "workflows": "write"
        },
        "slug": "chatgpt-codex-connector",
        "updated_at": "2026-04-20T16:37:15Z"
      },
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607488213/reactions"
      },
      "updated_at": "2026-09-09T19:26:01Z",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607488213",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/146120956?v=4",
        "events_url": "https://api.github.com/users/amthorn78/events{/privacy}",
        "followers_url": "https://api.github.com/users/amthorn78/followers",
        "following_url": "https://api.github.com/users/amthorn78/following{/other_user}",
        "gists_url": "https://api.github.com/users/amthorn78/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/amthorn78",
        "id": 146120956,
        "login": "amthorn78",
        "node_id": "U_kgDOCLWg_A",
        "organizations_url": "https://api.github.com/users/amthorn78/orgs",
        "received_events_url": "https://api.github.com/users/amthorn78/received_events",
        "repos_url": "https://api.github.com/users/amthorn78/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/amthorn78/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amthorn78/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/amthorn78",
        "user_view_type": "public"
      }
    },
    {
      "author_association": "OWNER",
      "body": "Disposition of [review 5158828852](https://github.com/amthorn78/glow-hdengine-v2/pull/403#pullrequestreview-5158828852): **not accepted as a code defect; retain the reported EIO as a limitation of that review environment.** No source change or waiver.\n\nThe exact base commit already calls `handle.flush(); os.fsync(handle.fileno())` before `os.replace` in [`_publish_staged`](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/tools/evidence/update_evidence_index.py#L4063-L4074). This durability call was not introduced by PR403. Selected Detailed Plan v1.1 (`libfile_7960d01d117881919c0004545ae3a4d7`, §5.2 step8) expressly requires same-directory temporary files, flush/fsync and replacement; its recovery duty refuses partial success.\n\nAn EIO reports a synchronization/writeback error, not a safe signal to skip the operation ([Linux man-pages](https://man7.org/linux/man-pages/man2/fsync.2.html)). Silently falling through to replacement would conceal that error. The existing [failure-injection proof](https://github.com/amthorn78/glow-hdengine-v2/blob/75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950/tests/config/test_config_artifacts.py#L308-L378) verifies that fsync failure precedes replacement, preserves the same exception and restores bytes/mode/mtime.\n\nIndependent one-byte regular-file probes in this engineering environment succeeded in both `/tmp` and task scratch at2026-09-09T19:24:34.144941Z. This does not dispute the reviewer's distinct overlay failure. Actual coordinated publication, deterministic repeat and owner checks succeeded here; [current-head CI34393325625](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34393325625) passed all seven lanes, including1544 affected tests,111 evidence-lane tests and clean release-attestation build/verify. Recovery of the reported I/O inability belongs to that execution environment. The governed writer keeps its existing fail-closed behavior.",
      "created_at": "2026-09-09T19:28:30Z",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607519817",
      "id": 5607519817,
      "issue_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/403",
      "minimized": null,
      "node_id": "IC_kwDOP103ks8AAAABTjv2SQ",
      "performed_via_github_app": {
        "client_id": "Iv23liVemv8A9if9v0F2",
        "created_at": "2025-02-14T01:37:05Z",
        "description": "Bring ChatGPT and Codex to your GitHub repositories.",
        "events": [
          "check_run",
          "check_suite",
          "commit_comment",
          "issues",
          "issue_comment",
          "pull_request",
          "pull_request_review",
          "pull_request_review_comment",
          "pull_request_review_thread",
          "repository",
          "status",
          "sub_issues"
        ],
        "external_url": "https://www.chatgpt.com",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 1144995,
        "name": "ChatGPT Codex Connector",
        "node_id": "A_kwHOAOQ6Gs4AEXij",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/14957082?v=4",
          "events_url": "https://api.github.com/users/openai/events{/privacy}",
          "followers_url": "https://api.github.com/users/openai/followers",
          "following_url": "https://api.github.com/users/openai/following{/other_user}",
          "gists_url": "https://api.github.com/users/openai/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/openai",
          "id": 14957082,
          "login": "openai",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0OTU3MDgy",
          "organizations_url": "https://api.github.com/users/openai/orgs",
          "received_events_url": "https://api.github.com/users/openai/received_events",
          "repos_url": "https://api.github.com/users/openai/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/openai/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/openai/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/openai",
          "user_view_type": "public"
        },
        "permissions": {
          "actions": "write",
          "checks": "read",
          "contents": "write",
          "emails": "read",
          "issues": "write",
          "metadata": "read",
          "pull_requests": "write",
          "statuses": "read",
          "workflows": "write"
        },
        "slug": "chatgpt-codex-connector",
        "updated_at": "2026-04-20T16:37:15Z"
      },
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607519817/reactions"
      },
      "updated_at": "2026-09-09T19:28:30Z",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607519817",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/146120956?v=4",
        "events_url": "https://api.github.com/users/amthorn78/events{/privacy}",
        "followers_url": "https://api.github.com/users/amthorn78/followers",
        "following_url": "https://api.github.com/users/amthorn78/following{/other_user}",
        "gists_url": "https://api.github.com/users/amthorn78/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/amthorn78",
        "id": 146120956,
        "login": "amthorn78",
        "node_id": "U_kgDOCLWg_A",
        "organizations_url": "https://api.github.com/users/amthorn78/orgs",
        "received_events_url": "https://api.github.com/users/amthorn78/received_events",
        "repos_url": "https://api.github.com/users/amthorn78/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/amthorn78/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amthorn78/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/amthorn78",
        "user_view_type": "public"
      }
    },
    {
      "author_association": "OWNER",
      "body": "Disposition of review 5158828852 (fsync/EIO): NOT_ACCEPTED_AS_CODE_DEFECT; no code change. The reported failure on the review environment is retained as an execution-environment limitation, rather than disputed or treated as a passing test.\n\nThe cited operation is already present in the exact base commit, not newly added by this PR: [baseline `_publish_staged`](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/tools/evidence/update_evidence_index.py#L4063-L4068) writes, flushes and fsyncs before replacement. The PO-selected Detailed Plan v1.1 (`libfile_7960d01d117881919c0004545ae3a4d7`, SHA-256 `a77d453aa2a8b50b8e559cb8f6e5e2098f667760802366646f539a772769916e`) §5.2 step 8 explicitly retains same-directory temporary files, flush/fsync and os.replace; §5.3 requires failure restoration.\n\n[EIO is a synchronization/writeback error](https://man7.org/linux/man-pages/man2/fsync.2.html), not a generic unsupported-operation signal. Ignoring it would allow publication after a real storage failure. [The existing adverse proof](https://github.com/amthorn78/glow-hdengine-v2/blob/75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950/tests/config/test_config_artifacts.py#L308-L378) checks that fsync failure occurs before replacement, propagates the identical original exception and restores bytes/mode/mtime.\n\nAn independent one-byte NamedTemporaryFile probe (write/flush/fsync/readback) succeeded here in both /tmp and the scratch evidence directory at 2026-09-09T19:24:34.144941Z; it does not certify the reviewer's distinct overlay. Actual coordinated publication succeeded, and [current-head CI](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34393325625) passed all seven lanes, including 1,544 affected tests, the 111-test evidence lane and clean release build/verify. No failure was suppressed and no waiver is supplied. The affected review environment needs working file synchronization to execute this existing writer contract; this PR does not claim every filesystem is capable or change that contract.",
      "created_at": "2026-09-09T19:34:54Z",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607603260",
      "id": 5607603260,
      "issue_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/403",
      "minimized": null,
      "node_id": "IC_kwDOP103ks8AAAABTj08PA",
      "performed_via_github_app": {
        "client_id": "Iv23liVemv8A9if9v0F2",
        "created_at": "2025-02-14T01:37:05Z",
        "description": "Bring ChatGPT and Codex to your GitHub repositories.",
        "events": [
          "check_run",
          "check_suite",
          "commit_comment",
          "issues",
          "issue_comment",
          "pull_request",
          "pull_request_review",
          "pull_request_review_comment",
          "pull_request_review_thread",
          "repository",
          "status",
          "sub_issues"
        ],
        "external_url": "https://www.chatgpt.com",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 1144995,
        "name": "ChatGPT Codex Connector",
        "node_id": "A_kwHOAOQ6Gs4AEXij",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/14957082?v=4",
          "events_url": "https://api.github.com/users/openai/events{/privacy}",
          "followers_url": "https://api.github.com/users/openai/followers",
          "following_url": "https://api.github.com/users/openai/following{/other_user}",
          "gists_url": "https://api.github.com/users/openai/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/openai",
          "id": 14957082,
          "login": "openai",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0OTU3MDgy",
          "organizations_url": "https://api.github.com/users/openai/orgs",
          "received_events_url": "https://api.github.com/users/openai/received_events",
          "repos_url": "https://api.github.com/users/openai/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/openai/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/openai/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/openai",
          "user_view_type": "public"
        },
        "permissions": {
          "actions": "write",
          "checks": "read",
          "contents": "write",
          "emails": "read",
          "issues": "write",
          "metadata": "read",
          "pull_requests": "write",
          "statuses": "read",
          "workflows": "write"
        },
        "slug": "chatgpt-codex-connector",
        "updated_at": "2026-04-20T16:37:15Z"
      },
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607603260/reactions"
      },
      "updated_at": "2026-09-09T19:34:54Z",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607603260",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/u/146120956?v=4",
        "events_url": "https://api.github.com/users/amthorn78/events{/privacy}",
        "followers_url": "https://api.github.com/users/amthorn78/followers",
        "following_url": "https://api.github.com/users/amthorn78/following{/other_user}",
        "gists_url": "https://api.github.com/users/amthorn78/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/amthorn78",
        "id": 146120956,
        "login": "amthorn78",
        "node_id": "U_kgDOCLWg_A",
        "organizations_url": "https://api.github.com/users/amthorn78/orgs",
        "received_events_url": "https://api.github.com/users/amthorn78/received_events",
        "repos_url": "https://api.github.com/users/amthorn78/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/amthorn78/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amthorn78/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/amthorn78",
        "user_view_type": "public"
      }
    },
    {
      "author_association": "NONE",
      "body": "### 🛡️ Codex Security Review\n\nSecurity review completed. No security issues were found in this pull request.\n\n**Reviewed commit:** `75ddaf2c94`\n\n[View security finding report](https://chatgpt.com/codex/cloud/tasks/task_e_6aa1b2cff3ec832d8f38bee495faba2d)\n\n_Only the user who started this review can view the report in Codex._\n\n<details> <summary>ℹ️ About Codex security reviews in GitHub</summary>\n<br/>\n\nThis is an experimental Codex feature. Security reviews are triggered when:\n- You comment \"@codex security review\"\n- A regular code review gets triggered (for example, \"@codex review\" or when a PR is opened), and you’re opted in so security review runs alongside code review\n\nOnce complete, Codex will leave suggestions, or a comment if no findings are found.\n\n\n</details>",
      "created_at": "2026-09-09T19:44:18Z",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607726236",
      "id": 5607726236,
      "issue_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/403",
      "minimized": null,
      "node_id": "IC_kwDOP103ks8AAAABTj8cnA",
      "performed_via_github_app": {
        "client_id": "Iv23liVemv8A9if9v0F2",
        "created_at": "2025-02-14T01:37:05Z",
        "description": "Bring ChatGPT and Codex to your GitHub repositories.",
        "events": [
          "check_run",
          "check_suite",
          "commit_comment",
          "issues",
          "issue_comment",
          "pull_request",
          "pull_request_review",
          "pull_request_review_comment",
          "pull_request_review_thread",
          "repository",
          "status",
          "sub_issues"
        ],
        "external_url": "https://www.chatgpt.com",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 1144995,
        "name": "ChatGPT Codex Connector",
        "node_id": "A_kwHOAOQ6Gs4AEXij",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/14957082?v=4",
          "events_url": "https://api.github.com/users/openai/events{/privacy}",
          "followers_url": "https://api.github.com/users/openai/followers",
          "following_url": "https://api.github.com/users/openai/following{/other_user}",
          "gists_url": "https://api.github.com/users/openai/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/openai",
          "id": 14957082,
          "login": "openai",
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE0OTU3MDgy",
          "organizations_url": "https://api.github.com/users/openai/orgs",
          "received_events_url": "https://api.github.com/users/openai/received_events",
          "repos_url": "https://api.github.com/users/openai/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/openai/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/openai/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/openai",
          "user_view_type": "public"
        },
        "permissions": {
          "actions": "write",
          "checks": "read",
          "contents": "write",
          "emails": "read",
          "issues": "write",
          "metadata": "read",
          "pull_requests": "write",
          "statuses": "read",
          "workflows": "write"
        },
        "slug": "chatgpt-codex-connector",
        "updated_at": "2026-04-20T16:37:15Z"
      },
      "reactions": {
        "+1": 0,
        "-1": 0,
        "confused": 0,
        "eyes": 0,
        "heart": 0,
        "hooray": 0,
        "laugh": 0,
        "rocket": 0,
        "total_count": 0,
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607726236/reactions"
      },
      "updated_at": "2026-09-09T19:44:18Z",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments/5607726236",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/in/1144995?v=4",
        "events_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/events{/privacy}",
        "followers_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 199175422,
        "login": "chatgpt-codex-connector[bot]",
        "node_id": "BOT_kgDOC98s_g",
        "organizations_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/orgs",
        "received_events_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/received_events",
        "repos_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/subscriptions",
        "type": "Bot",
        "url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D",
        "user_view_type": "public"
      }
    }
  ],
  "commits": [
    {
      "commit": {
        "author": {
          "date": "2026-09-09T18:49:07Z",
          "email": "146120956+amthorn78@users.noreply.github.com",
          "name": "amthorn78"
        },
        "comment_count": 0,
        "committer": {
          "date": "2026-09-09T18:49:07Z",
          "email": "146120956+amthorn78@users.noreply.github.com",
          "name": "amthorn78"
        },
        "message": "HDE-EPIC040-PR01: source-proven catalog and exact contract data\n\nImplement Detailed PR Plan v1.1 and PR Instruction v2.0 under the PO's PR-30 Proceed. Preserve catalog/schema domains, root-bound projections, coordinated evidence publication and fail-closed CI owners. Include the PO-authorized CRD fixture setup repair.\n\nNo merge, release activation, Ops or QA authorization is implied.",
        "tree": {
          "sha": "543ea921385410c6eda57404b8038b2d90f896e7",
          "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/trees/543ea921385410c6eda57404b8038b2d90f896e7"
        },
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/commits/924ae36a0bfe320f81fc9b6e4fd3891436096f27",
        "verification": {
          "payload": null,
          "reason": "unsigned",
          "signature": null,
          "verified": false,
          "verified_at": null
        }
      },
      "parents": [
        {
          "html_url": "https://github.com/amthorn78/glow-hdengine-v2/commit/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f",
          "sha": "9065e6f0c01ad82a65c78687cd6c55e26ca33a1f",
          "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/commits/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f"
        }
      ],
      "sha": "924ae36a0bfe320f81fc9b6e4fd3891436096f27"
    },
    {
      "commit": {
        "author": {
          "date": "2026-09-09T19:08:26Z",
          "email": "146120956+amthorn78@users.noreply.github.com",
          "name": "amthorn78"
        },
        "comment_count": 0,
        "committer": {
          "date": "2026-09-09T19:08:26Z",
          "email": "146120956+amthorn78@users.noreply.github.com",
          "name": "amthorn78"
        },
        "message": "Fix Markdown-escaped token reading in CI owner validation",
        "tree": {
          "sha": "529306a74268f2a46765bf40defdae49026d103e",
          "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/trees/529306a74268f2a46765bf40defdae49026d103e"
        },
        "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/commits/75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950",
        "verification": {
          "payload": null,
          "reason": "unsigned",
          "signature": null,
          "verified": false,
          "verified_at": null
        }
      },
      "parents": [
        {
          "html_url": "https://github.com/amthorn78/glow-hdengine-v2/commit/924ae36a0bfe320f81fc9b6e4fd3891436096f27",
          "sha": "924ae36a0bfe320f81fc9b6e4fd3891436096f27",
          "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/commits/924ae36a0bfe320f81fc9b6e4fd3891436096f27"
        }
      ],
      "sha": "75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950"
    }
  ],
  "disposition": {
    "comments": [
      5607519817,
      5607603260
    ],
    "review": 5158828852,
    "status": "NOT_ACCEPTED_AS_CODE_DEFECT / REVIEW_ENVIRONMENT_IO_LIMITATION",
    "waiver": null
  },
  "inline": [],
  "legacy_status": {
    "commit_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/commits/75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950",
    "repository": {
      "archive_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/comments{/number}",
      "commits_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/commits{/sha}",
      "compare_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/contributors",
      "deployments_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/deployments",
      "description": "Determinism",
      "downloads_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/downloads",
      "events_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/events",
      "fork": false,
      "forks_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/forks",
      "full_name": "amthorn78/glow-hdengine-v2",
      "git_commits_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/tags{/sha}",
      "hooks_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/hooks",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2",
      "id": 1063073682,
      "issue_comment_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/issues{/number}",
      "keys_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/labels{/name}",
      "languages_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/languages",
      "merges_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/merges",
      "milestones_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/milestones{/number}",
      "name": "glow-hdengine-v2",
      "node_id": "R_kgDOP103kg",
      "notifications_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/notifications{?since,all,participating}",
      "owner": {
        "avatar_url": "https://avatars.githubusercontent.com/u/146120956?v=4",
        "events_url": "https://api.github.com/users/amthorn78/events{/privacy}",
        "followers_url": "https://api.github.com/users/amthorn78/followers",
        "following_url": "https://api.github.com/users/amthorn78/following{/other_user}",
        "gists_url": "https://api.github.com/users/amthorn78/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/amthorn78",
        "id": 146120956,
        "login": "amthorn78",
        "node_id": "U_kgDOCLWg_A",
        "organizations_url": "https://api.github.com/users/amthorn78/orgs",
        "received_events_url": "https://api.github.com/users/amthorn78/received_events",
        "repos_url": "https://api.github.com/users/amthorn78/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/amthorn78/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/amthorn78/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/amthorn78",
        "user_view_type": "public"
      },
      "private": true,
      "pulls_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/pulls{/number}",
      "releases_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/stargazers",
      "statuses_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/subscribers",
      "subscription_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/subscription",
      "tags_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/tags",
      "teams_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/teams",
      "trees_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/git/trees{/sha}",
      "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2"
    },
    "sha": "75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950",
    "state": "pending",
    "statuses": [],
    "total_count": 0,
    "url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/commits/75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950/status"
  },
  "pagination": "All REST collections terminal on page1 withper_page100:8issuecomments,1formalreview,0inlinecomments,2commits,1checkrun,0legacycontexts. Threadtoolcompleteempty.",
  "pr": {
    "base": "9065e6f0c01ad82a65c78687cd6c55e26ca33a1f",
    "branch": "hde-epic040-pr01-source-contracts",
    "changed_files": 67,
    "head": "75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950",
    "merged": false,
    "number": 403,
    "state": "open",
    "url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403"
  },
  "reviews": [
    {
      "_links": {
        "html": {
          "href": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#pullrequestreview-5158828852"
        },
        "pull_request": {
          "href": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/pulls/403"
        }
      },
      "author_association": "NONE",
      "body": "\n### 💡 Codex Review\n\nhttps://github.com/amthorn78/glow-hdengine-v2/blob/75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950/tools/evidence/update_evidence_index.py#L4134\n**<sub><sub>![P1 Badge](https://img.shields.io/badge/P1-orange?style=flat)</sub></sub>  Preserve writes when file fsync is unavailable**\n\nOn the review environment's overlay filesystem, `os.fsync()` on an ordinary temporary file consistently raises `OSError: [Errno 5] Input/output error`; I reproduced this independently with a one-byte `NamedTemporaryFile`. Because every staged publication now unconditionally executes this call before `os.replace`, the canonical updater's write mode is unusable here: the selected suite produced 15 failures and 20 setup errors in evidence-index publication tests, while its read-only `--check` still passed. Retain atomic replacement while accommodating filesystems that do not support the added durability operation so the sole governed writer can still publish the evidence skeleton.\n\nAGENTS.md reference: [AGENTS.md:L38-L39](https://github.com/amthorn78/glow-hdengine-v2/blob/75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950/AGENTS.md#L38-L39)\n    \n\n<details> <summary>ℹ️ About Codex in GitHub</summary>\n<br/>\n\n[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you\n- Open a pull request for review\n- Mark a draft as ready\n- Comment \"@codex review\".\n\nIf Codex has suggestions, it will comment; otherwise it will react with 👍.\n\n\n\n\nCodex can also answer questions or update the PR. Try commenting \"@codex address that feedback\".\n            \n</details>",
      "commit_id": "75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950",
      "html_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403#pullrequestreview-5158828852",
      "id": 5158828852,
      "node_id": "PRR_kwDOP103ks8AAAABM317NA",
      "pull_request_url": "https://api.github.com/repos/amthorn78/glow-hdengine-v2/pulls/403",
      "state": "COMMENTED",
      "submitted_at": "2026-09-09T19:19:42Z",
      "user": {
        "avatar_url": "https://avatars.githubusercontent.com/in/1144995?v=4",
        "events_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/events{/privacy}",
        "followers_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/followers",
        "following_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/following{/other_user}",
        "gists_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/apps/chatgpt-codex-connector",
        "id": 199175422,
        "login": "chatgpt-codex-connector[bot]",
        "node_id": "BOT_kgDOC98s_g",
        "organizations_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/orgs",
        "received_events_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/received_events",
        "repos_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D/subscriptions",
        "type": "Bot",
        "url": "https://api.github.com/users/chatgpt-codex-connector%5Bbot%5D",
        "user_view_type": "public"
      }
    }
  ],
  "threads": {
    "review_threads": []
  }
}
```

## Final PR description integration

Only PR metadata was updated to record the completed outcomes; source/head did not change and no new review/CI run was required. The returned native update confirms open/unmerged status, current head and exact stored description. This is verification of the authorized metadata write, not merge polling.

```json
{
  "capture": "2026-09-09T19:56:20.250Z",
  "additions": 4089,
  "base": "main",
  "base_sha": "9065e6f0c01ad82a65c78687cd6c55e26ca33a1f",
  "body": "# HDE-EPIC040-PR01 — Source-proven catalog and exact contract data\n\nThe catalog currently differs from the approved taxonomy, and configuration writers can combine data, schemas, hashes or timestamps from different reads. This PR establishes the approved PR01 data and local validation layer and publishes its required evidence through the existing owners.\n\nChanges:\n\n- Correct the actual 36-row catalog differences while retaining all 64 Gate/Center facts and 108 Product metadata values.\n- Add the exact initial Magic-10 mechanics configuration and closed configuration, pure-result and internal-result schemas. Enforce duplicate-aware raw JSON, canonical bytes, exact integer domains, local schema resolution, source hashes and relational contracts.\n- Bind registry/config/bundle projections to captured selected-root sources, preserve FE/BE schema bytes, and reject stale primaries before deriving bundles.\n- Preserve the canonical gate's 26 targets and six selector identities, with numeric endpoint order only for the owning Channel Gate tuple.\n- Add bounded coordinated publication and recovery through the existing evidence updater, including the two already-required catalog validation logs and required companions.\n- Register exact affected paths with meaningful owner tests in the existing fail-closed CI classifier; retain its seven-lane consequence.\n\nAuthority and lineage:\n\n- EPIC / HDE-EPIC040 — Separation Pass 3; work unit HDE-EPIC040-PR01.\n- Detailed PR Plan v1.1: `libfile_7960d01d117881919c0004545ae3a4d7`, SHA-256 `a77d453aa2a8b50b8e559cb8f6e5e2098f667760802366646f539a772769916e`.\n- PR Instruction v2.0: `libfile_68be4bc4c4b88191aab5f5c7062c774b`, SHA-256 `dc556774202196b7d94f09870ff5b0d2c3fc47195e997f071ff4897ffb39e9fa`.\n- Approved whole-change Plan v2.1: `libfile_11c992cda3f0819199827e86584e41f1`; separate Isis-50 APPROVE review v2.1: `libfile_b85b81651a508191abdfd8f81803caf8`, 2026-09-09T13:36:43Z.\n- The Product Owner's exact PR-30 invocation supplies Proceed. Runtime 090926.1 / GCFPE-20260909.1; continuing dedicated PR01 session.\n\nPR01 supplies construction data, bounded local validation and associated evidence. Complete immutable admission/freezing remains PR02; actual classifier/kernel remains PR03; application identity and Reader corrections remain PR04. This local candidate does not activate a release or prove production fallback. Existing C040 decisions and historical evidence retain their owners and attribution.\n\nValidation at the published candidate tree `543ea921385410c6eda57404b8038b2d90f896e7`:\n\n- 548 affected tests pass, including strict contracts, writer/root fidelity, actual partial-write recovery, CI ownership and CRD fixtures.\n- All 12 read-only owner checks pass; repeated coordinated generation and subsequent checks/tests leave bytes and mtimes unchanged.\n- All 65 changed files map to the existing seven CI lanes and 63 supplemental owner-test targets. Actual GitHub CI and repository code/security reviews were pending at initial PR publication; the final outcomes are recorded below.\n- Bounded internal reviews found and repaired typed-error, source-capture and publication-recovery defects; corrected source was re-reviewed. These checks do not replace repository review outcomes.\n\nThe Product Owner additionally authorized fixing the two baseline CRD CI failures. Their fixture now constructs a coherent fresh CRD state in a temporary copy; original assertions and retained repository evidence remain intact. All 20 affected CRD tests pass. No check is waived.\n\nThe manifest cutter retains validation/calculation and delegates only its final bytes through a private callback into the existing atomic updater, so partial temporary writes cannot truncate the source manifest. Default API/CLI behavior and check-only behavior remain compatible. This is bounded support for the approved coordinated-recovery duty.\n\nBase: `9065e6f0c01ad82a65c78687cd6c55e26ca33a1f`. Initial commit: `924ae36a0bfe320f81fc9b6e4fd3891436096f27`.\n\nThe Product Owner retains manual merge control.\n\nCI repair after initial publication:\n\nThe first CI run exposed a pre-existing token reader bug: the retained PF04 snapshot contains the required token with Markdown-escaped underscores. The failure reproduces on both the base and initial PR commit. Commit `75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950` adds narrow underscore normalization and meaningful tests for unknown-token refusal and raw source hashes. Both existing owner modules pass (149 tests). No registry, Canon source or generated artifact changed. The current tree is `529306a74268f2a46765bf40defdae49026d103e`, spanning 67 changed paths. Initial repository code/security reviews completed without findings. Current-head code and security reviews and successor CI are now complete.\n\nFinal engineering endpoint — ready for Product Owner manual merge:\n\n- Current reviewed/tested head: `75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950`; tree `529306a74268f2a46765bf40defdae49026d103e`; 67 changed paths.\n- [CI run 34393325625](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34393325625) completed successfully. All seven selected lanes passed, including 1,544 affected owner tests, 111 evidence tests, and the final `CI_APPLICABILITY_AND_EXACT_HEAD_OK` guard. Counts from overlapping commands are not summed. The compatibility lane retained three closed-rails skips and two existing xfails; no selected lane was skipped or waived.\n- The repository code review completed for this head at 2026-09-09T19:23:36.540273Z. Its P1 fsync/EIO report was dispositioned with source and execution evidence: the reviewer reproduced EIO even on an independent one-byte temporary file; the baseline and approved Plan already require fsync. Suppressing writeback errors would weaken the required recovery behavior. Existing injected-failure tests and actual publication/CI pass. The original finding and both equivalent disposition comments remain visible; this is a review-environment limitation, with no silent code workaround or waiver.\n- [Security review](https://github.com/amthorn78/glow-hdengine-v2/pull/403#issuecomment-5607726236) completed for the same head at 2026-09-09T19:44:19.975498Z and explicitly reported no security issues. Complete issue-comment, formal-review, inline-comment, commit and check collections were retrieved; no applicable finding remains unaddressed.\n- The initial failed CI run and all review history remain preserved. CI fixtures and clean-candidate attestation are not live vendor QA, release activation, OPS01 or production fallback proof.\n\nPR01 engineering is complete. Merge remains the Product Owner's manual action. Subsequent PR-40 lineage review belongs to the retained whole-change IA after actual merge evidence is available.\n",
  "changed_files": 67,
  "closed_at": null,
  "comments": null,
  "commits": 2,
  "created_at": "2026-09-09T18:50:50Z",
  "deletions": 720,
  "diff": null,
  "display_title": "HDE-EPIC040-PR01: source-proven catalog and exact contract data",
  "display_url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403",
  "draft": false,
  "head": "hde-epic040-pr01-source-contracts",
  "head_repo_full_name": "amthorn78/glow-hdengine-v2",
  "head_repo_id": 1063073682,
  "head_sha": "75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950",
  "merge_commit_sha": "cbfc5f9c1c9464fe640a8bf2d509e98956b83062",
  "mergeable": true,
  "merged": false,
  "merged_at": null,
  "number": 403,
  "requested_reviewers": null,
  "requested_team_reviewers": null,
  "state": "open",
  "title": "HDE-EPIC040-PR01: source-proven catalog and exact contract data",
  "updated_at": "2026-09-09T19:54:27Z",
  "url": "https://github.com/amthorn78/glow-hdengine-v2/pull/403",
  "user": {
    "avatar_url": "https://avatars.githubusercontent.com/u/146120956?v=4",
    "email": null,
    "id": 146120956,
    "login": "amthorn78",
    "name": "amthorn78"
  }
}
```

## Evidence limits and endpoint

Initial local 548-test invocation/start/end were not retained; its actual log and initial tree are preserved without a reconstructed command. The corrected 149-test command and native CI command/log evidence are retained in full. All seven selected native CI lanes passed at current head 75ddaf2c94c2190c6b9d6a1e6e9894ba4591e950. Three retained closed-rails compatibility skips and two existing xfails are accurately reported; no selected lane was skipped or waived. Tests and CI clean-candidate attestation are not independent QA, OPS01 or active release proof.

Transient executor disconnects recovered through ordinary retries with the same workspace and source intact. The failed final-evidence file write was confirmed absent before its successful retry. No access bypass or model cause is inferred. Native Result creation and complete readback succeeded on their first supported routes in this finalization.

PR01 is MERGE_PENDING. The Product Owner owns manual merge. The historical Result remains valid after later native merge evidence; no duplicate Result or extra approval object is required.
