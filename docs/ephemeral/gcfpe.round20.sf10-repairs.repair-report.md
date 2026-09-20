---
artifact_type: GCFPE_SKILL_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-20
release: GCFPE-20260914.1 / 091426.1 / 55
author: PE34
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
authorised_by: 'Product Owner answers of 2026-09-20 — Q1 (SF10-03) "yes, prepare the fix", Q3 (SF10-05) "yes, disclaimer only", Q4 (SF10-06) "leave the body as-is and change the check"'
installed: false
installs_nothing: 'Only the Product Owner installs. The installed tree was never written to; every run used a scratch copy with PYTHONDONTWRITEBYTECODE=1 and produced zero .pyc files.'
snapshot: 'installed tree 321 files, digest excluding manifest.json c321be051b90c346a24d26524e132e7b90732953c3cc289e3def511e5fcfbaeb'
validator_revision: '3.2.6 -> 3.2.7'
new_finding: SF10-08
---

# SF10-03, SF10-05, SF10-06 — packaged, awaiting independent review

Three approved repairs, prepared as working copies with bench evidence and not installed.
Preparing them surfaced one new defect of the same class, recorded here as **`SF10-08`** and
fixed in the same package because leaving it would have kept the body-level fixture suite
unrunnable.

## Verdict

| | |
|---|---|
| status | `PACKAGED_AWAITING_INDEPENDENT_REVIEW` |
| files changed | **9**, across two skills — **4 substantive, 5 revision-only** (table below) |
| validator revision | 3.2.6 → **3.2.7** |
| body-level fixture suite | **crashes on the installed build; 164 cases, 0 failed on the repaired build** |
| contract fixture suite | 140 cases, 0 failed on both; the reports differ in one field, `validator_revision` |
| end-to-end errors on the 55-body corpus | **12 → 10**, and the 10 are exactly `SF10-07`, which is the Product Owner's open decision |
| two-run identity | holds on both the end-to-end run and the fixture suite |

Nothing else moved: every other field of the end-to-end output, including the frozen-graph
digest and all 55 body digests, is identical between the installed and repaired builds.

## What changed

Nine files differ from the installed tree, and the split is **four substantive, five
revision-only** — not the "seven and two" an earlier version of this line claimed. Review counted
the patch and was right; the corrected split, measured per file from the diff:

| file | added lines that are not a revision string |
|---|---|
| `flowmaster-validate/scripts/validate_gcfpe_20260914.py` | **125** — `SF10-03`, `SF10-06` |
| `flowmaster-validate/scripts/validate_gcfpe_artifact_timing.py` | **14** — `SF10-08` |
| `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py` | **7** — the `SF10-08` fixture anchor |
| `change-flow/SKILL.md` | **5** — the `SF10-05` disclaimer |
| `change-flow/scripts/validate_gcfpe_20260914.py` | 0 — revision pin only |
| `flowmaster-validate/SKILL.md` | 0 — revision declaration only |
| `flowmaster-validate/references/…-validation-profile.json` | 0 — revision pin only |
| `flowmaster-validate/scripts/validate_flowmaster.py` | 0 — revision pins only |
| `flowmaster-validate/scripts/validate_gcfpe_current.py` | 0 — revision pin only |

The distinction matters for review effort: **five of the nine files contain nothing an independent
reviewer needs to reason about behaviourally**, and treating them as repair implementations spreads
attention across nine files when four carry the whole change. Getting that wrong made the package
look larger and more diffuse than it is.

| file | installed sha256 | repaired sha256 |
|---|---|---|
| `change-flow/SKILL.md` | `e6bd29d59ca01522…` | `630f0c0bd575027d…` |
| `change-flow/scripts/validate_gcfpe_20260914.py` | `660d61fe619c9dd9…` | `8e7cbe435a6e9938…` |
| `flowmaster-validate/SKILL.md` | `f2729ba39de4f46b…` | `5b5898e6c54f5a64…` |
| `flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json` | `fac89991c5c4e5a1…` | `39c44ad84ca05d5e…` |
| `flowmaster-validate/scripts/validate_gcfpe_20260914.py` | `535a3b161ef09962…` | `b0456a27816c47de…` |
| `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py` | `433d2a1611e5671a…` | `7523947d952b1372…` |
| `flowmaster-validate/scripts/validate_gcfpe_artifact_timing.py` | `b5716af7882223d5…` | `8cff6c7ef685c0a0…` |
| `flowmaster-validate/scripts/validate_flowmaster.py` | `0e4c964c0dbf3701…` | `527bf522c0c602df…` |
| `flowmaster-validate/scripts/validate_gcfpe_current.py` | `00c8b2035263ed0f…` | `272d7b81fa091ce2…` |

The complete unified diff is at `gcfpe.round20.sf10-bench/repairs.patch`, 378 lines.

**The D8/D15 guard block is not touched.** It is the one part that must stay byte-identical
across both validator copies, and it still is: four functions, 7355 characters, md5
`46c69eaf8f00672e44f8502bbf43c721` in each copy.

### One thing that made this simpler than expected

The two `validate_gcfpe_20260914.py` copies are **not** the same file and do not need lockstep
here. The `change-flow` copy is 1057 lines and validates the contract only; the
`flowmaster-validate` copy is 2283 lines and adds the body-level layer. None of
`validate_qa_closure_bodies`, `validate_prompt_bodies`, `prompt_identity_header_valid` or
`notion_page_identity` exists in the `change-flow` copy, and it has no `--prompt-dir`. All three
approved repairs live in the body-level layer, so the `change-flow` copy of the validator carries
none of them — its only change is the one revision string described under `SF10-05`.

## `SF10-03` — the QA-120 class-map check

