# Proof log — PF05 v2.5.5 application — gtwpe-20261101-pf10-v14-0-5 — T-02

## 1. Identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.md`, in this directory |
| This log | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.proof-log.md` |
| Directory | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF05/` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-02/apply-r1`, applying package `drain-r1` |
| Applier | TW-APPLY-10 "Apply Validated Redlines", version 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when this step began (page last edited 2026-10-09T11:05:22Z) |
| Session | The same Claude Code document session that prepared the package, on branch `claude/gtwpe-triage-authoring-j94ewf`. Nathan's handoff authorizes both steps in this session. No subagent, reviewer or other session was used. |
| Execution date | 2026-11-02 (UTC, closed rails `TZ=UTC`) |
| Result | Applied. 13 content redlines and 3 derived header fields; zero rejected. |
| Save state | Recorded in §9 after both outputs were read back |

The revised PF is a document-session output under `docs/ephemeral/`. It is not authoritative publication: `docs/pfcanon/` is unchanged, and moving the file into canon is Nathan's action.

## 2. Inputs

| Input | Identity | Read |
| :---- | :---- | :---- |
| Exact original (application baseline) | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md`, title `PF05-Canon-HDE-CLI-API-Vendor-Ref`, v2.5.4; git blob `53e6a9028dfa5d79b91e9b98cc949160c5a5cefe`; raw-byte SHA-256 `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028`; 327,342 bytes; 4,461 lines | In full, earlier in this session, against the same verified bytes (coverage windows in the preparer's proof log §2) |
| Redlines | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.md`, this directory; SHA-256 `c1804a5954a288573ded0e427253d633aa0248fd96fb5d44c335a1e19aa1faab`; 22,317 bytes; committed in `0d22343` | In full |
| Preparer's proof log | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, this directory; SHA-256 `c698e90945915435f5aebc5d9f16c0bff66a37308c8c5bf5c7326f1a5e3e14d1`; committed in `0d22343` | In full |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`. Selected units: addendum 2.1 D-1 (l.225–276), D-2 (l.277–344), D-3 (l.345–396); context l.205–224 and l.491–516 | In full, earlier in this session |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-02; rows C-01, C-02, C-03; support C-06 | In full |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, blob `504712df548a02f3aa4e7b8c37027385e46a3878` | In full, earlier in this session |

## 3. Preparation-state verification

| Required fact | Established value | Evidence |
| :---- | :---- | :---- |
| Originating preparer and session | TW-DRAIN-10 100926.1, run in this session | Preparer's proof log §1 |
| Run and output identities | `drain-r1`; redlines and proof log at the paths above | Preparer's proof log §1 and §11; files present at `0d22343` |
| Baseline fingerprint and representation | Raw-byte SHA-256 `1de30cbb…3028` over the repository file bytes | Recomputed here from the same file; equal |
| Incoming-source versions and boundaries | HDE Build Notes v14.0.5, the 2.1 units above | Preparer's proof log §3; they agree with the handoff and ledger row T-02 |
| Target and selected-source coverage | Complete target reading; complete selected-unit reading | Preparer's proof log §2 and §3 |
| Unresolved items | None blocking. H-09 (PF05 §7.2.0 gap row) and H-05 (AGENTS.md) are held items outside the package, each with what it waits for. | Preparer's proof log §8 |
| Preparation outcome and save completeness | `READY` / `COMPLETE_PACKAGE`, with a completion receipt recorded after read-back | Preparer's proof log §11; the redlines file ends with `END OF REDLINES` |

Drift check. At application time `origin/main` is `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`. The PF05, PF10 and PF03 blobs there equal the baseline blobs at `e2b7427ff418ca8f08f05587c4a541308a76da56`. There is no material drift, and no preparer reconciliation is needed.

## 4. Whole-batch validation (before any output byte was written)

A scratch application script parsed only the saved redlines file. It resolved every operation against the unchanged original, derived the header plan, and checked the whole batch before writing.

- Operations. Every redline is `REPLACE` with an exact nonempty OLD block, expected occurrence 1, and a complete NEW block. No `DELETE`, `INSERT`, `FIND_AND_REPLACE` or unsupported operation is present, so the RL-045 rule has nothing to apply to.
- Counts. Each of the 13 OLD blocks occurs exactly once in the whole original. Each quoted section-path heading occurs exactly once, and the headings precede the span in order.
- Conflicts. The 13 content spans and the 3 header spans are strictly ordered with gaps between them. There is no overlap, no shared boundary and no insertion gap. No content operation touches the header lines (5–10).
- Change-log agreement. RL-13's added line begins `* v2.5.5 — `, the version this plan derives. The PF05 Change Log format records no date, so no date has to agree.
- Result: every member valid; the batch was accepted whole.

## 5. Header metadata plan

The header is §0.1 "Header", lines 5–10. Each control field occurs once. Labels, order, Markdown style and line-break suffixes are preserved; only field values change.

| Field | Before | After | Basis |
| :---- | :---- | :---- | :---- |
| Version | `v2.5.4` | `v2.5.5` | Native dotted numeric version: final component incremented once, prefix `v` and three components kept. Agrees with RL-13. |
| Effective date | `2026-10-26` | `2026-11-02` | Actual application execution date, in the native ISO `YYYY-MM-DD` format |
| Last Update Gate | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002_close_report.md` | `BN 14.0.5` | The package's only recorded source is `PF10-HDE-Build-Notes-v14.0.5.md` (preparer's proof log §3), so the gate is `BN` and its version number. No other source justified the update. |
| Status | `Canon` | unchanged | Not stale. The document stays permanent canon; no classification change. |
| Title, Invocation tag | unchanged | unchanged | Not authorized; neither restates the version |

Only the value bytes of each field were replaced. The Last Update Gate line keeps its original three trailing spaces (one after the value, then the two-space line break), and the Version and Effective date lines keep their two-space breaks. No other line restates the document's own version or revision date; the earlier §11.1 Change Log entries are history and were not touched.

## 6. Operation ledger

Each content operation's basis is quoted from the package: its rationale, its ledger row and its HDE Build Notes source lines (SRC-1 is `PF10-HDE-Build-Notes-v14.0.5.md`). Offsets are character positions in the original and in the output.

| ID | Location (original line) | Ledger row | Source basis (SRC-1) | Rationale (from the package) | Original span | Output offset |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| M-1 | §0.1, line 6 | — | Derived (§5) | Version bump | [111, 130) | 111 |
| M-2 | §0.1, line 8 | — | Derived (§5) | Execution date | [153, 183) | 153 |
| M-3 | §0.1, line 9 | — | Derived (§5) | Gate from the recorded source | [186, 292) | 186 |
| RL-01 | §4.6, line 956 | C-02 | 2.1 D-2, l.284–289 | D-2 decides that no non-v2 base reaches bodygraphs by fallback and that a terminal v1 base is retained legacy selection. This §4.6 permission stated the superseded posture and contradicted §7.1.10. | [85007, 85104) | 84932 |
| RL-02 | §5.5, line 2493 | C-03; support C-06 | 2.1 D-3, l.349–364 and l.377–378; C-06 l.223, l.506 | D-3 adds the dev/admin gate as step 2 of "Validation and environment gating", withdraws "authenticated" and "internal authentication" from "Success body", and records the no-credential posture, the wider-exposure rule and the accepted residual risk. The gate is not in the code at the snapshot, so the gap is stated beside it. | [189764, 190200) | 189840 |
| RL-03 | §5.5 "Headers & conditionals", line 2509 | C-03 | 2.1 D-3, l.350–355 | Under D-3 a non-production request outside `APP_ENV` dev, test or local is refused 403 before the method rules; the method rules apply only to an admitted request. | [191897, 191978) | 194192 |
| RL-04 | §5.5 "Parity (clarified)", line 2520 | C-03 | 2.1 D-3, l.358 and l.378 | D-3 supersedes "authenticated" in "Parity (clarified)"; no authentication mechanism exists in canon or code. | [193270, 193326) | 195592 |
| RL-05 | §7.1.10, line 3476 | C-02 | 2.1 D-2, l.281–283 and l.315 | D-2 extends the §7.1.10 scope from bg:resolve to compat chart acquisition by showcompat and conjunction. | [256843, 256973) | 259151 |
| RL-06 | §7.1.11, line 3507 | C-01 | 2.1 D-1, l.229–232 and l.259 | Once D-1 widens the contract to three paths, the S14 delivery covers only bg:resolve; the claim is narrowed to what was delivered. | [259896, 259956) | 262412 |
| RL-07 | §7.1.11, lines 3515–3521 | C-01; support C-06 | 2.1 D-1, l.259; C-06 l.223, l.506 | D-1 turns the limit "The gate covers only the command §7.1.11a names" into a gap against the decision. Bounded inspection at the snapshot confirms the uncovered paths. | [260978, 261835) | 263533 |
| RL-08 | §7.1.11a, line 3533 | C-01 | 2.1 D-1, l.229–234 and l.255 | D-1 supersedes "accepted only by hdctl bg:resolve --source vendor" with the three-path scope. | [262345, 262535) | 265603 |
| RL-09 | §7.1.11d, line 3577 | C-01 | 2.1 D-1, l.235 and l.256 | D-1 rewrites step 2 to "the invocation selects vendor acquisition" for each command. | [265281, 265385) | 268900 |
| RL-10 | §7.1.11d, line 3584 | C-01 | 2.1 D-1, l.236–238 | D-1 sets the scope of one authorization to the bounded acquisitions of one invocation, at most one per party and two for a pair, with no write, no public Reader or Aux traffic and no opening of a closed rail. | [265727, 265850) | 269485 |
| RL-11 | §7.1.11e, line 3588 | C-01 | 2.1 D-1, l.235, l.242–244 and l.257 | D-1 adds the showcompat carrier rule to §7.1.11e and aligns the usage case with the rewritten step 2. | [266196, 266426) | 270059 |
| RL-12 | §7.1.11f, line 3604 | C-01 | 2.1 D-1, l.241 and l.258 | D-1 supersedes the command rule "exactly bg:resolve" with the three values. | [267979, 268015) | 272201 |
| RL-13 | §11.1 Change Log, line 4148 | C-01, C-02, C-03 | PF05 §0.4 and §11.1 (the target's own logging rule) | PF05 §0.4 and §11.1 require a change to transport or the CLI contract to be logged. The entry names v2.5.5, the baseline v2.5.4 bumped once by the target's patch scheme; the format carries no date. | [309120, 309474) | 313392 |

The preparer's proof log §7 maps every item of the selected units to these redlines, to an already-represented location, to another target, or to a hold. §6 there records the reconciliation of D-1 l.259 with the §7.1.11 text the v2.5.4 baseline actually carries.

## 7. Application and preservation

Application. The 16 validated operations were applied once, in descending original offset, each checked against its original span immediately before replacement. No anchor was rematched in changed text. The file was handled as raw UTF-8 with LF line endings and no normalization.

Preservation checks, all passed:

- Reconstruction. The output equals the stream built from the original's untouched intervals and the 16 payloads, in original order.
- Untouched intervals. Every interval between operations, and the tail after the last one, appears verbatim at its shifted output offset: 323,157 characters, all of the original outside the 16 spans.
- Payloads. Each NEW block occurs exactly once in the output. Each OLD block is absent, except RL-13's, whose NEW block keeps the v2.5.4 line by design.
- Line-level audit. A line diff of original against output shows exactly 16 changed hunks, one per operation, and 4,445 identical lines.
- Cross-check. The output equals the preparer's one-pass simulation (SHA-256 `a3c9a08b7f0c685bfd5ba6a59441f63b0a961e475587e86efcf9483a34a248ee`) except in header lines 6, 8 and 9, which the simulation left at their v2.5.4 values by design.
- Structure. LF only, zero CR bytes. The file still ends with `---` and one blank line. The number of code-fence lines and table lines is unchanged; no payload contains a fence or a table row except RL-12, which replaces one table row with one table row.
- Drafting markers. No `TODO`, `TBD`, `FIXME` or draft-status language about the document is present. The three "Draft"/"draft" hits (lines 1194, 1738 and 1761) are the JSON Schema dialect name "Draft 2020-12" and a historical rationale about an earlier draft of the admin-bundle decision, both canon content. Existing `[OPEN]` markers are canon-recorded open decisions, not drafting notes.

| Measure | Original | Revised |
| :---- | :---- | :---- |
| Path | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md` | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF05/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.md` |
| Version | v2.5.4 | v2.5.5 |
| Bytes | 327,342 | 332,101 |
| Lines | 4,461 | 4,479 |
| SHA-256 | `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028` | `8afbfb89fcbe461c192862a661ce9844b6537f4b0743ad3d60c9a65707f54331` |

These are text checks on the document. They are not product QA.

## 8. Constraints, limitations and nonclaims

- The applier prepared no edits, improved no prose and performed no PF03 cleanup. Pre-existing ellipses in PF05 examples (original lines 279, 2117, 2188, 2495 and 3239) are retained, as the preparer's proof log §8 records.
- The new repository-state statements in RL-02 and RL-07 are pinned to `main@e2b7427ff418ca8f08f05587c4a541308a76da56` and come from the preparer's bounded read-only inspection under closed rails (preparer's proof log §5). They establish no runtime behavior.
- Held work stays held: H-09 (the PF05 §7.2.0 gap row, until the implementing change for Candidate CRD Items List item 9 delivers) and H-05 (AGENTS.md, which needs the Product Owner's explicit instruction).
- The revised PF says the D-1 and D-3 gates are Required-Now gaps; nothing here claims they are implemented.
- This application changes no `docs/pfcanon/` file, Specification, AGENTS.md or other task's file. It establishes no QA verdict, acceptance, deployment, PF09 movement or closure.

## 9. Save state

| File | Path | Bytes | SHA-256 | Verified |
| :---- | :---- | :---- | :---- | :---- |
| Revised PF | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF05/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.md` | 332,101 (4,479 lines) | `8afbfb89fcbe461c192862a661ce9844b6537f4b0743ad3d60c9a65707f54331` | Read back from disk in full: byte-identical to an independent re-derivation from the original and the saved redlines; every changed region reviewed |
| Proof log | This file | — | Not self-hashed | Read back in full after writing, and again after this receipt was added |

Completion receipt (2026-11-02, UTC). Both outputs were read back from disk in this session. The revised PF matched an independent re-derivation byte for byte, and its sixteen changed regions were reviewed. This log was read back in full; its identities agree with the revised PF and with the package it applies: original, source, ledger rows, `drain-r1` and `apply-r1`.

Save state: `COMPLETE_PACKAGE`. Application result: applied, 16 of 16 operations.

## 10. Next manual action

Nathan reviews the revised PF on draft PR [amthorn78/glow-hdengine-v2#826](https://github.com/amthorn78/glow-hdengine-v2/pull/826), branch `claude/gtwpe-triage-authoring-j94ewf`, and decides whether to transfer it into `docs/pfcanon/`. Nathan merges. The ledger's T-02 completion row records this result.
