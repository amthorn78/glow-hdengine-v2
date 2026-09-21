---
artifact_type: SKILL_FIT_SECTION_10_VERDICT
artifact_version: "1.0"
created_date: 2026-09-21
author: SFR-01
release: GCFPE-20260914.1 / 091426.1 / 55
subject: Independent §10 validation of the round-25 flowmaster-validate package (SF10-12)
supersedes: nothing — successor record to docs/ephemeral/gcfpe.round24/SECTION-10-REVIEW.md
---

# §10 verdict — round 25 (`SF10-12`, body-identity pins)

## Verdict

**`SKILL_REPAIR_REQUIRED`**, on two findings. A third is non-blocking.

Bound to exactly:

    flowmaster-validate.skill   29 files, 284004 bytes
    sha256 7cf4298c43d515c33c8d9fc4b4dc5892e421d39c740b495f8ae42356f3cd231a
    extracted tree digest (freeze.py, rooted at the skill directory)
    29 90e9d405061c3975884056d067ec595e533c6c35dcc9702bd67bcd4cd58410dc

**This verdict is void for any other bytes.** It is not a verdict on `e8f30b9a…`, which my
round-24 record still confirms and which is what is running; it is not a verdict on a repaired
successor. Both findings are small, confined to files this package already moves, and require
no movement in `change-flow`.

The change is right in substance. The gap `SF10-12` closes is real, I reproduced it against the
installed validator, and the 55 pins are exactly the registry's recorded values with nothing
invented. What fails review is not the check — it is the two records that tell an operator what
the check means: the convention under which the pins reproduce, which the shipped profile states
wrongly, and the error code the check emits, which it shares with an unrelated guard.

## What is installed, measured

Two records have been wrong about this, so I derived it before reading anything else.

| tree | measured here, `freeze.py` rooted at the skill directory |
|---|---|
| installed `flowmaster-validate` | **`29 f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd`** |
| installed `change-flow` | **`21 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2`** |

`f170a01c…` is round 24's package — the bytes my own round-24 record confirmed as
`e8f30b9a…` / 279481 and measured as this same tree digest. **§3's claim about the install state
is correct**, and so is `INSTALL-STATE-CORRECTION.md`. The round-24 package was installed; the
tree is one round behind, previously reviewed, not unreviewed. `REPORT.md`'s package table still
labels the pre-round-24 tree `5dcb95a9…` as "baseline — installed `flowmaster-validate`"; that
label is wrong and `INSTALL-STATE-CORRECTION.md` is the correction of record.

Both digests reproduce **unchanged after every experiment below**. Nothing was installed, nothing
was written to the synced skills directory, and zero `.pyc` were written anywhere. No skill moved
under me: `origin/pe35/round25-review` was `0856a9c` when I began and `0856a9c` when I finished.

## Gates I ran, and the one I could not

Run from the **extracted package** with the untouched sibling skills restored, on a scratch copy,
`PYTHONDONTWRITEBYTECODE=1`:

| gate | result |
|---|---|
| `validate_gcfpe_20260914.py change-flow --contract …` (no `--prompt-dir`) | exit 0, `ok: true`, 0 errors, `prompt_bodies_validated: false` |
| `run_gcfpe_20260914_fixtures.py change-flow --contract …` | exit 0, **155 cases, 0 failed**, `validator_revision: 3.2.10` |
| `validate_flowmaster.py` | exit 0, **`FLOWMASTER_SUITE_PASS`**, 0 blockers/errors/warnings/advisories, `validator_revision: 3.2.10` |
| `validate_gcfpe_current.py change-flow` | exit 0, `ok: true`, 0 errors |
| `change-flow/scripts/validate_gcfpe_20260914.py` | exit 0, `PASS` |
| `.pyc` written | **zero** |

