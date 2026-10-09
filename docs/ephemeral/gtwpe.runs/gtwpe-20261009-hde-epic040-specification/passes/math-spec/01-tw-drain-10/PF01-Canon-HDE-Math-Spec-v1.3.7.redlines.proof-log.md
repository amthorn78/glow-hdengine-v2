# Proof Log — HDE Math Spec (PF01) redlines

## Identity and association

- Proof log for: `PF01-Canon-HDE-Math-Spec-v1.3.7.redlines.md` (same directory).
- Run: `gtwpe-20261009-hde-epic040-specification`.
- Prompt: `TW-DRAIN-10 — Prepare PF Document Redlines — 100726.1` (Notion `3f24590a05eb81fc872ad0003ac03086`).
- Pass directory: `docs/ephemeral/gtwpe.runs/gtwpe-20261009-hde-epic040-specification/passes/math-spec/01-tw-drain-10/`.
- Originating preparer: TW-DRAIN-10 pass inside the GTWPE-FLOW-10 run above (this session).
- Preparation outcome: `READY`. Save completeness: `COMPLETE_PACKAGE`.

## Target (original identity and version)

- Directory + versionless name: `docs/pfcanon/` → `HDE Math Spec`.
- File: `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md`.
- In-document title: `PF01-Canon-HDE-Math-Spec`.
- Version: `v1.3.7`. Status: `Canon`. Effective date: `2026-08-25`. Last Update Gate: `BN 12.8.9`.
- Base blob (git): `ba07b5606153cadd033e41b1a8aafb967af10ea1`.
- Baseline SHA-256 (full bytes): `101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a`.
- Line count: 2441.

## Authority and sources (each read whole)

| Role | Source | Version / identity | SHA-256 |
| --- | --- | --- | --- |
| Governing change source | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` | v13.5 | `54df666e3c019c095e52bf8b0ce5376a79441e7afb5950305a5dcb32505ce795` |
| Incoming source (run input) | `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` | v1.2 | `09cfee2847c9dec09ab9b2f2106a42fbaa9badfff1d9dcbdf900180e98972def` |
| Incoming source (run input) | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` | v1.1 approved | `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| Incoming source (triage) | `docs/ephemeral/gtwpe.runs/gtwpe-20261009-hde-epic040-specification/passes/triage/01-tw-triage-10/triage.md` | — | `b418e5d9d13bc1ec13cbe75c67910ec17fe8542d5a8ef6c9c24d591731cfe6e0` |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` | v1.8.7 | `cb123d2134b634c64589c1e193ef41a0bb5045f5d0b3fc85a8ff2cd3336399f3` |

Canon was read from `origin/main` at intake `0c4dddece401c457b2429ddc9cb8f2e819b4a943`. `git hash-object` of the target and each `docs/pfcanon/` source equals the base blob recorded at intake; `docs/pfcanon/` is unchanged from that commit. Working branch `docs/20261009-gtwpe-run-hde-epic040-specification`.

Governing PF10 addenda read in full: `2.5` (C040-06; timestamp `2026-09-09T13:43:26Z`, C040-06 alternative A approved `2026-09-09T11:48:08Z` by Isis-50), `2.23` (C040-07; approved by the Product Owner `2026-09-26`), `2.25` (C040-08; approved by whole-change IA on Product Owner direction `2026-09-26`). Closure decision v1.2: decision `CLOSE`, state `CHANGE_CLOSED`, time `2026-09-29T19:53:33Z`. Specification v1.1 approval: `APPROVE` by Thoth `2026-09-08T13:23:24Z`.

## Change/disposition ledger

The triage file names exactly three changes against this target, all `HDE-EPIC040` (shown `CHANGE_CLOSED` by the closure decision):

| Change (PF10 addendum) | Disposition | Redlines | Supporting location |
| --- | --- | --- | --- |
| `2.5` C040-06 — Channel taxonomy / existing-state conformance | Drain the sixteen-case existing-predicate conformance oracle and route the static taxonomy home | `R22` | PF10 §2.5 "Complete approved existing-state conformance oracle" + "Permanent drainage targets and owners" (row `HDE-Math-Spec §§6.1–6.2`) |
| `2.23` C040-07 — Reader v2 / full Magic-10 exposure | Define the Reader v2 projection alongside v1; resolve every "future, versioned change" / preset / pack-change statement; state the v2 preimage and per-version emission rules | `R1`–`R18` | PF10 §2.23 "Canon decision and drainage — C040-07", drainage row `PF01 — HDE Math Spec` |
| `2.25` C040-08 — Reader v1 error-envelope conformance | Conform §2.3 to the delivered four-key error envelope (`schema`, `ok`, `code`, `error`; no `retry_after_ms`, no `details`) | `R19`–`R21` | PF10 §2.25 objective/required-delivery/closure ("The v1 error branch requires schema, ok, code and error. It has no retry_after_ms.") |

