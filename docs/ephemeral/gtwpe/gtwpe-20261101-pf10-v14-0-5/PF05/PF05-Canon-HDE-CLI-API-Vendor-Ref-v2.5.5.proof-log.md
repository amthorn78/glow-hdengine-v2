# Proof log — PF05 v2.5.5 application — gtwpe-20261101-pf10-v14-0-5 — T-02 — apply-r2

## 1. Identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.md`, in this directory |
| This log | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.proof-log.md` |
| Directory | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF05/` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-02/apply-r2`, applying package `drain-r2`. It replaces the `apply-r1` output (commit `a292ce96573410e0f08ea285d112b7774a3ba50a`) at the same paths, on the Product Owner's direction of 2026-11-02. `apply-r1` stays readable in that commit. |
| Applier | TW-APPLY-10 "Apply Validated Redlines", version 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when this run began (page last edited 2026-10-09T11:05:22Z, unchanged since `apply-r1`) |
| Session | The same Claude Code document session that prepared `drain-r2`, on branch `claude/gtwpe-triage-authoring-j94ewf`. The T-02 remediation handoff authorizes both steps in this session. No subagent, reviewer or other session was used. |
| Execution date | 2026-11-02 (UTC, closed rails `TZ=UTC`) |
| Result | Applied: 14 content redlines and 3 derived header fields, none rejected |
| Save state | Recorded in §9 after both outputs were read back |

The revised PF is a document-session output under `docs/ephemeral/`. It is not authoritative publication. `docs/pfcanon/` is unchanged, and moving the file into canon is Nathan's action.

## 2. Inputs

| Input | Identity | Read |
| :---- | :---- | :---- |
| Exact original (application baseline) | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md`, title `PF05-Canon-HDE-CLI-API-Vendor-Ref`, v2.5.4. Git blob `53e6a9028dfa5d79b91e9b98cc949160c5a5cefe`; raw-byte SHA-256 `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028`; 327,342 bytes; 4,461 lines | In full earlier in this session, against the same verified bytes (coverage windows are in the preparer's proof log §2) |
| Redlines (`drain-r2`) | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.md`, this directory. SHA-256 `cc0984889e9c9e3e40f23f6a86c5a05d32d78c5b21372a14fae1399378bb043a`; 25,034 bytes; committed in `3720785c029bf1e1ab18b8be7345bdcb0db873f8` | In full |
| Preparer's proof log (`drain-r2`) | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, this directory. SHA-256 `20327ae757335a8af3c44f9c4c7becfbe77d979bd178ac1c9fdaa470b56a9a6c`; committed in `3720785` | In full |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5. Blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`. Selected units: addendum 2.1 D-1 (l.225–276), D-2 (l.277–344) and D-3 (l.345–396); context l.205–224 and l.491–516 | In full earlier in this session |
| Product Owner direction, 2026-11-02 | The T-02 remediation handoff; its terms are recorded in the preparer's proof log §1A | Correction authority for RL-14 and the RL-13 extension. Not a Last Update Gate source. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`: task T-02; rows C-01, C-02, C-03; support C-06 | In full |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, blob `504712df548a02f3aa4e7b8c37027385e46a3878` | In full earlier in this session |

## 3. Preparation-state verification

| Required fact | Established value | Evidence |
| :---- | :---- | :---- |
| Originating preparer and session | TW-DRAIN-10 100926.1, run in this session | Preparer's proof log §1 |
| Run and output identities | `drain-r2`, superseding `drain-r1` at the same paths; files at `3720785` | Preparer's proof log §1, §1A and §11 |
| Baseline fingerprint and representation | Raw-byte SHA-256 `1de30cbb…3028` over the repository file bytes | Recomputed here from the same file; equal |
| Incoming-source versions and boundaries | HDE Build Notes v14.0.5, the 2.1 units above; RL-14's basis is D-2 (row C-02) | Preparer's proof log §3 and §1A; they agree with the handoff and ledger row T-02 |
| Target and selected-source coverage | Complete reading of the target and of the selected units; for `drain-r2`, line 119 and a fallback search of the whole file were redone | Preparer's proof log §2 and §1A |
| Pre-check required by the direction | The code still selects the legacy route for every non-v2 base other than a terminal `v1` (`vendor_client.py` lines 102–109 and 124–153; `resolver.py` lines 686–705, at `84d6d1c`), so RL-14's part (c) may be written | Preparer's proof log §1A and §5 |
| Unresolved items | None blocking. H-09 (PF05 §7.2.0 gap row) is held, as directed. H-05 (AGENTS.md) is outside this package; the Product Owner sent it to draft PR #827. | Preparer's proof log §8 |
| Preparation outcome and save completeness | `READY` / `COMPLETE_PACKAGE`, with a completion receipt recorded after read-back | Preparer's proof log §11; the redlines file ends with `END OF REDLINES` |

Drift check. At application time `origin/main` is `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`. The PF05 and PF10 blobs there equal the baseline blobs at `e2b7427ff418ca8f08f05587c4a541308a76da56`. There is no material drift, and no preparer reconciliation is needed.

## 4. Whole-batch validation (before any output byte was written)

A scratch application script parsed only the saved `drain-r2` redlines file. It resolved every operation against the unchanged original, derived the header plan, and checked the whole batch before writing anything.

- Operations. All 14 redlines are `REPLACE`: an exact nonempty OLD block, an expected occurrence of 1, and a complete NEW block. No other operation type is present, so the RL-045 rule has nothing to apply to.
- Counts. Each OLD block occurs exactly once in the whole original. Each quoted section-path heading occurs exactly once and precedes its span in order; this includes RL-14's indented `  ## **Vendor ingest (HDAPI)**`. For `apply-r2` the parser was tightened to read indented headings and to require one parsed heading per path segment.
- Conflicts. The 14 content spans and 3 header spans are strictly ordered with gaps between them. There is no overlap, no shared boundary and no insertion gap. No content operation touches header lines 5–10. RL-14 (line 119) sits between the header and RL-01.
- Change-log agreement. RL-13's added line begins `* v2.5.5 — `, the version this plan derives. The PF05 Change Log format records no date.
- Result: every member is valid, and the batch was accepted whole.

## 5. Header metadata plan

The header is §0.1 "Header", lines 5–10. Each control field occurs once. Labels, order, Markdown style and line-break suffixes are preserved; only the field values change.

| Field | Before | After | Basis |
| :---- | :---- | :---- | :---- |
| Version | `v2.5.4` | `v2.5.5` | Native dotted numeric version: the final component is incremented once, keeping the `v` prefix and three components. Agrees with RL-13. |
| Effective date | `2026-10-26` | `2026-11-02` | Actual application execution date, in the native ISO `YYYY-MM-DD` format |
| Last Update Gate | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002_close_report.md` | `BN 14.0.5` | The package's only recorded source is `PF10-HDE-Build-Notes-v14.0.5.md` (preparer's proof log §3). The Product Owner's direction is correction authority, not a source, and the handoff says the gate stays `BN 14.0.5`. |
| Status | `Canon` | unchanged | Not stale; no classification change |
| Title, Invocation tag | unchanged | unchanged | Not authorized; neither restates the version |

Only the value bytes of each field were replaced. The Last Update Gate line keeps its original three trailing spaces, and the Version and Effective date lines keep their two-space breaks. No other line restates the document's own version or revision date. The earlier §11.1 Change Log entries are history and were not touched.

## 6. Operation ledger

Each content operation's basis is quoted from the package: its rationale, its ledger row and its HDE Build Notes source lines (SRC-1 is `PF10-HDE-Build-Notes-v14.0.5.md`). Offsets are character positions in the original and in the output.

| ID | Location (original line) | Ledger row | Source basis (SRC-1) | Rationale (from the package) | Original span | Output offset |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| M-1 | §0.1, line 6 | — | Derived (§5) | Version bump | [111, 130) | 111 |
| M-2 | §0.1, line 8 | — | Derived (§5) | Execution date | [153, 183) | 153 |
| M-3 | §0.1, line 9 | — | Derived (§5) | Gate from the recorded source | [186, 292) | 186 |
| RL-14 | §1 "Vendor ingest (HDAPI)", line 119 | C-02 | 2.1 D-2, l.288–289 and l.303; Product Owner direction 2026-11-02 | Product Owner direction (2026-11-02): keep the dated record, but stop calling the legacy route a fallback. Its title and "non-v2 bases retain an explicit legacy `bodygraphs` fallback" contradict D-2 and §7.1.10. The pin, the nonclaims and the §§7.1.10, 7.2 and 7.4 pointer are kept. | [15975, 16690) | 15900 |
| RL-01 | §4.6, line 956 | C-02 | 2.1 D-2, l.284–289 | D-2 decides that no non-v2 base reaches bodygraphs by fallback and that a terminal v1 base is retained legacy selection. This §4.6 permission stated the superseded posture and contradicted §7.1.10. | [85007, 85104) | 85125 |
| RL-02 | §5.5, line 2493 | C-03; support C-06 | 2.1 D-3, l.349–364 and l.377–378; C-06 l.223, l.506 | D-3 adds the dev/admin gate as step 2 of "Validation and environment gating", withdraws "authenticated" and "internal authentication" from "Success body", and records the no-credential posture, the wider-exposure rule and the accepted residual risk. The gate is not in the code at the snapshot, so the gap is stated beside it. | [189764, 190200) | 190033 |
| RL-03 | §5.5 "Headers & conditionals", line 2509 | C-03 | 2.1 D-3, l.350–355 | Under D-3, a non-production request outside `APP_ENV` dev, test or local is refused with 403 before the method rules. The method rules apply only to an admitted request. | [191897, 191978) | 194385 |
| RL-04 | §5.5 "Parity (clarified)", line 2520 | C-03 | 2.1 D-3, l.358 and l.378 | D-3 supersedes "authenticated" in "Parity (clarified)"; no authentication mechanism exists in canon or code. | [193270, 193326) | 195785 |
| RL-05 | §7.1.10, line 3476 | C-02 | 2.1 D-2, l.281–283 and l.315 | D-2 extends the §7.1.10 scope from bg:resolve to compat chart acquisition by showcompat and conjunction. | [256843, 256973) | 259344 |
| RL-06 | §7.1.11, line 3507 | C-01 | 2.1 D-1, l.229–232 and l.259 | Once D-1 widens the contract to three paths, the S14 delivery covers only bg:resolve. The claim is narrowed to what was delivered. | [259896, 259956) | 262605 |
| RL-07 | §7.1.11, lines 3515–3521 | C-01; support C-06 | 2.1 D-1, l.259; C-06 l.223, l.506 | D-1 turns the limit "The gate covers only the command §7.1.11a names" into a gap against the decision. Bounded inspection at the snapshot confirms the uncovered paths. | [260978, 261835) | 263726 |
| RL-08 | §7.1.11a, line 3533 | C-01 | 2.1 D-1, l.229–234 and l.255 | D-1 supersedes "accepted only by hdctl bg:resolve --source vendor" with the three-path scope. | [262345, 262535) | 265796 |
| RL-09 | §7.1.11d, line 3577 | C-01 | 2.1 D-1, l.235 and l.256 | D-1 rewrites step 2 to "the invocation selects vendor acquisition" for each command. | [265281, 265385) | 269093 |
| RL-10 | §7.1.11d, line 3584 | C-01 | 2.1 D-1, l.236–238 | D-1 sets the scope of one authorization to the bounded acquisitions of one invocation: at most one per party and two for a pair, with no write, no public Reader or Aux traffic and no opening of a closed rail. | [265727, 265850) | 269678 |
| RL-11 | §7.1.11e, line 3588 | C-01 | 2.1 D-1, l.235, l.242–244 and l.257 | D-1 adds the showcompat carrier rule to §7.1.11e and aligns the usage case with the rewritten step 2. | [266196, 266426) | 270252 |
| RL-12 | §7.1.11f, line 3604 | C-01 | 2.1 D-1, l.241 and l.258 | D-1 supersedes the command rule "exactly bg:resolve" with the three values. | [267979, 268015) | 272394 |
| RL-13 | §11.1 Change Log, line 4148 | C-01, C-02, C-03 | PF05 §0.4 and §11.1 (the target's own logging rule) | PF05 §0.4 and §11.1 require a change to transport or the CLI contract to be logged. The entry names v2.5.5, which is the baseline v2.5.4 bumped once by the target's patch scheme; the format carries no date. In `drain-r2` the entry also covers RL-14 ("correct the §1 legacy-route wording to terminal-v1 legacy selection with the §7.2.0 non-v2 gap"). | [309120, 309474) | 313585 |

RL-01 to RL-12 are byte-identical to `drain-r1`. The preparer's proof log §7 maps every item of the selected units to these redlines, to an already-represented location, to another target, or to a hold. Its §1A records the Product Owner's direction behind RL-14.

## 7. Application and preservation

Application. The 17 validated operations were applied once, in descending original offset, and each was checked against its original span immediately before replacement. No anchor was rematched in changed text. The file was handled as raw UTF-8 with LF line endings and no normalization.

Preservation checks, all passed:

- Reconstruction. The output equals the stream built, in original order, from the original's untouched intervals and the 17 payloads.
- Untouched intervals. Every interval between operations, and the tail after the last one, appears verbatim at its shifted output offset: 322,442 characters, which is all of the original outside the 17 spans.
- Payloads. Each NEW block occurs exactly once in the output. Each OLD block is absent, except RL-13's, whose NEW block keeps the v2.5.4 line by design.
- Line-level audit. A line diff of original against output shows exactly 17 changed hunks, one per operation, and 4,444 identical lines.
- Cross-checks. The output equals the `drain-r2` simulation (SHA-256 `1587ea2110a62813f82e43c715c45c5dc097aecc88aabb9c2f71914667e2bad6`) except in header lines 6, 8 and 9, which the simulation leaves at their v2.5.4 values by design. Against the `apply-r1` output (SHA-256 `8afbfb89fcbe461c192862a661ce9844b6537f4b0743ad3d60c9a65707f54331`), it differs only at line 119 (RL-14) and line 4166 (the extended RL-13 entry).
- Structure. LF only, zero CR bytes. The file still ends with `---` and one blank line. The counts of code-fence lines and table lines are unchanged.
- Legacy-route wording. Every remaining occurrence of "fallback" near "legacy" (lines 119, 956 and 3497) is a negation ("legacy selection, not fallback").
- Drafting markers. There is no `TODO`, `TBD`, `FIXME` or draft-status language about the document. The three "Draft"/"draft" hits (lines 1194, 1738 and 1761) are canon content: the JSON Schema dialect name "Draft 2020-12", and a historical rationale. Existing `[OPEN]` markers are canon-recorded open decisions.

| Measure | Original | Revised |
| :---- | :---- | :---- |
| Path | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md` | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF05/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.md` |
| Version | v2.5.4 | v2.5.5 |
| Bytes | 327,342 | 332,395 |
| Lines | 4,461 | 4,479 |
| SHA-256 | `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028` | `e220991aafc946c990f9be859078d13921da1b8d3677a9a186ad9569a537319d` |

These are text checks on the document, not product QA.

## 8. Constraints, limitations and nonclaims

- The applier prepared no edits, improved no prose and performed no PF03 cleanup. The pre-existing ellipses in PF05 examples (original lines 279, 2117, 2188, 2495 and 3239) are retained.
- RL-14 keeps the §1 bullet a dated record pinned to `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`. That commit is not in this clone's shallow history. The bullet makes no new claim about it; it re-characterizes what the record already stated, and current code still shows that behaviour (preparer's proof log §1A).
- The new repository-state statements in RL-02 and RL-07 are pinned to `main@e2b7427ff418ca8f08f05587c4a541308a76da56`. They come from the preparer's bounded, read-only inspection under closed rails and establish no runtime behavior.
- Held work stays held: H-09 (the PF05 §7.2.0 gap row) waits until the implementing change for Candidate CRD Items List item 9 delivers. H-05 (AGENTS.md) is outside this package, in draft PR #827.
- The revised PF states the D-1 and D-3 gates as Required-Now gaps. Nothing here claims they are implemented.
- This application changes no `docs/pfcanon/` file, Specification, AGENTS.md or other task's file. It establishes no QA verdict, acceptance, deployment, PF09 movement or closure.

## 9. Save state

| File | Path | Bytes | SHA-256 | Verified |
| :---- | :---- | :---- | :---- | :---- |
| Revised PF (`apply-r2`) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF05/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.md` | 332,395 (4,479 lines) | `e220991aafc946c990f9be859078d13921da1b8d3677a9a186ad9569a537319d` | Read back in full from disk: byte-identical to an independent re-derivation from the original and the saved redlines, with the 17 changed regions audited |
| Proof log (`apply-r2`) | This file | — | Not self-hashed | Read back in full after writing, and again after this receipt was added |

Completion receipt (`apply-r2`, 2026-11-02, UTC). Both outputs were read back from disk in this session. The revised PF matched an independent re-derivation byte for byte, and its 17 changed regions were audited. This log was read back in full; its identities agree with the revised PF and with the package it applies: original, source, ledger rows, `drain-r2` and `apply-r2`.

Save state: `COMPLETE_PACKAGE`. Application result: applied, 17 of 17 operations.

## 10. Next manual action

Nathan reviews the revised PF on draft PR [amthorn78/glow-hdengine-v2#826](https://github.com/amthorn78/glow-hdengine-v2/pull/826), branch `claude/gtwpe-triage-authoring-j94ewf`, and decides whether to transfer it into `docs/pfcanon/`. Nathan merges. The ledger's T-02 completion row records this result.
