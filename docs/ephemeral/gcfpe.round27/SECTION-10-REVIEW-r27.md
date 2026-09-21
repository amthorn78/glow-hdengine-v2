---
artifact_type: SKILL_FIT_SECTION_10_VERDICT
artifact_version: "1.0"
created_date: 2026-09-21
author: SFR-01
release: GCFPE-20260914.1 / 091426.1 / 55
round: 27
subject: Independent §10 validation of the round-27 flowmaster-validate package cb3c6286…
supersedes: nothing — successor record to docs/ephemeral/gcfpe.round26/SECTION-10-REVIEW.md
---

# §10 verdict — round 27 (round 26's four findings repaired)

## Verdict

**`SKILL_FIT_CONFIRMED`**, with three non-blocking findings.

Bound to exactly:

    flowmaster-validate.skill   29 files, 284588 bytes
    sha256 cb3c628662a19b77b235634c77e2eac0e24e6d304debb8bb15ef573f1c727bfd
    extracted tree digest (freeze.py, rooted at the skill directory)
    29 9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833
    SKILL_TREE_SHA256 6f682315a9437c1275688d568ee8b79baeccdd52f9c896b89fdd617a46863a93

**This verdict is void for any other bytes.**

All four of my round-26 blocking findings are **fixed**, and each repair survives falsification in
someone else's hands. The fifth, non-blocking one is fixed too, and the report correction I asked
for was made and independently re-measured to the byte. The three findings below are new, all
minor, and none of them defeats a claim this round makes.

The thing that mattered most: I ran the documented procedure against a prompt body **the author did
not choose** — `CF-C-20`, a CF Specification author whose obligations `SF10-10` deliberately
changed — and it returned `ok: true`. Round 26 failed this exact test on the first body tried.

## Identity, before anything else

| check | measured here |
|---|---|
| package bytes / sha256 | **284588** / **`cb3c6286…`** — matches §1 |
| 29 entries, all under `flowmaster-validate/`, no traversal | **yes** |
| SKILL.md frontmatter vs installed | **identical** |
| extracted tree | **`29 9c0ca6fe…`** — matches §3 |
| installed `flowmaster-validate` (the baseline) | **`29 f170a01c…`** — matches §3 |
| installed `change-flow` | **`21 14981ba7…`** — matches §3 |
| declared `SKILL_TREE_SHA256` | **`6f682315…`** — matches §1, and the tree measures it |

§3 is correct in every particular. Both installed digests reproduce **unchanged after every
experiment below**. Nothing installed, nothing written to the synced skills directory, zero `.pyc`.

**One movement under me, disclosed.** `pe35/round27` advanced from the named commit `3c973394` to
`1f6b307`; the delta is one file, `REVIEWER-PROMPT-r27.md` itself, added after the commit it names.
No packaged byte, no `REPORT-r27.md`, no patch moved. The review is not void. This is the third
round running in which the prompt names the commit that precedes its own addition — harmless, but
it is now a pattern rather than an accident.

**§8f.** Exactly the nine files `round27.patch` names differ from the installed skill. The patch
applies clean at `-p1`, no `.rej`, no `.orig`, and the result is **byte-identical** to the package
(`diff -r` clean, digest `9c0ca6fe…`).

## Disposition of my four round-26 findings

