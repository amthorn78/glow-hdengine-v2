---
artifact_type: PROMPT_ECOSYSTEM_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INDEPENDENT_REVIEW
authority: Product Owner approval 2026-09-21, under the Prompt Corpus Storage and Fidelity Policy
subject: The prompt-corpus mirror is removed; bodies arrive from Notion, one page at a time
---

# Round 26 — validation without a corpus mirror

**`--prompt-dir` is gone.** Prompt bodies now arrive as `{prompt_id: text}` on **stdin**, supplied by
whoever read the pages from Notion, and the validator checks whatever it was given. There is
deliberately no path option: a file persists, and a persisted corpus is what the policy forbids.

One hash is added, and it is of **this skill**, never of a prompt.

## Why, and what it cost to learn

The Product Owner's **Prompt Corpus Storage and Fidelity Policy** of 2026-09-21 forbids
transcribing, exporting, mirroring, caching or hashing the prompt corpus to disk. `--prompt-dir`
required a complete local corpus of 55 files before any body-level gate would run. That is the
mirror, and the policy names requiring one as a violation in itself.

The machinery had already demonstrated the problem twice before the policy existed. The independent
reviewer declined the 55-body gate in round 24 — *"that run would have produced a number, not
evidence"* — and declined it again in round 25, *"rebuilding one means hand-transcribing 1.06 MB
where a slip is indistinguishable from drift."*

## The measurement that made this cheap

`validate_prompt_bodies` was **already per-prompt**. Every cross-prompt dependency was enumerated
before any code was written:

| | |
|---|---|
| the `rglob("*.md")` walk | the mirror itself |
| **`if set(paths) != EXPECTED_MEMBERS`** | **the single line demanding all 55** |
| `destination in EXPECTED_MEMBERS` | a *name* lookup against the roster; needs no body |
| `validate_qa_closure_bodies` | needs exactly three named bodies |

One line and one walk were the entire corpus dependency in that function. The dependency was wider
across the skill than the proposal estimated — **seven files, not one** — but every instance was the
same mechanical shape.

## Four checks were deleted with the mirror they policed

None described the ecosystem. Each described the copy.

| deleted | what it asked |
|---|---|
| `PROMPT_BODY_MEMBER_SET` | were all 55 files present? Membership belongs to the registry and the graph, which carry it already and need no bodies |
| `PROMPT_BODY_DUPLICATE` | two files for one id — impossible from dict keys |
| `PROMPT_BODY_FILENAME_ID` | does the filename match the id? There are no filenames |
| `PROMPT_BODY_UTF8` | does the file decode? Text arrives decoded |
| `CANDIDATE_PROMPT_ROOT_MISMATCH` | is the corpus at `<candidate-root>/prompts`? It institutionalised the parallel storage location the policy forbids |

**Body hashes are gone entirely**, and `prompt_body_sha256` with them.

## One check gained value

`PROMPT_BODY_MISSING_ID` becomes **`PROMPT_BODY_ID_MISMATCH`**: it compares the body's own
`Prompt ID:` header against the key it was supplied under. That catches the one error this interface
makes *likelier* than a directory did — reading or pasting the wrong page — and it names the page
you actually have. Measured: supplying `IA-30`'s text under the key `IA-10` returns
`PROMPT_BODY_ID_MISMATCH:IA-10:IA-30`.

## Coverage is reported, not required

The result now carries `prompt_bodies_validated` as a **list of ids** and
`prompt_body_checks_not_evaluated` naming the set-scoped checks that could not run. A caller who
supplies three bodies gets three validated and an explicit `QA_PASS_CLASS_MAP_AND_INTAKES` under
not-evaluated — never a false pass, never a spurious failure for pages that were not fetched.

A set-scoped check that stayed silent would read as a pass. That is the failure this interface
exists to prevent.

## The one hash — `SKILL_TREE_SHA256`

`SKILL.md` declares it; the validator digests its own tree at runtime and **refuses to certify
anything on mismatch**. The declaration line is excluded from the digest, or declaring the value
would change it.

It exists because nothing else catches the wrong package being installed. On 2026-09-21 a withdrawn
package was installed in place of its successor, under the identical filename the packager is
required to use, and the hash-pin chain, the fixture suites and the independent §10 review all
stayed green for a full round. This is `SFR-01`'s `Q3`, answered.

**A skill's own bytes are not the prompt corpus**, so the policy does not reach this.

