# SECTION-10 review, round tw1 — SFR-TW1-2

**Verdict: SKILL_FIT_CONFIRMED.**

The verdict is bound to these exact bytes and to nothing else:

- `tw-flowmaster.skill`: sha256 `88166c3d48fee16900e125f1cf2fe15cf2b46a2e0a6ac05ea0fdd5ef3c1a4b89`, 19,193 bytes, 2 entries. It extracts to 2 files, 55,131 bytes, tree digest `0581205ba29f195ce784ff585ca9019de5644750c9e357b06e377e91827a722c`, revision 1.3.0.
- `flowmaster-validate.skill`: sha256 `e1f495b3f40f9a75c713433236391763505cb3895364076f71eb771a72710f3f`, 322,860 bytes, 31 entries. It extracts to 31 files, 1,915,296 bytes, tree digest and declared `SKILL_TREE_SHA256` `284b3ac150bedb51054aa9b3d0ce7ddfc1679d29dfb4178ded6095022d1fd733`, revision 3.3.2.

The two packages are installed together. The verdict is void for any other bytes.

- **Required findings: 0.**
- **Listed findings: 2.** Neither blocks under D26-A rule 3. They go to Nathan as accepted risks or as an opt-in.
- This is a static review. Under HDE Governance §9.1.6 it is not runtime validation of a TW Flowmaster run.

## Identity and freeze

- **Baseline reproduced first,** using `skill_tree_digest` imported from each measured tree, with `PYTHONDONTWRITEBYTECODE=1`:
  - installed tw-flowmaster: 2 files, 58,775 bytes, `fd6c344b…f5576617`, revision 1.2.0;
  - installed flowmaster-validate: 31 files, 1,914,948 bytes, `ed52208f…3cc572af`, equal to its declaration, revision 3.3.1.
- **Every §1 value was derived from the bytes I was given:** archive sha256, sizes and entry counts; extracted file counts, bytes and tree digests; SKILL.md size and sha256 (`21c632e1…b09b1575`). All entries sit under their skill root, with no `..`, no absolute path, no symlink, no directory entry and no duplicate; `testzip` is clean. The frontmatter of each SKILL.md is byte-identical to the installed one, including `name:`.
- **Freeze held:**
  - The synced skill directories (338 files, 30 skill directories) were hashed at 13:38:45Z and again at 13:51Z. They were identical, with no `__pycache__`.
  - Both archives were unchanged at the end.
  - The branch head stayed `80d226c0…` throughout, and the repository working tree stayed clean.
  - I did not read or hash the synced root's `manifest.json`: the session's permission layer refused that read. It is sync-layer bookkeeping, which `skill-identity-and-freeze.md` excludes from freeze digests.
- **`freeze.py` values, so that a post-install check by the convention's own command has a reviewed value (L11):**

| Skill | `freeze.py` result | Compared with `skill_tree_digest` |
|---|---|---|
| tw-flowmaster | `2 0581205b…a827722c` | Equal |
| flowmaster-validate | `31 90c15e985a0c4b78d24298fe8187e8a50576689ddfc509d09fa11187ab97fcc2` | Differs, because `freeze.py` keeps the `SKILL_TREE_SHA256` line |
| flowmaster-validate, installed | `31 0ca2a74d…` | — |

  This verdict binds both values.

## Gates I ran (all from a fresh extraction, in `scratchpad/review-SFR-TW1-2/`)