**The repair.** `validate_qa_closure_bodies` now reads the class map through a new helper,
`qa_pass_class_rows`, which accepts either rendering the body may legitimately use — a Markdown
pipe table or an HTML table — and compares each destination by **page identity** via the existing
`notion_page_identity`, not as literal text.

**Scope preserved as instructed.** The predicate is not relaxed: still exactly two rows, still
exactly the `EPIC → CL-E-10` and `CRD → CL-C-10` mapping, still the same two destination pages.
Only the rendering assumption and the literal URL comparison are removed.

**Bench, all cases as expected:**

| case | result |
|---|---|
| installed build reports a defect on the real body | `QA_PASS_BODY_CLASS_MAP` — reproduced |
| repaired build reads the real HTML body | clean |
| repaired build also reads the pipe rendering | clean |
| repaired build still rejects a wrong receiver (`CL-E-10` → `CL-E-40`) | fires |
| repaired build still rejects a wrong page id | fires |

The last two matter most: the fix must not become a check that cannot fail, which is the defect
it was written to remove.

## `SF10-06` — the handoff obligation

**The repair, in one sentence: the token test is *scoped to the registry's roster* and a routing
obligation is *added beside it*.** This summary previously said "the token test is replaced by the
routing obligation," which describes **the design review rejected** — the one under which a body
could lose its handoff block entirely and still pass. It was the summary of an earlier revision,
left standing when the correction was written into the section below it, and it is exactly the sort
of stale opening that could get the rejected design implemented. Corrected here; the two obligations
are set out immediately below.

For every non-terminal public branch, each destination that is a prompt id must be named in the
body; a prompt with no named receiver owes no declaration. A new code,
`PROMPT_HANDOFF_RECEIVER:<prompt>:<destination>`, replaces `PROMPT_HANDOFF_CONTRACT:<prompt>` — a
changed predicate gets a new identifier rather than reusing one whose meaning was different.
Symbolic destinations (`NATHAN_TERMINAL_RETURN`, `ORIGINAL_NATIVE_STAGE`, `NATHAN_PROCEED`,
`NATHAN_MANUAL_MERGE_ASSERTION`, `ACTUAL_OWNER_TERMINAL_RETURN` — all **five**, enumerated in
`SYMBOLIC_DESTINATIONS`) are not prompts and are not name-checkable; anything that is neither a
member prompt nor one of those five is malformed rather than skipped. Malformed
`destinations` fails closed rather than being skipped.

**Two obligations, not one.** An earlier revision of this repair replaced the
`NEXT_PROMPT_HANDOFF` literal test with the receiver test. That was wrong in the other direction:
the **approved registry requires that literal on 53 of its 55 rows** and exempts exactly two,
`GCFPE-MGMT-10` and `PR-50`, whose rows carry no such required literal. `GCFPE-MGMT-10`'s empty
`required_literals` justifies exempting **that row**, not retiring the requirement for the other 53 —
and as first packaged, a body could have lost its handoff block entirely and still passed. The repair
now carries both:

1. **`PROMPT_HANDOFF_LITERAL:<prompt>`** — the literal is required of every prompt except the two the
   registry exempts. The roster is the **registry's**, named in a module constant
   `HANDOFF_LITERAL_EXEMPT`, not derived from the graph's branch shape. Deriving it from the graph is
   what produced `SF10-06` in the first place: the graph shape demanded the token of
   `GCFPE-MGMT-10`, and the registry does not.
2. **`PROMPT_HANDOFF_RECEIVER:<prompt>:<destination>`** — the routing obligation below.

**Receiver ids match as complete identifiers.** A plain substring test lets `QA-100` satisfy a branch
routing to `QA-10`. That is the **one** prefix collision among the 55 member ids — measured, not
assumed — and one is enough: a body could drop every real `QA-10` reference, keep a `QA-100`, and
pass. `names_prompt()` rejects a leading or trailing identifier character rather than relying on
`\b`, which treats `-` as a boundary and would not help.

**What the receiver predicate does and does not prove.** It asserts that each of **166 declared
receivers**, across the 54 prompts with a non-terminal public branch, is **named somewhere in that
prompt's body**. That is strictly more than the old check, which asserted the presence of one
string regardless of where any branch routed: a body that carried `NEXT_PROMPT_HANDOFF` while
never naming its declared receiver at all passed the old check and fails this one.

**It does not bind the name to the operative handoff.** If a body names its declared receiver in a
route inventory, a phase description or a prohibition, and the mention nearest its routing tail
points elsewhere, this check passes. The bench asserts that blind spot as its own case rather than
leaving it to be discovered.

**The stronger check review asked for is not implementable against this input, and the reason is
categorical.** Review asked me to "parse or structurally delimit the actual handoff binding before
validating its receiver." **There is no handoff binding in a body to parse.** Measured across all 55:
the literal `NEXT_PROMPT_HANDOFF` occurs **68 times, every one of them in prose, and zero inside a
fenced block.** All 68 are sentences of the form *"Every actual nonterminal result ends with exactly
one fenced `text` block beginning `NEXT_PROMPT_HANDOFF`"* — 30 distinct wordings of that instruction.
The bodies are **prompts**: they instruct a runtime to *emit* a handoff block. The block exists in
the run, not in the artifact, and this validator only ever reads the artifact. Parsing the operative
binding would require an input this check does not have.

**And the 17-of-166 measurement was a symptom I mistook for the reason.** A routing-section-scoped
variant was built and failed **17 of the 166** on bodies that are correct — CL-20 declares CL-30
under `## Next step and recovery`, again under `## Candidate direct-destination bindings`, and again
under `## Direct native branch packages`; CL-C-10, CL-E-10, PR-10 and CL-40 do the same under
headings of their own. I recorded that count as the rejection's grounds. It is not. **A false-failure
count says my locator was wrong; it does not establish that the predicate is unreachable** — and
treating the two as the same thing is precisely the error `SF-05`'s own analysis distinguishes, a
selector confused with a locator. The measurement above is the actual reason, and it holds however
the locator is written. The false-failure count survives only as evidence that any heading list wide
enough would cover most of the document.

