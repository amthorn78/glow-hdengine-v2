---
artifact_type: "GCFPE_MODIFICATION_RECORD"
format: "2.1"
modification_id: "MODIFICATION-20261027-gcfpe-backlog-open-items"
status: "EXECUTING"
targets: ["prompt", "skill", "rule", "graph", "registry", "notion_control", "tool"]
gate_tier: 2
closure: {"upstream": ["CF-C-20", "CF-C-30", "CF-C-40", "CF-E-20", "CF-E-30", "CF-E-40", "CL-20", "CL-30", "CL-C-10", "CL-E-10", "CL-E-40", "DOC-10", "DOC-20", "ESC-30", "ESC-40", "IA-10", "IA-20", "IA-30", "IA-40", "IA-50", "MGR-10", "OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-35", "PR-40", "QA-10", "QA-100", "QA-110", "QA-120", "QA-20", "QA-50", "QA-60", "QA-70", "QA-80", "QA-90", "RS-10", "RS-20", "RS-30", "RS-40"], "downstream": ["CF-C-10", "CF-C-40", "CF-E-10", "CF-E-40", "CF-PO-10", "CL-20", "CL-30", "CL-40", "CL-C-10", "CL-E-10", "CL-E-20", "CL-E-30", "CL-E-40", "DOC-10", "DOC-20", "ESC-10", "ESC-25", "ESC-30", "IA-10", "IA-20", "IA-30", "IA-40", "IA-50", "IA-60", "OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-35", "PR-40", "QA-10", "QA-100", "QA-110", "QA-120", "QA-20", "QA-50", "QA-60", "QA-70", "QA-80", "QA-90", "RS-10", "RS-20", "RS-30", "RS-40"], "state_sharers": ["CF-C-10", "CF-C-20", "CF-C-30", "CF-E-10", "CF-E-20", "CF-E-30", "CL-40", "CL-C-10", "CL-E-10", "CL-E-20", "CL-E-30", "DOC-10", "DOC-20", "ESC-25", "ESC-30", "ESC-40", "IA-10", "IA-20", "IA-30", "IA-40", "IA-60", "OPS-10", "OPS-20", "OPS-30", "PR-10", "PR-20", "PR-30", "PR-35", "PR-40", "QA-100", "QA-110", "QA-20", "QA-50", "QA-60", "QA-70", "QA-80", "QA-90", "RS-20", "RS-30", "RS-40", "UTIL-10"]}
readiness: "SPLIT_RECOMMENDED"
override: {"by": "", "overrides": [], "reason": ""}
interaction_cost_predicted: 23
interaction_cost_actual:
estimate: {"plan": "10–16 h and 6–10M aggregate tokens: a fresh read of about 56 pages for the dry run; operations for about 35 bodies, the CL-05 member, PE and two control pages; graph-part edits for five parts and a new part; registry guards with injected regressions for about twelve rules; redlines for three to five skill packages; the R1 successor rows; the qualification and promotion plans; then one FULL round of two reviewers and at most one DIFF_CHECK", "execute": "24–40 h and 12–20M aggregate tokens, excluding Product Owner waiting time: about 40 Notion body operations with fresh-read checks, a new member page, three to five packages through one D24 cycle, the qualification gates and post-flight, and, under DN-1 option D2, the promotion transaction of about 80 Notion writes and moves plus the sweep by literal"}
reviews: [{"mode": "ANALYZE", "kind": "DRY_RUN", "date": "2026-10-27", "required_open": 0, "outcome": "Author dry run, read-only, before any full review: 55 of 55 closure.py calls exit 0; the graph build reproduces D29's token (55 nodes, 235 edges, 593,569 bytes, sha256 43f84f29…); 8 of 9 installed skill digests equal their recorded values, and typesafe-scoring has no repository record; 240 of 240 repository and canon quotes match their sources; 52 Notion quotes are reproduced by an independent sweep and none conflicts; the decisive sentences of MB-001, MB-002, MB-012, MB-020, MB-021, MB-026 and MB-030 re-read on fresh fetches and in the graph parts; the record validator passes. No defect in the analysis is open from the dry run."}, {"mode": "ANALYZE", "kind": "FULL", "date": "2026-10-27", "required_open": 2, "outcome": "Round 1 at 4780f64a, two fresh reviewers, briefs at 8134979c. A: 2 required. R-A1 (R1): ITEM-14 confined PF04 §9.7.7's IA-30 business-case gate to the initial Plan review, so a material Plan delta adding or changing a work unit would pass unchecked. R-A2 (R3): DN-6 (a) recommended a commit route that the installed glow-write-boundary excludes, since an earlier task's instruction 'is not that instruction'. A also listed 24. B: 0 required, 19 listed. Both confirmed A-1's class reading, CD-1, CD-4, MB-010's test on the bodies they fetched, the derived items and tier 2. Distinct required count 2, none in repaired text. The author repairs R-A1 and R-A2 only (ITEM-14, ITEM-15, PART-03's targets, A-5, DN-6); the listed findings stay listed (D26-A rule 4); one DIFF_CHECK follows."}, {"mode": "ANALYZE", "kind": "DIFF_CHECK", "date": "2026-10-27", "required_open": 0, "outcome": "Reviewer C, who was neither A nor B, checked 02ba1797..46160491 under BRIEF-ANALYZE-DIFF.md (43fe026b). R-A1 fixed: the two named IA-30 reviews are its only approving modes. R-A2 fixed: A-5's quotes match the installed skill, and DN-6 (a) now asks in the committing session; ITEM-22 and PF19 §3.4.3 hold under every option. No new required defect. 5 LISTED (L-C1 to L-C5). Required count 2 to 0. This is the last ANALYZE review D26-A allows; the analysis returns to Nathan with every open finding listed."}, {"mode": "PLAN", "kind": "DRY_RUN", "date": "2026-10-27", "required_open": 0, "outcome": "Author dry run, read-only, of every normal-path gate (N0 to N10, plan/dry_run_102726.py). The first, on reads after 08:16:14Z, failed N2, N3, N7, N8 and N9 (13 uncovered guard rows; Notion's <code>/\\_ fetch rendering against Markdown-form assertions; CL-05's missing contract parent; three pre-existing suite findings; QA-120 intake markers). One bounded repair under D26-F trigger 2 (C-15 to C-22). The second, at acc39b04 on reads after 09:38:45Z, passes all eleven: 57/57 pages, 559/559 operations, 0 of 756 guard rows failing after, 56/56 registry rows with 972 injected regressions reported, 282 control operations rendered with none refused. Receipts plan/dry-run-1.json and plan/dry-run.json."}, {"mode": "PLAN", "kind": "FULL", "date": "2026-10-27", "required_open": 4, "outcome": "Round 1 at b0f2481, two fresh reviewers, briefs at 6385dbf. A: 2 required. R-1 (R1, R4): X1's and X26's repository edits had no committed applier, W1's note was stored anchored before D30, and the repository and notion-control guards ran only on fixtures, so X8 passed with a surviving retired line. R-2 (R3): L-C1, accepted by Nathan as a risk, was repaired without his opt-in in IA-30's delta review, G-W2-EM-2 and D30-A. A listed 15. B: 2 required. R-B1 (R1): the X17 post-flight would pipe raw fetches outside C-15's normalized form. R-B2 (R2): C-REG wrote the stale pull request #768 on the register. B listed 10. Distinct required 4, none in text the dry-run repair added (R-B1 sits in C-15's reach). Both confirmed the cascade (C-1), its fixpoint, the binding pass, C-15, C-16, CD-6, CD-9, PE's general rules, PART-13 and the D17 order. The author repairs the four only (C-23 to C-26); one DIFF_CHECK follows."}, {"mode": "PLAN", "kind": "DIFF_CHECK", "date": "2026-10-27", "required_open": 0, "outcome": "Reviewer C, who was neither A nor B, checked f2346b2..885638d under BRIEF-PLAN-DIFF.md (6474eca). R-1, R-2, R-B1 and R-B2 fixed, none with a new defect: repo_edits_102726.py self-test 14/14 and X1 then X26 clean on a scratch copy; the PART-17 guards reproduce the plan's counts on fresh Hub and register reads; D30 states exactly DN-3 (b). 8 LISTED (L-D1 to L-D8). Required count 4 to 0. This is the last PLAN review D26-A allows; the plan returns to Nathan with every open finding listed."}]
items:
  - {"id": "ITEM-01", "statement": "DOC-20 no longer routes a second PR-40 entry for a merge whose lineage PR-40 has already accepted (D23-E, once per merge).", "source": "MB-001", "disposition": ""}
  - {"id": "ITEM-02", "statement": "PR-20's description of PR-40 says that a REJECT re-plans through PR-20 (D23-F), not that it returns findings to the PR owner.", "source": "MB-002", "disposition": ""}
  - {"id": "ITEM-03", "statement": "The register-bound handoff operating procedure points to a current placement source, not to a stale dated report.", "source": "MB-004", "disposition": ""}
  - {"id": "ITEM-04", "statement": "One glow-merged-change-attribution-lock content is bound to revision 1.2.0, and any other content carries an unspent revision.", "source": "MB-005", "disposition": ""}
  - {"id": "ITEM-05", "statement": "Both briefs in reviewer-prompt-template.md name AGENTS.md among their governing documents and ask for a Canon relied on block.", "source": "MB-006", "disposition": ""}
  - {"id": "ITEM-06", "statement": "PE's generic addendum-authoring clause numbers every agent-authored addendum at creation (PF06 §0.1A), outside GCFPE as inside it.", "source": "MB-007", "disposition": ""}
  - {"id": "ITEM-07", "statement": "Two qualifying approvals made before one paste cannot leave two addenda with one number, or the Product Owner accepts that risk.", "source": "MB-009", "disposition": ""}
  - {"id": "ITEM-08", "statement": "No handoff or package sentence tells an agent that a handoff carries lineage, session identity or a complete native input package (D23-B, D27).", "source": "MB-010", "disposition": ""}
  - {"id": "ITEM-09", "statement": "PE Metaprompt gives no instruction scoped to the finished 20260914 repair.", "source": "MB-011", "disposition": ""}
  - {"id": "ITEM-10", "statement": "Neither the Glow Operations Hub nor the release register states 091426.1-era GCFPE policy as current.", "source": "MB-012", "disposition": ""}
  - {"id": "ITEM-11", "statement": "PR-35 fixes a review finding only on a real input, answers any other with the traced path and the stated limit, and asks one design question when a finding class repeats (PF06 §1.1.4, PF27).", "source": "MB-013", "disposition": ""}
  - {"id": "ITEM-12", "statement": "glow-hde-pr-development states the same finding rule as PR-35.", "source": "MB-014", "disposition": ""}
  - {"id": "ITEM-13", "statement": "Specification approval (CF-C-30, CF-E-30) blocks a requirement without a business case (PF04 §9.7.7).", "source": "MB-015", "disposition": ""}
  - {"id": "ITEM-14", "statement": "IA-30 checks each work unit's business case, in its initial Plan review and, for every work unit a material Plan delta adds or changes, in its material Plan-delta review (PF04 §9.7.7).", "source": "MB-016 (business case)", "disposition": ""}
  - {"id": "ITEM-15", "statement": "IA-30 rejects an acceptance criterion that depends on emulating an external system, in its initial Plan review and, for every work unit a material Plan delta adds or changes, in its material Plan-delta review.", "source": "MB-016 (emulation)", "disposition": ""}
  - {"id": "ITEM-16", "statement": "PR-10 carries the work unit's business case into the PR Instruction, and the Proceed package PR-20 prepares carries it (PF04 §9.7.7).", "source": "MB-017 (business case)", "disposition": ""}
  - {"id": "ITEM-17", "statement": "PR-10 requires a pin or a stated precondition, never a fidelity target, for a unit that depends on an external system.", "source": "MB-017 (pin or precondition)", "disposition": ""}
  - {"id": "ITEM-18", "statement": "PR-20 plans each component's real-input set and one refusal outside it, and limits boundary cases to real inputs.", "source": "MB-018", "disposition": ""}
  - {"id": "ITEM-19", "statement": "Whether a work unit's business-case measure was met is recorded where the Product Owner places it.", "source": "MB-019", "disposition": ""}
  - {"id": "ITEM-20", "statement": "IA-40's REDLINE_INCOMPLETE return to the same Isis reviewer continues to IA-30, which can receive and revise the returned redline in both lanes.", "source": "MB-020", "disposition": ""}
  - {"id": "ITEM-21", "statement": "An approved QA Plan that a delivered change has made stale has a lawful authoring and review route.", "source": "MB-021", "disposition": ""}
  - {"id": "ITEM-22", "statement": "QA-100 and QA-90 never leave published QA evidence only in scratch storage (PF19 §3.4.3).", "source": "MB-022", "disposition": ""}
  - {"id": "ITEM-23", "statement": "PR-35 fixes every real-input P1 and declines only a non-real-input P1, Product Owner first, and PR-40 checks that no real-input P1 was declined or left open (PF06 §1.1.4, PF27).", "source": "MB-023", "disposition": ""}
  - {"id": "ITEM-24", "statement": "glow-hde-pr-development no longer names the deprecated Codex security review.", "source": "MB-024", "disposition": ""}
  - {"id": "ITEM-25", "statement": "The bodies' provenance-procedure clause is settled: kept as an accepted risk, removed, or installed.", "source": "MB-025", "disposition": ""}
  - {"id": "ITEM-26", "statement": "QA-70 applies an operational coherence test on every review, including the review after QA-80, and QA-80 and QA-50 support it (the brief's requests 1 to 6).", "source": "MB-026", "disposition": ""}
  - {"id": "ITEM-27", "statement": "A DO_NOT_CLOSE for missing close evidence has a lawful next prompt, and no closure text treats the close mutation set as post-closure administration.", "source": "MB-027", "disposition": ""}
  - {"id": "ITEM-28", "statement": "An unchanged prompt in TW or another non-GCFPE ecosystem keeps its page across releases, as a GCFPE member does under D23-G.", "source": "MB-028", "disposition": ""}
  - {"id": "ITEM-29", "statement": "A relay-safety recommendation, if the Product Owner wants one, is defined and scoped.", "source": "MB-029", "disposition": ""}
  - {"id": "ITEM-30", "statement": "The close-mutation-set stage CL-05 is a release member, entered from QA-120 PASS and from a closure DO_NOT_CLOSE, and exiting to the closure decision (PF06 §3.5.1).", "source": "MB-030", "disposition": ""}
  - {"id": "ITEM-31", "statement": "The successor release that carries this Modification's prompt and skill parts is qualified, and its promotion packet is returned to Nathan.", "source": "Derived: D23-G and PF04 §9.1.6, one coherent successor selection for every member change", "disposition": ""}
  - {"id": "ITEM-32", "statement": "The promotion transaction runs after Nathan's exact promotion approval, if he gives it to this Modification under DN-1.", "source": "Derived: DN-1", "disposition": ""}
  - {"id": "ITEM-33", "statement": "glow-hde-pr-development SKILL.md:184 no longer cites a drained PF10 addendum by number.", "source": "DN-12 rider 1, approved 2026-10-27 (A-11)", "disposition": ""}
  - {"id": "ITEM-34", "statement": "PE Metaprompt no longer labels GCFPE-20261009.1 as the candidate.", "source": "DN-12 rider 2, approved 2026-10-27", "disposition": ""}
  - {"id": "ITEM-35", "statement": "ecosystem-change-management.md section 3 shows the current graph proof token, not the pre-D29 one.", "source": "DN-12 rider 3, approved 2026-10-27 (J-12)", "disposition": ""}
  - {"id": "ITEM-36", "statement": "PE Metaprompt no longer credits the TypeSafe rule to a drained HDE Build Notes addendum.", "source": "Nathan's DN-12 condition, 2026-10-27 (A-11, J-9 in part)", "disposition": ""}
parts:
  - {"id": "PART-01", "name": "PR review findings on real inputs (PF06 §1.1.4, PF27)", "items": ["ITEM-11", "ITEM-12", "ITEM-23"], "class": "B", "after": []}
  - {"id": "PART-02", "name": "Codex security review wording", "items": ["ITEM-24"], "class": "B", "after": []}
  - {"id": "PART-03", "name": "Business case per requirement and work unit (PF04 §9.7.7)", "items": ["ITEM-13", "ITEM-14", "ITEM-16"], "class": "B", "after": []}
  - {"id": "PART-04", "name": "Plan-side real inputs and no emulation", "items": ["ITEM-15", "ITEM-17", "ITEM-18"], "class": "A", "after": []}
  - {"id": "PART-05", "name": "Business-case measure record", "items": ["ITEM-19"], "class": "A", "after": []}
  - {"id": "PART-06", "name": "PR-20's description of a PR-40 REJECT (D23-F)", "items": ["ITEM-02"], "class": "B", "after": []}
  - {"id": "PART-07", "name": "Handoff package sentences (D23-B)", "items": ["ITEM-08"], "class": "B", "after": []}
  - {"id": "PART-08", "name": "DOC-20's second PR-40 entry (D23-E)", "items": ["ITEM-01"], "class": "B", "after": []}
  - {"id": "PART-09", "name": "IA-40 redline return to IA-30", "items": ["ITEM-20"], "class": "D", "after": []}
  - {"id": "PART-10", "name": "Approved QA Plan change route", "items": ["ITEM-21"], "class": "A", "after": []}
  - {"id": "PART-11", "name": "QA-70 coherence, QA-80 reshape and QA-50 CI binding", "items": ["ITEM-26"], "class": "B", "after": ["PART-10"]}
  - {"id": "PART-12", "name": "QA evidence persisted in the repository (PF19 §3.4.3)", "items": ["ITEM-22"], "class": "B", "after": []}
  - {"id": "PART-13", "name": "Close-mutation-set stage CL-05 (PF06 §3.5.1)", "items": ["ITEM-30", "ITEM-27"], "class": "B", "after": []}
  - {"id": "PART-14", "name": "PE Metaprompt: stale repair-scoped passages", "items": ["ITEM-09"], "class": "B", "after": []}
  - {"id": "PART-15", "name": "PE generic addendum clause outside GCFPE", "items": ["ITEM-06"], "class": "B", "after": []}
  - {"id": "PART-16", "name": "Concurrent addendum numbering", "items": ["ITEM-07"], "class": "A", "after": []}
  - {"id": "PART-17", "name": "Glow Operations Hub and register: 091426.1-era policy", "items": ["ITEM-10"], "class": "B", "after": []}
  - {"id": "PART-18", "name": "Provenance-procedure clause", "items": ["ITEM-25"], "class": "B", "after": []}
  - {"id": "PART-19", "name": "v5.0.0 operating procedure successor", "items": ["ITEM-03"], "class": "C", "after": []}
  - {"id": "PART-20", "name": "Attribution-lock revision identity", "items": ["ITEM-04"], "class": "C", "after": []}
  - {"id": "PART-21", "name": "Review briefs: Canon relied on", "items": ["ITEM-05"], "class": "C", "after": []}
  - {"id": "PART-22", "name": "Unchanged prompts outside GCFPE keep their pages", "items": ["ITEM-28"], "class": "A", "after": []}
  - {"id": "PART-23", "name": "Relay-safety scoring", "items": ["ITEM-29"], "class": "A", "after": []}
  - {"id": "PART-24", "name": "Successor release qualification and promotion packet", "items": ["ITEM-31"], "class": "C", "after": ["PART-01", "PART-02", "PART-03", "PART-04", "PART-05", "PART-06", "PART-07", "PART-08", "PART-09", "PART-10", "PART-11", "PART-12", "PART-13", "PART-14", "PART-15", "PART-16", "PART-18", "PART-26", "PART-27"]}
  - {"id": "PART-25", "name": "Promotion transaction", "items": ["ITEM-32"], "class": "B", "after": ["PART-24"]}
  - {"id": "PART-26", "name": "Stale drained-addendum citations (glow-hde-pr-development, PE)", "items": ["ITEM-33", "ITEM-36"], "class": "B", "after": []}
  - {"id": "PART-27", "name": "PE's candidate label for GCFPE-20261009.1", "items": ["ITEM-34"], "class": "B", "after": []}
  - {"id": "PART-28", "name": "Pre-D29 proof token in ecosystem-change-management.md", "items": ["ITEM-35"], "class": "C", "after": []}
