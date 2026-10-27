# Worker briefs — MODIFICATION-20261027-gcfpe-backlog-open-items

The ANALYZE pass ran as one bounded multi-agent pass (D26-F trigger 5: more than ten live bodies and more than one skill package), as a Workflow of nine read-only maintenance workers (D23 clarification: GCFPE-MGMT-10 workers may be subagents; `execution-and-delegation-model.md` §5). Six verifiers (V1, V2, V3, V4, V5a, V5b) each tested a cluster of backlog entries as claims against the live state. Three sweepers (LA, LB, LC) applied fixed regex families to all 55 bodies and PE.

Run `wf_e0631317-013`, 2026-10-27 01:08–02:59Z: 9 of 9 returned, 0 errors, 837 tool calls. Concurrency was 2 (a 4-CPU container), so the agents ran two at a time.

Below is the complete script the workers ran under, as executed (sha256 `eef04c43069abee985783f1769010fa226250bd5b36964ad70219eb3e2b3b21a`, 32007 bytes). Each verifier received `COMMON`, its cluster brief and the item schema; each sweeper received `COMMON`, the sweep brief and the families. The script holds no prompt-body text.

```javascript
export const meta = {
  name: 'mgmt10-analyze-backlog',
  description: 'GCFPE-MGMT-10 ANALYZE: verify every open backlog item against live 100926.1 bodies, skills and canon on main, and sweep all bodies by broad match',
  phases: [
    { title: 'Verify', detail: 'six cluster verifiers test each open entry as a claim against live state' },
    { title: 'Sweep', detail: 'three lanes apply fixed regex families to all 55 bodies plus PE' },
  ],
}

const S = args.S
const REPO = '/home/user/glow-hdengine-v2'

const COMMON = `
You are a read-only maintenance worker for a GCFPE-MGMT-10 run in MODE = ANALYZE (decision record D23's clarification: MGMT-10's workers may be subagents; execution-and-delegation-model.md §5: a worker writes nothing). Your job is to apply settled rules, not to revisit them. If a ruling looks wrong, say so in unresolved_questions and stop on that point.

HARD LIMITS
- Write nothing to the repository, to any git branch, or to Notion. No commit, push or PR. You may write only (a) findings files under ${S}/out/, and (b) a transient file needed to grep a prompt body, under decision D22's five conditions (outside the repository; serves only this read; never hashed or byte-compared; deleted when done, or left to harness teardown if deletion is refused; disclosed in transient_files).
- Never copy a prompt body into the repository or keep one for later. Reading bodies is unrestricted.
- Do not author plan steps or redlines. Do not decide policy: record it as a question for the Product Owner (Nathan) with options.

WHERE THINGS ARE
- Repository: ${REPO}, checked out at main @ 44dba78 (the branch head equals main). Read files directly. Search with grep/find (rg is not installed).
- Governing documents: docs/prompt_ecosystem_management/ — gcfpe.decision-record.md (D1–D29; D23-B handoffs; D23-E/F PR-40 entry and re-plan; D25-B; D26), ecosystem-change-management.md (classes A–E §2; defect classes §4), authoritative-surfaces.md, modification-template.md. AGENTS.md (canon-first rule; code review guidelines incl. "Report a finding only when its triggering input is real").
- Graph: docs/graph/parts/prompts/<ID>.json (routing, edges, state_routes). Closure: PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/closure.py <ID>. Registry: docs/prompt_ecosystem_management/project-prompt-contract-registry.md (535 KB; grep it, never read it whole).
- Installed skills (read-only): /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/<skill>/. Digest recipe: PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/freeze.py <skill dir>.
- Prompt bodies: selected release GCFPE-20261009.1 / 100926.1 / 55. ${S}/members.tsv maps each prompt key to its Notion URL and title. Read with the Notion fetch tool (load it first: ToolSearch query "select:mcp__Notion__notion-fetch"). A large result is saved by the harness to a file: read it by slice or grep. PE Metaprompt 100926.1: https://app.notion.com/p/3f44590a05eb81f98b76c83465dc1960.
- Backlog entries under test, verbatim from the GCFPE Modification Backlog (Notion page 3e54590a05eb81eb818fd0f42045167a, last edited 2026-10-26T02:46Z): ${S}/backlog/MB-XXX.md. Its header and severity scale: ${S}/backlog/_header.md.