| finding | disposition | how I established it |
|---|---|---|
| **F1** — the all-55 requirement moved rather than left | **FIXED** | `ARTIFACT_AVAILABILITY_BODY_SET` and `require_complete` are gone from all code; the only surviving mentions are one comment and dated SKILL.md prose. One real body now returns `ok: true` |
| **F2** — coverage silent exactly when coverage is zero | **FIXED** | `None` → `['ALL_BODY_LEVEL_CHECKS']`; `{}` → `['QA_PASS_CLASS_MAP_AND_INTAKES']`. The two cases are now distinguished, via `bodies is not None` at line 2581 |
| **F3** — SKILL.md documented the forbidden corpus | **FIXED** | The operator block no longer names `--prompt-dir`; it states the suite "reads no prompt bodies" and documents the `--bodies-stdin` procedure, including *"read those two fields, never `ok` alone."* The two surviving `--prompt-dir` mentions are dated prose recording the removal |
| **F4** — the suite never checked self-identity | **FIXED** | One byte appended to an unrelated script: **all three** gates now exit 1, and `validate_flowmaster` returns `FLOWMASTER_SUITE_FAIL`, naming `SKILL_SELF_IDENTITY:DECLARED_6f682315a943_MEASURED_52c2601243c5` |
| **Finding 5** (non-blocking) — duplicate declarations erased | **FIXED** | A second declaration line now returns `SKILL_SELF_IDENTITY:MULTIPLE_DECLARATIONS:2` |
| **Nit** — "the package is smaller" | **CORRECTED** | The report retracts it and re-measures. My figures: round 26 1,764,361, installed 1,756,991, round 27 **1,769,023**. The author's re-measurement matches mine exactly |

## Conformance to the Prompt Corpus Storage and Fidelity Policy

Stated separately from correctness, as §10 requires.

**Conforms.** No GCFPE path walks, constructs or requires a local corpus; there is no path option
for bodies anywhere in the GCFPE validators; all body hashing remains absent; `SKILL.md` now
instructs read-from-Notion-and-pipe and warns against reading `ok` alone. The behaviour a
conforming operator will meet is conforming, which is what round 26 could not say.

**One residue, not a breach of behaviour.** `validate_strength_middleware.validate_prompt_snapshot`
and `validate_epic_alpha.validate_snapshot` still exist, still `glob('*.md')` over a prompt
directory and still gate on a complete member set. They are unreachable — the `--prompts` flag now
returns `PROMPT_SNAPSHOT_DIRECTORY_RETIRED` and never calls them — but the policy says a
conflicting *element* is defective, not merely a conflicting execution. Finding 1 below.

**My own conduct.** No prompt corpus was created at any point, temporary or otherwise. The two
bodies I read (`CF-C-20`, and the earlier `IA-10` re-read is not repeated here) went from Notion
into a pipe and were never written to a file. Scratch holds no body and no body hash.

## Gates: which I ran, and the one I could not

From the **extracted package** with the untouched siblings restored, scratch copy,
`PYTHONDONTWRITEBYTECODE=1`:

| gate | result |
|---|---|
| `validate_gcfpe_20260914.py change-flow --contract …` | exit 0, `ok: true`, `not_evaluated: ['ALL_BODY_LEVEL_CHECKS']` |
| same, `--bodies-stdin` with `{}` | exit 0, `ok: true`, `not_evaluated: ['QA_PASS_CLASS_MAP_AND_INTAKES']` |
| same, with **`CF-C-20`'s real Notion text** | **exit 0, `ok: true`, `validated: ['CF-C-20']`, 0 errors** |
| `run_gcfpe_20260914_fixtures.py change-flow --contract …` | exit 0, **155 cases, 0 failed**, `suite_ok: true`, rev `3.2.12` |
| `validate_flowmaster.py` | exit 0, **`FLOWMASTER_SUITE_PASS`**, 0 blockers/errors/warnings/advisories |
| `validate_gcfpe_current.py change-flow` | exit 0, `ok: true`, 0 errors |
| `change-flow/scripts/validate_gcfpe_20260914.py` | exit 0, `PASS` |
| §8d tamper, all three gates | **all exit 1** |
| §8e second declaration line | `MULTIPLE_DECLARATIONS:2` |
| `.pyc` written | **zero** |

**Not run: the three-body QA-closure path against real pages.** `L1` says the author did not test
it; neither did I. It needs `QA-120`, `CL-E-10` and `CL-C-10` — about 86 KB of page text through a
session for one assertion. I confirmed by code reading that the trio gate is reached only when all
three ids are supplied and otherwise lands in `not_evaluated`, and the `{}` run demonstrates that
branch. The path itself remains unexercised on real text by anybody. It is the last untested thing
in this interface and it should be someone's next single command, not another round's `L1`.

## The claims

