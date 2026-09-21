---
artifact_type: SKILL_FIT_SECTION_10_VERDICT
artifact_version: "1.0"
created_date: 2026-09-21
author: SFR-01
release: GCFPE-20260914.1 / 091426.1 / 55
subject: Independent §10 validation of the round-26 flowmaster-validate package (corpus-mirror removal)
supersedes: nothing — successor record to docs/ephemeral/gcfpe.round25/SECTION-10-REVIEW.md
---

# §10 verdict — round 26 (the prompt-corpus mirror removed)

## Verdict

**`SKILL_REPAIR_REQUIRED`**, on four findings. A fifth and a nit are non-blocking.

Bound to exactly:

    flowmaster-validate.skill   29 files, 282752 bytes
    sha256 2495b2354d93414a0aa8dea3e40569b3fc5004100e22beeb2b56dca11589a805
    extracted tree digest (freeze.py, rooted at the skill directory)
    29 54604cf33194858521b714c29bb94b39ef4b7bd913e652aceaf0bb4cba773948

**This verdict is void for any other bytes.**

The direction is right and most of the work is done. The corpus walk, the `--prompt-dir` option in
the GCFPE path, body hashing and the storage-location check are genuinely gone, and the four
deleted checks were correctly identified as describing a directory rather than the ecosystem — I
could not construct a real ecosystem defect that any of them still catches. `PROMPT_BODY_ID_MISMATCH`
is a real gain and works in all three shapes. `SKILL_TREE_SHA256` is the right answer to my `Q3`.

What fails review is that **the all-55 requirement was not actually removed** — it moved. It now
lives one function away and fires as a hard error, so the exact procedure the new policy prescribes
returns `ok: false`. That is not a residue; it is the thing the round exists to remove, still
present and now louder.

## Preliminary: this package arrived under the wrong reviewer prompt

The prompt supplied to me was **round 24's** (`§1` naming `e8f30b9a…` / 279481 bytes, `§3` naming
baseline `5dcb95a9…`). Neither describes these bytes. Per that prompt's own `§3` I stopped before
reviewing, identified the artifact, and found the correct prompt checked in at
`docs/ephemeral/gcfpe.round26/REVIEWER-PROMPT.md` on `pe35/round26`, whose `§1` and `§3` match my
independent measurements exactly. The Product Owner confirmed I should proceed under it, and this
review is conducted under the round-26 prompt. No scope was invented.

**One movement under me, disclosed.** `pe35/round26` advanced from the named commit `f3bbc548` to
`49c6acf`. The delta is one file — `REVIEWER-PROMPT.md` itself, added after the commit it names. No
packaged byte, no `REPORT.md`, no patch moved. The review is not void.

## What is installed, measured

| tree | measured here, `freeze.py` rooted at the skill directory |
|---|---|
| installed `flowmaster-validate` | **`29 f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd`** |
| installed `change-flow` | **`21 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2`** |

`§3` is correct: the baseline is round 24's package, which carries my `SKILL_FIT_CONFIRMED`. Both
digests reproduce **unchanged after every experiment**. Nothing installed, nothing written to the
synced skills directory, zero `.pyc`.

## Conformance to the Prompt Corpus Storage and Fidelity Policy

Stated separately from correctness, as `§10` requires. I read the policy verbatim in the Glow
Operations Hub before reviewing.

**Substantially conforming, but not yet conforming.** What conforms: the `rglob("*.md")` walk is
gone; `--prompt-dir` is gone from the GCFPE validators and replaced by `--bodies-stdin` with no path
option; all body hashing and `prompt_body_sha256` are gone; `CANDIDATE_PROMPT_ROOT_MISMATCH`, which
institutionalised `<candidate-root>/prompts`, is gone. Those are the clauses on transcription,
mirroring, raw-byte identity checks and parallel storage locations, and the package satisfies them.

**Two live nonconformances remain**, both against the same clause — *"suggestions that a complete
local corpus is needed before work can proceed"*:

- `SKILL.md` still instructs the operator to pass `--prompt-dir <candidate-root>/prompts` and calls
  a *"required recursively scanned prompt corpus"* the condition for *"a complete candidate pass."*
  That is the prohibited suggestion, verbatim, in the most operator-visible file (**Finding 3**).
- The validator still **requires a complete 55-body set** before it will return `ok: true`. The
  policy's prohibition is no longer merely suggested in prose; it is enforced in code
  (**Finding 1**).

