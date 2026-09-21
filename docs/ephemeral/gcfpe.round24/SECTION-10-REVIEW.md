---
artifact_type: SKILL_FIT_SECTION_10_VERDICT
artifact_version: "1.0"
created_date: 2026-09-21
author: SFR-01
subject: Independent §10 validation of the round-24 flowmaster-validate package
supersedes: nothing — successor record to docs/ephemeral/gcfpe.round23/POST-INSTALL-AND-SECTION-10.md
---

# §10 verdict — round 24 (`F1` + `SF10-11`)

## Verdict

**`SKILL_FIT_CONFIRMED`**, with one finding and one nit, both non-blocking.

Bound to exactly:

    flowmaster-validate.skill   29 files, 279481 bytes
    sha256 e8f30b9a798ce12b0616d54ee6fb99af296bab9f1986cfa6158088a8c3bff872
    extracted tree digest (freeze.py, rooted at the skill directory)
    29 f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd

**This verdict is void for any other bytes.** `change-flow` was not in scope this round; its
round-23 confirmation carries, and I re-derived its installed digest as
`21 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` to confirm it has not moved.

Nothing was installed. Nothing was written to the synced skills directory — both installed
digests still reproduce after every experiment. Zero `.pyc` written anywhere.

One movement under me, disclosed: the evidence branch advanced from the named commit
`135388f` to `d48bccf`. The delta is one file, `gcfpe.round24/REVIEWER-PROMPT.md`, added after
the round under review. No packaged byte and no evidence file I relied on moved, so the review
is not void.

## 1. Identity reproduced before anything else

| claim | reproduced |
|---|---|
| package sha256 / byte count | `e8f30b9a…` / 279481 — **yes**, from the bytes I was given |
| baseline, installed `flowmaster-validate` | `29 5dcb95a9…` — **yes** |
| repaired tree | `29 f170a01c…` — **yes** |
| unchanged `change-flow` | `21 14981ba7…` — **yes** |
| superseded 317-file whole-tree value | measures `c607cedc…` in this container — **yes** |

Package hygiene: 29 file entries, zero directory entries, every entry under
`flowmaster-validate/`, no traversal sequence, no absolute path, no symlink entry.
`name: flowmaster-validate` present in SKILL.md frontmatter.

**§8c — the patch accounts for every difference.** Exactly five files differ between the
installed skill and the extracted package, and they are the five `round24.patch` names. I applied
the patch to a copy of the installed skill: it applied clean and the result is **byte-identical**
to the package (`diff -r` clean, digest `f170a01c…`). Nothing rides along.

## 2. The claims

| claim | disposition |
|---|---|
| **C1** `validator_revision` 3.2.8 → 3.2.9 at exactly four sites, all coupled | **confirmed** |
| **C2** `FLOWMASTER_VALIDATE_REVISION` → 3.2.11 at one mutable site, prose preserved | **confirmed** |
| **C3** both halves of the guard now have a uniquely-firing case | **confirmed by re-execution** |
| **C4** the hash-pin chain does not move | **confirmed** |
| **C5** a whole-tree digest is a tree identity, not a per-skill one | **conclusion sound; attribution unverifiable — see A4** |

**C1, recounted by grep, independently of the report.** Four value-bearing sites, all `3.2.9`,
all inside `flowmaster-validate`, none in `change-flow`, none in the candidate contract:
`references/…validation-profile.json:45`, `scripts/run_gcfpe_20260914_fixtures.py:667`,
`scripts/validate_gcfpe_20260914.py:1063`, `scripts/validate_flowmaster.py:1223`.
The coupling is real, not asserted: I reverted the profile alone to `3.2.8` and left the scripts
at `3.2.9`, and the candidate validator returned `ok: False`, `errors: ['PROFILE_IDENTITY']`.

**C2.** `FLOWMASTER_VALIDATE_REVISION` appears at four lines in SKILL.md; only line 8 is an
assignment, and it reads `3.2.11`. The other three are prose. No script anywhere checks
`FLOWMASTER_VALIDATE_REVISION`, so one mutable site is the correct count.

