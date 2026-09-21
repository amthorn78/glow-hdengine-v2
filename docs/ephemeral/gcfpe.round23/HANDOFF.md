---
artifact_type: PROMPT_ECOSYSTEM_SESSION_HANDOFF
artifact_version: "1.0"
created_date: 2026-09-21
author: PE34
successor: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
status: HANDOFF_OPEN
subject: SF10-10 — PO ruling on the PF10 roster; ship it with SF10-09; deliver the package file
---

# Handoff — PE34 to PE35

PE34's context is fading. This is the complete state and the work to finish. Read `AGENTS.md` first;
it governs. Nothing in this file overrides it.

## The Product Owner's ruling — this is the authority for SF10-10

Verbatim, 2026-09-21:

> "no, initial authoring does not require a PF10 built in this addendum. It is an input only, like
> all other pfcanon, but should not be a named input or output for an authoring prompt."

**What it settles.** PF10 is one PFCanon source among others, reached through the general
PFCanon-resolution rule that every body already carries. An **authoring prompt must not be required
to name PF10 as an input or an output.** So requiring a CF Specification author's body to state
"current controlled PF10 Markdown" is requiring the wrong thing.

**What to change.** Exempt the four CF Specification authors — `CF-C-20`, `CF-C-40`, `CF-E-20`,
`CF-E-40` — from `current_pf10_markdown_required`. That roster becomes the **ten** non-CF writers,
matching `active_addenda_required`. `authoring_context_required` stays at **twelve** (exempt only
`CF-C-20`, `CF-E-20`). Membership in `EXPECTED_WRITERS` stays at **fourteen** — the four keep every
other obligation, `approved_base_live_reauthoring_refused` above all.

**Expected measurement: the end-to-end validator goes 4 errors → 0.** Verify it; do not assume it.

**Why this is not the exemption round 21 rejected.** `SFR-01`'s R1 rejected an identical-looking
exemption because PE34 asserted it without evidence, and the bodies contradicted it. This is a
Product Owner ruling on what an authoring prompt should *say* — the owning authority for a semantic
question. Record it as the PO ruling it is, cited verbatim. Do not re-derive it from body
quotations, and do not present PE34's earlier body reading as its justification.

## Also outstanding: PE34 never delivered a package file

The PO's second correction: **"you did not create a skill."** PE34 reported package digests but left
the `.skill` archives in an ephemeral session scratchpad the PO cannot reach, and that container is
reclaimed. **A round is not delivered until the installable artifact is in the PO's hands.** Hand the
file over explicitly — do not report a digest and stop.

## State at handoff

**Installed tree** — `/root/.claude/skills/synced/<uuid>/`, one-way synced. **Never write to it.**
Always copy to scratch and run with `PYTHONDONTWRITEBYTECODE=1`.

| | value |
|---|---|
| files / digest | 318 / `2f5d14a691e0c28292227f17a6688ae6c2f6437255b2305c36299dff057da3fa` |
| `change-flow` | `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.7` |
| `flowmaster-validate` | `FLOWMASTER_VALIDATE_REVISION: 3.2.8` |
| `validator_revision` | `3.2.7` at four sites |
| candidate contract | `5d871b5d052f3ebabc850696db860802bac2b4ce44ad9e6b39a18ac784b18f36` / 610625 bytes |
| end-to-end, 55 bodies | exit 1 — 4 errors, all `CURRENT_PF10_MARKDOWN`, on the four CF authors |

`.bucket-<uuid>` and an empty `.staging/` sit in the **parent** `synced/` directory, outside the
skill tree — sync infrastructure, not skill files. Root the freeze at the skill tree or the count
reads 319.

**SF10-09 is NOT installed.** Its repair is committed as
`docs/ephemeral/gcfpe.round22/sf10-09.patch` (216 lines, on `main` at `22f45ec`) and is fully
reproducible from it. Its package `d5228e093dc871dae30a5f6d94afc36dc3aeeff6cc74fff9af6ef3e9283e3ee4`
existed only in PE34's scratch and is **superseded** — SF10-10 changes the same skill.

**Ship SF10-09 and SF10-10 together as one round.** SF10-09 alone was never reviewed or installed,
so there is no reason to split them, and splitting costs an extra §10 cycle.

## What SF10-10 touches

The roster lives in the **contract**, so this is a contract change and the hash-pin chain moves —
unlike SF10-09, which touched only validator logic.

1. `plan_writer_contract.body_obligation_ids.current_pf10_markdown_required` → the ten non-CF
   writers, in **both** bundled copies of the contract (`change-flow/references/` and
   `flowmaster-validate/references/`), which must stay byte-identical.
2. `EXPECTED_BODY_OBLIGATION_IDS["current_pf10_markdown_required"]` in
   `flowmaster-validate/scripts/validate_gcfpe_20260914.py` → `EXPECTED_WRITERS - SPECIFICATION_AUTHORS`.
3. The hash-pin chain fires in sequence — `CONTRACT_HASH` → `PROFILE_BUNDLED_CONTRACT_HASH` →
   `PROFILE_CONTRACT_PIN`. Update `EXPECTED_CANDIDATE_CONTRACT_SHA256` and
   `EXPECTED_CANDIDATE_CONTRACT_BYTES`, plus the validation profile's
   `candidate_contract.sha256` / `byte_count`.
4. Revisions. `change-flow` changes (bundled contract), so `CHANGE_FLOW_SPECIALIZATION_REVISION`
   **3.2.7 → 3.2.8** at its **six** sites, plus the profile's `installed_skill_revisions.change-flow`.
   `FLOWMASTER_VALIDATE_REVISION` **3.2.8 → 3.2.10** if SF10-09's 3.2.9 bump is folded in, and
   `validator_revision` **3.2.7 → 3.2.8** at its four sites. Verify each count by grep; do not trust
   this list.