| | |
|---|---|
| declared | `5bb632ce952b11649e5e868904a5fe7f4d594d5ec1083fa1c000c58cf1cd2fb6` |
| stable across re-measurement | yes |
| clean tree | no error |
| one comment appended to one unrelated script | `SKILL_SELF_IDENTITY:DECLARED_5bb632ce952b_MEASURED_1935f9180ac2` |
| **verified from the extracted package** | **no error** |

## Measured

Every run from a scratch copy, `PYTHONDONTWRITEBYTECODE=1`. Base is the installed tree.

| gate | base (installed) | work | from the extracted package |
|---|---|---|---|
| candidate validator | exit 0 | exit 0 | exit 0, `ok: true` |
| contract fixtures | 155 cases, 0 failed | 155, 0 failed | 155, 0 failed |
| flowmaster suite | `FLOWMASTER_SUITE_PASS` | `FLOWMASTER_SUITE_PASS` | `FLOWMASTER_SUITE_PASS` |
| `validate_gcfpe_current`, `change-flow` self | exit 0 | exit 0 | exit 0 |
| `validator_revision` | 3.2.9 | **3.2.11** | 3.2.11 |
| `.pyc` written | 0 | 0 | 0 |

The new interface at its edges, all measured:

| input | result |
|---|---|
| `{}` | `validated=[]`, no errors |
| an id outside the roster | `PROMPT_BODY_UNEXPECTED_ID:NOT-A-PROMPT` |
| key/header mismatch | `PROMPT_BODY_ID_MISMATCH:IA-10:IA-30` |
| header absent | `PROMPT_BODY_ID_MISMATCH:IA-10:ABSENT` |
| malformed stdin | `BODIES_STDIN_MALFORMED` |
| a list instead of a map | `BODIES_STDIN_NOT_ID_TO_TEXT_MAP` |

**Against real Notion text**, one page read this session and not persisted: `IA-10`'s actual
sentence — *"resolve and read the unique current controlled PF10 Markdown and every applicable
active addendum by its repository path"* — satisfies `states_current_pf10_markdown`, and a body
omitting it does not.

## What was NOT verified, stated plainly

**No full per-prompt run against a complete real body was performed**, because doing so would have
meant materialising a body on disk or retyping it. The mechanism is proven at its edges and the
writer predicate is proven against real text; the reviewer can now do the full run with one page
read, which is the point of the change.

## Scope and package

Seven files, all inside `flowmaster-validate`; `change-flow` byte-identical at `14981ba7…`. Diff:
`round26.patch`, 528 lines.

| | files | bytes | sha256 |
|---|---|---|---|
| `flowmaster-validate.skill` | 29 | 282752 | `2495b2354d93414a0aa8dea3e40569b3fc5004100e22beeb2b56dca11589a805` |
| baseline — the installed tree | 29 | — | `f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd` |
| repaired tree | 29 | — | `54604cf33194858521b714c29bb94b39ef4b7bd913e652aceaf0bb4cba773948` |

Verified path-by-path and digest-by-digest: 29 entries, every one identical to the tested tree, none
outside the skill root, no traversal, nothing unpackaged. **The package is smaller than the tree it
replaces.**

`validator_revision` 3.2.9 → **3.2.11** at four sites; `FLOWMASTER_VALIDATE_REVISION` 3.2.11 →
**3.2.13**. 3.2.10 and 3.2.12 belong to the withdrawn round-25 package that a published verdict
describes. `CHANGE_FLOW_SPECIALIZATION_REVISION` stays 3.2.8 and the candidate contract stays
`1c3c7969…` / 610549 in both copies — the hash-pin chain does not move.

## A follow-up finding, out of scope and recorded rather than silently left

`validate_epic_alpha.py` and `validate_strength_middleware.py` each carry a `validate_snapshot` /
`validate_prompt_snapshot` function that globs a directory of prompt `.md` files and gates on a
`SNAPSHOT_MEMBER_SET`. **Same defect class, different prompt sets.** Neither is reachable from any
GCFPE gate — both run only through their own CLI with an explicit `--prompts <dir>` — so they are
dormant rather than active. They are named here for a Product Owner decision instead of being
silently changed or silently ignored.

## What this does not claim

No QA verdict, no acceptance, no closure, no PF09 movement. Nothing installed, merged or
auto-merged. Round 25 stays withdrawn and its `SF10-12` body pins are absent from this package. The
selected release `GCFPE-20260913.1 / 091326.2 / 54` is untouched, and no prompt body, registry row
or graph part changed.
