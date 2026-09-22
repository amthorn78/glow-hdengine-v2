---
artifact_type: GCFPE_SECTION_10_INDEPENDENT_REVIEW
artifact_version: "1.0"
created_date: 2026-09-21
round: 29
reviewer: SFR-01
role: independent re-review of my own round-28 SKILL_REPAIR_REQUIRED verdict
verdict: SKILL_REPAIR_REQUIRED
status: SUCCESSOR_RECORD_DO_NOT_EDIT_IN_PLACE
supersedes: nothing — SECTION-10-REVIEW-r28.md stands as issued (AUTH-001)
---

# Round 29 — §10 independent re-review

## Verdict

**SKILL_REPAIR_REQUIRED.**

Bound to these bytes, measured by me from the archives I was given:

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 242827 | `ed7041c0ee2179afcc0b684954f0605fd5ab495fea203a4dfafd7eb3f97c7860` |
| `flowmaster-validate.skill` | 29 | 286739 | `423458d9f0a61f89d301a4ee8e1f7819aad554b8c5cd149dc17b50478a481f69` |

**Void for any other bytes**, and for either skill installed alone.

**Both round-28 findings are fixed.** I verified each by falsification, in both directions. The
repairs are correct, minimal, and better than what I proposed — the fixture suite in particular.
Nothing in this verdict walks back round 28's disposition.

The verdict is repair-required on **one new blocking finding that this round introduced**:
flowmaster-validate ships changed validation behaviour under an unchanged revision identity, which
is the defect the skill's own `SKILL.md` records as round 24's `F1`, raised by a prior §10 review
and "accepted without argument." One non-blocking finding is recorded below it.

## Round-28 findings — disposition verified, not accepted on report

### R28-F1 — governance check evaded by decoration → **FIXED**

`GOVERNANCE_LINE_LEAD_IN_RE` strips leading whitespace and Markdown lead-in before matching, and
the authority line is now tested as a substring of the stripped line. I re-ran every vector from my
round-28 table against both packages:

| vector | r28 | r29 |
|---|---|---|
| plain `Selection status:` / `Lifecycle:` / authority line | CAUGHT | CAUGHT |
| leading spaces | evades | **CAUGHT** |
| leading tab | evades | **CAUGHT** |
| `**bold:**` | evades | **CAUGHT** |
| `- bullet` | evades | **CAUGHT** |
| `> blockquote` | evades | **CAUGHT** |
| bolded authority line | evades | **CAUGHT** |

**C1 is exactly true: all nine vectors I named are caught.** The fix also closes six I did not
name — non-breaking space, `***nested***`, single-`*` italic, `_underscore_`, `> - **combined**`,
`>>` nested quote, four-space indent — and catches the authority line indented, bulleted, bolded
and mid-sentence.

**C2 holds.** All five of my false-positive controls still pass, and see A2 for the corpus test.

### R28-F2 — profile asserted `UNSELECTED_CANDIDATE` about the contract it pins → **FIXED**

Renamed to `selection_status_during_staging` in the profile and in `load_profile`'s required
subset. Falsified both directions:

- Reverting to the bare `selection_status` fails `PROFILE_CONTRACT_PIN`. **C3 is true: the
  assertion moved rather than disappearing.**
- More important, and not claimed by the report: the round-28 *trap* is gone. I added
  `selection_status_current: "SELECTED_PRODUCTION"` — the true current fact — to the pin block and
  the gate accepted it. In round 28, stating that truth **broke** the gate. The profile is no
  longer required to be silent-or-false about the contract's actual selection state.

### The defect found while fixing them → **REPAIRED, and better than I asked for**

The round-28 fixture suite tested only undecorated input, which is why R28-F1 survived it. Seven
decorated reject cases and one prose accept case are added. The prose control is tighter than I
would have written: it includes a bulleted and a block-quoted line, and
`> Selection status is never inferred from a page header.` sits one character — the colon — away
from firing. That is a control that would actually catch an over-broad strip.

## Findings

### R29-F1 (blocking) — changed validation behaviour ships under an unchanged revision identity