THE FACT THAT MOVED (verified by the coordinator; apply it)
PF10 on main is PF10-HDE-Build-Notes v13.8.9 (effective 2026-10-26) and carries NO addenda ("No current addenda"). The 35 addenda of v13.8.8 (2.1–2.35) were drained by a GTWPE run whose ledger is docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md (read "Precedence and closure controls", "Complete source inventory" rows A01–A35, and "Held and deferred items"). The drained canon replacements were moved into docs/pfcanon/ by PR #762: PF02 v2.4.7, PF04 v2.8.8, PF05 v2.5.4, PF06 v2.5.5, PF07 v2.3.4, PF09.3/.4/.7, PF12 v2.9.7, PF14 v3.5.9, PF19 v3.0.7, PF27 v2.0.6, PF29 v1.0.3, PF30.1 v0.9.2. The ledger states that for 2.1, 2.3, 2.11, 2.14, 2.18, 2.31 and 2.34 "the GCFPE prompt and skill wording changes belong to GCFPE-MGMT-10 and the Product Owner, not to a PF document."
Under PF10 front matter §6 you must NOT read any older PF10 base version (v13.8.8 or earlier), including through git history. Where a backlog entry cites "PF10 addendum 2.x", (1) read the ledger row for 2.x to learn its named permanent targets, then (2) read that permanent canon section on main and quote it. If the permanent canon does not carry the rule (the ledger records some addenda as "N for PF canon"), say so plainly: that rule may now have no live canon home, which changes the entry's authority.

