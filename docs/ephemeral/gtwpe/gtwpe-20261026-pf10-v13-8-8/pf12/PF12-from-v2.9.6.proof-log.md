# Proof log — revised PF12 from v2.9.6 (gtwpe-20261026-pf10-v13-8-8, T-PF12)

This proof log documents how the revised PF12 file was created. It is the TW-APPLY-10 application report. The revised PF12 is a working file under `docs/ephemeral/`, not an authoritative publication: `docs/pfcanon/` was not written, and canon transfer is the Product Owner's manual action. Nothing here establishes QA, acceptance, canon adoption or closure.

## 1. Artifact and outcome

| Field | Value |
| :- | :- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf12/PF12-from-v2.9.6.md` |
| Artifact identity | `PF12-Canon-HDE-Schemas-and-Artifacts` v2.9.7; 640,642 bytes; 6,264 LF terminators, the last line empty (ends `LF LF`); no CR; valid UTF-8; SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`; Git blob `d5bc01f83078bebe04f0854385317b47c1cd2de3` |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf12/PF12-from-v2.9.6.proof-log.md` |
| Outcome | Application SUCCESS: thirteen content operations and the three-field derived document-control plan applied; every verification in §7 passed |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b, fetched live on 2026-10-26 (page last edited 2026-10-09T11:05:22Z), the version and page the handoff names |
| Run identity | `gtwpe-20261026-pf10-v13-8-8/T-PF12/apply-run-1` |
| Applier | The same Claude Code cloud session as the preparer, https://claude.ai/code/session_01AaKkpYtrGxYudeyWaEnMX3. Nathan's T-PF12 handoff authorizes TW-DRAIN-10 then TW-APPLY-10 in this one session; each step ran under its own live-fetched prompt. No subagent, reviewer or other session took part |
| Execution date | 2026-10-26 (UTC, container clock `2026-10-26T22:01:08Z` at application) |
| Destination | Branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, shared draft PR https://github.com/amthorn78/glow-hdengine-v2/pull/761 |

## 2. Inputs and identities

| Input | Identity | How it was obtained |
| :- | :- | :- |
| Exact original (baseline) | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`, `PF12-Canon-HDE-Schemas-and-Artifacts` v2.9.6, Canon, effective 2026-10-09; Git blob `1542a8f78846fcdd684f6a4dec7b663616ec8c02`; 622,934 bytes; 6,096 LF; raw UTF-8 SHA-256 `5bf86058e30c4cfd7dbaa9532b169d9a9b0e3d64089abc254a75bbf162a2227d` | `git show origin/main:<path>` at `0838ba08254eaefc888019df49a06aa2ae99cc6c`, re-fetched immediately before application; byte-identical (`cmp`) to the baseline the preparer read in full and to the handoff baseline `9dda63dd`. `main` carries no newer PF12 version |
| Redlines package | `pf12/redlines-PF12-from-v2.9.6.md`; Git blob `d5673b3282f989d7c8aac4fb8d6d61c588782b79`; 48,813 bytes; 579 lines; SHA-256 `1fa231e84222d61d080cf51de5539de5cb02c9c3e1efe50467a12ff44a8e0dee` | Read in full from the pushed commit `8af0831` with `git show`, and equal to the working tree |
| Preparation evidence | `pf12/redlines-PF12-from-v2.9.6.proof-log.md`; Git blob `2619bcf07f6a477b3d79b71632ef58617c1fa1ef`; 27,170 bytes; 230 lines; SHA-256 `ad9e11470bfc71fe962bebcc72055347c37b984c46510ae46ec0ce9331348815` | Same commit; read in full |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, task T-PF12, rows A07, A08, A24, A25, A26, A15, A16, A17 with X03 and S-APR, and S-CR3 | Verified against the handoff: same target, rows and sections |

## 3. Preparation-state verification