request: "MODE = ANALYZE. Subject: every open item on the GCFPE Modification Backlog https://app.notion.com/p/3e54590a05eb81eb818fd0f42045167a"
requested_by: "Nathan"
analyze_approved_by: "Nathan"
analyze_approved_date: "2026-10-27"
item_count_at_approval: 36
plan_approved_by: "Nathan"
plan_approved_date: "2026-10-27"
supersedes: ""
spawned_from: ""
shares_package_with: []
---

# MODIFICATION-20261027-gcfpe-backlog-open-items

**ANALYZE result: all 28 open backlog entries are still live in 100926.1, and canon moved under them on 2026-10-27.**

- PF10 v13.8.9 carries no addenda; its rules now sit in permanent canon (PF04 v2.8.8, PF06 v2.5.5, PF19 v3.0.7, PF27 v2.0.6).
  - Ten entries now rest on permanent canon instead of an addendum.
  - Five rest, wholly or in part, on rules that reached no permanent home.
- Measured scope is wider than the entries name: 35 of 55 bodies, a new 56th member (CL-05), PE, the Hub and register, the graph, the registry, and three to five skill packages.
- Landing any prompt change needs a successor release (D23-G; PF04 §9.1.6) and a promotion, which GCFPE-MGMT-10 does not execute.
- Twelve decisions are Nathan's (§A.7).
- MB-029 cannot be scoped until he defines it, so a split is recommended for it alone.
- Nothing has been edited, packaged, installed or selected.

## §A — Analysis

### 1. Request, invocation and record

