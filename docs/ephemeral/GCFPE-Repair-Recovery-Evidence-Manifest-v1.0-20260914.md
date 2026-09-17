---
artifact_type: GCFPE_REPAIR_RECOVERY_EVIDENCE_MANIFEST
artifact_version: "1.0"
run_id: GCFPE-REPAIR-RECOVERY-20260914
mode: TARGETED
generated_at_utc: 2026-09-14T20:59:01Z
recovery_verdict: PARTIAL_RECOVERY_AVAILABLE
governance_audit_verdict: FAIL
source_snapshot_sha256: ef16e466220787227e3e1f24b8d3b382d3558387b41091323e57ac8894b484c5
source_count: 93
manifest_scope: BOUNDED_RECOVERY_EVIDENCE
---

# GCFPE Repair Recovery Evidence Manifest v1.0

## Machine-readable run record

```yaml
schema: gcfpe-repair-recovery-evidence-manifest/1.0
run:
  id: GCFPE-REPAIR-RECOVERY-20260914
  mode: TARGETED
  retrieval_window_utc:
    start: 2026-09-14T20:33:23Z
    end: 2026-09-14T21:02:49Z
  source_snapshot:
    source_count: 93
    sha256: ef16e466220787227e3e1f24b8d3b382d3558387b41091323e57ac8894b484c5
  primary_skill:
    name: amthor-workspace-governance-audit
    revision: 1.11.1
    mode: TARGETED
    verdict: FAIL
    finding_counts: {BLOCKER: 2, ERROR: 2, WARNING: 2, ADVISORY: 0}
    evidence_sha256: 27939fd34affd174bbce79f23ffe5ad35fff2e27954408e685424a932ec32b42
  optional_read_only_validator:
    name: flowmaster-validate
    revision: 3.2.2
    verdict: FLOWMASTER_SUITE_PASS
    suite_ok: true
    finding_counts: {BLOCKER: 0, ERROR: 0, WARNING: 0, ADVISORY: 0}
    receipt_sha256: c5aee855905cf6f4a3e0b1fa665f9f97eaca0d15f967ae9114e5363869c00648
    limitation: internal candidate consistency only; external Drive raw-byte identity not queried
  recovery_verdict: PARTIAL_RECOVERY_AVAILABLE
  required_deliverable_group_counts:
    denominator: 16
    RECOVERABLE_CONFIRMED: 2
    RECOVERABLE_WITH_REVALIDATION: 6
    PARTIAL_RECOVERABLE: 5
    CONFLICTING_OR_UNSAFE: 1
    UNVERIFIED: 0
    NOT_FOUND: 2
mutation_attestation:
  durable_writes:
    - GCFPE-Repair-Recovery-Validation-Report-v1.0-20260914.md
    - GCFPE-Repair-Recovery-Evidence-Manifest-v1.0-20260914.md
  prohibited_actions_performed: []
  pfcanon_representation_opened: controlled Markdown only
  library_used: false
  failed_session_contacted: false
```

## Authoritative and live source records

