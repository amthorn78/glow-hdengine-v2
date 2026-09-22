---
artifact_type: GCFPE_SECTION_10_INDEPENDENT_REVIEW
artifact_version: "1.0"
created_date: 2026-09-22
round: 30
reviewer: SFR-01
role: independent re-review; returned SKILL_REPAIR_REQUIRED on rounds 28 and 29
verdict: SKILL_FIT_CONFIRMED
status: SUCCESSOR_RECORD_DO_NOT_EDIT_IN_PLACE
supersedes: nothing — the round-28 and round-29 records stand as issued (AUTH-001)
---

# Round 30 — §10 independent re-review

## Verdict

**SKILL_FIT_CONFIRMED.**

Bound to these bytes, measured by me from the archives I was given:

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 242827 | `ed7041c0ee2179afcc0b684954f0605fd5ab495fea203a4dfafd7eb3f97c7860` |
| `flowmaster-validate.skill` | 29 | 288056 | `0e00084e397ede0848c68f9368469d6be50f55bb044826088b40fc8485982e09` |

**Void for any other bytes**, and for either skill installed alone. These two install together.

Both round-29 findings are fixed, verified by falsification rather than accepted on report. No
defect in these bytes is blocking. Four non-blocking items are recorded below, two of which are
corrections to claims in §5 rather than to the packages — the claims are narrower than they sound,
and the record should say so.

## Round-29 findings — disposition

### R29-F1 — changed behaviour under an unchanged revision identity → **FIXED**

| | r28 | r29 | r30 |
|---|---|---|---|
| package sha256 | `b5f5d3a3…` | `423458d9…` | `0e00084e…` |
| `FLOWMASTER_VALIDATE_REVISION` | 3.2.15 | 3.2.15 | **3.2.16** |
| `validator_revision` | 3.2.13 | 3.2.13 | **3.2.14** |
| `SKILL_TREE_SHA256` | `8ed6d8b0…` | `740844f0…` | `eb9634d6…` |
| freeze digest | `13353ffe…` | `5da1c46b…` | `b9ca212a…` |

These bytes take a fresh, unspent identity on all three advertised values. `3.2.14` has never been
a `validator_revision` and `3.2.16` has never been a `FLOWMASTER_VALIDATE_REVISION`. The rule
R29-F1 rested on — *"corrected bytes must not reuse"* an identity bound to a published §10
verdict — is satisfied.

**A3, audited by grep rather than by reading the report.** `validator_revision: 3.2.14` appears at
**exactly four executable sites** — `references/…validation-profile.json:45`,
`scripts/run_gcfpe_20260914_fixtures.py:702`, `scripts/validate_gcfpe_20260914.py:1090`,
`scripts/validate_flowmaster.py:1221` — which is the "four sites" round 24 established.
`FLOWMASTER_VALIDATE_REVISION: 3.2.16` appears in **exactly one** declarative place, `SKILL.md:8`.
**Zero** stale `3.2.13` or `3.2.15` remain in any `.py` or `.json`.
`CHANGE_FLOW_SPECIALIZATION_REVISION` is `3.2.9` at all six sites; the single `2.0.0` is the
old→new key of the `maintenance_metadata` mapping, which is correct and must stay.

### R29-F2 — `**Lifecycle**: X` and neighbours evade the prefix strip → **FIXED, and over-delivered**

The matcher now removes emphasis and code marks from the whole line before stripping the
list/quote/heading lead-in. I re-ran every vector from rounds 28 and 29 and added my own:

| group | result |
|---|---|
| all 18 round-28/29 vectors (indent, tab, bold, bullet, quote, NBSP, nested `***`, italic, underscore, combined, nested quote, 4-space indent, authority line in every form) | **all CAUGHT** — no regression |
| the 9 my round-29 correction closed (`**Lifecycle**:`, `**Selection status**:`, `1.`, `1)`, `#`, `###`, `~~`, backticked key, table cell) | **all CAUGHT** |
| 8 of my own inventions (heading+bold, table+bold, `> 1. **Lifecycle**:`, `__Lifecycle__:`, mixed `~*_\``, deep-indent bullet, pipe prefix, authority in a table / backticked) | **all CAUGHT** |

**C2 is true**, and it goes further than round 29's fix did.

