# Independent post-flight brief — MB-008, X13

Committed before either reviewer is spawned (PLAN §5 X13; DN-F option F1). Method and scope are
`docs/prompt_ecosystem_management/postflight-procedure.md`, which binds this brief; PLAN §3 PART-07 adds the
activation and the selected-stage registry values. Two fresh-context reviewer subagents receive the fenced
prompt as their only brief: `REVIEWER-POSTFLIGHT-A` writes `execute/REVIEW-POSTFLIGHT-A.md`,
`REVIEWER-POSTFLIGHT-B` writes `execute/REVIEW-POSTFLIGHT-B.md`, each under this directory.

```plain text
You are <REVIEWER_ID>, running the independent post-flight of the GCFPE-20261009.1 / 100926.1 candidate release
for MODIFICATION-20261011-gcfpe-mb008-to-promotion. You did not author it and you are not its D24 skill reviewer.
You are read-only: you repair nothing, install nothing, merge nothing, promote nothing, and write to Notion nothing.
Each finding returns to its owner. Your verdict decides whether a promotion decision packet may go to Nathan.

=== 1. WHAT GOVERNS YOU ===
Repository /home/user/glow-hdengine-v2, branch claude/mb-008-modification-promotion-fdz2sn (draft PR #605, NOT
MERGED). Read its HEAD. Read AGENTS.md first; it governs. Canon is docs/pfcanon/ on main: search it for the terms
you audit (git grep -n -i -E '<terms>' origin/main -- docs/pfcanon/) and read what governs. Then read, in full:
  docs/prompt_ecosystem_management/postflight-procedure.md — your method, scope, verdict set and corpus rule
  docs/prompt_ecosystem_management/prompt-corpus-policy.md and gcfpe.decision-record.md D22 — prompt bodies
  docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/PLAN-20261011.md — §3, §5, §7, §8, §10
  docs/ephemeral/modifications/MODIFICATION-20261011-gcfpe-mb008-to-promotion.md — §E (what EXECUTE did, X0–X12)
D22 binds the method: no prompt body on disk beyond a transient read for one check, no body hash, no comparison of
a body with a stored copy, no evidence containing body text. If a step here conflicts with that, report it and stop.

=== 2. WHAT YOU AUDIT ===
The release as it stands before promotion:
  - the 55 member pages in Notion: the 54 runtime members (page ids in plan/edits.json, "pages") and the
    GCFPE-MGMT-10 successor 3f74590a05eb81b69bd8c27106f7a59d; and PE Metaprompt 100926.1 3f44590a05eb81f98b76c83465dc1960;
  - the candidate graph parts execute/candidate-graph-parts/ (proof token 55 nodes · 235 edges · 55 state_routes ·
    593,625 bytes · sha256 a58666e5…) and the production parts execute/production-graph-parts/ (593,569 bytes ·
    sha256 43f84f29…);
  - the contracts execute/contracts/ (candidate 90593603…, production cd291f17…);
  - the candidate registry execute/candidate-registry.md (sha256 cb44a371…);
  - the six packages in /tmp/claude-0/-home-user-glow-hdengine-v2/11695baf-e0d2-5d3b-80fc-7c96de66c6a8/scratchpad/review-d24-r2/
    (read-only; copy and extract into your own scratch directory; digests in execute/x10-packages.json);
  - the activation of PLAN §7: plan/activation-ops.json as plan/activation_render.py renders it (§4 below);
  - the selected-stage registry values (plan/registry-header-100926.1.json, stages.selected).

=== 3. METHOD — postflight-procedure.md, in its order ===
  1. Reproduce the frozen identities first: each package's freeze digest (docs/prompt_ecosystem_management/freeze.py,
     rooted at each extracted skill) against execute/x10-packages.json; both graph builds against their proof tokens
     (<extracted glow-graph-contract>/scripts/graph_parts.py build <parts> <out.md>); the contracts' sha256; the
     candidate registry's sha256.
  2. Everything that needs no prompt body: the terminal-branch invariant (D15) on the parts; registry-versus-graph
     drift (plan/registry_assemble.py check --stage candidate --registry execute/candidate-registry.md --audit-root
     <extracted amthor-workspace-governance-audit> --graph-contract <extracted glow-graph-contract> --parts
     execute/candidate-graph-parts); the PF10 producer set; PR-20's declared inputs; the installed gates from the
     extracted packages (validate_flowmaster.py --skills-root <root of the six extracted skills plus flowmaster-primary,
     glow-merged-change-attribution-lock, glow-po-reporting, session-branch-flowmaster, skill-creator, tw-flowmaster
     and typesafe-scoring copied from /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/>).
  3. Then the bodies, lane by lane, so no context holds the corpus. Fetch each member page in your session with the
     Notion fetch tool. Pipe the lane's bodies on stdin as {"PROMPT-ID": "<text>"} to the extracted
     flowmaster-validate's scripts/validate_gcfpe_20261009.py <extracted change-flow> --contract <extracted
     change-flow>/references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json --bodies-stdin, from a pipe or a
     transient file outside the repository that you delete. Run every row's audit_assertions on your own reads with
     plan/registry_assemble.py assertions --registry execute/candidate-registry.md --audit-root <extracted audit>
     --since-minutes 900 --fetched-after <a UTC time, with milliseconds, taken just before your fetches>
     --page GCFPE-MGMT-10=3f74590a05eb81b69bd8c27106f7a59d@2026-10-12T02:24:58.597Z
     --shared MGMT10_URL=https://app.notion.com/p/3f74590a05eb81b69bd8c27106f7a59d --landed
     (it reads this session's fetch records; CLAUDE_CODE_SESSION_ID is set in your environment).
  4. Read the coverage fields — prompt_bodies_validated, prompt_body_checks_not_evaluated — never `ok` alone.
  5. Carry forward findings only: prompt id, verdict, the exact quoted clause, the page timestamp. Never a body.
Audit for what stops the flow (the procedure's list): a handoff naming a receiver that does not exist or naming it
wrongly; an artifact required before anything produces it; a terminal branch that emits a continuation or a
nonterminal one that emits none; two prompts disagreeing about who decides; a route the graph declares that the body
does not carry, or the reverse. Add, for this release: a body or control that contradicts PF10 addendum 2.1 (the
TypeSafe reading; no agent's own model or reasoning advice; surface advice kept, PF04 §9.1.3), D27 (role and artifact
continuity; the QA execution arrangement), PF06 §0.1A (the producer numbers its addendum), or the GCFPE-MGMT-10
successor's three-mode contract. Do not audit wording quality, prose drift, presentation or byte fidelity.

=== 4. THE ACTIVATION, AS EXACT SPECIFIED TEXT (PLAN §3 PART-07, §7) ===
In your session, fetch these nine control pages: PE 3f44590a05eb81f98b76c83465dc1960; Flow Index
3db4590a05eb81de9736ea69bac61016; hubs 3db4590a05eb81d59059eb6b95ed5fcf, 3db4590a05eb8195a2ccf7c0959a8b6e,
3db4590a05eb814d96d3dcfa8835f96d, 3db4590a05eb81cd938de84cfffead9c, 3db4590a05eb811b9c14f2ae89c28df7; Alpha
checklist 3db4590a05eb812f87caed515836687f; register 3d24590a05eb81ce942ad994cfca9fa1. Then run, from the repository root:
  python3 docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/activation_render.py plan
    --parts docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/candidate-graph-parts
    --pages 3f44590a05eb81f98b76c83465dc1960 3db4590a05eb81de9736ea69bac61016 3db4590a05eb81d59059eb6b95ed5fcf
            3db4590a05eb8195a2ccf7c0959a8b6e 3db4590a05eb814d96d3dcfa8835f96d 3db4590a05eb81cd938de84cfffead9c
            3db4590a05eb811b9c14f2ae89c28df7 3db4590a05eb812f87caed515836687f 3d24590a05eb81ce942ad994cfca9fa1
    --fetched-after <your pre-fetch time> --emit
    --set @MGMT10_PAGE_ID=3f74590a05eb81b69bd8c27106f7a59d
    --set "@PRODUCTION_TOKEN=55 nodes · 235 edges · 55 state_routes · 593,569 bytes · sha256 43f84f29…"
    --set @ACTIVATION_DATE=2026-10-13 --set @PROMOTION_APPROVED_AT=2026-10-13 --set @POSTFLIGHT_VERDICT=PASS
    --set @CATALOG_PAGE_ID=00000000000000000000000000000000 --set @REGISTER_ENTRY_PAGE_ID=ffffffffffffffffffffffffffffffff
    --pin 3f44590a05eb81f98b76c83465dc1960=2026-10-12T02:30:10.895Z --pin 3db4590a05eb81d59059eb6b95ed5fcf=2026-10-12T02:29:57.710Z
    --pin 3db4590a05eb8195a2ccf7c0959a8b6e=2026-10-12T02:30:54.130Z --pin 3db4590a05eb814d96d3dcfa8835f96d=2026-10-12T02:30:51.327Z
    --pin 3db4590a05eb81cd938de84cfffead9c=2026-10-12T02:29:51.552Z --pin 3db4590a05eb811b9c14f2ae89c28df7=2026-10-12T02:30:10.895Z
    --pin 3db4590a05eb81de9736ea69bac61016=2026-10-12T02:34:11.699Z
Run it once without --emit (the JSON report; read `ok` and each page's revision_matches_pin, refused, batch_safe,
findings_after), and once with --emit, reading every operation's new text and the two new pages' content in your
terminal. Never redirect --emit output into the repository. The pins for PE and the five hubs are their revisions
read after X6a (execute/x13-pins.json); the Flow Index's is a stand-in, since its X15 pin is read after X15(a); the
Alpha checklist's and the register's come from activation-ops.json. Stand-in values: @ACTIVATION_DATE,
@PROMOTION_APPROVED_AT, @POSTFLIGHT_VERDICT (your own verdict is not yet known), @CATALOG_PAGE_ID and
@REGISTER_ENTRY_PAGE_ID (pages X15 creates). Known values: @MGMT10_PAGE_ID (X1) and @PRODUCTION_TOKEN (X7).
Review each operation's text as what X15 and X16 will write: is any sentence false at some moment of X15–X22 or
after it, does any in-place control still state a release-bound value unstated, does anything change a dated record
or Alpha state, does anything assert what the evidence will not support? Then the selected-stage registry:
  plan/registry_assemble.py build --stage selected --audit-root <extracted audit> --graph-contract <extracted
    glow-graph-contract> --parts execute/candidate-graph-parts --revisions execute/x6-check.json --out <your scratch>/selected.md
    --set @MGMT10_PAGE_ID=3f74590a05eb81b69bd8c27106f7a59d --set @PROMOTION_APPROVED_AT=2026-10-13
    --set @CATALOG_PAGE_ID=00000000000000000000000000000000
  plan/registry_assemble.py check --stage selected --registry <your scratch>/selected.md <same roots> --parts execute/candidate-graph-parts
  plan/registry_assemble.py compare execute/candidate-registry.md <your scratch>/selected.md --audit-root <extracted audit>

=== 5. KNOWN LIMITS, VOLUNTEERED ===
L1. The activation is reviewed as rendered operations on your own reads, not as final bytes (PLAN §10 P-L2): a page
    that moves after your read is refused at X15 by its pin, and a write that diverges is caught by activation_render.py
    check, control_check.py and X18.
L2. control_check.py excuses a retired value with a predecessor marker in the 100 characters before it (P-L9); read
    the rendered text itself.
L3. Some markers are stand-ins (§4); a stand-in value is not a finding.
L4. The six packages are under their own D24 review: round 1 (execute/REVIEW-D24-A.md, -B.md) required a repair of
    the governance audit, now made (execute/d24-repair-redlines.json); round 2 (execute/REVIEW-D24-C.md, -D.md) runs
    beside you and you do not read it. You check that the packages' gates pass and that they fit the release, not
    their code quality.
L5. PE Metaprompt 100926.1 keeps three passages scoped to the 20260914 repair (P-L8), accepted at plan approval.
L6. The other open findings accepted at plan approval are in PLAN §10 and record §P; restating one is not a new finding.

=== 6. THE DELIVERABLE ===
Write your record to docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/<RECORD_FILE>.
First line: the verdict, exactly one of PASS, PASS WITH WARNINGS, FAIL, INDETERMINATE, and the count of mandatory
open findings. A finding is mandatory when it stops the flow, or when the activation as specified would write a
false or unsupported statement or silently breach a Product Owner ruling. For each finding: the prompt or control,
the exact defect, the evidence as a quoted clause, the smallest correction, and whether it stops the flow or merely
offends the record. Then the timestamp baseline: a table of every member's and PE's page_last_edited_at as you read
it. State which checks you ran and which you could not. End with a "Canon relied on" line (AGENTS.md).
Do not edit any other file, commit, push, merge, install, write to Notion, or edit a prompt body or skill.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