The policy also says *"If an existing skill, prompt, validator, plan, or proposed repair conflicts
with this policy, treat that element as defective."* Both of the above are such elements.

**My own conduct under the accumulation clause, disclosed.** My round-25 review left two real bodies
and three 55-member scratch corpora on disk. I deleted all of them before beginning this review,
along with a cached extract of the 55 recorded body hashes, and built no corpus during it. The one
body I needed (`IA-10`) was read from Notion and piped straight into the validator's stdin; it was
never written to a file. Nothing body-shaped remains in scratch.

## Gates: I ran all of them

From the **extracted package** with the untouched sibling skills restored, scratch copy,
`PYTHONDONTWRITEBYTECODE=1`:

| gate | result |
|---|---|
| `validate_gcfpe_20260914.py change-flow --contract …` | exit 0, `ok: true`, 0 errors |
| same, `--bodies-stdin` with `IA-10`'s real Notion text | **exit 1, `ok: false`, `ARTIFACT_AVAILABILITY_BODY_SET`** — Finding 1 |
| `run_gcfpe_20260914_fixtures.py change-flow --contract …` | exit 0, **155 cases, 0 failed**, `suite_ok: true`, `validator_revision: 3.2.11` |
| `validate_flowmaster.py` | exit 0, **`FLOWMASTER_SUITE_PASS`**, 0 blockers/errors/warnings/advisories |
| `validate_gcfpe_current.py change-flow` | exit 0, `ok: true`, 0 errors |
| `change-flow/scripts/validate_gcfpe_20260914.py` | exit 0, `PASS` |
| `.pyc` written | **zero** |

Nothing was skipped. The one red result is a defect in the package, not a gate I could not reach —
which is the difference from rounds 24 and 25, and to the round's credit.

## The claims

| claim | disposition |
|---|---|
| **C1** no path requires, constructs or walks a local corpus; no path option anywhere | **fails.** The walk and the path option are gone from the GCFPE path, but a complete 55-**set** is still required (Finding 1), `SKILL.md` still documents `--prompt-dir` (Finding 3), and two scripts retain `--prompts <dir>` (Q1) |
| **C2** four checks deleted; nothing became unobservable | **confirmed** — see A1 |
| **C3** `PROMPT_BODY_ID_MISMATCH` is a net gain | **confirmed by execution** |
| **C4** coverage reported, not required; a partial run can never read as a full pass | **fails both ways.** Zero bodies reports nothing skipped (Finding 2); a partial run produces a spurious *failure* (Finding 1), which the report explicitly promises it will not |
| **C5** all body hashing gone, including `prompt_body_sha256` | **confirmed** — no occurrence anywhere in the package |
| **C6** the validator refuses to certify anything on self-identity mismatch | **fails.** One validator refuses; the suite that issues the verdict does not (Finding 4) |
| **C7** hash-pin chain does not move; `change-flow` does not move; package is smaller | **first two confirmed; "smaller" is false** — see the nit |

## The attack (§6)

### A1 — break C2: is any real defect now invisible?

**No. The four deletions are sound and I could not construct a counter-example.**

| deleted check | a real ecosystem defect it might have caught | still caught? |
|---|---|---|
| `PROMPT_BODY_MEMBER_SET` | a member missing from the release roster | **yes** — `validate_gcfpe_20260914.py:1173` still requires 55 graph nodes equal to `EXPECTED_MEMBERS`, from the contract and graph, with no bodies. What is no longer checked is whether a *file* exists for each member, which is a property of the mirror, not the ecosystem |
| `PROMPT_BODY_DUPLICATE` | two bodies for one id | **vacuous** — dict keys are unique by construction |
| `PROMPT_BODY_FILENAME_ID` | a body filed under the wrong id | **yes, better** — `PROMPT_BODY_ID_MISMATCH` compares the body's own header to the key, which a filename check could not do |
| `PROMPT_BODY_UTF8` | undecodable bytes | **vacuous** — `json.loads` yields `str`, and `main()` rejects non-string values with `BODIES_STDIN_NOT_ID_TO_TEXT_MAP` |
| `CANDIDATE_PROMPT_ROOT_MISMATCH` | corpus in the wrong place | **deliberately gone** — it enforced the location the policy forbids |