**Could not run: the complete 55-body end-to-end gate, and the 181-case body-fixture suite.**
No body corpus exists on disk — the registry says so and I confirmed it — and rebuilding one
requires round-tripping 1,060,573 bytes of Notion page text through a session by hand, where a
single transcription slip is indistinguishable at first sight from corpus drift. The Product
Owner's own constraint on this work was that pinning must not require pulling all 55 bodies
through a session. I did not, so I do **not** confirm the author's "55 bodies, 0 errors" or
"181 cases, 0 failed" lines; they are unverified here, not contradicted. The 121 artifact-timing
and body-fixture cases that need the corpus are likewise unrun.

In place of it I ran the checks the corpus was needed for, directly and on real bytes: two bodies
fetched from Notion today and reconstructed byte-exactly, and a 55-member corpus in which those
two are genuine and the other 53 are header-valid stubs. That is enough to drive
`validate_prompt_bodies` end to end in both the installed and the packaged validator and to
compare them, which is what `A4` asks for.

## 1. Identity, scope and the patch

| claim | reproduced from the artifact |
|---|---|
| package sha256 / byte count | `7cf4298c…` / 284004 — **yes**, from the bytes I was given |
| extracted tree | `29 90e9d405…` — **yes** |
| installed tree | `29 f170a01c…` — **yes** |
| unchanged `change-flow` | `21 14981ba7…` — **yes** |

Package hygiene: 29 entries, every one under `flowmaster-validate/`, no traversal component, no
absolute path, no entry outside the skill root. `name: flowmaster-validate` present in SKILL.md
frontmatter.

**`C8` — confirmed.** Exactly five files differ between the installed skill and the extracted
package, and they are the five names in `round25-from-installed.patch`. Applied `-p1` to a copy
of the installed skill it applies clean, with no `.rej` and no `.orig`, and the result is
**byte-identical** to the package (`diff -r` clean, digest `90e9d405…`). Nothing rides along.
`round25.patch` does not apply to the installed tree, as §4 says.

## 2. The claims

| claim | disposition |
|---|---|
| **C1** a corrupted body passed the whole gate silently before this round | **confirmed — measured on the installed validator, seven ways** |
| **C2** all 55 identities were already recorded; nothing invented | **confirmed for all 55 against the registry; re-fetched 2 of 55 from Notion, both reproduce** |
| **C3** the pins belong in the profile, not the candidate contract | **confirmed, and the reasoning holds independently of cost — see A3** |
| **C4** exactly one trailing newline stripped, nothing else normalised | **confirmed as behaviour; the convention it is justified by is misstated — Finding 1** |
| **C5** absent pins are an error; the profile parameter is required | **confirmed** |
| **C6** everything round 24 confirmed survives unaltered but the one comment | **confirmed** |
| **C7** `validator_revision` → 3.2.10, `FLOWMASTER_VALIDATE_REVISION` → 3.2.12 | **confirmed, and the rule extension is right** |
| **C8** the delta is exactly those five files | **confirmed** |

**`C1`, measured against the installed validator rather than argued (`A4`).** I built a 55-member
corpus holding the two real bodies, corrupted one at a time, and ran the *installed*
`validate_prompt_bodies` and the *packaged* one over the identical directory.

| corruption of a pin-exact body | installed validator | packaged validator |
|---|---|---|
| one byte appended | **no error** | `PROMPT_BODY_IDENTITY:CF-C-10` |
| a second trailing newline | **no error** | `PROMPT_BODY_IDENTITY:CF-C-10` |
| every line ending converted to CRLF | **no error** | `PROMPT_BODY_IDENTITY:CF-C-10` |
| the literal `<content>` slice, `\n`+body+`\n` | **no error** | `PROMPT_BODY_IDENTITY:CF-C-10` |
| one trailing space added | **no error** | `PROMPT_BODY_IDENTITY:IA-60` |
| pristine | no error | no error |

Seven corruptions of a real body, invisible to the running validator. `C1` is true, and it is
now a measurement on the installed tree rather than an inference from a removed check.

**`C2`, checked against the registry rather than the report.** I parsed all 55
`evidence_contract` rows out of `project-prompt-contract-registry.md` and compared them with the
profile's `prompt_bodies.members`: the key sets are equal, all 55 byte counts and all 55 SHA-256
values are identical, none is absent, none is extra, and the recorded total reconciles at
**1,060,573 bytes**. Nothing was invented and nothing was adjusted. `A2` below covers the
freshness question the registry values cannot answer.