**Artifact.** `flowmaster-validate/SKILL.md` line 8; and `validator_revision` at its four sites:
`references/gcfpe-20260914.1-091426.1-validation-profile.json:45`,
`scripts/run_gcfpe_20260914_fixtures.py:688`, `scripts/validate_gcfpe_20260914.py:1078`,
`scripts/validate_flowmaster.py:1221`.

**Defect.** Two different byte-sets advertise the same revision identity while behaving
incompatibly.

| | round 28 | round 29 |
|---|---|---|
| package sha256 | `b5f5d3a3…` | `423458d9…` |
| `FLOWMASTER_VALIDATE_REVISION` | **3.2.15** | **3.2.15** |
| `validator_revision` (all four sites, all three reports) | **3.2.13** | **3.2.13** |
| `SKILL_TREE_SHA256` | `8ed6d8b0…` | `740844f0…` |
| fixture cases | 156 | 164 |

**Evidence — they are not merely different, they are mutually incompatible.** Each validator
rejects the other's validation profile. Measured on full sibling trees, profile swapped, each
validator running from its own tree:

| validator | profile carried | result |
|---|---|---|
| r28 | r28 (own) | clean |
| r29 | r29 (own) | clean |
| r28 | r29's profile | **`PROFILE_CONTRACT_PIN`** |
| r29 | r28's profile | **`PROFILE_CONTRACT_PIN`** |

And `prompt_body_governance_state` returns a different answer on fifteen of my vectors. Two
independent behaviour changes, one advertised identity.

**Why this is blocking, by the skill's own recorded standard.** `SKILL.md` states the rule twice,
and both clauses are violated:

> round 23 shipped `SF10-09`'s validation behaviour while still emitting `validator_revision:
> 3.2.8` … **The counts coincided and that coincidence was the hazard**, so `validator_revision`
> moves to **3.2.9** at its four sites.

> Because 3.2.10 is installed and **bound to a published §10 verdict, corrected bytes must not
> reuse it**, so `FLOWMASTER_VALIDATE_REVISION` moves to **3.2.11** in the same change.

3.2.15 and 3.2.13 are bound to a published §10 verdict: my round-28 **SKILL_REPAIR_REQUIRED**,
merged to `main` at `docs/ephemeral/gcfpe.round28/SECTION-10-REVIEW-r28.md`. These corrected bytes
reuse both numbers. A reader matching my round-28 verdict to a package by revision applies
`SKILL_REPAIR_REQUIRED` to bytes that fixed it, or this record to bytes that did not.

**The `SKILL_TREE_SHA256` mitigation is real but does not reach this.** That hash did move, and it
protects an installed tree against its own declaration — which is why it caught my own scratch
contamination last round. But **no report emits it.** I checked all three: `validate_flowmaster.py`,
`validate_gcfpe_20260914.py` and `run_gcfpe_20260914_fixtures.py` each emit
`validator_revision: "3.2.13"`, and the first emits `self_identity: "OK"`. Those strings are
byte-identical between the two packages. The tree hash surfaces only as a *mismatch* error, never
as a value, so nothing in the artifacts a reviewer actually quotes distinguishes `b5f5d3a3…` from
`423458d9…`.

This is the same failure mode as the incident `SKILL_TREE_SHA256` was built for — on 2026-09-21 a
withdrawn package was installed under the required filename and "the hash-pin chain, the fixture
suites and the independent review all stayed green for a full round."

**Smallest correction.** `validator_revision` → **3.2.14** at its four sites;
`FLOWMASTER_VALIDATE_REVISION` → **3.2.16** (3.2.15 is spent); add the round-29 paragraph to
`SKILL.md`, which currently ends at round 28 and describes this round nowhere; re-stamp
`SKILL_TREE_SHA256` last, since the edits above change it. Verified: all five gates green,
`fixture_suite_ok: true` at 164 cases with zero failures, `self_identity: OK`.

Worth noting plainly: §8f asked me to confirm the revisions were **unchanged**, and they are. The
confirmation is what surfaced the finding.

### R29-F2 (non-blocking) — residual evasion, ranked by whether Notion produces it

**Artifact.** `GOVERNANCE_LINE_LEAD_IN_RE` in `scripts/validate_gcfpe_20260914.py`.

**Defect.** `^[\s>*\-+]*(?:\*\*|__|\*|_)?\s*` strips a lead-in but cannot handle emphasis that
*closes* before the colon, nor markers outside its character class. Twelve vectors still evade.
The ones that matter are the ones Notion's editor produces from ordinary editing:

| vector | Notion produces it? | evades |
|---|---|---|
| `**Lifecycle**: X` — emphasis closes before the colon | **yes** — bolding the word but not the colon | yes |
| `1. Selection status: X` — ordered list | **yes** — numbered list | yes |
| `# Selection status: X` — heading | **yes** | yes |
| `` `Lifecycle:` X`` — code span | **yes**, and this corpus uses backticks heavily | yes |
| `\| Lifecycle: \| X \|` — table cell | **yes** — the lane hubs use tables | yes |
| `~~Lifecycle:~~ X` | plausible | yes |
| zero-width space, BOM, `&nbsp;`, `<b>` tag | no — requires intent | yes |

