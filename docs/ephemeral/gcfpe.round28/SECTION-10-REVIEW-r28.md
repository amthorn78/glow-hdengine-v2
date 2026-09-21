---
artifact_type: GCFPE_SECTION_10_INDEPENDENT_REVIEW
artifact_version: "1.0"
created_date: 2026-09-21
round: 28
reviewer: SFR-01
role: independent validation — did not author the change
verdict: SKILL_REPAIR_REQUIRED
status: SUCCESSOR_RECORD_DO_NOT_EDIT_IN_PLACE
supersedes: nothing — this is a new dated record (AUTH-001)
---

# Round 28 — §10 independent review

## Verdict

**SKILL_REPAIR_REQUIRED.**

Bound explicitly to these bytes, measured by me from the archives I was given:

| package | files | bytes | sha256 |
|---|---|---|---|
| `change-flow.skill` | 21 | 242827 | `ed7041c0ee2179afcc0b684954f0605fd5ab495fea203a4dfafd7eb3f97c7860` |
| `flowmaster-validate.skill` | 29 | 285630 | `b5f5d3a338a2cd7dafe8436b73af6713dec0633403ed03a24e026d4f2439fd36` |

**This verdict is void for any other bytes.** It does not carry to a repaired package, to a
rebuild, or to either skill installed alone. The two install together or not at all.

Two findings, both blocking, both verified by falsification, both one- to two-line corrections.
Neither makes the package worse than what is installed — the installed tree cannot reach a
consistent promoted state at all, and this package can. The verdict is *repair and re-issue*, not
rejection.

## Identity reproduced before anything else

`freeze.py` from the branch, rooted at each skill directory, `PYTHONDONTWRITEBYTECODE=1`:

| tree | files | digest | §3 says |
|---|---|---|---|
| baseline `change-flow` | 21 | `14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2` | matches |
| baseline `flowmaster-validate` | 29 | `9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833` | matches |
| repaired `change-flow` | 21 | `80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8` | matches |
| repaired `flowmaster-validate` | 29 | `13353ffed880aa0337b90f91aba4302b450708cacae91b042edee78583c8d289` | matches |

The baseline reproduces, so the review proceeded.

`SKILL_TREE_SHA256: 8ed6d8b00240d04a72e1caa69a0f1c4be473913d1035d36534d1a030bbaf5f23` — §3's
claim that this is a *different* recipe excluding its own declaration line is **confirmed
independently**: deleting that one line from `SKILL.md` and re-running `freeze.py` reproduces
`8ed6d8b0…` exactly. Both values are correct and are not meant to match.

Every entry in both archives sits under its own skill root. No traversal sequences, no entry
outside the root. `name:` is unchanged in both (`change-flow`, `flowmaster-validate`).

**The tree did not move under me.** At the end of the review the installed digests were still
`14981ba7…` and `9c0ca6fe…`. The only file with a changed mtime anywhere in the synced directory
was `manifest.json`, which `freeze.py` deliberately excludes as sync-layer bookkeeping; zero files
inside either reviewed skill changed. Nothing was installed. Nothing was written to the synced
directory — it contains zero `.pyc` and zero `__pycache__`.

## Findings

### F1 — `prompt_body_governance_state` is evaded by indentation and ordinary Markdown decoration

**Artifact.** `flowmaster-validate/scripts/validate_gcfpe_20260914.py`,
`prompt_body_governance_state()`.

**Defect.** The check tests `line.startswith(key)` over `nonblank`, and `nonblank` is
`[line for line in text.splitlines() if line.strip()]` — lines are *filtered* by whether they are
blank but never *stripped*. The authority line is tested by exact list membership
(`PROHIBITED_SELECTION_AUTHORITY_LINE in nonblank`). Any leading character defeats both.

**Evidence.** Measured against the shipped module and against the same module with the correction
below. `CAUGHT` means the check fired.