5. **Both packages ship** this round, because both skills change. They install together.
6. Fixtures: the roster-drift fixture `reject-body-obligation-roster-drift` targets
   `active_addenda_required`; check that the duplicate-id and drift cases still fire once the
   `current_pf10_markdown_required` roster is no longer all fourteen. A fixture that stops firing is
   the finding, not the nuisance.

Contract bytes round-trip exactly with
`json.dumps(d, indent=2, sort_keys=True, ensure_ascii=False) + "\n"`. Never hand-edit
`glow-hde-canonical-change-flow-r1.json` — it is the 2.0.0 oracle.

## The corpus

The 55 prompt bodies are **authored in Notion in place** and were cached in PE34's scratchpad, which
is gone. **PE35 must re-fetch them from Notion** to run the end-to-end and body-fixture suites. The
harness reads a directory of `<PROMPT-ID>.md` files passed as `--prompt-dir`.

Invocations that work — PE34 wasted a cycle getting these wrong, and every apparent failure was an
invocation artifact, not a defect:

```
python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow \
    --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json \
    [--prompt-dir <bodies>]
python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow \
    --contract <same> [--prompt-dir <bodies>]
python3 flowmaster-validate/scripts/validate_flowmaster.py          # needs the FULL skill set copied
python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow   # the argument is required
python3 change-flow/scripts/validate_gcfpe_20260914.py
```

Expected on the installed tree before any change: contract fixtures 155, body fixtures 179 once
SF10-09 is reapplied (145 / 169 without it); `FLOWMASTER_SUITE_PASS` with 6 skills; every gate
exit 0 except the end-to-end.

## Process that is not optional

- **The PO alone merges and the PO alone installs.** Never merge, never enable auto-merge, never
  write to the synced skills directory.
- **Independent validation is mandatory for every skill change** (Ops Hub). The package needs its own
  §10 from `SFR-01` before install; round 21's `SKILL_FIT_CONFIRMED` is scoped to its own digests.
- **Always hand the PO a reviewer prompt with the package** (Ops Hub). Never ask the reviewer to
  verify something only this session can reach — that was R1's error and PE34 nearly repeated it.
- **No skill may be installed while a review is running.** Freeze the tree, then review.
- One completed review cycle at a time; no overlapping cycles. Assess the whole review, fix related
  findings together, make the smallest coherent correction, test it fully locally, then confirm the
  summary, the evidence and the implementation agree.
- **Review scope:** changes confined to `docs/crd/`, `docs/ephemeral/`, `docs/graph/`,
  `docs/pfcanon/`, `docs/plans/`, `docs/prompt_ecosystem_management/`, `docs/qa/`, `docs/run/` are
  out of code-review scope — do not respond to reviews on them. Reviews on runtime and governance
  paths, `AGENTS.md` included, are handled normally.
- **Write boundary:** no repository write outside `docs/ephemeral/`, `docs/graph/`,
  `docs/prompt_ecosystem_management/` unless the PO instructed that specific change.
- **Dated records are never corrected** (`AUTH-001`) — add a successor sentence beside the old one.
- Derive every hash from the artifact; never transcribe one. A failed grep is not a file defect.
- Report: first line is the answer; close with `DECISION NEEDED` / `NOTHING NEEDED` / `IN FLIGHT`,
  and let the tag describe the session's actual state. Record in Notion before reporting.
- Untouchable: the selected release `GCFPE-20260913.1 / 091326.2 / 54`; anything naming
  `HDE-EPIC040`; `docs/pfcanon/**` (cite by title/§ only); prompt bodies, which are authored in
  Notion in place and never mirrored into the repository.

## Measurement discipline, from PE34's own errors this session

Each of these cost a cycle and each was caught by measuring rather than reasoning:

- A freeze rooted one directory too high reported 319 files and a non-comparable digest. **Root the
  measurement where the claim is.**
- A first encoding of the SF10-09 predicate raised on `IA-40`, whose body legitimately factors the
  source rule into its general PFCanon sentence. **Run the whole corpus before believing a
  predicate.**
- A corpus falsifier failed to discriminate because the old check's strictness defect was masked by
  its own looseness. **A test that cannot fail proves nothing** — check which of your cases actually
  fail on the old code, and say so.
- `grep -c` counts lines, not occurrences.
- A pipeline that truncates output also replaces the producer's exit status; `out=$(producer)`
  preserves it but `local x=$(producer)`, `echo "$(producer)"` and `producer | head` do not.

## Notion

Round tracking: page `3df4590a-05eb-81e0-9144-c1c36ffad28b` — append the round entry there before
reporting. Ops Hub: page `3ce4590a-05eb-814f-8892-f88ff8539308` — holds the independent-validation
and reviewer-prompt rules.

## Definition of done for SF10-10

1. Roster changed per the PO ruling, in both contract copies and the validator.
2. Hash-pin chain and all revision counts updated, each verified by grep.
3. SF10-09's predicate re-encoding carried in, reproduced from `sf10-09.patch`.
4. End-to-end measured at **0 errors**; every other gate exit 0 on both trees; fixture counts up,
   none failing; zero `.pyc`; installed tree byte-identical before and after.
5. Both `.skill` packages built, extracted and compared path-by-path against the tested tree, with
   no entries outside the skill root.
6. **The package files delivered to the PO**, not just their digests.
7. A reviewer prompt delivered with them.
8. Round report under `docs/ephemeral/gcfpe.round23/`, Notion updated, branch pushed.
9. Nothing installed until `SFR-01` rules on those exact bytes.