| claim | disposition |
|---|---|
| **C1** no remaining code path requires a complete body set | **confirmed** — see A1 |
| **C2** `None` → `ALL_BODY_LEVEL_CHECKS`; `{}` and partial sets → specific checks | **confirmed by execution** |
| **C3** no operating instruction for `--prompt-dir` survives | **confirmed** |
| **C4** `validate_flowmaster` and `validate_gcfpe_current` both refuse a tampered tree | **confirmed** |
| **C5** exactly one declaration permitted | **confirmed** |
| **C6** the two dormant snapshot validators are retired | **partially** — the flag is retired, the functions are not. Finding 1 |
| **C7** hash-pin chain, `change-flow` and 3.2.8 unmoved | **confirmed** |
| **C8** the procedure was executed end-to-end before packaging | **confirmed, and independently repeated on a different body** |

## The attack (§6)

### A1 — search the whole skill for any surviving complete-set assertion

**None of them is a corpus requirement.** I grepped every set-equality, superset and length
assertion in all 19 scripts rather than the two the author names, and classified each:

- `validate_gcfpe_20260914.py` lines 1173, 1198, 1387, 1389, 1391, 1549, 1802 and
  `validate_gcfpe_current.py` 195, 335 compare the **graph, registry, manifest, member list,
  state_routes and obligation scope** against `EXPECTED_MEMBERS`. These read the contract and the
  graph, need no bodies, and are the membership authority the deleted `PROMPT_BODY_MEMBER_SET`
  correctly deferred to. Legitimate contract checks.
- The body path itself contains **no** roster assertion. Its only use of `EXPECTED_MEMBERS` is the
  per-prompt lookup `if prompt_id not in EXPECTED_MEMBERS` — "is this id a member", not "are all
  members present". There is no `set(bodies)` or `set(texts)` comparison anywhere.
- `validate_strength_middleware.py:100` and `validate_epic_alpha.py:272` do hold complete-set
  assertions over a globbed prompt directory — but in functions nothing calls. Finding 1.

`ARTIFACT_AVAILABILITY_BODY_SET` and `require_complete` are absent from all executable code. F1 is
genuinely gone, not relocated again.

### A2 — is retiring a path by error return honest, or merely quiet-looking?

**The error return is honest; leaving the functions behind is not the whole job.** Returning
`PROMPT_SNAPSHOT_DIRECTORY_RETIRED` and setting `ok: false` is better than silently ignoring the
flag: an existing caller that passes `--prompts` gets a hard, named failure rather than a quiet
behaviour change, which is the right treatment for a retired interface. I would not prefer dropping
the flag entirely — an unrecognised-argument error tells the caller less than a named retirement
does.

What is not done is the removal itself. The glob and the member-set gate are still in the file,
reachable by anyone who imports the module or restores one line of CLI wiring. My round-26 answer
to `Q1` asked for both halves; this is the first. Finding 1.

### A3 — attack the self-identity coupling

Three of four attacks fail closed; the fourth exposes an inherent limit, and the coupling itself
costs the suite a diagnostic.

| attack | `validate_flowmaster` | `validate_gcfpe_current` |
|---|---|---|
| `validate_gcfpe_20260914.py` deleted | exit 1 | exit 1 |
| renamed | exit 1 | exit 1 |
| syntax-broken | exit 1 | exit 1 |
| **`validate_self_identity` neutered to `return []`** | **exit 0** | **exit 0** |

The fourth is not a defect to fix: a self-check cannot survive its own removal, and any package
that can be edited can have its checker edited. It does bound what the mechanism proves.

The first three fail closed but **by uncaught `ModuleNotFoundError` traceback**, not by a named
error — and `validate_gcfpe_20260914.py` is in `REQUIRED_SCRIPTS`, so the suite had already computed
a named missing-script finding and then crashed at line 1439 before printing it. Finding 2.