**C4, re-derived from the file, never transcribed.** The bundled candidate contract measures
`1c3c7969b7b933569362a35acdff6f756e2ab8577054f5038e4a95ad3794e179` / 610549 bytes; `cmp` shows
the two bundled copies byte-identical; the validator's `EXPECTED_CANDIDATE_CONTRACT_SHA256`
(line 943) and `_BYTES` (line 944) and the profile's `candidate_contract.sha256` /
`byte_count` all agree with the file itself. `CHANGE_FLOW_SPECIALIZATION_REVISION` is `3.2.8` at
every mutable site and the profile's `installed_skill_revisions.change-flow` is `3.2.8`.

**A5, recounted rather than accepted.** The two `3.2.7` occurrences
(`change-flow/SKILL.md:558`, `flowmaster-validate/SKILL.md:24`) are dated narrative records, and
so are the `3.2.10` mentions. One correction to the prompt's own framing: there are **two**
3.2.10 prose lines, not one — line 36 is round 23's record and line 43 is the round-24 successor
sentence beside it. Both are correct AUTH-001 preservation; the count in the prompt is off by one.
`3.2.9` has never been emitted as a `validator_revision` by any prior round, so the corrected
identity does not itself collide — which is the whole point of F1.

## 3. The attack (§6), in priority order

### A1 — C3's second half, re-run on throwaway copies

**All three experiments reproduce exactly as claimed.** Run against the shipped fixture code path
with the timing cases stubbed, on a corpus I rebuilt from Notion myself.

| experiment | author's claim | measured |
|---|---|---|
| remove `len(rows) != 2 or ` | only `reject-source-duplicate-crd-class-branch` fails | **only that case failed** |
| remove ` or {…} != expected` | only `reject-source-epic-to-crd` fails | **only that case failed** |
| remove the whole `if` + append | all four class-map cases fail | **all four failed** |

Unmodified, all **9** source cases pass and
`accept-live-source-class-specific-closure-intakes` returns `errors: []`.

The judgment under attack survives someone else's hands. Experiment 1 is the decisive one: with
the length half removed, `reject-source-absent-crd-class-branch` **still passes** — the mapping
half catches absence unaided. The absence fixture alone genuinely does not close the length
branch, and the duplicate fixture is genuinely what that branch needed. No case is one that
cannot fail.

### A2 — is the absence fixture's mutation shape real, or an artefact?

**The fixture tests what its name claims, and the shape is harmless — but the shipped reason
given for it is wrong.** Measured three shapes:

| shape | rows | length half | mapping half | observed |
|---|---|---|---|---|
| shipped: `<td>`CRD`</td>` → `` (element removed) | 1 | fires | fires | `['QA_PASS_BODY_CLASS_MAP']` |
| realistic: → `<td></td>` (a cleared Notion cell) | 1 | fires | fires | `['QA_PASS_BODY_CLASS_MAP']` |
| the shape the author rejected: whole `<tr>` removed | 1 | fires | fires | `['QA_PASS_BODY_CLASS_MAP']` |

All three are equivalent, so the choice costs nothing and the fixture does isolate the
`QA_PASS_BODY_CLASS_MAP` **error code**. A real body could carry the malformation: Notion renders
a cleared cell as `<td></td>`, which drives the identical branch.

But the shipped comment's stated reason does not hold — **see the finding in §4.**

**§8d, explicitly:** `reject-source-absent-crd-class-branch` observes exactly
`['QA_PASS_BODY_CLASS_MAP']`. Confirmed.

### A3 — the duplicate fixture's line scan

**Correct against the live body, and loud on every failure path I could construct.**
`<td>`CRD`</td>` occurs exactly once (index 45); `lines[anchor-1]` is `` <td>`PASS`</td> `` and
`lines[anchor-2]` is `<tr>`; the next `</tr>` closes the row at 47. The line-scanned row is
**identical** to what `QA_PASS_ROW_HTML_RE` matches — so the scan is right, and it got there
without using the regex under test, which is the point.