METHOD
- Each backlog entry is a CLAIM to test against the live state, not a fact. Refute by default. Decide still_present from what the live text does, not from its words (NAME-001, FUNC-001). A grep proves the absence of a string, never the absence of a behaviour: search for what the text does.
- Every evidence quote is verbatim: exact characters as fetched or as stored, never retyped from memory or normalised (EVID-001). Location = nearest section heading (Notion) or path:line (repository).
- Canon-first: search docs/pfcanon/*.md for the entry's terms and read every governing section you rely on in full. Record each document, version and section in canon_resolved.
- Scope is measured by broad match minus permitted exceptions, never by enumerating known phrasings (SCOPE-001). State the method beside the number.
- Classify each item A–E per ecosystem-change-management.md §2 (A rule change needs a Product Owner ruling recorded as a D-number before execution; B applies an existing ruling or canon; C repairs a control; D one prompt fails its own contract; E normalisation — do not do). Say when it is genuinely ambiguous.
- effect: ROUTING if graph routing (edges, result states) would change; PRODUCES if what a prompt produces changes but not routing; BOTH; TEXT_ONLY if only stale wording with no behaviour change; NONE if nothing to change.
- sequential_discovery = true only if this item's scope cannot be measured until another item has been executed.
- Escape hatch: report any in-scope line your instructions do not cover, and anything adjacent you notice that is outside these items (adjacent_scope) — do not widen the items.
- If a source cannot be fetched or uniquely resolved, record it in not_checked with the reason; never infer absence.
`

const ITEM_SCHEMA = {
  type: 'object',
  properties: {
    mb_id: { type: 'string' },
    still_present: { type: 'string', enum: ['YES', 'NO', 'PARTIAL', 'UNVERIFIED'] },
    verdict: { type: 'string' },
    evidence: { type: 'array', items: { type: 'object', properties: { source: { type: 'string' }, location: { type: 'string' }, quote: { type: 'string' }, bears_on: { type: 'string' } }, required: ['source', 'location', 'quote', 'bears_on'] } },
    moved_since_entry: { type: 'array', items: { type: 'string' } },
    authority_now: { type: 'string' },
    canon_quotes: { type: 'array', items: { type: 'object', properties: { document: { type: 'string' }, section: { type: 'string' }, quote: { type: 'string' } }, required: ['document', 'section', 'quote'] } },
    targets: { type: 'array', items: { type: 'string' } },
    class_proposal: { type: 'string' },
    class_ambiguous: { type: 'boolean' },
    effect: { type: 'string', enum: ['ROUTING', 'PRODUCES', 'BOTH', 'TEXT_ONLY', 'NONE'] },
    graph_change: { type: 'string' },
    scope: { type: 'object', properties: { method: { type: 'string' }, count: { type: 'string' }, detail: { type: 'string' } }, required: ['method', 'count', 'detail'] },
    po_questions: { type: 'array', items: { type: 'object', properties: { question: { type: 'string' }, options: { type: 'array', items: { type: 'string' } }, why_his: { type: 'string' } }, required: ['question', 'options', 'why_his'] } },
    dependencies: { type: 'array', items: { type: 'string' } },
    severity_now: { type: 'string' },
    risks: { type: 'array', items: { type: 'string' } },
    defect_classes: { type: 'array', items: { type: 'string' } },
    sequential_discovery: { type: 'boolean' },
    sequential_reason: { type: 'string' },
  },
  required: ['mb_id', 'still_present', 'verdict', 'evidence', 'moved_since_entry', 'authority_now', 'canon_quotes', 'targets', 'class_proposal', 'class_ambiguous', 'effect', 'graph_change', 'scope', 'po_questions', 'dependencies', 'severity_now', 'risks', 'defect_classes', 'sequential_discovery', 'sequential_reason'],
}

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    cluster_id: { type: 'string' },
    items_surveyed: { type: 'array', items: { type: 'string' } },
    base_commit: { type: 'string' },
    canon_resolved: { type: 'array', items: { type: 'object', properties: { document: { type: 'string' }, version: { type: 'string' }, sections_read: { type: 'string' } }, required: ['document', 'version', 'sections_read'] } },
    items: { type: 'array', items: ITEM_SCHEMA },
    adjacent_scope: { type: 'array', items: { type: 'object', properties: { finding: { type: 'string' }, evidence: { type: 'string' }, suggested_severity: { type: 'string' } }, required: ['finding', 'evidence', 'suggested_severity'] } },
    unresolved_questions: { type: 'array', items: { type: 'string' } },
    transient_files: { type: 'array', items: { type: 'string' } },
    not_checked: { type: 'array', items: { type: 'object', properties: { what: { type: 'string' }, reason: { type: 'string' } }, required: ['what', 'reason'] } },
  },
  required: ['cluster_id', 'items_surveyed', 'base_commit', 'canon_resolved', 'items', 'adjacent_scope', 'unresolved_questions', 'transient_files', 'not_checked'],
}

const CLUSTERS = [
  { id: 'V1', items: ['MB-001', 'MB-013', 'MB-014', 'MB-023', 'MB-024'], brief: `
CLUSTER V1 — PR review findings, the P1 rule, the Codex security review, and PR-40 entry.
- MB-001: read DOC-20's body (Result routing) and DOC-10's description of the same step; read docs/graph/parts/prompts/DOC-20.json and run closure.py DOC-20 to establish whether DOC-20 has a PR-40 edge. Compare with D23-E and its successor "PR-40 is entered once per merge" in the decision record, and with PR-40's own entry text.
- MB-013: read PR-35's body: "Review-first and action-efficient execution" steps 3 and 4, "Genuine merge-readiness gate", "Remote-action ledger and durable checkpoints". Test: is there any class for a finding whose triggering input is constructed? any repeated-class escalation? Find where the drained rules of 2.11 (rules 4,5 real inputs/constructed input, 7, 8 repeated finding class) and 2.18 (no cost ceiling) now live in permanent canon (ledger rows A11, A18: PF27 "Source-bound review authority and exact-fix limits", PF06 §1.1.4, PF04 §9.7.7) and quote them. Also quote AGENTS.md's code-review rule on real inputs.
- MB-014: the installed glow-hde-pr-development skill (1.4.0). Confirm SKILL.md sha256 is 5091aa26e65354f5d7f1873bf7b9e273649e362955b6ad5f4f0265cea7f66c4b and the tree's freeze digest. Read sections "4. In PR-35, put review findings before stale CI", "5. In PR-35, reach genuine merge readiness", "Control remote-action cost", and references/behavior-cases.md "Open review findings and active CI".
- MB-023: the 2.14 P1 rule (a P1 on a real input is fixed and never declined; only a P1 on a non-real input may be declined, Product Owner first). Ledger row A14 names PF27 and PF06 §1.1.4: quote the drained text. Check PR-35 step 3 and PR-40 for any P1 handling.
- MB-024: the skill's line naming "Codex code and security reviews" (entry says line 90); PR-35 "Required inputs and continuity identity" and step 2. Ledger row A03 says 2.3 is "N for PF canon" and H-06 holds PF04 §9.1.1's review-chain entry as undecided. Read PF04 v2.8.8 §9.1.1 and search all canon for "Codex" and "security review". State what authority now supports removing the Codex security review wording, given PF10 2.3 is gone.
- For all five: the batching the entries ask for (MB-013 + MB-014 + MB-023 + MB-024 in one PR-35/PR-40 body change and one skill package) — confirm or refute that they must land together (one rule across its surfaces).` },
  { id: 'V2', items: ['MB-002', 'MB-010', 'MB-015', 'MB-016', 'MB-017', 'MB-018', 'MB-019'], brief: `
CLUSTER V2 — the business case and real inputs in planning and review, PR-20's PR-40 description, and the handoff-package sentence.
- MB-015: CF-C-30 and CF-E-30 bodies: "Review modes and inputs" (INITIAL_SPECIFICATION_REVIEW), "Execute" step 1, "Required result". Broad-match each body for business|value|benefit|beneficiar|budget|cost|measure|warrant and read every hit in context.
- MB-016: IA-30 body: "Execute" -> "Initial Plan review" checklist; "Material Plan-delta review"; the shared Material definition.
- MB-017: PR-10 body: "Execute" step 2 (the instruction's contents); "Semantic readiness before INSTRUCTION_READY"; "Working rules". Test for any pin-or-precondition rule for external systems.
- MB-018: PR-20 body: "Execute" steps 3 to 5 and step 7 ("challenge assumptions and boundary cases"); "Required result".
- MB-019: PR-30 "Required result"; PR-40 "Execute" step 3 and "Required result": does either record whether the unit's business-case measure was met? (The ceiling part is withdrawn.)
- Canon for MB-015..019: ledger rows A11 and A18 name PF04 §9.7.7, PF27 "Business Case (MUST)", PF30.1 §4.1, PF06. Read the drained sections on main and quote what each now requires (business case per requirement and per work unit? for CRDs as well as Epics? beneficiary, evidence, benefit, measure? no cost ceiling? the emulation / pin-or-precondition rule (2.11 rule 6)? real-input set?). If a rule the entry relies on is NOT in permanent canon, say so.
- MB-002: PR-20's "Native result and boundary" PR-40 DOWNSTREAM description ("REJECT returns precise in-scope findings to the PR owner"?) versus PR-40's own REJECT routing and D23-F (re-plan through PR-20). Check PR-20's and PR-40's graph parts for the REJECT edge.
- MB-010: the sentence "Each handoff carries the complete native input package, exact artifact and version lineage, session identity, manual prerequisites, recovery context and result-specific terminal behavior" (or its family) in PR-10, PR-20, PR-30, PR-40 "Managed entry, execution posture and continuing identity", OPS-20 and PR-40 "Direct native handoff packages"; compare with D23-B and the same pages' "Mandatory single-block handoff" section. Also read D27's "Continuity" row. (A corpus-wide count of this family is run separately by sweepers; you establish the behaviour and the exact sentences in these six bodies.)
- Say which of these must land together (one rule across its surfaces) and which are independent.` },
  { id: 'V3', items: ['MB-020', 'MB-021', 'MB-022', 'MB-026'], brief: `
CLUSTER V3 — IA and QA routing gaps, and QA evidence persistence.
- MB-020: IA-40 body: "Controlled sources and exact-redline boundary", "Results and routing", "Handoff contract" — is REDLINE_INCOMPLETE still terminal to the same Isis reviewer with no continuation block? IA-30 body: "Review modes and inputs", "Required results and routing" — does any mode accept a returned redline? Read graph parts IA-40.json (branch redline_incomplete) and IA-30.json. Then MEASURE the entry's last bullet: which other author prompts return an unapplicable or ambiguous redline to their reviewer, and is that return terminal? Candidates by function, not name: every prompt whose role is applying a reviewer's redline (look in the graph parts for result states or branches like REDLINE_INCOMPLETE, *_RETURN, terminal returns to a reviewer; e.g. CF-C-40, CF-E-40, QA-80, RS-30, UTIL-10, CL-E-40, ESC prompts). State the method and the count.
- MB-021: QA-70 body "Required inputs and review mode" and "Required result and routing" (APPROVED_QA_PLAN_DELTA_REVIEW; delta DENY wording); QA-80 "Role and native purpose" ("never revises an already approved QA Plan") and WRONG_ROUTE_APPROVED_BASE. Is there now any prompt that authors an approved-QA-Plan delta? Read PF19 v3.0.7 (search for delta, approved QA Plan, Kronos, §10.6). Ledger rows A27 and A28: 2.27 "No canon change"; 2.28 PO-5 drains to PF19 §3.4.3. Read docs/ephemeral/HDE-CRD-0002-po-direction-qa110-f01-c1-route-v1.1.md (and v1.0) and state what authority now governs the route for a FUTURE change (HDE-CRD-0002 is closed).
- MB-022: QA-100 body "Execute" step 4 ("If a direct repository evidence commit is explicitly authorized…"); QA-90's commit-grant wording. Read PF19 v3.0.7 §3.4.3, §3.5.7, §4.4 for the drained evidence-persistence rule (PO-5) and quote it. Read docs/ephemeral/HDE-CRD-0002-po-direction-qa-evidence-persistence-v1.0.md (E-1, E-2). Does the body now contradict permanent canon?
- MB-026: QA-70 "Execute and decision criteria" step 2 and its INITIAL_QA_PLAN_REVIEW mode as used after QA-80; QA-80 "Execute" step 2; QA-50 (does it let a check re-run what bound CI evidence proves — R5). Read the brief docs/ephemeral/GCFPE-alpha-feedback-qa-plan-approval-coherence-v1.0.md in full (its §3 requests 1–6, §5 acceptance replays, causes R4–R6) and check R4–R6 against 100926.1 as well. Read PF19 §3.3, §3.4.14 and PF27 "Evidence coverage" as the brief cites them, on main.
- MB-021 and MB-026 are on the same QA-70/QA-80 bodies: say whether they must land together.` },
  { id: 'V4', items: ['MB-027', 'MB-030'], brief: `
CLUSTER V4 — the close mutation set and the CL-05 stage.
- Read permanent canon on main for the drained 2.31 (ledger row A31): PF06 v2.5.5 §3.5.1 and §3.5.2 (and §3.5.2.1–§3.5.2.4, §1.0.6, §0.4.1.3); PF19 v3.0.7 §3.1.3 and the close-pack sections; PF27 v2.0.6 (a close-mutation-set task template beside the Ops Task Record?); PF12 v2.9.7 "Close-pack artifacts"; PF04 v2.8.8 §2.0.19. Quote exactly what canon now says about a stage that prepares and publishes the close mutation set, its entries (from QA-120 PASS?), its exit to the closure decision, DO_NOT_CLOSE returns, close-tooling repair, and "Dev, not Ops".
- Read the 100926.1 bodies QA-120 (its PASS routes and the close-pack measure), CL-C-10 and CL-E-10 (inputs, DO_NOT_CLOSE routes), and check IA-10, IA-30 and PR-10 only for whether they plan a close mutation set as a work unit. Read the graph parts QA-120.json, CL-C-10.json, CL-E-10.json for the edges that would change. Run closure.py on QA-120, CL-C-10 and CL-E-10.
- Read the candidate page "CL-05 — Prepare and Publish the Close Mutation Set — 102626.2 (candidate)" https://app.notion.com/p/4054590a05eb8155b301e2cb6dec31d5 in full, including its installation notes, and say what installing it as a release member requires (a new 56th member: graph part, registry row, catalog, register, Flow Index, lane hub; routing edges into and out of it).
- Read the HDE-CRD-0002 records of CL-05's first run and the closure: docs/ephemeral/ files named HDE-CRD-0002-CL-05-* and HDE-CRD-0002-CL-C-10-closure-decision-v1.2* (find them), and docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-close-mutation-set-stage-v1.0.md. Did the run expose further prompt or candidate defects (e.g. B-6) that bear on installing CL-05?
- MB-027: read its brief docs/ephemeral/GCFPE-alpha-feedback-epic-closure-evidence-task-v1.0.md (§4 requests 1–4, §6 acceptance) and say which requests CL-05 covers and which remain. The entry says "Take it with MB-027, which closes with it": confirm or refute.
- Classify carefully: installing a new member changes the release's membership and routing (is that Class A needing a D-number, or B applying canon PF06 §3.5 now carries?). Say if ambiguous.` },
  { id: 'V5a', items: ['MB-007', 'MB-009', 'MB-011', 'MB-012'], brief: `
CLUSTER V5a — PE Metaprompt, the Glow Operations Hub, and PF10 addendum numbering.
- Read PE Metaprompt 100926.1 in full (https://app.notion.com/p/3f44590a05eb81f98b76c83465dc1960).
- MB-007: PE's generic Glow addendum-authoring clause as it applies outside GCFPE (does it still say the producer does not allocate canon numbering and Nathan allocates the number?), and its "Standards and preservation" sentence about a standalone PF10 addendum not authorizing "live PF10 inspection, numbering, insertion…". Compare with PF06 v2.5.5 §0.1A (read on main) and PF27 "Canon precedence for template use". Which ecosystems besides GCFPE does PE govern (TW/GTWPE)? Does their own control (docs/prompt_ecosystem_management/gtwpe/) number at creation?
- MB-009: read the addendum-number clause of each of the six qualifying producers CF-C-30, CF-E-30, IA-30, QA-70, RS-20, ESC-40 (100926.1). Read PF10 v13.8.9 front matter §3–§5 (continuous sequence, lettered sets) and PF06 §0.1A; decision D8. Is concurrent numbering still possible? Is this a rule change needing a Product Owner ruling (Class A)?
- MB-011: PE's authoring requirements, result vocabularies and publication passages: quote each passage that names GCFPE-20260914.1, GCFPE-20260913.1, 091426.1 or 091326.2 and say whether it gives current instruction or historical record.
- MB-012: read the Glow Operations Hub (https://app.notion.com/p/3ce4590a05eb814f8892f88ff8539308; large page: read by search/slice). Locate the four sections headed "Current GCFPE … — 091426.1", the three lines calling 091426.1 the candidate, the dated note under "Current selection", and the "Current GCFPE PF10 reference boundary" paragraph under "Mandatory PR and PF-document authority boundaries — Product Owner, 2026-09-05". Quote each. Since PF10 v13.8.9 has no addenda, check also whether the Hub cites PF10 addenda by number as current (e.g. 2.1) — that would be newly stale. Note SCOPE-002: a surface serving two releases is labelled, not rewritten.
- For each, give the targets (PE is a control page, not a member: no graph part; the Hub is a Notion control/operational page) and whether control_check.py applies (find it: it was used by MODIFICATION-20261011-gcfpe-mb008-to-promotion; search docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/).` },
  { id: 'V5b', items: ['MB-004', 'MB-005', 'MB-006', 'MB-025', 'MB-028', 'MB-029'], brief: `
CLUSTER V5b — repository controls, the provenance clause, and two Product Owner requests.
- MB-004: docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.0.0-20260923.md line 37 and its pointer to docs/ephemeral/modifications/evidence/e3/E3-E4-report.md. Is there a later version of this procedure? Does any live prompt body, skill or control still cite this procedure as operative (search the repository and the registry; establish the consumer before calling it a defect — NORM-001)? Is it a dated record (AUTH-001)?
- MB-005: glow-merged-change-attribution-lock: confirm the installed tree's file count, freeze digest and advertised revision. Search the repository for any record binding a digest of this skill to a review verdict (grep for c518ccb0 and ee253cfa). Check the installed flowmaster-validate (3.4.1) GCFPE profile for whether it requires this skill as a sibling (search its scripts and references). Is the 11-file archive available anywhere in this environment?
- MB-006: docs/prompt_ecosystem_management/reviewer-prompt-template.md, second template ("ANALYZE and PLAN review brief"), §1 and fixed §6. Read .claude/hooks/check_canon_relied_on.py (what it checks, which paths, advisory or blocking). Note §3, §5 and §6 are fixed text "not the author's to widen or tighten": what authority changes fixed text in a governed template (a PR to a BINDING control; Class A or C)?
- MB-025: list docs/changes/ on main. Read the shared section "Native identity, source fidelity, and recovery" in two or three 100926.1 bodies and quote the provenance clause exactly. Read AGENTS.md's sentence on "the deferred repository prompt-use provenance helper". (A corpus-wide count of the clause is run separately by sweepers.) Is this a Product Owner decision (install or remove)? Note docs/changes/ is outside the writable set of glow-write-boundary.
- MB-028: the request "version bumping without sibling creation" for TW and other non-GCFPE ecosystems. Read docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md and gtwpe.handoffs.md: has GTWPE already adopted a register-membership rule like D23-G? Read PE Metaprompt 100926.1's general version and sibling rules (https://app.notion.com/p/3f44590a05eb81f98b76c83465dc1960). Is any TW or other ecosystem Modification running now? Is this measurable now or sequential (does it wait for a TW Modification)?
- MB-029: the request "safe relay scoring as a reusable skill". Read the installed typesafe-scoring and session-relay-flowmaster skills' SKILL.md, and permanent canon for the drained 2.1 (ledger row A01: PF04 v2.8.8 §9.1.3, §9.1.6). Does anything give a relay-safety score today? Is this a new capability needing the Product Owner's decision before it can be scoped (unmeasured scope)?
- Additionally (completeness): search docs/ephemeral/ files changed since 2026-10-24 (git log --since=2026-10-24 --name-only -- docs/ephemeral) for prompt or skill defects explicitly routed to GCFPE-MGMT-10 or "GCFPE feedback" that are NOT one of MB-001..MB-030. Report each as adjacent_scope with its path and quote.` },
]

const SWEEP_SCHEMA = {
  type: 'object',
  properties: {
    lane_id: { type: 'string' },
    prompt_ids_surveyed: { type: 'array', items: { type: 'string' } },
    coverage: { type: 'array', items: { type: 'object', properties: { prompt_id: { type: 'string' }, method: { type: 'string', enum: ['FILE', 'INLINE', 'FAILED'] }, note: { type: 'string' }, counts: { type: 'object', properties: { F1: { type: 'integer' }, F2: { type: 'integer' }, F3: { type: 'integer' }, F4: { type: 'integer' }, F5: { type: 'integer' }, F6: { type: 'integer' }, F7: { type: 'integer' }, F8: { type: 'integer' }, F9: { type: 'integer' } }, required: ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9'] } }, required: ['prompt_id', 'method', 'note', 'counts'] } },
    hits: { type: 'array', items: { type: 'object', properties: { prompt_id: { type: 'string' }, family: { type: 'string' }, heading: { type: 'string' }, line: { type: 'string' } }, required: ['prompt_id', 'family', 'heading', 'line'] } },
    uncovered_lines: { type: 'array', items: { type: 'object', properties: { prompt_id: { type: 'string' }, line: { type: 'string' }, why: { type: 'string' } }, required: ['prompt_id', 'line', 'why'] } },
    fetch_failures: { type: 'array', items: { type: 'string' } },
    transient_files: { type: 'array', items: { type: 'string' } },
  },
  required: ['lane_id', 'prompt_ids_surveyed', 'coverage', 'hits', 'uncovered_lines', 'fetch_failures', 'transient_files'],
}

const FAMILIES = `
FAMILIES — apply every family to every line of every body, case-insensitive (Python re.I). A line may hit several families; record it once per family.
F1 handoff package (MB-010): input package|native input package|handoff package|handoffs? carr(y|ies)|complete [^.\\n]{0,40}package
F2 provenance clause (MB-025): provenance|GCFPE_PROMPT_PROVENANCE|docs/changes
F3 Codex / security review (MB-024): codex|security[ -]reviews?
F4 PF10 addendum numbering (MB-007, MB-009): allocat|addendum number|next (continuous )?number|numbering|numbers? (the|an|its|each) addend
F5 predecessor release ids (MB-011): 20260914|20260913|091426|091326
F6 commit-authorization default (MB-022): explicitly authori[sz]ed|commit (grant|scope|authori)|uncommitted|scratch (clone|storage|director)|evidence commit
F7 finding, real-input and business-case vocabulary (MB-013 to MB-019, MB-023): business case|real[- ]inputs?|constructed input|cost ceiling|\\bceiling\\b|\\bP1\\b|emulat|fidelity|repeated[- ]class|same class
F8 numbered PF10 addendum citation (adjacent: PF10 v13.8.9 has no addenda): addend(um|a)\\s+2\\.\\d+|PF10[^.\\n]{0,60}\\b2\\.\\d+\\b
F9 closure / close pack (MB-027, MB-030): close[- ]pack|close mutation|CL-05|close[- ]candidate|DO_NOT_CLOSE|close[- ]run
`

const LANES = [
  { id: 'LA', keys: ['CF-C-10', 'CF-C-20', 'CF-C-30', 'CF-C-40', 'CF-E-10', 'CF-E-20', 'CF-E-30', 'CF-E-40', 'CF-PO-10', 'CL-20', 'CL-30', 'CL-40', 'CL-C-10', 'CL-E-10', 'CL-E-20', 'CL-E-30', 'CL-E-40', 'DOC-10', 'DOC-20'] },
  { id: 'LB', keys: ['ESC-10', 'ESC-25', 'ESC-30', 'ESC-40', 'GCFPE-MGMT-10', 'IA-10', 'IA-20', 'IA-30', 'IA-40', 'IA-50', 'IA-60', 'MGR-10', 'OPS-10', 'OPS-20', 'OPS-30', 'RS-10', 'RS-20', 'RS-30', 'RS-40', 'UTIL-10', 'PE-METAPROMPT'] },
  { id: 'LC', keys: ['PR-10', 'PR-20', 'PR-30', 'PR-35', 'PR-40', 'PR-50', 'QA-10', 'QA-100', 'QA-110', 'QA-120', 'QA-20', 'QA-50', 'QA-60', 'QA-70', 'QA-80', 'QA-90'] },
]

const sweepPrompt = (lane) => `${COMMON}
YOUR TASK — SWEEP LANE ${lane.id}. You classify nothing; you measure. Coverage must be arithmetic.
Bodies assigned (exactly these, no more, no fewer): ${lane.keys.join(', ')}. URLs are in ${S}/members.tsv (column 2); PE-METAPROMPT is https://app.notion.com/p/3f44590a05eb81f98b76c83465dc1960.
For each body: fetch it once with the Notion fetch tool. Use only the text inside <content>…</content>.
- If the harness saved the result to a file (method FILE): extract the content programmatically with python3 -I (json.load the file, take ['text'], slice between '<content>' and '</content>') into a transient file in ${S}/out/tmp-${lane.id}/ and apply the families with a python3 -I script using re.I, line by line, tracking the nearest preceding Markdown heading line (starting with #). Delete the transient files when the lane is done.
- If the result came back inline (method INLINE): apply the families by reading, line by line, and copy each matched line exactly as fetched.
${FAMILIES}
Return per body the count of matching lines per family (0 when none), and every hit: prompt_id, family, nearest heading, and the full matched line verbatim (if a line is longer than 600 characters, give the 600 characters centred on the match and mark the cut with … at the cut ends).
Escape hatch: if you see an in-scope line that none of the families catches but that plainly states the same behaviour as a family (for example a handoff-content list worded differently from F1, or a commit default worded differently from F6), add it to uncovered_lines with why.
Also write your complete JSON return to ${S}/out/sweep-${lane.id}.json (this is a findings file, not a body copy).
`

const verifyPrompt = (c) => `${COMMON}
YOUR TASK — ${c.id}. Items assigned (items_surveyed must equal exactly): ${c.items.join(', ')}.
Read each assigned entry file first: ${c.items.map(i => `${S}/backlog/${i}.md`).join(', ')}.
${c.brief}
Return one items[] entry per assigned MB id. Also write your complete JSON return to ${S}/out/verify-${c.id}.json.
`

phase('Verify')
const verifyRuns = CLUSTERS.map(c => () => agent(verifyPrompt(c), { label: `verify:${c.id}`, phase: 'Verify', schema: VERIFY_SCHEMA }))
const sweepRuns = LANES.map(l => () => agent(sweepPrompt(l), { label: `sweep:${l.id}`, phase: 'Sweep', schema: SWEEP_SCHEMA }))
const all = await parallel([...verifyRuns, ...sweepRuns])
const verify = all.slice(0, CLUSTERS.length)
const sweep = all.slice(CLUSTERS.length)
const missing = []
CLUSTERS.forEach((c, i) => { if (!verify[i]) missing.push(c.id) })
LANES.forEach((l, i) => { if (!sweep[i]) missing.push(l.id) })
if (missing.length) log(`agents with no return: ${missing.join(', ')}`)
return {
  verify_summary: verify.map((v, i) => v ? { cluster: v.cluster_id, assigned: CLUSTERS[i].items, surveyed: v.items_surveyed, items: v.items.map(x => ({ mb: x.mb_id, present: x.still_present, effect: x.effect, cls: x.class_proposal.slice(0, 80) })), adjacent: v.adjacent_scope.length, not_checked: v.not_checked.length } : { cluster: CLUSTERS[i].id, failed: true }),
  sweep_summary: sweep.map((s, i) => s ? { lane: s.lane_id, assigned: LANES[i].keys.length, surveyed: s.prompt_ids_surveyed.length, hits: s.hits.length, failures: s.fetch_failures, uncovered: s.uncovered_lines.length } : { lane: LANES[i].id, failed: true }),
  missing,
}
```
