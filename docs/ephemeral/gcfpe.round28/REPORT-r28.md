---
artifact_type: GCFPE_REPAIR_ROUND_REPORT
artifact_version: "1.0"
created_date: 2026-09-21
round: 28
release: GCFPE-20260914.1 / 091426.1 / 55 (SELECTED)
authority: Product Owner, 2026-09-21 — "yes fix it. and create a policy that such things should not be appended to prompts in the future."
status: PACKAGED_AWAITING_INDEPENDENT_SECTION_10
---

# Round 28 — a prompt body carries behaviour, not governance state

Promotion on 2026-09-21 left `UNSELECTED_CANDIDATE` literals inside the release's own content.
This round removes them and makes their return impossible. The Product Owner's instruction was
not only to fix the literals but to stop the class: *"such things should not be appended to
prompts in the future."*

## What was actually wrong

`prompt_identity_header_valid` had two modes and **both required a selection line in the body**.

| | candidate mode | production mode |
|---|---|---|
| selection line | must read `UNSELECTED_CANDIDATE` | must read `REGISTER_CONTROLLED` |
| how many | `len(status_lines) == 1` | `len(status_lines) == 1` |
| URL prefix | `Candidate Notion URL:` | `Notion URL:` |
| extra | — | **adds** a required `Selection authority: …` line |

There was no third mode and no branch where the line was absent. **Promotion did not remove it —
it rewrote it and appended a second one.** The metadata would have grown at every release.

And it bought nothing. `SELECTION_HEADER_KEYS` appears in exactly one function, which derives the
value it expects **from the contract's own status** and then confirms the body repeats it. Nothing
routes on it. `091326.2` — the release that actually ran — carries no such line on any of its 54
bodies.

## Three coupled defects, each requiring the release to still be a candidate

Found by running the gates against a promoted contract rather than by reading the code:

1. **`change-flow` hard-required `selection_status == "UNSELECTED_CANDIDATE"`.** A promoted
   contract failed that gate outright.
2. **`change-flow` required `candidate_page_binding` on every member** — a key promotion removes,
   and which `flowmaster-validate` rejects as `PRODUCTION_CANDIDATE_PAGE_BINDING` once present in
   production. The two validators contradicted each other the moment the release was selected.
3. **`validate_graph_contract` pinned the graph to `UNSELECTED_CANDIDATE`** with no production
   branch, so the graph was *required* to contradict a promoted contract.

Together these meant **the ecosystem could not reach a consistent promoted state at all.** The
promotion recorded on 2026-09-21 was correct in the register and unreachable in the machine.

## What changed

**Validator.** `prompt_identity_header_valid` is identity only and has no production mode — title,
`Prompt ID:`, `Prompt version:`, `Ecosystem release:`, exactly one `Notion URL:` line whose page
identity matches the registry. A new `prompt_body_governance_state` reports
`PROMPT_BODY_GOVERNANCE_STATE` for any `Selection status:` or `Lifecycle:` line or the old
authority disclaimer — a separate check with its own code, because a body can be identity-valid
and still carry governance state. `PRODUCTION_SELECTION_AUTHORITY_LINE` became
`PROHIBITED_SELECTION_AUTHORITY_LINE`: the same literal, now detected instead of demanded.

**The three coupled defects**, repaired as above. The graph now mirrors the contract's
`selection_status` instead of pinning a literal, bounded by `GRAPH_SELECTION_STATUS`.

**Contracts.** The direct-handoff contract completes its designed promotion transition — status,
`contract_id`, `selection_status`, `selection_claim`, `publication_evidence`,
`selected_member_count`, all 55 registry and manifest entries, all 55 member lifecycles, the five
prompt references and the alpha successor trigger. Every member's `candidate_page_binding` is
dropped. **Zero occurrences of `UNSELECTED_CANDIDATE` remain in it**, down from 173.

**Graph.** 56 parts changed and the graph rebuilt by script — never hand-edited. 55 nodes, 227
edges, 55 state_routes, 569835 bytes, `90021eb7…`.

**Bodies.** All 55 cleaned: selection line removed, `Candidate Notion URL:` renamed to
`Notion URL:`, and **no** authority line added. Two header dialects were found in the corpus —
`Lifecycle:` and `Selection status:` — which the old validator's two-key tuple had quietly
tolerated and which are now both rejected.