- **The invocation.** Nathan, 2026-10-27, invoked [GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1](https://app.notion.com/p/3f74590a05eb81b69bd8c27106f7a59d) with `MODE = ANALYZE` and the subject "every open item on the GCFPE Modification Backlog". This is the selected release's member, read in full.
  - The invocation carried this session's TypeSafe v8.2 reading, cell *Opus 5.5 at extra high*, flagged "boundary between high and extra high".
  - It states no pick, so none is recorded.
- **The backlog.** [GCFPE Modification Backlog](https://app.notion.com/p/3e54590a05eb81eb818fd0f42045167a), last edited 2026-10-26T02:46Z, was read in full (76,713 characters).
  - It holds 30 entries: 28 `OPEN`, and MB-003 and MB-008 `CLOSED`.
  - This record takes the 28 as items. MB-016 and MB-017 each carry two rules with different authority, so each becomes two items.
  - Two items are derived for the release that lands the prompt changes (§A.4, ITEM-31 and ITEM-32).
- **No other Modification covers these entries.** Searched:
  - `main`: 16 records, all `COMPLETE` or `ABANDONED`;
  - every remote branch: no `docs/*-modification-*` branch exists, and the other `claude/` branches carry no Modification;
  - the backlog itself: no entry is marked taken.
- **The record.** It is new, created by this ANALYZE from `modification-template.md` at format 2.1.
- **Branch deviation, disclosed.** MGMT-10 names `docs/20261027-modification-gcfpe-backlog-open-items`. This session's harness requires `claude/cool-bardeen-zwduzl` and forbids pushing elsewhere without permission; `MODIFICATION-20261011-gcfpe-mb008-to-promotion` §A.1 made the same deviation. A fresh session finds this record through its pull request, or on `main` once merged.
- **Baseline.**
  - Selected release `GCFPE-20261009.1` / `100926.1` / 55 (register; D29).
  - Repository `main` @ `44dba78`, which this branch equals.

### 2. Canon relied on

> When PF10 is silent, authority returns to the relevant permanent PF-Canon document. *(PF10-HDE-Build-Notes v13.8.9, front matter §8, Silence rule)*

> Once a newer base version exists, agents must not read, reuse, compare, reconcile, or carry forward content from an older base version. *(the same, §6, Current-version rule)*

**PF10 is silent on every topic below.** v13.8.9's index reads "No current addenda". No PF10 base version older than v13.8.9 was read, including through git history.

Where a backlog entry cites "addendum 2.x", this record cites the permanent home. It finds that home through the drainage ledger `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, which is routing and provenance only, and then reads the canon section itself on `main`.

| Source, on `main` `44dba78` | Sections read in full | Use |
|---|---|---|
| PF10-HDE-Build-Notes v13.8.9 | whole file, 189 lines | Silence (§8); current version (§6); continuous sequence (§4) for MB-009 |
| PF04-Canon-HDE-Governance v2.8.8 | §9.1.1; §9.1.3, including *GCFPE model and reasoning-level guidance*; §9.1.4; §9.1.5; §9.1.6; §9.7.7, all business-case bullets; §2.0.19 opening and the close-pack baseline bullet | PF04 §9.7.7: the business case per requirement and per work unit, its fields, no ceiling, and its gates (Specification approval, IA-30, PR-10, the Proceed; "A work unit whose business case is met stops").<br>PF04 §9.1.6: one coherent successor selection; admission needs the actual membership update; the provenance helper is deferred.<br>PF04 §9.1.3: the TypeSafe reading. |
| PF06-Canon-Change-Process-Guide v2.5.5 | §0.1, §0.1A; §0.4.1.3; §0.6.10; §1.0.6; §1.1.4, with *PR review finding disposition (every pull request; real inputs only)*; §3.5.1, with *Close-mutation-set stage*; §3.5.2 and §3.5.2.1 to §3.5.2.4 | Real input, below-P1, P1, the one P1 exception, and the repeated finding class (MB-013, MB-014, MB-023).<br>The close-mutation-set stage, its entries, exit and authority (MB-027, MB-030).<br>Addendum numbering at creation (MB-007, MB-009, MB-012). |
| PF19-Canon-Glow-QA-Guide v3.0.7 | §0.4.3; §3.1.2 and §3.1.3; §3.3; §3.4.3, with *Evidence persistence (normative)*; §3.4.14; §3.5.7; §3.6, planning bullets only; §4.4 to §4.4.2; §10.6; *Close-pack truthfulness and same-run execution* | §3.4.3: "QA evidence is persisted in the repository. It is never left only in temporary or scratch storage." (MB-022).<br>§3.1.3: the close mutation set precedes the closure decision (MB-027).<br>§3.6 and §10.6: Kronos updates an affected QA Plan through its review owner (MB-021).<br>§3.3 and §3.4.14: evidence binding (MB-026). |
| PF27-Canon-Plan-Templates v2.0.6 | *Canon precedence for template use*; *Source-bound review authority and exact-fix limits*; *Business Case (MUST)*, with the requirement and work-unit business case; *Evidence coverage and optional legacy-token binding*; *Live QA Plan approval materiality discipline*; §2A, CRD intake; §3, *Not a PR (normative)*; §3B, *Close Mutation Set Task Record (Template)* | Finding disposition on real inputs, P1 and the repeated class (MB-013, MB-023); business-case fields and no ceiling (MB-015 to MB-019); §3B names "CL-05 — Prepare and Publish the Close Mutation Set" (MB-030) |
| PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7 | §1.2, *Close-pack artifacts*; *Change-container compatibility*; *Generic close-pack writer*; §8.17, the close-run family for admitted CRDs only | No Epic close-run family is admitted (MB-027, MB-030) |
| PF14-Canon-HDE-Mechanics-Guide v3.5.9 | §0.2 | The provenance helper: "do not install, invoke, recreate or require it, or invent a replacement ledger" (MB-025) |
| PF30.1-Canon-HDE-CRD-Records v0.9.2 | §4.1; the HDE-CRD-0002 record's business-case, closure and material-change rows | CRD record contract; history only |
| PF03-Reference-Technical-Writing-Best-Practices v1.8.8 | §9, *Output* | Addendum numbering (MB-007, MB-009) |
| PF23-Canon-Reality-Audits v1.2.3 | rows RA-09 and FND-020, by search | Observation only (MB-024, MB-025) |

**In-flight and record sources:**
- the drainage ledger above, rows A01 to A35, *Precedence and closure controls* and *Held and deferred items*;
- the two Product Owner briefs `docs/ephemeral/GCFPE-alpha-feedback-qa-plan-approval-coherence-v1.0.md` (MB-026) and `docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md` (MB-027);
- the HDE-CRD-0002 Product Owner directions `HDE-CRD-0002-po-direction-qa110-f01-c1-route-v1.0.md` and `-v1.1.md` (MB-021), and `HDE-CRD-0002-po-direction-qa-evidence-persistence-v1.0.md` (MB-022);
- the HDE-CRD-0002 CL-05 result records v1.0 and v1.1, and its CL-C-10 closure decisions v1.0 to v1.2 (MB-030);
- `docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.0.0-20260923.md` (MB-004).

**Repository controls:**
- `AGENTS.md`;
- decision record D8, D12 to D14 and D20 to D29;
- the seven MGMT spine documents;
- `notion-write-boundary.md`, `prompt-corpus-policy.md`, `skill-identity-and-freeze.md`;
- `docs/prompt_ecosystem_management/gtwpe/` (MB-028).

**Where canon is silent.** Each of these is a decision in §A.7:
- the plan-side real-input and no-emulation rules (the ledger records parts of 2.11 as out of target);
- where a business-case measure is checked (PF04 §9.7.7 defines the measure and names no stage);
- the mechanism for changing an approved QA Plan (PF19 §3.6 names the actors only);
- allocation between concurrent addendum drafts;
- the Codex security review's deprecation (the ledger records 2.3 as "N for PF canon").

### 3. What moved since the entries were written

| Change | Effect on this Modification |
|---|---|
| **PF10 v13.8.8 drained.** Its 14 canon replacements moved into `docs/pfcanon/` (#762), and PF10 v13.8.9 (`44dba78`, 2026-10-27) carries no addenda | **The authority behind ten entries moved from a temporary addendum to permanent canon:**<br>• MB-013, MB-014, MB-023 → PF06 §1.1.4 and PF27;<br>• MB-015, MB-016, MB-017, MB-019 → PF04 §9.7.7 and PF27;<br>• MB-022 → PF19 §3.4.3;<br>• MB-027, MB-030 → PF06 §3.5.1, PF19 §3.1.3 and PF27 §3B.<br>Each now contradicts permanent canon.<br>**The cost ceiling is withdrawn everywhere** (PF04 §9.7.7, "No cost ceiling"). So are the ceiling parts of MB-013, MB-014, MB-016, MB-017, MB-018 and MB-019, as the entries' own 2026-10-25 notes anticipated, and MB-014's "growing number of review rounds" escalation, which PF04 §9.7.7 and PF06 §1.1.4 ("not a push count") now rule out |
| **Rules that reached no permanent home** | • 2.3, the Codex security review deprecated ("N for PF canon"): MB-024's authority.<br>• Parts of 2.11 as planning rules (each component's real-input set, the refusal outside it, no emulation): MB-016, MB-017, MB-018.<br>• 2.27 C-1 and 2.28's restatement, the approved-QA-Plan delta route ("No canon change"): MB-021.<br>• 2.31's interim routing rule: MB-030's interim reading.<br>• 2.34, documentation-only changes: the CL-40 boundary (§A.9, J-1). |
| **HDE-CRD-0002 closed** (CL-C-10 v1.2, `CLOSE`, 2026-10-26T16:40Z) | CL-05 102626.2 ran twice for it. The runs repaired close-tooling defects B-4 to B-6 and reported at least nine candidate-text defects, which are not revised on the page (MB-030). The HDE-CRD-0002 direction on MB-021's route bound one decision of a closed change. |
| **MB-009 happened in a real run** | 2026-10-21: three addenda resolved overlapping numbers before one paste, and were published as 2.20, 2.18 and 2.19 |
| **MB-028 holds in practice for TW** | GTWPE-MGMT-10 100726.1 creates a sibling only for a changed page; three TW releases kept unchanged members' pages |
| **MB-005 is bound for qualification** | DN-E E1 (2026-10-11) binds the installed 10-file tree `c518ccb0…` |
| **Installed skills and the graph** | Unchanged since D29: 8 of 9 measured digests equal their recorded values, typesafe-scoring `3 8e26b055…` has no repository record, and the graph proof token reproduces |

### 4. Items and parts: class, tier and targets

Per-prompt `closure.py` output, all 55 calls exiting 0, and the union radius per part are in [closure.md](evidence/20261027-gcfpe-backlog-open-items/closure.md); the union is in the frontmatter. For targets with no graph part (skills, PE, the Hub, the register, the procedure, the template, the CL-05 candidate) closure is undefined, not empty.

**How the parts are cut.** A part is one rule across its surfaces (D21-B), so every part below carries one rule. Parts that edit the same body share that body's one successor page (D23-G). Parts that change the same skill share one package, one review and one install (template rule 7).

| Part | Class, and why | Targets | Tier |
|---|---|---|---|
| PART-01 | B: applies PF06 §1.1.4 and PF27 | PR-35 (step 3, step 4, readiness gate); RS-40 (its PR-35 section, the same rule); PR-40 (the P1 check); PR-20 (its description of PR-35); glow-hde-pr-development (`SKILL.md` 90, 91, 96, 105; `behavior-cases.md` 7, 17, 41, 91); change-flow `SKILL.md:317`; registry guards | 1: changes what PR-35 produces; radius 32 |
| PART-02 | B: applies Nathan's direction of 2026-10-13 (CD-4); canon names no Codex security review | glow-hde-pr-development `SKILL.md:90` only (0 bodies name Codex); a forbidden guard on the prompt rows | 0 for routing: skill only |
| PART-03 | B: applies PF04 §9.7.7 and PF27 | CF-C-30, CF-E-30 (the Specification gate); IA-30 (the unit gate, in both its initial Plan review and its material Plan-delta review, since PF04 §9.7.7 names no mode); PR-10 (carries it); PR-20 (the Proceed package carries it); registry guards. The author prompts (CF-C-20, CF-E-20, CF-C-40, CF-E-40, IA-10, IA-20, IA-40) are read at PLAN's dry run and change only where a body lists required contents that omit the business case | 1: radius 33 |
| PART-04 | **A, ambiguous with B (DN-3).** No live canon states these as planning rules. PF06 §1.1.4's *Real input* bullet ("justifies no requirement, design element, test, fix or blocking finding; an input outside the real set receives one refusal or a stated limit, never a model of it") reaches them by its words, under a heading scoped to review findings | IA-30, PR-10, PR-20; registry guards | 1: radius 31 |
| PART-05 | A: canon defines the measure and names no stage (DN-4) | PR-40, or QA-120 and the closure decisions, or nothing | 1, or none under (d) |
| PART-06 | B: applies D23-F and C-REPLAN | PR-20, 1 line; a forbidden guard | 0: a description of a downstream stage; neither routing nor PR-20's output changes |
| PART-07 | B: applies D23-B and D27 *Continuity* | 23 bodies, 95 lines (§A.5); a forbidden guard | 1: radius 50 |
| PART-08 | B: applies D23-E's once-per-merge rule (CD-1) | DOC-20 body; `DOC-20.json` (remove the `landed_lineage_review` edge to PR-40); a guard | 1: routing moves; radius 25 |
| PART-09 | D: IA-40's return breaks its own handoff contract. That would be A if the intake were widened beyond IA-30, which the measurement does not support (CD-5) | IA-40, IA-30; `IA-40.json`, `IA-30.json` (an IA-40 → IA-30 edge for `REDLINE_INCOMPLETE`); a guard. R1 pins nothing here: its one `REDLINE_INCOMPLETE` is GCF-05, a Thoth row | 1: routing moves; radius 12 |
| PART-10 | A: a route choice canon leaves open (DN-5) | QA-70, QA-80; and the text that routes or refuses an approved-base change in QA-50, QA-60, QA-90, QA-110, ESC-40; `QA-70.json`, `QA-80.json`; a guard | 1: routing moves; radius 36 |
| PART-11 | B: applies PF19 §3.3, §3.4.14 and PF27 to Nathan's brief (requests 1, 2, 3, 5); request 4 per CD-6 | QA-70, QA-80, QA-50 | 1: radius 27 |
| PART-12 | B: applies PF19 §3.4.3; the mechanism is DN-6 | QA-100 (3 lines), QA-90 (1), QA-50 (1); glow-write-boundary only under DN-6 (b) | 1: radius 28 |
| PART-13 | **B, ambiguous with A (DN-2).** It applies PF06 §3.5.1, PF27 §3B and Nathan's direction of 2026-10-26 ("It needs to become PART of the change flow"). It also reverses the route pinned in R1 (GCF-24 → GCF-25), which by precedent changes only under his approval | CL-05 as the 56th member (page, `CL-05.json`, registry row, catalog row); QA-120 (`pass_crd`, `pass_epic` → CL-05); CL-C-10 and CL-E-10 (a new `DO_NOT_CLOSE` branch to CL-05, the close mutation set as input, and the PF19 §3.1.3 classification sentence in *Execute* steps 3 and 5 for MB-027); `global.json` `qa_closure_contract`; R1 successor rows; the candidate's first-run defects (CD-7); change-flow and flowmaster-validate pins | **2:** a new node and a shared-contract change |
| PART-14 | B: applies D29 and *Restating is allowed; asserting is not* | PE successor: 3 passages and 2 more repair-scoped passages | none: PE is not a graph node |
| PART-15 | B: applies PF06 §0.1A; the scope is DN-8 | PE, 2 sentences | none |
| PART-16 | A: a numbering rule canon is silent on (DN-7) | the six producers, PE, `global.json` addendum format, or nothing under DN-7 (a) | 1, or none |
| PART-17 | B: applies D29 and PF06 §0.1A; scope per DN-9 | Glow Operations Hub (4 sections, 1 paragraph, 3 lines, 2 workspace-wide texts); the register's copy of the PF10 reference-boundary paragraph | none: Notion controls |
| PART-18 | B under (a) removal; A under (c) installation (DN-10) | 54 bodies, or nothing | none, or 2 under (a) |
| PART-19 | C: a stale register-bound control (STALE-001) | a successor procedure `…-v5.1.0-…md` in `docs/ephemeral/`, and the register's binding moved to it (CD-9) | none |
| PART-20 | C: an identity record | a record of the installed `c518ccb0…` as 1.2.0 (CD-10) | none |
| PART-21 | C: applies `AGENTS.md`'s canon-first rule to a binding template | `reviewer-prompt-template.md`, both briefs (CD-11) | none |
| PART-22 | A if PE's general rules change (they also govern TW) | none under DN-8 (c); PE under (a) | none |
| PART-23 | A: a new capability; unmeasured | undefined until DN-11 | — |
| PART-24 | C: the release gate | the successor release's graph build, registry, both packages' contract and validation profile, validators over every member, injected regressions, the D24 review, an independent post-flight, the promotion packet | **2:** corpus-wide by definition |
| PART-25 | B: applies Nathan's promotion decision | register, catalog, Flow Index, lane hubs, archive moves, `docs/graph/parts/` and the registry replaced, the sweep by literal | **2** |

**The Modification's tier is 2.** The prompt parts together reach 50 of 55 members, and PART-13 changes the shared contract.

**Skill packages, each one package, one review and one install:**
- glow-hde-pr-development (PART-01, PART-02);
- change-flow (PART-01's line 317; the release contract and pins that any routing part, PART-08, PART-09, PART-10 or PART-13, regenerates);
- flowmaster-validate (the release contract and validation profile; the R1 successor for PART-13);
- glow-graph-contract (probable: its contract value tables pin `qa_closure_contract` and `reject_replan`; PLAN confirms or rules it out);
- glow-write-boundary, only under DN-6 (b).

### 5. Scope, and how it was measured

Every number is broad match minus named exceptions, read in context. Methods, patterns and per-page counts are in [scope-measurement.md](evidence/20261027-gcfpe-backlog-open-items/scope-measurement.md).

**The corpus sweep.** Three read-only sweep workers fetched all 55 members and PE once, live, on 2026-10-27, and applied nine fixed families line by line: 56 of 56 pages read, 0 failures, plus 202 escape-hatch lines. Six verifiers tested the entries as claims. Their briefs are in [worker-brief.md](evidence/20261027-gcfpe-backlog-open-items/worker-brief.md) and their condensed returns in [findings.md](evidence/20261027-gcfpe-backlog-open-items/findings.md).

| What | Measured | Entry said |
|---|---|---|
| MB-010 handoff-package sentences | **95 lines on 23 pages** (234 broad, minus 139 conformant or unrelated) | 9 lines on 5 pages |
| Drained rules in any body (F7: "business case", "real input", "constructed input", "P1", "emulat", "repeated class") | **0 of 56 pages** | — |
| Codex named in any body (F3) | 0 of 56 pages: the 8 F3 lines are generic "code/security review" | 1 skill line |
| Provenance clause (F2) | 168 lines on 55 pages: every runtime body and PE, not GCFPE-MGMT-10 | "every prompt" |
| Numbered PF10 addendum citations (F8) | 0 pages | — |
| MB-013 finding rule | PR-35, plus RS-40's PR-35 section, PR-20's description, change-flow `SKILL.md:317` | PR-35 |
| MB-022 commit default | 5 lines in QA-100, QA-90 and QA-50 | QA-100, QA-90 |
| MB-020 unapplicable-redline returns | 1 of 8 redline-applying prompts returns terminally (IA-40) | "only IA-40 was checked" |
| MB-021 approved-QA-Plan change | 0 authors; 7 bodies route or refuse one | QA-70, QA-80 |
| MB-030 close stage | 2 edges to retarget; ≥ 2 branches and 1 node to add; 1 shared-contract field; ≥ 9 candidate-text defects | install CL-05 |
| MB-029 relay scoring | **unmeasured**: "relay safety" is defined nowhere | — |

### 6. Findings, contradictions and risks

| ID | Finding | Defect class |
|---|---|---|
| **A-1** | **Landing needs a successor release, and GCFPE-MGMT-10 stops short of promotion.**<br>• D23-G gives a changed member a successor page, which the register records in a new release.<br>• PF04 §9.1.6 requires every member change to be reconciled "in one coherent successor selection"; "an edited subgroup is not ready while an affected counterpart remains incompatible"; and a new member needs "the actual membership update".<br>• GCFPE-MGMT-10 "does not execute ... release selection, promotion or archival". So the prompt parts land as candidate successor pages, and go live only at a promotion that is Nathan's (DN-1).<br>**The class reading this implies.** MGMT-10's PLAN rule says a selected member's edit "is Class A". Under D23-G the edit lands on a candidate successor, not on the selected page; Nathan's promotion is the act that touches the selected release. Each part is therefore classed by the rule it applies, as `ecosystem-change-management.md` §2 does. The review attacks this reading first (§A.11). | SCOPE-002 |
| **A-2** | **Canon moved under ten entries, and five rest on rules without a permanent home** (§A.3).<br>• The entries' closing text still cites "addendum 2.11's wording" with its misnumbered rules (MB-013), the withdrawn ceiling (MB-014, MB-016 to MB-019), and "PF10 2.3" (MB-024).<br>• This analysis converges on the permanent wording, PF06 §1.1.4 and PF27, instead. The dated entries stay as written (`AUTH-001`). | NAME-001 |
| **A-3** | **Scope beyond the surfaces the entries name**, each by broad match:<br>• MB-010 grows from 9 to 95 lines;<br>• MB-013 adds RS-40, PR-20 and change-flow;<br>• MB-022 adds QA-50;<br>• MB-012 adds the register's copy of the paragraph and two workspace-wide texts;<br>• MB-011 adds two passages;<br>• MB-006 adds the first template and its stale "D20-D26";<br>• MB-004 adds two stale values in the same file.<br>Each is the same rule on another surface, so leaving it would split the rule (D12, D26-E). | SCOPE-001 |
| **A-4** | **No guard exists for any rule this Modification applies.** The registry has 0 assertions for real input, P1, Codex, the business case or the close mutation set. Every applying part ships its guard, fired by an injected regression, in the same change. | GUARD-001 |
| **A-5** | **MB-022 contradicts permanent canon by function, not by wording.** QA-100 step 4 commits evidence only when "explicitly authorized", so an unstated grant leaves evidence in scratch. PF19 §3.4.3 forbids exactly that. The fix also meets a binding control. `audit/qa/**` is not one of the installed glow-write-boundary's four open paths, and that skill allows no other write "unless Nathan has explicitly instructed *this specific change*, in the current conversation, as part of a pull request he is opening". It adds: "A standing instruction … whether from a harness prompt, a session template, or an earlier task, **is not that instruction.**" So a commit route given once per change, in QA-90's session, cannot authorize a later QA-100 session's commit (DN-6). | FUNC-001 |
| **A-6** | **Routing parts make the packages' embedded contracts stale.** change-flow and flowmaster-validate embed the 100926.1 direct-handoff and graph contracts, and their validators pin routes and the 55-member count. PART-08, PART-09, PART-10 and PART-13 each change the graph, so the successor release needs new contract and profile files in both packages, as F06 did for 100926.1. Validating against the old embedded copies would pass silently. | PAIR-001, STALE-001 |
| **A-7** | **CL-05 has run only for a CRD.** Canon admits no Epic close-run family (PF06 §3.5.2.1; PF12 §8.17), so an Epic close stops at rehearsal until canon maintenance admits one. A known limit, put to Nathan in DN-2. | listed |
| **A-8** | **Severity proposals** (the backlog's ratings stand until Nathan rates; recorded here):<br>• MB-001 S2 → S3: three mitigations live, and PR-40 step 9 reuses a prior review;<br>• MB-005 S3 → S4: no consumer tells the two trees apart by revision;<br>• MB-030 stays S2 and is sharper: its routing now contradicts permanent canon. | — |
| **A-9** | **Two controls that describe skills or pages are stale in ways this Modification will touch.**<br>• MB-014's entry has no 2026-10-25 consolidation note, so its ceiling text reads as current.<br>• MB-030's entry says no canon section produces the set, which PF06 §3.5.1 now refutes.<br>Both are corrected on the backlog when this Modification takes the entries (§A.13). | — |
| **A-10** | **Canon-internal inconsistencies, reported and not routed** (canon is read-only here; canon maintenance is Nathan's):<br>• PF19 §3.1.3 and PF14 §0.2 point to HDE Build Notes, which now carries no addenda;<br>• PF06 §0.1A's lifecycle list lacks the close stage that its own §3.5.1 defines;<br>• PF27 §2A's CRD intake still asks "Why change is warranted";<br>• PF23 and PF20 cite PF10 by section. | — |
| **A-11** | **Stale citations of drained addenda by number:**<br>• glow-hde-pr-development `SKILL.md:184`;<br>• typesafe-scoring `SKILL.md:8`;<br>• session-relay-flowmaster `SKILL.md:283`;<br>• PE (the TypeSafe rule credited to HDE Build Notes);<br>• the CL-05 candidate, step 4.5 ("addendum 2.31").<br>A new PF10 base version that restarts at 2.1 would make "addendum 2.1" ambiguous. CL-05's citation is fixed by CD-7, and the first rides PART-01 if opted in (DN-12). | NAME-001 |

### 7. Decisions

#### The coordinator's (evidence-determined; `ecosystem-change-management.md` §6). Nathan may override any.

- **CD-1, MB-001.** DOC-20 → PR-40 is always a second entry: DOC-20's only inbound edge is PR-40's `ACCEPT` for the same merge. The edge is removed. A missing or unverifiable PR-40 acceptance takes DOC-20's existing `ORIGINAL_NATIVE_STAGE` recovery or a return to Nathan. This applies D23-E's "entered once per merge".
- **CD-2, MB-013.** The design question on a repeated finding class is asked in the PR-35 session, which continues on the answer. No new result state and no graph change.
- **CD-3, MB-023.** PR-40 gains one check: a real-input P1 declined, or left open, before merge is a substantiated defect. This applies PF06 §1.1.4 ("not merge-ready").
- **CD-4, MB-024.** The removal rests on Nathan's direction of 2026-10-13 and on canon naming no Codex security review. Applying his ruling needs no new D-number. PR-35's generic "security review" wording already meets the entry's ask and is unchanged.
- **CD-5, MB-020.** The intake is IA-30's only. The other seven redline-applying prompts were measured: none returns terminally, so CF-C-30 and CF-E-30's receiving-side gap is recorded separately (§A.9, J-6). PLAN chooses between an input in the existing modes and a fourth mode, keeping "These modes never collapse".
- **CD-6, MB-026.** Request 4, the reviewer stating the combined effect of all redlines before a `DENY`, is adopted as an extension of the one-pass apply simulation that PF27 and PF06 already require. It is not a new free-standing duty.
- **CD-7, MB-030.** The installed CL-05 text is the corrected text. It carries:
  - every defect its first run reported, among them CL-L7, the route for a close PR merged before its closeout run, intake 3 against entry (b), and allowed change 3;
  - its two passages that PF10's drain made stale ("work under every addendum"; "addendum 2.31").
  It is not installed as 102626.2 stands.
- **CD-8, MB-027.**
  - CL-C-10 and CL-E-10 *Execute* steps 3 and 5 gain the PF19 §3.1.3 classification: the close mutation set precedes the decision and is not post-closure administration.
  - The brief's "lands the QA evidence of record" clause moves to PART-12.
  - Request 4 needs no change, because PF06 §3.5.1 makes Nathan's invocation the Proceed.
- **CD-9, MB-004.** A successor procedure, v5.1.0, points to the registry rows. Its release field and graph token are made current, and the register's binding moves to it. v5.0.0 stays as written (`AUTH-001`).
- **CD-10, MB-005.** The repository records that the installed 10-file tree `c518ccb0…` is the 1.2.0 of record, and that any other content delivered again carries an unspent revision.
- **CD-11, MB-006.** Both briefs get:
  - `AGENTS.md` among their governing documents;
  - a Canon relied on line in their deliverable;
  - "D20-D26" made "D20-D29".
  §3 and §5, the fixed rubric and exit that D26-A protects, are untouched.
- **CD-12, MB-011.** The five repair-scoped passages ride one PE successor, bound at promotion.
- **CD-13, MB-010.** Applied on all 23 pages. One rule is never split across authorizations (D12).
- **CD-14, MB-015 to MB-017.** Applied at the five gates canon names. The author prompts are checked at PLAN's dry run (PART-03 targets). PF04 §9.7.7's stop rule ("A work unit whose business case is met stops") is placed by PLAN on the implementing phase that would otherwise continue.
- **CD-15, MB-014.** The skill change drops the entry's ceiling and round-count escalation, which canon now forbids.

#### Nathan's. Each is a round trip; one reply can answer all twelve.

**DN-1 — The promotion boundary (A-1).**
- **D2, recommended.** After qualification (PART-24), EXECUTE returns `PROMOTION_CHECKPOINT_REQUIRED` with the packet. Your exact promotion approval then authorizes this Modification to run the transaction (PART-25), including the install hand-off and the digest checks. This waives, for this run only, MGMT-10's line that it does not execute promotion, as DN-D did for `MODIFICATION-20261011-gcfpe-mb008-to-promotion`.
- **D1.** Stop at the checkpoint, and let a separate release-transaction run do the rest. That adds about four round trips, and the installs wait for it.

**DN-2 — CL-05's authority, and the R1 successor (PART-13).**
- **(b), recommended.** Class B, under PF06 §3.5.1, PF27 §3B and your direction of 2026-10-26. Your approval of this analysis also authorizes the R1 successor rows (GCF-24 → the close stage → GCF-25), which this record states here so that the approval names them.
- **(a).** A D-number first, adopting the stage and the R1 successor.
- **(c).** Defer the installation. CL-05 keeps running only at your direct invocation, which PF06 §3.5.1 *Authority and actor* supports.

In each option, the Epic limit (A-7) is a listed risk until canon admits an Epic close-run family.

**DN-3 — The plan-side real-input and no-emulation rules (PART-04).**
- **(a), recommended.** Read PF06 §1.1.4's *Real input* bullet by its words, which reach "requirement, design element, test" and say "never a model of it". PART-04 then applies it to IA-30, PR-10 and PR-20, as class B.
- **(b).** Record a D-number (class A).
- **(c).** Drop PART-04, keeping the rules on the review side only.

**DN-4 — Where the business-case measure is recorded (PART-05).**
- **(a), recommended.** PR-40 records the measure's status (met, not met, or not yet observable) as a fact. It has no effect on `ACCEPT`, `REJECT` or `PENDING`.
- **(b).** "Not met" becomes a `REJECT` or `PENDING` ground. That is a routing change.
- **(c).** Record it at QA-120 or at the closure decision instead.
- **(d).** WON'T DO.

**DN-5 — The approved-QA-Plan change route (PART-10).**
- **(a), recommended:** generalise your HDE-CRD-0002 direction (v1.1):
  - QA-70 reviews the approved Plan against the delivered change, using `INITIAL_QA_PLAN_REVIEW`'s decisions;
  - a `DENY` sends exact redlines to QA-80, which may then revise an approved base into a successor;
  - QA-70 approves the successor;
  - the route produces no PF10 addendum.
  It is your latest direction on this, and it reuses the existing loop.
- **(b).** A Kronos delta-authoring mode, in QA-80 or a new prompt, feeding QA-70's existing delta review, with an addendum on a material approval as QA-70's contract says.
- **(c).** Both, by trigger.

**DN-6 — Persisting QA evidence under the write boundary (PART-12, A-5).**
- **(a), recommended.** No skill change.
  - QA-90 names, in every task, the exact evidence paths and the pull request route by which they land, and states that the commit needs your instruction.
  - QA-100 asks you, in its own session and before execution, to instruct that specific commit, in the pull request it opens.
  - Without your instruction, QA-100 stops before executing, so no evidence exists only in scratch.
  - This meets PF19 §3.4.3 and the write boundary's "in the current conversation" condition, at one question per QA-100 session. It is how HDE-CRD-0002's QA-100 committed its evidence.
- **(b).** Amend glow-write-boundary so that the change's QA evidence root is open to QA-100 by default. That removes the question in each session. It is a storage-boundary change, and adds one package and one install.
- **(c).** Both: (b) as the default route, with QA-90 still naming the paths in each task.

**DN-7 — Concurrent addendum numbering (PART-16).**
- **(a), recommended.** WON'T DO: the published number governs and you renumber at paste. It is listed as an accepted risk, and passes D8's simplicity test.
- **(b).** Producers also read unpasted addendum records under `docs/ephemeral/`.
- **(c).** Number at paste, which contradicts PF06 §0.1A and needs a canon change.
- **(d).** A reservation record.

**DN-8 — PE's general rules, which also govern TW (PART-15, PART-22).** D23-G's successor of 2026-09-23 keeps those rules unchanged and TW out of scope.
- **(c), recommended.** No change. No producer outside GCFPE authors an addendum (GTWPE-D3), so MB-007's clause has no consumer (NORM-001). TW already keeps unchanged members' pages (MB-028). Both close as `NOT_APPLICABLE`, with that evidence.
- **(a).** One PE successor applies PF06 §0.1A to every agent-authored addendum, and states D23-G's register-membership rule for every ecosystem PE governs.
- **(b).** Route both to GTWPE-MGMT-10.

**DN-9 — How far PART-17 may edit (MB-012).** In every option, the four 091426.1 sections are marked historical with pointers to the 100926.1 prompts and the register, and the PF10 reference-boundary paragraph on the Hub and the register is restated to PF06 §0.1A.
- **Recommended.** Also replace the workspace-wide *PF10 build-notes addendum format — canonical* section's numbering and confirmation text with a pointer to PF06 §0.1A and PF27. It restates canon, and it keeps D8's struck confirmation step (DERIV-001).
- **Alternative.** Restate only its GCFPE application, and label the rest by scope (SCOPE-002).
- **Alternative.** Leave the workspace-wide texts to whoever owns them.

**DN-10 — The provenance clause (PART-18).**
- **(b), recommended.** Keep it as written, and accept the repeated PENDING row as a listed risk. Canon (PF04 §9.1.6, PF14 §0.2, PF19 §0.4.3) keeps the helper deferred, and the clause agrees with it. Removing the clause is 54 successor pages for an S4 line.
- **(a).** Remove it from 54 bodies and CL-05, with a guard.
- **(c).** Install the procedure. That needs your canon change first.

**DN-11 — Relay-safety scoring (PART-23).** It cannot be scoped until "relay safety" is defined. Within GCFPE, PF04 §9.1.3 forbids any model or effort recommendation beside the TypeSafe reading.
- **Recommended.** WON'T DO, or a separate run once you define what it measures (a non-model relay-integrity check, for example).

**DN-12 — Opt-ins.**
1. **Record J-1 to J-14 (§A.9) on the backlog now.** Recommended: yes.
2. **Let three zero-cost riders join files this Modification already changes.** Recommended: yes. Each is a different defect from its host part, so each needs your yes:
   - the stale addendum citation at glow-hde-pr-development `SKILL.md:184` (PART-01's package);
   - PE's "the GCFPE-20261009.1 candidate" label (PART-14's successor);
   - the pre-D29 proof token in `ecosystem-change-management.md` §3 (PART-21's pull request).

### 8. Readiness and interaction cost

**Readiness: `SPLIT_RECOMMENDED`, for PART-23 alone. It is advisory.**
- **Unmeasured scope holds for MB-029.** "Relay safety" is defined in no record, so its surfaces cannot be bounded.
- **No sequential discovery.** Every other item is measured now. PART-11's wording follows PART-10's ruling, which is an execution order, not discovery.
- **`NEEDS_RULING` also holds**, for the twelve decisions in §A.7.

```
interaction_cost = open rulings 12 + 2 + ANALYZE and PLAN review rounds 2 + skill review cycles 1
                   + installs 4 + merges 2 = 23
```

- **Installs:** glow-hde-pr-development, change-flow, flowmaster-validate and, probably, glow-graph-contract. glow-write-boundary is a fifth only under DN-6 (b).
- **Merges:** this record's pull request, and the promotion pull request that replaces `docs/graph/parts/` and the registry.
- **Outside the formula:** your promotion approval.
- **Range: 21 to 28.**
  - Lower: DN-12 folds into another reply, and glow-graph-contract proves unaffected.
  - Higher: a second FULL review in each mode, a repeated skill cycle, and the fifth install.
  - Answering the twelve in one message makes the actual lower.

**What a split would save:**

| Split | Net effect | Note |
|---|---|---|
| PART-23 to its own run | about −1 now; +2 later only if you want it | Recommended: it is the one unmeasured item |
| PART-13 (CL-05) to its own run | about +9 | It shares the change-flow and flowmaster-validate packages, and would need its own release, qualification, skill cycle and promotion |
| The controls-only parts (PART-17, PART-19, PART-20, PART-21) to a run of their own | +2 approvals and +1 merge; saves nothing | They need no install and no release |
| A second successor release | about +9 | — |

No other open Modification changes these skills.

**Estimate** (frontmatter `estimate`; twice it triggers a re-price, D26-D):
- PLAN: 10–16 h and 6–10M aggregate tokens.
- EXECUTE: 24–40 h and 12–20M, excluding waiting.
- For calibration, this ANALYZE used about 2.5 h, of which the nine-worker pass took 1 h 54 min and about 4.2M worker tokens. It ran two agents at a time on this 4-CPU container.

### 9. Adjacent work, recorded for a separate Modification

These were found while measuring, are outside every entry's rule, and are not taken. DN-12 asks whether to put them on the backlog now. Severity is the finder's proposal.

| ID | Finding | Severity |
|---|---|---|
| J-1 | CL-40's addendum boundary: CL-40 never prepares a PF10 addendum, and does not name the documentation-only route of 2.34. That route is "N for PF canon", so its authority must be re-established first (CL-40 cycle gap scan v1.1, line 236) | S4 |
| J-2 | Lessons CL-L8 (close tooling's first real run inside the work unit that builds it: the PR and IA prompts) and CL-L2 (schedule the Plan's Close Gate before the closure decision: QA-120 and CL-C-10), routed to GCFPE-MGMT-10 by CL-C-10 v1.2 | S3 |
| J-3 | `PR-40.json` routes `REJECT` to PR-10 (`reject_instruction_owner`), which the 100926.1 PR-40 body does not describe | S3 |
| J-4 | PR-40's *Accepted-final lineage protection* sends a merged-but-not-accepted finding to RS-10 without separating out a precise in-scope defect, which D23-F re-plans | S3 |
| J-5 | ESC-40 forbids a replacement Implementation Plan in remediation, while PF19 §10.6 has the IA prepare one complete successor Plan (plausible; needs its own read) | S2 |
| J-6 | CF-C-30 and CF-E-30 have no mode that receives a redline CF-C-40 or CF-E-40 returns as missing or contradictory (the return goes to `ORIGINAL_NATIVE_STAGE`) | S3 |
| J-7 | CL-E-20, on a corrective invocation, has no outcome for an ambiguous review item | S3 |
| J-8 | The OPS lane's evidence commit-scope default (OPS-10, OPS-20, OPS-30: "Task authors specify exact permitted evidence paths and commit scope"), the Ops counterpart of MB-022 | S3 |
| J-9 | Stale drained-addendum citations in typesafe-scoring `SKILL.md:8`, session-relay-flowmaster `SKILL.md:283` and PE's TypeSafe attribution (A-11) | S4 |
| J-10 | Graph `source_evidence` pointers name `candidate/prompts/c/…` and sections the 100926.1 bodies lack (DOC-20, PR-20, PR-40 parts) | S4 |
| J-11 | `docs/prompt_ecosystem_management/README.md` still says the closeout workflow is dispatch-only, which #752 changed | S3 |
| J-12 | `ecosystem-change-management.md` §3 still shows the pre-D29 proof token `ae2bd159…` (a DN-12 rider) | S4 |
| J-13 | The registry's QA-120 consumers omit QA-90, although `QA-120.json` routes `INTERIM` to QA-90 (plausible) | S4 |
| J-14 | The installed typesafe-scoring tree, `3 8e26b055…`, has no repository record | S4 |

### 10. Checks, limits and transient reads

**Checks run:**
- 55 `closure.py` calls; the graph build against D29's token; 9 installed skill digests against their records;
- the validator on all 16 existing records and on this one;
- 240 repository and canon quotes, checked programmatically;
- 166 Notion quotes, cross-checked against an independent sweep;
- the decisive sentences re-read on fresh fetches, and the routing claims read from the graph parts;
- the TypeSafe script, run once.

**Not run:**
- no body was edited, no package built, and no registry assertion, validator over bodies or governance audit run;
- the flowmaster-validate and change-flow suites, because nothing has changed for them to check yet.

**Limits:**
- **L-1.** 114 of the 166 Notion quotes rest on the verifier's verbatim capture alone (`scope-measurement.md` §4). Every decisive one was re-checked.
- **L-2.** MB-010's 95 lines come from a stated test plus a read of the residue. PLAN re-reads every anchor.
- **L-3.** PART-03's seven author prompts were not read for content lists; PLAN's dry run reads them.
- **L-4.** The GTWPE catalog page was not re-fetched (MB-028).
- **L-5.** The 11-file attribution-lock archive is not in this environment (MB-005).
- **L-6.** Rule numbers inside drained addenda are mapped only through the ledger, because PF10 §6 forbids reading the older base.

**Transient reads (D22, condition 5).**
- **Workers.** Prompt bodies were read through Notion fetches; the harness saved the larger results in its session store. Each worker's grep extracts (`tmp-LA`, `tmp-LB`, `tmp-LC`, `tV2`, and two decoded control pages) were deleted at lane end, and their absence was confirmed.
- **The coordinator.** I read PR-20 and the Hub from harness saves, in memory, and QA-70, QA-80 and CL-05 inline.
- **What is left.** The harness's own saves are left to its teardown and never read again. The workers' returns, which hold matched lines, stay in the scratchpad for this task only and are deleted when it ends. No body text is committed beyond the short quotes in `findings.md`.
- **Working tree.** One worker's stray `__pycache__` file in the working tree was found absent, and the tree is clean.

### 11. Review (D26-A)

- **Dry run, 2026-10-27:** passed. It is the first ledger entry: no defect in the analysis was open after it.
- **FULL review 1, 2026-10-27,** at `4780f64a`. Two fresh reviewers ran under the committed briefs `BRIEF-ANALYZE-1-A.md` and `-1-B.md` (`8134979c`). Their own records, unedited, are [REVIEW-ANALYZE-1-A.md](evidence/20261027-gcfpe-backlog-open-items/REVIEW-ANALYZE-1-A.md) and [REVIEW-ANALYZE-1-B.md](evidence/20261027-gcfpe-backlog-open-items/REVIEW-ANALYZE-1-B.md).
  - **Confirmed by both:** A-1's class reading (the first attack); CD-1; CD-4; MB-010's test on the bodies they fetched; the derived ITEM-31 and ITEM-32; tier 2; the cost of 23.
  - **Required, 2, both from reviewer A, both repaired.**
    - R-A1 (R1): the IA-30 business-case gate was confined to the initial review. ITEM-14, ITEM-15 and PART-03's targets now name both IA-30 reviews, because PF04 §9.7.7 names no mode.
    - R-A2 (R3): DN-6 (a) relied on an instruction from an earlier task, which glow-write-boundary says "is not that instruction". A-5 now quotes both of its conditions, and DN-6 (a) has QA-100 ask in its own session.
  - **Listed: 24 from A and 19 from B, which overlap to 31 distinct.** They are not repaired (D26-A rule 4) and are listed in §A.13 for approval as accepted risks, unless you opt in.
- **DIFF_CHECK, 2026-10-27,** by reviewer C, who was neither A nor B, on `02ba1797..46160491` under [BRIEF-ANALYZE-DIFF.md](evidence/20261027-gcfpe-backlog-open-items/BRIEF-ANALYZE-DIFF.md). The record is [REVIEW-ANALYZE-DIFF.md](evidence/20261027-gcfpe-backlog-open-items/REVIEW-ANALYZE-DIFF.md), committed unedited.
  - R-A1 and R-A2 are fixed, and the repair adds no required defect.
  - It lists 5 findings (L-C1 to L-C5).
  - **Trend: 2 required, then 0.** This was the last ANALYZE review D26-A allows. Every open finding is listed in §A.13.

### 12. TypeSafe reading for the PLAN session, and surface advice

The reading below came from running the installed TypeSafe scoring skill's script once (request v8.2), on 2026-10-27, on the action text in [evidence](evidence/20261027-gcfpe-backlog-open-items/typesafe-plan.md). It is recorded as the skill printed it. No Notion row was written (GCFPE-MGMT-10). No agent gives its own model, reasoning-level or effort assessment (PF04 §9.1.3).

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.25 (confidence 0.76); rung probabilities low 0.01, medium 0.04, high 0.72, extra high 0.19, max 0.01, ultracode 0.03. Model probabilities Fable 5.1 0.01, Opus 5.5 0.95, Sonnet 5.5 0.03, Haiku 5.5 0.01 (confidence 0.93). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.007, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.009, Opus 5.5 at medium 0.038, Opus 5.5 at high 0.684, Opus 5.5 at extra high 0.180, Opus 5.5 at max 0.009, Opus 5.5 at ultracode 0.028, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.022, Sonnet 5.5 at extra high 0.006, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.001, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.007, Haiku 5.5 at extra high 0.002, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-27T03:12:50Z. Nathan picks the cell.
- **Flags:** none printed.

**Execution surface for PLAN** (task-specific; no model or effort content):
- **What it needs.** A Claude Code session on `amthorn78/glow-hdengine-v2` with:
  - the Notion connector, for fresh reads of about 56 pages in the dry run;
  - the installed glow-graph-contract (`graph_parts.py`), change-flow and flowmaster-validate, for the contract and profile work;
  - the TypeSafe credential, for the EXECUTE reading;
  - repository push, for the record's branch.
- **Where it can resume.** It can be this session, continuing at the mode boundary once the approval is recorded (D21-D, D26-C), or a fresh one invoked with `MODE = PLAN` and this Modification's ID.
- **Parallel workers.** On this 4-CPU cloud container a workflow runs two agents at a time, so a parallel dry run of 56 pages takes roughly as long as this analysis's pass did.

### 13. Return to Nathan — 2026-10-27

**`PRODUCT_OWNER_ACTION_PENDING`: approve §A to enter PLAN, with your answers to DN-1 to DN-12.**

- **The analysis is reviewed.** A dry run, one FULL round by two fresh reviewers and one check of the repair's diff. Required defects went from 2 to 0.
- **36 distinct findings stay listed**, below. Approving the analysis accepts them as risks (`DISP-001`, D26-A rule 4), except those you opt in to repairing.
- **Who set this stop.** D26-A: two full reviews at most, then one diff check. This mode has used one full review and the diff check.

**Five listed findings change what you are asked.** Read them with the decisions they touch:

| Finding | Decision it touches | What it changes |
|---|---|---|
| L-A02 / L-B7 | DN-3 | Option (a) carries ITEM-18, the plan-side real-input rules: the PF06 drain put 2.11 rules 4 and 5 into the *Real input* bullet. It does not carry ITEM-15 or ITEM-17, the no-emulation and pin rules, which the drain recorded as out of target. To keep those two items, they need (b), a D-number, or (c), dropping them. So read DN-3 as (a) for ITEM-18 and (b) or (c) for ITEM-15 and ITEM-17 |
| L-B12 | CD-9 | Moving the register's operating-procedure binding touches the selected release's *Current selection*, which `ecosystem-change-management.md` §6 makes yours. Approving §A approves it; say if you would rather it wait for the promotion |
| L-A22 | CD-6 | Request 4 is new QA-70 reviewer behaviour, not an extension of the mechanical one-pass apply simulation. Approving §A adopts it; say if you want it left out |
| L-A23 | DN-12.1 | Recording J-1 to J-14 on the backlog is template rule 3's job once scope freezes, and the backlog's destination rule authorizes it. It needs no ruling: answer only if you object |
| L-B13 | CD-11 | CD-11 edits the *fixed* §6 deliverable text of the ANALYZE and PLAN brief, and the first brief's §10, by adding a Canon relied on line. It does not touch the rubric, cap or exit that D26-A protects |

**The approval, in one line if you agree with every recommendation:** "approve §A of MODIFICATION-20261027-gcfpe-backlog-open-items with the recommended options for DN-1 to DN-12". Name any decision where you choose differently, and any listed finding below you want repaired.

**Open findings, accepted as risks on approval** (path; likelihood; consequence). Each is listed rather than repaired because none meets R1 to R4 (D26-A rule 3). The full text is in the three review records.

| ID | Finding | Path | Likelihood | Consequence |
|---|---|---|---|---|
| L-A01 | MGMT-10's PLAN line "authored in Notion in place" is the only text that reads like in-place editing. A-1 cites neither D20-B nor mb008's precedent of B and C classes for candidate siblings | normal | certain | low: wording; the register's *Release rule* governs |
| L-A02 / L-B7 | DN-3 (a) cannot carry ITEM-15 or ITEM-17 (above) | normal, if (a) | likely | a rule installed as B on a contested citation |
| L-A03 | ITEM-18's "one refusal outside it" is narrower than PF06's "one refusal or a stated limit" | normal | possible | plans demand refusals where a stated limit suffices; PLAN converges on canon's wording |
| L-A04 / L-B8 | PF04 §9.7.7's stop rule ("a work unit whose business case is met stops") has no item; PLAN places it | normal | plausible | a canon-silent placement, or a P1 conflict and a return to you |
| L-A05 / L-B17 | PART-03's seven author prompts are unread, so their scope is unmeasured | normal | certain | PART-03 may grow by up to seven bodies at PLAN; readiness and estimate understated |
| L-A06 | ITEM-11 omits PF06's "declining a security finding goes to the Product Owner first" and "unchanged duty" | normal | unlikely | PLAN carries canon's full wording |
| L-A07 / L-B6 | CD-1's `ORIGINAL_NATIVE_STAGE` recovery applies to remediation only; ordinary documentation uses the terminal return | failure | low | a loud terminal return |
| L-A08 / L-B14 | CD-4's direction (2026-10-13) is findable only through a closed change's addendum record | normal | low | record its GCFPE consequence in the decision record when PART-02 lands |
| L-A09 | "168 lines on 55 pages" for the provenance clause has nothing subtracted (IA-30's and MGR-10's hits are other sentences) | normal | certain | DN-10's "54 pages" is overstated; under (a), PLAN re-measures by the clause's text |
| L-A10 / L-B16 | "50 of 55 members" should read 53 of 55 (all but GCFPE-MGMT-10 and PR-50) | normal | certain | none; tier 2 stands |
| L-A11 | PART-13 does not narrow CL-C-10's and CL-E-10's `do_not_close_new_remedy` → ESC-30 branch for close-tooling defects | normal | possible | two `DO_NOT_CLOSE` branches fit one result; PLAN applies CL-05's installation note ("not as ESC-30 work") |
| L-A12 / L-B1 | `global.json` `member_count`, `member_rule`, `proofs`, `protected_identities`, `stage_categories`, and both packages' `EXPECTED_POLICY`, are not named in PART-13 | normal | likely | stale contract facts unless PART-24's profile catches them; flowmaster-validate's 55-node pin fails loudly |
| L-A13 / L-B2 | PF04 §9.1.6's Living Prompt Flow Map and the Flow Index are named only at promotion, not at candidate publication | normal or failure | likely | a stale map, or a loud stop of the E-2 kind |
| L-A14 / L-B4 | DN-2 (b) leaves the R1 successor rows recorded only in this Modification | normal | certain, if (b) | add a decision-record successor entry, as D23 Amendment 1 did, and name the exact rows at PLAN approval |
| L-A15 | PART-09's "R1 pins nothing" should cite GCF-12's `STOP_REDLINE_APPLICATION_AMBIGUITY`; the conclusion holds | normal | certain | none |
| L-A16 | Under DN-1 D1, the skill halves of PART-01 and PART-02 wait for the separate run | option D1 | certain | PLAN disposes of them; `COMPLETE` is not reachable inside this run |
| L-A17 / L-B15 | The cost range's upper bound is 27, not 28, and the controls-only split row omits its own two review rounds | normal | certain | off by one; no conclusion changes |
| L-A18 / L-B10 | J-2's CL-L2 half is already covered by PART-13 and CD-8; only CL-L8 is adjacent | normal | certain | a duplicate backlog row if recorded as written |
| L-A19 / L-B9 | J-4 concerns D23-F, PART-06's rule, although PR-40's RS-10 package already routes correctly | normal | low | it could ride PR-40's successor page |
| L-A20 | PART-06's corrected PR-20 sentence still omits `reject_instruction_owner` → PR-10 (J-3) | normal | certain | PR-20's description stays partial until J-3 is decided |
| L-A21 | J-9's three stale TypeSafe citations are the same defect as DN-12's `SKILL.md:184` rider | normal | certain | offer all four together, or one defect is fixed on one of four surfaces |
| L-A22 | CD-6 overstates its basis (above) | normal | certain | a new QA-70 duty on an overstated basis |
| L-A23 | DN-12.1 is template rule 3's job, not a ruling (above) | normal | certain | one wasted round trip |
| L-A24 | A fresh session cannot find this record until its pull request merges, or unless it is told this branch | failure | loud | a blocked resume; the pull request names the branch |
| L-B3 | CL-05's "Removing stopgaps" note has no recorded disposition (F9: 0 hits in IA-10, IA-30, PR-10) | normal | low | PLAN records "no change" |
| L-B5 | MB-010's 13 lines read in context are not named in a committed file, so the 95 cannot be reproduced exactly (CL-20 gives 3 or 4) | normal | certain | PLAN re-measures with the stated test, and may differ by a few lines |
| L-B11 | Two verifier findings have no disposition: CL-05's PRs and PF06 §1.1.4 (covered in substance through glow-hde-pr-development), and MB-022's PF19 §3.5.7 scope | normal | certain | no prompt is affected |
| L-B12 | CD-9 touches the selected release (above) | normal | certain | authorized by your approval of §A |
| L-B13 | CD-11 edits fixed §6 text (above) | normal | certain | the rubric, cap and exit are unchanged |
| L-B18 | DN-8 (c)'s premise, that no producer outside GCFPE authors an addendum, rests on GTWPE-D3, which is about drain targets, not authorship | normal | low | MB-007 could close while a TW producer still leaves the number to you |
| L-B19 | Parts sharing a successor page: a D26-B restore of that page also reverts the other parts' edits | failure | low | PLAN orders the parts on each shared page |
| L-C1 | ITEM-14 and ITEM-15 cut the delta check by work unit; a delta can change a criterion or the outcome without editing a unit | normal | low | one criterion or case escapes the delta review |
| L-C2 | DN-6 (a) wording: "it opens" against the skill's "he is opening", and "its own session" against D27's venue latitude | normal | low | wording; PLAN converges on the skill's text |
| L-C3 | DN-6 (c) also changes glow-write-boundary, but §A.4 and §A.8 say "only under DN-6 (b)" | option (c) | low | one package short in the count under (c); loud at PLAN |
| L-C4 | §A.11 pointed here before this section was written | normal | certain | none now |
| L-C5 | No item lands the QA evidence of record on `main` before closure; under DN-6 (a), it rests on your merge of the evidence pull request | normal | plausible | closure can proceed with QA evidence unmerged, which is the HDE-EPIC040 brief's case; PF19 §3.4.3 is met by a branch |

**Then:**
- **In this session.** On your approval, I record it in the frontmatter with your words quoted here, mark the taken backlog entries with this Modification's ID, record J-1 to J-14 on the backlog under template rule 3, and go on to PLAN (D21-D).
- **In a fresh session.** Invoke GCFPE-MGMT-10 with `MODE = PLAN` and `MODIFICATION-20261027-gcfpe-backlog-open-items`, naming branch `claude/cool-bardeen-zwduzl` until the pull request merges (L-A24).
- **The PLAN session's reading** is in §A.12: **TypeSafe v8.2: Opus 5.5 at high**, no flags. You pick the cell.

### 14. Approval to enter PLAN — 2026-10-27

Nathan, approving, in the PLAN invocation of 2026-10-27:

> "approve §A of MODIFICATION-20261027-gcfpe-backlog-open-items with the recommended options for DN-1, DN-2, DN-4, DN-5, DN-6, DN-7, DN-8, DN-9, DN-10 and DN-12, and with these choices and conditions:
> - DN-3: option (a) for ITEM-18; option (b) for ITEM-15 and ITEM-17, recorded as a decision-record ruling before execution.
> - DN-11: close MB-029 as delivered. Its quantified relay reading is the typesafe-scoring skill, which every GCFPE handoff runs (PF04 §9.1.3); its qualitative Claude recommendation is withdrawn by my direction of 2026-10-11 that no AI model recommendation is given.
> - CD-9: move the register's procedure binding in the promotion transaction (PART-25), not before.
> - CD-6: adopt request 4 as a new QA-70 reviewer duty, stated as new.
> - DN-12: also carry PE's stale addendum citation for the TypeSafe rule into PART-14's PE successor.
> - PLAN covers L-A12 / L-B1 and L-A13 / L-B2 within PART-13 and PART-24, and records PART-13's R1 successor rows in the decision record (L-A14).
> All other listed findings are accepted as risks."

**What this approves.**

| Decision | Answer | Effect on PLAN |
|---|---|---|
| DN-1 | D2 | After PART-24, EXECUTE returns `PROMOTION_CHECKPOINT_REQUIRED`; Nathan's exact promotion approval authorizes PART-25 for this run only |
| DN-2 | (b) | PART-13 is class B. The R1 successor rows (GCF-24 → the close stage → GCF-25) are authorized; PLAN records them in the decision record (L-A14). The Epic limit (A-7) stays a listed risk |
| DN-3 | (a) for ITEM-18; (b) for ITEM-15 and ITEM-17 | ITEM-18 applies PF06 §1.1.4's *Real input* bullet (class B). ITEM-15 and ITEM-17 rest on a new decision-record ruling, recorded before execution (class A). PART-04 stays class A |
| DN-4 | (a) | PR-40 records the business-case measure's status as a fact, with no effect on its verdict |
| DN-5 | (a) | The HDE-CRD-0002 v1.1 route, generalised: QA-70 reviews, a `DENY` sends redlines to QA-80, QA-70 approves the successor, no PF10 addendum |
| DN-6 | (a) | No skill change: QA-90 names paths and route; QA-100 asks for Nathan's instruction in its own session and stops without it |
| DN-7 | (a) | WON'T DO. PART-16 makes no edit; MB-009's risk is accepted |
| DN-8 | (c) | No change. PART-15 and PART-22 close `NOT_APPLICABLE` with their evidence |
| DN-9 | recommended | The Hub's workspace-wide *PF10 build-notes addendum format — canonical* numbering and confirmation text is replaced by a pointer to PF06 §0.1A and PF27 |
| DN-10 | (b) | The provenance clause is kept; PART-18 makes no edit; the PENDING row is an accepted risk |
| DN-11 | close as delivered | PART-23 makes no edit. MB-029 closes as delivered by typesafe-scoring under PF04 §9.1.3, with the qualitative recommendation withdrawn by Nathan's direction of 2026-10-11 |
| DN-12 | yes to both, plus one | J-1 to J-14 go on the backlog now. The three riders and PE's stale TypeSafe-rule citation become ITEM-33 to ITEM-36 (PART-26 to PART-28) |
| CD-6 | condition | Request 4 is adopted as a new QA-70 reviewer duty and stated as new, not as an extension of the apply simulation (L-A22) |
| CD-9 | condition | The register's procedure binding moves inside the promotion transaction, not before (L-B12). PART-19's successor file is written earlier; its binding step runs in PART-25's window |
| L-A12 / L-B1, L-A13 / L-B2 | opted in | PLAN plans `global.json`'s member facts, both packages' `EXPECTED_POLICY`, the Living Prompt Flow Map and the Flow Index inside PART-13 and PART-24 |
| L-A14 | opted in | PLAN writes PART-13's R1 successor rows into the decision record |

**Scope at approval: 36 items.** The four approved riders were added as ITEM-33 to ITEM-36 when this approval was recorded, before `item_count_at_approval` was set, so they are inside the frozen scope (template rule 3). They sit in their own parts because each is a different defect from the part whose file it rides (§A.7, DN-12). The analysis above (§A.1 to §A.13) is otherwise unchanged and now frozen. Every other listed finding in §A.13 is accepted as a risk (`DISP-001`). `plan_approved_by` stays empty until Nathan approves the plan.

**The PLAN session's model and setting.** The invocation repeats §A.12's reading and ends "Nathan picks the cell"; it states no pick, so none is recorded.

## §P — Plan

**PLAN is complete, and its normal path passes a full dry run.** The detail is in [PLAN-20261027.md](evidence/20261027-gcfpe-backlog-open-items/PLAN-20261027.md). Its tools, operations, guards, registry inputs, activation operations and dry-run receipts are under [plan/](evidence/20261027-gcfpe-backlog-open-items/plan/). EXECUTE lands the 36 items as one successor release, `GCFPE-20261027.1 / 102726.1 / 56`:
- 54 runtime successors, PE and the new member CL-05 (C-1); GCFPE-MGMT-10 is kept;
- four skill packages;
- `PROMOTION_CHECKPOINT_REQUIRED` with the packet, then, after Nathan's exact promotion approval, the register-last transaction (DN-1 D2).

The first dry run failed five gates. One bounded repair (C-15 to C-22, D26-F trigger 2) fixed them. The second, at `acc39b04` on reads after 2026-10-27T09:38:45Z, passes all eleven gates, N0 to N10. The PLAN review's first FULL round found four required defects; they are repaired (C-23 to C-26), and one diff check follows (D26-A).

Canon relied on:
- PF10-HDE-Build-Notes v13.9: its one addendum, 2.1 (S19), is silent here, and its numbering restart makes drained "2.x" citations ambiguous.
- PF04-Canon-HDE-Governance v2.8.8 §9.1.1 to §9.1.6 and §9.7.7.
- PF06-Canon-Change-Process-Guide v2.5.5 §0.1A, §1.0.6, §1.1.4, §3.5.1 and §3.5.2.
- PF19-Canon-Glow-QA-Guide v3.0.7 §0.4.3, §3.1.2, §3.1.3, §3.3, §3.4.3, §3.4.14, §3.5.7, §3.6 and §10.6.
- PF27-Canon-Plan-Templates v2.0.6: the sections in PLAN §1, with §3B.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7 §1.2 and §8.17.
- PF30.1-Canon-HDE-CRD-Records v0.9.2 §4.1.
- Decisions D8, D12 to D14, D17 and D20 to D30.

### Steps

Every step's verification can fail; a forbidden guard searches every page for surviving old text (template rule 4, D26-E). A failure takes D26-B's path: a failure record that reaches `main` in a record pull request, a read-only sweep, the freeze kept, and a return to Nathan. Resumption is only at D26-C's checkpoints: X0, X18's check on `main`, and X27. Not safe to send twice: X2, X5, X6, X8, X9, X20, X21 and X28 (PLAN §5).

| # | part | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|---|
| X0 | all | skills, graph, PF10, register, 57 pages, 11 control pages | none: preflight; dry run rerun | D26-C | 9 digests; D29 token; PF10 v13.9 with only 2.1; selection 100926.1 / 55; every pin; D30 once on the branch | stop |
| X1 | 02, 19, 20, 21, 28 | v5.1.0 file; `skill-identity-and-freeze.md`; `reviewer-prompt-template.md`; `ecosystem-change-management.md` §3; PART-02 note after D30 | `plan/repo_edits_102726.py check --state before`, `apply` and `check --state after`, `--set X1`; controls pull request, its number recorded once in `execute/controls-pr-102726.1.json`; Nathan merges it before the packet | CD-9, CD-10, CD-11, C-11, C-12, C-23, C-26 | each `old` string at its count, each `new` once; the 7 repository guards through `body_check.py`'s guard functions; the note once, after `## D30`; v5.0.0 unchanged; validator | revert before merge |
| X2 | 24 | 56 source pages | duplicate; move where needed; title | C-1; D23-G | parent, title, head, no child, source revision unchanged | move to archive |
| X3 | 24 | `execute/successor-pages-102726.1.json` | write the map once | W7-D8; D26-C | map checks: 56 members, 54 SUCCESSOR, 1 KEPT, 1 ADDED, PE | stop |
| X4 | body parts | 56 successors and GCFPE-MGMT-10 | none: fresh reads; `body_check.py plan` | D22 | `ok`; revisions at the map's pins | stop the page |
| X5 | 24 | PR-50 102726.1 | head and binding operations, one call | C-22 | every operation LANDED; head read back as planned | page history |
| X6 | 01, 03–14, 24, 26, 27 | the other 55 successors | one update_content each | §A.14 decisions; C-1 to C-22 | each call succeeds | page history |
| X7 | body parts | the same pages | none: `check` and `registry` | GUARD-001 | every operation LANDED; every guard passes; BIND, NAME and REL guards at 0 | page history |
| X8 | 17, 21 | Glow Operations Hub, register | 21 and 3 operations | DN-9; C-10; C-23 | `activation_render_102726.py plan` and `check --phase part17`, which evaluate the Hub and register guards (G-W6-HUB-*, G-W6-REG-*) on the normalized reads: W6's counts before, every guard passing after | page history |
| X9 | 24 | catalog (new), Flow Index, five hubs, register | candidate records; C-REG's link filled with `--set @CONTROLS_PR=<number>`, refused unfilled | L-A13 / L-B2; D-W8-3, D-W8-5; C-26 | `check --phase candidate`; `control_check_102726.py --phase candidate` | page history |
| X10 | 24, 13 | regenerator, R1 successor | Q0 to Q2 | D23 successor; L-A14 | 100926.1 contract EQUAL; R1 47 rows at the recorded digests | discard scratch |
| X11 | 24, 08–10, 13 | candidate and production graphs | Q3, Q4 | C-11 | 56 · 240 · 56; route checks; flip-only difference | discard scratch |
| X12 | 24 | 102726.1 contracts | Q5 | W7-D5; C-7; C-19 | 56 ids; no `promoted_at`; semantic equality; PLAN pin | none |
| X13 | 24 and skill parts | 4 packages | Q6: 105 redlines, build, gates in two copies | D24; D28; W7-D2, W7-D3 | all LANDED; suite, fixtures, validators pass with only C-21's named findings | rebuild |
| X14 | 24 | 56 bodies | Q7, `x12_qualify_102726.py` | promotion predicate 1 | 56 validated, none unevaluated, `ok` | stop |
| X15 | 24 | `GCFPE-PCR-20261027.1` | Q8 | D13; GUARD-001 | validator 0; 56 rows; every regression reported | revert |
| X16 | 24 | the 4 packages | Q9, D24, two reviewers | D24; D26-A | both `SKILL_FIT_CONFIRMED` on the same digests | repair within cap |
| X17 | 24 | the release | Q10, post-flight, two reviewers; the brief names `plan/normalize_fetch.py` as the one text form, and the reviewers run `x12_qualify_102726.py` and `registry_assemble_102726.py assertions` on their own reads | postflight-procedure; C-15; C-25 | `PASS` or `PASS WITH WARNINGS`, no mandatory finding; both runs report the normalized form (56 bodies validated, none unevaluated; 56 rows evaluated) | stop |
| X18 | 24 | Flow Index; packet | C4, Q11; controls merge checked on `main` | DN-1 D2 | every packet value from a receipt; pins recorded | none |
| X19 | 25 | all | P0 | promotion approval | selection, pins, map, digests, v5.1.0 sha256 equal | stop |
| X20 | 25, 19 | entry (new), catalog, PE, Flow Index, five hubs, Alpha checklist | P1 bindings | D17 | `check`; `control_check_102726.py --phase activation --register-pending` | stop |
| X21 | 25, 19 | register | P2, last; procedure binding to v5.1.0 | D17; CD-9 | ten pages pass; selection names 102726.1 / 56 and v5.1.0 | stop |
| X22 | 25 | installed skills | P3: Nathan installs 4 | D24 | `freeze.py` digests equal the reviewed ones | reinstall |
| X23 | 25 | activated state | P4, `x18_validate_102726.py` | D17 | every flag; 56 bodies; every row passes | stop; no archival |
| X24 | 25 | 57 pages | P5, move to the archive | D17; D29 | all 57 under the archive, intact; `--phase archived` ok | move back |
| X25 | 25 | workspace | P6, sweep by literal; never a member body | authoritative-surfaces | a second search finds none | page history |
| X26 | 25 | this branch | R1 to R5: parts, registry, surfaces, D31, §E, the surfaces and D31 by `plan/repo_edits_102726.py --set X26` with the receipts' values; promotion pull request | D17; C-23 | token reproduced; registry checks; validator | revert |
| X27 | 25 | `main` | R7 after Nathan's merge, detected by files | D26-C | token, registry, D31, digests on `main` | stop |
| X28 | all | backlog; record pull request | dispositions; `ECOSYSTEM_CHANGE_COMPLETE` | template rule 5 | backlog rows re-fetched | page history |

### Decisions applied

DN-1 to DN-12, CD-1 to CD-15 with Nathan's CD-6 and CD-9 conditions, and the opt-ins L-A12 / L-B1, L-A13 / L-B2 and L-A14 apply as recorded in §A.14. C-1 to C-26 apply as recorded in `plan/coordinator-decisions.md`. Among them:
- C-1, the cascade: every member citing a changed member's page gets a successor, so 54 plus PE plus CL-05.
- One successor map, written once.
- D30 is recorded now, the PART-02 note follows it, and the promotion entry is D31.
- A frozen PLAN file is pinned by the contract.
- The controls pull request is merged before the packet.
- One normalized text form for every check.
- C-16's judged lines.
- CL-05's parent comes from the map.
- One successor's write is read back before the batch.

PART-15 and PART-22 close `NOT_APPLICABLE` (DN-8 (c)). PART-16 and PART-18 are accepted risks (DN-7 (a), DN-10 (b)). PART-23 closes delivered (DN-11, in Nathan's words). PART-19's binding moves inside PART-25 (CD-9). R-P1 and R-P2 are prepared as excluded conditional sets (C-13).

### Open findings, accepted as risks

28, P-L1 to P-L28, each with its path, likelihood, consequence and reason in PLAN §10, together with those accepted at ANALYZE approval (§A.13, less the three opt-ins). They include:
- C-11's stale `candidate_member_rule`;
- C-19's carried parent ids;
- C-21's pre-existing suite findings;
- C-15's pre-existing rendering failure of the selected registry;
- the Hub's "all 55" line;
- C-16's judgement calls;
- stand-in-dependent digests;
- the Ops Hub's volatility;
- R-P1, R-P2 and the governance-audit lines of C-3, which are Nathan's.

Approving this plan accepts them (`DISP-001`).

### Product Owner actions

- Approve this plan in Nathan's own words, saying whether R-P1 and R-P2 are opted in.
- Merge the controls pull request before X18; X18 and P0 verify it on `main`.
- Approve promotion of the exact X18 packet snapshot.
- Install the four packages at X22, verified by `freeze.py` digest.
- Merge the promotion pull request; X27 verifies it from `main`.
- Merge the record pull request.

Each merge preserves the record and approves nothing (D21-C).

### Explicitly not in scope

- J-1 to J-14 and the C-14 backlog rows.
- The governance-audit lines (C-3); R-P1 and R-P2 unless opted in.
- QA-70's delta-mode retirement.
- The TW ecosystem and PE's general rules.
- typesafe-scoring and session-relay-flowmaster.
- The selected 100926.1 contract bytes.
- PF canon and A-10's canon inconsistencies.
- Alpha state.

### Disclosed deviations

- **Branch.** The branch is the harness's `claude/ecosystem-change-mgmt-drvb4v`, not `docs/20261027-modification-gcfpe-backlog-open-items`, as ANALYZE used the harness's branch.
- **Riders.** The four riders (ITEM-33 to ITEM-36) were added at approval, inside the frozen scope.
- **Cascade.** C-1 widens ITEM-31's measured surface to 54 runtime successors, PE and CL-05. No item is added.
- **PF10.** PF10 moved to v13.9 after ANALYZE's v13.8.9 baseline.
- **Merges.** The controls pull request adds a third merge to §A.8's count.
- **Re-price.** EXECUTE is re-priced at 18–30 h and 16–26M, replacing 24–40 h and 12–20M (PLAN §13).
- **D30-A.** D30-A was corrected in place on the unmerged branch under C-24: its delta bullet now reads by work unit, as ITEM-15 does, and L-C1 stays an accepted risk.

### Return to Nathan — 2026-10-27

**`PRODUCT_OWNER_ACTION_PENDING` — `DECISION NEEDED`: approve this plan, and say which of four opt-ins you take.**

- **The plan is reviewed.** It had a dry run (failed once, repaired under D26-F trigger 2, then passed N0 to N10), one FULL round by two fresh reviewers, and one check of the repair's diff by a third. Required defects went **4 → 0**.
  - Round 1: [REVIEW-PLAN-1-A.md](evidence/20261027-gcfpe-backlog-open-items/REVIEW-PLAN-1-A.md), [REVIEW-PLAN-1-B.md](evidence/20261027-gcfpe-backlog-open-items/REVIEW-PLAN-1-B.md). The four required (R-1, R-2, R-B1, R-B2) are repaired as C-23 to C-26 in `plan/coordinator-decisions.md`.
  - Diff check: [REVIEW-PLAN-DIFF.md](evidence/20261027-gcfpe-backlog-open-items/REVIEW-PLAN-DIFF.md): all four fixed, none with a new defect.
- **Who set this stop:** D26-A (two FULL reviews at most, then one diff check; a second FULL round was not needed). Every open finding is listed below; approving the plan accepts them (`DISP-001`).
- **Correction, stated once:** while repairing, the PLAN document's introduction was also changed to state D26-A's bound correctly ("at most two FULL reviews, then one diff check"). That resolves round 1's listed L-8, which the repair record does not name (L-D4).
- **Scope:** still 36 items. The cascade (C-1: 54 runtime successors, PE and CL-05; GCFPE-MGMT-10 kept) is ITEM-31's measured surface; both reviewers confirmed it is the coordinator's call and that its fixpoint holds.

**Your opt-ins.** Each is outside the frozen scope, so none is applied unless you say so.

| Opt-in | What it does | Cost |
|---|---|---|
| **R-P1** | The stale drained-addendum citation ITEM-33 fixes, also in flowmaster-validate `SKILL.md:168` (and a fixture comment) and change-flow `SKILL.md:305` (and its revision note). PF10 v13.9 restarted at 2.1, so these now point at the unrelated S19 addendum | zero: both packages are rebuilt anyway; the redlines are prepared as an excluded set |
| **R-P2** | PE's "from the release after 100926.1" corrected to 091426.1 | zero: one PE operation, prepared and dry-run |
| **L-C1** | IA-30's delta review also checks a criterion or outcome a delta changes without editing a work unit (accepted as a risk at ANALYZE; reverted here under C-24) | small: the reverted clause, D30-A's wider bullet and G-W2-EM-2's cut, restored; one more fresh dry run of IA-30 |
| **Governance-audit lines** (C-3) | The two lines in amthor-workspace-governance-audit that keep ITEM-08's retired rule (now MB-045) | not prepared: a fifth package, review and install, so a plan revision |

Recommendation: take R-P1 and R-P2; leave L-C1 and the governance-audit lines on the backlog.

**Approval, in one line if you take the recommendation:** "approve the plan of MODIFICATION-20261027-gcfpe-backlog-open-items at `<commit>` with R-P1 and R-P2, accepting the open findings listed in §P." Name any opt-in you choose differently. `plan_approved_by` stays empty until you approve (D21-C: merging approves nothing).

**Open findings, accepted as risks on approval** (path; likelihood; consequence). Each is listed rather than repaired because none meets R1 to R4 (D26-A rule 3). The plan's own 28 are P-L1 to P-L28 in [PLAN-20261027.md](evidence/20261027-gcfpe-backlog-open-items/PLAN-20261027.md) §10. The reviewers' are below; their full text is in the three records.

| ID | Finding | Path | Likelihood | Consequence |
|---|---|---|---|---|
| L-1 / L-B4 | X2's duplicate check passes on a duplicate missing a span no anchor, guard or profile marker reaches | normal | low | content lost silently outside every guarded passage |
| L-2 / L-B1 | X5's head-first page (PR-50) writes no `<code>`, `<b>` or `\_` span; those first appear in X6's 55-page batch | normal | possible | loud at X7, then 55 pages restored by Nathan from page history (D26-B) |
| L-3 / L-B2 | the normalizer ships in no skill: after promotion, raw-read audits and profile runs report false failures (now MB-050) | normal, after promotion | certain | false failures that can hide a real reintroduction |
| L-4 | X14's `ok` was never observed true; 111 contract-level errors were accepted as probe artefacts | normal | possible | a loud stop at X14 |
| L-5 / L-B8 | the binding pass matches exact predecessor titles only, and rewrites any "<title> — 100926.1", historical mentions included | normal | low | a variant title survives, or a historical mention is rewritten |
| L-6 / L-B5 | the controls pull request stays open while X2 to X17 commit to the same branch; no merge detection before X18 | normal | likely | post-merge commits mis-landed or a conflict at X26 (loud) |
| L-7 | C-REG cited #768 | — | — | repaired as R-B2 (C-26) |
| L-8 | the D26-A bound stated as one FULL round | — | — | resolved by the wording change (L-D4) |
| L-9 | merges and review rounds undercounted in `interaction_cost` (see below) | normal | certain | the prediction understated by about 4 |
| L-10 / L-B10 | P-L6 counts "four exceptions on five rows"; the receipt has five exceptions on four prompts | normal | certain | a count only |
| L-11 | D30's guard paragraph says "§P lists five guards"; PLAN §3 PART-04 lists them | normal | certain | wording |
| L-12 | C-16's DOC-10 G-HP-5 exception is a judgement call | normal | low | ITEM-08 arguably incomplete on DOC-10 |
| L-13 | GCF-24.CLOSE sits in the material partition although the stage is on every close path | normal | certain | a consumer treating non-core rows as optional misreads it; the must-fail fixture mitigates |
| L-14 | DN-5 (a)'s "no PF10 addendum" rests on QA-70's existing contract only, with no guard | normal | low | a successor approval read as a material delta |
| L-15 | C-15's "no verdict changes but rendering ones" is shown by counts, not class by class | normal | possible | an unreconciled class difference |
| L-B3 | the 100926.1 catalog and CL-05 candidate ids are not forbidden in member bodies | normal | low | silent if real: a body points at an archived page |
| L-B6 | binding by page URL makes D23-G's "unchanged keeps its page" reachable only for GCFPE-MGMT-10 (now MB-051) | — | certain | a design cost, not a defect |
| L-B7 | frontmatter `interaction_cost_predicted` (23) and `estimate.execute` are ANALYZE's and differ from §P's re-price | normal | certain | the validator does not compare them |
| L-B9 | W6-PE-14g removes "preserve exactly one operative Alpha baseline" with the stale baseline | normal | certain | low; the remaining sentence keeps the rule |
| L-D1 | X8 refuses a page whose before-count differs from W6's, even when a foreign edit removed a retired line | failure | low | a loud stop before any write |
| L-D2 | `@CONTROLS_PR` and `@PROCEDURE_PR` name one pull request from two sources, unchecked for equality | failure | low | two pull requests cited on the register |
| L-D3 | C-24's L-C1 opt-in was not in the plan's actions | — | — | answered by this return's opt-in table |
| L-D4 | the L-8 wording change was not disclosed | — | — | disclosed above |
| L-D5 | `repo_edits_102726.py check --state before` reports `ok` without `--values` | normal, if misinvoked | low | a before-check that tests no marker; no write follows |
| L-D6 | X26's after-check defaults to `origin/main`; a stale one fails falsely | failure | low | a loud false stop |
| L-D7 | the EXECUTE TypeSafe action text says four control files; X1 writes five | normal | certain | the reading's input is worded slightly low |
| L-D8 | D30 carries no mark of its in-place correction; the disclosure is in §P, PLAN §12 and C-24 | normal | certain | a decision-record reader sees no trace; branch history keeps it |

**Recorded on the backlog now** (template rule 3), read back: MB-045 (governance-audit lines), MB-046 (QA-70's authorless delta mode), MB-047 (the continuing named-session sentence, D27), MB-048 (the Hub's "all 55"), MB-049 (the pre-existing suite failure), MB-050 (raw-rendering audits, S2), MB-051 (binding by URL, not rated), and an update on MB-039. R-P1 and R-P2 go on it only if you do not take them.

**Interaction cost.** Predicted 23 at ANALYZE. On today's count it is about 27: two more review rounds (ANALYZE's and PLAN's diff checks), and two more merges (this record's pull request and the controls pull request). Answering the opt-ins with the approval keeps the rest at the prediction.

**Spend, PLAN.**
- **Time:** about 6 h 25 min, from the approval at about 04:45Z to about 11:10Z, inside the 10–16 h estimate.
- **Tokens:** subagents 10.4M as the harness reported them (design workers 4.39M, assembly 2.01M, dry-run repair 1.83M, drafting 0.49M, PLAN reviewers A and B 0.86M, round-1 repair 0.42M, reviewer C 0.27M, backlog worker 0.15M), plus the coordinator's about 0.5M: about 10.9M. That is above the 6–10M estimate and under twice it, so D26-D needs no re-price. The binding cascade and the dry-run repair drove the excess.

**EXECUTE, re-priced:** 18–30 h and 16–26M tokens, excluding your waiting time (PLAN §13), against ANALYZE's 24–40 h and 12–20M.

**TypeSafe reading for the EXECUTE session.** Taken by running the installed TypeSafe scoring skill's script once on the action text in [typesafe-execute.md](evidence/20261027-gcfpe-backlog-open-items/typesafe-execute.md). The skill's Notion row was not written.
- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.89 (confidence 0.39); rung probabilities low 0.02, medium 0.14, high 0.17, extra high 0.40, max 0.14, ultracode 0.13. Model probabilities Fable 5.1 0.01, Opus 5.5 0.97, Sonnet 5.5 0.01, Haiku 5.5 0.01 (confidence 0.96). The 24 cells are in the evidence file. Flags: none printed. Sent 2026-10-27T10:34:38Z. Nathan picks the cell.
- **Surface advice** (no model or effort content): a Claude Code cloud session on this branch, with GitHub push, the Notion connector (writes at X2 to X9, X18, X20 to X25 and X28) and the TypeSafe service attached, and the installed skills directory readable. The four installs at X22 and the merges are yours, on your own surfaces. The session is long, so compaction is likely: it resumes only at D26-C's checkpoints (X0, X18, X27), and X2, X5, X6, X8, X9, X20, X21 and X28 are not safe to send twice.
- **Your pick:** recorded here when you state it; none is recorded now.

**Then.**
- **In this session:** on your approval I record it in the frontmatter with your words quoted here, apply your opt-ins, and go on to EXECUTE at X0 (D21-D).
- **In a fresh session:** invoke GCFPE-MGMT-10 with `MODE = EXECUTE` and `MODIFICATION-20261027-gcfpe-backlog-open-items`, naming branch `claude/ecosystem-change-mgmt-drvb4v` until its pull request merges.

### Approval to enter EXECUTE — 2026-10-27

Nathan, approving, in the EXECUTE invocation of 2026-10-27:

> "approve the plan of MODIFICATION-20261027-gcfpe-backlog-open-items at `58e20b0` (merged to main as `229a4291`) with R-P1 and R-P2, accepting the open findings listed in §P, with two conditions:
> - After X5 and before the rest of X6, send one successor whose operations carry <code>, <b> and \_ spans, and confirm on a fresh read that every one of its operations LANDED before the remaining pages are written (reviewer A's smallest fix for L-2).
> - At X0, if PF10 has moved past v13.9, read every addendum it adds. If they are silent on this Modification's subjects, record that and continue; otherwise stop and return."

**What this approves.**

| Subject | Answer | Effect on EXECUTE |
|---|---|---|
| The plan | approved at `58e20b0` | `58e20b0`'s tree is `main` `229a4291`'s (`8c810564…`), so the plan EXECUTE runs is the one on `main`. `PLAN-20261027.md` is frozen at that tree (sha256 `a3b11f46…`, 84,106 B; C-11, P-L14) |
| R-P1 | opted in | X4 and X13 run with `--with-conditional R-P1`: the stale drained-addendum citation also leaves flowmaster-validate `SKILL.md:168` and its fixture comment, and change-flow `SKILL.md:305` and its revision note (C-13) |
| R-P2 | opted in | X4 runs with `--with-conditional R-P2`: PE's "from the release after 100926.1" reads 091426.1 (C-13) |
| L-C1 | not opted in | stays an accepted risk on the backlog (C-24) |
| Governance-audit lines (C-3) | not opted in | stay on the backlog as MB-045; no fifth package |
| Open findings | accepted | every finding §P lists, P-L1 to P-L28 and the reviewers' L-1 to L-D8, with those accepted at ANALYZE approval (`DISP-001`). P-L9 and P-L10 are resolved by the opt-ins rather than accepted |
| Condition 1 (L-2 / L-B1) | adopted | between X5 and the rest of X6, one successor whose operations carry `<code>`, `<b>` and `\_` spans is sent alone and every one of its operations is confirmed `LANDED` on a fresh read before the remaining pages are written (§E, X6a) |
| Condition 2 (PF10) | adopted | X0(c) reads PF10 on `main`; if it has moved past v13.9, every addendum it adds is read, and EXECUTE stops and returns unless all are silent on this Modification's subjects |

Because R-P1 and R-P2 are taken, neither goes on the backlog (C-14).

**The EXECUTE session's model and setting.** The invocation repeats the reading in [typesafe-execute.md](evidence/20261027-gcfpe-backlog-open-items/typesafe-execute.md) (TypeSafe v8.2: Opus 5.5 at extra high) and ends "Nathan picks the cell"; it states no pick, so none is recorded.

## §E — Execution

*Written by MODE = EXECUTE, which began 2026-10-27 after the approval above.*

| step | part | disposition | evidence |
|---|---|---|---|
| X0 | all | VERIFIED | Fresh reads of the 57 pages and the 11 control pages by seven read-only workers, captured 11:30:20–11:33:56Z after `fetched-after` 2026-10-27T11:29:52.469Z. (a), (b), (f): `plan/dry_run_102726.py run` on those reads ([execute/x0-dry-run.json](evidence/20261027-gcfpe-backlog-open-items/execute/x0-dry-run.json), `--previous-receipt plan/dry-run.json`): `ok` true, every gate N0 to N12 and the dry run's self-test true. N0: 9 of 9 installed skills and their copies equal W7's digests; `docs/graph/parts` builds `55 nodes · 235 edges · 55 state_routes · 593569 bytes · 43f84f29…`, D29's token. N2: 57 of 57 pages read, every revision at its pin, none moved; 559 of 559 operations apply once (113 binding under the stand-in map); 57 batches safe; 756 guard rows, 240 failing before and 0 after; with R-P2, PE 16 operations and no guard failing. N10: control pins 10 of 10 and the 100926.1 catalog's read-only pin match; the Glow Operations Hub also reads at its PLAN revision `2026-10-27T03:02:37.191Z`. N11 and N12 pass. (c) `main` `229a4291` carries only `PF10-HDE-Build-Notes-v13.9.md`; its §1.1 index lists one addendum, 2.1 (S19 vendor and security policy), and a search of 2.1's body for this plan's topics finds none, so PF10 has not moved past v13.9 and Nathan's condition 2 needs no further read. (d) the register's first current section is *Current selection — GCFPE-20261009.1 / 100926.1*, "exactly 55 members", at its pin `2026-10-12T17:17:45.991Z`. (e) a workspace search for `102726.1` finds no page titled "— 102726.1". (g) `grep -c '^## D30 — '` on the branch's decision record: 1 (also on `main`). (h) Nathan's words take R-P1 and R-P2 (§P, *Approval to enter EXECUTE*) |
| X1 | PART-02, 19, 20, 21, 28 | VERIFIED | `plan/repo_edits_102726.py --set X1` ([execute/x1-repo-edits-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x1-repo-edits-102726.1.json)). Before: `ok`, the 20 `old` strings at their counts, v5.1.0 absent, the 7 repository guards at W6's counts (19F 4, 19R 0, 20R 0, 21F 2, 21R 0, 28F 1, 28R 0). Apply: 5 files written. After: `ok`, each `new` once and each `old` only inside its own replacement; G-W6-RE-19F 0, 19R 2, 20R 1, 21F 0, 21R 4, 28F 0, 28R 1; v5.0.0 byte-equal to `origin/main`; the PART-02 note heading once, after `## D30`; `reviewer-prompt-template.md` at 1.3. A second apply is refused (`NEW_FILE_EXISTS`, `OLD_COUNT`) and writes nothing. Committed at `ccb5de0`; `modification_validate.py` 17 of 17. The controls pull request is [amthorn78/glow-hdengine-v2#770](https://github.com/amthorn78/glow-hdengine-v2/pull/770), recorded once in [execute/controls-pr-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/controls-pr-102726.1.json) at `ff7039a`. Nathan merges it before X18 (C-12) |
| X2 | PART-24 | VERIFIED after AM-1 | Started 11:40:48.720Z. One `notion-duplicate-page` call on W8's first row, CF-C-10 (`3f44590a05eb810f83d4d539e5b0e588`), at 11:40:51Z created `4064590a05eb811e821bc064f56de3a3` under the HDE Change Flow hub, its planned parent, so no move was needed. It was not retitled. Fresh read (as of 11:40:52.663Z): parent as planned; no child page; the body's first line equals the source's. **But Notion remapped both of the body's self-references**: the source's id (2 occurrences) became the duplicate's own id, and the self-mention's title reads "… — 100926.1 (1)". With those remapped back, the body equals the source's. So `HEAD-CF-C-10-U`, whose start anchor is the predecessor's own `Notion URL` mention, resolves 0 times. In memory, `body_check.py plan --no-ops --prompts CF-C-10` on the duplicate's read, with a scratch map naming the duplicate: `START_COUNT_0`, `ops_not_applied` `["HEAD-CF-C-10-U"]`, `ok` false. `edits.json` carries 54 such head self-mention operations on 54 pages, so X4's verification, "every operation applies once", cannot pass on any successor: the plan is wrong. The other 55 duplications and the title were not run. First run: BLOCKED, as above; D26-B record and Nathan's decisions below. **After AM-1, VERIFIED.** In Nathan's order, CF-C-10's kept duplicate was retitled; PE was duplicated as `4064590a05eb8173b2e7d37929e7fe4d` under the TW hub; and CL-05 as `4064590a05eb814fba57ed387ee2cddd`, moved under the HDE Change Flow hub; both were retitled. Fresh reads after 12:02:02.990Z: all three pass X2's checks ([execute/x2-three-verify-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x2-three-verify-102726.1.json)). X4's `body_check.py plan` in memory on those reads, with a scratch map naming the three, returned `ok`, 3 of 3 ([execute/x2-three-x4-plan-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x2-three-x4-plan-102726.1.json)): every revision at its pin; CF-C-10 10 operations, with `HEAD-CF-C-10-U` `SATISFIED_BY_DUPLICATION`; PE 16 operations (R-P2's included); CL-05 27; every batch safe; no guard failing after; bindings current, 0 unresolved. Then the other 53 sources were duplicated once each, in two runs: two rows in one lane (a narrower launch than intended, disclosed below) and 51 in six lanes. Each id was logged when its call returned; each page was fetched once and retitled; none was moved, since each landed under its planned parent. Every source was duplicated exactly once ([execute/x2-duplications-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x2-duplications-102726.1.json)). Fresh reads of the 56 duplicates, their 56 sources and GCFPE-MGMT-10 after 12:17:20.643Z: `page_facts_102726.py x2` `ok`, 56 of 56 ([execute/x2-verify-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x2-verify-102726.1.json)): parent as planned, title exact, the body's first line the source's, fully copied (same line count), no child page, source revision unchanged, and 56 distinct new ids |
| X3 | PART-24 | VERIFIED | [execute/successor-pages-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/successor-pages-102726.1.json), written once by `execute/write_successor_map_102726.py` from the X2 logs and the reads after 12:17:20.643Z (each revision is the duplicate's newest read, after its title). It records 56 members: 54 `SUCCESSOR`, each with a distinct new id and its TSV predecessor; GCFPE-MGMT-10 `KEPT` at `3f74590a05eb81b69bd8c27106f7a59d`; CL-05 the only `ADDED`, duplicated from the candidate; and PE `4064590a05eb8173b2e7d37929e7fe4d`. `successor_map_102726.py check` with no `--stand-in-ok`: `map_ok`, no errors. `binding_pass.py validate`: `ok` |
| X4 | all body parts | VERIFIED after AM-2 | Fresh reads of the 56 successors and GCFPE-MGMT-10 by seven read-only workers after 12:23:13.860Z. `body_check.py plan --no-ops --successor-map <map> --with-conditional R-P1 R-P2` ([execute/x4-plan-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x4-plan-102726.1.json)): `ok` false, 55 of 57 pages `ok`. CL-E-20 and DOC-10 fail `G-W8-NAME-1` after the edits; the cause is in *Failure record — 2026-10-27, X4*. Every other predicate holds on all 57: 57 revisions at their map pins, 1,134 operations apply once, 54 head self-mentions `SATISFIED_BY_DUPLICATION` (AM-1), 57 batches safe, 57 landing checks would pass, 57 bindings current, 0 unresolved, 295 guard rows failing before and 2 after. GCFPE-MGMT-10 needs no edit. First run: BLOCKED, as above; D26-B record and Nathan's decisions below. **After AM-2, VERIFIED** on the same reads: `ok`, 57 of 57 pages ([execute/x4-plan-am2-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x4-plan-am2-102726.1.json)). 1,190 operations: 1,136 apply once and 54 are `SATISFIED_BY_DUPLICATION`. 57 revisions at their pins, 57 batches safe, 57 landing checks would pass, 57 bindings current, 0 unresolved; 0 of 756 guard rows failing after |
| X4b | all (Nathan's addition after X4) | VERIFIED, with tool rows recorded | `plan/dry_run_102726.py run` once, read-only, on the real successor map and the X4 reads (`fetched-after` 2026-10-27T12:23:13.860Z; four control pages read fresh after it so all 11 have reads after the X4 cut-off), with AM-1 and AM-2 applied ([execute/x4b-dry-run-real-map-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x4b-dry-run-real-map-102726.1.json)). **First attempt:** it stopped in N11 with a `KeyError` before writing a receipt. N11 rehearses X1's repository edits on copies of the live target files, which already carry X1 (landed at `ccb5de0`, #770), so its before-check refused and its report code could not read the refusal. **Second attempt,** the receipt above: run from a scratch worktree of this branch's `5ddc98b` in which only X1's five target files were put back to their pre-X1 state from `229a4291` (the four edited files restored, v5.1.0 removed); the tool, the plan, AM-1, AM-2, the map and the reads were unchanged, and the worktree was then removed. **Gates:** N0 `true` (9 of 9 digests; the selected graph token `43f84f29…`); N1 `true` (`body_check.py` 118 guards, 377 fixture rows; the stand-in refusal row `NOT_APPLICABLE_REAL_MAP`); N2 `true` (57 of 57 pages, every revision at its map pin; 1,135 operations apply once (PE's R-P2 operation is rehearsed in its own row); 57 batches safe; 57 landing checks would pass; 57 bindings current; 756 guard rows, 295 failing before and 0 after); N3 `true` (329 fixture rows and 756 page rows, the registry form agreeing everywhere); N4 `true` (candidate and production graphs check and route); N5 `true` (R1 successor 47 rows matching the decision record; contracts run; Q1 PASS); N6 `true` (42 substitutions); N7 `true` (56 bodies through the 102726.1 profile, normalized text); N9 `true` (56 of 56 body rows, 3,177 assertions, 0 findings after, 972 injected regressions reported, 0 missed); N11 `true`; N12 `true`; the dry run's self-test `true`. **False, because the tools cannot take the real map without a code change** (Nathan's rule: recorded, and X5 follows). N8 is false only on `package_build_102726.py`'s self-test case `stops_on_stand_in_map_without_flag`: it drops `--stand-in-ok` and expects the build to stop, which happens only with a stand-in map. The build itself passes (105 redlines landed; exit 0; check byte-identical; G1 and G3 to G6 true; the suite's only findings are C-21's three pre-existing ones). N10 is false because `activation_render_102726.py`'s self-test and its two `--chain` runs refuse stand-in marker values with a real map ("stand-in marker values are refused with a real successor map", its line 91). The rest of N10 passes: `make_activation_ops` check, `control_check` self-test 40 of 40 (archive set 57), today's control pages failing as they must, and PART-17's plan on the fresh Hub and register reads (24 operations, guards at W6's counts before and all passing after). No gate failed on a body, an operation or a guard |
| X5 | PART-24 | VERIFIED | 13:01Z: PR-50's one update_content, from X4's plan on the X4 read (`execute/payload_102726.py`): 9 operations, the head title line `HEAD-PR-50-T` and 8 binding mention rewrites to successor pages; `HEAD-PR-50-U` is `SATISFIED_BY_DUPLICATION` and was not sent. The call returned success with no warning. Fresh read (as of 13:01:37.364Z): `body_check.py check --prompts PR-50` `ok` ([execute/x5-check-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x5-check-102726.1.json)): revision moved; `HEAD-PR-50-T` and `HEAD-PR-50-U` `LANDED`; bindings current; 10 of 10 guards pass. The title line, `Prompt ID: PR-50` and the `Notion URL` mention read back in the planned form at the successor's own URL `4064590a05eb81dcbf95e23b4112e43c`; the predecessor's id no longer occurs in the body |
| X6a | PART-24 (Nathan's condition 1) | VERIFIED | After X5 and before the rest of X6, CF-C-30 was sent alone: its operations carry all three span forms (`<code>`, `<b>` and `\_`). 13:02Z: one update_content, 10 operations (W2-CF-C-30-BC-1 and -BC-2, C16-CF-C-30-01, `HEAD-CF-C-30-T` and 6 binding operations; `HEAD-CF-C-30-U` satisfied by duplication), success with no warning. Fresh read (as of 13:03:01.779Z): `body_check.py check --prompts CF-C-30` `ok` ([execute/x6a-check-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x6a-check-102726.1.json)): revision moved; every operation `LANDED`; bindings current; 14 of 14 guards pass. The `<code>PF04-Canon-HDE-Governance</code>` span, both `<b>…— 102726.1</b>` titles and the `INITIAL\_APPROVE` and `INITIAL\_DENY, CORRECTION\_REDLINE, or DELTA\_DENY` escapes read back exactly as sent, and no `— 100926.1</b>` remains. So every operation LANDED before the remaining pages were written (Nathan's condition 1) |
| X6 | PART-01, 03–14, 24, 26, 27 | APPLIED | 13:07–13:24Z, by six write workers, one lane each, two at a time. One update_content on each of the remaining 54 successors, each payload printed on stdout by `execute/payload_102726.py` from `body_check.py plan` on the X4 read and sent once: 1,117 operations, one call per page (no page needed the `--max-chars` fallback); every call returned success, with no warning. With X5's 9 and X6a's 10: 56 pages, 1,136 operations ([execute/x6-writes-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x6-writes-102726.1.json), ids and counts only). The 54 head self-mentions satisfied by duplication were not sent (AM-1) |
| X7 | all body parts | VERIFIED | Fresh reads of the 56 successors and GCFPE-MGMT-10 by seven read-only workers after 13:24:41.758Z. `body_check.py check --successor-map <map> --with-conditional R-P1 R-P2` ([execute/landing-check-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/landing-check-102726.1.json), counts, ids and revisions only): on all 56 written pages `ok`, each revision moved from its map pin; 447 checked operations, every one `LANDED`; bindings current on all 57; 756 of 756 guard rows pass, so every forbidden guard finds no surviving old text (template rule 4, D26-E); `G-W7-BIND-1` and `G-W8-NAME-1` 0 on all 57 bodies and `G-W7-REL-1` 0 on its 56. GCFPE-MGMT-10 is the only row with `ok` false, and only on `revision_moved`: it is the KEPT member, with no operations, and the plan does not change it (PLAN §2), so its revision stays at its pin as it must. `body_check.py registry --audit-root <installed amthor-workspace-governance-audit>`: `ok`; 329 fixture rows and 756 page rows, the registry form agreeing on every row |
| X8 | PART-17, 21 | BLOCKED | Fresh reads of the Hub and the register after 13:29:44.374Z: the Hub at `2026-10-27T03:02:37.191Z`, pinned at that read (`--pin`), and the register at its pin `2026-10-12T17:17:45.991Z`. `activation_render_102726.py plan --phase part17`: `ok`. On the Hub, 21 operations apply and none is refused, with its notion-control guards at W6's before-counts (`G-W6-HUB-F` 13, RH 0, RN 0, RP 0); on the register, 3 apply, with `G-W6-REG-F` 4 and RN 0. 13:30–13:31Z: one update_content per page, the register's 3 then the Hub's 21, each returning success with no warning. Fresh reads after 13:31:46.801Z: `activation_render_102726.py check --phase part17` `ok` false ([execute/x8-check-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x8-check-102726.1.json)). Both revisions moved, and every guard is at W6's after-count (`G-W6-HUB-F` 0, RH 4, RN 2, RP 2; `G-W6-REG-F` 2, RN 2), with control `ok` and 0 findings on both. But only 22 of 24 operations read `LANDED`: `W6-REG-3` and `W6-HUB-10` hold their text in Notion's split-bold form (*Failure record — 2026-10-27, X8*). The register's *Current selection* is unchanged |
| X9 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X10 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X11 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X12 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X13 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X14 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X15 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X16 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X17 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X18 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X19 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X20 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X21 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X22 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X23 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X24 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X25 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X26 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X27 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |
| X28 | — | NOT_RUN | the stop at X8 (*Failure record — 2026-10-27, X8*) |

### Failure record — 2026-10-27, X2 (D26-B)

EXECUTE stops at X2. The plan's normal path cannot be executed mechanically on a real duplicate. GCFPE-MGMT-10: "If the plan is wrong, stop and return; do not repair it in flight." This comes after the first external write, so D26-B applies: a failure record that reaches `main` in a record pull request, a read-only sweep, the freeze kept, and a return to Nathan.

- **What is wrong.** Each runtime successor's head operation `HEAD-<ID>-U` (54 in `plan/edits.json`) rewrites the duplicate's `Notion URL` self-mention from the predecessor's URL to the successor's. On a real duplicate, Notion has already made that rewrite: it remaps the page's own references to the new page.
  - So the operation's start anchor is absent, and X4's predicate cannot pass.
  - In memory, with the retitle simulated, the duplicate's self-mention equals the operation's `new` text. `body_check.py`'s landing predicate already counts it `LANDED` (start absent, `new` present). Only X4's "applies once" cannot be met.
- **Why the dry run missed it.** The PLAN dry run used the stand-in map, in which each successor is its own predecessor page and nothing is duplicated (PLAN §4, *Stand-ins*). No dry-run read was ever of a real duplicate.
- **Read-only sweep, 11:43:12–11:43:39Z.** One read-only worker fetched four pages, one call each; header facts by `execute/page_facts_102726.py`:
  - the duplicate `4064590a05eb811e821bc064f56de3a3`: under the HDE Change Flow hub, titled "CF-C-10 — Prepare CRD Specification Kickoff Handoff — 100926.1 (1)", 0 child pages, revision `2026-10-27T11:40:52.663Z`;
  - its source CF-C-10 100926.1: at its pin `2026-10-12T02:29:03.544Z`, unchanged;
  - the HDE Change Flow hub: its revision moved to `2026-10-27T11:40:52.663Z` because the duplicate is now its child page, and the hub lists it;
  - the register: at its pin `2026-10-12T17:17:45.991Z`; its first current section is still *Current selection — GCFPE-20261009.1 / 100926.1*.
- **What is live.**
  - Notion: that one duplicate page. Nothing else was written: no title, move, body operation or control page.
  - Repository: this branch, in the open pull request [amthorn78/glow-hdengine-v2#770](https://github.com/amthorn78/glow-hdengine-v2/pull/770), which carries X1's five controls and this record.
  - Skills: nothing built or installed.
- **The freeze is kept.** No Notion write, package build or install follows until Nathan decides.
- **The record reaches `main`** when #770 merges. That merge is Nathan's, and it preserves the record and approves nothing (D21-C).

### Disclosed deviations (EXECUTE)

- **Branch.** This session runs on the harness's `claude/ecstatic-mccarthy-m9b2lz`. The PLAN branch `claude/ecosystem-change-mgmt-drvb4v` merged as #769 and no longer exists. `main` `229a4291` has the approved tree, so this branch began equal to it.
- **X2, one in-memory comparison (D22).** To diagnose the failed anchor, the duplicate's body was compared once in memory with its source's X0 read: lengths, the positions of differing segments, counts of the two page ids, and equality after remapping the ids. D22 forbids comparing a body with another read. Nothing was written and no digest was taken. The result is used for the diagnosis above, not as X2's verification.
- **An EXECUTE helper.** `execute/page_facts_102726.py` reports header facts (revision, title, parent, child-page count, body length) from this session's fetch records, using `body_check.py`'s reader. It was added for X0(d) and X2's checks. It prints no body text.
- **Fetch results saved by the harness.** At X0 and in the sweep, the harness saved six large fetch results to its own tool-results folder. Workers did not open them, and the tools read them only as D22 transient reads. They stay there for the harness's cleanup.
- **X2, a narrower launch than intended.** The first launch for the remaining duplications was given only two rows (CF-C-20 and CF-E-40) instead of all 53. Both were duplicated once and retitled. The relaunch read its 51 rows from a file and excluded those two, so no source was duplicated twice. `write_successor_map_102726.py rows` refuses any prompt with more or fewer than one duplication.
- **X2, two helpers and the readiness test.** `execute/x2_partial_map_102726.py` builds the scratch map for Nathan's three-page check; it refuses any path in the repository. `execute/write_successor_map_102726.py` writes the map once. `page_facts_102726.py` tests a duplicate's readiness by line count and first line, not character count, because Notion's remap changes a duplicate's length.
- **X6a, a payload in a scratch file.** CF-C-30's payload was written once to a scratch temp file for one command, then deleted at once. The plan's rule is that payloads travel on stdout only (D22); nothing was committed, and later payloads are read from stdout. The batch helper `payload_102726.py` gained a `--max-chars` fallback, which sends a payload too large for a worker's tool output to show in full as ordered chunks, one call each.

### Return to Nathan — 2026-10-27, after X2

**EXECUTE stopped at X2 after one duplication: on a real duplicate, Notion has already rewritten the page's self-mention, so the plan's 54 `HEAD-<ID>-U` operations cannot apply, and X4 cannot pass. `DECISION NEEDED`.**

| # | Question | Recommendation |
|---|---|---|
| 1 | How the plan defect is repaired | amendment AM-1, below |
| 2 | What happens to the CF-C-10 duplicate | keep it as CF-C-10's successor |
| 3 | The record pull request | merge #770 now |

**1. The repair.** The head operation exists to point each successor's `Notion URL` line at the successor. Duplication already does that, so the end state is right; only the plan's tool refuses to count it. If nothing changes, X4 fails on all 56 pages, and EXECUTE can go no further.
- **Option A, AM-1 (recommended).** In `plan/body_check.py`'s `plan` mode, a head self-mention operation counts as `SATISFIED_BY_DUPLICATION`, and is not sent, only when:
  - its start is absent;
  - its expanded `new` text occurs exactly once;
  - the page's own id appears where the predecessor's did.
  The change is recorded in §E as AM-1, as PIN-1-A and AM-2 were in the precedent. Three self-test cases go with it (satisfied; neither present; `new` twice), the self-test is rerun, and CF-C-10's duplicate is planned in memory after its retitle, all before any further write. X5's and X7's checks are unchanged, since their landing predicate already accepts this state. Cost: about 45 minutes and under 0.5M tokens.
- **Option B: a PLAN successor section.** A full re-plan of the head operations, a dry run on a real duplicate, and one D26-A diff check. Cost: several hours, about 2–4M tokens, and another approval round trip.

**2. The duplicate** `4064590a05eb811e821bc064f56de3a3`, titled "… — 100926.1 (1)", sits under the HDE Change Flow hub.
- **Keep it (recommended).** X2 resumes by retitling it and continues from W8's second row. Its id goes into the successor map at X3.
- **Archive it.** Move it to *04 Archived Prompt Versions* (X2's rollback) and duplicate CF-C-10 again.

**3. Record pull request.** #770 now carries this failure record and X1's controls. C-12 needs those controls on `main` before X18 anyway.
- **Merge #770 now (recommended).** The run then continues on this branch, restarted from `main`, in a new pull request.
- **Keep it open.** The failure record stays off `main` until it merges, which D26-B step 1 does not intend.

**Spend in EXECUTE so far.**
- **Time:** about 25 minutes, 11:20Z to 11:46Z.
- **Tokens:** about 1.4M of subagent tokens (the X0 reads 1.09M, the sweep 0.10M, two single-read probes 0.18M), plus the coordinator's.
- That is well inside the 18–30 h and 16–26M re-price.

**In one line, if you take the recommendations:** "AM-1 as described; keep the CF-C-10 duplicate; I merge #770 as the record pull request."

### Nathan's decisions after X2 — 2026-10-27

Nathan's words:

> "AM-1 as described, with one addition: after CF-C-10, duplicate PE and CL-05 next, and run X4's plan check in memory on those three real duplicates before duplicating the rest. Keep the CF-C-10 duplicate. I have merged #770 as the record pull request; continue on a branch restarted from main, in a new pull request."

**Applied.**

- **The record pull request.** #770 merged as `5b3ccdc`, detected by files on `main` (D26-C):
  - the X2 failure record, `execute/controls-pr-102726.1.json` and the v5.1.0 file are on `main`;
  - `reviewer-prompt-template.md` is at 1.3;
  - `main`'s tree equals the branch's (`50aa28c1…`).

  The branch `claude/ecstatic-mccarthy-m9b2lz` was deleted at merge. It was restarted from `main` at `5b3ccdc` and pushed fresh, and the run continues in a new pull request. #770 also merged X1's controls, so C-12's precondition for X18 is met; X18 still verifies it by files.
- **AM-1**, in [plan/body_check.py](evidence/20261027-gcfpe-backlog-open-items/plan/body_check.py), committed before any further Notion write.
  - *The rule.* In `plan` mode, a head self-mention operation (`head: true`, its start a `<mention url=…>`) whose start is absent counts as `SATISFIED_BY_DUPLICATION`, and is not sent, when two things hold:
    - its expanded replacement occurs exactly once;
    - that replacement names the page's own URL.
  - *What `plan` reports.* `ops_satisfied_by_duplication` lists them, `ops_not_applied` excludes them, and a page's `ok` accepts them.
  - *Unchanged.* `check` mode, `apply_all`, the batch-safety check and the payload: an operation satisfied this way is never in `ops_payload_for_execute`.
  - *Scope.* `edits.json` has exactly 54 operations whose start or end names their own page's 100926.1 id, all head self-mentions (`HEAD-<ID>-U`). PE's head (`HEAD-PE`, frontmatter) and CL-05's (`HEAD-CL-05`, on `Prompt ID: CL-05`) name none, so AM-1 reaches only those 54.
  - *Self-test.* `body_check.py selftest`: `ok`; 118 guards; 377 fixture rows, none failing. Five AM-1 cases are added, each true:
    - a duplicate whose self-mention already names the duplicate is satisfied;
    - with neither the start nor the replacement present, it is refused;
    - with the replacement present twice, it is refused;
    - a head operation that is not a self-mention never qualifies;
    - with the start still present, it is not satisfied.

  The fifth case, beyond the three described, shows the rule never displaces an operation that can still apply. No other plan file changes, and `PLAN-20261027.md` is untouched (C-11, P-L14).
- **The order of X2**, Nathan's addition:
  1. retitle CF-C-10's duplicate `4064590a05eb811e821bc064f56de3a3`, which is kept;
  2. duplicate PE, then CL-05, moving CL-05 under the HDE Change Flow hub;
  3. read all three fresh and run X4's `body_check.py plan` on them in memory, with a scratch map that names the three real duplicates;
  4. only if that passes, duplicate the remaining 53.

  The scratch map is not the successor map: X3 writes that once, after all 56.

### Failure record — 2026-10-27, X4 (D26-B)

EXECUTE stops at X4, before X5's first body write. X4's verification is not met on 2 of 57 pages, and the cause is a second plan defect from the same remap as X2's: the plan's normal path still cannot be executed mechanically on real duplicates. D26-B applies, as at X2.

- **What failed.** `body_check.py plan` on fresh reads of the 56 successors and GCFPE-MGMT-10 after 12:23:13.860Z, with the successor map and `--with-conditional R-P1 R-P2` ([execute/x4-plan-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x4-plan-102726.1.json)).
  - Not met on 2 pages: `ok` false, 55 of 57 pages `ok`. On CL-E-20 and DOC-10, `G-W8-NAME-1` (no body names a member with a successor by its "— 100926.1" title) fails after the edits.
  - Every other predicate holds on all 57:
    - every revision at its map pin;
    - 1,134 operations apply once, and the 54 head self-mentions are satisfied by duplication (AM-1);
    - every batch safe; the landing check would pass;
    - bindings current, 0 unresolved;
    - 295 guard rows failing before, 2 after.
- **The cause.**
  - On each of those two pages, one line names the page itself twice: its own title in a `<code>` span, then a self-mention.
  - On the source page, that self-mention carried the predecessor's URL. So the binding pass treated the whole line as stale and rewrote both the mention and the `<code>` title (the PLAN dry run, on the stand-in map, did exactly that).
  - On the real duplicate, Notion has remapped that self-mention to the duplicate, and it renders the new "… — 102726.1" title. The binding pass's C-9 rule skips any line that already carries `102726.1`, so the line is left alone and the `<code>` title "… — 100926.1" survives.
  - `G-W8-NAME-1` passes on the other 55 pages, so no other page has such a line.
- **Read-only sweep.**
  - The X4 reads above are a fresh read of all 57 member pages after the last write. Each is at its map revision: the duplicate's state after its title, with no body edit.
  - The register, the Flow Index and the five hubs were read after 12:30:00.255Z: the register at its pin `2026-10-12T17:17:45.991Z`, its first current section still *Current selection — GCFPE-20261009.1 / 100926.1*; the Flow Index at its pin `2026-10-12T17:17:19.872Z`; each hub's revision moved only because the duplicates are its children, and each holds exactly twice its member count: Change Flow 38 (19 + 19), IA 42 (21 + 21), QA 20 (10 + 10), Escalation 8 (4 + 4), TW 4 (2 + 2)
- **What is live.**
  - Notion: the 56 successor pages, created, placed and titled, their bodies as duplicated, and nothing else. No body operation, control page or register change.
  - Repository: this branch, in draft [amthorn78/glow-hdengine-v2#771](https://github.com/amthorn78/glow-hdengine-v2/pull/771), with AM-1, the successor map and this record.
  - Skills: nothing built or installed.
- **The freeze is kept.** No Notion write follows until Nathan decides.
- **The record reaches `main`** when #771 merges (D21-C: merging preserves the record and approves nothing).

### Return to Nathan — 2026-10-27, after X4

**EXECUTE stopped at X4, before any page body was written. On 2 of the 56 real duplicates, CL-E-20 and DOC-10, the plan would leave each page's own old title "… — 100926.1" in one line, so X4's guard `G-W8-NAME-1` fails. `DECISION NEEDED`.**

| # | Question | Recommendation |
|---|---|---|
| 1 | How this second remap defect is repaired | amendment AM-2, below |
| 2 | The record pull request | mark #771 ready and merge it as the record pull request |

**1. The repair.** The binding pass rewrites every line that cites a superseded member. Its rule C-9 skips a line already carrying "102726.1". On a real duplicate, the page's own self-mention, remapped by Notion, now carries "102726.1", so C-9 also skips a line whose other citation, the page's own title in a `<code>` span, is still stale. If nothing changes, those two bodies keep their superseded titles, and X4, X7 and the post-flight all fail on them.
- **Option A, AM-2 (recommended).** In `plan/binding_pass.py`'s `generate`, C-9's test ignores the page's own successor self-mention, so that a line whose only "102726.1" is that self-mention still has its stale citations rewritten. Nothing else changes.
  - **Measured in memory** on the X4 reads (no file changed): X4 then passes on all 57 pages. Only CL-E-20 and DOC-10 change, each gaining one binding operation. 1,136 operations apply, 54 are satisfied by duplication, and 0 guard rows fail after.
  - **With it:** three self-test cases (a remapped self-mention line with a stale own title gets one operation; a line with any other "102726.1" is still skipped; after the operation the line is current), then the self-tests rerun and X4 rerun on these same reads before X5. Cost: about 30 minutes and under 0.3M tokens.
- **Option B: two stored operations instead.** One per page, on the `<code>` title, added to `plan/edits.json` through its assembler. It reaches only these two lines, and it leaves the binding pass blind to the same pattern if it recurs. Cost: similar, and `assemble_edits.py` must regenerate `edits.json`.

**2. Record pull request.** #771 is a draft and now carries both failure records, AM-1 and the successor map.
- **Mark it ready and merge it now (recommended):** D26-B step 1, as #770 was. The run then continues on this branch, restarted from `main`, in a new pull request.
- **Keep it open:** the X4 record stays off `main` until it merges.

**Spend in EXECUTE so far.**
- **Time:** about 1 h 10 min, 11:20Z to 12:31Z.
- **Tokens:** about 5.4M of subagent tokens, plus the coordinator's. The X0, X2-verify and X4 reads were 3.6M; the duplication lanes 1.1M.
- That is inside the 18–30 h and 16–26M re-price.

**In one line, if you take the recommendations:** "AM-2 as described (option A); I merge #771 as the record pull request."

### Nathan's decisions after X4 — 2026-10-27

Nathan's words:

> "AM-2 as described (option A), with one addition: before X5, run the plan's dry run (plan/dry_run_102726.py) once, read-only, on the real successor map and the X4 reads with AM-1 and AM-2 applied, and record its gates in §E. If it fails, stop and return before any body write. If the tool cannot take the real map without a code change, record that and continue to X5. I have merged #771 as the record pull request; continue on a branch restarted from main, in a new pull request."

**Applied.**

- **The record pull request.** #771 merged as `f480456`, detected by files on `main` (D26-C): the X4 failure record, the successor map and AM-1 are on `main`, and `main`'s tree equals the branch's (`ddcfffbb…`). The branch was restarted from `main` at `f480456` and pushed fresh. The run continues in a new pull request.
- **AM-2**, in [plan/binding_pass.py](evidence/20261027-gcfpe-backlog-open-items/plan/binding_pass.py), committed before any body write.
  - *The rule.* `generate`'s C-9 test ("a line already carrying 102726.1 is skipped") ignores the page's own successor self-mention. A line whose only "102726.1" is that self-mention, remapped by Notion, still has its stale citations rewritten. A line carrying any other "102726.1" is skipped exactly as before, so the self-test's existing C-9 case is unchanged.
  - *Self-test.* `binding_pass.py selftest`: `ok`, 32 checks. Three AM-2 cases are added, each true:
    - a remapped own self-mention line with a stale own `<code>` title gets one operation and is clean after;
    - a line with another member's "102726.1" is still skipped;
    - after the operation, the line is current.
  - `body_check.py selftest`: `ok`; 118 guards; 377 fixture rows, none failing.
- **X4 rerun** on the same reads (after 12:23:13.860Z; nothing was written since), `body_check.py plan --no-ops --successor-map <map> --with-conditional R-P1 R-P2`: `ok`, 57 of 57 pages ([execute/x4-plan-am2-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x4-plan-am2-102726.1.json)).
  - Revisions: 57 at their map pins.
  - Operations: 1,190, of which 1,136 apply once and 54 are `SATISFIED_BY_DUPLICATION`; none is left unapplied.
  - Pages: 57 batches safe, 57 landing checks would pass, 57 bindings current, 0 unresolved.
  - Markup and references: 0 markup spans refused, 0 references dropped.
  - Guard rows: 756, of which 295 fail before and 0 after.
  - Only CL-E-20 and DOC-10 changed against the first X4 run, each gaining one binding operation.
- **The dry run before X5, Nathan's addition.** Its result is recorded below as X4b, before any body write.

### Failure record — 2026-10-27, X8 (D26-B)

EXECUTE stops at X8, after PART-17's two writes. X8's verification requires all 24 operations `LANDED`. 22 do; the other two hold their text in a form the landing check does not read as landed. D26-B applies.

- **What failed.** `activation_render_102726.py check --phase part17` on fresh reads after 13:31:46.801Z ([execute/x8-check-102726.1.json](evidence/20261027-gcfpe-backlog-open-items/execute/x8-check-102726.1.json)): `ok` false.
  - The register: 2 of 3 operations `LANDED`; `W6-REG-3` not.
  - The Glow Operations Hub: 20 of 21; `W6-HUB-10` not.
  - Both revisions moved.
  - Every PART-17 guard passes at W6's after-count: `G-W6-HUB-F` 0, `G-W6-HUB-RH` 4, `G-W6-HUB-RN` 2, `G-W6-HUB-RP` 2, `G-W6-REG-F` 2, `G-W6-REG-RN` 2.
  - Both pages' control judgement is `ok`, with 0 findings.
  - The register's first current section is still *Current selection — GCFPE-20261009.1 / 100926.1*.
- **The cause.** `W6-REG-3` and `W6-HUB-10` are the same edit on the two pages. It extends a sentence inside a bold run, "superseded for required GCFPE read-only source checks:", with ", and for addendum numbering by `<code>PF06-Canon-Change-Process-Guide</code>` §0.1A:".
  - Notion stored the inline code by closing and reopening the bold around it: `…by </b><b><code>PF06-Canon-Change-Process-Guide</code></b><b> §0.1A:`.
  - On each page that form occurs once, the planned raw form occurs 0 times, and the normalized page text contains the normalized planned text. The bold runs balance.
  - The landing check compares raw text (C-15 keeps landing on the raw read), so it reads both as not landed.
  - The 56 bodies had no such case: all 447 checked operations landed at X7.
- **Why it blocks.** X9's `activation_render_102726.py plan --phase candidate` refuses any page on which an earlier phase's listed operation has not landed. The register is that page: C-REG is appended to it at X9, and P2 writes it later. The Hub's later sweep operations meet the same refusal.
- **Read-only sweep.** No page has changed since its last read:
  - the two X8 pages, read after their writes (above);
  - the 56 successors and GCFPE-MGMT-10, read at X7 after their writes (after 13:24:41.758Z);
  - the Flow Index and the five hubs, read at 12:30, before the body writes. The writes do not touch them, but a page's revision is the newest edit in its subtree, so the hubs' revisions have moved; that is expected, and X9 re-pins them.
- **What is live.**
  - Notion: the 56 successors with all 1,136 operations, the register's three PART-17 operations, and the Hub's twenty-one. Nothing else changed: no candidate record, no catalog, no selection.
  - Repository: this branch, in draft [amthorn78/glow-hdengine-v2#772](https://github.com/amthorn78/glow-hdengine-v2/pull/772).
  - Skills: nothing built or installed.
- **The freeze is kept.** No Notion write follows until Nathan decides.
- **The record reaches `main`** when #772 merges (D21-C).

### Return to Nathan — 2026-10-27, after X8

**EXECUTE stopped at X8. Both PART-17 pages hold every planned edit, and all their guards pass. But on one edit per page Notion stored the inline code by splitting the surrounding bold, so the raw landing check reads 2 of 24 operations as not landed. X9 refuses to write the register until they read as landed. `DECISION NEEDED`.**

| # | Question | Recommendation |
|---|---|---|
| 1 | How the landing check treats Notion's split bold | amendment AM-3, below |
| 2 | The record pull request | mark #772 ready and merge it as the record pull request |

**1. The repair.** The landing check proves an operation's replacement is on the page. Notion rewrites `<b>A <code>B</code> C</b>` as `<b>A </b><b><code>B</code></b><b> C</b>`: the same text and formatting, in a different raw form. If nothing changes, X9 refuses the register, and every later step that writes the register or the Hub refuses the same way.
- **Option A, AM-3 (recommended).** In `plan/activation_render_102726.py`'s landing predicate, an operation also counts as `LANDED` when the page holds its replacement after one fold: `</b><b><code>` read as `<code>`, and `</code></b><b>` as `</code>`, on the read and the replacement alike. Nothing else changes.
  - With it: a self-test case each way (a split replacement lands; a missing one still does not), the self-tests rerun, and X8's check rerun on these same reads, before X9's first write.
  - Cost: about 30 minutes and under 0.3M tokens.
  - The prompt bodies need no change: none of their operations met this form.
- **Option B: a re-write.** Write the two sentences again in Notion's split form, so the raw check matches. That is two more Notion writes, outside the plan's operations, and the next nested code span would stop the run the same way.

**2. Record pull request.** Draft #772 carries this record, AM-2, the X4b dry run and every receipt through X7.
- **Mark it ready and merge it now (recommended).** The run continues on this branch, restarted from `main`, in a new pull request.
- **Keep it open.** The X8 record stays off `main` until it merges.

**Spend in EXECUTE so far.**
- **Time:** about 2 h 15 min, 11:20Z to 13:36Z.
- **Tokens:** about 7.8M of subagent tokens, plus the coordinator's. Reads were about 5.7M; the duplication and write lanes 2.0M.
- That is inside the 18–30 h and 16–26M re-price.

**In one line, if you take the recommendations:** "AM-3 as described (option A); I merge #772 as the record pull request."
