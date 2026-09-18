---
artifact_type: PROMPT_ECOSYSTEM_CHANGE_MANAGEMENT_MODEL
artifact_version: "1.1"
created_date: 2026-09-18
status: BINDING
authority: Product Owner approval, 2026-09-18 (strategic assessment of the repair process)
applies_to: The prompt-management ecosystem generally, not one release
supersedes_for_planning: The six-batch repair sequence (Batches 3-6) — see execution-and-delegation-model.md §0A
---

# Ecosystem change management

**Why this document exists.** The 2026-09 repair took weeks because the ecosystem had no
change process — only a remediation plan. Every finding was treated as novel, every
decision was re-litigated, and the controls that were supposed to catch defects were
themselves the largest source of them. This document exists so the *next* change is
routine work rather than another repair effort.

It is the process half. `execution-and-delegation-model.md` is the mechanics half (how
work is delegated and verified). `gcfpe.decision-record.md` holds the rulings this
process must not relitigate. `authoritative-surfaces.md` says where truth lives.

---

## 1. The governing observation

**Two completed batches found the prompts substantially correct and the defects in the
controls.**

| Batch | Findings | Prompt edits required |
|---|---|---|
| Batch 1 | its own report: *"Root cause found at the control, not the prompts"* | control-side |
| Batch 2 | 22 of 22 contract findings closed on the prompt side | **zero** |

The two repairs that did change prompt bodies — drainage removal (142 passage families /
280 occurrences, 54 prompts) and the Drive → repository storage pass (333 passages, 44
prompts) — were each **one ruling applied corpus-wide**, and both ran outside the batch
sequence entirely.

**The consequence for change management:** a change to this ecosystem is normally a
change to *a rule*, not to *a prompt*. Scope it by rule and apply it to every prompt the
rule reaches, in one authorization. Splitting one rule across several authorizations
creates several chances to apply it several different ways.

---

## 2. The change lifecycle

Five steps. Every ecosystem change runs all five, however small. The cost of the process
scales with the change; the *shape* does not.

### Step 1 — Classify the change

Before any scoping, name which of these it is. The class determines everything that
follows.

| Class | What it is | Authorization | Verification |
|---|---|---|---|
| **A — Rule change** | A settled behaviour is changed for the whole corpus (Drive is not a storage authority; drainage is retired) | **Product Owner.** Recorded in `gcfpe.decision-record.md` as a D-number *before* execution | Corpus-wide gate |
| **B — Rule application** | An already-ruled decision is carried into prompts, graph, registry | **Coordinator.** The ruling is the authorization | Isolated readback of everything changed + guard regex |
| **C — Control repair** | The registry, graph, validator or CI is wrong about correct prompts | **Coordinator**, with the corrected control recorded | The control is tested against injected regressions |
| **D — Prompt defect** | One prompt genuinely fails its own contract | **Coordinator** | The registry assertion that should have caught it, added |
| **E — Normalisation** | Structural symmetry with no functional consumer | **Do not do it.** See §4, `NORM-001` | — |

Most work is B and C. **If a finding cannot be placed in a class, it has not been
understood yet — establish what the affected prompt actually does before proceeding.**

### Step 2 — Scope by measurement, not by pattern

Binding, and the single most expensive lesson of the repair. Discovery by enumerating
known phrasings undercounted three separate times:

| Measured | By pattern | By reading | Error |
|---|---|---|---|
| Drainage passage families | 93 | 142 | −35% |
| PFCanon-through-Drive prompts | 39 | 42 | −7% |
| Storage-pass occurrence lines | 236 | 333 | −29% |

The method that works: **match the broad term, subtract the permitted exceptions, and
read the remainder in context.** Never assemble a list of the phrasings seen so far —
that finds only the phrasings already seen.

The 236 → 333 miss is the instructive one. Applying the first pass alone would have left
twelve prompts contradicting themselves two lines apart. It was caught because two
independent workers flagged lines their instructions did not account for. **Build that
escape hatch into every worker brief: "report any in-scope line your instructions do not
cover."**

A scope figure is not reportable until it has been measured this way. State the method
alongside the number.

### Step 3 — Apply in one controlled pass

Per `execution-and-delegation-model.md`. The essentials:

- Precompute the hit list centrally so coverage is arithmetic, not trust.
- Hand each worker an exact scope and the settled rules; require a structured return.
- **Converge on existing wording.** Do not invent new phrasing for a rule already applied
  elsewhere in the corpus.
- Cross-cutting decisions are taken once by the coordinator and applied uniformly, never
  delegated per lane.

### Step 4 — Verify against behaviour, in isolation

Three properties, all required:

1. **Isolated.** A worker producing evidence must not see the expected answer
   (`execution-and-delegation-model.md` §7).
2. **Programmatic.** Evidence is extracted by an exact documented slice, file → script →
   file. **Never retyped.** Both defects found in the 2026-09-18 verification were in the
   evidence, not the source: a worker silently flattened curly quotes in three captures,
   and the pre-edit fetch corpus dropped a whole line from two prompts and altered a
   sentence in a third. Live Notion was correct every time. Byte comparison caught both;
   worker self-reports did not.
3. **Behavioural.** The check must distinguish a correct artifact from an incorrect one.
   See D11 and §4 `CHK-001`.

### Step 5 — Record where it can be found again

**A conversation is not a record.** A finding, ruling or correction exists only if it is
in a repository document or a Notion page, at a named path.

| What | Where |
|---|---|
| A Product Owner ruling and its consequences | `gcfpe.decision-record.md`, next D-number |
| A change to how work is executed or verified | `execution-and-delegation-model.md` |
| A change to what a prompt must satisfy | `project-prompt-contract-registry.md` (with assertions) |
| Run evidence for a specific pass | `docs/ephemeral/<release>.<pass>.repair-report.md` |
| Anything a successor session must not rediscover | the succession record |
| Operational status, navigation, plan state | Notion |

---

## 3. Standing instruments

What the repair built that is reusable. These are the reason the next change should be
routine; keep them working rather than rebuilding them.

| Instrument | Where | What it gives you |
|---|---|---|
| **Contract registry with behavioural assertions** | `project-prompt-contract-registry.md` | 499 assertions across 55 prompts, 0 failing. `required_regex` binds release identity and Canon source; `forbidden_regex` guards D7 against Drive reintroduction in any of its four forms. |
| **Governance audit** | `amthor-workspace-governance-audit` skill | Executes the registry assertions on demand. Not on push — this material is outside application CI by design (see `README.md`). |
| **Graph parts + proof token** | `docs/graph/parts/`, rebuilt on demand | Machine-readable restatement of the corpus. Derived output is never committed (D7); the token `55 nodes · 227 edges · 55 state_routes · 571,513 bytes · sha256 d7832c73…` proves a rebuild matched. |
| **Isolated-readback harness** | pattern, `execution-and-delegation-model.md` §7 | Proves an applied change landed, without the verifier knowing the expectation. |
| **Regression-injection test** | pattern, D11 | Proves a guard actually catches what it claims. The D7 guard was tested against five injected regressions and a clean control. |
| **Succession record** | `pe-succession/` | Lets a session be replaced without losing the inheritance. |
| **Reporting standard** | `glow-po-reporting` skill + succession record | How the Product Owner is asked for a decision and told about completed work. |
| **Write-boundary skills** | `glow-write-boundary`, `glow-artifact-storage` | The four open paths and the storage precedence chain, enforced at the tool layer. |

**A guard that has never been tested against a regression is not a guard.** Any new
assertion added to the registry ships with the injected regression that proves it fires.

---

## 4. Defect-class catalogue

Every class below was observed in this ecosystem. The catalogue exists so a future
session recognises a class on sight instead of re-deriving it. The first four are
**control defects** — the dominant class, and the one the batch model was worst at
finding.

### CHK-001 — A check that cannot fail selectively

**Symptom:** an assertion fails on every member of a set, or on none.
**Example:** `select only the controlled Markdown lane` was asserted on 45 rows, was
absent from all 55 bodies, and had never been present in any of them. Meanwhile the 44
prompts that named Drive as the Canon authority were flagged by nothing.
**Rule:** a check must distinguish a correct artifact from an incorrect one. A check
failing uniformly is telling you about the check. **70 of 269 assertions were this.**
**Repair:** check the behaviour — the named location, the failure state, the prohibited
source — not the sentence the artifact uses to express it. (D11)

### CHK-002 — Wording asserted as if it were behaviour