`**Lifecycle**: X` is the sharp one, and the author flagged it and asked me to rule. It is not an
exotic tail: bolding the label in Notion yields `**Lifecycle:** X` if the colon is inside the
selection and `**Lifecycle**: X` if it is not. The check catches the first and misses the second,
so it catches roughly half of one of the three most common renderings.

**Why it is not blocking.** A substring scan over rendered Markdown has an infinite tail, and
completeness is not an achievable bar. The difference from round 28 is qualitative: there the gate
failed on the three *most common* renderings and the report claimed it made the class's return
impossible. Here every common rendering except this one is caught, the author claimed only what is
true, disclosed the residual, and asked for a ruling. The gate is a backstop; the primary controls
are the policy, the removal of the requirement, and the fact that nothing routes on the line.

**Smallest correction**, which I verified:

```python
GOVERNANCE_LINE_LEAD_IN_RE = re.compile(r"^[\s>#*_~`+|.\d\-]*\s*")
GOVERNANCE_KEY_RE = re.compile(r"^(?:Selection status|Lifecycle)[*_~`]*\s*:", re.IGNORECASE)
```

matching with `GOVERNANCE_KEY_RE.match(line)` instead of `startswith`. This closes eight of the
twelve — every Notion-natural one, including `**Lifecycle**:`, ordered lists, headings, code spans,
tables and strikethrough — keeps everything the current check catches, and introduces **zero** false
positives against the real corpus lines in A2. The four survivors (zero-width, BOM, HTML entity,
`<b>`) are not editor output and require intent. Add fixture cases for `**key**:` and `1.` at
minimum, since the present suite would not catch a regression in either.

## §6 — answered explicitly

**A1 — what the strip regex still misses.** Answered as R29-F2, with the full table above. Of the
author's own candidate list: heading markers, `1.` ordered lists, `~~strikethrough~~`, HTML
entities, zero-width characters and the BOM all still evade; **non-breaking space and nested
emphasis `***` are already caught** — `\s` matches U+00A0 in Python 3 str mode, and the `*` in the
character class consumes arbitrary runs. On the specific question asked: **`**Lifecycle**: X` does
evade, I confirmed it, and it matters** — it is half of "bold the label," not a tail case. It is
worth fixing in the same change as R29-F1 rather than a round of its own.

**A2 — is there a real false positive in the corpus?** **I looked and did not find one.** I ran the
shipped `prompt_body_governance_state` over twelve real lines drawn from the seven bodies I have now
read in full (`IA-10`, `UTIL-10`, `CF-E-20`, `MGR-10`, `GCFPE-MGMT-10`, `CL-30`, `PR-35`),
deliberately including the lines that come closest: `## Selection and authority`, "An unselected
candidate … is not selection evidence", "the selected release register remains the sole
runtime-selection authority", and bulleted lines beginning with backticked identifiers. **Zero
fired.**