**The limit that matters for `Q2`, measured.** A *coherent wrong package* passes its own check.
I ran round 26's rejected package against its own `validate_self_identity`: **no error**. So
`SKILL_TREE_SHA256` detects a **tampered or partially installed** tree, not the **wrong package**
case that motivated it — install any internally consistent superseded build and it certifies
itself. The only control for wrong-package is comparing the digest against the one in the §10
verdict, and the gate does not print a digest to compare: `validate_flowmaster` reports
`self_identity: "OK"` and nothing else. Finding 3.

### A4 — is `ALL_BODY_LEVEL_CHECKS` enough?

**Adequate for a person, inconsistent for a machine.** As English it is unambiguous: nothing
body-level ran. My concern is narrower — the field now carries two different kinds of value. With
`{}` or a partial set it lists *check names* (`QA_PASS_CLASS_MAP_AND_INTAKES`); with no bodies at
all it carries a *category sentinel*. A consumer cannot treat entries uniformly, and a future
reader may take `ALL_BODY_LEVEL_CHECKS` for the name of a check that exists.

I would not enumerate every body-level check for the zero-body case — that is a long list whose
content adds nothing over the sentinel, and it would bury the specific names in the cases where
they matter. I would document the sentinel where the field is described, or prefix it
(`ALL:BODY_LEVEL`) so its different kind is legible. This is a judgement call, not a finding.

### A5 — a body the author did not pick

**Closed, and it passes.** `CF-C-20` — *Create CRD Specification*, one of the four CF Specification
authors `SF10-10` exempted from the current-PF10 obligation — read from Notion (page
`3db4590a05eb8173a73edc73f302a90a`, `page_last_edited_at` 2026-09-18T03:06:03Z), piped in, never
written to disk:

    ok: true   errors: []   validated: ['CF-C-20']   not_evaluated: ['QA_PASS_CLASS_MAP_AND_INTAKES']

A pass proves nothing unless the check can fail, so I bracketed it: a synthetic body carrying
`CF-C-20`'s real identity headers but no handoff literal returns
`['PROMPT_HANDOFF_LITERAL:CF-C-20', 'PROMPT_HANDOFF_RECEIVER:CF-C-20:CF-C-10',
'PROMPT_HANDOFF_RECEIVER:CF-C-20:CF-C-30']`. The per-prompt path is live on this id and the real
page satisfies it. `SF10-10`'s exemption is visible in the same run: `CF-C-20` owes no entries in
`EXPECTED_BODY_OBLIGATION_IDS` while sitting in `EXPECTED_WRITERS`.

### A6 — revision recount and contract identity

**Confirmed.** `validator_revision` is `3.2.12` at exactly **four** value-bearing sites:
`references/…validation-profile.json:45`, `scripts/run_gcfpe_20260914_fixtures.py:664`,
`scripts/validate_gcfpe_20260914.py:1063`, `scripts/validate_flowmaster.py:1221`.
`FLOWMASTER_VALIDATE_REVISION` is `3.2.14` at its single assignment, `SKILL.md:8`.
`CHANGE_FLOW_SPECIALIZATION_REVISION` is untouched at **3.2.8** at every asserting site and in the
installed `change-flow/SKILL.md:8`. **No** `3.2.9`, `3.2.10`, `3.2.11` or `3.2.13` survives as a
live identity in any script or data file — correct, since each is bound to a package a published
verdict describes. The candidate contract measures **610549 bytes / `1c3c7969…`** and `cmp` shows
the two bundled copies **byte-identical**.

## Findings

### Finding 1 — the retired snapshot validators are unwired, not removed (non-blocking)

*Artifact:* `flowmaster-validate/scripts/validate_strength_middleware.py` lines 98–100
(`validate_prompt_snapshot`) and `flowmaster-validate/scripts/validate_epic_alpha.py` lines 271–273
(`validate_snapshot`).

*Defect.* `C6` says the two dormant validators are retired. The CLI is: `--prompts` returns
`PROMPT_SNAPSHOT_DIRECTORY_RETIRED` and fails the run. The functions are not: both still hold
`glob('*.md')` over a prompt directory, a `set(paths) != SUBSTANTIVE|{ANALYZER}` complete-set gate,
and a `read_text()` loop over every file found.