**A check that fails on correct bodies is worse than one with a stated limit**, so the whole-document
form is what is offered, with its limit recorded here and asserted in the bench.

Closing the remaining gap needs per-branch structure a prose body does not carry; it is named as a
follow-up, not smuggled in as covered.

**Measured: 54 of 54 prompts pass, including GCFPE-MGMT-10**, whose body names PR-10 with a
mention link at line 34.

**Bench:**

| case | result |
|---|---|
| installed build reports `PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10` | reproduced |
| repaired build clears the corpus, `GCFPE-MGMT-10` and `PR-50` included | clean — the exemption working, since both bodies lack the literal |
| repaired build catches PR-30 dropping PR-35 | `PROMPT_HANDOFF_RECEIVER:PR-30:PR-35` |
| repaired build catches GCFPE-MGMT-10 dropping PR-10 | `PROMPT_HANDOFF_RECEIVER:GCFPE-MGMT-10:PR-10` |
| repaired build catches a **dropped handoff literal** on PR-30 | `PROMPT_HANDOFF_LITERAL:PR-30` |
| repaired build catches a **prefix-collision receiver**, MGR-10's `QA-10` swapped for `QA-100` | `PROMPT_HANDOFF_RECEIVER:MGR-10:QA-10` |

The installed build is not contrasted on the literal case, because it also catches a dropped literal
on PR-30 — PR-30 has a non-terminal public branch, so the old graph-derived rule demanded the token
too. **The two builds differ only on `GCFPE-MGMT-10`**, which is the first case in the table. An
earlier version of this bench asserted a contrast that does not exist, and it is removed rather than
reworded.

### A correction to the round-10 artifact's classification

Round 10 recorded `SF10-06` as a **corpus** finding — a body gap — reasoning that 53 of 54 bodies
carry the token. That reasoned from the corpus instead of from the authority, and the authority
disagrees: the **approved registry** requires the `NEXT_PROMPT_HANDOFF` literal on **53 of 55**
rows and `GCFPE-MGMT-10`'s row carries `required_literals: []`. PR-50's row does not require it
either. So the registry, approved 2026-09-17, already says GCFPE-MGMT-10 owes no handoff token,
and the validator imposed one anyway.

`SF10-06` is therefore a **validator defect**, and the Product Owner's answer — leave the body,
change the check — is what the approved registry already said. The round-10 record is dated and
is not edited; this is its correction.

## `SF10-05` — the `change-flow` disclaimer

**The repair.** Two paragraphs added to `change-flow/SKILL.md`, immediately after the existing
disclaimer for the older correction reference files, in the same terms:

1. The three superseded direct-handoff contracts are immutable historical provenance, are not
   executed as current routing overlays, and confer no current skill binding. Where three files
   share `contract_id GCFPE-PF10-INTEGRITY-20260913.1`, that identifier resolves for current
   execution to `gcfpe-current-direct-handoff-contract.json` alone, which carries
   `status: SELECTED_PRODUCTION`. A `CANDIDATE_VALIDATED` or
   `CANDIDATE_UNTIL_SELECTED_IN_NOTION_REGISTER` copy is never the current answer.
2. The `support_skill: glow-hde-devops` field in those copies is a dated record of what the
   contract said when written, not a current binding; **D16** retires that skill; the current
   contract declares only `primary_skill: glow-hde-pr-development`; and **those dated bytes are
   not to be edited.**

**No contract bytes were changed**, as instructed. `AUTH-001` holds.

**The revision is bumped, 3.2.5 → 3.2.6.** The first version of this repair did not bump it,
reasoning that the disclaimer only states which of several identically-identified files is already
current. **Independent review judged otherwise, and it is right:** before the rule, a run had no
stated way to resolve the shared `contract_id`, so two runs could resolve it differently. That is
execution behaviour, and leaving the revision at 3.2.5 would let the old and new behaviours
advertise the same specialization identity — which is exactly what the revision exists to prevent.
The report had pre-committed to bumping if review judged it behaviour, so this is that.

**Seven sites move together.** This report first said three, then six; both were miscounts of the
same family as the `SF10-07` pricing, and the seventh was found by the suite rather than by reading:

| site | what it is |
|---|---|
| `change-flow/SKILL.md:8` | the declaration |
| `change-flow/scripts/validate_gcfpe_20260914.py:746` | `require(... "3.2.5" in skill ...)` |
| `flowmaster-validate/references/…-validation-profile.json` | `installed_skill_revisions.change-flow` |
| `flowmaster-validate/scripts/validate_gcfpe_current.py:633` | the count check |
| `flowmaster-validate/scripts/validate_gcfpe_current.py:634` | the error-message string |
| `flowmaster-validate/scripts/validate_flowmaster.py:148` | the `change-flow` anchor tuple |
| `flowmaster-validate/scripts/validate_flowmaster.py:688` | the `maintenance_metadata` mapping value |

**How the seventh was found, and the claim it corrects.** The six-site version of this table said
`validate_gcfpe_20260914.py:2284` "reads the revision from the installed `SKILL.md`, so it follows
automatically and is not a pin." That was wrong: it reads
`profile.get("installed_skill_revisions", {}).get("change-flow")` — from the **validation profile**.
So with the profile still at 3.2.5 the end-to-end run reported an eleventh error,
`CHANGE_FLOW_CONTRACT:CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.5`, and the suite caught in one run
what reading the code had got wrong. With the profile bumped, the run is back to exactly the 10
`PROMPT_WRITER` errors of `SF10-07`.

