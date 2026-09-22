---
artifact_type: PROMPT_ENGINEER_SESSION_SUCCESSION_RECORD
artifact_version: "1.0"
created_date: 2026-09-22
status: BINDING
predecessor: PE35
successor: PE36
authority: Product Owner instruction, 2026-09-22
baseline: main @ 3e943ad (PR #455, merged) at authorship; PE36 initialized against main @ 76689ac.
role_change: true
---

# PE35 → PE36 succession record

| | |
|---|---|
| Predecessor | **PE35** — `session_01WRuFH1x24NoYSsjoLJ4zGt` — **RETIRED 2026-09-22** |
| Successor | **PE36** — `session_01Aniz3abekzoEbAax1UbWar` — initialized 2026-09-22 |
| Charter | **General prompt engineering and maintenance.** Not a repair campaign |
| Baseline | `main @ 3e943ad`, **zero open pull requests** |
| Installed | `change-flow` `80e877c2…` · `flowmaster-validate` `b9ca212a…` — round 30, digest-verified 2026-09-22 |

PE35's transcript is not a system of record and is not available to PE36 by design.

**Read this with `authoritative-surfaces.md` and `gcfpe.decision-record.md` (now D1–D18).** Then
`execution-and-delegation-model.md` before delegating, and `ecosystem-change-management.md` before
proposing any change. The round-by-round narrative is the Notion page *GCFPE Workflow Skill Repair
— Round Tracking — 091426.1*, current through round 30 §10.

## The charter changed, and that is the most important line in this record

**PE31 through PE35 were a repair campaign. It finished.** The release is promoted and selected,
both skills are installed and independently confirmed, Alpha is resumed, and the repository has
zero open pull requests. There is no gate waiting on you.

PE36 is **general prompt engineering and maintenance**: steady state. The failure mode of a
successor inheriting a campaign posture is to go looking for a crisis and manufacture one — to
open a round because rounds are what the predecessor did. **Do not open a repair round without a
defect that someone can name.** The deferred items below are deferred *by the Product Owner*, with
owners; they are not a backlog to burn down on your own initiative.

### You have one authorized task, and it is named

> **Correction, 2026-09-22.** This record originally said the queue was empty by design. That was
> true when it was written and stopped being true the same day: the Product Owner authorized the
> skill revision round that item 1 below had recorded as needing authorization.

**`docs/ephemeral/pe36.task-01/TASK-01-skill-write-boundary-revision.md` is your first task.** It
is authorized, scoped, and has a definition of done. Start there rather than asking what the work
is. Everything else in "Open — carried" remains deferred with its existing owner.

## Where the work stands

| | |
|---|---|
| Selected release | `GCFPE-20260914.1` / `091426.1` / **55** — promoted 2026-09-21 (`D17`), predecessors archived intact |
| Selection authority | the **GCFPE Membership and Release Register**, and nothing else. Every control reads `REGISTER_CONTROLLED` |
| Skills | round 30 installed and digest-verified. `FLOWMASTER_VALIDATE_REVISION` 3.2.16, `validator_revision` 3.2.14 at exactly four sites, `CHANGE_FLOW_SPECIALIZATION_REVISION` 3.2.9, `SKILL_TREE_SHA256` `eb9634d6…` |
| §10 verdict | **`SKILL_FIT_CONFIRMED`**, round 30, bound to `ed7041c0…` and `0e00084e…`, void for other bytes |
| Alpha | **`ALPHA_RESUMED`** 2026-09-21 (`D18`). `HDE-EPIC040-PR04` has run `PR-10` (#452) and `PR-20` (#453, DRAFT, finding F01) |
| Pins | contract `2b78f877…` / 606657 · graph `90021eb7…` / 569835 · `55 nodes · 227 edges · 55 state_routes` |

**`HDE-EPIC040` is product work and is not yours.** It is listed so you recognise it, not so you
touch it.

## Open — carried, with owners

1. **Three skills contradict the Notion write-boundary policy** (`notion-write-boundary.md`, PO
   2026-09-22). **Now authorized as PE36's Task 01** — see the brief above. Identified by PE35 and
   deliberately **not modified** then, per the instruction that created the policy. `glow-workspace-currency` is the serious one: *"close every task by writing any state
   change back to Notion"* makes a Notion write the default close-out of every task, and its
   description is permanently in context. `glow-artifact-storage` and `glow-write-boundary` carry
   milder versions. **The documentation now says the right thing and the skills still say the old
   thing, and skills are what load into a session.** A revision round needs Product Owner
   authorization; it has not been given.

2. **`AF-004`** — 40 of 55 prompt bodies have never been scanned for a decorated governance line.
   Deferred by the Product Owner, 2026-09-21, to the next `GCFPE-MGMT-10` run. Round 30 widened
   what such a scan would catch in **both** directions: it catches every good-faith rendering now,
   and it also newly fires on a line that names the forbidden field while forbidding it. No real
   instance is observed in the 15 bodies read. If a sweep finds one, the fix is narrow — require a
   governance *value* after the key, or exempt a line containing a prohibition word — **never a
   looser strip.**

3. **`AF-001`, `AF-002`, `AF-003`** stand as recorded on the Alpha Feedback page. All Product
   Owner-deferred. `AF-002` carries the release-scope trap `SCOPE-002` — older-release contracts
   correctly still contain the retired drainage lifecycle and **must not be "fixed"**.

4. **`reconciliation-backlog.md`** holds the surfaces still carrying retired drainage, Drive
   storage and struck-check language. The `HDE Change Flow Overview`'s operating paragraphs were
   annotated 2026-09-22 rather than rewritten, and that annotation names what is retired.

## Settled — do not reopen without new evidence

- **Reading prompts is not restricted. Copying them is.** `prompt-corpus-policy.md`. The corpus is
  never mirrored, exported, hashed or cached to disk. Read one or read all fifty-five, as the work
  requires. PE35 misread this as a prohibition on reading and had to be corrected by the Product
  Owner; the carve-out now sits at the exact rule that was misread.
- **A prompt body carries behaviour, not governance state.** `prompt-body-content-policy.md`.
  Selection, lifecycle and release-phase state live in the register, never in a body.
- **Notion writes are not the default outcome of executing a prompt.**
  `notion-write-boundary.md`. A plausible destination is not a destination rule.
- **`AUTH-001`** — a dated record is never corrected in place. Add a successor beside it. A
  *current-state* field (`status`, `gate`, frontmatter) is corrected in place; the dated entries
  below it are not.
- **No page asserts its own selection.** Every control reads `REGISTER_CONTROLLED`. A heading that
  calls itself "Sole operative Alpha state" on a page that is not the Flow Index is a defect —
  that exact defect was found twice on 2026-09-22.
- **The graph is rebuilt by script, never hand-edited.** Parts at `docs/graph/parts/`; the
  assembled graph is derived output and is never committed.
- **Freeze digests are rooted at the skill directory, never the synced tree.** A whole-tree digest
  is hostage to unrelated skills the sync layer updates.
- **`SKILL_TREE_SHA256` is a tamper check, not a version check.** A coherently built wrong package
  self-certifies. Only comparing the installed digest to the one the §10 verdict named catches it.
- **`D16` — no DevOps skill.** The Ops lane executes natively with no skill binding, by design.

## Completed by PE35

- **Promotion of `GCFPE-20260914.1 / 091426.1 / 55`** as a coordinated transaction in the mandated
  order — 10 bindings activated and read back, register updated **last**, production validation
  rerun, then 56 pages archived intact. No receipt inferred. `D17`.
- **Alpha resumed** (`D18`), with `ALPHA_RESUMED` minted because the vocabulary had no token for
  Alpha actually running.
- **Rounds 28, 29 and 30** — governance state removed from all 55 prompt bodies; three coupled
  validator defects that made a promoted release unreachable; the decorated-line matcher; the
  revision-identity collision. Round 30 returned `SKILL_FIT_CONFIRMED` and is installed.
- **Procedure moved out of Notion into `docs/prompt_ecosystem_management/`** at the Product
  Owner's direction, with the Hub reduced to briefs pointing at the repository.
- **Three policies written**: prompt-body content, corpus reading-vs-copying, Notion write
  boundaries.
- **`HDE-EPIC040` lineage transition reference and the PR04 `PR-10` kickoff handoff**, which
  unblocked the Epic.
- **A stale-state sweep** that found a top-level navigation page still declaring the superseded
  54-member release a day after promotion.

## Process faults PE35 made — do not repeat

These cost real rounds. They are listed because each is a habit, not an accident.

- **Broke the revision-identity rule twice, in the file that states it.** Rounds 28 and 29 shipped
  mutually incompatible validators both advertising `3.2.15` / `3.2.13`, while PE35 was editing the
  paragraph in that same `SKILL.md` describing round 24's identical finding. **Narrating a rule is
  not applying it.** `skill-identity-and-freeze.md` now carries the imperative version — diff the
  advertised identity against the previous package before packaging, and treat a match as a defect.
- **Reported a state without reading it back.** Pushed a commit to a branch whose pull request had
  already merged, then told the Product Owner the PR "now carries both" — an inference from having
  pushed. It did not. **Check the PR's state before pushing to its branch, and read the result
  before describing it.**
- **Claimed an archive had happened before it had.** Caught and corrected in the same turn, but the
  claim was written first and that is the fault.
- **Overstated two claims in a report** (`C1`, `C3` of round 30) in the round whose subject was an
  identity claim that overstated its evidence. The reviewer had to narrow both.
- **Delivered a reviewer prompt pinned to a commit**, two behind the branch, whose §6 and §7 stated
  the opposite of the policy in force. **Pin reviewer prompts to the branch HEAD, and say what to
  do if the branch has merged and been deleted** — that happened two rounds running.
- **Wrote that enforcement existed before it did**, in the policy document that required it.
- **Set eight control pages to `status: SELECTED`**, against the design in which no page asserts
  its own selection. Corrected to `REGISTER_CONTROLLED`.
- **Let Notion mangle a table** containing escaped pipes, twice, and only found it by reading back.
  Notion normalises inline code adjacent to bold and breaks `\|` in cells. **Use a fenced code
  block for literal lines, and always read back a structured write.**

The through-line: **every one of these was a claim made before the measurement that would have
checked it.** The measurement was always cheap.

## PE36's first actions, in order

1. **Confirm the baseline yourself.** `python3 docs/prompt_ecosystem_management/freeze.py` against
   each installed skill directory; compare to `80e877c2…` and `b9ca212a…`. Confirm `main` is at
   `3e943ad` or later and that nothing is open that you did not open.
2. **Read the three policies before touching anything** — corpus, prompt-body content, Notion write
   boundary. Two of them exist because a predecessor got the rule wrong.
3. **Read `docs/ephemeral/pe36.task-01/TASK-01-skill-write-boundary-revision.md` and do it.**
   It is your authorized first task. Read the three skills yourself before trusting the brief's
   quotations of them — PE35 quoted them from the installed tree, but a brief is not the artifact.
4. **Find out what already exists before writing anything** — search both Notion and the
   repository. Most defects in this ecosystem's history were a second copy of something that
   already existed.
5. **After Task 01, do not invent the next one.** Ask. The campaign is over; the deferred items
   have owners and are not yours to start unbidden.

## How to work

Nathan alone merges; never merge, never enable auto-merge. Skills live in a one-way synced
directory — never write to it; copy to scratch, run with `PYTHONDONTWRITEBYTECODE=1`, package, and
hand the `.skill` files to Nathan, because only he can install them. Independent §10 validation is
mandatory before any install, and a prior verdict never carries to new bytes. Prompt bodies are
authored in Notion in place and never mirrored into the repository. `docs/pfcanon/` is read-only.
Write only to `docs/ephemeral/`, `docs/graph/`, `docs/prompt_ecosystem_management/`, Notion where a
destination rule allows it, and installed skills.

Report the way `glow-po-reporting` requires: the answer first, the correction plainly and not
buried, and close with `DECISION NEEDED`, `NOTHING NEEDED` or `IN FLIGHT`. Record before reporting,
and read the record back before claiming it.