- **Preparer and run.** Originating preparer: TW-DRAIN-10 100926.1 in this session; preparation run `gtwpe-20261026-pf10-v13-8-8/T-PF12`, preparation revision `P1`.
- **Outcome and save state.** The package records `READY` and `COMPLETE_PACKAGE` (preparation proof log §11), written only after both files were saved and read back. The redlines end with `END OF REDLINES` and one LF.
- **Coverage.** The preparer read the whole target in 27 hash-matched windows whose concatenation equals the baseline bytes (preparation proof log §3), and read each selected source unit completely at its stated boundary (§4). This Apply step reuses that complete reading against the same verified baseline bytes and re-read the redlines and preparation evidence in full.
- **Unresolved items.** None blocking. Held items touched: none (ledger H-01, FND-021, is recorded and not drafted; H-02 to H-06 do not bear on PF12). Observations O-1 to O-6 are recorded as not drafted and need no Apply action.
- **Selected scope.** The package's source boundaries match the handoff and the ledger rows (§4 below); no unselected PF10 addendum was required.

## 4. Selected sources and boundaries

| Ref | Source | Boundary used |
| :- | :- | :- |
| SR1 | HDE Build Notes v13.8.8, `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f` | front matter 1–223; addenda 2.7 (688–889), 2.8 (890–1002), 2.15 (1620–1690), 2.16 (1691–1825), 2.17 (1826–1955), 2.24 (2693–2790), 2.25 (2791–2899), 2.26 (2900–2986); 2.18 (1956–2081) as supporting reading for the withdrawn ceiling passages |
| SR2 | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, blob `c4802a5a7fa3` | S-APR 147–193; CR-3 221–230 |
| SR3 | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, blob `9408d6ed091b` | C-8 to C-12, overlaying SR2 |
| X03 | `docs/adr/hde/close_pack_writer_adr.md`, blob `2d91679a1981` | Decision section and the canon table, lines 76–88 (supporting cross-reference) |
| X10 to X14 | Specification review, closure decision `HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md` (blob `2260eae17974`), post-closure record, QA-120 report, close report | closure evidence: HDE-CRD-0002 is closed |