`C3` verified by execution, all three shapes: `{"IA-10": "Prompt ID: IA-30"}` →
`PROMPT_BODY_ID_MISMATCH:IA-10:IA-30`; a body with no header → `…:IA-10:ABSENT`; an id outside the
roster → `PROMPT_BODY_UNEXPECTED_ID:NOT-A-PROMPT`.

### A2 — attack the digest exclusion

**One real weakness: two materially different `SKILL.md` files produce the same digest and both are
accepted.** `SELF_IDENTITY_RE.sub(b"", data)` removes *every* line matching
`^SKILL_TREE_SHA256: [0-9a-f]{64}\n`, while `SELF_IDENTITY_DECLARATION_RE.search()` honours only the
first. Measured on scratch copies:

| variant | digest | verdict |
|---|---|---|
| untouched | `5bb632ce952b` | accepted |
| **+ a second declaration line with a different value** | **`5bb632ce952b`** | **accepted, silently** |
| **+ 20 extra declaration lines** | **`5bb632ce952b`** | **accepted, silently** |
| a fake declaration placed first | `5bb632ce952b` | caught — `DECLARED_000000000000_MEASURED_5bb632ce952b` |
| declaration line + one trailing space | `615180cffad7` | caught — `UNDECLARED` |
| a declaration inside a `~~~bash` fence | `44c90aec31d3` | caught — declared ≠ measured |

Four of six attacks fail closed, which is good. The duplicate-line case does not (**Finding 5**).
`manifest.json` is not inside the skill root, so `F2` from round 23 is **not** reintroduced by the
unfiltered `rglob`.

### A3 — is reporting sufficient, or should the validator refuse `ok: true` on zero bodies?

**Reporting is the right design, but it is not implemented for the case that matters** — see
Finding 2. My answer to the question as posed: do **not** make zero bodies an error. A contract-only
run is legitimate and common, and failing it would push callers back toward supplying everything,
which is the mirror again. Instead make the report honest in that case: when no bodies are supplied,
`prompt_body_checks_not_evaluated` should name every body-scoped check, not be empty. An operator
following step 4 of the standing procedure would then read the truth, which is the whole premise of
"reported, not required."

### A4 — the round's largest unverified claim, closed

**Closed, and it fails.** I read `IA-10` from Notion (page `3db4590a05eb817aa191f1e822c30480`,
`page_last_edited_at` 2026-09-18T12:09:09Z) and piped its real text straight into the validator with
no file written:

    ok: false
    errors: ['ARTIFACT_AVAILABILITY_BODY_SET']
    prompt_bodies_validated: ['IA-10']
    prompt_body_checks_not_evaluated: ['QA_PASS_CLASS_MAP_AND_INTAKES']

The per-prompt obligations did run — `IA-10` is listed as validated and produced no per-prompt
error, so the writer predicates pass on real text as the report claims. But the run as a whole
returns **`ok: false`**, on a set-scoped check that demanded the other 54 pages. This is Finding 1,
and it is exactly the case `L1` said was untested.

### A5 — is 155 honest?

**Yes, and the count is honest — but one renamed case carries Finding 1 into the fixture suite.**
155 is the same contract-fixture count the installed tree produces without bodies, so no
contract-level case was lost. The body cases are not deleted; they are conditional on
`--bodies-stdin` (`run_gcfpe_20260914_fixtures.py:594`, `:658`) and the comment says plainly that the
suite "reports fewer cases rather than inventing a result." That is the correct posture.

However, the timing case was **renamed** from `artifact-timing-complete-55-source-bodies` to
`artifact-timing-supplied-source-bodies` — for the new model — while its behaviour was not changed.
Measured with one body supplied: the case runs and **fails**, `errors:
['ARTIFACT_AVAILABILITY_BODY_SET']`. The name was updated for partial supply; the check was not.

### A6 — revision recount by grep

**Confirmed, all three.** `validator_revision` is `3.2.11` at exactly **four** value-bearing sites:
`references/…validation-profile.json:45`, `scripts/run_gcfpe_20260914_fixtures.py:664`,
`scripts/validate_gcfpe_20260914.py:1063`, `scripts/validate_flowmaster.py:1221`.
`FLOWMASTER_VALIDATE_REVISION` is `3.2.13` at its single assignment, `SKILL.md:8`.
`CHANGE_FLOW_SPECIALIZATION_REVISION` is untouched at **3.2.8** at every asserting site, and the
installed `change-flow/SKILL.md:8` declares `3.2.8`. No `3.2.9`, `3.2.10` or `3.2.12` survives as a
live identity in any script or data file — correct, since 3.2.10/3.2.12 belong to the withdrawn
round-25 package a published verdict describes.

