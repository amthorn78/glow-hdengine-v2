---
artifact_type: PROMPT_ENGINEER_SESSION_SUCCESSION_RECORD
artifact_version: "1.0"
created_date: 2026-09-19
status: BINDING
predecessor: PE32
successor: PE33
authority: Product Owner instruction, 2026-09-19
baseline: main @ e0c0ac3 (PR #417, merged) plus open PR #418
---

# PE32 → PE33 succession record

| | |
|---|---|
| Predecessor | **PE32** — `session_014ZinT4DGXAoN8bW3KQpzvi` — **RETIRED 2026-09-19** |
| Successor | **PE33** — `session_01Ch4SUzUjLbqL58QLQ8Y3XD` — initialized 2026-09-19 |
| Initialized from | branch `docs/20260919-addendum-schema-guard` (PR #418), which carries this record |
| Baseline | `main @ e0c0ac3`; open PR **#418**, branch `docs/20260919-addendum-schema-guard`, 5 ahead / 0 behind |

PE32's transcript is not a system of record and is not available to PE33 by design.

**Read this with `authoritative-surfaces.md` and `gcfpe.decision-record.md` (now D1–D16).**
Then `execution-and-delegation-model.md` before delegating, and
`ecosystem-change-management.md` before proposing any change — it carries the defect-class
catalogue. The round-by-round narrative is the Notion page *GCFPE Workflow Skill Repair —
Round Tracking — 091426.1*, which is current through round 16.

## Where the work stands

The plan's §10 dedicated skill-fit review is the gate. It has now run **seven times** and
has never returned `SKILL_FIT_CONFIRMED`. It gates §11 independent post-flight, which gates
the Product Owner promotion packet, which gates Epic Alpha resumption.

Everything else the reviews raised is closed. **One thing is not, and it is the whole gate.**

## The open item — the D8 guard, five versions, four defeats

D8 struck the post-addendum PF10 comparison check. A prohibited RS-40 branch implementing it
by function survived into the candidate graph and was removed (PR #417). D14 requires every
ruling to carry a guard that has been fired by an injected regression. That guard has been
written five times:

| Version | Basis | Defeated by |
|---|---|---|
| v1 | three English phrasings | paraphrase |
| v2 | `PF10` + one of four overlay tokens | synonym |
| v3 | allow-list keyed on `(prompt, branch_id)` | key reuse; non-boundary edge |
| v4 | digest over `(prompt, branch_id, condition)`, boundary-destined only | gate in `route_steps` / `notes`; non-boundary edge |
| **v5** | **whole branch object hashed, both surfaces, any destination** | **not yet reviewed** |

**v5 is packaged as round 16 and awaits installation.** Pin `dcfcf6c3d3189cb43f3067369e9288b7`,
144 rows, identical across all four bundled contract files. Eleven injected attacks all behave
correctly in PE32's testing; it has had **no independent review**.

**The lesson that cost four rounds:** every one of v1–v4 tried to *recognise* a prohibited
branch from its contents, and every one shipped with a comment asserting a robustness it did
not have. Those comments were worse than useless — a reviewer who reads a comment instead of
running an injection is stopped by it. v5 detects **change, not intent**, and says so. Do not
replace it with a cleverer recogniser. If it must change, keep the property that it consults
no vocabulary and privileges no field.

## Genuinely open — needs Product Owner input

1. **SF-05 — the body-level half of D8 is still vocabulary-based.** The registry's `CTR-002`
   assertions are the literals `state the mismatch` and `[Cc]ompare the current PF10`. The
   wordings that defeated v2–v4 contain neither. The registry's mechanism is regex over body
   text, so the structural fix used for the contract is not expressible there. **Do not widen
   the word list** — that is the move that failed four times. This needs a decision about how
   the behavioural half of D14 is satisfied for prompt bodies.

2. **The extraction convention is ambiguous.** The registry states the body identity as "the
   exact slice between the fetch result's `<content>` and `</content>` markers, with no
   trailing newline added". Read literally it keeps both boundary newlines and yields bodies
   two bytes larger than the registry's actual basis. The convention in force strips both.
   Proven twice: reverse-applying PE32's 30 edits reproduces the recorded pre-edit SHA-256 for
   21 of 21 under strip-both and 0 of 21 otherwise; and three untouched prompts reproduce their
   recorded digests only under strip-both. **The wording is unchanged pending a decision.** It
   defines the ecosystem's tamper-evidence and it silently corrupted one refresh already.

3. **`prompt_bodies_validated` is `false` in every validator run.** No body corpus exists on
   disk; `candidate/prompts/` is recorded as `HISTORICAL_LINEAGE_NOT_A_RESOLVABLE_PATH`. Every
   green flag covers contract, graph, fixtures and skills — **not** the 55 bodies, and none of
   the 55 rows' literal or regex assertions are exercised. The round-6 and round-7 reviewers
   each assembled and hash-verified a corpus themselves; nothing prevents the instruments from
   doing the same if a corpus is staged.

## Settled — do not reopen without new evidence

- **D16 — no DevOps skill.** `glow-hde-devops` is retired; none is installed, required, or to
  be created. **OPS-20 and the Ops lane execute natively with no skill binding, and that is
  correct by design, not a gap.** This closes §10 questions 1, 4 and 8.
- **`artifacts/ops/` and `artifacts/qa/` are governed locations**, named in PF02 §1001 and
  enumerated by filename in PF04 §3807–3814. They are *not* subject to the PE session's own
  write boundary, which covers only where **this session** may write. PE32 briefed a subagent
  that conflated the two and nearly deleted a Canon-mandated destination from OPS-10/OPS-20.
- **Dated records are not corrected.** Before/After token tables, readback receipts, the
  observational workspace skill registry, superseded checkpoint sections — each was accurate on
  its date. When an approved artifact disagrees with an unapproved one, fix the **authority
  relationship**, not the easier-to-edit fact. Recorded as `AUTH-001`.
- **The graph is rebuilt by script, never hand-edited.** Parts at `docs/graph/parts/`; the
  assembled graph is derived output and is never committed. Current token
  `55 nodes · 227 edges · 55 state_routes · 569,902 bytes · sha256 1d0b7258…`.

## Completed by PE32

- 30 edits across 21 prompt bodies: `artifact_version` removed from PF10 addendum field lists
  (9), QA removed from support-skill capability lists (18), three CL-40 prompt names corrected.
  Each body extracted twice independently and byte-identical; reverse-applying the edits
  reproduces the registry's pre-edit SHA-256 for 21 of 21.
- Addendum-schema guard on all 55 registry rows, anchored on function, five fixtures verified
  by mutation.
- The prohibited RS-40 branch removed from the parts and rebuilt by script (merged, PR #417).
- D16 recorded; the observational-registry disposition note added.
- `graph_proofs.semantic_branch_count` deleted — eleven candidate definitions tested, none
  produced 269, no validator read it.
- `tw-flowmaster` and `session-relay-flowmaster` corrected from the pre-PR-35 architecture;
  `glow-graph-contract`'s phantom orphan-route warning corrected.
- Notion skill-fit record brought current by **appended checkpoint**, not by editing history.

## PR #418 — transferred to PE33

Branch `docs/20260919-addendum-schema-guard`, 5 commits, 0 behind `origin/main`. Carries the
55-row addendum-schema guard, the `evidence_contract` refresh for the 21 edited prompts, the
run-evidence report, and the registry disposition note.

**Do not merge it until a §10 review returns clean against a frozen snapshot with v5
installed.** Nathan alone merges. PE32 held it for that reason and the reason still holds.

## Process faults PE32 made — do not repeat

- **Installed a skill package while a review was running.** §10 requires the review to run
  against the final installed snapshot; one that moves mid-run cannot be final. Freeze the tree,
  then review.
- **Claimed a guard was function-based on the strength of a rename test.** The test passed and
  the claim was still too strong, because it exercised only the axis the guard covered. A guard
  is proven against the attack actually run, and the attack worth running is the one a competent
  author produces by accident — a rewording, not a rename.
- **Read subsidiary section flags instead of a tool's own top-level flag.** Always read
  `ok`, `fixture_suite_ok`, `suite_ok`/`verdict`, and the suite result — never a green section
  flag while the overall flag is false.

## PE33's first actions, in order

1. Confirm round 16 is installed: full recursive diff against the package, and confirm
   `terminal_boundary_surface` hashes whole branches with no destination filter.
2. Freeze the tree. Announce no installs in flight.
3. Run the §10 dedicated skill-fit review against that frozen snapshot. Instruct the reviewer
   to attack v5 adversarially and to report the exact injected object and flags on any defeat.
4. Machine-verify every quote before accepting any finding. PE32 rejected two false positives
   across seven reviews by doing this, and accepted several corrections to its own work the
   same way.
5. If the verdict is `SKILL_FIT_CONFIRMED`, the §11 post-flight follows — run by an auditor who
   is neither the author nor the skill reviewer.

## How to work

Nathan alone merges; never merge, never enable auto-merge. The selected release
`GCFPE-20260913.1 / 091326.2 / 54` is never touched — its contracts and fixtures correctly
still contain the drainage lifecycle. Anything mentioning `HDE-EPIC040` is out of scope.
`docs/pfcanon/` is read-only. Prompts are authored in Notion in place, never mirrored into the
repository. Skills live in a one-way synced directory: edit working copies, package them, and
hand them to Nathan, because only he can install them.

Report findings the way `glow-po-reporting` requires: the correction first, plainly, not buried
under the work that surrounds it.