| vector | as shipped | with correction |
|---|---|---|
| `Selection status: UNSELECTED_CANDIDATE` | CAUGHT | CAUGHT |
| `Lifecycle: UNSELECTED_CANDIDATE` | CAUGHT | CAUGHT |
| authority disclaimer, exact | CAUGHT | CAUGHT |
| `··Selection status: …` (leading spaces) | **evades** | CAUGHT |
| `→Lifecycle: …` (leading tab) | **evades** | CAUGHT |
| `**Selection status:** …` (bold) | **evades** | CAUGHT |
| `- Selection status: …` (bullet) | **evades** | CAUGHT |
| `> Selection status: …` (blockquote) | **evades** | CAUGHT |
| `**` + authority disclaimer | **evades** | CAUGHT |
| the same fact in prose | evades | evades |
| a different key (`Selection state:`) | evades | evades |

Bold and bulleted lines are not exotic in this corpus: the bodies are Notion blocks, and Notion's
own editor produces both from ordinary use. The last two rows are genuinely uncatchable by a
substring scan and A2 says so; they are not part of this finding.

**Why this is blocking.** The round's authority is an instruction to stop the class — *"such
things should not be appended to prompts in the future"* — and this check is the mechanism. The
report states the change "makes their return impossible". It does not: three plausible renderings
walk through it.

**Second consequence, which is the more serious half.** The identical blind spot exists in the
**old** validator's `len(status_lines) == 1`, which collected lines the same unstripped way. That
predicate is the sole support for A1's inferential proof. A decorated or indented selection line
would have been invisible to the round-27 post-flight, would not have been counted, would not have
matched the exact-match replace anchor, and would still be there — invisible to the new check too.
So A1's argument is sound **only for undecorated, unindented lines**. See A1 below.

**Smallest correction.** Strip leading whitespace and common Markdown lead-in before matching, and
test the authority line by containment rather than equality:

```python
stripped = [re.sub(r"^[\s>*\-+]*(?:\*\*|__)?", "", line) for line in nonblank]
return any(
    line.startswith(key) for line in stripped for key in SELECTION_HEADER_KEYS
) or any(
    PROHIBITED_SELECTION_AUTHORITY_LINE in line for line in stripped
)
```

Verified: closes all six vectors, `validate_gcfpe_20260914.py` stays green on every substantive
check, fixture suite stays `fixture_suite_ok: true` at 156 cases. Add fixture cases for at least
the indented and bolded forms — the present eight test only undecorated input.

### F2 — the validation profile still asserts `UNSELECTED_CANDIDATE` about the contract it pins

**Artifact.** `flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json`,
`candidate_contract` block; and `load_profile()` in
`flowmaster-validate/scripts/validate_gcfpe_20260914.py`.

**Defect.** The block pins the **promoted** contract — `sha256: 2b78f877…`,
`byte_count: 606657`, both updated in this round — while still declaring
`"selection_status": "UNSELECTED_CANDIDATE"`. The contract it pins declares
`SELECTED_PRODUCTION`. `load_profile()` does not merely tolerate the stale value, it **requires**
it, through `subset_errors(candidate_pin, {… "selection_status": "UNSELECTED_CANDIDATE"},
"PROFILE_CONTRACT_PIN")`.

**Evidence.** Setting the field to the truthful value for the artifact it pins makes the gate
fail:

```
errors: ['PROFILE_CONTRACT_PIN', …]
ok: False
```

That it is a stale current fact and not a deliberate historical label is settled by the profile's
own convention: three sibling historical fields in the same file carry an explicit suffix —
`selected_release_during_staging`, `selected_prompt_version_during_staging`,
`selected_member_count_during_staging`. This field does not, and it sits beside `schema_version`,
`sha256` and `byte_count`, all live properties of the artifact. Two of the three were updated this
round; the third was not.

**Why this is blocking.** This is the same trap as coupled defects 1 and 3 — a selection value
pinned to a literal with no production branch — surviving in a fourth site. It makes a governance
artifact state a falsehood about the contract it pins, and it means the *next* maintainer who
corrects the profile to the truth breaks the gate. Every other surviving candidate-ism in this
release was disclosed as a question or a limit (Q1, Q2, Q3, L3). This one was not disclosed
because it was not found.

