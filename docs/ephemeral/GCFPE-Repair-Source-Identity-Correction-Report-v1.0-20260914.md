# GCFPE Repair Source Identity Correction Report

Source-only verification: `PASS`. This is not a candidate, skill-fit, release, independent-postflight, or Alpha-readiness verdict.

## Corrected raw capture defects

Every row below is proven by a full byte comparison: the failed-session capture equals the complete live raw file plus exactly one trailing LF (`0a`). The historical captures are preserved unchanged.

| Source | Historical bytes | Raw bytes | Correct raw SHA-256 |
| --- | ---: | ---: | --- |
| GCFPE-Change-Flow-Repair-Plan-v2.0-20260914.md | 53119 | 53118 | `e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01` |
| PF27-Canon-Plan-Templates-v2.0.5.md | 354326 | 354325 | `4f4f015bc8fe8c0a9f7d518fce13b7428a1427b49ca463982b769827169b22a0` |
| PF13- Reference-Glow-Development-Philosophy v1.md | 26816 | 26815 | `106c50bb2e06702c1c72764ccece3d5c500bddf4b553e12afa0c4d1f8c7a4c21` |
| PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md | 619585 | 619584 | `90e6af98fd18ce3ab4e91cb16fcfefbdb5bdf539690d8726f8e47359238bf853` |
| PF04-Canon-HDE-Governance-v2.8.6.md | 558989 | 558988 | `e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696` |
| PF19-Canon-Glow-QA-Guide-v3.0.5.md | 657009 | 657008 | `2a4a254422da92933e7f4dce9e074bcd7e1a1a6609ed54a7897d3f5f8cc059d0` |
| PF10-HDE-Build-Notes-v13.2.6.md | 175084 | 175083 | `4b2b0d198cecf6f4ece852c82951342e512124abfb93fa90678df8d97b4f4f86` |
| PF06-Canon-Change-Process-Guide-v2.5.4.md | 395892 | 395891 | `ad238a8fc07af27bcecf5afce71368766d96d0d40104649b2a005a0f721dd2f9` |
| PF21-Reference-7 Phases of Alchemical Engineering.md | 10376 | 10375 | `391bf7d2eb51022e22edb69b90a2ed6eaa63f621dedcf817513c2ae1a0c77e24` |

## Scope and limitations

- Selected authority remains `GCFPE-20260913.1 / 091326.2 / 54`; candidate remains unselected `GCFPE-20260914.1 / 091426.1 / 55` with sole addition PR-35.
- All 54 selected and 55 candidate prompt representations were fetched completely. Twelve Notion candidate controls and the Drive procedure were also fetched; the direct-handoff control copy exists locally but the exact Drive filename search returned no result. Its publication is an unmet later control dependency, not proof of completed work.
- Eight PFCanon sources were acquired only as raw Markdown with verified direct parent. No native-document PFCanon content was accessed.
- Six complete installed packages and all fourteen installed skill identity files were pinned to Git. No installed source was changed.
- Historical capture manifests, prior validation reports, and draft handoff files remain evidence only. Correct raw pins do not validate consumers that still carry defective digests.
- Source-only SRC-003 defects are resolved in this new snapshot. Candidate binding/provenance defects remain open until the later correction and validation phases.
- Alpha remains stopped after PR03 accepted-final; PR04/PR-10 is not started. No PF10 mutation, archive, product GitHub, CI, deployment, or Alpha-resumption action occurred.

## Verification record