The candidate contract measures **610549 bytes / `1c3c7969b7b933569362a35acdff6f756e2ab8577054f5038e4a95ad3794e179`**
and `cmp` shows the two bundled copies **byte-identical**. The hash-pin chain does not move.

**§8e:** exactly the seven files `round26.patch` names differ from the installed skill; the patch
applies clean at `-p1` with no `.rej` or `.orig`, and the result is **byte-identical** to the
package (`diff -r` clean, digest `54604cf3…`).

## Findings

### Finding 1 — the all-55 requirement was not removed; it moved, and now fails the run (blocking)

*Artifact:* `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2421`, calling
`validate_artifact_timing_bodies(dict(texts))`; the check itself at
`flowmaster-validate/scripts/validate_gcfpe_artifact_timing.py:41`.

*Defect.* `validate_artifact_timing_bodies(bodies, *, require_complete=True)` emits
`ARTIFACT_AVAILABILITY_BODY_SET` whenever `set(bodies) != set(all 55 categories)`. The round-26 call
site does not pass `require_complete=False`. So the corpus dependency the round set out to delete
survives one function away, converted from "the gate will not run" into "the run fails."

*Evidence.* `IA-10`'s real text piped in returns `ok: false` with that single error (A4). Threshold
measured directly against the shipped function with placeholder keys: the error fires at 0, 1, 3 and
54 bodies and clears only at **55**. `require_complete=False` suppresses it and **is used nowhere in
the package** — the escape hatch is pre-existing, identical in the installed tree, and was not wired
up. The fixture suite carries the same defect at
`validate_gcfpe_artifact_timing.py:82`, where the renamed case `artifact-timing-supplied-source-bodies`
fails on any partial set.

*Why it matters.* This is the policy's named violation — *"suggestions that a complete local corpus
is needed before work can proceed"* — now enforced in code rather than merely suggested. It makes
the standing procedure in the Operations Hub unusable as written: *"A change to one prompt needs one
page… pipe the bodies in"* returns `ok: false` every time. It also inverts `C4`'s promise of "never
a spurious failure for pages that were not fetched" into exactly that.

*Smallest correction.* Pass `require_complete=False` at both body-driven call sites
(`validate_gcfpe_20260914.py:2421` and `validate_gcfpe_artifact_timing.py:82`), and append
`ARTIFACT_AVAILABILITY_BODY_SET` to `not_evaluated` when the supplied set is partial, so the run says
the completeness check did not run rather than failing or staying silent.

### Finding 2 — the coverage report is silent exactly when coverage is zero (blocking)

*Artifact:* `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2574`, `if bodies:`; the same
pattern at `validate_gcfpe_current.py:662` and `:670`.

*Defect.* `main()` deliberately distinguishes "no flag" (`bodies is None`) from "empty map"
(`bodies = {}`, line 2617). `if bodies:` discards that distinction, because `{}` is falsy — so
`validate_prompt_bodies` is never called and `prompt_body_checks_not_evaluated` stays `[]`.

*Evidence.* Both forms of validating nothing:

| invocation | result |
|---|---|
| no `--bodies-stdin` | `ok=True  validated=[]  not_evaluated=[]` |
| `echo '{}' \| … --bodies-stdin` | `ok=True  validated=[]  not_evaluated=[]` |

*Why it matters.* The honesty mechanism is the round's whole answer to "a partial run must not read
as a full pass," and the standing procedure tells operators to read these fields *instead of* `ok`.
In the zero-body case — the default, and what every existing automated caller produces, including
the flowmaster suite and CI — the fields assert that **nothing was skipped**, which is false: every
body-scoped check was. An operator doing exactly what the new procedure says is misled.

*Smallest correction.* `if bodies is not None:` makes the explicit `{}` honest immediately. For the
no-flag case, populate `not_evaluated` with every body-scoped check name.

### Finding 3 — SKILL.md still instructs the operator to build the corpus the policy forbids (blocking)

*Artifact:* `flowmaster-validate/SKILL.md`, lines 146, 154 and 162.

