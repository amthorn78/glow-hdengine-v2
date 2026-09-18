---
artifact_type: GCFPE_CONSOLIDATED_PASS_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-18
release: GCFPE-20260914.1 / 091426.1 / 55
scope: The 37 prompts formerly assigned to Batches 3-6, plus a release-wide gate over all 55
authority: Product Owner authorization, 2026-09-18, under D12
verdict: CONSOLIDATED_PASS_COMPLETE_GATE_PASSED
---

# Consolidated pass — repair report

The single pass that replaced Batches 3–6 under D12, plus the release-wide gate.

## Scope and coverage

| Lane | Prompts | Formerly |
|---|---|---|
| PR | PR-10, PR-20, PR-30, PR-35, RS-10, RS-20, RS-30, RS-40, PR-40, PR-50 | Batch 3 |
| QA | QA-10, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, QA-100, QA-110, QA-120 | Batch 4 |
| Escalation / Ops / Doc | ESC-10, ESC-25, ESC-30, ESC-40, OPS-10, OPS-20, OPS-30, DOC-10, DOC-20 | Batch 5 |
| Closure | CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, CL-20, CL-30, CL-40 | Batch 6 |

**37 prompts, no duplicates, none unassigned.** 37 + the 18 of Batches 1–2 = 55. All four
lanes ran concurrently. Every lane returned its full roster: 10/10, 10/10, 9/9, 8/8.

## Method

Discovery was precomputed centrally so coverage is arithmetic. Each worker received an exact
scope, the settled rules, the approved contract row, and a byte-exact local copy of the body;
workers did not fetch from Notion and did not see each other's work or the graph.

**Every quoted piece of evidence was machine-verified.** 62 findings carried 56 quotes; all 56
were confirmed byte-for-byte against the body files by script, with 6 findings correctly using
an empty quote for an absence claim. **Zero quotes failed verification.**

Prompt bodies were extracted programmatically from the capture workers' transcripts — sliced
file → script → file, never retyped — per EVID-001.

## Findings and disposition

**62 findings across 37 prompts.** 9 prompts were clean.

| Disposition | Findings |
|---|---|
| Registry regenerated from the graph | 33 |
| Reviewed, no change, reason recorded | 15 |
| False positive, resolved with evidence | 8 |
| Body repair applied | 4 |
| Registry input token corrected | 2 |

### The dominant cause — one control defect, not 42 prompt defects

The registry's routing and state declarations were never derived from the bodies. **Two
independent instruments agree against it**: the graph parts, and four workers reading bodies
blind. 28 rows disagreed on consumers, 15 on output states; 33 rows were regenerated.

The sharpest example: `PR-30`'s declared success state was `MERGE_PENDING`, which its body
forbids, while its actual success state `PR_CANDIDATE_PUBLISHED` was undeclared; the lane's
busiest edge `PR-30 → PR-35` was missing, and a twice-prohibited `PR-30 → PR-40` edge was
declared.

**Two checks of my own were discarded before use**, both because they failed on nearly every
member of the set, which under D11 indicts the check: an artifact-equality closure test
(109 of 114 pairs "failed" — consumers declare references such as `SPECIFICATION_ID` where
producers declare artifacts such as `CRD_SPECIFICATION`), and a state comparison drawn from
`state_vocabularies`, which is populated only where an explicit vocabulary exists. The correct
sources are graph edges and `node.result_states`.

### Body repairs applied — both settled-ruling violations that used no banned token

**`RS-40` reinstated the retired PF10 addendum drainage lifecycle by function.** It compared
current PF10 against the addendum's stable anchor and normalized approved delta and **stopped
terminally on a mismatch**, stranding an approved rescope with an open PR whenever the Product
Owner's paste had not yet landed or was worded differently. D8 forbids a mandatory
post-addendum check and any replacement for it. It was also the only one of the seven
addendum-related prompts missing the settled clause that a PF10 read is *"evidence of what was
read, never a gate on later work."*

The drainage-removal pass missed this because it searched for retired tokens and `RS-40`
contains none. It was found by judging function. The comparison and its terminal stop are
deleted; the `SOURCE_RESOLUTION_ERROR` predicate and the fresh read are kept; the provenance
clause, which appears verbatim in 36 other bodies, is added, together with an explicit
prohibition on ever comparing or waiting again.

**`QA-10` permitted writing its three governed artifacts off-repository**, in three passages,
contradicting its own Required result and Save sections which specify `docs/ephemeral/`. It
evaded the D7 guard because it named no Drive location. Both defects are isolated:
`off-repositor` appears in no other body, and the only Drive sentence anywhere in the 55 is the
single permitted conditional one.

**`OPS-20`** carried stale copied text naming `ESC-10` where the caution concerns this prompt.
Corrected; `ESC-10` no longer appears in `OPS-20`.

All three edits were verified by **isolated readback** — a worker that had not seen the
intended text fetched the pages and answered factual questions about them.

### Registry repairs applied

- **33 rows regenerated**: `outputs[].consumers`, `outputs[].states` and `required_interfaces`
  now derive from the graph.
- **10 legacy input tokens** replaced across 8 prompts, in every case with the artifact a
  current prompt actually produces: `REMEDIATION_PLAN_REVIEW_ID` → `REMEDIATION_REVIEW_ID`
  (ESC-40 produces it), `REMEDIATION_PLAN_ID` → `REMEDIATION_PROPOSAL_ID` (ESC-30),
  `QA_GUIDE_ID` → `LIVE_QA_GUIDE_ID` (QA-20).