## Identities

| artifact | before | after |
|---|---|---|
| direct-handoff contract | `1c3c7969…` / 610549 | `2b78f877…` / 606657 |
| graph contract | `1d0b7258…` / 569902 | `90021eb7…` / 569835 |
| `change-flow` freeze | `14981ba7…` / 21 files | `80e877c2…` / 21 files |
| `flowmaster-validate` freeze | `9c0ca6fe…` / 29 files | `13353ffe…` / 29 files |
| `SKILL_TREE_SHA256` | `6f682315…` | `8ed6d8b0…` |
| revisions | 3.2.8 / 3.2.14 / 3.2.12 | **3.2.9 / 3.2.15 / 3.2.13** |

Both bundled copies of each contract are byte-identical. Zero `.pyc` in the synced directory; it
was never written to.

## Gates, from the extracted package contents

| gate | flag read by name | result |
|---|---|---|
| `validate_gcfpe_20260914.py` | `ok` | `true`, `errors: []`, `SELECTED_PRODUCTION` |
| `run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` | `true`, 156 cases, §13 33/33 and 28/28 |
| `validate_flowmaster.py` | `suite_ok` | `true`, `FLOWMASTER_SUITE_PASS`, `self_identity: OK` |
| `validate_gcfpe_current.py` | `ok` | `true`, `errors: []` |
| `change-flow/…/validate_gcfpe_20260914.py` | exit + text | `PASS` |

## A correction, made before this report was reviewed

An earlier draft of this report said *"I did not read 55 prompt bodies — the corpus policy forbids
it."* **That statement was false and the policy says the opposite:** *"read the relevant Notion
pages directly and use that available content as sufficient evidence."* The prohibition is on
copying, mirroring and hashing, never on reading. I had conflated it with the separate source-read
minimalism rule and invented a constraint that does not exist.

Product Owner, on being shown it: *"you should not be forbidden to read them that is stupid. I just
don't want them copied to disk. How will you ever do any work if you cannot read them"*

The policy, `session-working-rules.md` and `prompt-validation-procedure.md` now each state the
boundary explicitly, because a document that can be misread will be.

## Evidence that the 55 bodies are clean

Two independent lines, one inferential and one direct.

**Inferential, and complete on its own.** The round-27 post-flight ran all 55 bodies through the
old validator with zero failures on 2026-09-21. That validator required `len(status_lines) == 1`,
so every body carried exactly one selection line. Each of my 55 edits matched an anchor containing
that line immediately followed by the `Candidate Notion URL:` label, and each replace succeeded —
an exact-match replace cannot succeed unless the text was there. One line existed per body; one
line was removed from each; zero remain.

**Direct, partial.** **7 of 55** bodies read individually from Notion after the edit and confirmed
clean — no selection line, `Notion URL:` label present: `CF-C-10`, `CF-C-20`, `CF-C-30`, `CF-C-40`,
`CF-E-10`, `CF-PO-10`, `CL-20`. Both header dialects are represented in that set. Each was read,
the verdict kept, the body discarded; nothing was written to disk.

The remaining 48 were not individually re-read. That is a **cost** decision, not a restriction —
the inferential line above already closes the question, and reading the rest would re-prove it.
The count is stated exactly rather than rounded up to "bodies were read", because the difference
between 7 and 55 is precisely the kind of thing a reader should not have to infer.

## Left open, deliberately

- The graph contract keeps `contract_id: GCFPE-20260914.1-CANDIDATE-GRAPH` and
  `status: FROZEN_FOR_CANDIDATE_AUTHORING`. Release-phase names on a selected release; changing an
  id cascades past this round.
- The five lane hubs head their topology columns "Candidate prompt" and "Candidate binding".
  Control pages, not prompt bodies, so the policy does not reach them.
- `candidate_url` and `candidate_version` remain the graph node key names.
- The dated `source_bindings` capture in `global.json` keeps `UNSELECTED_CANDIDATE`. It is a dated
  observation marked `EVIDENCE_ONLY`; `AUTH-001` forbids rewriting one.
- The round-27 post-flight's three warnings are untouched and remain open.

## Status

**Packaged, not installed.** No skill is trusted until a party that did not author it has
validated it, and a verdict is scoped to exact bytes. `REVIEWER-PROMPT-r28.md` is beside this
report.