The two `CHANGE_FLOW_SPECIALIZATION_REVISION: 2.0.0` references — in the R1 oracle JSON and as the
`maintenance_metadata` key — are the **immutable R1 oracle's** historical value and are untouched.
Guard-block parity is unaffected: both installed validator copies still carry the identical four
functions, 7355 characters, md5 `46c69eaf8f00672e44f8502bbf43c721`.

**Correction to a claim made repeatedly in this report, the PR body and several review replies:**
the `change-flow` copy of the validator is **no longer unchanged**. Site 2 above is in it. What
remains true, and is the claim that mattered, is that **the D8/D15 guard block is untouched and
still byte-identical across both copies** — the change to the `change-flow` copy is one revision
string, nothing else.

## `SF10-08` — new: a check that could not fail on half its subjects

Found by running the bench, not by inspection, and fixed here because `SF10-03` cannot be proven
by the repository's own fixture suite while the suite crashes.

**The chain, in the order it appeared.** The body-level fixture suite (`--prompt-dir`) did not
run at all on the installed build: it raised `ValueError: Mutation anchor absent:
reject-source-epic-to-crd`. Two of its six body mutations anchor on the Markdown pipe rendering
of QA-120's class map — the same assumption as `SF10-03`. Repairing those two anchors moved the
crash to `ValueError: Native intake anchor missing: IA-10`, in the artifact-timing fixtures, whose
mutation helper located a prompt's intake section by one of two exact headings.

**Then the real defect.** `validate_gcfpe_artifact_timing._inputs()` selects the intake section by
matching one of four exact headings: `Inputs`, `Required inputs`, `Required input`,
`Sole substantive input`. The live corpus also uses `Entry and inputs`, `Entry modes and inputs`
and `Required and conditional inputs`. So for **5 of the 10 prompts** the input-based timing
checks apply to, `_inputs()` returned an empty string:

| prompt | its actual heading | locator saw |
|---|---|---|
| CF-C-20 | `## Entry and inputs` | nothing |
| CF-E-20 | `## Entry and inputs` | nothing |
| CF-PO-10 | `## Entry modes and inputs` | nothing |
| IA-10 | `## Entry modes and inputs` | nothing |
| IA-20 | `## Required and conditional inputs` | nothing |

`INITIAL_IA_OWN_APPROVAL_INPUT`, `FORMATION_FUTURE_PLAN_INPUT` and `QA_FUTURE_ARTIFACT_INPUT`
therefore **could not fail** for those five. Across all 55 bodies the locator is blind for 13.
The fixtures existed to catch exactly this and could not, because they crashed first.

**The repair.** Both locators — the fixture mutation helper and `_inputs()` — now match any
heading whose title names inputs, **singular or plural**: `## [^\n]*[Ii]nputs?\b`. Verified: the
widened form selects the same section in every case where the narrow form worked, and matches
exactly once per body.

**A first version of this repair left the two locators unaligned**, and review caught it. `_inputs()`
took `inputs?` while the fixture helper still required the plural, so the helper would raise
`Native intake anchor missing` on a body the production validator supports. That is live rather than
hypothetical: **OPS-20 is headed `## Sole substantive input` and PR-20 carries
`## Authoritative PF10 and overlay input`** — and `Required input` was in the original narrow list,
so the singular form is supported by design. The report had claimed both locators were aligned when
they were not. They are now, by the same regex.

**This is not the "widen the word list" mistake.** A forbidden-vocabulary list is a safety
predicate, and widening it buys one round because the next paraphrase walks through. These are
**locators** — they decide *where in a document to look*, not *what counts as a violation*. The
predicate is unchanged; it now runs on the text it was always meant to read.

**The repair surfaces no new body defect.** With the widened locator, the 55 clean bodies produce
**zero** timing errors. The corpus genuinely satisfies the rules; the checks were not looking at
five of them.

## Regression evidence

Everything below ran from a scratch copy of the whole tree, with
`PYTHONDONTWRITEBYTECODE=1 LC_ALL=C LANG=C TZ=UTC`, against the same 55-body corpus. Exit codes
are the commands' own, captured directly.

| run | installed build | repaired build |
|---|---|---|
| `change-flow/scripts/validate_gcfpe_20260914.py` | exit 0 | exit 0, output byte-identical |
| `run_gcfpe_20260914_fixtures.py` (contract only) | exit 0 — 140 cases, 0 failed | exit 0 — 140 cases, 0 failed; report differs only in `validator_revision` |
| `run_gcfpe_20260914_fixtures.py --prompt-dir` | **exit 1 — crash, suite cannot run** | **exit 0 — 164 cases, 0 failed** |
| `validate_flowmaster.py` | exit 0 | exit 0; the whole 1600-line report differs in exactly two lines, the fixture-source path and `validator_revision` |
| end-to-end `--prompt-dir` | exit 1 — 12 errors | exit 1 — **10 errors**, all `PROMPT_WRITER` (`SF10-07`) |

Two-run identity holds: the end-to-end JSON is equal field for field across two runs, and the
fixture report is equal with absolute paths scrubbed.

**One pre-existing failure is recorded and not claimed as fixed:** `validate_gcfpe_current.py`
exits 1 on **both** builds with the identical single error `CONTRACT_MISSING`. It validates the
54-member selected contract and is outside this package.

That line was briefly at risk of being wrong in the other direction. After the revision bump a run
appeared to show it exiting 0 on the repaired build, which would have meant the bump fixed it. It did
not: the `exit=0` was a harness artefact — `$?` read after a command substitution in the same
statement, so it captured the substitution rather than the validator. Re-run with the exit code taken
directly, both builds fail identically. **This is the second instance this session of the same
exit-capture bug**, the first being a `tail | tr` pipeline, and the second appeared inside the loop
written to avoid the first.

### `_` joins the boundary class, and the hazard is real rather than hypothetical