**Symptom:** an exact-substring assertion breaks on a legitimate variant.
**Example:** the release carries two header conventions — `Prompt version: \`091426.1\``
in eleven prompts, `Prompt Version: 091426.1` in forty-four. Both declare the identity
the rule guarantees; an exact literal failed eleven correct prompts.
**Repair:** tolerant `required_regex` on the identity, not the sentence.

### NAME-001 — Judged by name instead of function

**Symptom:** something is classified by what it is called, and the classification is
wrong.
**Examples, all from one session:** `audit/docdeltas/PF10_*` looked like Canon material
and is application-side delivery evidence; a registry assertion demanded PF10 from a
prompt-repair tool that never touches build notes; and the word "drain" names two
unrelated concepts, one retired and one permanent — a lexical sweep on it destroys
legitimate Canon disposition.
**Rule:** classify by function, every time, including when the name is unambiguous-looking.
**This is the ecosystem's single most recurrent failure mode.**

### SCOPE-001 — Pattern-derived scope reported as measured

**Symptom:** a scope figure derived by enumerating known phrasings, reported without its
method.
**Consequence when acted on:** partial application. Twelve prompts would have carried
contradictory statements two lines apart.
**Repair:** §2 above. State the method with the number.

### NORM-001 — Normalisation without a consumer

**Symptom:** a proposal to make artifacts structurally symmetric because they differ.
**Example:** `rollback` present in IA-20 and absent from IA-10. No prompt in the release
requires a rollback section; nothing consumes it. The Product Owner ruled it out.
**Rule:** establish the consumer before proposing the repair. Structural asymmetry is not
a defect.

### EVID-001 — Evidence corrupted in transit

**Symptom:** verification evidence differs from the live source in ways the source never
had. Curly quotes flattened; a dropped line; an altered sentence.
**Cause:** a worker retyping or paraphrasing rather than slicing.
**Repair:** programmatic extraction and byte comparison (§2, Step 4). Treat a
worker's *report* that bytes match as unverified.

### DISP-001 — "Non-blocking" used as a disposition

**Symptom:** a finding is recorded as non-blocking and carried forward unresolved.
**Consequence:** it survives across sessions, accumulating, and then costs a dedicated
pass.
**Rule (Product Owner, 2026-09-18):** "non-blocking" means only that it does not prevent
the current execution step. It is **not** a resolution. Drive every finding to resolution
in the session that finds it, or name the specific Product Owner decision it needs.

### STALE-001 — A committed copy of derived output

**Symptom:** a derived artifact is stored, drifts from its source, and is then read as
authority.
**Example:** the committed assembled graph still carried the entire retired drainage
machine and would have handed it back to a future session.
**Rule:** derived output is never committed. Use a proof token. Where a snapshot must be
kept, label its scope and its staleness.

### FUNC-001 — A retired behaviour reinstated by function

**Symptom:** a prompt violates a settled ruling while containing none of that ruling's banned
vocabulary, so every token sweep passes it.
**Example:** `RS-40` compared current PF10 against an addendum's normalized approved delta and
stopped terminally on a mismatch — the retired PF10 drainage lifecycle, rebuilt out of ordinary
words, in a body carrying none of the thirteen retired tokens. `QA-10` permitted writing its
governed artifacts *off-repository*, a D7 violation naming no Drive location.
**Why it survives:** the sweep that retires a behaviour is normally written against the
vocabulary the behaviour used, so it cannot see the behaviour expressed differently.
**Repair:** ask what the prompt makes an agent *do*. For each retired behaviour, state the
functional test — here, *does anything gate later work on whether the addendum has landed?* —
and apply it to the bodies, not to a word list. (D14)

### GUARD-001 — A ruling applied without a guard

**Symptom:** a ruling was applied and verified once, and nothing prevents its reintroduction.
**Example:** the thirteen retired drainage tokens had **no assertion anywhere in the registry**
after the drainage removal. A whole repair rested on a one-time verification.
**Rule:** a ruling is not applied until a guard exists that would catch the reintroduction and
that guard has been fired by an injected regression. Ship the guard with the repair, in the same
change. (D14)

### DERIV-001 — A derived field authored by hand

**Symptom:** two artifacts state the same fact independently, and drift.
**Example:** the registry's `consumers`, `required_interfaces` and output `states` were authored
by hand although the graph already modelled routing. 33 of 55 rows had drifted; `PR-30` declared
a success state its own body forbids.
**Rule:** name the authority for each fact and derive the rest. Where a machine-readable source
already carries a fact, the second copy is generated, never typed. (D13)

