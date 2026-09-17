---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-EPIC040-PR02-PR-IMPLEMENTATION-RESULT
artifact_version: 3.0
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
created_at_utc: 2026-09-13T19:11:45Z
---

# HDE-EPIC040-PR02 — Resumed PR Implementation Result v3.0

## 1. Outcome

**RESCOPE_PENDING — Not ready to merge.** The same PR02 directory and original Git identities are recovered. The approved/drained F01 and F02 correction and the later user-authorized archive untracking are preserved locally. Focused validation records 562 passes and one manifest-dependent failure; default regression records 1,800 passes and three existing skips. Eight of nine writer/evidence checks pass. The remaining check proves an explicit scope conflict, not a missing file or an unverified PF10 drain.

Exactly one new complete formal request has been saved and read back: [HDE-EPIC040-PR02-F03-rescope-request-v1.0.md](https://drive.google.com/file/d/1iKB5nFqGNXM8fbAZiC2tItvP8nVA3LaZ/view?usp=drivesdk), ID `HDE-EPIC040-PR02-F03-RESCOPE-REQUEST`, v1.0, SHA-256 `3939035a85b3697d2816e9d0b799326d746b0b878f2aa08fce7c386eca1a294f`. It contains the exact proposed maintenance exception, complete native inputs, all preserved constraints, test evidence, and the full 47,076-byte current textual correction plus exact archive deletion identities. This result is a complete successor to linked Result v2.0; that predecessor and original Result v1.0 remain immutable.

F02/PF10 §2.9 requires each of four named modules—including `engine/serializer/canon.py`—to retain the actual top-level executing code object. The prepared local implementation of that approved predicate changes the wrapper from 485 to 795 bytes while retaining the shared serializer behavior; the code itself has not received independent approval. The same F02 overlay expressly freezes the actual 15-member manifest in PR02. That manifest already lists this wrapper with the old exact hash and size.

The unchanged owning gate `scripts/release_id_recompute.py::manifest_only_problems` audits actual bytes of every listed member. It reports exactly one mismatch: the wrapper. The other 14 member bindings still match. The existing canonical JSON gate's `_validate_release_manifest_snapshot` independently refuses `release_manifest_member_integrity_mismatch`, causing the one targeted fixture-proof failure. The CI release lane runs `python scripts/release_id_recompute.py --check-manifest-only`, so publishing this known state cannot satisfy required CI.

This conflict is now established from actual code and local gate results. It was not identified in the approved F02 request/review's feasibility treatment; those documents required both provenance-bearing modules and an unchanged 15-member manifest. It is separate from F01's Gate-schema closure, from the restored `.bytes` evidence file, and from the user-authorized archive removals.

Two bounded diagnostics test the ordinary alternatives without changing the repository manifest. Passing an in-memory one-row refreshed manifest to the existing snapshot validator succeeds using its own temporary fixture/canonical check. Restoring the exact old wrapper bytes only in an isolated 44-member test fixture makes active admission refuse `EXECUTION_PROVENANCE_UNAVAILABLE`. Thus simply restoring the old wrapper does not implement the approved F02 predicate. No captured source was executed by the production admission comparison; fixture imports are ordinary isolated test execution.

Removing provenance, substituting function-only/source-hash proof, weakening the integrity check, retaining unmanifested old source or introducing import/deployment machinery would change or evade the approved boundary. Deferring PR02 acceptance until PR06 would conflict with their dependency order. The smallest proposed correction is an explicit source-row maintenance exception with bounded owning evidence convergence. It requires the same IA's decision because the engineer cannot change the explicit current-manifest prohibition.

## 2. Immutable base and overlay lineage

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

Specification v1.1 remains Thoth-17 APPROVE, 2026-09-08T13:23:24Z; whole-change Plan/review v2.1 remain immutable, with Isis-50 APPROVE at 2026-09-09T13:36:43Z. No new Plan, Instruction or Proceed was created.

## 3. Verified PF10 drain

Current authoritative source: [PF10-HDE-Build-Notes-v13.2.2.md](https://drive.google.com/file/d/1suxrnM-g96R3tqThIpND3ll9s1qKaopK/view?usp=drivesdk), 116,473 bytes, SHA-256 `d1db160a6a10aac25ed034e820f7026537cc9d178f22e8e978ed1620a61b0bec`. It was independently resolved through Glow / Core Docs / PFCanon, with direct parent `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3`; only one current controlled PF10 Markdown was selected. Native Google Docs and repository PF copies were not substituted.

Nathan's invocation asserts his completed manual drain. The engineer independently compared the complete body beginning `## 2.9 HDE-EPIC040-PR02-F02 — Executing-Code Coherence Rescope` with the approved F02 addendum. Substantive content matches. Raw Markdown is not byte-identical: emphasis, escaped punctuation, self-label links, table alignment, list markers and whitespace differ. The terminal PF10 `<eof>` marker is outside the addendum and excluded. No substantive clause is waived; the standalone YAML transport envelope is not treated as page body. F01 §2.7 remains byte-identical to its section in pre-F02 PF10 v13.2.1; §2.8's form rule remains present.

The review's historical state `APPROVED_PENDING_MANUAL_PF10_DRAIN` and the standalone addendum's `READY_FOR_MANUAL_DRAIN` / `NON_CANONICAL_PENDING_MANUAL_DRAIN` labels remain source metadata. The current PF10 body and independent comparison establish the effective overlay. F01 and F02 are approved and drained; F03 is new and unapproved. No PF10 edit or addendum was made by this engineer.

## 4. Same session, worktree, branch and PR

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

## 5. Work prepared under effective F01/F02 authority

The coherent local correction is prepared, uncommitted and preserved; independent corrected-candidate review and merge readiness are not claimed.

- F01: `schemas/gates_v1.schema.json` is a manifest-bound required member; `_load_gates` executes the existing owning schema validator on captured Gate bytes before active admission. Captured schema identity, canonical bytes, local references and relational checks remain enforced. Missing, rejecting, malformed and unbound schema/member cases remain covered.
- F02: the synthetic complete roster is exactly 44. It adds `engine/stable/sercanon.py` and `engine/categories/registry.py` to F01's 42. All four named modules retain their actual top-level execution code and origin/compilation provenance. Admission validates the four actual owners, safe common origin and matching interpreter/optimization semantics, then compares retained code with compilation of exact captured manifest-bound bytes using `dont_inherit=True`. Captured source is not executed or reimported.
- The shared serializer wrapper, underlying serializer and category registry remain their owners. The prior duplicate serializer, copied category order and import-time disk hash attempt were removed from the current correction. Their complete prior state remains recoverable in the predecessor F02 request and the original four-file snapshot.
- Ordinary repair 3997351895: the packaged manifest is captured once and final verification uses its retained metadata instead of physically rereading it. A descriptor-level `os.open` observation checks one physical manifest open on success, malformed manifest, member hash failure and manifest change after capture. Other members retain rereads and the complete final identity pass.
- Existing symlink refusal, inter-read mutation detection, recursive freezing, no fallback and the explicit non-atomicity limit remain. Public admission fixes the verified execution root. The existing private fixture seam can use copied identical implementation bytes, still requiring all four executable comparisons.
- Tests cover fresh public imports at optimization levels 0/1/2; materially changed captured source for each module; source replaced after import; timestamp-valid stale bytecode A versus source B, with actual A/B behavior and fresh B separately checked; unsupported provenance, live origin disagreement and real deployment symlinks; 42/43/45 roster refusal; helper absence/format/hash/size/change/symlink refusal; unavailable captured members; actual shared consumers; and physical manifest read counts.
- The existing CI classifier registers exact ownership for the added tests/owners and the exact five retired archives; `.gitignore` conservatively selects full validation. It does not change workflow triggers, suppress required tests, or exempt the manifest check.

The claim remains executable-code equivalence for four modules, distinct from exact source/config/manifest/release identities. It is not exact historical imported-source byte identity, universal runtime integrity, arbitrary in-process tamper resistance, process-death atomicity, multi-file atomic visibility, cross-process locking or stronger deployment portability. The actual 15-member manifest is still byte-for-byte unchanged and production active admission remains incomplete until PR06.

## 6. Requested archive cleanup and bytes-file disposition

Nathan's later request, “can you remove the archives, or at least untrack them?”, explicitly authorizes this separate housekeeping change. Exactly these five paths were untracked locally and receive exact ignore entries. Deletions are staged; no remote deletion or history rewrite has occurred. These are archive removals, not deletion of current primary evidence. Historical inventory references remain historical and were not edited.

| Retired archive | Historical bytes | Recorded Git blob |
| --- | ---: | --- |
| `.backup_epic004/changelog_20251024121758.tgz` | 3377 | `8a42139545e06ced6540fb749755bc334d2b583b` |
| `_backup_1761350008.tgz` | 82375 | `fea562083cb704e60a00f634b3022919aeb9c413` |
| `_backup_corrupted_1761349750.tgz` | 94584 | `14fb708b5ee17627f4025a05083444eb36244716` |
| `_backup_corrupted_1761349780.tgz` | 96598 | `2f0a423cd24e736749a89c3bae7e12157a14910b` |
| `handoff/epic004_live_evidence_20251022T202304Z.tar.gz` | 368739 | `49977f3d57d9a6d7df04d0697902f8bd159a52b6` |

`artifacts/engine/order/abba_identity.bytes` is not an archive. It is the generated 32-byte SHA-256 digest used by the AB↔BA ordering-evidence family, its index/path proofs and `tests/order/test_ordering_artifacts_stability.py`. It is not loaded by active mechanics admission. It was kept and restored through `tools/order/generate_ordering_artifacts.py`, after proving the other owning outputs already matched. Its SHA-256 is `5dd560e80a411b3e428d4f8190740f269c1020b401410129b28d55ab803e2ae2`; its Git blob is `0949b8e6d0ee5fc2e50fcace9decb7cda74964e0`. It has no tracked diff. This restoration supplies required evidence bytes; it does not create new acceptance evidence.

## 7. Current local source identities and worktree state

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

There are 16 local changed paths and 20 cumulative base-to-candidate paths. The complete textual diff relative to `eed8a63807f573abc29de6f6d5ceac54f0c8da85` has SHA-256 `a2644c0e7c8b802c274e46c8074db569e1e02e7c339f9188ac73a5690bae8af2` and is embedded in the read-back F03 request. Five staged deletions are not content-reconstructed from unavailable archive blobs. The initial four-file recovery delta remains unchanged in its pre-recovery snapshot and is durably preserved by the predecessor F02 request; current modifications are attributable continuations, not a replacement implementation.

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

The actual 15-member manifest remains exactly `c0f5f24fbbcbb04d01d1613be386c26fddbfb37d53cbb0f9c65d5cf55e97c2a4` / 1,981 bytes and equals its published-head bytes. The ordering digest is restored exactly with no tracked change. The workspace is not clean/committed; all observed differences are explicitly accounted for. No generated evidence was hand-edited and no current manifest, PFCanon document, original workspace or prior approval was mutated.

## 8. Tests, governed checks and changed-path proof

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

## 9. Substantive review and CI state

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

## 10. New F03 request and bounded decision scope

The requested decision is a narrowly bounded exception to the actual-manifest freeze, not a replacement Plan or a new source/execution design. The following is **proposed and not implemented**:

1. Permit PR02 to rebind only the existing `engine/serializer/canon.py` row in `catalog/manifest.json` to the exact final reviewed provenance-bearing wrapper bytes, using the existing canonical manifest writer. Change only that row's `sha256` and `size`. Keep the actual roster at 15, preserve its other 14 rows, ordering, `root`, `version` and `built_at_utc`, and add no F01/F02/future member to the actual manifest in PR02.
2. Keep `release_id = sha256(exact manifest bytes)` and all separate source/config/manifest identities. A source-row refresh necessarily changes the manifest/release identity value; do not keep a stale release identifier or mislabel this as byte-unchanged. On the present preserved candidate, the old row is `f56cdacfb90b7d9cb467d7e6005ad62e62e83d4b04c022c53e9f9b190e7777c3:485` and the proposed row is `2a077c957c7526f9c0fe9c482d299b6912df05b084fa5fc9c5f63b555e23eec5:795`. The unchanged actual manifest is `c0f5f24fbbcbb04d01d1613be386c26fddbfb37d53cbb0f9c65d5cf55e97c2a4` (1,981 bytes). An in-memory one-row refresh has proposed manifest/release SHA-256 `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856` (1,981 bytes). These candidate values are evidence, not a fixed future hash independent of final review corrections.
3. Permit only the corresponding existing canonical JSON gate/evidence maintenance required by this source-row refresh. The gate owner is `tools/evidence/run_canonical_json_gate.py`; its six current outputs are `audit/gates/canonical_json/json_canonical_check.log`, `audit/gates/canonical_json/json_canon_compare.log`, `audit/gates/canonical_json/canonical_json.gate.json`, `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`, `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`, and `audit/gates/json_gate/canonical/json_gate_structured_record.json`, with their owned `.path_proof.txt` companions. The sole evidence updater owns any resulting INDEX/Mirror/checksum/orientation/path-proof convergence in its existing families. Do not hand-edit evidence, recapture historical vendor/QA/Ops/CLI inputs, rewrite capture-time identity claims, introduce a new evidence family, or refresh unrelated artifacts. An additional required identity/evidence family outside this explicit closure requires its owning decision rather than an open-ended cascade.
4. Preserve all strict manifest content, canonical JSON, ownership and CI checks. No special-case waiver, ignored serializer row, xfail, narrowed assertion, fake hash, unmanifested old-source authority, import hook, loader/reload scheme, `sys.modules` mutation, duplicate serializer or altered deployment protocol is proposed.
5. PR02 remains responsible for its F01/F02 implementation, this one existing-row maintenance exception, corresponding local tests and exact-head review/CI. PR06 retains the final complete **44-member** actual-manifest materialization, complete member refresh, final identity recomputation/convergence and eventual promotion after PR03–PR05. The proposed exception does not move final 44-member promotion to PR02 or change unit order. PR03–PR05 and PR07 retain their existing owners and scope.
6. Keep Specification intent, requirement wording, mathematics, taxonomy, public/API/CLI contracts and identity formulas unchanged. K040-REQ-007/008/009 and existing K040-REQ-011/012 evidence/ownership duties require reconciliation of the actual maintained source and manifest; AC040-04/05 retain their existing PR02 versus PR06 completion split. No PR01 rerun, QA/Ops, live vendor/database work, release activation, deployment, merge, PF10 edit or Epic closure is authorized.
7. If the same IA approves this exact bounded exception, it produces one native RESCOPE_REVIEW and exactly one separate page-ready PF10_BUILD_NOTES_ADDENDUM under the current form rule. Nathan alone manually drains and verifies it. Only then may the same PR02 session resume via selected RS-40 under the original Proceed and apply that explicit exception.

The IA must decide whether this is a permissible bounded implementation/evidence-maintenance overlay within the approved Specification, and expressly reconcile the existing unchanged-manifest clause. This engineer does not self-approve it. If the proposed closure is insufficient or conflicts with a remaining owning rule, return precise bounded redlines or the actual Product Owner/Specification question through the native selected result; do not approve an unspecified integrity mechanism or assume permission to rewrite historical evidence.

## 11. Carried Canon-conflict register

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

## 12. Truthful return and recovery action

Sole next destination: [RS-20 — Review Bounded Work-Unit Rescope — 091326.2](https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb?pvs=204), in the same continuing whole-change HDE-EPIC040 IA that issued F01/F02. Review the exact read-back F03 request. No downstream prompt was executed, no replacement IA/PR session created, and no approval owner impersonated. The original Product Owner Proceed remains the existing implementation authority; a new exception still requires the native IA decision and Nathan's verified PF10 drain before this engineer can rely on it.

If a bounded exception is approved and drained, return to selected RS-40 in `PR-02 HDE-EPIC040` with this same recovery directory/branch/PR/head and preserved delta, then complete actual local validation, one coherent candidate publication, substantive current-head code/security review, applicable owner dispositions and exact-final-head CI. Do not reuse historical green CI for changed source, waive a failed integrity gate or merge. No conditional PR-40 handoff is emitted because genuine merge readiness is not established.

## 13. Prompt-use evidence

Usage `GCFPE-USE-HDE-EPIC040-PR02-RS40-F02-20260913-02`: RS-40 / 091326.2, [exact selected page](https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3?pvs=204), retrieved page revision 2026-09-13T11:35:51.889Z. Role/stage: continuing PR02 engineer, approved F01/F02 implementation, local validation and F03 boundary return. Exact Specification v1.1 and work-unit/component/requirement references are carried above. Capture/result time `2026-09-13T19:11:45Z`; selected release GCFPE-20260913.1, 54 members, [selection register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1?pvs=204). Runtime model configuration is not a routing or approval field. Prior uses remain retrievable in linked Results v1.0/v2.0 and reviews; none are overwritten.

RS-20 / 091326.2 was fetched for receiver compatibility only (page revision 2026-09-13T11:33:42.699Z), not executed and no other session was messaged. Repository prompt-use persistence remains pending/non-gating: no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` writer/procedure was found. The next authorized repository writer must use an actually installed supported schema; no new process file or fabricated record was committed.