**`C6`, enumerated rather than assumed.** The whole delta is 12 hunks across the 5 files: one
revision line and one new dated paragraph in `SKILL.md`; the `prompt_bodies` block and
`validator_revision` in the profile; the corrected fixture comment and `validator_revision` in
the fixture runner; `validator_revision` in `validate_flowmaster.py`; and in
`validate_gcfpe_20260914.py` the profile pin, the signature, the new check and its call site.
Nothing else moved. Key-by-key on the profile: **zero keys removed, exactly one changed**
(`validator_revision`, 3.2.9 → 3.2.10), 113 added and every one under `prompt_bodies`. The
round-24 coupling still holds: reverting the profile alone to 3.2.9 returns
`ok: false, errors: ['PROFILE_IDENTITY']`.

**`C7`.** The rule is right and I would apply it the same way. 3.2.9 and 3.2.11 are the identities
my published round-24 verdict describes; `e8f30b9a…` is now both an installed build and a
verdict subject, so the increment is unambiguous. Note the consequence for the repair this
verdict requires: 3.2.10 and 3.2.12 are now identities *this* published verdict describes, so
repaired bytes must move again, to **3.2.11** and **3.2.13**.

## 3. The attack (§6)

### A1 — `C4`, the normalisation, which is the weakest point

**The stripping behaviour is right. The convention the package records for it is wrong, and that
is Finding 1.**

The behaviour first, measured: exactly one trailing `\n` is tolerated and nothing else. A second
blank line, a trailing space, CRLF endings and the literal two-newline slice all fail, as the
table above shows. Stripping one trailing newline hides exactly one thing — whether the file that
holds a body ends in a newline — which is a property of the file and not of the page, so hiding
it is correct. Not stripping it would make the check unusable in the ordinary case, because a
file written from the slice normally ends in one.

There is one residual ambiguity, worth recording but not worth blocking on: the strip is
unconditional, so a body whose own last byte is `\n` cannot be held in a file ending in exactly
one newline — such a file would hash one byte short. Neither of the two bodies I fetched ends in
a newline, and the fetch rendering does not appear to produce one, so I did not observe it.

The convention is the defect. I fetched `CF-C-10` from Notion today and reconstructed it
byte-exactly, then hashed all four candidate readings:

| reading | bytes | sha256 |
|---|---|---|
| **strip both boundary newlines** (registry's `in_force`) | **7203** | **`41dce73a…` — the pin, exactly** |
| the literal slice, `\n`+body+`\n` | 7205 | `5e32802d…` |
| leading newline dropped only, body+`\n` | 7204 | `ed9aba9c…` |
| trailing newline dropped only, `\n`+body | 7204 | `cb122f3e…` |

Only strip-both reproduces. The profile records the convention as *"the exact slice between the
fetch result's `<content>` and `</content>` markers, with no trailing newline added"* — which is
not strip-both, and under which the pins it ships do not reproduce. Detail in Finding 1.

### A2 — are the 2026-09-18/19 pins still true today?

**No drift found in the sample. Two of 55 re-fetched from Notion on 2026-09-21 and both reproduce
their pins exactly.**

| prompt | page id | fetched today, strip-both | pin | |
|---|---|---|---|---|
| `CF-C-10` | `3db4590a05eb8119a5a8e4d083fcf360` | 7203 B, `41dce73a62735927d291bd8f7342654d314d38de47070fe37f8a6c9318fd1702` | identical | **match** |
| `IA-60` | `3db4590a05eb8141b5b2c8fbf7b725e2` | 5633 B, `5addd33093e4c794e609829bba434275f06e798d313eda8ed29d63ffdba3e8c6` | identical | **match** |

Both pages report `page_last_edited_at` inside the recorded extraction window (2026-09-18), so
this is a fresh fetch agreeing with a dated record, not a dated record agreeing with itself. The
remaining 53 are unsampled; I make no claim about them. `CF-C-10` is one of the three prompts the
registry names as reproducing only under strip-both, and my independent extraction reproduces
that result exactly, which is also the evidence for Finding 1.

### A3 — was the profile chosen because it is right, or because it is cheap?

**Right, and I would put them there for reasons the report does not give.**

The cheapness is real but it is not the load-bearing argument, and the decision survives without
it. The candidate contract is a *contract*: a statement of what the release's members are and how
they route, shared by `change-flow` and pinned by a chain that reaches into
`EXPECTED_CANDIDATE_CONTRACT_SHA256`. A body's byte count and SHA-256 are not terms any party
agrees to; they are an expectation one validator holds about an artifact it will be handed. That
is the profile's whole job, and `candidate_contract.sha256` is already there for exactly the same
reason. Putting the pins in the contract would also make every authorised body edit a contract
change, which would move `change-flow`, move the hash-pin chain, and make the cost of re-pinning
high enough to tempt people to skip it — a worse outcome than the one being avoided.

Two things follow that the report does not say, and that bear on `Q3`. The profile's own bytes
are pinned by nothing: no script carries its SHA-256 the way `validate_gcfpe_20260914.py:943`
carries the contract's. And `subset_errors` pins nine profile fields but neither
`prompt_bodies.count` nor the member roster, so `count: 55` is recorded and never read. Neither
is exploitable for silence — a stripped block raises `PROMPT_BODY_PINS_ABSENT`, a short roster
raises `:UNPINNED` per missing id, and a wrong pin value raises a false positive rather than
hiding a true one — so neither is a finding. They are the reason the answer to `Q3` is what it is.

### A4 — `C1` against the installed validator

Done above, seven corruptions, all invisible to the installed build. The justification for the
change is established on the running bytes and does not depend on the author removing their own
check.

### A5 — revision recount by grep

**Confirmed, all three.**

`validator_revision` is `3.2.10` at exactly **four** value-bearing sites, all inside
`flowmaster-validate`, none in `change-flow`, none in the candidate contract:
`references/…validation-profile.json:272`, `scripts/run_gcfpe_20260914_fixtures.py:674`,
`scripts/validate_gcfpe_20260914.py:1063`, `scripts/validate_flowmaster.py:1223`. The four SKILL.md
occurrences are prose.

`FLOWMASTER_VALIDATE_REVISION` is `3.2.12` at its single assignment, `SKILL.md:8`; the other four
occurrences are dated narrative. `CHANGE_FLOW_SPECIALIZATION_REVISION` is untouched at **3.2.8**
at every site that asserts it, and the profile's `installed_skill_revisions.change-flow` is
`3.2.8`. Every surviving `3.2.9` and `3.2.11` is AUTH-001 narrative in SKILL.md, not a live
identity.

**The candidate contract (`§8f`), re-derived from the file and never transcribed.** 610549 bytes,
`1c3c7969b7b933569362a35acdff6f756e2ab8577054f5038e4a95ad3794e179`. `cmp` shows the
`flowmaster-validate` copy and the installed `change-flow` copy **byte-identical**. The
validator's `EXPECTED_CANDIDATE_CONTRACT_SHA256` (line 943) and `_BYTES` (line 944) and the
profile's `candidate_contract.sha256` / `byte_count` all agree with the file itself.

### A6 — the profile still round-trips

**Confirmed.** `json.dumps(indent=2, sort_keys=True, ensure_ascii=False)` plus a trailing newline
reproduces the shipped file **byte-for-byte**, as it does for the installed copy. Nothing changed
beyond `validator_revision` and the new `prompt_bodies` block — zero keys removed, one changed,
113 added and all under `prompt_bodies`.

One correction to the prompt's framing: the profile is **10673** bytes, not 10672. 2473 is right.

### A7 — treating stated install state as suspect

Applied. Every digest in this record is derived from the artifact in front of me. §3's claim about
the installed tree turned out to be correct, which I established before reading the report.

## 4. Findings

### Finding 1 — the profile records a convention under which its own pins do not reproduce (blocking)

*Artifact:* `flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json`,
`prompt_bodies.extraction_convention`; the same wording at
`flowmaster-validate/scripts/validate_gcfpe_20260914.py` lines 2235–2238.

*Defect.* The shipped value is:

> the exact slice between the fetch result's `<content>` and `</content>` markers, with no
> trailing newline added; a file holding one body may carry a single trailing newline, which the
> validator strips before hashing

The approved registry's authority key `body_extraction_convention.in_force` is
**`STRIP_BOTH_BOUNDARY_NEWLINES`**, and that key dispositions this exact wording by name:
*"incomplete in two ways: it omits the leading newline entirely, and it states the trailing
treatment as an addition withheld rather than a byte dropped. Read literally it describes a
different corpus from the one the recorded digests identify."* The key landed on `main` in #421 on
2026-09-20, one day before this package. The profile's `recorded_from` cites the registry's
`evidence_contract` but not the key that governs how those rows were produced.

*Evidence, from my own extraction rather than the record.* `CF-C-10` fetched from Notion
2026-09-21: strip-both gives 7203 B / `41dce73a…`, which is the pin exactly; the profile's stated
reading gives 7205 B / `5e32802d…`; the two one-newline readings give 7204 B. And because the
validator strips exactly one trailing newline, a file written under the profile's own stated
convention is hashed as `\n`+body and fails. Measured: that scenario produces
`PROMPT_BODY_IDENTITY:CF-C-10` — the fourth row of the `A4` table.

*Why it matters, beyond tidiness.* The pins exist so that a session other than the one that built
the corpus can rebuild it and be checked. An operator who follows the convention the shipped
profile states will fail all 55 bodies at once and will have no way to tell a build error from
drift in Notion — with `Q1`'s fatal disposition, that stops every gate in the ecosystem. This
reproduces, inside the artifact that introduces the check, the same ambiguity the registry says
*"already produced one silent two-byte error that no amount of agreement between independent
extractions would have surfaced."*

*Smallest correction.* Replace the value with the convention in force, and cite the key that
carries it — for example: *"STRIP_BOTH_BOUNDARY_NEWLINES per `body_extraction_convention` in
docs/prompt_ecosystem_management/project-prompt-contract-registry.md: the exact slice between the
fetch result's `<content>` and `</content>` markers with the two boundary newlines dropped — the
newline following `<content>` and the one preceding `</content>`; a file holding one body may
carry a single trailing newline, which the validator strips before hashing."* Same correction to
the code comment. No behaviour changes; the pins are already correct.

### Finding 2 — the new check reuses another guard's error code, and the shared string is de-duplicated (blocking)

*Artifact:* `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2253`, colliding with the
pre-existing emission at `:2265`, inside `validate_prompt_bodies`, which returns
`sorted(set(errors))` at `:2391`.

*Defect.* Two unrelated guards in the same loop append the identical literal
`PROMPT_BODY_IDENTITY:{prompt_id}`: the new byte-pin comparison (2253) and the long-standing
identity-**header** check `prompt_identity_header_valid` (2265). Because the function de-duplicates
before returning, a body that fails **both** reports the same single string as a body that fails
**either**. One of the two signals is destroyed, not merely mislabelled.

*Evidence.* Measured on the real `CF-C-10`:

| corpus | occurrences of the literal `PROMPT_BODY_IDENTITY:CF-C-10` |
|---|---|
| pristine | 0 |
| one byte appended (pin guard alone fires) | **1** |
| title line replaced (both guards verified to fire individually) | **1** |

In the third row I confirmed each guard independently: the pin comparison is true, and
`prompt_identity_header_valid(...)` returns `False`. Two defects, one string.

*Why it matters.* The two failures have opposite remedies — investigate drift and re-pin, versus
repair a malformed header — and the operator cannot tell which fired, or that both did. Having
fixed the header they would re-run and see the same error unchanged. The author's own
falsification table reads `PROMPT_BODY_IDENTITY:IA-30` as if it names the pin check; it does not,
and after this change it never will unambiguously. This is the failure mode the same file's
comments already name — *"a fixture that fires two guards cannot prove which one caught it"* —
moved from a fixture into the shipped error vocabulary.

*Smallest correction.* Give the new comparison its own code. The block already suffixes
`:UNPINNED` for its other outcome, so `PROMPT_BODY_IDENTITY:{prompt_id}:BYTES` keeps the family and
is a one-token change; a distinct `PROMPT_BODY_PIN:{prompt_id}` would also do. Either way the
report and SKILL.md paragraph need the new code.

### Finding 3 — the "24 of 55" justification in the shipped comment is unsupported and points the wrong way (non-blocking)

*Artifact:* `flowmaster-validate/scripts/validate_gcfpe_20260914.py` lines 2241–2244; repeated in
`REPORT.md`.

*Defect.* The comment says: *"Getting this wrong in the other direction is not hypothetical: 24 of
55 `evidence_contract` entries once reproduced only with a trailing newline the page does not
contain."* Grepped across `docs/`, the only record carrying "24 of 55" is the registry's
`body_extraction_convention.evidence_scope`, where 24 is the number of bodies the **evidence
covers** — 21 repaired plus 3 untouched — and not a count of anything that reproduced with a
trailing newline. The adjacent `evidence` key reports the opposite result: *"0 of 21 under
as-extracted, leading-only or trailing-only."*

*Why it matters.* This is the same species as my round-24 finding, one round later: a true number
carried out of the context that gives it meaning and into a claim it does not support, shipped in
a comment that justifies a design choice. The choice it justifies is correct on other grounds, so
nothing downstream is wrong — but the next maintainer inherits a citation that does not check out.

*Smallest correction.* Delete the sentence, or restate the registry's actual finding (21 of 21
repaired bodies reproduce under strip-both and 0 of 21 under any other variant) and cite
`body_extraction_convention.evidence`.

