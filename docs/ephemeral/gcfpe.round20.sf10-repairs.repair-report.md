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
| files changed | **7**, across two skills |
| validator revision | 3.2.6 → **3.2.7** |
| body-level fixture suite | **crashes on the installed build; 164 cases, 0 failed on the repaired build** |
| contract fixture suite | 140 cases, 0 failed — unchanged |
| end-to-end errors on the 55-body corpus | **12 → 10**, and the 10 are exactly `SF10-07`, which is the Product Owner's open decision |
| two-run identity | holds on both the end-to-end run and the fixture suite |

Nothing else moved: every other field of the end-to-end output, including the frozen-graph
digest and all 55 body digests, is identical between the installed and repaired builds.

## What changed

| file | installed sha256 | repaired sha256 |
|---|---|---|
| `change-flow/SKILL.md` | `e6bd29d59ca01522…` | `aff778a075b4cbd9…` |
| `flowmaster-validate/SKILL.md` | `f2729ba39de4f46b…` | `5b5898e6c54f5a64…` |
| `flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json` | `fac89991c5c4e5a1…` | `66999a2160b6bbab…` |
| `flowmaster-validate/scripts/validate_gcfpe_20260914.py` | `535a3b161ef09962…` | `5716f631915d9333…` |
| `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py` | `433d2a1611e5671a…` | `7523947d952b1372…` |
| `flowmaster-validate/scripts/validate_gcfpe_artifact_timing.py` | `b5716af7882223d5…` | `f68dae449829758c…` |
| `flowmaster-validate/scripts/validate_flowmaster.py` | `0e4c964c0dbf3701…` | `2fde743a31cc3a90…` |

The complete unified diff is at `gcfpe.round20.sf10-bench/repairs.patch`, 213 lines.

**The D8/D15 guard block is not touched.** It is the one part that must stay byte-identical
across both validator copies, and the `change-flow` copy of the validator is not changed at all.

### One thing that made this simpler than expected

The two `validate_gcfpe_20260914.py` copies are **not** the same file and do not need lockstep
here. The `change-flow` copy is 1057 lines and validates the contract only; the
`flowmaster-validate` copy is 2283 lines and adds the body-level layer. None of
`validate_qa_closure_bodies`, `validate_prompt_bodies`, `prompt_identity_header_valid` or
`notion_page_identity` exists in the `change-flow` copy, and it has no `--prompt-dir`. All three
approved repairs live in the body-level layer, so only the `flowmaster-validate` copy changes.

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

**The repair.** The token test is replaced by the routing obligation. For every non-terminal
public branch, each destination that is a prompt id must be named in the body; a prompt with no
named receiver owes no declaration. A new code, `PROMPT_HANDOFF_RECEIVER:<prompt>:<destination>`,
replaces `PROMPT_HANDOFF_CONTRACT:<prompt>` — a changed predicate gets a new identifier rather
than reusing one whose meaning was different. Symbolic destinations
(`NATHAN_TERMINAL_RETURN`, `ORIGINAL_NATIVE_STAGE`, `NATHAN_PROCEED`,
`NATHAN_MANUAL_MERGE_ASSERTION`) are not prompts and are not name-checkable. Malformed
`destinations` fails closed rather than being skipped.

**The new predicate is stronger, not weaker.** It verifies **166 specific receiver bindings**
across the 54 prompts that have a non-terminal public branch, where the old check verified the
presence of one string. A body that carried `NEXT_PROMPT_HANDOFF` while naming the wrong receiver
passed the old check and fails the new one.

**Measured: 54 of 54 prompts pass, including GCFPE-MGMT-10**, whose body names PR-10 with a
mention link at line 34.

**Bench:**

