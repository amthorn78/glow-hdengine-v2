# GCFPE Repair Graph Source-Rebinding Report

The existing unselected graph has been rebound to the corrected raw-source snapshot. Its 55 nodes, 230 edges, state vocabulary, manual boundaries, and all other semantic fields are unchanged. The static graph/source check passed 1,500 checks with zero failures. This is not a complete-candidate or independent-governance PASS.

The same two Drive file IDs were updated only after their complete preimages matched the preserved local evidence. Both updated files were raw-fetched and byte-compared successfully. Existing historical captures and before-images remain intact.

```yaml
{
  "run_id": "GCFPE-REPAIR-RECOVERY-CORRECTION-20260914.1",
  "phase": "PHASE_2_GRAPH_SOURCE_REBINDING",
  "recorded_at_utc": "2026-09-14T22:04:58.631Z",
  "candidate_release": "GCFPE-20260914.1",
  "version": "091426.1",
  "selection_status": "UNSELECTED_CANDIDATE",
  "graph_sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
  "source_snapshot_sha256": "a8f3351c15279224af81eac4e013d7bbcc7436c3dd5b26b7385abd870f7160be",
  "graph_delta": {
    "changed_top_level_fields": [
      "authority_sources",
      "source_bindings"
    ],
    "all_other_fields_byte_semantically_identical": true,
    "node_count": 55,
    "edge_count": 230,
    "sole_new_prompt": "PR-35",
    "workflow_or_approval_changes": 0
  },
  "deterministic_result": {
    "result": "PASS",
    "checks": 1500,
    "failures": 0,
    "scope": "STATIC_GRAPH_AND_SOURCE_BINDINGS_NOT_INDEPENDENT_POSTFLIGHT",
    "complete_prompt_semantic_readback": "PENDING_PHASE_3",
    "protected_core_byte_validation": "PENDING_PHASE_5"
  },
  "local_mutations": [
    {
      "path": "/workspace/scratch/040256eb5cd7/candidate/graph/build_candidate_graph.py",
      "before_sha256": "5299491c29c61e3c506ba812fd27c90df73f48a09ff8858cbadd053b5a1cb64f",
      "after_sha256": "22eb846ff0f421943956aeedaa667fb5914fbb5d255f53b618fec1f7b77c7e49",
      "after_bytes": 73527
    },
    {
      "path": "/workspace/scratch/040256eb5cd7/candidate/graph/validate_candidate_graph.py",
      "before_sha256": "ce6a2947321e32a32619461648e0af213360d4a7cd02ab7c3a203665b32e1e42",
      "after_sha256": "4f29ad42ef32660f6432db37894b12d58f4e984dda0d3fed125efc0abd3da3ff",
      "after_bytes": 27570
    },
    {
      "path": "/workspace/scratch/040256eb5cd7/candidate/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json",
      "before_sha256": "c746f3f0c0f6f7b4df4c7e845d2b491f01370693c8327a7d0a3f877ef6fe06f7",
      "after_sha256": "47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
      "after_bytes": 518308
    },
    {
      "path": "/workspace/scratch/040256eb5cd7/candidate/graph/GCFPE-20260914.1-Candidate-Graph-Contract.md",
      "before_sha256": "2a5b591cd5a40d90889b69c85f90a61de647dbe521c6a70b7d8afed21261f471",
      "after_sha256": "a7bd0fb700cd23ba7f0cfd982095c9560a5cc6a464c664de3711d1c44dd16c1d",
      "after_bytes": 518875
    },
    {
      "path": "/workspace/scratch/040256eb5cd7/candidate/graph/GCFPE-20260914.1-Candidate-Graph-Validation.json",
      "before_sha256": "0541a676c0697b2f3073c5c7acaaa46db176a397ad80002d4fc3a0bd56a25b75",
      "after_sha256": "794250ae01d74d5af84cfca5259e9f8dc6295dbe52ce2369a2af3ba6499fc787",
      "after_bytes": 318861
    },
    {
      "path": "/workspace/scratch/040256eb5cd7/candidate/graph/GCFPE-20260914.1-Candidate-Graph-Validation.md",
      "before_sha256": "d2ec67e0959da5b4f640cb15ac3959a0152a3074151f6d07d9947701c1501d5c",
      "after_sha256": "365622cb75e3f6c1ef08bbbba278e19b34644e626bebc58020106edae20275bb",
      "after_bytes": 183905
    },
    {
      "path": "/workspace/scratch/040256eb5cd7/candidate/graph/GCFPE-20260914.1-Recovery-Source-Bindings.json",
      "before_sha256": null,
      "after_sha256": "db78986d456c2d1b34952bdd05c314630833d9b11b6b8d9d7b43202e43af1e11",
      "after_bytes": 7476
    }
  ],
  "drive_before": [
    {
      "expected_sha256": "2a5b591cd5a40d90889b69c85f90a61de647dbe521c6a70b7d8afed21261f471",
      "id": "1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp",
      "local_beforeimage_matches": true,
      "metadata": {
        "created_time": null,
        "current_user_can_share": null,
        "display_url": "https://drive.google.com/file/d/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp/view?usp=drivesdk",
        "drive_id": null,
        "file_or_folder": "file",
        "has_augmented_permissions": null,
        "id": "1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp",
        "mime_type": "text/markdown",
        "modified_time": "2026-09-14T18:56:31.531Z",
        "parent_ids": [
          "1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc"
        ],
        "permissions": null,
        "shared": null,
        "size": "510934",
        "source_visibility_status": "access_not_verified",
        "title": "GCFPE-20260914.1-Candidate-Graph-Contract.md",
        "url": "https://drive.google.com/file/d/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp/view?usp=drivesdk"
      },
      "name": "GCFPE-20260914.1-Candidate-Graph-Contract.md",
      "path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp-before.md",
      "retrieved_at_utc": "2026-09-14T22:02:06.257Z"
    },
    {
      "expected_sha256": "d2ec67e0959da5b4f640cb15ac3959a0152a3074151f6d07d9947701c1501d5c",
      "id": "11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5",
      "local_beforeimage_matches": true,
      "metadata": {
        "created_time": null,
        "current_user_can_share": null,
        "display_url": "https://drive.google.com/file/d/11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5/view?usp=drivesdk",
        "drive_id": null,
        "file_or_folder": "file",
        "has_augmented_permissions": null,
        "id": "11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5",
        "mime_type": "text/markdown",
        "modified_time": "2026-09-14T18:56:12.677Z",
        "parent_ids": [
          "1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc"
        ],
        "permissions": null,
        "shared": null,
        "size": "300584",
        "source_visibility_status": "access_not_verified",
        "title": "GCFPE-20260914.1-Candidate-Graph-Validation.md",
        "url": "https://drive.google.com/file/d/11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5/view?usp=drivesdk"
      },
      "name": "GCFPE-20260914.1-Candidate-Graph-Validation.md",
      "path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5-before.md",
      "retrieved_at_utc": "2026-09-14T22:02:06.258Z"
    }
  ],
  "drive_after": [
    {
      "bytes_identical": true,
      "id": "1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp",
      "identity_preserved": true,
      "metadata": {
        "created_time": null,
        "current_user_can_share": null,
        "display_url": "https://drive.google.com/file/d/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp/view?usp=drivesdk",
        "drive_id": null,
        "file_or_folder": "file",
        "has_augmented_permissions": null,
        "id": "1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp",
        "mime_type": "text/markdown",
        "modified_time": "2026-09-14T22:02:47.741Z",
        "parent_ids": [
          "1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc"
        ],
        "permissions": null,
        "shared": null,
        "size": "518875",
        "source_visibility_status": "access_not_verified",
        "title": "GCFPE-20260914.1-Candidate-Graph-Contract.md",
        "url": "https://drive.google.com/file/d/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp/view?usp=drivesdk"
      },
      "operation": "UPDATE_EXISTING_UNSELECTED_GRAPH_EVIDENCE_ONLY",
      "readback_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp-phase2.md",
      "retrieved_at_utc": "2026-09-14T22:02:48.980Z"
    },
    {
      "bytes_identical": true,
      "id": "11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5",
      "identity_preserved": true,
      "metadata": {
        "created_time": null,
        "current_user_can_share": null,
        "display_url": "https://drive.google.com/file/d/11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5/view?usp=drivesdk",
        "drive_id": null,
        "file_or_folder": "file",
        "has_augmented_permissions": null,
        "id": "11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5",
        "mime_type": "text/markdown",
        "modified_time": "2026-09-14T22:02:55.716Z",
        "parent_ids": [
          "1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc"
        ],
        "permissions": null,
        "shared": null,
        "size": "183905",
        "source_visibility_status": "access_not_verified",
        "title": "GCFPE-20260914.1-Candidate-Graph-Validation.md",
        "url": "https://drive.google.com/file/d/11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5/view?usp=drivesdk"
      },
      "operation": "UPDATE_EXISTING_UNSELECTED_GRAPH_EVIDENCE_ONLY",
      "readback_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5-phase2.md",
      "retrieved_at_utc": "2026-09-14T22:02:56.744Z"
    }
  ],
  "protected_state_guard": [
    {
      "complete_representation_unchanged": true,
      "last_edited_at": "2026-09-13T12:20:20.795Z",
      "retrieved_at_utc": "2026-09-14T22:03:49.893Z",
      "revision_unchanged": true,
      "source": "register",
      "source_id": "3d24590a05eb81ce942ad994cfca9fa1"
    },
    {
      "complete_representation_unchanged": true,
      "last_edited_at": "2026-09-14T12:47:55.512Z",
      "retrieved_at_utc": "2026-09-14T22:03:51.297Z",
      "revision_unchanged": true,
      "source": "alpha",
      "source_id": "3d64590a05eb81e1a645e0ca209b45c0"
    }
  ],
  "installed_skills": {
    "head": "517039dc7d2ddc2c4b0a8adbde83cae6cf3bb0be",
    "status": "CLEAN_UNCHANGED"
  },
  "open_dependencies": [
    "All downstream candidate control/manifests/fixtures must be rebound and revalidated against graph 47439465a46866e4f0c98a648887a822913a3a8ad18be66b6651634fb90eb7cb",
    "Live candidate LOCAL_DRAFT_ONLY provenance corrections",
    "Complete 55-prompt and 14-control semantic readback",
    "Installed-skill source binding correction under governed skill-maintenance route",
    "Independent postflight; exact-candidate Product Owner promotion approval"
  ],
  "not_performed": [
    "Selected prompt or register-selection mutation",
    "PF10 write or drain",
    "Alpha or PR04 execution",
    "Archive move/delete",
    "Product GitHub, CI, deployment, merge"
  ],
  "safe_next_phase": "PHASE_3_CANDIDATE_PROMPT_AND_CONTROL_RECONCILIATION"
}
```

## Phase boundary

Phase 2's schema/source-binding gate is complete. Candidate consumers of the prior graph digest remain explicitly stale until Phase 3–4 reconciliation. No prompt/skill completeness or promotion claim is inferred from this graph-only result. The selected 54-member release and stopped Alpha were fetched again after the graph edits and remain unchanged.