Supporting reading recorded by the preparer and relied on for this application: Technical Writing Best Practices (`PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, read in full); HDE Governance §9.1.1 and §1.1; HDE-CLI-API-Vendor-Ref §5.6 and the start of §5.7; HDE Architecture §3.5; HDE Users Guide §1.1; Plan Templates (`pf27.step_log_header.v2`); and read-only inspection of the repository surfaces the package lists at `0838ba0c`.

## 5. Application operation ledger

### 5.1 Mechanics

All operations are `REPLACE` with expected non-overlapping count 1 in the whole original, observed 1. Offsets are UTF-8 byte offsets, half-open.

| ID | Original lines | Original bytes | Revised lines | Revised bytes | OLD bytes | NEW bytes | NEW SHA-256 |
| :- | :- | :- | :- | :- | -: | -: | :- |
| M-1 | 6 | 114–135 | 6 | 114–135 | 21 | 21 | `04fbeb8bf16f95c7b747164b80205e115f88cbcb365692103ef4b168f7d45d3e` |
| M-2 | 8 | 156–188 | 8 | 156–188 | 32 | 32 | `4591a55835de189fe86f99c4901a923a04c0f4860208d9244f8d87bbfd1a5892` |
| M-3 | 9 | 189–310 | 9 | 189–314 | 121 | 125 | `f59628f5620292328afeb5ed3e95dd80ade3a9c068e7dd04fd20b9e12bb61cd0` |
| RL-001 | 590 | 45,010–45,243 | 590 | 45,014–45,397 | 233 | 383 | `ef403e26c2908a5980d00043e16428371bad72b209c9df2118f56dcbd188fccc` |
| RL-002 | 595 | 45,796–46,011 | 595–607 | 45,950–48,879 | 215 | 2,929 | `5bbb14155731f9b817e365478dffc5272e943a854f1019b2055784680a1f96b5` |
| RL-003 | 654 | 50,937–51,167 | 666–668 | 53,805–54,778 | 230 | 973 | `9336d2f610f87dda92db125493f9a52dc24a1c9e4d9056e96e7427b72f580269` |
| RL-004 | 926 | 85,914–86,020 | 940–944 | 89,525–90,366 | 106 | 841 | `b3a77c50bd260f016a0355a9ac7f887d1e378e47e945a93d9c39e8d6aeca24f1` |
| RL-005 | 2318 | 210,362–210,625 | 2336 | 214,708–215,661 | 263 | 953 | `81af8e0417481fc12666916c8f0c5b35336a71038d13f9392b86963b6281dbfa` |
| RL-006 | 4708–4709 | 528,519–528,983 | 4726–4727 | 533,555–534,127 | 464 | 572 | `ec5e05e38046543994d6100fdba6f6599784b8546ca73add671a8110cf40aa97` |
| RL-007 | 4716 | 529,297–529,482 | 4734–4738 | 534,441–535,235 | 185 | 794 | `8126bc33e4669b8c683bd3f6226de37a240a54d7b7154ce23af666c25f1e99b0` |
| RL-008 | 4720 | 529,516–529,730 | 4742–4755 | 535,269–537,767 | 214 | 2,498 | `a86f2b3573f2c494d8660072db2082a60598429880c5aa019df06430d63f3c66` |
| RL-009 | 5273 | 572,992–573,179 | 5308 | 581,029–581,363 | 187 | 334 | `f5691ba9ce2bcb28240b8cea440e3703e50b6a160833a7b61764bc7a9c8f4736` |
| RL-010 | 5362 | 579,891–580,043 | 5397–5408 | 588,075–590,744 | 152 | 2,669 | `5eefa1d9a8e5c87719013fdf2d9aa63ff07df86ddbd99a7834950c6a09add6dd` |
| RL-011 | 5377 | 580,629–580,827 | 5423–5424 | 591,330–591,736 | 198 | 406 | `f6fe42dfc7efbb5385f859aa70a860e16414c206ab14f95e3e0d1479b86a6775` |
| RL-012 | 5395–5396 | 582,032–582,368 | 5442–5443 | 592,941–593,360 | 336 | 419 | `216c3987e59ee0d90348e35de48fe8e3a6fa02b4c1eee57e76cf9ebde81985e7` |
| RL-013 | 5994–5995 | 614,207–614,271 | 6041–6163 | 625,199–631,979 | 64 | 6,780 | `29091cfe2f7328bcd3c41dccc898d9a14b09d8517390a7ba794ee5e04413f842` |

Every NEW SHA-256 above was recomputed from the applied payload; for RL-001 to RL-013 each equals the value stated under its NEW literal in the redlines package.

### 5.2 Basis for each operation

Each basis restates the preparer's rationale and its source-ledger reference (preparation proof log §6; redlines "Controlling basis and rationale").

| ID | Sections changed | Source rows | Basis |
| :- | :- | :- | :- |
| M-1 to M-3 | §0.1 Header | TW-APPLY-10 document-control contract; package §8 header provenance | Version bumped once by the established patch scheme; effective date set to the application date; Last Update Gate set from the sources the package records (§6) |
| RL-001 | §1.2 "Change-container compatibility", second bullet | S-CR3 (CR-3, APPROVED_AS_CHANGED); CD-2 | CR-3 finds that §1.2 points to "the stable CRD ID recorded in PF30", a record HDE Governance §9.1.1 forbids the active workflow to create. The bullet now names the controlled CRD ID, assigned by the Product Owner at class selection and recorded by the approved CRD Specification (HDE Governance §9.1.1, §1.1), and states that the identity does not depend on an HDE CRD Records entry |
| RL-002 | §1.2, after the paragraph closing "Change-container compatibility" | A15 (approved design), A16 (required drainage: §1.2 "Close-pack artifacts"), A17 (amended design, routed by title), X03 (canon table row for §1.2; Decision 1 to 4, 6, 8; "Epic-only identity inventory"), S-APR (S21) | 2.15 approves one writer with a closed v2 schema for Epic and CRD identities, v1 unchanged, CRD paths of record, rendering from tracked inputs, the kept feedback-dependency refusal, requirement text by reference, and absent-tolerant CRD close-pack Index rows; 2.16 names §1.2 as required drainage. The closed Epic-only inventory comes from the ADR. Closure criteria and the closure-override treatment (2.17 resolution A) are routed by title to Change Process Guide and HDE-Governance |
| RL-003 | §1.2, after the baseline-closure-artifacts paragraph | A15 (close-run family introduced), X03 (canon table row for §1.2; Decision 7), S-APR (S21: where close-workflow run evidence lives) | 2.15 introduces the post-verdict close-run family for an admitted CRD and admits no Epic family; §1.2 states path, status and boundary, and defers membership, writer and indexing to §8.17 |
| RL-004 | §1.2 "Close-pack manifest key_outputs" | A15 (key_outputs map of path strings), A16 (S21 acceptance (1)), X03 (Decision 5) | The v2 manifest's `key_outputs` minimum: 5 to 64 string-valued entries, the key pattern and the five required keys, as confirmed in `schemas/close_candidate_source.v2.json` and HDE-CRD-0002's committed manifest. The generic map rule is unchanged |
| RL-005 | §8.3 "Allowed top-level keys and unknown-key rejection" | A24 (CR-10, alternative (a)), A25, A26 | CR-10: the mutual-exclusion rule is enforced by the canonical updater and `ci/checks/check_mirror_schema.sh` (`EPIC_CRD_EXCLUSIVE`); the Mirror skeleton test and the QA harness accept `crd_id` only, stated as a limit. `crd_id` was already an allowed key |
| RL-006 | §8.8 "Minimum required fields", classification and env_gate bullets | A07 (CR-7, AD-1; `public_aux`), A08 (required drainage), X04 (§8.8 row) | CR-7 and HDE-CLI-API-Vendor-Ref §5.6 require PF12 to register `public_aux` and the public sentinel for the Aux record; the sentinel must not appear on an internal record, as the validator enforces |
| RL-007 | §8.8, after the writer-surface key | A07 (AD-1 class (b)), A08 (aliases on the Aux record), X04 | The optional `aliases` key and its validation rules, as HDE-CLI-API-Vendor-Ref §5.6 requires and the validator enforces |
| RL-008 | §8.8, after "Minimum schema" | A07 (CR-7; AD-1 accounting rule, classes (a) to (d), canon-retired refusal; AD-6 enumeration test), A08, X04 | The Aux narrative record and the Catalog population rule: every served pair accounted for once, the four exclusion classes, the canon-retired set from HDE Architecture and HDE Users Guide, refusal of a retired or unmounted record, and the enumeration test that fails CI; route removal stays with its canon owner |
| RL-009 | §8.17 "Change-container identity", second bullet | S-CR3 (CR-3; §8.17 added by Specification review v1.0 §6); CD-2 | The same reasoning and wording as RL-001, for `<change-id>` |
| RL-010 | §8.17, after "Current-state evidence" | A15 (close-run family: path, holdings, status, writer, membership, scoped exception, no Epic family), X03 (canon table rows for §8.17; Decision 7) | The close-run family exception for admitted CRDs: the `ADMITTED_CRD_QA` table, the `pf27.step_log_header.v2` header, `PASS`/`FAIL`/`BLOCKED` posture, post-verdict status, the sole writer `publish_crd_close_run_family`, closed membership, the `close/`-only exception to the no-enumeration rule, the Index key form and Mirror role, and no Epic family |
| RL-011 | §8.17.1 "EPIC_QA_ROOT MAY contain" | A15, X03 (canon table row for §8.17.1) | The QA root contents list gains `close/`, limited to admitted CRDs and written only by the canonical updater |
| RL-012 | §8.17.1 "Directory name rules", first two bullets | A15 (members are directories named by check ID), X03 (§8.17.1) | `close/` is a structural child directory, and its member directories are named by lower-case check IDs, as the harness's `validate_check_id` requires |
| RL-013 | new §9.6 after §9.5 | §9.1 (a Doc-Delta is required for a change to governed evidence or parity rules); §9.2 template in the established form of §9.5; TW-DRAIN-10 change-history rule | The change-history entry the document's own rules require, naming v2.9.7 and the revision date 2026-10-26, citing HDE Build Notes by title only, stating that §5.3 is not refreshed, and stating no Apply outcome in advance |

## 6. Derived document-control plan and history agreement

| Field | Before | After | Derivation |
| :- | :- | :- | :- |
| Version | `v2.9.6` | `v2.9.7` | One increment of the final numeric component of the native dotted version; prefix `v` and three components kept. The previous drainage moved v2.9.5 to v2.9.6 the same way (§9.5) |
| Effective date | `2026-10-09` | `2026-10-26` | Actual application execution date, native `YYYY-MM-DD` format |
| Last Update Gate | `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md` | The sources the package records as justifying the update, in recorded source order, deduplicated, separated by `; `: PF10 v13.8.8 as `BN 13.8.8`; the approved Specification and the closure decision by filename alone (both exist on `main`). Delta 01 justified no PF12 change and is not listed; the ADR and plan v2.0 are supporting cross-references, not sources |
| Status | `Canon` | `Canon` | Unchanged; correct for the document's classification |
| Title, Invocation tag | unchanged | unchanged | No authorization to change them |

- Header labels, order, two-space line endings and every other field are preserved. Each control field occurs exactly once in the document.
- Internal restatements of the document's own version or date: only the header. The remaining `v2.9.6` occurrences in the revised PF are §9.5 history (revised lines 5882 and 6036) and the output filename `PF12-from-v2.9.6.proof-log.md` inside the new §9.6 evidence path (line 6137); none restates the current version.
- History agreement: the new §9.6 heading date, its `date: "2026-10-26"`, its `document_version: "v2.9.7"` and its change-log entry `v2.9.7 / 2026-10-26` agree with the header Version and Effective date. The new record carries every §9.2 template key except `traceability.commit`, which it replaces with `source_baseline_commit`, exactly as the established §9.5 record does.
- No explicit package header operation existed, so no duplicate authorization arose.

## 7. Exact application and preservation

- **Whole-batch validation before any edit.** An independent parser read the saved redlines file (not the preparer's in-memory payloads): thirteen `## RL-` blocks, each with Operation `REPLACE`, expected count `1`, and OLD and NEW literals whose byte counts and SHA-256 values equal the values stated under them. Every OLD literal and the three metadata spans were resolved against the unchanged original: nonempty, exactly one non-overlapping occurrence, starting at a line start and ending at a line end, at the stated context lines, NEW different from OLD and free of CR. The sixteen spans, sorted by original offset, neither intersect nor touch. No `FIND_AND_REPLACE`, `INSERT`, `DELETE`, MOVE or free-form instruction occurs.
- **Application.** The sixteen operations were applied on original offsets in descending order, each asserting that its span still held the exact OLD text, with no rematching on changed content. Raw UTF-8 was preserved; no line ending, whitespace, table, code or escape was normalized.
- **Preservation.** Every untouched original interval (17 intervals) equals the revised bytes at its computed shifted offset, and every payload sits at its computed position. The revised length equals the original length plus the sum of NEW minus OLD lengths. POSIX `diff` against the baseline reports sixteen hunks, at original lines 6, 8–9, 590, 596, 655, 927, 2318, 4708–4709, 4717, 4721, 5273, 5363, 5377, 5395–5396 and 5994, and nothing else.
- **Byte counts.** Original 622,934 bytes, 6,096 LF, SHA-256 `5bf86058e30c4cfd7dbaa9532b169d9a9b0e3d64089abc254a75bbf162a2227d`. Revised 640,642 bytes, 6,264 LF, SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`. The preparer's simulated content-only revision was 640,638 bytes; the 4-byte difference is exactly the Last Update Gate change (M-3, 121 to 125 bytes), since M-1 and M-2 keep their lengths.
- **Document checks.** EOF still `LF LF`; no CR or TAB; fences balanced with none open at EOF; exactly one `## 9.6` heading; the added text carries no Draft status language, placeholder, TODO, drafting note, editorial comment or ellipsis. The single Unicode ellipsis in the document is the pre-existing one in §5.3 (preparation observation O-4), unchanged.
- **Determinism.** A second independent run of the application on the same pushed package and baseline produced a byte-identical file (`cmp` silent).

These are text checks, not product QA.

## 8. Deviations, constraints and interpretations

- **D-1, preparation evidence label.** The preparation proof log §7 column headed "Original byte span" holds Unicode code-point offsets from its validator, not UTF-8 byte offsets; for example RL-001 is code points 44,897–45,130 and bytes 45,010–45,243. The operations bind by exact literal and count, not by offset, so application is unaffected. §5.1 above gives the byte offsets. The preparation artifacts were not changed; correcting that label, if wanted, is a preparer action.
- **D-2, preparation limits wording.** The preparation proof log §10 says no network access was used or needed. The live Notion fetch of TW-DRAIN-10 and the Git fetch of the shared branch did use the network; no product, vendor, database or Railway access occurred. The statement is corrected here rather than in the committed preparation artifact.
- **Gate interpretation.** The Last Update Gate lists the closure decision because the package records it as a source that justified the update, in the same form as the prior gate's closure decision. Apply did not add or drop any gate source.
- **History form.** The new §9.6 heading has no outer bold, unlike §9.5; the preparer chose this under Technical Writing Best Practices §8. Apply applied the payload as given and did not normalize either heading.
- **Read-back method.** The saved revised PF was read back completely as bytes and verified against the reconstructed expected byte stream; every changed region (the header and the sixteen hunks) was also read as text from the saved file. Untouched intervals are proven byte-identical to the baseline the preparer read in full.

## 9. Unresolved items and observations

- Preparation observations O-1 to O-6 (preparation proof log §9) remain open and undrafted, for the Product Owner: §5.3's stale release_id; the PF30 wording in §0.2 and the §8.3 `crd_id` bullet; damaged `audit/qa/\\/` placeholders in §8.17; the §5.3 Unicode ellipsis; the `docs/ENDPOINTS_CATALOG.json` symlink; and the unlisted `description` field.
- O-7 (noticed at read-back, pre-existing, not changed): §8.17.1's QA-root paragraph (revised line 5418) says per-check directories under `checks/` "are exempt from the lower-case rule", while its "Directory name rules" require that slug to be lower-case ASCII, in the baseline as well (original line 5396). Suggested route: Product Owner.
- Held items touched: none.

## 10. Limits

- Repository statements rest on static inspection of checked-in bytes at `0838ba0c`; no test, validator, writer or updater was executed. Closed rails were kept (`SAFE_MODE=1`, `ALLOW_NETWORK=0` defaults untouched); no production, vendor, database, Railway, TypeSafe or Google Drive access was used. Network use was limited to the live Notion fetch of each prompt and the Git fetch and push of the shared branch.
- The revised PF is a document output, not an authoritative publication. It establishes no QA verdict, acceptance, canon adoption or closure.

## 11. Next manual action

Nathan reviews PR #761 and, if he accepts the revised PF12, transfers it to `docs/pfcanon/` as his own manual canon action. Nathan alone merges.

## 12. Verified application completion receipt

Recorded after both outputs were saved and read back; see the line below.

Both outputs were saved under `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf12/` on branch `docs/20261026-gtwpe-pf10-v13-8-8-documents` and read back before commit. Revised PF: `PF12-from-v2.9.6.md`, 640,642 bytes, 6,264 LF, SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`, Git blob `d5bc01f83078bebe04f0854385317b47c1cd2de3`, internal version v2.9.7, effective date 2026-10-26, byte-identical to the verified application output. This proof log was read in full before this receipt was added and is read back again after it; its own hash is given in the final response and the ledger cell. Package status: COMPLETE_PACKAGE; application outcome: SUCCESS.