**Smallest correction.** Rename the field to `selection_status_during_staging` in the profile and
in the required subset in `load_profile()` — which makes the assertion true as history and matches
the file's existing convention. Verified: gates stay green, suite stays 156/156. Dropping the field
entirely is equally sound, since `sha256` already pins the artifact exactly; mirroring the contract
the way `validate_graph_contract` now does is *not* available here without restructuring, because
`load_profile()` does not receive the contract.

## Gates — what I actually ran

All five, from the extracted contents, in a full sibling tree (the whole synced directory restored
around the two replaced skills, per §3g), `PYTHONDONTWRITEBYTECODE=1`, flags read by name.

| gate | flag | result | author's measurement |
|---|---|---|---|
| `flowmaster-validate/…/validate_gcfpe_20260914.py` | `ok` | `true`, `errors: []`, `contract_status: SELECTED_PRODUCTION` | matches |
| `flowmaster-validate/…/run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` | `true`, 156 cases, §13 33/33 and 28/28 variants | matches |
| `flowmaster-validate/…/validate_flowmaster.py` | `suite_ok` | `true`, `FLOWMASTER_SUITE_PASS`, `self_identity: OK` | matches |
| `flowmaster-validate/…/validate_gcfpe_current.py` | `ok` | `true`, `errors: []` | matches |
| `change-flow/…/validate_gcfpe_20260914.py` | exit + text | `PASS` | matches |

**Every author measurement in §8 reproduced.** I contradicted none of them.

§8b's warning reproduces too: passing the graph contract instead of the direct-handoff contract
raises `TypeError: 'NoneType' object is not iterable` at line 1865. I confirmed this is
**pre-existing** — the installed baseline crashes identically — so it is disclosed, not introduced,
and out of this round's scope. It remains a usability wart: a wrong-argument mistake deserves a
message, not a traceback.

**What I could not run.** Nothing. There is no gate in §8 I was unable to execute. The one thing I
did not do exhaustively is read all 55 prompt bodies; that was a cost decision of mine, not a
restriction, and I say exactly how far I got under A1.

## The change accounts for itself

Twelve files differ between the installed tree and the extracted packages, and the report accounts
for all twelve. File lists are otherwise identical — nothing added, nothing removed.

`change-flow`: `SKILL.md`, both contracts, `scripts/validate_gcfpe_20260914.py`.
`flowmaster-validate`: `SKILL.md`, both contracts, `references/…validation-profile.json`,
`scripts/run_gcfpe_20260914_fixtures.py`, `scripts/validate_flowmaster.py`,
`scripts/validate_gcfpe_20260914.py`, `scripts/validate_gcfpe_current.py`.

`validate_gcfpe_current.py` and `validate_flowmaster.py` change only because they pin
`change-flow`'s revision string; both diffs are `3.2.8` → `3.2.9` plus the validator revision.
Both `SKILL.md` diffs are additive narrative plus the revision and tree-hash bumps; prior-round
history is preserved rather than rewritten, as AUTH-001 requires.

### Promotion transition — §8d, every item

Checked against the direct-handoff contract itself, not the report. All pass:
`status` and `selection_status` `SELECTED_PRODUCTION`; `contract_id`
`GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED`; `selection_claim` and `publication_evidence`
both `true`; `selected_member_count` 55; all 55 `member_registry` and all 55
`notion_page_manifest` entries `SELECTED_PRODUCTION`; all 55 member lifecycles
`SELECTED_PRODUCTION`; **zero** members retain `candidate_page_binding`; all five prompt references
and `alpha_resumption_contract.successor_trigger.prompt` `SELECTED_PRODUCTION`.

**`UNSELECTED_CANDIDATE` occurs 0 times in that file**, down from 173.

### Hash pins — §8e, recomputed from the artifacts