| perturbation | behaviour |
|---|---|
| class cell renamed | `ValueError` — loud, generic (from `.index()`) |
| `PASS` cell changed above it | `ValueError` — loud, custom message |
| `<tr>` gains an attribute | `ValueError` — loud, custom message |
| anchor at index 0 (negative-index wrap) | `ValueError` — loud, custom message |

No silent path found. The two `.index()` calls raise a generic `ValueError` rather than the
custom "Mutation anchor absent" message; both are uncaught, so both are loud. Worth knowing, not
worth changing.

### A4 — C5, a claim about the author's own instrument

**I can rule out the half that matters, and I cannot confirm the half that does not.**

Ruled out by measurement, independently of the report: **nothing of ours moved.**
`flowmaster-validate` installed reproduces `5dcb95a9…` — the exact baseline round 24 diffed
against — and `change-flow` reproduces `14981ba7…`, the value round 23 confirmed. Those are the
only two skills this project owns. "Something of ours moved and the explanation is convenient" is
false.

Not confirmable: that `built-in-browser/SKILL.md` specifically is the mover. A 317-file digest is
one scalar; it records *that* something moved, never *what*. No round-23 per-skill record exists
for the other 24 skills, and every file in the tree carries the same container-start mtime, so
mtime does not separate them either. The attribution should be read as the author's unverified
explanation, not as an established fact.

That unfalsifiability is itself the strongest evidence **for** C5: an identity you cannot
attribute is not an identity. Rooting the same unchanged script at the skill directory produces a
digest that reproduced exactly, in a different container, for both skills. C5's conclusion is
correct and the recipe change is right.

## 4. Findings

### Finding 1 — the absence fixture's shipped comment states a reason that is false of this fixture, and claims coverage the round itself disproved

*Artifact:* `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py`, the comment block above
`("reject-source-absent-crd-class-branch", …)` (patch lines corresponding to the new comment).

*Defect, two parts.*

1. **Wrong scope.** The comment says: "Deleting the row also trips
   `PROMPT_HANDOFF_RECEIVER:QA-120:CL-C-10`, and a fixture that fires two guards cannot prove
   which one caught it." `PROMPT_HANDOFF_RECEIVER` is emitted in `validate_prompt_bodies`
   (`validate_gcfpe_20260914.py` lines 2293/2299/2306). This fixture calls only
   `validate_qa_closure_bodies` (lines 2101–2139) and never reaches that guard. Measured: with
   the whole row deleted, the fixture observes exactly `['QA_PASS_BODY_CLASS_MAP']` — **one**
   guard, not two. The justification for choosing the cell over the row does not apply to the
   fixture it justifies.