### The defect found while fixing them → repaired, and the control is the right one

C4 checks out exactly. **164 → 172, zero cases removed**, confirmed by comparing emitted case
*names*: eight new `reject-governance-state-*` cases for bold-label-only, italic-label, ordered
list, heading, code span, table cell, nested quote and authority-mid-sentence. The prose control
gained three lines, and they are well chosen — `## Selection and authority` is a **real corpus
line**, and `1. Resolve the current lifecycle from the owning register, not from this page.`
guards the exact ordered-list stripping this round introduced. That is the author testing the
surface they widened, which is what the previous two fixture rounds failed to do.

## Findings — all non-blocking

### R30-N1 — C1 claims more than is true, and more than these bytes could deliver

**Claim.** *"Rounds 28, 29 and 30 are now mutually distinguishable on all three advertised
values."*

**Measured.** False on the strict reading. Rounds 28 and 29 **still share**
`FLOWMASTER_VALIDATE_REVISION: 3.2.15` and `validator_revision: 3.2.13`. Only `SKILL_TREE_SHA256`
separates that pair. All three rounds are distinguishable *taken together*, because the tree hash
is distinct across all three — which is the charitable reading and is true.

**Not a finding against these bytes, and not repairable.** Rounds 28 and 29 are published,
immutable, and superseded. No round-30 change could make them differ from each other. More to the
point, the hazard I actually raised in R29-F1 is gone: both r28 and r29 carry the same outcome —
`SKILL_REPAIR_REQUIRED` — so confusing them costs nothing, and r30, the package that would be
installed, is distinct from both on every value.

**Correction, not repair.** The sentence should read that *round 30* is distinguishable from both
predecessors on all three values, and that rounds 28 and 29 remain separable only by tree hash.

### R30-N2 — C3's "no new false positives" is true of its controls and not of the surface

**Claim.** *"The fix creates no new false positives. 7 of 7 controls pass."*

**Measured.** The controls do pass — I ran the real-corpus ones myself and they pass. But the
false-positive surface **did** grow, exactly where A1 predicted. Four shapes now fire that did not
in round 29:

| line | r29 | r30 |
|---|---|---|
| ``- `Selection status:` — prohibited in a body`` | evades | **fires** |
| ``- `Lifecycle:` — prohibited`` | evades | **fires** |
| ``\| `Lifecycle:` \| prohibited \| register \|`` | evades | **fires** |
| ``## `Selection status:` is prohibited`` | evades | **fires** |

All four are the same shape: **a line that names the forbidden field while forbidding it**, as a
bullet, a table row, or a heading. Removing code marks from the whole line is what makes the
backticks stop protecting them.

**I hunted the corpus and did not find a real one.** I ran the shipped matcher over real lines from
the bodies I have read across three rounds and none fired, including the closest approaches —
`## Selection and authority`, "An unselected candidate … is not selection evidence", the register
prose, `session_disposition` lines, and bulleted lines carrying backticked identifiers. I read two
further bodies this round chosen for structural risk (`IA-10` in round 29, `QA-90` here, both with
heavy bulleted field lists) and both are clean. The corpus convention is to name fields as
backticked identifiers *inside* sentences, never as line-leading labels, and that convention is
what keeps the check safe.

**Distinct bodies now directly confirmed clean: 15 of 55** — the author's 7 from round 28, plus 8
read by me (`PR-35`, `CF-E-20`, `CL-30`, `GCFPE-MGMT-10`, `MGR-10`, `UTIL-10`, `IA-10`, `QA-90`),
with no overlap between the two sets. That is two more than `AF-004` records.

**Why non-blocking.** `AF-004` already names this exact risk — *"a field name inside a
`NEXT_PROMPT_HANDOFF` template block, for instance — the gate would begin failing on a corpus that
is fine"* — as Product Owner-deferred to the next `GCFPE-MGMT-10` run, with an owner. L1 states
plainly that round 30 widens what such a scan would catch and does not claim it closed. Nothing
runs this check automatically; it fires only under `--bodies-stdin`. No instance is observed.

**Correction, not repair.** C3 should say the controls pass and the surface grew, and should point
at `AF-004`, because the widening is a real input to that deferred item. If the scan ever does turn
one up, the fix is a narrow exception — require the key to be followed by a governance *value*, or
exempt a line that also contains a prohibition word — not a looser strip.