The residual risk is constructed, not observed: a line like
`- Lifecycle: resolve from the register, never this page` **does** fire, and it is an instruction
rather than an assertion of state. No body writes one. The corpus phrases these as sentences —
"Resolve lifecycle from the owning operational register." — which pass. C2 is accurate for what the
corpus actually contains, and a substring scan cannot distinguish a labelled instruction from a
labelled assertion; if a future author writes one, the gate will need a narrow exception rather
than a looser strip.

One structural note worth recording: `#` is absent from the strip class, which is simultaneously
the heading evasion in R29-F2 **and** what protects `## Selection and authority` from firing. My
proposed correction adds `#` and keeps that control passing, because the real heading has no colon.

**A3 — is renaming the right shape of fix for F2, or merely quiet?** **Sufficient, and the premise
that the profile cannot express the contract's actual state is not correct.** `subset_errors`
checks a subset, so extra keys are permitted — I added `selection_status_current:
"SELECTED_PRODUCTION"` to the pin block and the gate accepted it. What F2 was about was a *required
falsehood*, and that is gone: the block now states history under a historical name, and the truth
can sit beside it.

Restructuring so `load_profile` sees the contract would let the profile's current-state claim be
*verified* rather than merely *stated*, and an unverified field is not worth adding. But it is not
needed: the contract is the authority for its own selection state, `validate_contract` already pins
that state to `status` through `CANDIDATE_SELECTION_ISOLATION` and `PRODUCTION_SELECTION_EVIDENCE`,
and gate 1 already cross-checks contract against graph. A third surface asserting the same fact is
what this whole repair sequence exists to remove. **Leave it renamed.**

**A4 — change-flow was not re-audited beyond byte-identity.** That is the right call, and I
confirmed the premise myself rather than accepting it: `diff -r` between the round-28 and round-29
extractions of `change-flow` reports **zero differences** — not equal digests, identical trees, file
by file. The freeze digest reproduces at `80e877c2…`, all 21 files, and `name: change-flow` is
unchanged.

**I am explicitly reusing my round-28 measurements on `change-flow`,** as §2 permits: the three
coupled-defect repairs, the symmetric staging-binding branch, the promotion transition, the hash
pins and the graph rebuild. I re-ran what is cheap and behavioural rather than assuming it:
`change-flow/scripts/validate_gcfpe_20260914.py` **PASS**, gate 1 green against its bundled
contract, `EXPECTED_GRAPH_SHA` recomputed and matching, both bundled contract copies and both graph
copies byte-identical. I did not rebuild the graph from `docs/graph/parts/` this round; it is the
same bytes I rebuilt in round 28 and reproduced at `90021eb7…`.

**A5 — fixture arithmetic.** **Confirmed, no case silently removed.** I compared the emitted case
*names*, not just the counts: 156 → 164, delta 8, **removed: none**, added exactly the eight named
in the diff — `accept-prose-mentioning-lifecycle-and-selection` plus seven
`reject-governance-state-*` cases for leading spaces, leading tab, bold, bullet, blockquote,
bullet-and-bold, and the bolded authority line. `fixture_suite_ok: true`, zero failures.

## Questions carried from round 28

**Q1** (graph `contract_id: …-CANDIDATE-GRAPH`, `status: FROZEN_FOR_CANDIDATE_AUTHORING`), **Q2**
(lane hub "Candidate prompt" / "Candidate binding" column headers) and **Q3** (`candidate_url` /
`candidate_version` node keys) are unchanged and remain questions, not findings. My round-28
reasoning stands and I have nothing to add: leave all three, and move Q1 in a round scoped to the
rename with its cascade enumerated first.

## Gates — what I ran, and what I did not

All five, from the extracted contents, in a full sibling tree with the whole synced directory
restored around the two replaced skills, `PYTHONDONTWRITEBYTECODE=1` everywhere including the
`importlib` calls.