### Nit

`prompt_bodies.count: 55` is recorded and never read; `subset_errors` pins nine profile fields and
neither this one nor the member roster. Not exploitable — a short roster raises `:UNPINNED` per
missing id — so not a finding. Worth pinning when the block is next touched.

## 5. Disposition of the round-24 finding

**FIXED, and the replacement text is correct.** I verified both halves by execution against the
shipped checker rather than by reading the new comment.

| the corrected comment's claim | measured |
|---|---|
| `PROMPT_HANDOFF_RECEIVER` is emitted by the end-to-end `validate_prompt_bodies`, and `validate_qa_closure_bodies` "never emits that error at all" | **true.** Across four producer shapes that checker emitted only `QA_PASS_BODY_CLASS_MAP`, `QA_CLASS_UNRESOLVED_HANDOFF`, `QA_PASS_BODY_INTAKE`, `QA_PASS_RECEIVER_BODY:*` — never `PROMPT_HANDOFF_RECEIVER` |
| the absence case does **not** isolate the arity branch — it "drops the row count to one AND breaks the mapping" | **true.** rows = 1; length half fires **and** mapping half fires |
| "measured by removing the length half, after which this case still passes" | **true.** With `len(rows) != 2` removed, the mapping comparison alone still rejects the absence case |
| `reject-source-duplicate-crd-class-branch` "is the case that isolates the length half" | **true.** rows = 3, mapping half does **not** fire (the duplicate collapses in the dict), length half fires alone |