| pin | consumer agrees |
|---|---|
| contract `2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b`, 606657 bytes | yes |
| graph `90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223`, 569835 bytes | yes |
| `contract.source_snapshot.frozen_candidate_graph.sha256` | yes |
| `EXPECTED_FROZEN_GRAPH_SHA256` / `_BYTES` | yes |
| `EXPECTED_CANDIDATE_CONTRACT_SHA256` / `_BYTES` | yes |
| `change-flow` `EXPECTED_GRAPH_SHA` | yes |
| profile `candidate_contract` and `frozen_graph` sha256 / byte_count | yes — **but see F2** |

Both bundled copies of the contract are byte-identical; both bundled copies of the graph are
byte-identical. Every digest above was derived from the artifact in front of me. None was
transcribed from the report.

### Graph rebuild — §8f, independent of the author's number

`graph_parts.py build` over the 56 parts at `docs/graph/parts/`:

```
build: 55 nodes, 227 edges, 55 state_routes
       embedded JSON 569835 bytes  sha256 90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223
       validation PASS
```

The rebuilt JSON block is **byte-identical** to both bundled copies. The graph is derived, not
hand-edited, and it reproduces.

Revision sites recounted by grep: `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9` at six sites, all
current; `FLOWMASTER_VALIDATE_REVISION: 3.2.15`; `validator_revision 3.2.13` at four executable
sites. Remaining `3.2.8` / `3.2.12` / `3.2.14` strings are all historical narrative in `SKILL.md`
describing earlier rounds, correctly preserved.

## §6 — answered explicitly

**A1 — the claim that all 55 bodies are clean.** *Partly sustained, with a named hole.*

The inferential line is **sound for undecorated, unindented selection lines**, and I verified each
step rather than accepting it. The old validator collected every line anywhere in the body
beginning with `Selection status:` or `Lifecycle:` and required exactly one, so a second plain
occurrence anywhere would have failed round-27's post-flight. An exact-match replace cannot succeed
against absent text. One existed, one was removed, zero plain ones remain. That reasoning holds.

The hole is F1: neither the old count nor the new check sees an indented, bolded, bulleted or
quoted selection line. A body carrying one *in addition to* the plain line would have passed the
round-27 post-flight, kept it through the replace, and still carry it. The inferential argument
cannot close that case, because the predicate it rests on is blind to exactly it.

**I could not falsify the claim on any prompt.** I read **6 bodies in full, none of them among the
author's 7** — `CF-E-20`, `CL-30`, `GCFPE-MGMT-10`, `MGR-10`, `UTIL-10`, `PR-35` — chosen one per
lane across the 48 the author did not re-read, and including the new member. All six are clean in
every form: no selection line plain, indented or decorated; `Notion URL:` present with no
release-phase label; no authority disclaimer. Both header dialects are represented in my sample
(`Prompt Version:` + `Set:` and the backticked `Prompt version:`).

Direct confirmation therefore stands at **13 of 55** — the author's 7 plus my independent 6, with
no overlap. The other 42 rest on an argument with a known blind spot. That is not a finding against
the change, and I am not asserting any body is dirty; it is the honest residual, and F1's
correction plus one sweep with `--bodies-stdin` would close it.

Two things I checked and found *not* to be problems, having suspected both: the corpus really does
carry two header dialects, and `PROMPT_VERSION_HEADER_RE` is `^Prompt [Vv]ersion: …`, which
tolerates both and is unchanged from baseline. And `prompt_identity_header_valid` passes on real
bodies of both dialects, including the mention-rendered `Notion URL:` line — I piped two real
bodies through `--bodies-stdin` and neither raised `PROMPT_BODY_IDENTITY` or
`PROMPT_BODY_GOVERNANCE_STATE`.

**A2 — what `prompt_body_governance_state` misses.** Answered as **F1**. Leading whitespace: yes,
misses it. A different key: yes, and uncatchable. The same fact in prose: yes, and uncatchable. The
author named the right three; the measurement adds bold, bullet and blockquote, which matter more
than whitespace because Notion's editor produces them from ordinary use.

