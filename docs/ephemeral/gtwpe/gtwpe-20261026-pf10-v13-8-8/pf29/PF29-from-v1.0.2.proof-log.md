# T-PF29 — application proof log for `PF29-from-v1.0.2.md`

This is the application report for the revised PF beside it, `PF29-from-v1.0.2.md` in `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf29/`. Both files belong to run `gtwpe-20261026-pf10-v13-8-8/T-PF29`, preparation revision `P1`. The revised PF is not authoritative publication: `docs/pfcanon/` is unchanged, and canon moves only when the Product Owner transfers it.

## Outcome

- Application outcome: **SUCCESS**. All fifteen content operations and the three-field metadata plan were validated against the unchanged original before any output byte was written, then applied in one pass.
- Revised PF: `PF29-Canon-HDE-Users-Guide` **v1.0.3**, Effective date 2026-10-26, Last Update Gate `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md`.
- Save completeness: see "Save verification" at the end.

## Identity

| Item | Value |
| --- | --- |
| Task | T-PF29, ledger `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`); rows A10 with X06, S-APR with X05, A08 with X04 |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b, fetched live on 2026-10-26 (Notion page state 2026-10-09T11:05:22Z) |
| Applier | TW-APPLY-10 in the Nathan-started T-PF29 document session, Claude Code cloud session https://claude.ai/code/session_016STkEGvGYVWWaqSxnj76eo. Nathan's handoff authorized preparation then application in this one session. No subagent, no reviewer, no other session |
| Originating preparer | TW-DRAIN-10 100926.1 in the same session, run `gtwpe-20261026-pf10-v13-8-8/T-PF29`, revision `P1` |
| Original (application baseline) | `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`, `PF29-Canon-HDE-Users-Guide` v1.0.2, at `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`; Git blob `6a0d4725a710bfe1289282729156e15cc8acfcce`; 72,066 bytes; 1,072 lines; raw UTF-8 SHA-256 `36c3b1bdce884f902dce56650065bdbd26aa3dcb1da8954f62f2c38f83fd5601`. Re-fetched at application time (2026-10-26T22:09Z): `main` still at `0838ba08`, same blob, no newer PF29 |
| Package | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf29/redlines-PF29-from-v1.0.2.md` (36,774 bytes, SHA-256 `0a421b03b5654a4d5e0222c00a2d22690e9e365feae2f913afce56bdf8436ea1`) and its proof log `redlines-PF29-from-v1.0.2.proof-log.md` (31,166 bytes, SHA-256 `a20ebe045899d3af3ca539b09ce4edfee7470202ebf89de849506393671813c5`), both at commit `d3f3eabe4bd7aaa15c49dd6c7607094f9e097463` on `docs/20261026-gtwpe-pf10-v13-8-8-documents`. Application read them from that commit |
| Selected sources (the preparer's boundaries, checked against the handoff and the ledger) | PF10-HDE-Build-Notes v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter 1–223, addenda 2.8 (890–1002) and 2.10 (1102–1204). HDE-CRD-0002 Specification v1.1 (`docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, blob `c4802a5a7fa3`) lines 147–193, overlaid by delta 01 (blob `9408d6ed091b`) C-8 to C-12. Supporting cross-references X04 (plan v2.0 §18, 753–792), X05 (plan v1.0 §17, 701–739), X06 (result v1.0 §10, 156–165) |
| Output | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf29/PF29-from-v1.0.2.md` and this proof log, on branch `docs/20261026-gtwpe-pf10-v13-8-8-documents` (shared draft PR #761, https://github.com/amthorn78/glow-hdengine-v2/pull/761) |

## Intake and preparation-state verification

- **Complete reading.** The original (all 1,072 lines), the complete redlines file and the complete preparation proof log were read before any edit.
- **Preparation state.** Preparation outcome **READY**; save completeness **COMPLETE_PACKAGE**. Target and selected-source coverage were complete, and the package records no blocking item. The held items H-03 and H-04 are recorded as not drafted, so no blocked work is being made applicable. The redlines file ends with `END OF REDLINES`.
- **Baseline equality.** The preparer's recorded raw-byte SHA-256 equals the SHA-256 of the bytes read from `origin/main` at application time (`36c3b1bdce884f902dce56650065bdbd26aa3dcb1da8954f62f2c38f83fd5601`), in the same raw UTF-8 byte representation. The blob is unchanged, and `main` has not moved since preparation. No reconciliation is needed.
- **Scope.** The preparer's selected units equal the handoff's and the ledger's T-PF29 selection. No unselected PF10 addendum was read for application.
- **Destination.** PR #760 merged at 2026-10-26T21:18:51Z, so work continues on the ledger's predeclared continuation branch `docs/20261026-gtwpe-pf10-v13-8-8-documents` and its one shared draft PR #761 (opened by the T-PF07 session and recorded on the ledger's continuation line). This session created no branch or PR.

## Whole-batch validation (before any output byte)

The redlines file was re-parsed from commit `d3f3eab`; the preparer's in-memory data was not used. Every operation was resolved independently against the unchanged original.

| ID | Operation | Original lines | Expected / observed | Complete lines, unique heading path, inside section | Result |
| --- | --- | --- | --- | --- | --- |
| RL-001 | `REPLACE` | 81 | 1 / 1 | yes | valid |
| RL-002 | `REPLACE` | 113 | 1 / 1 | yes | valid |
| RL-003 | `REPLACE` | 245 | 1 / 1 | yes | valid |
| RL-004 | `REPLACE` | 341 | 1 / 1 | yes | valid |
| RL-005 | `REPLACE` | 637 | 1 / 1 | yes | valid |
| RL-006 | `REPLACE` | 700–702 | 1 / 1 | yes | valid |
| RL-007 | `REPLACE` | 840 | 1 / 1 | yes | valid |
| RL-008 | `REPLACE` | 937–941 | 1 / 1 | yes | valid |
| RL-009 | `REPLACE` | 977 | 1 / 1 | yes | valid |
| RL-010 | `REPLACE` | 978 | 1 / 1 | yes | valid |
| RL-011 | `REPLACE` | 979 | 1 / 1 | yes | valid |
| RL-012 | `REPLACE` | 980 | 1 / 1 | yes | valid |
| RL-013 | `REPLACE` | 999 | 1 / 1 | yes | valid |
| RL-014 | `REPLACE` | 1047–1049 | 1 / 1 | yes | valid |
| RL-015 | `REPLACE` | 1072 | 1 / 1 | yes | valid |
| MD-VERSION | metadata | 7 | 1 / 1 | §0.1 "Header" | valid |
| MD-EFFECTIVE-DATE | metadata | 11 | 1 / 1 | §0.1 "Header" | valid |
| MD-LAST-UPDATE-GATE | metadata | 13 | 1 / 1 | §0.1 "Header" | valid |

- **Operation checks.** Every content operation is a supported `REPLACE` with a nonempty exact OLD block, expected count 1, observed count 1 (non-overlapping and overlapping searches agree), complete-line boundaries and a complete, different NEW payload. No `FIND_AND_REPLACE` is used, so the RL-045 preflight has nothing to reject.
- **Conflicts.** None across the eighteen spans, metadata included. RL-009 to RL-012 occupy consecutive lines with one untouched LF between each pair; no spans intersect.
- **Header conflicts.** The metadata lines (7, 11, 13) are far from the first content span (line 81). No package operation touches the header, so no duplicate header authorization arose.

## Deterministic document-control metadata plan

| Field | Original value | Revised value | Basis |
| --- | --- | --- | --- |
| Version | `v1.0.2` | `v1.0.3` | An unambiguous native dotted numeric version with a `v` prefix; the final numeric component was incremented once, and the prefix and component count were preserved |
| Effective date | `2026-10-09` | `2026-10-26` | The actual application execution date in the native `YYYY-MM-DD` form. `date -u` gave 2026-10-26T22:09:07Z at application time |
| Last Update Gate | `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md` | The sources that justified this update, as the preparation proof log records them, deduplicated, in source order, separated by `; `. PF10-HDE-Build-Notes v13.8.8 becomes `BN 13.8.8`; the approved Specification is named by its filename. Delta 01 justified no change; X04, X05 and X06 are supporting cross-references; PF03 and PF05 are PF documents read in support; the ledger is never a gate |

- **Unchanged fields.** Title `PF29-Canon-HDE-Users-Guide`, Status `Canon` (not stale) and Invocation tag `INV-f2ac55d77ce9aacc` are unchanged. Labels, order and style of the header are preserved.
- **Restatements.** The document restates its own version or date nowhere outside the header (checked: no other line contains `v1.0.2` or `2026-10-09`), so there is no restatement to synchronize.
- **Change history.** PF29 has no change log, revision history or Doc-Delta section, and no rule requiring one, so the package carries no history entry. The version, date and gate agree with one another.

## Operation ledger

Each operation's basis is stated here as the preparer gives it: its rationale and its source-ledger reference.

| ID | Section | Source-ledger reference | Change type | What changed and why |
| --- | --- | --- | --- | --- |
| RL-001 | §1.1 opening paragraph | A08, A10, S-APR (all content redlines); PF03 §4 step 5 | CONSISTENCY | The paragraph attributed all availability to snapshot `e7265a09`. The statements this package changes were verified at `0838ba08`, and were false at `e7265a09`. It now keeps `e7265a09` for every unchanged statement, names `0838ba08` and the statements checked against it, and keeps "no recipe was executed for this revision" |
| RL-002 | §1.1 retired-route block | A10 (2.10 S19-F03 and the production-posture probes; "Required canon drainage") with X06 (§10 "Stale canon passages": HDE Users Guide §1.1); the WU-PR-05 plan §19 as supporting reading | CANON_UPDATE | Adds that an application created in a production-like posture answers the three canon-retired `/ops` paths as unknown paths for every method, with the governed `ERR_NOT_FOUND` 404, before any handler runs, while every other posture, including the dev runner, still runs their handlers. Verified in `adapter/http_reader.py` and `adapter/env_guard.py`. It makes no claim about router-level `OPTIONS` or redirect answers on dev-harness paths (held H-03) |
| RL-003 | §4.1 bind paragraph | A08 (2.8 AD-3; S10 last clause; independent check "Gate and runner") with X04 (§18: HDE Users Guide §4.1) | CANON_UPDATE | `0.0.0.0` becomes `127.0.0.1` (loopback only), debugger and reloader off. The helper passes APP_ENV through and sets no default. The exception clause that only reconciled the old bind is removed. Verified in `adapter/http_reader.py` `__main__` and `scripts/dev_start_reader.sh` |
| RL-004 | §6.1 discrepancy paragraph | A08 (2.8 S10 / (2), CR-8, NC-1) | CANON_UPDATE | The \[Current gap\] paragraph ("treats a missing APP\_ENV as dev") becomes the exact-comparison rule: unset, empty, test, local, padded or differently cased `dev` and all other values refuse with `ERR_READER_FORBIDDEN`. The claim boundary is kept. Verified in `_reader_dev_env_explicit` |
| RL-005 | §10.1 pair-file paragraph | S-APR (Fermentation row: S08) with X05 (§17: HDE Users Guide §10.1, stale after S08) | CANON_UPDATE | "--band does not override it" becomes "an explicit --band replaces only that band, and the selected category must still be present in the file". Verified in `aux_preview._resolve_from_pair_file` |
| RL-006 | §11.2 precondition and command | S-APR (S14) with X05 (§17 Recipe F row); PF29 §0.2 | CONSISTENCY | The command gains `APP_ENV=dev`. A paragraph now states the operator-facing classification: an unset, unrecognized or disagreeing APP\_ENV/ENGINE\_ENV refuses `PROVIDER_CONFIG_INVALID`; a production-like value refuses `PROVIDER_PROD_OVERRIDE_REQUIRED` unless the §13.3 override is used. It routes to HDE CLI/API/Vendor Ref by title. Verified in `classify_vendor_environment` and `_resolve_vendor` |
| RL-007 | §13.3 production command | S-APR (S14) with X05 (§17: "a production-like one needs the flag"); PF29 §0.2 | CONSISTENCY | Before the production dry-run command, a paragraph states the production override: required even for a dry-run, only an authenticated human initiator may supply it, the refusal codes, one bounded read, never a rail opening, and `--upsert` or any production write still refused. The command gains `APP_ENV=prod` and `--allow-prod-vendor <AUTHORIZATION_REF>` as placeholders, plus an instruction to set APP_ENV to the real environment. Verified in `engine/cli/main.py` and `engine/bodygraph/resolver.py`; the contract stays with HDE CLI/API/Vendor Ref §7.1.11 |
| RL-008 | §15 Recipe F body | S-APR (S14) with X05 (§17: HDE Users Guide Recipe F) | CANON_UPDATE | The command gains `APP_ENV=dev` (matching Recipe G), and the precondition paragraph points to §11.2 for the classification. The expected-behavior paragraph is unchanged |
| RL-009 | §16 unknown-path bullet | A08 (2.8 S02 / (1)) | CANON_UPDATE | The Flask HTML 404 limitation becomes: in `adapter.factory`, `adapter.http_reader.create_app` and `adapter.wsgi` an unknown path answers 404 with the governed `ERR_NOT_FOUND` JSON envelope. It routes bytes to HDE CLI/API/Vendor Ref and keeps the checked-in versus deployed boundary. Verified in the three 404 handlers |
| RL-010 | §16 `--dump-reader` and CLI help bullet | A08 (2.8 S07 / (3)) | CANON_UPDATE | The CLI help now describes `showcompat` stdout as the canonical `magic10_compat_result.v1` document and names `--dump-reader` for Reader v1 bytes. The other three sentences are unchanged. Verified in the `showcompat` subparser help |
| RL-011 | §16 `--allow-prod-vendor` bullet | S-APR (S14 status drainage: this bullet "become[s] stale once S14 lands") with X05 (§17: HDE Users Guide §16) | CANON_UPDATE | "absent from the inspected active CLI parser" becomes: implemented for `bg:resolve --source vendor` only; required in a production-like environment and refused in a recognized non-production one; human initiator only; one bounded read; no `--upsert`, production write, public Reader or Aux vendor traffic or rail opening. Owner routing and a live/deployed nonclaim are included |
| RL-012 | §16 dev GET `/reader` bullet | A08 (2.8 S10 / (2)); A10 (2.10 S19-F02 and its gate matrix) | CANON_UPDATE | "still defaults a missing APP_ENV to dev" becomes the exact gates (`dev` for `/reader`; `dev`, `test` or `local` for the sampler and conjunction dev routes; no trimming or case-folding; unset refuses). The waiver sentence for the vanished discrepancy is removed. Verified in `_reader_dev_env_explicit` and `_dev_admin_gate` |
| RL-013 | §17 `PROVIDER_CONFIG_INVALID` row | S-APR (S14) with X05 (§17 Recipe F row) | CANON_UPDATE | The row's cause and action now cover an unset, unrecognized or disagreeing APP\_ENV/ENGINE\_ENV for `bg:resolve --source vendor`. One row is added for `PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID` and `PROVIDER_AUDIT_UNAVAILABLE`. Codes verified in `engine/bodygraph/resolver.py` |
| RL-014 | §18 dry-run lead-in and command | S-APR (S14) with X05 (§17 Recipe F row) | CONSISTENCY | The quick reference's copy of the Recipe F command gains `APP_ENV=dev`, and the lead-in points to §11.2 |
| RL-015 | §18 closing paragraph | S-APR (S14), consequent on RL-011 | CONSISTENCY | "unsupported flag" becomes "production override", matching the replaced §16 bullet |

## Application and preservation

- **Method.** The eighteen validated original-bound edits were applied in descending original offset, without rematching. Python raw UTF-8 handling was used: no line-ending conversion, no trimming, no normalization.
- **Whole-document preservation.** An expected byte stream was rebuilt from the nineteen untouched original intervals plus the eighteen payloads. It equals the revised output exactly. Every payload sits at its computed position, and every original byte outside the eighteen spans is preserved.
- **Independent diff cross-check.** `git diff --no-index` from original to revised changes only lines inside the operation spans and the three header lines: 18 hunks, 28 lines added, 21 deleted. Unchanged lines inside multi-line spans, such as the blank lines and Recipe F's expected-behavior paragraph, match as unchanged.
- **Byte counts.** Original 72,066 bytes and 1,072 lines. Revised 76,613 bytes and 1,079 lines: RL-006 adds two lines, RL-007 four and RL-013 one. The content-only result before metadata (76,656 bytes, SHA-256 `27659df884b9744842551425fe8eb57422c8d7e5e4aadfba15433bb0f3332eaf`) equals the preparer's simulation. The gate change shortens the file by 43 bytes.
- **Revised SHA-256.** `2ef3b8a7bfabbc768bf0ae1799d29449fe3ecdc37b509a03dd7292f09f0c8301`.
- **Format.** LF line endings only, no CR. The file ends with exactly one LF, as the original does. Tables, fenced code blocks and escapes outside the spans are untouched.
- **Markers.** The revised PF contains no `Draft` or similar status language about the document, no TODO, TBD, FIXME or drafting note, no editorial comment or instruction to a future writer, no ASCII or Unicode ellipsis, and no stale status. The operator placeholders and availability labels that the preparation log classifies as canon-required are retained.
- **Not product QA.** These are text checks. No test, recipe, `hdctl` command, server, vendor, database or production access was run.

## Limitations

- The revised PF is a working file under `docs/ephemeral/`. It is not published canon, and it establishes no canon adoption, QA, acceptance, PF09 or PF30 movement, deployment or closure.
- Every availability statement the package does not change still rests on repository snapshot `e7265a09`, as RL-001 states. The preparation log lists the observations left for the Product Owner: the §16 test-baseline clause, the §1.1 and §1.2 summary rows, and §12.1's lack of an audit-sink key.
- Held items H-03 and H-04 remain undrafted with the Product Owner.

## Next manual action

Nathan decides whether and when to transfer the revised PF29 v1.0.3 into `docs/pfcanon/`, and alone merges PR #761. No further TW step is due for T-PF29.

## Save verification

Recorded after both files were read back from the working tree of branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`.

- `PF29-from-v1.0.2.md`: 76,613 bytes, 1,079 lines, SHA-256 `2ef3b8a7bfabbc768bf0ae1799d29449fe3ecdc37b509a03dd7292f09f0c8301`. Byte comparison with the validated output found it identical. The header and every changed region were read back.
- This proof log was read back in full after this entry was written. It names its revised PF, run, package and commit.
- Save completeness: **COMPLETE_PACKAGE**. The commit that holds both files is given in the final response and in the T-PF29 ledger row.