| gate | flag | result | author's measurement |
|---|---|---|---|
| `flowmaster-validate/…/validate_gcfpe_20260914.py` | `ok` | `true`, `errors: []`, `SELECTED_PRODUCTION` | matches |
| `flowmaster-validate/…/run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` | `true`, 164 cases, §13 33/33 and 28/28 | matches |
| `flowmaster-validate/…/validate_flowmaster.py` | `suite_ok` | `true`, `FLOWMASTER_SUITE_PASS`, `self_identity: OK`, 0 findings | matches |
| `flowmaster-validate/…/validate_gcfpe_current.py` | `ok` | `true`, `errors: []` | matches |
| `change-flow/…/validate_gcfpe_20260914.py` | exit + text | `PASS` | matches |

**Every author measurement in §8 reproduced. I contradicted none of them.** R29-F1 is not a
contradiction of a measurement — it is a consequence of one §8f asked me to confirm.

**What I could not run:** nothing. **What I chose not to re-run:** the graph rebuild from
`docs/graph/parts/`, on identical `change-flow` bytes I rebuilt last round (A4).

## Identity, and the void check

| tree | files | digest | §3 |
|---|---|---|---|
| baseline `change-flow` (installed, still round-27) | 21 | `14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` | matches |
| baseline `flowmaster-validate` | 29 | `9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833` | matches |
| repaired `change-flow` | 21 | `80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8` | matches |
| repaired `flowmaster-validate` | 29 | `5da1c46b913a3494a17e72760384e524f37b6d76d94085495c444111b49ecb85` | matches |

The baseline reproduces, so the review proceeded. `SKILL_TREE_SHA256:
740844f0ba0fd7bd655f0cf703ac75e9063c102e849bfbf951154cba0053ae76` reproduces independently under
its own recipe — delete the declaration line, re-run `freeze.py`, same value.

Every archive entry sits under its own skill root; no traversal sequences, no absolute paths, no
entry outside the root; `name:` unchanged in both.

**§8c holds exactly as claimed:** `change-flow` differs in nothing; `flowmaster-validate` differs in
exactly the validator, the fixture runner and the validation profile, plus `SKILL.md`, whose only
change is the digest line. No files added or removed.

**All pins unmoved (§8f):** contract `2b78f877…` / 606657, graph `90021eb7…` / 569835, the
`source_snapshot` pin, both `EXPECTED_*` pairs, `change-flow`'s `EXPECTED_GRAPH_SHA`, and both
profile blocks. Both bundled copies of each artifact byte-identical. Revisions 3.2.9 / 3.2.15 /
3.2.13 — unchanged, which is R29-F1.

**The tree did not move under me.** The installed digests were still `14981ba7…` and `9c0ca6fe…` at
the end. Nothing was installed. The synced directory contains zero `.pyc`, zero `__pycache__`, and
zero files changed inside either reviewed skill. **No bytecode was written anywhere in scratch this
round** — round 28's contamination was my own `importlib` call without
`PYTHONDONTWRITEBYTECODE=1`, and §8's instruction closed it.

## Two procedural notes

**Round 28's prompt-drift finding was acted on, and it worked.** The copy I was handed this round is
**byte-identical** to the repository's — `abf26e1d…`, 11797 bytes, zero diff. Reading the branch
HEAD rather than a pinned commit is the correct instruction and I had no stale-copy problem.

**But the branch named in §4 no longer exists.** `docs/20260921-prompt-body-policy` was merged as
**#445** and deleted; the round-29 evidence, the policies, `freeze.py` and my own round-28 record now
live on `main` at `5b565bb`. I read them there. My round-28 record landed **verbatim** — I diffed it
against the commit I pushed. Nothing in §4's file list was missing, so this cost nothing, but the
next prompt should point at `main`.

## What is needed

Bump the revision identity (R29-F1), and fold the regex correction (R29-F2) into the same change
rather than spending another round on it. Re-issue both packages together and re-run §10 against the
new digests. `change-flow` need not be rebuilt; it is correct as-is, and if it is re-packaged
unchanged its digest must stay `ed7041c0…`.

**A1's residual is exactly where L1 says: 13 of 55 bodies directly confirmed, and the sweep with the
corrected tool has not been run.** That is honestly stated and I am not treating it as a finding.
It is now worth running: the tool that would close it is, with R29-F2 fixed, actually good enough to
be worth pointing at all 55.

---

DECISION NEEDED