**A3 — removing the production mode rather than fixing it.** *Verified, no finding.* The only
`production_mode` uses removed are the four inside `prompt_identity_header_valid` and its two call
sites. Every other branch survives textually unchanged: `PRODUCTION_SELECTION_EVIDENCE`,
`PRODUCTION_MEMBER_LIFECYCLE`, `PRODUCTION_CANDIDATE_PAGE_BINDING`, the production prompt-reference
block in `validate_contract`, and the contract-hash / bundle-comparison branches. They are still
correct: `PRODUCTION_SELECTION_EVIDENCE` pins `contract_id`, `selected_member_count`,
`selection_status`, `publication_evidence` and `selection_claim` together, and every member record
is required to mirror the contract's `selection_status`. Removing the mode from a body-identity
check was the right call — a body's identity genuinely does not depend on release selection.

**A4 — the graph mirroring the contract, bounded by `GRAPH_SELECTION_STATUS`.** *Sufficient.* The
concern is that a mirror cannot disagree, so it cannot catch a wrong contract value. But the
contract's `selection_status` is not free: `LIFECYCLE_STATUS` bounds `status` to three values, and
then `CANDIDATE_SELECTION_ISOLATION` and `PRODUCTION_SELECTION_EVIDENCE` between them force
`selection_status` to a single determined value in every one of those three cases. So the value the
graph mirrors is already independently pinned, and the explicit two-value bound is correct
belt-and-braces. The `if/elif` is right: out-of-bounds reports `GRAPH_SELECTION_STATUS`, otherwise
mismatch reports `GRAPH_SELECTION_STATUS_CONTRACT_MISMATCH`.

**A5 — PR-35's "new member" fact.** *Confirmed, survives in both places claimed.* The contract
carries `"sole_added_member": "PR-35"`, and the graph carries
`candidate.member_rule: "54 selected predecessors + PR-35; no removals"`. Both name PR-35
explicitly. The lifecycle moving to `SELECTED_PRODUCTION` is correct and loses nothing, because the
"new member" fact was never carried by the lifecycle value. I read PR-35's body as well; it is
clean.

**A6 — the eight replaced fixture cases.** *Read; they are adequate, and the arithmetic checks
out.* Eight old cases became nine new ones, which is the 155 → 156 the report claims. The new set
is a positive identity control, four identity rejections (`Candidate ` label, `Selected ` label,
duplicate generic URL, wrong extra generic URL), a governance-free negative control, and three
governance rejections (`Selection status:` production form, backticked `Lifecycle:`, the authority
disclaimer). Splitting identity from governance into two checks with separate falsification is
better than what it replaced, and `reject-selected-url-label` is a genuinely new test — the URL
regex matches `Selected ` too, so that label had to be rejected explicitly.

They are still the author's tests of the author's work, and they share the author's blind spot:
**every case uses undecorated, unindented input.** That is why F1 survived them, and why the
correction needs cases of its own.

## Questions this round deliberately did not settle

**Q1 — the graph contract keeps `contract_id: GCFPE-20260914.1-CANDIDATE-GRAPH` and
`status: FROZEN_FOR_CANDIDATE_AUTHORING`. Should they move?** *Not in this round, and the author
was right to leave them.* An id is a join key; the profile, the contract's `source_snapshot` pin
and `validate_graph_contract`'s `GRAPH_IDENTITY` subset all key off it, and changing it cascades
into artifacts this package does not contain. `FROZEN_FOR_CANDIDATE_AUTHORING` is also accurate as
a statement about the graph's *authoring* state — it is frozen, and it was authored during the
candidate phase. Move both in a round scoped to the rename, with the cascade enumerated first.
Leaving them is not the same defect as F2: these are not *asserted to be false*, they are
release-phase names on a stable identifier, and the graph's own `selection_status` now correctly
reads `SELECTED_PRODUCTION`.

**Q2 — the five lane hubs still head their topology columns "Candidate prompt" and "Candidate
binding".** *Correct to leave, and the reasoning given is right.* They are control pages, not
prompt bodies; `prompt-body-content-policy.md` reaches prompt bodies. I confirmed from Notion that
the hubs carry this table and a hub-level `selection_rule` that explicitly disclaims self-selection
— *"This version is operative if and only if the register selects … It does not assert its own
selection"* — which is the opposite of the defect this round removes. The column headings are
stale-sounding labels on an accurate table. Worth tidying when a hub is next edited; not a defect.