Review asked whether `_` belongs in `names_prompt`'s boundary class. It does. The old class was
`[0-9A-Za-z-]`, so `QA-10_RECEIVER` satisfied a branch routing to `QA-10` — the `QA-100` failure
again, one character over.

**Measured, because "could happen" is not evidence.** The corpus contains **54 underscore-adjacent
prompt-id occurrences**, and they are not contrived: `PR_RETURN_PHASE` values are written
`PR-30_PREPUBLICATION` and `PR-30_POSTPUBLICATION` across eight bodies, and OPS-20 and OPS-30 write
`NOT_PRODUCED_BY_OPS-20` / `-30`. Those are enum values, not routing mentions. A body whose last
plain `PR-30` was edited away while its enum tokens stayed would have passed.

**And it flips nothing today.** Of the **166 declared receiver checks**, adding `_` to the class
changes **zero** verdicts in either direction — the end-to-end output is byte-identical to the run
before the change. So this closes a reachable hole at no behavioural cost, which is the only kind of
safety change that needs no argument.

The new bench case buries **ESC-40**'s five complete `PR-30` mentions inside the real enum token.
ESC-40 is the subject because it is real on both halves: it declares `PR-30` as a receiver *and*
already carries six `PR-30_` tokens, so after the mutation it is a body that discusses
`PR-30_PREPUBLICATION` constantly and never names `PR-30`. **My first version of this case used
CL-E-20, which does not declare `PR-30` at all** — the fixture would have asserted an error the
validator had no reason to emit. Caught by checking the declared-receiver set before running, not
after.

No second `FLOWMASTER_VALIDATE_REVISION` bump: the package is unreleased and 3.2.6 → 3.2.7 already
distinguishes it from every installed build, so one bump covers the round.

### Two failures of my own this round, both caught by counting rather than by reading

**I shipped bytecode into a package.** The measurement scripts that imported the validator to count
receiver checks ran **without `PYTHONDONTWRITEBYTECODE=1`**, and Python wrote
`flowmaster-validate/scripts/__pycache__/*.pyc` into the working copy. The rebuild packaged them:
`flowmaster-validate.skill` came out at **31 files and 342177 bytes** instead of 29 and ~271k. The
file count is what exposed it. Cleaned, rebuilt, and re-verified at 29 files with exactly nine files
differing from base and no binary entries in the patch. **The installed tree was never involved** —
the contamination was in the scratch copy — but the rule that was broken is the one that exists to
prevent exactly this, and it was broken in the scripts I wrote to check someone else's finding.

**I nearly reported the frozen tree as altered.** Measuring the freeze from `/root/.claude/skills`
gave **323 files** and a digest of `4779ca6a…` against the recorded `c321be05…`. The tree is fine:
the freeze is rooted at `synced/<bucket-id>/`, and my path included `session-start-hook/SKILL.md`
and a `.bucket-…` marker that live outside it. Measured at the correct root: **321 files, digest
`c321be051b90c346a24d26524e132e7b90732953c3cc289e3def511e5fcfbaeb`, 0 `.pyc`** — and the only file
with an mtime after the v11 install is `manifest.json`, which the freeze excludes by construction.
**A wrong root is not a changed tree**, and the same discipline that stops a failed grep becoming a
file defect applies to a digest.

For the record, since I had to rediscover them: the D8/D15 guard block is `_addendum_paths`,
`_ambiguous_addendum_keys`, `pf10_addendum_contract_key_drift` and `addendum_list_value_drift`.
Verified identical in **all four copies** — both skills, both builds — at 7355 characters and md5
`46c69eaf8f00672e44f8502bbf43c721`. My first parity script guessed four other function names, found
none of them, and produced md5 `d41d8cd9…` — the hash of the empty string. That is a harness
returning a confident answer about nothing, and it is not credited anywhere.

### Malformed route data now fails closed, and one of its two shapes was a crash

Review found that the `destinations` guard validated only the **container**, never the elements, so
the `MALFORMED_DESTINATIONS` code did not cover what it appeared to. Measured, and it is worse than
the finding said:

| `destinations` | before | after |
|---|---|---|
| a non-string scalar element, e.g. `7` | absent from `EXPECTED_MEMBERS`, **silently skipped** | `MALFORMED_DESTINATIONS` |
| an unhashable **dict** element | `TypeError: unhashable type: 'dict'` — **aborts body validation** | `MALFORMED_DESTINATIONS` |
| an unhashable **list** element | `TypeError: unhashable type: 'list'` — **aborts body validation** | `MALFORMED_DESTINATIONS` |
| **`null`** | accepted; the loop iterates nothing | `MALFORMED_DESTINATIONS` |
| **key absent** | accepted; the loop iterates nothing | `MALFORMED_DESTINATIONS` |
| an **empty list** | not flagged | **still not flagged** — deliberately, see below |

The finding named the dict; **a list is unhashable too**, so there were two crash shapes rather than
one. And a crash here is the same failure the installed build already has in its fixture suite:
**an abort instead of a verdict**, which is strictly worse than a reported defect because it takes
the whole validation down with it. Every element is now checked for `str` before any membership test.

This was the only site at risk. I grepped the other set-membership tests in the changed file — they
take `prompt_id` or `path.stem`, which are filenames and always strings — and `qa_pass_class_rows`
operates on regex groups, which are strings by construction. One site, and it was mine.

**The bench's own landed-mutation guard was half-built, and these cases exposed it.** The guard
hashed `data["bodies"]` only. The first contract-mutating case legitimately leaves the bodies
untouched, so the guard reported `mutation changed nothing` for a mutation that had landed — and,
read the other way, it **would have scored a contract-mutating case that changed nothing at all.**
No case had exercised that path before, which is exactly how a half-built guard survives being
written. It now hashes the whole input, bodies and contract together.

### Null and absent `destinations` too — and a matching defect in code this package does not touch

