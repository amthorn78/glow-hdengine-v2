---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-21
status: BINDING
authority: Product Owner direction, 2026-09-21
---

# What may be written into a prompt body

**Product Owner, 2026-09-21:** *"create a policy that such things should not be appended to
prompts in the future"* — and, on what "such things" means: *"of course they may be changed, but
not with useless unapproved things like that."*

## The rule

**A prompt body carries the prompt's behaviour. Nothing else.**

Prompt bodies are edited freely, in Notion, in place — that is how the ecosystem works and this
policy does not restrict it. What it forbids is a *class of content*: governance state written
into a body that does not need it and cannot be resolved there.

**Never written into a prompt body:**

- selection state — `Selection status:`, `Lifecycle:`, `UNSELECTED_CANDIDATE`, `SELECTED`,
  `REGISTER_CONTROLLED`, or any successor vocabulary
- release-phase language — `Candidate` as a prefix on a locator label, staging markers, promotion
  status
- an assertion about which authority owns the prompt's selection, including a disclaimer that the
  header makes no such claim
- any field whose value changes because of a *release event* rather than a *behaviour change*

**Legitimately in a body:** the prompt's title, `Prompt ID:`, its own `Notion URL:`, and the
instructions themselves.

A release's membership and each member's current version live in the register and the
complete-prompt-set catalog. A member whose body changes gets a successor page at the new version;
a member whose body does not change keeps its page, and the register records it in the new
release. Bodies carry no release-bound header line. It applies from the release after 091426.1;
091426.1's bodies were edited in place by `MODIFICATION-20260923-alpha-feedback-open-entries`
(`D23-G`).

The test is mechanical. **Ask what makes the field change.** If the answer is "a promotion, an
archival, a selection" rather than "someone changed what this prompt does", it does not belong in
the body.

## Why

Selection is resolved from the **GCFPE Membership and Release Register** and from nowhere else.
That rule is older than this policy and already binding. A body that also declares selection state
is a second authority, and a second authority is how a release ends up half-promoted with nobody
able to say which half.

It is also a cost that scales with the corpus. A release event that has to rewrite 55 bodies is a
release event that edits 55 artifacts an independent review was scoped to — and *"a verdict is
scoped to exact bytes and does not carry."* Governance state in a body converts a one-line
register change into a corpus-wide edit plus a fresh review round, every time.

## What this replaced

`091426.1` shipped with `Lifecycle: `UNSELECTED_CANDIDATE`` in all 55 bodies, and the validator
required it: `prompt_identity_header_valid` demanded exactly one selection line in both of its
modes, and in production mode demanded a **second** line asserting the register's authority.

**There was no mode in which the line was absent.** Promotion rewrote it and appended to it. The
predecessor release settles the question of whether it was ever needed: `091326.2` bodies carry no
such line at all, and that release ran.

So the machinery would have kept 55 bodies carrying governance metadata forever, and grown it at
each promotion. The validator was changed to match this policy (installed in round 30, 3.2.16),
not the policy bent to match the validator.

### Is the line useful?

No. Its only consumer is the check that verifies the line itself. `SELECTION_HEADER_KEYS` appears
in exactly one function, and that function derives the value it expects **from the contract's own
status** and then confirms the body repeats it. Nothing routes on it; no prompt reads another
prompt's lifecycle.

The one real argument for it is a human warning — *this is a candidate, do not run it*. That
belongs where it is read once, on the catalog or the index, not replicated across 55 bodies that
must then be maintained at every release. `091326.2` shipped and ran with no such line on any of
its 54 bodies.

## Enforcement — INSTALLED

A rule with no consumer that fails on mismatch is decoration — see
`prompt-validation-procedure.md`. The validator change below **is installed**. It was built in
`change-flow` 3.2.9 and `flowmaster-validate` 3.2.15, and installed after a §10 verdict as round
30's `flowmaster-validate` 3.2.16. The `PROMPT_BODY_RELEASE_HEADER` rejection (`D23-G`) was
installed with `change-flow` 3.3.0 and `flowmaster-validate` 3.3.0 on 2026-09-23
(`MODIFICATION-20260923-alpha-feedback-open-entries` §E, stage E6). No skill is trusted until a
party that did not author it has validated it, and each revision here was.

`prompt_identity_header_valid` now:

- requires identity — title, `Prompt ID:`, exactly one `Notion URL:` line whose page identity
  matches the registry binding; rejects `Prompt version:`, `Set:` and `Ecosystem release:` in the
  header window as `PROMPT_BODY_RELEASE_HEADER` (D23-G);
- **rejects** a body carrying `Selection status:` or `Lifecycle:`, as `PROMPT_BODY_GOVERNANCE_STATE`
  — a separate check with its own code, because a body can be identity-valid and still carry
  governance state;
- **rejects** the `Candidate Notion URL:` and `Selected Notion URL:` prefixes, as release-phase
  language on a locator label;
- **has no production mode at all**, because nothing in a body should depend on whether the release
  is selected.

Three coupled defects were repaired in the same change. Without them the ecosystem could not reach
a consistent promoted state — each required the release to still be a candidate:

- `change-flow` hard-required `contract["selection_status"] == "UNSELECTED_CANDIDATE"`;
- `change-flow` also required a `candidate_page_binding` on every member, which promotion removes
  and which `flowmaster-validate` rejects once present in production;
- `validate_graph_contract` pinned the graph to `UNSELECTED_CANDIDATE` with no production branch,
  so the graph was required to contradict a promoted contract. It now mirrors the contract.

The 55 bodies were cleaned in the same change: the selection line removed, `Candidate Notion URL:`
renamed to `Notion URL:`, and **no** selection-authority line added. Both header dialects were
found in the corpus — `Lifecycle:` and `Selection status:` — and both are rejected.

## The general form

**Governance state belongs to the artifact that governs it.** Selection belongs to the register.
Skill identity belongs to the skill's own digest. Contract lifecycle belongs to the contract.
Copying any of them into a body that merely *participates* in that state creates a surface that
can disagree with its own authority, and the disagreement always surfaces at the worst moment —
during a release, when both are being read.