*Evidence.* Grep of the package: `validate_strength_middleware.py:99-100` and
`validate_epic_alpha.py:272-273` are present and unchanged in shape; no caller remains in either
file. The policy's clause is about elements, not only executions: *"If an existing skill, prompt,
validator, plan, or proposed repair conflicts with this policy, treat that element as defective."*

*Why it is not blocking.* Nothing reaches them, no documentation mentions them, and the behaviour
an operator meets is conformant. This is a residue with a latent cost — the next author who needs a
body-level check finds a working corpus walker — rather than a live defect.

*Smallest correction.* Delete both functions. They are dead code with no GCFPE caller, so removal
cannot regress a gate. Keep the flag's named error return; that part is right.

### Finding 2 — the self-identity import costs the suite its own missing-script diagnostic (non-blocking)

*Artifact:* `flowmaster-validate/scripts/validate_flowmaster.py:1439` and
`flowmaster-validate/scripts/validate_gcfpe_current.py:663` — bare
`from validate_gcfpe_20260914 import validate_self_identity`, no guard.

*Defect.* `validate_gcfpe_20260914.py` is listed in `REQUIRED_SCRIPTS` for `flowmaster-validate`, so
its absence is a condition the suite already detects and names. But the unguarded import raises
`ModuleNotFoundError` at line 1439, after `missing` has been computed and before the report is
printed, so the operator gets a Python traceback instead of the finding the suite had in hand.

*Evidence.* With `validate_gcfpe_20260914.py` deleted, both gates exit 1 with
`ModuleNotFoundError: No module named 'validate_gcfpe_20260914'` and no JSON report. Renaming and
introducing a syntax error produce the same shape.

*Why it is not blocking.* It fails closed. Exit 1 on a tree missing a required script is the right
outcome, and no tampered tree passes through this hole.

*Smallest correction.* Wrap the import and emit a named error —
`SKILL_SELF_IDENTITY:CHECKER_UNAVAILABLE` — so the run still prints its report, including the
`REQUIRED_SCRIPTS` finding that explains why.

### Finding 3 — the gate never prints the digest the canonical rule says to compare (non-blocking)

*Artifact:* `flowmaster-validate/scripts/validate_flowmaster.py:1441`,
`report["self_identity"] = self_identity or "OK"`; no measured digest in any report.

*Defect.* `SKILL_TREE_SHA256` verifies a tree against **its own** declaration. A coherent wrong
package therefore certifies itself, which I measured: round 26's rejected package, checked against
its own declaration, returns no error. The mechanism catches a tampered or partially installed
tree; it does not catch the wrong-package case that motivated it, and the Operations Hub rule it
implements — *An install is not complete until its digest is compared* — is satisfied only by
comparing the installed digest against the digest in the §10 verdict. That comparison needs a
number, and the gates emit `"OK"`.

*Evidence.* `validate_flowmaster`'s clean run reports `self_identity: 'OK'`;
`validate_gcfpe_20260914`'s report carries `contract_sha256` and `frozen_graph_sha256` but no tree
digest. To perform the canonical comparison today an operator must open `SKILL.md` by hand.

*Why it is not blocking.* `C4` claims only that the gates refuse a tampered tree, and they do. The
overclaim is in round 26's framing and the Hub rule's wording, not in this round's stated claims.

*Smallest correction.* Emit the measured digest — `"self_identity": {"declared": …, "measured": …}`
or a `skill_tree_sha256` field — in all three reports, so the post-install comparison can be done
from gate output rather than from a file read. One line each, and it turns the procedure into
something a person can actually execute.

## The three questions

### Q1 — what should the promotion packet cite as body-level evidence? *(carried from round 26)*

**Per-prompt provenance, never a corpus-wide count.** For each page actually read: the prompt id,
the Notion page id, the page's `page_last_edited_at`, the release and prompt version it was read
under, the validator revision, and the outcome — then, explicitly, the contents of
`prompt_body_checks_not_evaluated`. That is reproducible without a mirror, because anyone can
reopen the page and see the same last-edited timestamp, and it states what was examined instead of
asserting a number over pages nobody can re-derive.