### R30-N3 — five vectors still evade, all requiring intent

Answering **A2**, which asks me to name what my round-29 correction left open and whether round 30
closed it. It closed none of those four, and they are the same four:

| vector | still evades | Notion produces it? |
|---|---|---|
| zero-width space `U+200B` | yes | no |
| BOM / ZWNBSP `U+FEFF` | yes | no |
| HTML entity `&nbsp;` | yes | no |
| `<b>Lifecycle:</b>` | yes | no |
| `#######` (7+ hashes) — `#{0,6}` caps at six | yes | no; not valid Markdown either |

**Does not matter, and I would not spend a round on it.** None is editor output; each requires
someone deliberately encoding a governance line to slip a check. That is not the threat model —
the threat is a line added in good faith, and every good-faith rendering is now caught. Recording
them so the next reviewer does not re-derive the list.

### R30-N4 — §8c undercounts the changed files by one

`flowmaster-validate` differs from round 29 in **five** files, not the four §8c enumerates:
`SKILL.md`, the validation profile, the fixture runner, `validate_gcfpe_20260914.py`, **and
`validate_flowmaster.py`**. That fifth diff is a single line — `"validator_revision": "3.2.13"` →
`"3.2.14"` — and is mechanically required by R29-F1's own fix, since `validate_flowmaster.py` is
one of the four revision sites.

The change is correct; the enumeration is not. Worth recording precisely because A3 says the
revision bump has *"now got it wrong twice"*: the instruction that verifies it should list all five
files, or the next person checking "and nothing else" will read a legitimate diff as an extra.

## §6 — answered explicitly

**A1 — hunt the corpus for a line that now fires and should not.** Answered as **R30-N2**. The
surface did grow and I characterised exactly how; I looked for a real instance and did not find
one; 15 of 55 bodies are now directly confirmed. I did not read all 42 remaining, and I am not
claiming `AF-004` closed — `AF-004` itself says a passing gate run and a `notion-search` query do
not close it, and I agree.

**A2 — name what still evades and decide whether it matters.** Answered as **R30-N3**: the same
four I named in round 29, plus `#######`. None matters.

**A3 — confirm the revision bump.** Done by grep, reported under R29-F1 above. Four executable
sites for `3.2.14`, one declarative site for `3.2.16`, zero stale `3.2.13`/`3.2.15` in code or
data, `CHANGE_FLOW_SPECIALIZATION_REVISION` still `3.2.9` at all six sites.