| ID | Source ID / URL / path | Type | Complete | Revision / digest / object | Retrieved UTC | WP | Findings | Classification | Lifecycle | Attribution basis | Uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 | [Plan v2.0](https://drive.google.com/file/d/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI/view?usp=drivesdk) | Drive raw Markdown | yes, 53,118 B | SHA-256 `e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01`; modified `2026-09-14T14:21:41.416Z` | `20:35:01.262Z` | WP0–WP8 baseline | all | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | exact named ID, title, parent, raw bytes | instruction source, not proof of implementation |
| A-002 | [Implementation Prompt v1.0](https://drive.google.com/file/d/1NhVE0jZLS0UIfZWsokymRiglsYv1Z4Lc/view?usp=drivesdk) | Drive raw Markdown | yes, 27,689 B | SHA-256 `b82a3e0074d0d61ec1f49734cd6bfefd160d565a7a396039b750adda8a5260ad`; modified `2026-09-14T14:36:37.515Z` | `20:35:01.703Z` | attribution baseline | all | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | exact named ID, title, parent, raw bytes | authority baseline, not completion evidence |
| A-003 | [Selected operating procedure v3.1.0](https://drive.google.com/file/d/1KvX86E4yP4sGHC17tlcfCPRNavnhckEm/view?usp=drivesdk) | Drive raw Markdown | yes, 22,782 B | SHA-256 `c62dde03425b09e1b8bc51b6cc5d870392075e8a0e0cd21ad961c7ecdc6d8e7c`; modified `2026-09-13T11:39:12.231Z` | `20:35:01.258Z` | WP0/WP4 | baseline | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact named ID and selected register binding | no immutable Drive revision object exposed |
| A-004 | [Selected catalog](https://app.notion.com/p/3da4590a05eb81bcbc5deb2d2cec4f1f?pvs=204) | Notion page | yes | enhanced-Markdown SHA-256 `4cfc36aeef4486854fbf232daf20bde4bc19f4dd362ba1ccba09e67e163bb454`; edited `2026-09-13T12:20:24.692Z` | `20:33:24.813Z`; rechecked end | WP0 | baseline | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact page ID, parent path, complete body, register cross-link | Notion native revision ID unavailable |
| A-005 | [Release register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1?pvs=204) | Notion page | yes | SHA-256 `f45bf4b9b166cbdfb8747bc90b4098f601b8fbc3e5878011e0c60ad3bbde3ff0`; edited `2026-09-13T12:20:20.795Z` | `20:33:25.917Z`; rechecked end | WP0/WP7 | baseline, RF-005 | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact page ID and current selected entry | native revision ID unavailable |
| A-006 | [Selected GCFPE-MGMT-10](https://app.notion.com/p/3da4590a05eb81ac80e6d886a25aa026?pvs=204) | Notion page | yes | SHA-256 `5c7d0e5e6c4b08eb52592164683f8ff132d5c7c542977a47d2aa52cd1f9658e9`; edited `2026-09-13T11:36:03.382Z` | `20:33:24.856Z`; rechecked end | WP0 | baseline | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact page ID/title/version/parent | native revision ID unavailable |
| A-007 | [Alpha notes](https://app.notion.com/p/3d64590a05eb81e1a645e0ca209b45c0?pvs=204) | Notion page | yes | SHA-256 `3648468c695fcf1c636cfdb4f094accc280834d28d2b14c30b087e381597e48c`; edited `2026-09-14T12:47:55.512Z` | `20:33:24.743Z`; rechecked end | WP0/WP4/WP8 | baseline | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact page ID, top operative state, edit predates failed session | older historical sections remain in page but top state controls |
| A-008 | [PR-development skill-fit decision](https://app.notion.com/p/3d94590a05eb81f6824ff4bf507d474c?pvs=204) | Notion page | yes | SHA-256 `2bbf011e978c4924ca8fbd33ae946b369a3b879790a1c9f9f572788f45e1f078`; edited `2026-09-13T12:19:49.506Z` | `20:33:24.785Z`; rechecked end | WP0/WP3 | baseline | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact named page and complete body | successor decision must still be revalidated |
| A-009 | [PF10 Markdown v13.2.6](https://drive.google.com/file/d/1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP/view?usp=drivesdk) | Drive raw Markdown | yes, 175,083 B | SHA-256 `4b2b0d198cecf6f4ece852c82951342e512124abfb93fa90678df8d97b4f4f86`; modified `2026-09-14T12:52:03.000Z`; parent `1gdB...` | `20:47:40Z`; metadata rechecked end | WP0/WP1/WP5 | RF-001, RF-002, RF-003 | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact controlled Markdown direct child and raw bytes | native GDoc sibling identified by metadata only; never opened |
| A-010 | `audit_snapshot` | local pinned bundle | yes, 93 files | snapshot SHA-256 `ef16e466220787227e3e1f24b8d3b382d3558387b41091323e57ac8894b484c5` | `20:48:35Z` | audit | all | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | deterministic manifest over retrieved files | local audit workspace is transient |

## Candidate Notion records

| ID | Source ID / URL | Type | Complete | Revision / digest | Retrieved UTC | WP | Findings | Classification | Lifecycle | Attribution basis | Uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-001 | [candidate catalog](https://app.notion.com/p/3db4590a05eb81738ef1d846e3c0df8c?pvs=204) | Notion page | yes | SHA-256 `3aa3da5451e5c322fbff181cc0a2c30af9c5429b0dc8a326b8c21b1198dc98ab`; edited `16:23:58.833Z` | `20:43:10.576Z` | WP1/WP2/WP4 | RF-004 | `PARTIAL_RECOVERABLE` | `VALIDATED_UNSELECTED_CANDIDATE` | exact candidate ID, 55-member table, candidate parent | false `LOCAL_DRAFT_ONLY` provenance; all 55 not freshly refetched |
| C-002 | [candidate register entry](https://app.notion.com/p/3db4590a05eb816f925ef3b0659de3b8) | Notion page | yes | SHA-256 `f4357c41ef4067fe574fe1e7e5241e6e691807977772fc509eb9f2a3e7973ca0`; edited `16:24:22.035Z` | `20:36:52.118Z`; rechecked end | WP4/WP7 | RF-004, RF-005 | `PARTIAL_RECOVERABLE` | `DRAFT_CANDIDATE` | exact child of current register, explicitly unselected | false `LOCAL_DRAFT_ONLY` provenance |
| C-003 | [candidate MGMT](https://app.notion.com/p/3db4590a05eb81d1bb64ebcb3ca8eb54?pvs=204) | Notion page | yes | SHA-256 `2daa0b587609bf628de7bcf973e0dbde0bbdfe1f1521b3021822d3268f5f6721`; edited `17:55:37.576Z` | `20:43:10.276Z` | WP2 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `VALIDATED_UNSELECTED_CANDIDATE` | exact ID/title/parent; normalized body equals local candidate | source lineage requires correction |
| C-004 | [candidate PR-30](https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204) | Notion page | yes | SHA-256 `0476c1ae9d78cda843e87eab5e3f5d7ce8f57be46f7b5a09df81236c11926636`; edited `17:56:29.229Z` | `20:43:10.275Z` | WP2/WP5 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `VALIDATED_UNSELECTED_CANDIDATE` | exact ID/title/PR parent; normalized body equals local | full suite needs corrected-source postflight |
| C-005 | [candidate PR-35](https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204) | Notion page | yes | SHA-256 `4de3cfa5f0547197a0f7e507562e446cfe0ba631704de8cf688cd0e7da838296`; edited `17:56:31.066Z` | `20:43:10.494Z` | WP1/WP2/WP5 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `VALIDATED_UNSELECTED_CANDIDATE` | sole new member; exact ID/title/parent; normalized body equals local | full suite needs corrected-source postflight |
| C-006 | [candidate RS-20](https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204) | Notion page | yes | SHA-256 `eb999087c203ea44646704e03bad53cef0b015557c100c9c764a233ab39bcfbe`; edited `16:08:27.910Z` | `20:43:10.380Z` | WP2/WP5 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `VALIDATED_UNSELECTED_CANDIDATE` | exact ID/title/parent; semantic delta only mention serialization | full suite needs corrected-source postflight |
| C-007 | [candidate RS-40](https://app.notion.com/p/3db4590a05eb8183b5ffdf4270133226?pvs=204) | Notion page | yes | SHA-256 `77cce40f9172f038d0999012a6893657b9a75e098097fbc3f10ef20f8dc84ce5`; edited `17:59:43.225Z` | `20:43:10.695Z` | WP2/WP5 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `VALIDATED_UNSELECTED_CANDIDATE` | exact ID/title/parent; semantic delta only mention serialization | full suite needs corrected-source postflight |

## Attributable Drive artifact cluster

Every item below is a complete raw Markdown read from parent folder `1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc`. Attribution is based on exact `GCFPE-20260914.1` identity, content lineage, cross-references, parentage, and recovered-workspace match; creation time is only a discovery clue.

| ID | Drive source | Complete / SHA-256 | Created; retrieved UTC | WP | Findings | Classification | Lifecycle | Attribution / uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D-001 | [Governance Preflight Report](https://drive.google.com/file/d/1hgLXNXIW5_KUMknR1TCy_519Y3sf-0n_/view?usp=drivesdk) | yes; `d3c396d8d3e2a30fa1198991017937416e8bf655c01433b8ebf0a52247c05c78` | `15:16:33.712Z`; `20:38:21.339Z` | WP0 | RF-001 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | exact release/preflight lineage; affected by pin defect |
| D-002 | [Phase-A Source Manifest](https://drive.google.com/file/d/1KOZNFGSJ5OtQHddbAUfrmFz-lUftuVgY/view?usp=drivesdk) | yes; `760b9729cf3f56ac1abca8c2f8afe1e473f43a82eb9157b2f2f14cf64336e417` | `15:17:36.668Z`; `20:38:21.519Z` | WP0 | RF-001, RF-002 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | exact failed-session manifest; 8 raw size discrepancies |
| D-003 | [Governance Preflight Evidence](https://drive.google.com/file/d/1mpN-OvW1WP3UDCivYiDhremJHMZFUMIC/view?usp=drivesdk) | yes; `ea2a9be292771a0bc7c4b1fbc40b47e165707313fc59d4e63a33b2bce31b39b6` | `15:17:43.047Z`; `20:38:15.773Z` | WP0 | RF-001 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | exact release/source lineage; pin defect limits trust |
| D-004 | [Repair-Batch Preflight Findings](https://drive.google.com/file/d/12_MUtOrF7asR4DgqZihpBG6mM2-BDiQ8/view?usp=drivesdk) | yes; `7029f04da16fbf0b952e59ff141dabbb021febb171b5deba1b5d8c8ef4b72f68` | `15:17:48.296Z`; `20:38:15.775Z` | WP0 | RF-001 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | useful historical findings; not current verdict |
| D-005 | [Observed Workspace Skill Registry](https://drive.google.com/file/d/1Ic5zQrl_MaLufUDCWYNlwfRbdn4EWb5I/view?usp=drivesdk) | yes; `e6c4ce94ab7fe9e5c85cac760468d4185867ca7b6e6202990a2a662ce7760405` | `15:17:54.968Z`; `20:38:15.578Z` | WP0/WP3 | RF-003 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | pre-change registry; current Git supersedes revisions |
| D-006 | [Predecessor Project Prompt Registry](https://drive.google.com/file/d/1XKrOSAh6Zuae8sIGJziPVXfRRNSO1O9p/view?usp=drivesdk) | yes; `d708fdf4e380625fd90bf493903a162c650aee209aabf0cfc333643a27c9a107` | `15:18:01.670Z`; `20:38:15.733Z` | WP0 | RF-001 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | useful selected predecessor inventory; source pin caveat |
| D-007 | [Preflight Proposed Changeset](https://drive.google.com/file/d/1kBlzZcMFm6_CCzG0qxZFGepxofTXlD8x/view?usp=drivesdk) | yes; `e1a3c0a1e714d6cfb7519dbf4ef297587589dc37af00bd7203f77dc683dd6ac9` | `15:18:06.744Z`; `20:38:09.982Z` | WP0 | RF-006 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | failed-session proposal only; never authority |
| D-008 | [Phase-A Drive Readback Receipt](https://drive.google.com/file/d/1Lra_mSpGTigF2tRyUvRstt6wWvQvYrvg/view?usp=drivesdk) | yes; `d4201dea940946efe76bc9f7cb6d223247d692dba9198d655159aac2f5591d7d` | `15:18:40.595Z`; `20:38:10.094Z` | WP0 | RF-001 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | receipt exists; it did not catch transformed raw bytes |
| D-009 | [Candidate Authoring Contract](https://drive.google.com/file/d/1WpDExJLnUguZIYrr04nc7vVf3QHyFP8p/view?usp=drivesdk) | yes; `ab53d05e2d43ed01dbd0bf594a02cf64bd6abf7ab89761c756fe1bcbc48dbe1b` | `15:31:29.012Z`; `20:38:09.938Z` | WP1/WP2 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `DRAFT_CANDIDATE` | exact candidate lineage; requires corrected pins |
| D-010 | [Candidate Graph Contract](https://drive.google.com/file/d/1wEmpnwMJ_OhTdC61lDqr4q-undkA4-Hp/view?usp=drivesdk) | yes; `2a5b591cd5a40d90889b69c85f90a61de647dbe521c6a70b7d8afed21261f471` | `15:31:32.482Z`; `20:38:02.750Z` | WP1/WP2 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `VALIDATED_UNSELECTED_CANDIDATE` | fresh validator passes graph; source lineage remains open |
| D-011 | [Candidate Graph Validation](https://drive.google.com/file/d/11ZFW5FG04lI8PmYoSjcS7LJRDjtNqmv5/view?usp=drivesdk) | yes; `d2ec67e0959da5b4f640cb15ac3959a0152a3074151f6d07d9947701c1501d5c` | `15:31:37.498Z`; `20:38:09.925Z` | WP1/WP5 | RF-002 | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | independently corroborated for internal graph scope only |
| D-012 | [Procedure v4.0.0 candidate](https://drive.google.com/file/d/1TDtZNMNxgqt6h-HzQ2up_syK5zauLqBj/view?usp=drivesdk) | yes; `a1f2dac133144f2ddc29f107cace08a3e37e242950a5bf5899a461f9e1d920b2` | `16:16:38.872Z`; `20:37:55.866Z` | WP4 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `COMPLETE_UNSELECTED_CANDIDATE` | exact candidate procedure; not selected; repin first |
| D-013 | [Complete Candidate Semantic Ledger](https://drive.google.com/file/d/1TrzGWkpKImk105fgsBLp2wVQVnOeh9Kr/view?usp=drivesdk) | yes; `dad411064f0aa5f30de2098014a6155312246eedf24f5fec664bc5afc544f603` | `16:21:55.406Z`; `20:38:03.009Z` | WP2/WP5 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `EVIDENCE_ONLY` | complete ledger; external source lineage open |
| D-014 | [Complete Candidate Source Manifest](https://drive.google.com/file/d/1nBBvD2eIq6H1kx8SZR4aVp133Iv1ztN-/view?usp=drivesdk) | yes; `9f8c5f3c2977e449805f54e073e26aac765da2dc76124b03b542bd84cc01cc7a` | `16:21:59.627Z`; `20:38:04.374Z` | WP2/WP5 | RF-001, RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `EVIDENCE_ONLY` | 55-body/readback evidence; upstream pin defective |
| D-015 | [Candidate Suite Validation](https://drive.google.com/file/d/1ewDlZAGGDAbPyv07DzAZ_SsAJ4V-fWjw/view?usp=drivesdk) | yes; `12d1240cd98473bb11734e828704638e23228021d780e786e3c0437ef83458c2` | `16:22:02.825Z`; `20:38:02.542Z` | WP5 | RF-002 | `RECOVERABLE_WITH_REVALIDATION` | `EVIDENCE_ONLY` | internal validation evidence; external raw bytes out of scope |
| D-016 | [Behavior Fixture Specification](https://drive.google.com/file/d/1PXP6vwzQf7myV1UgKOfFlmUYMsn2Pnl7/view?usp=drivesdk) | yes; `f349105395ecf219b92de89db1602c75b4507816cc35e348f14d3bc2bc70fd67` | `16:22:06.544Z`; `20:37:55.675Z` | WP5 | none for internal scope | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | exact fixture identity and fresh deterministic corroboration |
| D-017 | [Behavior Fixture Results](https://drive.google.com/file/d/1zJ4LuLBsszmuHBVE0zVw26DRltkQpskE/view?usp=drivesdk) | yes; `74924e095bc2b65463d542f548d0179c918ed3372547a459541b0a3f82cd038f` | `16:22:10.504Z`; `20:37:55.782Z` | WP5 | RF-002 limitation | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | fresh Flowmaster corroborates internal fixture behavior |
| D-018 | [Skill-Fit Commit and Readback Evidence](https://drive.google.com/file/d/1bi9x7sd445T2bYuRcPqqflFR3tO43iUv/view?usp=drivesdk) | yes; `70e984e95d25c69879df6eeb6501bfa34cb9e79c79629137b6c7daed8691027e` | `17:52:06.928Z`; `20:37:55.727Z` | WP3 | RF-003 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | Git corroborates commits/hashes; candidate binding defect remains |
| D-019 | [Production Activation Delta Manifest](https://drive.google.com/file/d/1WzKq1qJu4TkmjeauGIdELV5iUgnkY6PF/view?usp=drivesdk) | yes; `919923e6129dde51dba6c811f31c5da4c4e156212342c5c0999be164791ee0b5` | `19:27:19.512Z`; `20:37:49.486Z` | WP7 | RF-005 | `RECOVERABLE_WITH_REVALIDATION` | `DRAFT_CANDIDATE` | exact transaction input; no execution authority |
| D-020 | [Live Notion Delta Overlay](https://drive.google.com/file/d/1ekxXn3uKRFKw7czef04t7e6-HSPdIy9j/view?usp=drivesdk) | yes; `dbb8ab53b565e7e2627fa8ad294a5c439da9776547e59b7dd159b67803ed5b15` | `19:41:27.757Z`; `20:37:49.718Z` | WP7 | RF-005 | `RECOVERABLE_WITH_REVALIDATION` | `DRAFT_CANDIDATE` | exact planned serialization; never executed |
| D-021 | [Live Notion Activation Preflight](https://drive.google.com/file/d/1E9ITE1ytZXpiWfnedc5IS2fuiCqi7eGo/view?usp=drivesdk) | yes; `fa5b9a79b15d88cd279295cc3f06b0ca643649ba526cc968a898f4156a7eba82` | `19:41:31.196Z`; `20:37:49.440Z` | WP7 | RF-005 | `RECOVERABLE_WITH_REVALIDATION` | `EVIDENCE_ONLY` | 67/174 preflight evidence; live state must be re-read |
| D-022 | [Intact Archive Transaction Manifest](https://drive.google.com/file/d/1kpupleZ4zeXqPdEb-k85CZP55uvjUc2c/view?usp=drivesdk) | yes; `3d1c75a7e381b9831bd57e88563053eee91121edbf5f6632ece335bc43384d48` | `19:42:24.141Z`; `20:37:43.479Z` | WP7 | RF-005 | `RECOVERABLE_WITH_REVALIDATION` | `DRAFT_CANDIDATE` | archive plan only; no move receipt |
| D-023 | [Drive Artifact Readback Receipt](https://drive.google.com/file/d/1F2s_1ilDbO2Gpsb7qGfiwXJJ_eEgOSOz/view?usp=drivesdk) | yes; `141bf6bcdad2111476e2a26f95b22505114f1e8278f20da260ef67b8daef15de` | `19:44:02.016Z`; `20:37:43.378Z` | WP5/WP7 | RF-005 | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | artifact presence/readback corroborated by this audit; not completion proof |
| D-024 | [Prepared Register Selection Block](https://drive.google.com/file/d/1q3CKds-xekuGr6v5H14htPQXjRVxB6aj/view?usp=drivesdk) | yes; `d5a980d2a6df2f15de2bff02742e55a8a7449b909f23b8cdaf6241d6df4546df` | `19:56:44.457Z`; `20:37:43.486Z` | WP7 | RF-005 | `RECOVERABLE_WITH_REVALIDATION` | `DRAFT_CANDIDATE` | prepared payload only; must not be executed unchanged |
| D-025 | [Recovery Checkpoint](https://drive.google.com/file/d/1G6EuxyOKEgVnXJBDZwGxNrrHglbclsRq/view?usp=drivesdk) | yes; `c51e721dd01196b35f063794b1a36ff6cfcd939197a5709177d4ec4e011fd35c` | `20:09:58.263Z`; `20:37:43.393Z` | recovery | RF-006 | `CONFLICTING_OR_UNSAFE` | `EVIDENCE_ONLY` | exact lineage; liveness/authority conclusions contradicted |
| D-026 | [Production Promotion Transaction Plan](https://drive.google.com/file/d/1fi0Zpp3MGUlwQucve4ZY19WW8sfxbSfC/view?usp=drivesdk) | yes; `4f9ea5e1ea87456100352b57e64e2681eaf039754d6d49eccb5a475704c52165` | `20:17:27.106Z`; `20:37:43.479Z` | WP7 | RF-005 | `RECOVERABLE_WITH_REVALIDATION` | `EVIDENCE_ONLY` | latest failed-session state; explicitly no remote mutation and pending gate |

## Installed skills, Git, workspaces, and validators

| ID | Source / path | Type | Complete | Revision / digest / object | Retrieved UTC | WP | Findings | Classification | Lifecycle | Attribution basis | Uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G-001 | `/root/.codex/skills/remote-skills` | Git repository | yes for requested paths | head=`origin/master`=`517039dc7d2ddc2c4b0a8adbde83cae6cf3bb0be`; clean; 23 commits after `669d0f81` | `21:02:49Z` | WP3 | RF-003 | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | object identity, log, diff, status | commit authorship inferred from lineage/content, not timestamp alone |
| S-001 | `skill-6a93504b...` | installed skill | yes | governance-audit 1.11.1; SHA `e4536aae...`; commit `ae897543...` | `21:02:49Z` | WP3 | none scoped | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact installed bytes and Git object | package-wide behavior beyond GCFPE not rerun |
| S-002 | `skill-6a8f9739...` | installed skill | yes | flowmaster-validate 3.2.2; SHA `5295a873...`; semantic commit `6001e747...`; head `517039dc...` | `21:02:49Z` | WP3/WP5 | RF-002, RF-003 | `CONFLICTING_OR_UNSAFE` | `SELECTED_UNVERIFIED` | exact installed bytes; fresh internal validator pass | candidate contract resource has wrong external digest |
| S-003 | `skill-6a8f94d5...` | installed skill | yes | change-flow 3.2.4; SHA `57971dcd...`; commit `87da6b67...` | `21:02:49Z` | WP3 | RF-002, RF-003 | `CONFLICTING_OR_UNSAFE` | `SELECTED_UNVERIFIED` | exact installed bytes and Git diff | selected alias remains predecessor; candidate resource unsafe |
| S-004 | `skill-6aa5cd93...` | installed skill | yes | pr-development 1.2.4; SHA `cd7acb3a...`; commit `bb97c851...` | `21:02:49Z` | WP3 | none scoped | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact installed bytes, Git, fresh scoped fixtures | only GCFPE-relevant behavior verified |
| S-005 | `skill-6a92b8d4...` | installed skill | yes | devops 1.5.0; SHA `499b8c23...`; no diff after baseline | `21:02:49Z` | WP3 | none | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact installed bytes and path history | support-only fit retained |
| S-006 | `skill-6a920c8f...` | installed skill | yes | attribution-lock 1.2.0; SHA `4da572c9...`; no diff after baseline | `21:02:49Z` | WP3 | none | `RECOVERABLE_CONFIRMED` | `SELECTED_VALIDATED` | exact installed bytes and path history | read-only support fit retained |
| W-001 | `/workspace/scratch/040256eb5cd7` | local recovered workspace | yes, bounded candidate tree | local postflight snapshot `579cf3c7ef0863a27a00798574f4c1e4c553cf7f963ea666ba207e6e38a1b4c2`; prompt-set SHA `86733a26...` | `20:45Z` | WP0–WP8 | RF-001–RF-006 | `PARTIAL_RECOVERABLE` | `DRAFT_CANDIDATE` | exact files match Drive/Git/Notion lineage | scratch path may not persist; not a Git worktree |
| W-002 | `/workspace/scratch/433e98ff98ff` | older local workspace | bounded metadata only | different earlier release lineage | `20:45Z` | inventory | none | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | distinct release identity/content | not attributed to current failed session |
| W-003 | Git worktree registry | Git metadata | yes | 1 live main worktree; 12 prunable missing-path registrations | `20:45Z` | inventory | none | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | `git worktree list --porcelain` | stale entries not cleaned; creators not attributed |
| V-001 | `audit_work/fresh-flowmaster-candidate-validation.json` | deterministic validation receipt | yes | SHA `c5aee855...`; `FLOWMASTER_SUITE_PASS`; 0/0/0/0 findings; 55 candidate prompts; 121 GCFPE cases; 46 R1 rows | `20:44Z` | WP5 | RF-002 limitation | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | exact candidate root and installed validator | does not query external Drive raw bytes |
| V-002 | `WGA-GCFPE-REPAIR-RECOVERY-20260914-Evidence.json` | targeted governance evidence | yes | SHA `27939fd3...`; verdict `FAIL`; 6 findings | `20:54Z` | recovery audit | RF-001–RF-006 | `RECOVERABLE_CONFIRMED` | `EVIDENCE_ONLY` | primary skill deterministic output plus semantic packet | local audit evidence summarized in Drive deliverables |
| V-003 | `candidate/postflight/GCFPE-20260914.1-Independent-Governance-Postflight.{json,md}` | local failed-session postflight | complete local packet | declared PASS; snapshot `579cf3c7...`; checkout `517039dc...` | file mtime `19:18:11Z` | WP6 | RF-001, RF-002, RF-005 | `PARTIAL_RECOVERABLE` | `EVIDENCE_ONLY` | exact recovered workspace and internal receipts | not final durable gate; wrong source digest; plan later says pending |
| V-004 | `candidate/drive/HDE-EPIC040-PR04-PR10-Alpha-Resumption-Handoff-v1.0-DRAFT-NONOPERATIVE.md` | local handoff draft | yes | SHA `c4791d3e18160ef47b27c2702c15434fd6945d0a390875fd20cf8db8dfe070a2` | file prepared `18:53:35Z` | WP8 | RF-002 | `PARTIAL_RECOVERABLE` | `DRAFT_CANDIDATE` | exact candidate lineage and explicit `do_not_invoke` | not uploaded/read back; wrong PF10 hash; release unselected |

## Required-deliverable classification records

```yaml
classification_denominator: approved_plan_required_deliverables_1_through_16
records:
  - {id: RD-01, item: pinned_source_manifest_and_hashes, work_package: WP0, classification: PARTIAL_RECOVERABLE, lifecycle: EVIDENCE_ONLY, evidence: [D-001, D-002, D-003, D-008, A-009], findings: [RF-001, RF-002]}
  - {id: RD-02, item: candidate_catalog_and_graph, work_package: [WP1, WP2], classification: PARTIAL_RECOVERABLE, lifecycle: VALIDATED_UNSELECTED_CANDIDATE, evidence: [C-001, D-009, D-010, D-011], findings: [RF-002, RF-004]}
  - {id: RD-03, item: prompt_impact_and_disposition_ledger, work_package: WP2, classification: RECOVERABLE_WITH_REVALIDATION, lifecycle: VALIDATED_UNSELECTED_CANDIDATE, evidence: [D-013, D-014], findings: [RF-002]}
  - {id: RD-04, item: PR_30_and_PR_35, work_package: WP2, classification: RECOVERABLE_WITH_REVALIDATION, lifecycle: VALIDATED_UNSELECTED_CANDIDATE, evidence: [C-004, C-005, V-001], findings: [RF-002]}
  - {id: RD-05, item: RS_20_RS_30_RS_40, work_package: WP2, classification: RECOVERABLE_WITH_REVALIDATION, lifecycle: VALIDATED_UNSELECTED_CANDIDATE, evidence: [C-006, C-007, V-001], findings: [RF-002]}
  - {id: RD-06, item: PR_20_and_PR_40, work_package: WP2, classification: RECOVERABLE_WITH_REVALIDATION, lifecycle: VALIDATED_UNSELECTED_CANDIDATE, evidence: [D-013, D-014, V-001], findings: [RF-002]}
  - {id: RD-07, item: MGMT_and_PE_Metaprompt, work_package: WP2, classification: RECOVERABLE_WITH_REVALIDATION, lifecycle: VALIDATED_UNSELECTED_CANDIDATE, evidence: [C-003, D-014, V-001], findings: [RF-002]}
  - {id: RD-08, item: writer_and_qualifying_producer_audit, work_package: [WP2, WP5], classification: RECOVERABLE_WITH_REVALIDATION, lifecycle: EVIDENCE_ONLY, evidence: [D-015, V-001], findings: [RF-001, RF-002]}
  - {id: RD-09, item: pr_development_skill_bundle, work_package: WP3, classification: RECOVERABLE_CONFIRMED, lifecycle: SELECTED_VALIDATED, evidence: [S-004, D-018, V-001], findings: []}
  - {id: RD-10, item: aligned_skill_and_validator_contracts, work_package: WP3, classification: CONFLICTING_OR_UNSAFE, lifecycle: SELECTED_UNVERIFIED, evidence: [S-001, S-002, S-003, S-005, S-006], findings: [RF-002, RF-003]}
  - {id: RD-11, item: procedure_catalog_register_hubs_checklist_alpha_successors, work_package: WP4, classification: PARTIAL_RECOVERABLE, lifecycle: VALIDATED_UNSELECTED_CANDIDATE, evidence: [C-001, C-002, D-012, D-014], findings: [RF-002, RF-004]}
  - {id: RD-12, item: deterministic_fixtures_and_semantic_readback, work_package: WP5, classification: RECOVERABLE_CONFIRMED, lifecycle: EVIDENCE_ONLY, evidence: [D-011, D-016, D-017, V-001], findings: []}
  - {id: RD-13, item: independent_governance_postflight, work_package: WP6, classification: PARTIAL_RECOVERABLE, lifecycle: EVIDENCE_ONLY, evidence: [V-003, D-026], findings: [RF-001, RF-002, RF-005]}
  - {id: RD-14, item: promotion_and_intact_archive_report, work_package: WP7, classification: NOT_FOUND, lifecycle: NOT_STARTED, evidence: [D-019, D-020, D-021, D-022, D-024, D-026], findings: [RF-005]}
  - {id: RD-15, item: post_promotion_validation_report, work_package: WP7, classification: NOT_FOUND, lifecycle: NOT_STARTED, evidence: [], findings: [RF-005]}
  - {id: RD-16, item: saved_read_back_PR04_PR10_handoff, work_package: WP8, classification: PARTIAL_RECOVERABLE, lifecycle: DRAFT_CANDIDATE, evidence: [V-004], findings: [RF-002, RF-005]}
```

## Finding records

```yaml
findings:
  - recovery_id: RF-001
    governance_id: WGA-GCFPE-REPAIR-RECOVERY-20260914-0006
    rule_id: SRC-003
    severity: BLOCKER
    subject: GCFPE-20260914.1-PHASE-A
    state: OPEN
    evidence: [A-009, D-002]
  - recovery_id: RF-002
    governance_id: WGA-GCFPE-REPAIR-RECOVERY-20260914-0002
    rule_id: ART-002
    severity: ERROR
    subject: PF10-DIGEST-PROPAGATION
    state: OPEN
    evidence: [A-009, S-002, S-003, V-003, V-004]
  - recovery_id: RF-003
    governance_id: WGA-GCFPE-REPAIR-RECOVERY-20260914-0005
    rule_id: SKL-001
    severity: ERROR
    subject: CHANGE-FLOW-AND-FLOWMASTER-CANDIDATE-BINDINGS
    state: OPEN
    evidence: [G-001, S-002, S-003]
  - recovery_id: RF-004
    governance_id: WGA-GCFPE-REPAIR-RECOVERY-20260914-0003
    rule_id: CTR-001
    severity: WARNING
    subject: CANDIDATE-CATALOG-AND-REGISTER
    state: OPEN
    evidence: [C-001, C-002]
  - recovery_id: RF-005
    governance_id: WGA-GCFPE-REPAIR-RECOVERY-20260914-0004
    rule_id: PUB-001
    severity: BLOCKER
    subject: GCFPE-20260914.1-PROMOTION-GATE
    state: OPEN
    evidence: [D-026, V-003]
  - recovery_id: RF-006
    governance_id: WGA-GCFPE-REPAIR-RECOVERY-20260914-0001
    rule_id: ART-001
    severity: WARNING
    subject: GCFPE-20260914.1-RECOVERY-CHECKPOINT
    state: OPEN
    evidence: [D-025, W-001]
source_change_check:
  SRC-002_observed: false
  rechecked_sources: [A-001, A-002, A-003, A-004, A-005, A-006, A-007, A-008, A-009, C-002]
safe_recovery_point:
  earliest_unmet_dependency: WP0_TASK_2_EXACT_SOURCE_HASH_AND_REPRESENTATION_PINNING
  workspace_to_rediscover_first: /workspace/scratch/040256eb5cd7
  prohibition: DO_NOT_ENTER_WP7_OR_RESUME_ALPHA
```

`<eof>`
