---
artifact_type: HANDOFF
artifact_id: HDE-EPIC040-PR06a-PR10-HANDOFF
artifact_version: "1.0"
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06a
finding_ref: HDE-EPIC040-PR07-F01
decision_ref: HDE-EPIC040-PR07-F01-RESCOPE-DECISION v1.0
receiver_prompt: PR-10 — Create PR Work-Unit Instructions — 091426.1
receiver_prompt_url: https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d?pvs=204
receiver: the retained whole-change HDE-EPIC040 Implementation Architect
created_at_utc: 2026-09-26T02:55:39Z
---

# HDE-EPIC040-PR06a — PR-10 Handoff v1.0

Paste the block below into the **retained whole-change HDE-EPIC040 Implementation Architect** session. It is complete and needs no editing.

```text
NEXT_PROMPT_HANDOFF

Run PR-10 — Create PR Work-Unit Instructions — 091426.1
https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d?pvs=204

=== RECEIVING ROLE AND SESSION ===
Actor: the retained whole-change HDE-EPIC040 Implementation Architect — the same session that
wrote the PR01-PR06 instructions and raised the PR07 scope analysis this decision answers.
session_disposition: RETAIN_EXISTING; the operator selects it. Do not create, restart or replace a
session and do not invent a platform session ID. invocation_binding: HDE-EPIC040 /
HDE-EPIC040-PR06a / PR-10. context_conflict: NONE established.
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION. AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS.
Selected release: GCFPE-20260914.1 / 091426.1 / 55, per the release register.

=== WHAT WAS DECIDED ===
Your PR07 scope analysis asked two questions. Both are answered.
1. Option: OPTION 1. A bounded code unit, HDE-EPIC040-PR06a, is added between PR06 and PR07.
   PR07 stays documentation-only exactly as Plan v2.1 §6.7 defines it. Decided by Isis-50 on the
   Product Owner's delegation, 2026-09-26T02:55:39Z.
2. F05 identity set: NEITHER of the two you offered. Nathan / Product Owner decided the public
   Reader exposes the FULL MAGIC-10 SET ("we don't want to just emit harmony"; "we need full magic
   10"). Current canon already prescribes how: PF04 §15.2 OI-001 requires a versioned reader.v2
   carrying all ten categories in canonical order, and Reader v1 kept unchanged. So full Magic-10
   ships as Reader v2 (v=2); Reader v1 stays harmony-only and its schema is corrected to that
   unchanged covenant. The four *_leader identities are the retired scorer's; they leave the
   published contract.
This reverses the approved Specification v1.1 exclusion "No public ten-category expansion" (line
265). That supersession is the Product Owner's decision, recorded as such; the numeric-result
exclusion stands.

=== AUTHORITY YOU ARE ACTING UNDER ===
Decision: docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md
Overlay:  docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md
Both are in amthorn78/glow-hdengine-v2, stored through PR #504 on branch claude/nice-mayer-tf9l4c;
read them from main if #504 has merged, otherwise from the branch. Read both completely. The overlay is the operative authority:
it defines PR06a's objective, the five required deliveries, owned loci, proof, exclusions and
completion, adds canon decision C040-07 (NEW_CANON, APPROVED by the Product Owner), and changes the
dependency order to PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR06a → PR07 → OPS01. It is
page-ready under PF10-FORM-001 with its number NOT allocated; drainage into PF10 is Nathan's manual
action and is not a prerequisite for your work.

=== PR06a IN BRIEF — READ THE OVERLAY FOR THE AUTHORITATIVE TEXT ===
1. Reader v2 — new schemas/reader.v2.schema.json; ten {id, band} items in canonical governed order
   from the complete canonical matrix when eligible, [] when ineligible; same six-key numeric-free
   envelope with reader_version "v2"; same preimage recipe, AB/BA and two-run identity; selected by
   v=2 on the production route; existing runtime and single emitter, no new presenter; new goldens
   under goldens/reader/v2/.
2. Reader v1 conformance (F05) — schemas/reader.v1.schema.json admits harmony only, drops prompt,
   enforces six-key closure; goldens/reader/v1/* reconciled through their owner.
3. Production route (F03) — POST /api/reader for v=1 and v=2 by the mechanism consistent with PF05
   §5.6 and its alias posture; dev GET /reader unchanged and v1; ENDPOINTS_CATALOG rows including
   O-03's POST success row; /api ingress scope confirmed; PR04 plan note O-13 superseded.
4. Dev conjunction evidence (F07) — real admitted identity, no dev stamp; dev-only resolver seam,
   absent by default; generator assertions updated; generator registered in
   _EVIDENCE_GENERATOR_TEST_OWNERS; writer artifacts regenerated through their owner.
5. Release re-cut — schemas/reader.v2.schema.json is the one new release member, so the roster
   becomes 45; ADMITTED_RELEASE_ROSTER, its count invariant and the admitted version (1.2.0)
   change in engine/config/registry_loader.py and nothing else there; admission logic and the
   PF10 §2.12 boundary unchanged; cut through scripts/cut_release_manifest.py; release_id
   recomputed; evidence converged through existing owning writers; strict attestation in CI.
Exclusions include: no Magic-10 math, order or catalog change; no public numeric; no new CLI flag
(CLI dump parity stays a v1 family); no v1 contract change; no change to hde.release_attestation.v1
or PR06R_B_FINAL_PASS; no admission-logic change; no deployment, activation or live vendor/DB
operation; no PF-Canon edit; PR06 not rerun.

=== WHAT IS SETTLED AND MUST NOT BE REOPENED ===
The option, the full-Magic-10 product decision, the Reader v2 mechanism, the F07 identity answer,
and PR07's documentation-only boundary. Do not re-argue options 2 or 3, v1-in-place widening, or
the *_leader identity set; the decision record §6 carries the evidence against each.

=== PRESERVED STATE ===
PR01-PR06 are ACCEPTED_FINAL and are never rerun. PR06 admitted the 44-member release at version
1.1.0, release_id 988ed2a7…; that admission is valid history, superseded as the current release
only by PR06a's re-cut. The immutable Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review
v2.1 are unchanged. The F03, F05 and F07 deferral records at PF10 §§2.16-2.18 remain intact as
decision history; this overlay reassigns their return point from PR07 to PR06a. PR07's PR-10 waits
until PR06a is ACCEPTED_FINAL.

=== PF10 AND CANON ===
Resolve and completely read current controlled PF10 from docs/pfcanon/ yourself. At decision time
it resolved, by its own §6 current-version rule, to docs/pfcanon/PF10-HDE-Build-Notes-v13.3.3.md,
SHA-256 6337d600e8555955f65cb68c0c29c485c6c42acb4c8c56765467b5ab70077b6a, addenda through §2.22;
the older v13.3, v13.3.1 and v13.3.2 files are not read. Read every applicable active overlay by
its repository path — the overlay's front matter lists them — plus PF01 v1.3.7, PF04 v2.8.6, PF05
v2.5.2 and PF12 v2.9.5 for the Reader and release sections the unit touches. Resolve every PF source
only from docs/pfcanon/, which is read-only. Record the versions actually read as provenance.

=== CARRIED REGISTER AND UNRESOLVED ITEMS ===
CANON_CONFLICT_REGISTER C040-01 through C040-06 carried unchanged; C040-07 added (NEW_CANON,
APPROVED by the Product Owner, 2026-09-26: public full Magic-10 via Reader v2; drainage to PF01,
PF04, PF05, PF12 maintainers; consequential PF14 and PF29). Unresolved, all non-gating for PR06a:
the Specification-delta route (CF-E-30) is available to Nathan if he wants the superseded exclusion
recorded in the Specification lineage; C040-07 drainage is pending with its maintainers; no
external consumer of the Reader v1 shape was found in the repository; the exact /api/reader mount
mechanism is yours and PR-20's to choose within PF05 §5.6; PF12 v2.9.5 against the register's
v2.9.6 stays with the PF12 maintainer.

=== CONSTRAINTS ===
Produce the PR06a PR work-unit instruction only. Do not implement, create a product branch or pull
request, request or fabricate a Proceed, rewrite the immutable Plan, restart IA-30 or IA-40, rerun
accepted-final work, edit PF10, allocate a PF10 number, claim canonical adoption, merge, enable
auto-merge, or invoke or route to PR-50. Repository paths outside docs/ephemeral/ and docs/graph/ are
not written; docs/pfcanon/ is read-only. Notion is read-only for this task under
docs/prompt_ecosystem_management/notion-write-boundary.md. Google Drive is not a source, store or
authority.

=== NEXT ACTION AND EXPECTED OUTPUT ===
Re-verify the repository head. Then issue HDE-EPIC040-PR06a-PR-INSTRUCTION v1.0, state
INSTRUCTION_READY, as complete Markdown under docs/ephemeral/, committed and pushed on a working
branch, read back completely and referenced by repository path, with one pull request; Nathan alone
merges. Resolve the overlay's owned loci to exact paths from the delivered tree, carry the five
deliveries, proof, exclusions and completion into the instruction, and name the dedicated PR06a
development session that will run PR-20. Include a paste-ready PR-20 handoff for that session, and
paste it into your reply as well so it does not have to be found. This invocation supplies no
implementation authority, Proceed, merge permission, QA verdict, PF09 movement or closure.
```
