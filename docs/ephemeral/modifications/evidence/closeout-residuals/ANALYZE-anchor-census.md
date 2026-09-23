# ANALYZE anchor census — MODIFICATION-20260923-closeout-residuals

All 55 live `091426.1` bodies and the unpromoted GCFPE-MGMT-10 PROPOSED BODY (page `3e34590a05eb811b93d2da9b4ef8106d`),
each read completely from Notion under `D22` on 2026-09-23 (workflow run `wf_256c17f9-d29`; no body copied,
hashed or stored). The census reports every occurrence of each anchor, by effect, with a context of at most 14
words. It answers the review finding that the first sweep and re-check judged one shared sentence two ways: **each
shared sentence below gets one verdict, which applies to every carrier and overrides any contradicting lane verdict**
in `ANALYZE-body-evidence.md`.

| anchor | the sentence (by effect) | live carriers | verdict, applied to every carrier | reason |
|---|---|---|---|---|
| A1 | usage, task, result, attempt or requirement mappings kept "in … metadata or [the/returned] handoff" | 34: CL-20, CL-30, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-35, PR-40, QA-10, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30 | REAL | offers the handoff as the only copy's home; C-ART: "it never carries the only copy of a fact" |
| A2 | `CANON_CONFLICT_REGISTER` preserved "in the … artifact and handoff" or carried by a package | 34: CF-C-30, CF-E-30, CL-30, CL-C-10, CL-E-10, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, IA-10, IA-20, IA-30, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10, QA-100, QA-110, QA-120, QA-20, QA-50, QA-60, QA-70, QA-80, QA-90, RS-10, RS-20, RS-30 | REAL | the register holds decisions and history; C-HANDOFF: the handoff "does not restate … decisions … that the … files hold" |
| A3 | author-directed text: "Embed only applicable workflow contracts", "reusable prompt policy", "Do not copy those pins into reusable prompt text", "historical example constants into this reusable contract" | 13: CL-20, CL-30, CL-40, CL-C-10, CL-E-10, OPS-10, OPS-20, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10 | REAL | addressed to the prompt's author; an executor authors no prompt text and has been read as embedding contracts in the handoff (OPS-30) |
| A4 | "candidate URL tokens must be replaced", "During local candidate authoring", "This authoring candidate" | 5: CL-20, CL-30, CL-40, CL-C-10, CL-E-10 | REAL | release-phase authoring text in a selected body; CL-40's instance reads as forbidding the list update its step 7 authorizes |
| A5 | "Repository paths outside `docs/ephemeral/` and `docs/graph/` are not written" | 37 | REAL only in GCFPE-MGMT-10, PR-35, RS-40; correct elsewhere | PR-35 and RS-40 push code; GCFPE-MGMT-10 writes `docs/prompt_ecosystem_management/`, the registry and the decision record. PR-30 pushes code and does not carry the sentence |
| A6 | the body calls itself, its role or its session read-only, or says it does not edit, mutate or act on the repository, without excepting its own committed outputs | 13: CL-20, CL-30, CL-40, CL-E-20, DOC-20, ESC-25, GCFPE-MGMT-10, OPS-10, OPS-30, PR-20, PR-40, PR-50, QA-10 | REAL | ruling 2: every prompt commits its output files. Scoped phrases ("read-only checks", "read-only evidence access", "Read-only actors …" as a rule about others) are correct and stay |
| A7 | PR-40 entry described as Nathan's merge assertion or invocation alone, with no `MERGE_OBSERVED` (three shared sentences: *Product Owner merge action*, *Working rules*, and "PR-40 independently verifies the later asserted merge"; plus local lines) | 21: CL-20, CL-30, CL-40, CL-C-10, CL-E-10, CL-E-20, CL-E-30, CL-E-40, DOC-10, DOC-20, ESC-10, ESC-25, ESC-30, ESC-40, OPS-30, PR-10, PR-20, PR-30, PR-40, QA-10, QA-20 | REAL | D23-E and A1-5: PR-40 is entered on `MERGE_OBSERVED`, the assertion only where none was returned, once per merge. The `MERGE_PENDING` conditional block is the fallback and is correct |
| A8 | a `Prompt version:`, `Set:` or `Ecosystem release:` label line anywhere in a body | **0 live**; 2 in the proposed MGMT-10 body (non-blank lines 14 and 15) | — | widening the release-line check to the whole body (ITEM-36) meets no live instance and no false positive |
| A9 | C-LAT's *Decide it during work* block | 10: DOC-10, DOC-20, IA-30, PR-10, PR-20, PR-30, PR-35, PR-40, RS-10, RS-20 | — | exactly the spec v2 placement. PR-30 and PR-35 implement code and keep it; the other 8 are ITEM-37's bodies |