*Defect.* Two sentences and a command block survive unchanged from the installed tree (they were
lines 121/129/135 there; only their line numbers moved). They describe the suite as validating a
*"recursively scanned 55-member prompt corpus"*, call a *"required recursively scanned prompt
corpus"* the condition for *"a complete candidate pass"*, and give this as the operator's command:

    python3 scripts/validate_gcfpe_20260914.py /exact/change-flow-skill \
      --contract … \
      --candidate-root /exact/GCFPE-20260914.1-candidate-snapshot \
      --prompt-dir /exact/GCFPE-20260914.1-candidate-snapshot/prompts

*Evidence.* Run against the package, that documented command fails:
`validate_gcfpe_20260914.py: error: unrecognized arguments: --prompt-dir …`, exit 2. So it is both a
broken instruction and a live instruction to maintain a mirrored prompt tree at a fixed location —
in the round whose sole purpose is conformance to the policy prohibiting exactly that.

*Smallest correction.* Rewrite that block to the `--bodies-stdin` form and delete both phrases
describing a required scanned corpus. No code change.

### Finding 4 — the suite that issues the verdict never checks SKILL_TREE_SHA256 (blocking)

*Artifact:* `validate_self_identity` is called from one place only,
`flowmaster-validate/scripts/validate_gcfpe_20260914.py:2571`.

*Defect.* `C6` says the mechanism "makes the validator refuse to certify anything" on mismatch. Three
of the four gates do not consult it, including `validate_flowmaster.py`, which emits the top-level
`FLOWMASTER_SUITE_PASS` and is the instrument the rest of the suite is judged by.

*Evidence.* One comment appended to one unrelated script (`validate_epic_alpha.py`) in a scratch
copy:

| gate | result on the tampered tree |
|---|---|
| `validate_gcfpe_20260914.py` | **refuses** — `SKILL_SELF_IDENTITY:DECLARED_5bb632ce952b_MEASURED_9b6305b67407` |
| `validate_flowmaster.py` | **`FLOWMASTER_SUITE_PASS`**, 0 findings |
| `validate_gcfpe_current.py` | **`ok: true`**, 0 errors |
| contract fixtures | **`suite_ok: true`**, 155 cases, 0 failed |

*Why it matters.* The rule this mechanises is *"An install is not complete until its digest is
compared,"* written because a withdrawn package ran green for a full round. The gate an operator
would most naturally run after an install is the flowmaster suite, and it is the one that still
stays green on the wrong tree.

*Smallest correction.* Call the existing `validate_self_identity` from `validate_flowmaster.py` and
`validate_gcfpe_current.py`, surfacing a mismatch as a BLOCKER-class finding in the suite.

### Finding 5 — duplicate declaration lines are erased from the digest (non-blocking)

*Artifact:* `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2205` and `:2218`.

*Defect.* The exclusion substitutes every matching line; the declaration read uses the first. Adding
further `SKILL_TREE_SHA256: <64 hex>` lines changes `SKILL.md`'s visible content without changing
the digest, and is accepted with no error. Measured: 1 extra line and 20 extra lines both yield the
declared digest `5bb632ce952b` and no finding. The smuggled content is constrained to 64-hex-character
lines, so this is a confusion and integrity gap rather than an injection route — a reader sees two
contradictory hashes and the validator silently honours one.

*Smallest correction.* Require exactly one declaration: count the matches and return
`SKILL_SELF_IDENTITY:MULTIPLE_DECLARATIONS` for more than one, stripping only that single line.

### Nit — "the package is smaller than the tree it replaces" is false

`REPORT.md` states this in bold. Measured: the installed tree's files total **1,756,991 bytes** and
the package's **1,764,361** — **7,370 bytes larger**. The archive is likewise larger, 279,481 →
282,752. It is smaller than the *withdrawn round-25* package (284,004), which is not the tree it
replaces. The claim is report-only and not in the shipped bytes. Delete it or restate the referent;
nothing depends on it.

## The three open questions

### Q1 — `validate_epic_alpha.py` and `validate_strength_middleware.py`: repair, delete, or leave dormant?

**Not dormant. Remove the corpus path now; decide the scripts' fate separately.** Both are
unreachable from any GCFPE gate — each runs only through its own CLI with an explicit `--prompts
<dir>` — so neither is an active violation of ecosystem behaviour today. But the policy is explicit
that a conflicting *element* is defective, not merely a conflicting execution, and a dormant
directory-globbing prompt option is precisely how the retired practice returns: the next author who
needs a body-level check finds a working `--prompts` and uses it.

