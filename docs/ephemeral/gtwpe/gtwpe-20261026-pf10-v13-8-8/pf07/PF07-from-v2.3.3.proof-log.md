# T-PF07 — application proof log for `PF07-from-v2.3.3.md`

This is the application report for the revised PF beside it, `PF07-from-v2.3.3.md` in `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf07/`. That file is the complete `PF07-Canon-Glow-Infrastructure` v2.3.4, produced by applying the T-PF07 redline package to PF07 v2.3.3. Run `gtwpe-20261026-pf10-v13-8-8/T-PF07`, package revision `P1`.

The revised PF is a working file under `docs/ephemeral/`. It is not authoritative publication. `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md` on `main` is unchanged; Nathan transfers canon manually.

## Outcome

- **Application: SUCCESS.** All 8 package operations and the 3-field header plan were applied in one original-bound pass, and every verification below passed.
- **Save completeness:** see "Save verification" at the end. It is recorded only after both outputs were read back.

## Identity

| Item | Value |
| --- | --- |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b. Re-fetched live when this step began, 2026-10-26; page state 2026-10-09T11:05:22Z, unchanged from the session's first fetch |
| Authorization | Nathan's T-PF07 handoff (GTWPE 100926.1) authorizes TW-DRAIN-10 then TW-APPLY-10 in this one session |
| Applier | TW-APPLY-10 in the same Nathan-started T-PF07 document session: Claude Code cloud session https://claude.ai/code/session_01Tgfx3BStUkwc3FCxt1iDDU |
| Originating preparer | TW-DRAIN-10 in that same session, run `gtwpe-20261026-pf10-v13-8-8/T-PF07`, revision `P1` |
| Original (application baseline) | `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`, `PF07-Canon-Glow-Infrastructure` v2.3.3, at `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a`. It is byte-identical at the current `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`, so there is no drift since preparation. Blob `7d2734ce2b75a7277a632b881bfb931ff88bf7af`; 98,175 bytes; 1,431 LF characters, with the 1,432nd line unterminated (no trailing newline); raw UTF-8 SHA-256 `573ceecfb93557cb93db04179a535a0d3c1209a99f5128e0408384f22b4110cc`, the same raw-byte representation the preparer recorded |
| Package | Commit `28184eab1a8ba36e6c4cec5d073acbb9d3db6e38` on `docs/20261026-gtwpe-pf10-v13-8-8-documents`. `redlines-PF07-from-v2.3.3.md`: blob `ef52b9f8add7`, 13,363 bytes, SHA-256 `59c2ce8541a1da19814d06341a421ca7bb1ba074124870a15340ae5d9dcd6148`. `redlines-PF07-from-v2.3.3.proof-log.md`: blob `12cf7f3382c0`, SHA-256 `4cc538ff40af071dcc445fb7fe32b5f9ebebe2674a121edcc5a451e4d9edf9c9` |
| Preparation state | READY / COMPLETE_PACKAGE, read from the package proof log's "Outcome" and "Save verification". Complete target and selected-source coverage, every selected change accounted for, no blocking item |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7`; task T-PF07; rows A19; A09 with X05; A20 and A35. Held H-05 is not touched |
| Selected sources | PF10-HDE-Build-Notes v13.8.8, `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`. Units: front matter 1–223; 2.9 (1003–1101); 2.19 (2082–2321); 2.20 (2322–2395); 2.35 (3725–3955). Supporting cross-reference X05: `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md` §17, lines 701–739, blob `6baead456619` |
| Output | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf07/PF07-from-v2.3.3.md`, `PF07-Canon-Glow-Infrastructure` v2.3.4, and this proof log |

**Intake checks.**

- The preparer's selected scope matches the handoff and ledger row T-PF07: §3.1 and §4.1 (A19); §8 config keys (A09 with X05); §10 (A20 and A35).
- I re-read each selected unit at its recorded identity to confirm the provenance and decisions the package cites.
- No unselected PF10 addendum was read.
- The output names `PF07-from-v2.3.3.md` and `PF07-from-v2.3.3.proof-log.md` did not exist on the local branch or on `origin/docs/20261026-gtwpe-pf10-v13-8-8-documents` before writing.

## Applied operations and their basis

The basis below is the preparer's rationale and source-ledger reference for each operation, restated here.

| ID | Operation, count | Change | Basis (preparer's rationale; ledger rows) |
| --- | --- | --- | --- |
| RL-001 | REPLACE, 1/1, original lines 582–584 | §3.1 Railway gains **Deploy source (names-only)** → HD Engine: commits landing on `main` of `amthorn78/glow-hdengine-v2` (Product Owner-provided deployed environment fact). The closing routing line is reproduced unchanged | **A19.** 2.19 P-18 records the Product Owner direction of 2026-10-21 that the candidate reaches the service when its commit lands on `main`. That is a PO-provided deployed environment fact, which PF07 §2.4 does not allow to be downgraded to OPEN/TBD. P-18 names §3.1 as a doc-delta target |
| RL-002 | REPLACE, 1/1, lines 632–633 | §4.1 HD Engine gains a **Deploy source** bullet between the unchanged Source and Build artifact bullets, noting that the build and start commands are not recorded | **A19.** 2.19 P-18 names §4.1 as the second target, and P-9 and P-18 state that the build and start commands are not discovered or recorded. Build artifact stays **TBD** |
| RL-003 | REPLACE, 1/1, line 638 | §4.1 Start command pointer: "(canonical Railway command kept verbatim)" → "(checked-in declarations only; the live Railway start setting is not verified)" | **A20, A35, A19.** 2.20 and 2.35 keep the live start setting unverified as a stated limit, and 2.19 records that no start command is recorded. §10 (line 1357) already disclaims any declaration as the current Railway start command; this consistency change aligns the §4.1 pointer with that limit. Decision on the ledger's §10 uncertainty: §10's wording needed no change |
| RL-004 | REPLACE, 1/1, line 871 | §6.3.1 Backend: removes "— confirm" | **TW-DRAIN-10 marker rule** (no ledger row). A bare to-do that canon does not require; **TBD** already records that the value is unconfirmed, and the two candidate forms are kept |
| RL-005 | REPLACE, 1/1, line 895 | §6.4: "CNAME *(confirm exact hostnames as we populate)*" → "CNAME *(exact hostnames OPEN/TBD)*" | **Marker rule.** A to-do with drafting-status language, restated in PF07's own notation, as the adjacent TXT bullet does |
| RL-006 | FIND_AND_REPLACE, whole PF, 3/3, lines 956, 965, 974 | §7.1: "*(via DB proxy; confirm)*" → "*(via DB proxy; unconfirmed)*" | **Marker rule.** Removes the instruction form and keeps the uncertainty that PF07's no-guessing rule (§6.5, §8) requires |
| RL-007 | REPLACE, 1/1, line 1268 (reproduced), followed by the new block | §8.2.1 gains the key block `HDE_VENDOR_OVERRIDE_AUDIT_PATH`. It states what the key names, that it is not a secret, and that its bindings are OPEN/TBD. It describes the checked-in fallback locations and the paths the code refuses, and routes the semantics to HDE-CLI-API-Vendor-Ref by title | **A09 with X05.** 2.9 carries the plan v1.0 §17 doc-delta candidates, and X05 §17 lists "Glow Infrastructure §8 config keys — the new key `HDE_VENDOR_OVERRIDE_AUDIT_PATH`". The key name and fallback paths were confirmed read-only in `engine/bodygraph/vendor_audit.py` on `main` `0838ba08` |
| RL-008 | REPLACE, 1/1, line 1295 | §8.2.3 Notes: deletes "Please supply the value when known." | **Marker rule.** A request to the reader; the OPEN/TBD definition before it is kept |

## Document-control header (metadata plan)

| Field | Before | After | Basis |
| --- | --- | --- | --- |
| Version | `v2.3.3` | `v2.3.4` | One increment of the final component of the native dotted numeric version |
| Effective date | `2026-10-09` | `2026-10-26` | Actual application execution date (UTC, read at 2026-10-26T21:39:22Z), native `YYYY-MM-DD`. It is the only revision date field |
| Last Update Gate | `BN 13.5; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` | `BN 13.8.8` | The source that justified the update, as the package records it: `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, PF10 version 13.8.8 |