| case | result |
|---|---|
| installed build reports `PROMPT_HANDOFF_CONTRACT:GCFPE-MGMT-10` | reproduced |
| repaired build clears the corpus | clean |
| repaired build catches PR-30 dropping PR-35 | `PROMPT_HANDOFF_RECEIVER:PR-30:PR-35` |
| repaired build catches GCFPE-MGMT-10 dropping PR-10 | `PROMPT_HANDOFF_RECEIVER:GCFPE-MGMT-10:PR-10` |

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

**Regression.** The `change-flow` contract validator passes on the repaired tree, output
byte-identical to the installed tree, so the `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.5` pin —
asserted in three places — is still satisfied. The revision was **not** bumped: the disclaimer
adds no routing behaviour, it states which of several identically-identified files is already
current. If independent review judges a resolution rule to be behaviour, the bump is 3.2.5 → 3.2.6
in `change-flow/SKILL.md` plus three pin sites, and is trivially reversible either way.

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
heading whose title names inputs. Verified: the widened form selects the same section in every
case where the narrow form worked, and matches exactly once per body.

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
| `run_gcfpe_20260914_fixtures.py` (contract only) | exit 0 — 140 cases, 0 failed | exit 0 — 140 cases, 0 failed |
| `run_gcfpe_20260914_fixtures.py --prompt-dir` | **exit 1 — crash, suite cannot run** | **exit 0 — 164 cases, 0 failed** |
| `validate_flowmaster.py` | exit 0 | exit 0, identical but for the fixture-source path |
| end-to-end `--prompt-dir` | exit 1 — 12 errors | exit 1 — **10 errors**, all `PROMPT_WRITER` (`SF10-07`) |

Two-run identity holds: the end-to-end JSON is equal field for field across two runs, and the
fixture report is equal with absolute paths scrubbed.

**One pre-existing failure is recorded and not claimed as fixed:** `validate_gcfpe_current.py`
exits 1 with `"ok": false` on **both** builds, identically. It validates the 54-member selected
contract and is outside this package.

### A harness failure of my own, recorded

The first regression sweep printed `exit=0` for every command including ones that had clearly
errored, because `$?` captured a `tail | tr` pipeline rather than the command. That measurement
was void and is credited nowhere; the table above is the re-run with exit codes captured
directly. This is the third instance this session of a harness that reports success while
testing nothing, and the reason the bench keeps its three phases apart.

## The bench

`gcfpe.round20.sf10-bench/bench.py`, nine cases, exit 0. It keeps three phases apart, because
round 18 proved that sharing one `try` lets a setup failure be credited as a passing gate:

1. **apply** — build the fixture. Failure is `HARNESS FAILURE`, never a result; exit 1.
2. **import** — load the validator under test. Failure is `HARNESS FAILURE`; exit 1.
3. **evaluate** — run the check. Only this phase produces a verdict, and it fails closed.

Each case also refuses to run if applying its mutation leaves the input unchanged, so a placement
that silently matches nothing cannot be scored as caught.

## Packages

Built from the working copies and verified by extracting each and diffing recursively against the
source — both identical, with the file counts unchanged from the reviewed v11 packages:

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 241805 | `8e8f366af1f42a6f2ac8275f88c75452496c1c4bed77eb264cdc58ca77bb4fff` |
| `flowmaster-validate.skill` | 29 | 269957 | `9d874758cd35c62cc375546b4c7af596cdf8016b3bd8ccf81238a887f7de5f48` |

The validator asserts its own revision against the profile's, so **3.2.6 → 3.2.7 moves in five
places together**: `flowmaster-validate/SKILL.md`, the validation profile, `validate_gcfpe_20260914.py`,
`run_gcfpe_20260914_fixtures.py` and `validate_flowmaster.py`. All five are in this package;
missing one would turn the suite red.

## What this package does not claim

Not installed, and not to be installed by any agent. Not reviewed — that is the next step, and
the package exists in this form so an independent reviewer can read the diff without the
archives. No prompt body was edited. No contract bytes were edited. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` was not touched. `SF10-07` is untouched and remains the
Product Owner's open decision; the 10 errors it produces are the whole of what the repaired build
still reports.
