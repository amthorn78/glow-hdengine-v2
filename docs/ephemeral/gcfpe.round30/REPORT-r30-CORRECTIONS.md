---
artifact_type: GCFPE_REPAIR_ROUND_REPORT_SUCCESSOR_CORRECTIONS
artifact_version: "1.0"
created_date: 2026-09-22
round: 30
release: GCFPE-20260914.1 / 091426.1 / 55 (SELECTED)
authority: SFR-01 §10 verdict on round 30 — SKILL_FIT_CONFIRMED, four non-blocking items
corrects: docs/ephemeral/gcfpe.round30/REPORT-r30.md — by succession, never in place (AUTH-001)
packages_unchanged: true
status: CORRECTIONS_RECORDED_PACKAGES_AWAITING_PRODUCT_OWNER_INSTALL
---

# Round 30 — two claims were wider than the evidence

`SFR-01` returned **`SKILL_FIT_CONFIRMED`**, bound to `change-flow.skill` `ed7041c0…` and
`flowmaster-validate.skill` `0e00084e…`, void for any other bytes and for either skill alone.
Both round-29 findings verified fixed by falsification. Every gate measurement reproduced; none
contradicted.

**Two of the four non-blocking items are corrections to what round 30 *claimed*, not to what it
*built*.** The packages are unchanged and are not rebuilt for this. `REPORT-r30.md` stands as
issued; this is its successor.

## C1 was false on the strict reading — corrected

**What round 30 said:** *"Rounds 28, 29 and 30 are now mutually distinguishable on all three
advertised values."*

**What is true:** rounds 28 and 29 still share `FLOWMASTER_VALIDATE_REVISION: 3.2.15` and
`validator_revision: 3.2.13`. Only `SKILL_TREE_SHA256` separates that pair.

**The corrected sentence:** *round 30 is distinguishable from both predecessors on all three
advertised values; rounds 28 and 29 remain separable only by tree hash.*

Not repairable, and the reviewer said so before I could: rounds 28 and 29 are published, immutable
and superseded, and **both carry `SKILL_REPAIR_REQUIRED`**, so confusing them costs nothing. The
hazard R29-F1 actually named is gone — the package that would be installed is distinct from both on
every value. The damage is permanent and cosmetic, which is the right way round.

It is still a claim that overstated its evidence, in a round whose entire subject was an identity
claim that overstated its evidence.

## C3 was true of its controls and not of its surface — corrected

**What round 30 said:** *"The fix creates no new false positives. 7 of 7 controls pass."*

**What is true:** the controls pass, and the false-positive surface grew — exactly where `A1`
predicted it would. **I measured this myself against both packages rather than accepting the
report:**

| line | r29 | r30 |
|---|---|---|
| ``- `Selection status:` — prohibited in a body`` | `False` | **`True`** |
| ``- `Lifecycle:` — prohibited`` | `False` | **`True`** |
| ``\| `Lifecycle:` \| prohibited \| register \|`` | `False` | **`True`** |
| ``## `Selection status:` is prohibited`` | `False` | **`True`** |

All four are one shape: **a line that names the forbidden field while forbidding it**, as a bullet,
a table row or a heading. Removing code marks from the whole line is what stops the backticks
protecting them. Five controls — including `## Selection and authority`, the register prose and a
line carrying a backticked identifier mid-sentence — return `False` in both rounds.

**The corrected sentence:** *the controls pass and the surface grew in a characterised way; the
widening is a real input to `AF-004`, which stays open.*

**No real instance is observed.** `SFR-01` ran the shipped matcher over real lines from the bodies
it has read across three rounds and read two further bodies chosen for structural risk. The corpus
convention — field names as backticked identifiers *inside* sentences, never as line-leading
labels — is what keeps the check safe, and that convention is not enforced anywhere.

**If a sweep ever does turn one up, the fix is narrow, not a looser strip:** require the key to be
followed by a governance *value*, or exempt a line that also contains a prohibition word.

## Two items that are corrections to the instructions, and are fixed here

### The changed-file enumeration was short by one

`flowmaster-validate` differs from round 29 in **five** files, not the four §8c listed:

```
SKILL.md
references/gcfpe-20260914.1-091426.1-validation-profile.json
scripts/run_gcfpe_20260914_fixtures.py
scripts/validate_flowmaster.py            <-- omitted
scripts/validate_gcfpe_20260914.py
```

`validate_flowmaster.py`'s only diff is one line — `"validator_revision": "3.2.13"` → `"3.2.14"` —
**mechanically required by R29-F1's own fix**, because it is one of the four revision sites. The
change is correct; the enumeration was not. Verified here by `diff -rq`, which is the point.

It matters because `A3` says the revision bump has now been got wrong twice: a reviewer told to
confirm "these files and nothing else" would read a legitimate diff as an extra.

**Fixed in `reviewer-prompt-template.md` §8c:** the changed-file list must be *derived* by
`diff -rq` or `git diff --name-only` and pasted, never typed from memory, and a file whose only
change is a version string still belongs on it.

### The branch was gone by review time, for the second round running

`docs/20260922-gcfpe-round30` had merged as **#449** and been deleted before `SFR-01` looked, just
as `docs/20260921-prompt-body-policy` merged as #445 the round before. The reviewer read `main` at
`2efd4e1` and found nothing missing, but it is a step that should not exist.

**Fixed in `reviewer-prompt-template.md` §4:** if the named branch does not exist, it merged and
was deleted — read the same paths on `main` — and the prompt names the pull request alongside the
branch.

## The one suggestion, converted into a control

`A4` found the `SKILL.md` narrative accurate rather than self-serving, with one weakness: it
**narrates rather than prescribes**, so a reader learns the rule was broken twice and is not told
what to do.

That is right, and it is why the rule failed to stop me while I was editing the paragraph that
states it. `skill-identity-and-freeze.md` now carries **"Advertised identity must be unspent"** —
the diff command to run before packaging, the definition of a spent identity, why
`SKILL_TREE_SHA256` cannot do this job (it moves automatically and no report emits it), and the
three occasions the rule has been broken.

Putting it there rather than in `SKILL.md` keeps the confirmed packages unchanged. The next
packaging round should carry the same imperative into `SKILL.md`, where the author will be looking.

## Five vectors still evade, and none should be chased

Confirmed by measurement against the shipped package:

| vector | evades | Notion produces it? |
|---|---|---|
| zero-width space `U+200B` | yes | no |
| BOM / ZWNBSP `U+FEFF` | yes | no |
| `&nbsp;` **as leading whitespace** | yes | no |
| `<b>Lifecycle:</b>` | yes | no |
| `#######` — `#{0,6}` caps at six | yes | no; not valid Markdown either |

One refinement to the reviewer's table, from measuring it: `&nbsp;` evades only in the **lead-in**
position. As a value separator — `Lifecycle:&nbsp;X` — it is caught, in round 29 as well as round
30, because the key still leads the line. The literal NBSP *character* is caught in both positions.

Each of these requires someone deliberately encoding a governance line to slip a check. **That is
not the threat model** — the threat is a line added in good faith, and every good-faith rendering
is now caught. Recorded so the next reviewer does not re-derive the list; not worth a round.

## What did not change

The packages. `change-flow.skill` `ed7041c0…` / 242827 and `flowmaster-validate.skill`
`0e00084e…` / 288056 are the confirmed bytes and are the bytes to install. Nothing in this record
alters them, and the verdict remains void for any others.

Contract `2b78f877…` / 606657 and graph `90021eb7…` / 569835 unmoved, confirmed by the reviewer
against every consumer.

## `AF-004` — moved, not closed

Distinct bodies directly confirmed clean: **15 of 55**, up from 13 — the 7 read in round 28 plus 8
read by `SFR-01` (`PR-35`, `CF-E-20`, `CL-30`, `GCFPE-MGMT-10`, `MGR-10`, `UTIL-10`, `IA-10`,
`QA-90`), with no overlap. **The other 40 have never been looked at.**

It remains open and Product Owner-deferred to the next `GCFPE-MGMT-10` run, and it is now more
worth running than it was: the matcher a sweep would exercise catches every good-faith rendering,
so the sweep produces a real answer in both directions rather than a partial one — and the widened
surface above is a second reason to run it.