Other header facts:

- **Gate inputs.** X05 is supporting reading per the ledger, so it is not a gate source. The ledger and the redlines file are never gate sources.
- **Unchanged fields.** Title, Status (`Canon`), the invocation tag `INV-f2ac55d77ce9aacc`, and the labels, order and style of every field.
- **Status.** `Canon` is not stale. PF07 still declares itself the canonical infrastructure inventory.
- **No restatements.** PF07 restates its own version or date nowhere else. `### **2.3.3 Ops-only identity**` is a section number and was left intact.
- **No history entry.** PF07 has no change log or revision-history rule, so none is required.
- **No header redline.** The package carries none, so no duplicate authorization arose.
- **Agreement.** Version, date and gate agree. Each occurs exactly once in the output.

## Validation and preservation

Every check ran on the committed package blob and on the original read from `git show origin/main:…`, using a local Python 3 script. Exact literal matching was used throughout, with no normalization.

**Intake and conflicts.**

- The package parsed to 8 operations, RL-001 to RL-008, in order, with `END OF REDLINES`.
- Every `REPLACE` OLD block is nonempty, consists of complete lines, and occurs once in the whole original. Every NEW block differs from its OLD block.
- RL-006 passes the RL-045 preflight: expected 3 (at least 2), observed 3, whole-PF scope. FIND is nonempty, and REPLACE differs from FIND and does not contain it.
- The 3 header spans were included in the conflict check. 13 spans in all (10 content, 3 metadata); none intersects another, and there is no insertion gap.