**Q3 — `member_registry` node keys `candidate_url` and `candidate_version`.** *Leave.* These are
schema key names inside a derived artifact, consumed by position in the graph parts and rebuilt by
script. Renaming them is a schema migration across 56 parts plus every consumer, to remove a word
from a key that no longer carries meaning. Nothing reads selection state from them. Lowest priority
of the three.

## C6 — the round-27 post-flight's three warnings

All three are genuinely **unaffected by this change and remain open**, as C6 states. I verified
rather than accepted:

1. **§3g scratch-copy scope.** Unaffected — it is a warning about review method, not package
   content. §8b now spells out the full-sibling-restore requirement, which is the mitigation; it
   worked, and I hit no phantom `SKILL_MISSING`.
2. **721-vs-831 assertion count.** Unaffected; nothing in this diff touches the counting.
3. **`fixture_suite_ok` not qualified by families that evaluated nothing.** Still open and
   confirmed live: the suite reports `fixture_suite_ok: true` alongside
   `artifact_timing_case_count: 0` and `qa_closure_source_case_count: 0`, with no
   `not_evaluated` key anywhere in the report.

Worth recording as a contrast the round earned: `validate_gcfpe_20260914.py` now *does* qualify
itself, reporting `prompt_body_checks_not_evaluated: ["ALL_BODY_LEVEL_CHECKS"]` and
`prompt_body_count: 0` when run without bodies. That is exactly the discipline warning 3 asks for,
applied in one tool and not yet in the other. The `--bodies-stdin` interface is the right shape:
coverage is reported, never assumed, and a partial supply yields a named list of what could not run
rather than a false pass.

## Two procedural notes, volunteered

**The reviewer prompt I was given is not the one on the branch, and the difference is material.**
The copy I received is byte-identical to commit `24dfe87`. It pins its evidence to commit
`b83bd107` — which is *earlier* than the commit the copy itself is — and the branch has since moved
two commits further, to `9a35f9d`. Those two commits rewrite A1, L2 and §9, which are precisely the
constraints on whether a reviewer may read prompt bodies. My copy says *"I did not read 55 bodies —
the corpus policy forbids it"* and *"Doing so would be a corpus read the policy prohibits"*; the
branch now says the opposite, and so does the policy.

I resolved this against `prompt-corpus-policy.md` itself, which governs: **storage is prohibited
absolutely; reading is not restricted at all.** So I read the bodies the review needed, held them
in context, and wrote none to disk. Had I followed the copy I was handed, I would have reproduced
the exact misreading the branch exists to correct. Flagging it because the next reviewer will be
handed a file too, and a pinned commit that is older than the file pinning it is a trap worth
removing.

**I contaminated my own scratch tree once, and it proves a check works.** An `importlib` call I ran
without `PYTHONDONTWRITEBYTECODE=1` wrote two `.pyc` files into my extracted copy. The next gate
run caught it immediately —
`SKILL_SELF_IDENTITY:DECLARED_8ed6d8b00240_MEASURED_2a7372d8644d` — which is the self-identity
check doing exactly its job against an unannounced change. I removed them and re-verified both
digests back to `80e877c2…` and `13353ffe…`, and re-ran the gates green. The synced directory was
never written to at any point.

## What is needed

Repair F1 and F2, re-issue the two packages together, and re-run §10 against the new digests. Both
corrections are small and I verified both leave every gate green and the suite at 156 cases. F1
should also gain fixture cases for the indented and decorated forms, since the present eight cannot
catch the defect they now need to. Neither package should be installed until then, and neither
should be installed without the other.

The three coupled defects this round set out to fix are genuinely fixed, and fixed symmetrically
rather than loosened — `change-flow`'s staging binding is now *required while staging and
prohibited once selected*, which is the shape the repair needed. The promotion transition is
complete and coherent. The graph reproduces from source. That work stands; it is the two gaps above
that need another pass.

---

DECISION NEEDED