The comment now says which checker emits what and stops claiming coverage the round's own
experiment disproved. No defect found while checking it. The shipped bytes and `REPORT.md` now
agree, which was the substance of the finding.

`F1` and `F2` remain closed and were not reopened.

## 6. The three open questions

### Q1 — should `PROMPT_BODY_IDENTITY` be fatal, or routed to re-pinning?

**Fatal is correct. Keep it.** A body's bytes are the ecosystem's tamper-evidence; an unexplained
difference between the page and its recorded identity is precisely the condition no run should
proceed past, and "report as drift and carry on" is how a check becomes decoration. The forcing
function is the point: an authorised body edit in Notion *is* a change to the corpus's identity,
and re-pinning the profile is part of performing that change, not an exception to it — the report
says this and it is right.

It is a trap only if re-pinning is expensive or undocumented, and today it is neither
well-documented nor cheap: it requires a new package, a new `validator_revision`, and an
independent §10 review, for a change that may be a single word in one prompt. That is a real cost
and it will be paid at the worst moment. I would not soften the check to fix it. I would make the
remedy explicit — a named re-pinning procedure in SKILL.md stating that an authorised body change
carries a profile re-pin and a revision increment in the same package — so the operator who hits
a red gate at 2am finds the path rather than inventing one. Finding 1 must be fixed first: a fatal
check whose reproduction instructions are wrong is a trap regardless of this answer.