**A4 — is the SKILL.md narrative accurate or self-serving, and would it warn the next author?**
**Accurate, and unusually so.** It states the defect in bold rather than burying it, names the
concrete consequence (*"mutually incompatible: each rejects the other's profile"*, *"differ on
fifteen vectors"*), names why it escaped (*"No report emits the tree hash, so nothing downstream
could tell them apart"*), and then says the thing a self-serving paragraph would omit: **"Both
clauses were violated in the file that states them,"** with the rule quoted verbatim from four
paragraphs above. It does not credit the tree hash with saving it, does not describe the finding as
minor, and does not blame the reviewer for raising it. The commit title on `main` — *"the revision
rule, broken in the file that states it"* — carries the same framing.

Would it warn the next author? **Mostly.** It makes the failure concrete and puts it immediately
before the bump, which is the right place. Its one weakness is that it *narrates* rather than
*prescribes*: a reader learns the rule was broken twice but is not told what to do about it. One
imperative sentence — diff the advertised identity against the previous package before packaging,
and treat a match as a defect — would convert a good postmortem into a control. That is a
suggestion, not a finding.

**A5 — fixture arithmetic by name sets.** Confirmed: 164 → 172, delta 8, **removed: none**, and the
eight added are exactly the eight named. The three prose-control lines are additions to an existing
case rather than new cases, which is why the case count moves by 8 and not 11 — C4 is consistent.

## Gates — what I ran, and what I did not

All five, from the extracted contents, in a full sibling tree with the whole synced directory
restored around the two replaced skills, `PYTHONDONTWRITEBYTECODE=1` everywhere including every
`importlib` call.

| gate | flag | result | author's measurement |
|---|---|---|---|
| `flowmaster-validate/…/validate_gcfpe_20260914.py` | `ok` | `true`, `errors: []`, `SELECTED_PRODUCTION` | matches |
| `flowmaster-validate/…/run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` | `true`, **172** cases, §13 33/33 and 28/28, zero failures | matches |
| `flowmaster-validate/…/validate_flowmaster.py` | `suite_ok` | `true`, `FLOWMASTER_SUITE_PASS`, `self_identity: OK`, 0 findings/warnings/advisories | matches |
| `flowmaster-validate/…/validate_gcfpe_current.py` | `ok` | `true`, `errors: []` | matches |
| `change-flow/…/validate_gcfpe_20260914.py` | exit + text | `PASS` | matches |

**Every author measurement in §8 reproduced. I contradicted none of them.**

**What I could not run:** nothing. **What I chose not to re-run:** the graph rebuild from
`docs/graph/parts/`, on `change-flow` bytes that are identical to the ones I rebuilt in round 28
and reproduced at `90021eb7…`.

**Reuse declared, per §1 and §2.** `change-flow` is byte-identical to rounds 28 and 29 — `diff -r`
against the round-29 extraction reports **zero differences**, file by file, not merely an equal
digest. I am explicitly reusing my round-28 measurements on it: the three coupled-defect repairs,
the symmetric staging-binding branch, the promotion transition and the graph rebuild. I re-ran what
is behavioural: its own gate `PASS`, `EXPECTED_GRAPH_SHA` recomputed and matching, both bundled
contract copies and both graph copies byte-identical.

## Identity, pins, and the void check

| tree | files | digest | §3 |
|---|---|---|---|
| baseline `change-flow` (installed, still round-27) | 21 | `14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` | matches |
| baseline `flowmaster-validate` | 29 | `9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833` | matches |
| repaired `change-flow` | 21 | `80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8` | matches |
| repaired `flowmaster-validate` | 29 | `b9ca212ac1275f16af12d34ad15d3df6e95fc71a95f2ce1ab56ee7245a3317af` | matches |

The baseline reproduces, so the review proceeded. Every archive entry sits under its own skill
root; no traversal sequences, no absolute paths; `name:` unchanged in both.

**All pins unmoved (§8f):** contract `2b78f877…` / 606657, graph `90021eb7…` / 569835, the
contract's `source_snapshot` pin, both profile blocks, both `EXPECTED_*` constants, and
`change-flow`'s `EXPECTED_GRAPH_SHA`. Both bundled copies of each artifact byte-identical. The
profile still carries `selection_status_during_staging` and not the bare name, so round 28's F2
repair is intact.

**The tree did not move under me.** The installed digests were still `14981ba7…` and `9c0ca6fe…` at
the end. Nothing was installed. The synced directory contains zero `.pyc`, zero `__pycache__`, and
zero files changed inside either reviewed skill. **No bytecode was written anywhere in scratch.**

## Procedural note

No prompt drift this round: the copy I was handed is **byte-identical** to the repository's
(`688baee4…`, 10325 bytes, zero diff), and my round-29 record landed on `main` **verbatim** — I
diffed it against the commit I pushed.

§4's branch `docs/20260922-gcfpe-round30` did not exist when I looked; it had merged as **#449** and
been deleted, exactly as `docs/20260921-prompt-body-policy` had merged as #445 the round before. I
read the evidence on `main` at `2efd4e1`. Nothing in §4's file list was missing. This is now the
second consecutive round where the named branch was gone by review time; pointing the next prompt at
`main`, or naming the merge PR alongside the branch, would remove the step.

## What is needed

Nothing blocking. The two corrections above are to the round-30 report's claims, not to the
packages, and belong in a successor record rather than an edit to it. If C1 and C3 are restated, say
that round 30 is distinguishable from both predecessors while rounds 28 and 29 remain separable only
by tree hash, and that the false-positive surface grew in a characterised way that feeds `AF-004`.

`AF-004` remains open, correctly, with its Product Owner deferral and its owner. It is now more
worth running than it was: the matcher it would exercise catches every good-faith rendering, so a
sweep would produce a real answer in both directions rather than a partial one. I have moved it from
13 of 55 to **15 of 55** directly confirmed; the other 40 have still never been looked at.

---

NOTHING NEEDED