## The proposed MGMT-10 body

Carries A1, A2, A3, A4, A5 and A8. The census also found these internal contradictions an executing agent would hit:

- *`MODE = ANALYZE` › Readiness, decided by predicates and never by a score*: Must not: change anything, propose a plan, decide a policy question — count=2 self-descriptions; occurrence 1/2. Same body commits and pushes its own Modification artifact on the branch (Artifact and source boundaries)
- *`MODE = PLAN`*: Must not: apply anything, add scope not in the analysis — occurrence 2/2 (weaker wording); PLAN still writes, commits, pushes its plan section
- *The spine — true in every mode › The record*: Every invocation reads and writes exactly one Modification — conflicts with ANALYZE 'Must not: change anything' while ANALYZE writes, commits, pushes its section
- *`MODE = EXECUTE`*: genuinely new scope becomes a new Modification — creating a spawned Modification conflicts with 'exactly one Modification' per invocation and EXECUTE's no-scope-expansion rule; writer unstated
- *Result routing*: One result per invocation, returned to Nathan. — only three codes; ANALYZE/PLAN pending-approval return has no result code; one session may also span several modes
- *Artifact and source boundaries*: Every artifact is complete machine-readable Markdown under docs/ephemeral/, committed and pushed — graph parts (docs/graph/) and rule PRs (docs/prompt_ecosystem_management/) are not Markdown under docs/ephemeral/
- *Entry contract*: For ANALYZE: the request, in whatever form it arrives — raw-request ANALYZE has no id, yet 'Find the Modification by its id'; creating the file and branch is not specified
- *The spine — true in every mode › Boundaries*: An open pull request is a complete outcome. — vs ECOSYSTEM_CHANGE_COMPLETE 'applied and verified' and 'part lands whole'; result code for unmerged PR or pending install is unclear
- *`MODE = PLAN`*: package, independent review, Nathan installs, post-install digest comparison — EXECUTE stops at install, so the post-install verification step cannot finish inside EXECUTE
- *Native purpose*: does not execute product Change Flow, implementation, QA, release selection, promotion — PLAN's prompt step moves registry rows of selected release members; the boundary with release selection is unclear
- *The spine — true in every mode › The record*: Each mode writes only its own section. — body does not say which mode or session writes analyze_approved_by/plan_approved_by when modes chain in one session
- *(page preamble, above first ---)*: status: APPROVED_FOR_TESTING / approved_by: Nathan, 2026-09-22 — page carries YAML governance state, but the body says 'A prompt body carries behaviour, never governance state'

## Measured part scopes

- PART-05 (read-only claims and the storage sentence): 15 bodies — CL-20, CL-30, CL-40, CL-E-20, DOC-20, ESC-25, GCFPE-MGMT-10, OPS-10, OPS-30, PR-20, PR-35, PR-40, PR-50, QA-10, RS-40.
- PART-13 (handoff content): 48 bodies — the 46 with REAL routing findings (ITEM-26) and every A1 and A2 carrier (ITEM-27).
- PART-14 (PR-40 entry and results): 21 bodies with A7, plus PR-35 and RS-40 for ITEM-30.
- PART-15 (author-only text): 13 bodies with A3 or A4, plus PR-10 for ITEM-38.
- Live bodies touched by the Modification: 50.