### Q2 — a dated pin, or a pinned date with a required fresh fetch?

**A dated pin is the right artifact.** A pin is an identity; a date is provenance. Requiring a
fresh fetch would make the gate depend on network access, on Notion's availability and on its
rendering staying stable, and would turn a deterministic offline check into a flaky one — while
answering a different question. It would also destroy the property that makes this change
valuable: that a corpus built anywhere, by anyone, at any time, can be checked against a fixed
value. The profile already records both dates and the source, so a mismatch is diagnosable.

What a dated pin does not tell you is whether the pin is still *current*. That is a separate
control and should stay separate — a periodic re-fetch that compares live pages against the pins
and reports drift, which is exactly what I did for two of the 55 in `A2`. Keep the pin fatal and
offline; make freshness a scheduled audit, not a runtime dependency.

### Q3 — is a procedural post-install digest comparison sufficient?

**No. Make it a control.** This round is the evidence: a procedure held by one session failed on
its first real test, and every existing control — the hash-pin chain, the fixture suites, §10
itself — passed happily against a superseded build, because each one validates the *contents* of
whatever tree it is running from and none of them validates *which tree that is*. A procedure is a
control only while someone follows it, and the session that wrote the rule into every reviewer
prompt it produced is the session that then recommended skipping the gate.

The fix is cheap and belongs in the artifact that already carries every other expected identity.
The validator should compute the freeze digest of the skill directory it is running from and
compare it with a declared self-identity, failing with something like `SKILL_SELF_IDENTITY` when
they differ. Note the two constraints that make this less trivial than it sounds, both of which
this ecosystem has already solved once: the digest must be rooted at the skill directory and must
exclude `manifest.json`, or it becomes a per-container value — the round-23 defect; and the
declared value cannot live inside the tree it measures without a fixed-point problem, so it must
be recorded where the package's identity is already recorded, with the file holding it excluded
from its own digest.

I would not remove the procedural rule. A control catches the wrong package at run time; the
procedure catches it at install time, which is hours earlier and before anyone has trusted a
green gate. Both, and the control is the one that does not depend on anybody remembering.

## 7. What I did not do

No skill installed. Nothing written to the synced skills directory — both installed digests
reproduce unchanged after every experiment. Nothing merged, no auto-merge enabled. No edit to
`docs/pfcanon/**`. No prompt body changed in Notion: two were read, neither was written, and
neither was adjusted to fit — both reproduced their pins as recorded. No dated record corrected in
place; this is a successor record under AUTH-001. No QA verdict, acceptance, closure or PF
movement.

## 8. What this needs

`SKILL_REPAIR_REQUIRED` on Findings 1 and 2; Finding 3 folds into the same pass. All three
corrections are text or a single error string, inside files this package already moves, and none
touches `change-flow` or the hash-pin chain. Per `C7`'s own rule, the repaired bytes must not
reuse the identities this verdict describes: `validator_revision` **3.2.10 → 3.2.11** at its four
sites and `FLOWMASTER_VALIDATE_REVISION` **3.2.12 → 3.2.13**.

The installed tree stays as it is meanwhile. It is one round behind and carries a published
confirmation; it lacks the pins, so a corrupted body still passes in silence — that gap has stood
for every prior round and one more review cycle does not widen it.

**DECISION NEEDED** — whether to accept the two findings as blocking and authorise a round-26
repair package, and whether to adopt the `Q1` re-pinning procedure and the `Q3` self-identity
control as separate work.