A second review round on the same guard found that `destinations is not None and not isinstance(...)`
let **null** and an **absent key** through, after which the loop iterated nothing. On a *non-terminal*
public row that is silence where a verdict belongs: such a row's whole meaning is that the invocation
continues somewhere, so declaring no route at all is malformed.

**Measured before changing it**, because requiring a list unconditionally could have produced false
failures: **all 208 non-terminal public rows in the real contract carry a non-empty list.** Zero
affected. The guard now requires a list unconditionally.

**Two reasons this was the right scope, and one thing deliberately left alone.** The contract-level
`STATE_DESTINATION` check in this same file **already** requires a list here — so the lax body-level
guard was not merely incomplete, it **disagreed with the stricter check beside it**, and they now
agree. For the same reason an **empty list is deliberately still not flagged**: `STATE_DESTINATION`
does not flag it either, and this check should not become quietly stricter than the rule it mirrors.
If an empty `destinations` on a non-terminal row ought to be an error, that belongs to both checks at
once and is a decision, not a fix.

**And a defect in unchanged code, named rather than fixed.** Checking the contract-level rule to
compare predicates, I found it carries **the same unhashable-element crash** I had just repaired at
body level: `destination not in allowed_nodes` at `validate_gcfpe_20260914.py:1719` raises
`TypeError: unhashable type` for a dict or list element, so a malformed contract aborts contract
validation instead of reporting `STATE_DESTINATION`. Verified by executing the predicate on all four
shapes. **This is outside the three authorized repairs and I have not touched it** — widening the
package is not mine to decide. It is recorded here as a finding for the Product Owner, and it is the
strongest independent evidence that the body-level fix was worth making: the same mistake existed
twice in the same file, and only one instance was in code this package is allowed to change.

### One habit behind three findings: a correction that stops at the paragraph

Three of this round's findings share a single shape, and calling them three accidents would be the
wrong record:

| the corrected premise | where the correction landed | where the old conclusion survived |
|---|---|---|
| the PF10-comparison stop is not proven absent from the bodies | §3's opening | **§3.6**, two paragraphs after the admission that contradicts it |
| `artifact_type` already distinguishes the two regimes | §2.3's analysis | **§2.3's own closing**, "the next person pays for it" |
| the literal test is kept, not replaced | `SF10-06`'s body | **`SF10-06`'s opening summary**, describing the rejected design |

In each case the corrected reasoning went into the body and **the summary above it kept the old
conclusion** — and the summary is the part a reader trusts first. The third was the worst: an opening
that stated the design review had rejected, in a document written to guide a decision.

**The rule adopted, not just the three fixes: when a finding corrects a premise, the correction is
not finished until every summary, opening and recommendation resting on that premise has been
re-read. The document, not the paragraph.** That pass has now been run over both files for all three
premises; the only surviving occurrences of the old wording are inside the corrections that quote it.

### The run is landed, because the repository's own rule said it had to be

Review pointed out that in a clean checkout none of the bench's three inputs exist and no run output
is committed, so the PASS counts in this report could not be independently verified — and it cited
the repository's own standard against me. The registry's `corroboration_not_reproducible_here` key
says a review whose "report, inputs or command is checked in" is absent "cannot be reproduced and it
is recorded here as corroboration, never as evidence," and that it "is promoted to evidence only by
landing the run." My counts were in precisely that position: asserted numbers with no landed run, in
a report that elsewhere insists on the distinction.

`gcfpe.round20.sf10-bench/run-record.md` now lands it, **generated programmatically from the
artefacts** so nothing in it was transcribed: the commands verbatim, every input's identity (the
frozen tree's file count and digest, all 55 body SHA-256s and byte counts, the nine changed files'
before/after digests, the package digests), and the outputs themselves — both end-to-end error lists
in full, both fixture-suite results including the installed build's crash line, the guard-block
parity table, and the bench's complete stdout.

**What it does not do, stated rather than glossed.** It does not make the runs reproducible in a
clean checkout, because the inputs cannot be landed: the 55 bodies are authored in Notion in place and
never mirrored here, and the two skill trees live in a one-way synced directory that is not a git
checkout and that only the Product Owner installs into. Neither is mine to commit. So a clean checkout
gets the commands and the input identities but not the inputs; anyone holding the inputs can confirm
they are the same ones by digest. That is the strongest form available here and it is weaker than a
self-contained harness — which is exactly the distinction the registry key draws, and the report
should not be read as claiming the stronger one.

**Two escaping artefacts in the generated file, found and fixed before committing.** The command
block came out with a typo'd path (`prompt_ecosystema_management`) and **doubled backslashes**, so the
shell continuations would not have run. Same species as the mangled regex in an earlier review reply:
the claim was right and the record was not. Generating a file does not exempt it from being read.

### An unknown destination was indistinguishable from a symbol

Review found that a value which is neither a member prompt nor a declared symbol — `PR-300`, say —
passed the new type guard and was then **silently skipped**, exactly as `NATHAN_PROCEED` is, so the
receiver that row meant to name went unchecked. Correct, and the fix is an explicit roster rather
than an absence test.

**The roster, counted from the contract rather than recalled.** 208 destinations sit on non-terminal
public rows: **166 member prompts and 42 symbolic**, the symbolic being `ORIGINAL_NATIVE_STAGE` (39),
`NATHAN_MANUAL_MERGE_ASSERTION` (2) and `NATHAN_PROCEED` (1). Across all rows there are **five**
symbols, adding `NATHAN_TERMINAL_RETURN` (54) and `ACTUAL_OWNER_TERMINAL_RETURN` (18).
`SYMBOLIC_DESTINATIONS` names all five; anything that is neither a member nor one of them is now
`MALFORMED_DESTINATIONS`.