**Application.**

- One pass in descending offset order, with no rematching.

**Preservation.**

- **Reconstruction.** Rebuilding the expected stream from the 14 untouched original intervals plus the exact payloads gives a result identical to the output. Each untouched interval was compared byte for byte at its position in the output.
- **Line audit.** A line-level `difflib` opcode audit shows changes only on the planned original lines: 4, 6, 7, 638, 871, 895, 956, 965, 974 and 1295. The insertions follow lines 584, 632 and 1268.
- **Structure.** EOF is preserved; the file ends with "…enumerate token names." and no trailing newline. No CR appears, the count of code fences is unchanged (the §10 blocks are untouched), and the count of table pipes is unchanged (no table touched).

**Post-application.**

- FIND is absent and its replacement occurs exactly 3 times. Each NEW payload occurs exactly once.
- The output contains no `Draft` status language. It also contains none of "— confirm)", "; confirm)", "as we populate", "Please supply", "TODO" or "FIXME".
- The canon-required notation is kept: `TBD` goes from 117 to 119, the +2 being the `OPEN/TBD` added by RL-005 and RL-007.

**Bytes.**

- Original: 98,175 bytes, SHA-256 `573ceecfb93557cb93db04179a535a0d3c1209a99f5128e0408384f22b4110cc`.
- Output: 99,393 bytes, 1,443 LF characters with the last line unterminated, SHA-256 `9e00712a3af2c1b498b5dddf5ada35c72b44952293d3b73ec3915cbba586d790`, Git blob `60fd3f0b3feff007491dc7add29a9c4491cbdf95`.
- The preparer's content-only simulation was 99,437 bytes, and the output is 44 bytes shorter. The header plan accounts for all 44:
  - the gate: `BN 13.5; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` → `BN 13.8.8`, 53 → 9 bytes, −44;
  - the version: 0;
  - the date: 0.

These are text checks, not product QA.

## Constraints and interpretations

- **Basis of the hygiene redlines.** RL-004 to RL-006 and RL-008 rest on the prompt's marker rule, not on a ledger row. This step applied them as prepared and did not judge their wording.
- **Conflict register.** The 2.19 and 2.20 numbering question about who records the deployment facts changes no PF07 text, as the package proof log explains.

## Limitations and unresolved items

- **For the Product Owner, unchanged from preparation:**
  - Pre-existing ellipses: `Bearer …` and the `<epic-id>/...` path patterns. PF03 prohibits ellipses, but no selected source covers these lines.
  - PF07 §2.5.1, §5.1.1 and §5.1.3 still name `scripts/ops/admin_vendor_qa.py` as the supported prod-QA harness, which OBS-P4-4 records as non-functional.
- **Held items.** H-05 and the other held items are untouched.
- **No live observation.** No production, Railway, vendor or database surface was observed. Rails stayed closed.
- **Nonclaims.** This establishes no QA verdict, acceptance, canon adoption, drainage into `docs/pfcanon/` or closure.

## Next manual action

Nathan reviews the revised PF07 v2.3.4 on draft PR [amthorn78/glow-hdengine-v2#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761). He decides whether and when to transfer it to `docs/pfcanon/`, and alone merges.

## Save verification

Recorded after both outputs were saved and read back in full.

- `PF07-from-v2.3.3.md`: 99,393 bytes, 1,443 LF characters with no final LF (as in the original), UTF-8, no CR, SHA-256 `9e00712a3af2c1b498b5dddf5ada35c72b44952293d3b73ec3915cbba586d790`. This equals the applier's verified output. The header reads v2.3.4, 2026-10-26, `BN 13.8.8`, and the file contains no run or report material.
- This proof log was read back complete before this receipt was added, and read again after it. It does not carry its own hash.
- This proof log carries run `gtwpe-20261026-pf10-v13-8-8/T-PF07` and names the revised PF by path and SHA-256. The revised PF carries no run material, by design.
- Save completeness: **COMPLETE_PACKAGE**. Application: **SUCCESS**.