2. **Overclaimed coverage.** The same comment says the absence case "isolates the arity branch".
   It does not: I measured that absence fires **both** halves, and experiment A1-1 shows the
   mapping half catches it alone. The comment twenty lines below contradicts it correctly
   ("the mapping half … catches absence on its own, so the length half still had nothing firing
   it"), and `REPORT.md` states it correctly too.

*Why it matters, beyond tidiness.* SF10-11 exists because a fixture **name** advertised coverage
it did not provide, and D5 recorded the lesson as "concealed coverage is worse than visible
absence". This comment re-creates that failure one layer down: a maintainer reading only the
absence fixture's comment would conclude it exercises the length branch and could delete the
duplicate fixture as redundant — reopening precisely the gap this round closed.

*Evidence.* `REPORT.md` has both statements right — it writes "in the end-to-end validator" and
says plainly that absence "drops the row count to one *and* breaks the mapping". The shipped
comment dropped the qualifier and inverted the conclusion. The report is accurate; the bytes are
not, and the bytes are what ships.

*Smallest correction.* In that comment only, two edits, no behaviour change:
- add the scope qualifier — "trips `PROMPT_HANDOFF_RECEIVER:QA-120:CL-C-10` **in the end-to-end
  validator**";
- replace "and this case isolates the arity branch:" with what was actually measured — e.g. "and
  the observed error is exactly `['QA_PASS_BODY_CLASS_MAP']`:" — and let the duplicate fixture's
  comment keep sole ownership of the length-branch claim.

*Severity.* Non-blocking. Behaviour is correct, the guard is fully covered, all 9 source cases
pass. This is a reasoning record in shipped bytes, of the exact kind this project treats as
evidence.

### Nit — one unwrapped line in the new SKILL.md paragraph

`flowmaster-validate/SKILL.md:51` is 138 characters where the round-24 paragraph it sits in
(lines 38–52) wraps at 86–92. Cosmetic only, and **not** a file-wide violation — SKILL.md carries
many long lines elsewhere (up to 790 characters), and no validator enforces a wrap. Correction:
rewrap line 51 to match its paragraph. Mentioned for completeness, not as a defect.

## 5. Gates — what I actually ran, and what I could not

**Ran, green, from the extracted contents** (the package placed into a copy of the installed
tree so its siblings are present, per L2; `PYTHONDONTWRITEBYTECODE=1` throughout). Top-level
flags read by name, not section counts:

| gate | top-level flag | result |
|---|---|---|
| contract fixtures (no `--prompt-dir`) | `fixture_suite_ok: true` | exit 0 — 155 cases, 0 failed |
| candidate validator (no `--prompt-dir`) | `ok: true` | exit 0 — `errors: []` |
| `validate_flowmaster.py` | `suite_ok: true`, `verdict: FLOWMASTER_SUITE_PASS` | exit 0 |
| `validate_gcfpe_current.py change-flow` | `ok: true` | exit 0 — `errors: []` |
| `change-flow/scripts/validate_gcfpe_20260914.py` | — | exit 0 — `PASS` |

`validator_revision` emitted by the repaired tree: **3.2.9**. By the installed tree: **3.2.8**.

**Ran in part — the body-fixture gate.** I executed the shipped source-case block, all **9**
cases, against a three-body corpus (`QA-120`, `CL-E-10`, `CL-C-10`) that I fetched from Notion
myself from the contract's own `notion_page_manifest` and wrote to disk. That block reads exactly
those three bodies. On the installed tree the same corpus yields **7** source cases at
`validator_revision 3.2.8`; on the repaired tree, **9** at `3.2.9`.

This is the whole of round 24's body-fixture delta: 155 contract cases + 9 source cases + 17
timing cases = **181**, and 155 + 7 + 17 = **179**. The 17 timing cases are untouched by this
round. So the part of the body-fixture gate that this round changes, I ran; the part I did not
run, this round does not touch.

**Not run — the end-to-end gate on all 55 bodies, and the timing cases.** Stated plainly rather
than inferred. Notion is reachable, so L1's stated fallback does not apply, but the corpus is not
reproducible to a standard I would sign:

- each body is retrievable only one page at a time through a tool whose output must be
  transcribed by hand into a file — there is no credential in this environment that would let a
  script fetch them;
- **no body hashes are pinned anywhere** — not in the contract, not in the profile. The validator
  computes `prompt_body_sha256` and reports it; nothing checks it. So a rebuilt corpus cannot be
  verified against any reference, and my own transcription errors would be undetectable;
- I caught myself dropping a sentence from the first body I transcribed. Across 55 bodies that
  error rate makes a "0 errors" result a claim about my typing, not about the package.

A transcribed 55-body run would have produced a number, not evidence. I did not produce one.

**A standing observation for the Product Owner, not a finding against this package:** these two
gates are structurally unreproducible by any independent reviewer, for the reasons above. Every
§10 round will hit this same wall. Pinning `prompt_body_sha256` for the 55 members into the
profile would make the corpus verifiable and these gates independently runnable, at the cost of
re-pinning whenever a body legitimately changes. That is a Product Owner call, and it belongs to
its own round, not this one.

## 6. Questions this round did not settle

### Q1 — was adding the second fixture beyond approved scope the right call?

**Yes.** A question, not a finding.

The Product Owner approved "F1 plus the class-map fixture gap". Falsification showed the approved
fix did not close that gap: with only the absence fixture, removing the length half breaks
nothing. Shipping it alone would have delivered a fixture whose presence implies coverage the
author had **already disproved in the same round** — which is D5's concealed-coverage defect
reproduced, not repaired. Honouring the letter of the approved scope would have violated its
purpose.

The economics the project has already ruled on point the same way. Packaged bytes are
hash-scoped, so deferring one fixture costs a full extra cycle — new package, install, fresh §10
— for one line. The D5 note settled that such items batch into the round that already moves the
bytes; that is why F1 and this gap were batched into round 24 in the first place. Deferring the
duplicate case would have contradicted the ruling that produced this round.

The addition is also minimal and strictly additive: one fixture, no contract change, no new error
code, no behaviour change, nine cases all passing. And the author disclosed it as added scope and
supplied the falsification to test it. That is the right shape. My only reservation is that the
disclosure in the shipped bytes is inaccurate — which is Finding 1, and is a defect in the
disclosure, not in the decision.

### Q2 — is `SF10-11` the right identifier, and is one identifier correct for two fixtures?

**Yes to both.** A question, not a finding.

*On the series.* `SF10-NN` denotes a substantive validation-behaviour repair to these skills. It
is not a provenance tag, and provenance is already recorded elsewhere — D5 for the gap, the §10
record for the review that surfaced it. Minting a separate series for reviewer-originated defects
would fragment the numbering and destroy the one property `SF10-NN` has: a single total order
over the changes to these bytes. The distinction is being applied consistently in this very
round — `F1`, also reviewer-originated, correctly did **not** receive an SF10 number, because it
corrects a recorded identity rather than validation behaviour.

*On one identifier for two fixtures.* Correct. They are one repair — "give each half of one guard
a case that uniquely fires it" — and neither closes it alone. The absence fixture's real role is
as the experiment that proved the duplicate fixture necessary; numbered separately it would look
like an independent, separately-deferrable change, which is exactly the deferral that would have
cost an extra §10 round. One defect, one identifier, two fixtures.

## 7. Disposition of every prior finding

| finding | status |
|---|---|
| **F1** — `validator_revision` should be 3.2.9 | **FIXED.** Applied at all four sites and nowhere else; coupling verified by mutation; `FLOWMASTER_VALIDATE_REVISION` correctly moved to 3.2.11 alongside, because 3.2.10 is installed and bound to a published verdict naming `26a8d476…`. The round-23 prose recording the 3.2.10 increment is preserved with a successor paragraph beside it, per AUTH-001, not rewritten. |
| **F2** — the freeze recipe was not reproducible | **STILL CLOSED**, and re-tested rather than assumed. `freeze.py` with `EXCLUDE = {"manifest.json"}` reproduced all four published digests exactly in this container. No defect found while checking it. |

One observation found while checking F2, **out of scope for this verdict** because `freeze.py`
is a repository evidence file and not among the 29 packaged files: its docstring still says "the
count printed … is one fewer than the tree's file count". That holds when the script is rooted at
the synced tree, but C5 now roots it at a skill directory, where no `manifest.json` exists and the
count equals the file count (29 = 29, 21 = 21). The sentence is stale relative to the recipe's new
scope. Repair it in whatever round next touches that file.

## 8. What I did not do

Did not install. Did not write to the synced skills directory — verified after the fact, both
installed digests still reproduce and no `.pyc` exists anywhere. Did not merge and did not enable
auto-merge. Did not edit `docs/pfcanon/**`. Did not change prompt bodies in Notion — every fetch
was a read. Did not change the candidate contract, the graph parts, or the approved registry.
Every digest in this record was derived from the artifact in front of me; none was transcribed
from `REPORT.md`.

---

**DECISION NEEDED** — the bytes are confirmed and Finding 1 is non-blocking, so the call is yours:
install `e8f30b9a…` as it stands and carry the comment correction into the next round that moves
these bytes (the precedent F1 itself set), or hold for a corrected package and spend a cycle on a
two-line comment edit. My recommendation is the former. The behaviour is right; the record of why
is what needs one more pass.