**My own comment's roster was wrong twice**, which is the fifth accounting error of this family: it
listed **four** symbols, **omitted `ACTUAL_OWNER_TERMINAL_RETURN` entirely**, and included
`NATHAN_TERMINAL_RETURN`, which never appears on the rows this guard actually inspects. Corrected
from the measurement, with the counts in the constant's docstring so the next reader does not have to
re-derive them.

### The bench no longer depends on how it was invoked

Review pointed out that the bench's usage block shows no `PYTHONDONTWRITEBYTECODE=1`, and `load()`
calls `exec_module` on a validator **inside each supplied tree** — so a reviewer following the usage
block exactly would write `__pycache__/*.pyc` into both trees, mutating inputs this bench calls
frozen. That is not hypothetical: it is precisely the failure recorded two sections above, which put
two `.pyc` files into a `.skill` archive, **and it happened for exactly this reason** — a script
relying on an environment variable its own documentation never showed.

`bench.py` now sets `sys.dont_write_bytecode = True` itself, before any import. **Verified by running
it with no environment variable at all**, exactly as the usage block prints: nineteen cases, exit 0,
and **zero `.pyc` or `__pycache__` in either tree afterwards**. A harness must not depend on how it
was invoked to leave its inputs untouched — and the fix belongs in the harness, not in a note telling
the caller to remember.

### Three stale records, one cause, and a guard instead of a resolution

All three findings this round were stale figures my own corrections had not propagated: the run
record still named the **previous validator digest**, the **previous package size** and an
**18-case bench run**; the report's opening **Verdict** still carried the seven-and-two split its own
corrected table replaced; and the `SF10-06` description still listed **four** symbolic destinations
after the correction below established that omitting the fifth was the defect.

**The run record one was the worst of the three.** That file exists so a reviewer can verify the
reviewed package. Naming last round's digests does not merely mislead — it **sends them to verify
bytes that are not under review**, which is worse than having no record at all.

**Two rounds ago I adopted a rule for exactly this** — re-read every summary, opening and
recommendation resting on a corrected premise — and then broke it three times in one round. A rule I
cannot keep is not a control, so the check is now mechanical.

`gcfpe.round20.sf10-bench/make_run_record.py --check` recomputes every identity from the artefacts —
the nine file digests, both package digests, file counts and byte counts, the patch's line count, the
bench's case count and its stdout verbatim — and requires each to appear in the records, naming
expected and actual on any drift.

**Fired with three injected regressions, because an unfired guard proves nothing** — D14's rule
applied to my own instrument:

| injected | result |
|---|---|
| revert the run record's validator digest to the previous value | **caught**, exit 1 |
| revert the report's bench case count to "eighteen" | **not caught at first — see below** |
| revert the package byte count to the previous value | **caught**, exit 1 |

**The second control found a hole in the guard.** The case-count check was
`if spelled not in rp and str(n) not in rp`, and `"19"` occurs inside unrelated numbers in the
report, so the bare-digit branch passed a reverted count. **That is the too-weak-selector mistake
this whole package is about, committed inside the guard written to prevent it** — and it was found by
firing the regression, not by reading the code. The check now requires the exact phrase
`"<spelled> cases, exit 0"` **and** rejects any other spelled count in that role. All three controls
now fire, and the guard passes on the real records.

### The guard reproduced the defect it was built to prevent, twice

The record checker landed last round had two defects of its own, both found by review, and the first
is the one worth keeping on the record.

**`--check` computed the corpus identities and never read them.** `identities()` built
`ids["bodies"]` — 55 prompt ids with digests and byte counts — and `check()` never touched it. So the
command could print **"records agree with the artefacts"** against a stale, substituted or **entirely
nonexistent** corpus. **That is the bench's own original defect** — a corpus accepted by count while
the docstring promised a digest check — **reproduced inside the guard written to stop stale records.**
The same mistake, one abstraction level up, three rounds later.

It now verifies the roster and every digest and size, and it is **fired by four injected
regressions** rather than trusted:

| injected | result |
|---|---|
| one body's bytes substituted | **caught** — names `QA-10` |
| one body removed (54 supplied) | **caught** — count *and* the now-unmatched row |
| a body the record does not list | **caught** — both directions |
| an empty corpus directory | **caught** — 57 problems |

**And `--write` did not write.** It printed an identity JSON document and left both records untouched,
while the docstring offered `(--write | --check)` and this report claimed regeneration was
programmatic. I had regenerated the run record with an ad-hoc script and then landed a `--write` that
could not repeat it — **a command documented by what I meant it to do rather than by what it did.**
It now regenerates the changed-files table, the package table, the 55-body table and the bench block
in place, and is **idempotent on the current artefacts**, which is how I know the committed record
already matched them.

**Nothing in the two skills changed this round**, so the patch is unchanged at 378 lines and both
package digests are unchanged. The defects were in the repository-side instrument, not the package.

### The whole table above was re-run against the packaged copies

After the revision bump, and after the two `.skill` archives were rebuilt and verified to extract
byte-identically to the working copies, every row of the table was re-run from scratch against
those same copies. All of it reproduced: 12 → 10 with the 10 exactly `SF10-07`; the body suite
crashing on the installed build with `ValueError: Mutation anchor absent: reject-source-epic-to-crd`
and clean at 164/0 on the repaired one; 140/0 on both contract suites; `validate_flowmaster.py`
exit 0 on both; the `change-flow` contract validator exit 0 with byte-identical stdout on both; and
the bench at nineteen cases, exit 0, with the corpus gate confirming all 55 registry digests. The
end-to-end outputs are 6179 and 6104 bytes, the same sizes as the first sweep.