No other change in the closure decision or the specification bears on PF01 (the specification's §10.3 ADR proposals C040-01–04 are already canonized by PF10 §2.2 and drain to other documents, not PF01). No change is held back: HDE-EPIC040 is `CHANGE_CLOSED`.

## Substantive changes made (summary)

- **§2**: heading updated to "Reader v1 and v2" (`R1`); §2.2 "future, versioned change" statement resolved to the delivered Reader v2 (`R2`); new §2.5 defines the Reader v2 public projection — same six success keys with `reader_version: "v2"`, exactly ten `{id, band}` items in canonical governed order (`harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`), `[]` when ineligible, ordered (not set-sorted), and Reader v1 unchanged (`R3`).
- **§2.3**: error object is exactly four keys `{ok, code, error, schema:"v1"}`; `retry_after_ms` and `details` removed; heading drops the numeric exception; posture note conforms (`R19`–`R21`).
- **§3.2**: Reader v2 five-key preimage stated (shared recipe, `reader_version:"v2"`, ten-item array) (`R4`).
- **§4.4 / §4.7**: per-version emission rules (v1 one item, v2 ten items; ineligible `[]` both versions) (`R5`–`R8`).
- **§5.1 / §5.4.4 / §5.6**: "future, versioned change"/"future public exposure"/"(future)" statements resolved to Reader v2 (`R9`–`R11`).
- **§1 map**: Reader bullet, Magic-10 bullet, public projection, and preset public rule reflect Reader v2 (`R12`–`R15`).
- **§7.4 / §8.4 / §12**: preset/aggregation/implementation public-boundary statements reflect Reader v2 (`R16`–`R18`).
- **§6.1**: added the exhaustive sixteen-case existing-state conformance oracle (CS-01…CS-16) as a clarification of the existing §6.1 five-state predicates, with normalized full-owner attribution and no independent hanging-Gate contribution, and routed the static Channel taxonomy (circuit/substream classification + thirty-six-row assignment) to HDE-Schemas & Artifacts §2.1 (`R22`).

## Basis for the changes

- C040-06: PF10 §2.5 "Complete approved existing-state conformance oracle" (CS-01…CS-16 table and its priority/ownership/seven-four-two-two-one reading) is the authoritative sixteen-case expansion; the drainage table limits PF01 to the existing-predicate clarification and routing, not the taxonomy table itself.
- C040-07: PF10 §2.23 "Canon decision and drainage — C040-07" defines the Reader v2 contract (six keys, ten categories in canonical `catalog/magic10.json` order, ordered array, v1 unchanged) and lists the PF01 drainage obligations.
- C040-08: PF10 §2.25 required delivery item 1 and the closure state define the four-key v1 error envelope and the removal of `retry_after_ms`/`details`.

## Constraints, assumptions, interpretations

- Reader v1 statements are preserved verbatim wherever they remain true; only the "future/versioned change" and now-inaccurate error-shape claims are changed. Reader v2 is added, never substituted for v1.
- The new §2.5 is appended after §2.4's closing paragraph (a `REPLACE` of that unique paragraph), avoiding a renumber of §2.3/§2.4.
- The sixteen-case oracle is placed immediately before the existing §6.1 "Throat flags" heading via a `REPLACE` of that unique heading, so no new top-level section numbering is introduced.
- Document-control fields (version, dates, Last Update Gate) are reserved for TW-APPLY-10's header contract and are not prepared as redlines. PF01's §0.2 states it "does not maintain revision history", so no change-log entry is required.
- The §6.1 "Detection (normative rules)" heading's pre-existing leading-space formatting is out of scope and left untouched.

## Validation and verification

- Complete target read: all 2441 lines of PF01 read (structure map + full line-level reads of every edited section and all intervening content).
- Complete source reads: PF10 addenda 2.5, 2.23, 2.25 in full (plus their index/register references); the closure decision (190 lines); the specification (412 lines); the triage (114 lines); PF03 (613 lines).
- Anchor/count check: for every redline, the OLD block (or the §6.1 heading used as the R22 OLD) was programmatically counted in the exact target bytes — `observed occurrence = 1` for all 22 redlines; the INSERT-style ambiguity was eliminated by converting R22 to a `REPLACE` on the unique heading.
- RL-045 regression: every single-occurrence edit is authored as `REPLACE` (none as `FIND_AND_REPLACE`); no repeated-replacement operation is used.
- Non-overlap/conflict: the 22 OLD blocks target distinct, non-intersecting lines (R19=248, R20=250–256, R21=263 are adjacent in §2.3 but disjoint; all other ranges are far apart). No two redlines consume intersecting text.
- One-pass simulation: applying all 22 `REPLACE` operations to a copy of the target (non-overlapping, in-place) yields a coherent result in which every NEW block is present and no fully-replaced OLD block remains (append-style NEWs for R3/R4 legitimately re-include their OLD as a prefix). Simulated line count 2442 → 2489.
- Fence integrity: 44 fenced blocks (22 OLD + 22 NEW), fences are four backticks and are longer than any fence in the payloads.
- Saved-pair verification: both files read back after writing (see "Preparation/save outcomes").

## Outside dependencies

- None. The three changes are all `HDE-EPIC040`-scoped and `CHANGE_CLOSED`; no change belongs to an unclosed epic or CRD, and no decision or file from Nathan is required for this preparation.

## Preparation/save outcomes

- Artifact produced: `PF01-Canon-HDE-Math-Spec-v1.3.7.redlines.md`, terminating in `END OF REDLINES`.
- Companion: `PF01-Canon-HDE-Math-Spec-v1.3.7.redlines.proof-log.md` (this file).
- Both files committed and pushed on branch `docs/20261009-gtwpe-run-hde-epic040-specification` (never merged).
- Completion state: `READY` / `COMPLETE_PACKAGE`.

## Input/output filenames, versions, paths

- Inputs: the five sources listed in the authority table above.
- Outputs:
  - `docs/ephemeral/gtwpe.runs/gtwpe-20261009-hde-epic040-specification/passes/math-spec/01-tw-drain-10/PF01-Canon-HDE-Math-Spec-v1.3.7.redlines.md`
  - `docs/ephemeral/gtwpe.runs/gtwpe-20261009-hde-epic040-specification/passes/math-spec/01-tw-drain-10/PF01-Canon-HDE-Math-Spec-v1.3.7.redlines.proof-log.md`

## Next owner and prompt

- Next owner: Nathan (the only merger; TW-APPLY-10 runs under his direction).
- Next prompt: `TW-APPLY-10` (versionless role name), carrying the exact original, the completed redlines file and this proof log, each by repository path and nothing else.