The cheapest conforming action is to delete the `--prompts` option and the `validate_snapshot` /
`validate_prompt_snapshot` functions from both scripts in the repair round. They are dead paths with
no GCFPE caller, so removal cannot regress a gate and needs no new design. The only thing worth
establishing first is whether either script has a live non-GCFPE owner who passes `--prompts`; if
one does, that owner converts to stdin on the same pattern. Absent a named owner, delete. Keeping
the scripts themselves is fine — it is the corpus door that should close.

### Q2 — what should the promotion packet cite as body-level evidence?

**Per-prompt provenance, not a corpus-wide count.** For each page actually read: the prompt id, the
Notion page id, the page's `page_last_edited_at`, the release and prompt version it was read under,
the validator revision, and the outcome. Then, explicitly, the set-scoped checks that were *not*
evaluated. That is reproducible without a mirror — anyone can reopen the page and see the same
last-edited timestamp — and it is a stronger claim than the old one, because it says which pages
were examined rather than asserting a number over pages nobody can re-derive.

`"0 errors across 55 bodies"` should not be revived in any form. It was never a continuous control;
it ran only when a session built a mirror, and the packet that cited it was citing that session's
copy, not the ecosystem. If a decision genuinely needs corpus-wide assurance, that is a dated,
scoped, Product Owner-authorised sweep that reads pages and reports per prompt — recorded as a
point-in-time review with its own date, never as a standing gate. Note that Finding 1 must be fixed
before any of this is possible: today a packet citing three validated prompts would have to cite a
run that returned `ok: false`.

### Q3 — should `SKILL_TREE_SHA256` be adopted by the other installed skills?

**Yes — declare it everywhere, verify it centrally. `flowmaster-validate` is the first case, not a
special one.** The hazard is structural and not specific to this skill: every skill installs under a
filename the packager is required to reuse, so any of them can be silently replaced by a superseded
build, and nothing today would notice.

What *is* specific to `flowmaster-validate` is that it is the only skill with a runtime that could
refuse. The others have no validator to host a self-check, and inventing one in each would be a lot
of machinery for a property that only matters at install time. So the right shape is the split:
every skill declares `SKILL_TREE_SHA256` in its `SKILL.md`, and `flowmaster-validate` — which
already walks every sibling `*/SKILL.md` in four separate places — measures each sibling tree and
compares it with that skill's declaration, failing the suite on any mismatch. One implementation,
every skill covered, and the check lands in the instrument whose job this already is.

Two caveats. Finding 4 must be fixed first, or the central verifier is the one gate that does not
run the check. And the digest recipe must be the skill-rooted one with the declaration line excluded
— the round-23 `F2` lesson: a digest that reaches sync-layer bookkeeping is a per-container value,
not an identity. This package gets that right.

## What I did not do

No skill installed. Nothing written to the synced skills directory — both installed digests
reproduce unchanged after every experiment. Nothing merged, no auto-merge. **No prompt corpus built
at any point**, temporary or otherwise: the one body I needed was read from Notion and piped to
stdin, and the round-25 corpora and cached body hashes were deleted before this review began. No
edit to `docs/pfcanon/**`. No prompt body changed in Notion. No QA verdict, acceptance, closure or
PF movement.

## What this needs

`SKILL_REPAIR_REQUIRED` on Findings 1–4; Finding 5 and the nit fold into the same pass. Findings 1,
2 and 4 are between one and three lines each and the mechanisms they need already exist in the code
(`require_complete=False`, `is not None`, `validate_self_identity`). Finding 3 is prose. None touches
`change-flow` or the hash-pin chain.

Per the rule this round applied to itself, the repaired bytes must not reuse the identities this
verdict describes: `validator_revision` **3.2.11 → 3.2.12** at its four sites and
`FLOWMASTER_VALIDATE_REVISION` **3.2.13 → 3.2.14**. `SKILL_TREE_SHA256` must be recomputed and
re-declared in the same change, and the declaration is excluded from its own digest, so it can be
stamped last.

The installed tree stays as it is meanwhile. It is two rounds behind and carries a published
confirmation; it does not conform to the policy, but neither does this package yet, and the gap is
now four small corrections wide.

**DECISION NEEDED** — whether to accept Findings 1–4 as blocking and authorise a round-27 repair;
and the `Q1` disposition of the two dormant `--prompts` scripts, which is a Product Owner call the
author correctly declined to make alone.