```yaml
{
  "run_id": "GCFPE-REPAIR-RECOVERY-CORRECTION-20260914.1",
  "mode": "TARGETED_SOURCE_ONLY",
  "completed_at_utc": "2026-09-14T21:54:05.354826+00:00",
  "verdict": "PASS",
  "snapshot_sha256": "a8f3351c15279224af81eac4e013d7bbcc7436c3dd5b26b7385abd870f7160be",
  "source_count": 357,
  "issues": [],
  "scope_counts": {
    "selected_control": 10,
    "governing_error_log": 1,
    "selected_prompt": 54,
    "candidate_prompt": 55,
    "candidate_control": 12,
    "context_page": 3,
    "directory_lineage_receipt": 1,
    "controlled_pf_markdown": 8,
    "governing_or_evidence_markdown": 9,
    "candidate_control_markdown": 1,
    "installed_skill": 14,
    "installed_skill_source": 91,
    "candidate_before_image": 98
  },
  "raw_capture_corrections": [
    {
      "exact_match": false,
      "new_bytes": 53118,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI.md",
      "new_sha256": "e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01",
      "old_bytes": 53119,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/core/GCFPE-Change-Flow-Repair-Plan-v2.0-20260914.md",
      "old_sha256": "94478a230055b9119074086e225c7f09697448edb96155ca3859f11f42d4a80d",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI",
      "title": "GCFPE-Change-Flow-Repair-Plan-v2.0-20260914.md"
    },
    {
      "exact_match": false,
      "new_bytes": 354325,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4.md",
      "new_sha256": "4f4f015bc8fe8c0a9f7d518fce13b7428a1427b49ca463982b769827169b22a0",
      "old_bytes": 354326,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md",
      "old_sha256": "4b66d291684ff3b7eb5b8913bc18be90a94c4bd9c5960772f74c7a45685a1ba1",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4",
      "title": "PF27-Canon-Plan-Templates-v2.0.5.md"
    },
    {
      "exact_match": false,
      "new_bytes": 26815,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j.md",
      "new_sha256": "106c50bb2e06702c1c72764ccece3d5c500bddf4b553e12afa0c4d1f8c7a4c21",
      "old_bytes": 26816,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/pfcanon/PF13- Reference-Glow-Development-Philosophy v1.md",
      "old_sha256": "85841e6cfbaa7bbbd309e4125b111fdb3cffa8d3a9d9cd9c76c3d3cef8af5373",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j",
      "title": "PF13- Reference-Glow-Development-Philosophy v1.md"
    },
    {
      "exact_match": false,
      "new_bytes": 619584,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ.md",
      "new_sha256": "90e6af98fd18ce3ab4e91cb16fcfefbdb5bdf539690d8726f8e47359238bf853",
      "old_bytes": 619585,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md",
      "old_sha256": "f7939d5902276f23f3a314f9e09f1e9b83970490aab75f77465e3a0f28fe972c",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ",
      "title": "PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md"
    },
    {
      "exact_match": false,
      "new_bytes": 558988,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp.md",
      "new_sha256": "e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696",
      "old_bytes": 558989,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md",
      "old_sha256": "e329dd657da1fd123cc818d8a48c03e842f4ee61113536ef78bf42ae09f49653",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp",
      "title": "PF04-Canon-HDE-Governance-v2.8.6.md"
    },
    {
      "exact_match": false,
      "new_bytes": 657008,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt.md",
      "new_sha256": "2a4a254422da92933e7f4dce9e074bcd7e1a1a6609ed54a7897d3f5f8cc059d0",
      "old_bytes": 657009,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md",
      "old_sha256": "2a09ad6ace7bc0fe89b1f0f09716695058409265b6a113286b5feea620b8d043",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt",
      "title": "PF19-Canon-Glow-QA-Guide-v3.0.5.md"
    },
    {
      "exact_match": false,
      "new_bytes": 175083,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP.md",
      "new_sha256": "4b2b0d198cecf6f4ece852c82951342e512124abfb93fa90678df8d97b4f4f86",
      "old_bytes": 175084,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/pfcanon/PF10-HDE-Build-Notes-v13.2.6.md",
      "old_sha256": "4a2545197cf6fec854f053ca888651b737384f4db11fde9e68eca91b4f4f0b48",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP",
      "title": "PF10-HDE-Build-Notes-v13.2.6.md"
    },
    {
      "exact_match": false,
      "new_bytes": 395891,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9.md",
      "new_sha256": "ad238a8fc07af27bcecf5afce71368766d96d0d40104649b2a005a0f721dd2f9",
      "old_bytes": 395892,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md",
      "old_sha256": "034a1dadbec6ec03eeba34c41443b7f4173424cc53a18732e9b58f911caf87bc",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9",
      "title": "PF06-Canon-Change-Process-Guide-v2.5.4.md"
    },
    {
      "exact_match": false,
      "new_bytes": 10375,
      "new_path": "/workspace/scratch/040256eb5cd7/recovery-20260914.1/sources/drive/1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI.md",
      "new_sha256": "391bf7d2eb51022e22edb69b90a2ed6eaa63f621dedcf817513c2ae1a0c77e24",
      "old_bytes": 10376,
      "old_equals_raw_plus_one_LF": true,
      "old_extra_hex": "0a",
      "old_path": "/workspace/scratch/040256eb5cd7/baseline/pfcanon/PF21-Reference-7 Phases of Alchemical Engineering.md",
      "old_sha256": "c17b98797704a5ccc525ba24a20bb247b0e929ee92c737e92ae8512584c064ba",
      "raw_prefix_exact": true,
      "source_id": "drive-file:1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI",
      "title": "PF21-Reference-7 Phases of Alchemical Engineering.md"
    }
  ],
  "protected_state_changes": 0,
  "candidate_or_skill_edits": 0,
  "not_full_ecosystem_validation": true,
  "follow_on_dependencies": [
    "Rebind nine defective historical source identities in candidate consumers",
    "Correct live candidate LOCAL_DRAFT_ONLY provenance",
    "Publish/read back missing direct-handoff control copy only after its governed skill bindings are corrected",
    "Independent final review before promotion approval"
  ]
}
```

## Sequential gate

After exact Drive upload/readback of this report and its paired source manifest, Phase 1 may close. Phase 2 begins with rebinding the recovered graph and its consumers to these exact raw-source identities. Promotion and Alpha execution remain unauthorized at this gate.