My round-26 answer noted this was not yet *possible*, because a packet citing validated prompts
would have had to cite a run that returned `ok: false`. That blocker is gone: the `CF-C-20` run
above is exactly the citation shape a packet should carry. `"0 errors across 55 bodies"` should not
be revived in any form; if a decision genuinely needs corpus-wide assurance, that is a dated,
scoped, Product Owner-authorised sweep reported per prompt, recorded as a point-in-time review and
never as a standing gate.

### Q2 — should `SKILL_TREE_SHA256` be adopted by the other skills? *(carried from round 26)*

**Yes — declare it everywhere, verify it centrally — and this round's measurement changes what
that buys you.** The hazard is structural: every skill installs under a filename the packager must
reuse, so any can be replaced by a superseded build. `flowmaster-validate` is only special in
having a runtime that can refuse; the others have none, so inventing one in each is a lot of
machinery for an install-time property. The right shape remains the split: each skill declares
`SKILL_TREE_SHA256` in its `SKILL.md`, and `flowmaster-validate` — which already walks every
sibling `*/SKILL.md` in four places — measures each sibling tree and fails the suite on any
mismatch.

What I now know that I did not in round 26: **self-declaration alone does not catch a wrong
package**, because the wrong package declares itself correctly. Central verification is therefore
not a convenience, it is the part that works — a sibling's declaration checked by an instrument
that is not that sibling is a real control, whereas a skill vouching for itself is not. And it
still does not close the case where `flowmaster-validate` *itself* is the wrong package; only the
digest comparison against the §10 verdict does that, which is why Finding 3 matters more than its
severity suggests. Fix Finding 3 and adopt the declaration everywhere; verify siblings here.

### Q3 — is a fixture suite with no body-level cases still adequate? *(new)*

**No. The body path needs fixtures of its own, and they should be built from synthetic bodies.**
155 contract cases are honest about what they cover, and dropping the 26 mirror-dependent cases was
correct — they required the corpus. But the result is that the one code path this round rewrote is
the one path with no regression test. `F1` and `F2` were both defects in that path, both survived
the author's review, and both were caught only by a human running one command by hand. That is not
a test strategy.

Synthetic bodies are the answer and they are policy-clean: the policy forbids mirroring **the
corpus**, and a fabricated body carrying an id header and a handoff literal is not a prompt and
not a copy of one. I demonstrated the shape twice in this review without touching disk — a
constructed `CF-C-20` body that fires exactly three expected errors, and a `QA-120` class-map
producer built from the row regex in round 26. Fixtures worth having: zero bodies →
`ALL_BODY_LEVEL_CHECKS`; one body → validated, trio not evaluated; the full trio → the closure
checks actually run; a key/header mismatch; an unexpected id; each per-prompt obligation firing and
not firing. All in-memory, none of them a corpus, and every one of them would have caught this
round's predecessors.

## What I did not do

No skill installed. Nothing written to the synced skills directory — both installed digests
reproduce unchanged after every experiment. Nothing merged, no auto-merge. **No prompt corpus
built, temporary or otherwise**; the one body read for `A5` went from Notion into a pipe and was
never written. No edit to `docs/pfcanon/**`. No prompt body changed in Notion. No QA verdict,
acceptance, closure or PF movement.

## What this needs

Nothing blocking. The package is fit to install on this verdict, and installing it is the Product
Owner's call.

The three findings are all small and can ride the next package rather than forcing one: delete two
dead functions, guard two imports, and emit the measured digest in three reports. Finding 3 is the
one I would not leave indefinitely — until the gates print a digest, the canonical post-install
comparison is a procedure with no instrument behind it, and that is the failure this whole sequence
began with.

If the Product Owner installs, the install is complete only when the installed tree is measured and
compared with `9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833` — the digest this
verdict binds to — and not merely when the gates come back green.

**DECISION NEEDED** — whether to install `cb3c6286…`, and whether the three non-blocking findings
ride a later package or are folded in before installation.