**Two of my own invocation errors during that re-run, recorded so they are not read as results.**
First, the bench was launched without `--registry` from a directory where its default relative path
does not resolve; it exited 1 with `HARNESS FAILURE: no registry`, which is the corpus gate working
and not a bench failure. Second, the end-to-end validator was handed the **candidate-graph**
contract instead of the **direct-handoff** contract and died with
`TypeError: 'NoneType' object is not iterable` inside `validate_contract`. Both builds died
identically, so nothing was even comparable, let alone creditable. Neither measurement is credited;
the numbers above are the runs with the correct inputs, and the output sizes matching the first
sweep are the check that they are.

### A harness failure of my own, recorded

The first regression sweep printed `exit=0` for every command including ones that had clearly
errored, because `$?` captured a `tail | tr` pipeline rather than the command. That measurement
was void and is credited nowhere; the table above is the re-run with exit codes captured
directly. This is the third instance this session of a harness that reports success while
testing nothing, and the reason the bench keeps its three phases apart.

## The bench

`gcfpe.round20.sf10-bench/bench.py`, **nineteen cases, exit 0**. It keeps three phases apart, because
round 18 proved that sharing one `try` lets a setup failure be credited as a passing gate:

1. **apply** — build the fixture. Failure is `HARNESS FAILURE`, never a result; exit 1.
2. **import** — load the validator under test. Failure is `HARNESS FAILURE`; exit 1.
3. **evaluate** — run the check. Only this phase produces a verdict, and it fails closed.

Each case also refuses to run if applying its mutation leaves the input unchanged, so a placement
that silently matches nothing cannot be scored as caught.

**Every case calls the validator's own functions.** The `SF10-03` cases call
`validate_qa_closure_bodies`; the `SF10-06` cases write the mutated corpus to a temporary
directory and call `validate_prompt_bodies`, which is the function the validator uses in
production. An earlier revision of this bench reimplemented the `SF10-06` branch and chose between
implementations by testing for an unrelated symbol, so its cases would have passed even if the
real branch were absent, unreachable or written differently — a bench that tested its author's
copy of the logic rather than the repair. That is the third instance this session of an instrument
that could report success while measuring nothing, and it is why the tenth case exists.

**The tenth case asserts a failure.** It retargets PR-30's last mention of PR-35 to PR-40, leaving
the earlier mentions in place, and asserts that the check does **not** fire. It also refuses to
run if the mutation removes the name entirely, because then the whole-document predicate would
catch it and the blind spot would not be modelled — which is exactly the mistake the first version
of that fixture made.

### The corpus gate

The bench refuses to run on a corpus it cannot verify. Before any case, it parses the 55
`prompt_key` → `evidence_contract` SHA-256 pairs out of
`docs/prompt_ecosystem_management/project-prompt-contract-registry.md` — repository-resident, and
parsed with a regex so the bench carries no dependency beyond the standard library — and requires
the supplied directory to be exactly those 55 prompts with exactly those digests.

An earlier revision accepted any 55 Markdown files **by count alone**, while its own docstring
promised the registry verification. A stale or substituted corpus could have produced exit 0 and
been credited as evidence for the current corpus. Two controls now prove the gate bites: appending
one line to `PR-30.md` gives `HARNESS FAILURE: 1 body/bodies do not match their registry
evidence_contract digest: ['PR-30']`, and a directory holding one body is rejected with the 54
missing prompt ids named. Both exit 1 before a single case runs.

### Why the fixture trees are not committed

The bench takes `--base`, `--work` and `--bodies` and fails with the path it wanted if any is
missing. It cannot reconstruct them, and committing them would be wrong rather than merely
inconvenient:

- `--base` and `--work` are copies of the **installed skills tree**, which lives in a one-way
  synced directory outside this repository and is installed only by the Product Owner. Vendoring
  it would create a second, drifting copy of the thing under test.
- `--bodies` is the **55-prompt corpus**. Prompt bodies are authored in Notion in place and are
  never mirrored into this repository; the corpus is fetched per run and is verified against the
  registry's recorded `evidence_contract` digests by the gate above — so the corpus is not committed
  but it is also not taken on trust.

So the committed script is the reproducible part and the inputs are named, not assumed. A reader
who wants the evidence without the inputs has `repairs.patch`, which is the whole change.

## Packages

Built from the working copies and verified by extracting each and diffing recursively against the
source — both identical, with the file counts unchanged from the reviewed v11 packages:

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 241846 | `cb1239324f080df7c5a8f1f17624542688b1994fc05d04f05cbe45b76367968e` |
| `flowmaster-validate.skill` | 29 | 272630 | `94e3e63f8eaad6285c9116fd5d803714955f1d4bd4ee795c7166b00cd6221757` |

The validator asserts its own revision against the profile's, so **`FLOWMASTER_VALIDATE_REVISION`
3.2.6 → 3.2.7 moves in five places together**: `flowmaster-validate/SKILL.md`, the validation
profile, `validate_gcfpe_20260914.py`, `run_gcfpe_20260914_fixtures.py` and
`validate_flowmaster.py`. All five are inside `flowmaster-validate.skill`.

**The two packages must be installed together, or the suite goes red.** The seven
`CHANGE_FLOW_SPECIALIZATION_REVISION` 3.2.5 → 3.2.6 sites listed under `SF10-05` **span both
packages**: two are in `change-flow` (its `SKILL.md` and its validator copy) and five are in
`flowmaster-validate` (the validation profile, `validate_gcfpe_current.py` twice,
`validate_flowmaster.py` twice). Installing either package alone leaves a 3.2.5 assertion pointed
at a 3.2.6 declaration, or the reverse. This is a property of the bump, not of the repairs, and it
is the reason the seventh site was worth chasing.

## What this package does not claim

Not installed, and not to be installed by any agent. Not reviewed — that is the next step, and
the package exists in this form so an independent reviewer can read the diff without the
archives. No prompt body was edited. No contract bytes were edited. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` was not touched. `SF10-07` is untouched and remains the
Product Owner's open decision; the 10 errors it produces are the whole of what the repaired build
still reports.