- **`PR-40`'s declared inputs** were a single string truncated after the first of eight bullets;
  the full list is captured.
- **All 55 `evidence_contract` entries recomputed** — see below.

### False positives, resolved with evidence rather than carried

- `ESC-40` "routing contradiction": the sentence is **shared boilerplate in 9 bodies**
  constraining RS-40's behaviour, not an ESC-40 routing instruction.
- `CL-E-40 → CL-E-20` "dead end": the loop closes through `CL-E-30 → CL-E-40`, an edge the
  worker did not check.
- `CL-40`, `QA-10`, `PR-40` "over-binding" destinations: these are the graph's deliberate
  `ORIGINAL_NATIVE_STAGE` runtime-resolved boundary node, not undeclared edges.
- `ESC-40`'s missing session-identity paragraph: only 16 of 37 bodies carry it and no consumer
  reads it. Restoring it would be normalisation without a consumer (NORM-001). **No change.**
- `CL-E-20`'s state-to-consumer mapping: the registry schema carries a flat consumer list and
  cannot express per-state routing. The graph does, through edge state predicates. **No change;
  a schema limit, not a row defect.**

## The evidence defect found at the start of the pass

Comparing the stored captures against live Notion — rather than against each other, which is
how the earlier check was run — showed that **25 of 55 approved `evidence_contract` entries did
not reproduce**:

- **24** reproduced only with a trailing newline the page does not contain. The corpus had been
  assembled by two different methods and no single documented rule reproduced all 55.
- **1**, `ESC-40`, did not reproduce at all: its stored capture carried an **841-byte paragraph
  the live page has never had**, and `page_last_edited_at` proves the page was not edited after
  the capture. The contaminated capture is what the approved registry was built from.

All 55 entries are recomputed from the live captures, and each now records the reproduction
rule explicitly:

> Extraction convention: the exact slice between the fetch result's `<content>` and `</content>`
> markers, with no trailing newline added

**55 of 55 now reproduce.** This closes the defect class rather than the instance.

## Guards added, and proved

The registry previously had **no guard at all** against the retired drainage tokens: the
drainage removal was verified once and nothing prevented reintroduction. Added across all 55
rows:

| Guard | Rule |
|---|---|
| `off-repositor` forbidden | D7 storage |
| `state the mismatch` forbidden | D8 post-addendum check |
| `[Cc]ompare the current PF10` forbidden | D8 post-addendum check |
| The 13 retired drainage tokens forbidden | D6 |
| `never a gate on later work` required in `QA-70` and `RS-40` | D5 provenance |

Assertions rose from **499 to 721**. Tested against **eight injected regressions** — the
off-repository permission, the PF10 mismatch gate, the comparison sentence, Canon resolved from
a Drive folder, a direct Drive link, an `EPHEMERAL_DRIVE` token, a retired drain token, and
deletion of the provenance clause — **all eight were caught**, and the clean control passed at
0 failing. A negative control confirms the guard does **not** fire on legitimate Canon drainage
text (*"Preserve the permanent Canon drainage target and owner"*), which must survive.

## Release-wide gate

| Check | Result |
|---|---|
| Registry validator on all 55 live bodies | **721 assertions, 0 failing** |
| `evidence_contract` reproduces from the live page | **55 / 55** |
| Registry consumers vs graph | **0 rows drift** |
| Registry `required_interfaces` vs graph | **0 rows drift** |
| Graph nodes / edges | **55 / 227** |
| Graph edges with an unresolved endpoint | **0** |
| Prompt-originated inbound edges to `PR-50` | **0** |
| PF10 addendum producers | **exactly the six** |
| D7 Drive markers across 55 bodies | **0** |
| Retired drainage tokens across 55 bodies | **0** |
| Off-repository storage permission | **0** |
| PF10 mismatch gate | **0** |
| Legitimate Canon disposition preserved | PF09 in 14 bodies · `CANON_CONFLICT_REGISTER` in 32 · `NEW_CANON` in 9 · `CANON_RECONCILIATION` in 9 |

## Open items

**None.** No finding was carried forward unresolved and no Product Owner decision was required:
every finding resolved from evidence in the corpus, the graph, or a settled ruling.

## Graph rebuild — proof token reproduced

The graph was rebuilt from the committed parts with `scripts/graph_parts.py build`, which
ships with the `glow-graph-contract` skill:

    build: 55 nodes, 227 edges, 55 state_routes
           embedded JSON 571493 bytes  sha256 3b54d6207126e0a99b7b98cd660a2bf43245b2a049f498ebbd8cc9891e14b09d
           validation PASS

**The proof token reproduces exactly**, and the builder reported no orphan-route warning — the
long-standing `RS-40.drain_verified` orphan is confirmed closed. The assembled graph was built
to the session scratchpad and is not committed, per D7.

> An earlier revision of this report claimed the assembly script was absent from the
> repository and that the token could not be reproduced. That was wrong. The script is shipped
> with the `glow-graph-contract` skill — by design, because it is reusable behaviour rather
> than data — and `authoritative-surfaces.md` lists that skill. The error came from searching
> only the repository tree instead of reading the document that says where things live. It is
> the same failure this ecosystem keeps producing: judging by what a search returned rather
> than establishing what is actually there.