### PAIR-001 — A stale copy and a disabled checker hiding each other

**Symptom:** an invariant is violated for a long time and every check passes, because the only
instrument that tests it cannot run, and the data it would have tested is a stale copy in which
the violation does not exist.
**Example:** ten qualifying-approval branches kept `terminal_for_invocation: true` after the
drainage removal re-pointed them and gave them a handoff (D15). `flowmaster-validate` is the
only thing that tests the terminal/handoff invariant, and it aborted before running (F6); the
graph copy bundled beside it was the pre-D6 version in which those branches really were
terminal. Neither artifact looked broken on its own.
**Rule:** when a validator cannot run, the invariants it alone enforces are **unverified**, not
passing. Record them as unverified and fix the validator before trusting the surface. Treat a
committed copy of derived output as suspect whenever the checker that reads it is broken —
`STALE-001` and a dead guard are the same failure seen from two sides.

### SCOPE-002 — A shared surface edited outside its release scope

**Symptom:** a "fix" applied to text that is correct for the *selected* release.
**Example:** workspace Notion surfaces carry blocks for both `091326.2` (live, still has
drainage, correct) and `091426.1` (candidate, retired). Editing the former would
misrepresent the live system.
**Rule:** find the nearest heading and establish the release scope before editing. When a
surface serves both, **label the scope rather than rewrite the block.**

---

## 5. Definition of done

A change to this ecosystem is done when all seven hold. Not six.

1. **Applied** everywhere the rule reaches, with coverage arithmetic from a measured
   scope (§2).
2. **Verified** by isolated readback, extracted programmatically, compared by bytes.
3. **Guarded** — a registry assertion exists that would catch the reintroduction, it has been
   tested against an injected regression, and where the change retires a behaviour the guard
   tests the behaviour, not the vocabulary it happened to use (FUNC-001, GUARD-001).
4. **Reconciled** — graph parts rebuilt and closing, registry validator at zero failures,
   producer/consumer interfaces closing.
5. **Recorded** at a named path (§2, Step 5) — repository document, Notion page, or both
   where each is authoritative for its layer.
6. **No open findings.** Every finding resolved, or named as a specific Product Owner
   decision with a brief. Nothing parked (`DISP-001`).
7. **Successor-legible.** A session with no transcript can pick it up from the succession
   record and the three governing documents alone.

---

## 6. Authorization: what needs the Product Owner

Deliberately short. The repair cost time to over-escalation as much as to defects.

**His:**

- A **Class A rule change** — new settled behaviour for the corpus, or reversing one.
- **Promotion** of a release candidate.
- Anything **expensive or hard to reverse**: touching the selected release, deleting
  evidence, changing the storage architecture.
- A genuine **policy question** with no evidence-determined answer.

**Not his — the coordinator's, and asking costs two rounds:**

- Applying a ruling he has already made, including its implementation consequences.
- Repairing a control that is wrong about correct prompts.
- Any finding resolvable from evidence in the corpus.

**How to ask,** when it is genuinely his: the four-part brief in the succession record's
*How to report to Nathan* and the `glow-po-reporting` skill — what the thing does in
plain language; what concretely breaks in a real run if nothing changes; the options with
their costs; the recommendation and why. **A schema difference is not an impact.** If you
cannot say what the affected prompt does, you are not ready to ask.

---

## 7. Applying this to a routine future change

Worked shape, for a change of ordinary size:

1. **Classify** (§2 Step 1). Usually B or C. If A, get the ruling recorded first.
2. **Measure** the surface by broad match minus permitted exceptions; read the remainder.
3. **Check the catalogue** (§4) before writing a brief — most findings are a known class.
4. **Apply** in one pass, converging on existing wording, workers briefed with the escape
   hatch.
5. **Verify** isolated, programmatic, behavioural.
6. **Guard** — add or adjust the registry assertion; test it against an injected
   regression.
7. **Gate** once, corpus-wide: graph closure, registry validator, interface closure,
   readback of everything changed.
8. **Record** and close. Nothing parked.

A change that fits this shape does not need a batch plan, a phased sequence, or
per-stage authorization. **That is the point.**