| Gate | Result, by its own top-level flag |
|---|---|
| `validate_flowmaster.py --skills-root $R --strict-warnings`, where $R is the 29 synced skill dirs other than canva, with the two extracted skills in place of the installed ones | exit 0. `verdict` FLOWMASTER_SUITE_PASS, `suite_ok` true, `self_identity` OK, `validator_revision` 3.3.2. All finding counts 0, `warnings` []. All six Flowmaster skills PASS with 0 errors and 0 warnings, `core_sync` true. Change-flow fixtures: `fixture_suite_ok` true, 32/32 (13 positive, 19 negative). GCFPE current fixtures: `fixture_suite_ok` true, 236/236 cases, section-13 37/37 and 38/38. Direct handoff `ok` true |
| `guard_proof.py $R <scratch>/guard` | exit 0, 12/12 PASS. Each live case: exit 1, with 1 tw-flowmaster error. Each disabled case: exit 1, with 0 tw-flowmaster errors |
| One guard case by hand (`PF_RENDERED_PAGE_COUNTS`) | Live: the only error is `superseded contract present: PF_RENDERED_PAGE_COUNTS`. Disabled: exit 1 only on `SKILL_SELF_IDENTITY:DECLARED_284b3ac150be_MEASURED_76e22e7bc4c1`, with no tw-flowmaster error, as the brief predicts |
| `skill_edits.py <synced root> <scratch>/rebuilt`, then `diff -r` of each rebuilt skill against the extracted one | exit 0, `edits 32`, `SKILL_TREE_SHA256 284b3ac1…`. Both diffs empty |
| Each of the 32 `old` strings counted in the *original* installed files (the script itself checks only sequentially) | Each occurs exactly once. No CR bytes in any edited file |
| `diff -rq` of installed against extracted | Exactly the six listed files, and nothing else |
| skill-creator `quick_validate`, run from the root's copy, on each extracted skill | `Skill is valid!`, exit 0 for both |
| Installed 3.3.1 validator on a baseline isolated root (the installed trees), full report compared with the review root's report (paths normalized) | Baseline: FLOWMASTER_SUITE_PASS, exit 0. The reports differ in exactly 2 values: `validator_revision` and `gcfpe_current_fixtures.validator_revision`, both 3.3.1 → 3.3.2 |

**Gates I could not run:**

- X3 post-install validation: nothing is installed, by design.
- Anything in Notion: prohibited by the brief's §9.
- Prompt bodies: prohibited by D22.
- Any runtime TW Flowmaster run: no executable TW check exists (K-6).

**The author's measurements:** each one reproduced, and none was contradicted.

## The claims

- **C1 — confirmed.** 32 literal edits, each matching once in the originals, in six files; `SKILL_TREE_SHA256` recomputed and equal to the measured tree; the rebuild is byte-identical.
- **C2 — confirmed.** The core block is 18,255 bytes, sha256 `4d8bb9bf…d409`. It is identical in the installed tw-flowmaster, the extracted tw-flowmaster and flowmaster-primary, and also in change-flow, session-branch-flowmaster and session-relay-flowmaster. It equals the report's `primary_sha256`.
- **C3 — confirmed.** See A1 and A2. tw-flowmaster names no TW-ASSESS-10, analyzer or strength term anywhere in the file. `CONTRACT_REQUIRED["tw-flowmaster"]` requires 1.3.0 and drops exactly the three old terms. `CONTRACT_FORBIDDEN["tw-flowmaster"]` adds exactly the six identifiers; no other skill's lists changed.
- **C4 — confirmed,** as in the table above.
- **C5 — confirmed.** The quotes match the record:
  - §A *Revision of 2026-09-30*, record lines 373–384;
  - `analyze_approved_by`, line 88;
  - `plan_approved_by`, line 90.

  The bytes stay inside that authority:
  - There is no refusing guard. tw-flowmaster cannot even name TW-ASSESS-10, because the validator forbids it.
  - The validator guard is kept.
  - Beyond removal, the only changes are the revision moves that `skill-identity-and-freeze.md` requires, and the rewrites of the profile condition and of READY's route that "matching the new prompts" requires.
  - The convention's identity diff shows every advertised value moved. A search of the repository's `docs/` finds no earlier use of validator 3.3.2 or TW 1.3.0.
  - A canon-basis note is listed as SFR-TW1-2-L2.

## Answers to §6

**A1. Nothing in 1.3.0 routes a selected-catalog TW run through an assessment, and no fixed-model or page-count clause remains to govern one. I found nothing beyond K-1.**

What now governs a selected-catalog run:

- The condition (line 328) is "carry the exact no-redlines contract". No edit in `edits.json` touches that contract, so the profile still matches the new release.
- Assessment wording appears only in GCFPE lines 312, 314 and 444. The core (lines 12–228) has none. TW-ALPHA members are not GCFPE members (§A).
- The fixed-model and page-count clauses are gone from the whole file: 0 hits for Sol, GPT, Ultra, rendered or page count. "Max" appears only in the stall prohibition (line 339).
- Direct creation-to-application now governs the profile run, by design:
  - Line 330 supersedes only the repository-source and all-targets-must-apply clauses.
  - *Redline application* (lines 440–449) dispatches TW-APPLY-10 after a validated creation.
  - This matches `edits.json` DRAIN-10.04 and .09 and DRAIN-20.04 and .09 ("the immediate next prompt is TW-APPLY-10"), APPLY-10.04 and .05 ("Work can be invoked directly."), DRAIN-10.08 and APPLY-10.12 (a corrected package without pre-Apply), and DRAIN-10.11 (no recommendation field). Lines 335 to 337 mirror each of these.

Two refinements of K-1, not findings:

1. **The K-1 window is likely loud, not silent.** Line 335 accepts a READY output only when it "points to TW-APPLY-10", and line 436 forbids advancing an unverified creation. The old drains' READY step, quoted in `edits.json` as DRAIN-10.09's `old` text, names "TW-ASSESS-10 assessing TW-APPLY-10, not direct application". The old Apply says "direct invocation never bypasses assessment" (APPLY-10.05's `old` text). These rest only on `edits.json` quotes (D22), so K-1's "would skip them" stays the conservative statement.
2. **A run resumed across the install has the same consequence through another entry.** A run started under 1.2.0 and resumed under 1.3.0 inside the window is K-1's consequence reached another way. After X4.3 its pinned versions are no longer selected members, so the profile stops applying. 1.2.0 already had that fall-through for any run resumed across a selection change.

**A2. The edited sentences read coherently, and nothing kept imposes a fixed model or effort policy on a non-GCFPE stage.**

- Old line 339's kept rule is now line 334, "Record actual configuration only when directly verified.", and stands alone.
- Lines 345 and 346 (old 351 and 352) and line 444 (old 451) keep only their GCFPE sentences.
- The GCFPE binding block (lines 297–324, 29 lines) is byte-identical to 1.2.0's.
- What remains of model and effort wording falls into four kinds:
  - GCFPE lines: 310, 312, 314, 345, 346, 386, 444;
  - records of actual state: 334, 434, 474;
  - the stall bullet's prohibitions: 339;
  - the `/model` control preference, which names no model: 348.
- Line 312's last sentence, "Non-GCFPE runs retain their existing scoped defaults", pointed in 1.2.0 at the removed policies. In 1.3.0 the only such default for TW is none, so it imposes nothing. It sits inside C4's kept text.
- Line 335's "PF10 triage remains list-only and exempt" lost its likely object, the assessment checkpoints. It now reads as exempt from application, which has no consequence.

**L8: the wording is confirmed; the consequence is refuted.**

- Line 386 now attaches "only the capabilities required" to "the GCFPE target", so the wording point stands.
- But selected-catalog TW runs are bound by line 333 ("Require only capabilities needed by the pinned stage").
- And every run is bound by the core's session-scoped capability rule (lines 180–186: each *required* capability is invoked only from ABSENT, and only when authorized).
- The residual effect is wording only.

**A3. No consumer pins the validation profile's bytes or hash, every path consumer agrees, and GCFPE validation is otherwise unchanged.**

- Neither sha256 (installed `1690c91d…`, built `3f35e35c…`) occurs anywhere in the root.
- In the repository, read through `git show` (`docs/prompt_ecosystem_management`, `docs/graph`, `docs/ephemeral`, `tools`, `ci`, `scripts`, `.github`), `1690c91d…` appears only in a dated historical record: the closeout-residuals `manifest.json`. No executable or current convention reads either skill's identity.
- The path consumers:
  - `validate_gcfpe_20260914.py`: `PROFILE_PATH`, then `load_profile`'s `PROFILE_IDENTITY` subset, which expects `"3.3.2"` and agrees;
  - `run_gcfpe_20260914_fixtures.py`, through `load_profile`;
  - `validate_flowmaster.py`: `REQUIRED_SCRIPTS` (existence) and `SELF_FORBIDDEN` (a phrase that is still absent).
- change-flow's own scripts do not read the file. Its `PROFILE_IDENTITY` error appears under change-flow only because that check runs flowmaster-validate's loader.
- The file's bytes are covered only by `SKILL_TREE_SHA256`, which was recomputed and equals the measured tree.
- The profile diff is that one line. The full reports differ only in `validator_revision`; the contract sha `dbae180b…`, the graph `ae2bd159…` and the fixture results are unchanged.
- Not searched: Notion (L13; prohibited).

**A4. Nothing still expects the old terms.**

- The removed TW identifiers and phrases (PRE_CREATION_ASSESSMENT, PRE_APPLY_ASSESSMENT, ULTRA_IF_RENDERED, TW-ASSESS, STRENGTH_ANALYZER, APPLICATION_REASONING_POLICY, PF_RENDERED_PAGE_COUNTS, two-checkpoint, pre-Apply, pre-creation), searched case-insensitively across the whole root, appear only in the new guard (`validate_flowmaster.py` lines 312–319) and in flowmaster-validate SKILL.md line 184's account of the removal.
- No fixture or reference names TW at all: `flowmaster-validate/fixtures`, `flowmaster-validate/references`, `change-flow/references` and `glow-graph-contract` were all searched.
- "1.2.0" survives only as other skills' own revisions.
- "3.3.1" survives only as `CHANGE_FLOW_SPECIALIZATION_REVISION`, which is change-flow's identity and not the validator's:
  - change-flow SKILL.md line 8;
  - change-flow's `validate_gcfpe_20260914.py` line 746;
  - flowmaster-validate's `validate_gcfpe_current.py` lines 640–641;
  - `validate_flowmaster.py` lines 146 and 1334;
  - the profile's `installed_skill_revisions`.
- No old file hash or tree digest of either skill is pinned anywhere in the root.

## Listed findings (not required; D26-A rules 3 and 4)

**SFR-TW1-2-L1 — The validator guard sees identifiers, not the removed wording.**

- **Artifact:** `flowmaster-validate/scripts/validate_flowmaster.py`, `CONTRACT_FORBIDDEN["tw-flowmaster"]`.
- **Defect:**
  - None of the six identifiers occurs in the removed fixed-model sentences or in the old profile condition.
  - `ULTRA_IF_RENDERED_PAGES_GT_100_OR_UNKNOWN` left `CONTRACT_REQUIRED` without entering `CONTRACT_FORBIDDEN`.
  - Reinstating old line 351 ("use GPT-5.6 Sol with Max reasoning …") would pass the validator.
  - So would reinstating the old condition ("carry the mandatory pre-creation/pre-Apply assessment and exact no-redlines contracts"). That revert would silently stop the profile matching the new release and route TW runs to the legacy repository-source clauses, which is §A's S-1 path.
- **Evidence:**
  - Counted case-insensitively in the 1.2.0 file and then the 1.3.0 file: `Sol Max` 2→0, `Sol Ultra` 1→0, `GPT-5.6` 1→0, `two-checkpoint` 1→0, `pre-Apply` 5→0, `pre-creation` 1→0, `rendered PF page count` 1→0, `ULTRA_IF_…` 1→0.
  - None of these is forbidden.
  - The prompt-side `absent_after` check is broader: it includes `Ultra`, `GPT-`, `pre-Apply` and `analyzer`.
- **Classification:**
  - Path: future maintenance. Likelihood: low. Consequence: a silent regression that no gate catches.
  - Listed rather than required, because these bytes implement exactly the guard that §A proposed, that Nathan's analysis approval kept, and that the approved plan fixed.
- **Smallest correction (Nathan's opt-in only).** It needs new bytes, a new revision and a fresh D24 round:
  - add those eight strings to `CONTRACT_FORBIDDEN["tw-flowmaster"]` (each is 0 today);
  - optionally require "carry the exact no-redlines contract" and "READY creator output points to TW-APPLY-10." (each occurs once).

**SFR-TW1-2-L2 — The record's canon basis omits HDE Governance §9.1.3's advice requirement.**

- **Artifact:** the record's §A *Consult (Canon)* and its *Canon and rulings relied on* lists in §A and §P. This is not in the package bytes.
- **Defect:**
  - §9.1.3, on `main` at `f83c755`, still says "Every downstream-session prompt must receive task-specific human advice for execution surface, model and reasoning level".
  - PF10 2.38 says that requirement "is outside this addendum. Whether it continues is open for Product Owner determination". It also says 2.31 left that requirement unchanged.
  - The record cites §9.1.6, 2.31 and 2.38, and concludes "canon permits the headers and requires none" without reading §9.1.3.
  - 1.3.0 gives TW stages no advice; GCFPE stages keep theirs.
- **Disposition:**
  - Nathan's direction of 2026-09-29 ("no hard coded model recommendations or strength assessments at all"; TW-ASSESS-10 retired with no replacement) is formally approved as ITEM-01, ITEM-02 and ITEM-04.
  - It adjudicates exactly this scope, so under AGENTS.md's rescope clause it governs here. It is also the determination that 2.38 leaves to him.
  - The packages are therefore fit.
- **Classification:** path: documentation. Likelihood: certain. Consequence: low. A later audit applying §9.1.3 could read TW runs as non-conforming.
- **Smallest correction:** a dated successor note, in §E or in `CHANGE-NOTE-tw1.md`, naming §9.1.3 and Nathan's direction as its determination for TW. No byte change and no canon edit.

## Limits

- **"Matching the new prompts" was checked only against `edits.json`'s `new` texts and the record (D22).** One point cannot be confirmed without the bodies. The old text "The analyzer returns the populated TW-APPLY-10 invocation" is removed (DRAIN-10.10). Line 335 now expects that invocation in the drain's own READY output. That rests on the drains' unread handoff text (K-5).
- **Nothing outside my scratch directory was written:** no repository file, no Notion page, no install and no agent.

## Canon relied on

- **`AGENTS.md`:** the canon-first rule; PF canon is read-only; the truncation guardrail.
- **Canon search:** `git grep` on `origin/main` (`f83c7559`) over `docs/pfcanon/` for tw-flowmaster, flowmaster, TW-ASSESS, skill package, interacting skill, model advice, technical writing flow and GTWPE, plus PF10's addenda index. Hits came only in the sections below.
- **HDE Governance (PF04) v2.8.6:** §9.1.3 and §9.1.6, read in full; §9.1.4 and §9.1.5, read but not applied.
- **HDE Build Notes (PF10) v13.5:** 2.31 PF10-HDR-001 and 2.38 PF10-AINEUTRAL-001, read in full.
- **Repository documents, on branch `docs/20260930-modification-gtwpe-tw-model-advice` at `80d226c0`:**
  - the record: §A (Consult, Scope, Revision of 2026-09-30, the dry runs, Canon); §P (Values, Evidence files, Steps, The skill edits, The D24 brief, K-1 to K-6, L1 to L21 and DL-1 to DL-9, the successor of 2026-10-04); §E (X1.0 to X1.3);
  - `skill_edits.py`, `guard_proof.py`, `packages-tw1.json`, `edits.json`, `D24-BRIEF-tw1.md`;
  - `skill-packaging-and-delivery.md` 1.1, `skill-identity-and-freeze.md` 1.0, `freeze.py`, `reviewer-prompt-template.md` 1.2;
  - `gcfpe.decision-record.md` D22, D24 and D26.

This record is new for this reviewer ID. It corrects no earlier record (AUTH-001).

IN FLIGHT
