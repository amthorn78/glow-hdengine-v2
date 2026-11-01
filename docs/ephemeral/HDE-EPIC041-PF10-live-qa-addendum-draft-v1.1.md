---
artifact_type: PF10_ADDENDUM_DRAFT
artifact_version: "1.1"
supersedes: "docs/ephemeral/HDE-EPIC041-PF10-live-qa-addendum-draft-v1.0.md (v1.0, never published; preserved unchanged)"
change_from_v1_0: "R-1's deployed-service check now requires the two-person Reader test on two named synthetic stored people (Product Owner, 2026-11-01: \"yes we need 2 synthetic people obviously\"); the Ops task reference moves to OPS01 v1.1; MB-060 is cited"
logical_id: HDE-EPIC041-PF10-LIVE-QA-ADDENDUM-DRAFT
target: "HDE Build Notes, the next addendum after 2.14 (numbered 2.15 on the current base version v14.0.3), plus one Addendum Index line"
publication: "The Product Owner's manual action. Nothing under docs/pfcanon/ is edited by this record."
origin: "Product Owner direction, 2026-11-01, after the HDE-EPIC041 CL-40 successor scan"
recorded: "2026-11-01T19:50Z"
producer: "Isis, continuing Lead Developer for HDE-EPIC041 (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)"
---

# Draft PF10 addendum: Live QA means a live, open-rails test of the product

**How to use this record.**
* The text between the two horizontal rules below is the addendum, ready to paste into HDE Build Notes after addendum 2.14.
* The index line under "Addendum Index line" goes at the end of §1.1.
* Bump the version and effective date as you usually do; HDE Build Notes §3 to §6 govern that.
* The body follows the HDE Build Notes cross-reference rule: PF documents are named by title and section only.

## Addendum Index line

* 2.15 Live QA means a live, open-rails test of the product: every Epic's QA runs the live compat test on synthetic data, only the Product Owner can waive any part of it, and HDE-EPIC041 closed without one

---

## 2.15 Live QA means a live, open-rails test of the product: every Epic's QA runs the live compat test on synthetic data, only the Product Owner can waive any part of it, and HDE-EPIC041 closed without one

Timestamp: 110126 19:50 (UTC). Details:
* **What this records.** The Product Owner's direction of 2026-11-01 that QA without a live test is pointless. It also records that HDE-EPIC041 closed without any live test, and that the existing open-rails rules did not stop this.
* **What this decides.** Rules R-1 to R-6 below. They state what every Epic's Live QA must run, who alone may waive it, what may be called Live QA, and how every stage enforces it.

### Decision and approval status

* **Decision.**
  * On 2026-11-01, the Product Owner said: "this epic also failed to do any live QA".
  * He directed: "I need to make sure AGAIN that is well litigated and enforced. QA is literally pointless without it."
  * He also stated that compat "is literally the most important part of the HDE", and that he is not reopening HDE-EPIC041.
  * On the deployed test, he decided: "yes we need 2 synthetic people obviously".
  * Rules R-1 to R-6 state that direction as canon.
* **Status.** Proposed. The rules take effect as canon when this addendum is published in HDE Build Notes.
* **Relation to other canon.**
  * These documents already require open-rails live proof in some cases:
    * HDE Governance §3.4 ("Production-functional epic live-proof requirement" and "Other production-affecting scope");
    * Change Process Guide §3.5.2.8 ("Live QA via harness (required for epic closeout)");
    * Glow QA Guide §3.5.5 (its "Production-affecting Live QA minimum").
  * Each makes the requirement depend on whether the Epic "touches" or "can affect" a production surface, and leaves that finding to the Specification, the plans and the QA stages.
  * This addendum supersedes that dependency for the scopes R-1 to R-4 address:
    * the minimum live test every Epic runs;
    * who decides that any part of it does not apply;
    * the meaning of "Live QA";
    * stage enforcement.
  * Every other control in those sections still governs:
    * authorization, request limits and synthetic data;
    * redaction, secret scanning and the classification of failures;
    * the rule that Ops evidence stays Ops evidence;
    * the nonclaims of a passing test.

### The failure that prompted it

* **The facts.** HDE-EPIC041, Separation Pass 4, ran its whole QA chain under closed rails on a repository clone. It closed on that basis:
  * **QA-10 readiness** found neither open-rails binding condition met, because no production entry reaches the changed chart entry. It put that finding to no one.
  * **The QA-20 guide and the QA-50 plan** were both titled "Live QA". The plan's target environment read "repository-local closed-rails execution … no deployed, production or vendor target exists for this change". It excluded "any live vendor, production database, deployed-service, HTTP or CLI exercise".
  * **QA-70** approved the plan with "Open rails not required".
  * **QA-100** ran seven checks. Every primary log records `SAFE_MODE=1` and `ALLOW_NETWORK=0`. The evidence branch was named `qa/hde-epic041-live-qa-evidence`.
  * **The QA-120 report** gave verdict `PASS`. It stated that live vendor, production, HTTP and CLI behavior were not exercised.
  * **CL-05 and the CL-E-10 closure decision** accepted that report and closed the Epic.
  * **The Product Owner was never asked** at any stage whether a QA without a live test was acceptable.
* **What the code shows.**
  * The finding that nothing live reaches the change is true: the new chart entry has no production caller.
  * The production compat path is different. The Reader, the compat handler and `hdctl showcompat` resolve charts through the BodyGraph resolver, and that path was never run.
  * So HDE-EPIC041's QA says nothing about whether the product works.
  * In the same period, the compat-determinism generator has exited 2 since HDE-EPIC040 PR-04, when the placeholder `compat_public` was removed. HDE Governance §12.2, D.1 and D.3 list that generator as `GATE:CORE-DET` evidence. Every stage carried it as excluded scope, and none treated it as a gap in compat proof.
* **Why existing canon did not stop it.**
  * The live-proof rules apply only after someone finds that the Epic touches a production surface.
  * An agent made that finding, and agents accepted it at every later stage.
  * The rule that "silence … or closed-rails success is not an exemption" never engaged, because no exemption was sought.
  * The label "Live QA" was not reserved, so a run with no live step carried it to closure.

### R-1 — Every Epic's Live QA runs the live compat test

* **Scope.** Every Epic's QA plan includes, and its QA run executes, the live compat test below. This holds whatever the Epic changed, and whether or not its own surfaces are on a production path.
* **Why.** Compat is the product. A QA verdict that has not seen compat work live says nothing about the product.
* **What the test runs.**
  * **Live vendor compat.** `hdctl showcompat --source vendor` under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, step-local, on synthetic birth data only, at the Epic's QA execution source.
  * **Pairs.** At least two distinct pairs, each run as AB and as BA, and one pair run twice.
  * **Pass predicates:**
    * each output has the canonical result shape and the release identity of the source;
    * AB and BA are byte-identical;
    * the two runs are byte-identical;
    * the Reader bytes stay `{id, band}` only;
    * the two pairs produce different results.
* **The deployed-service check.** A check of the production HD Engine:
  * its `/internal/version` release identity, compared with the release on `main`;
  * the production Reader, for each Reader version, scoring the two synthetic stored people SYN-A and SYN-B in both orders.
  * **Its pass predicates:**
    * each answer is eligible and bands-only;
    * AB and BA are byte-identical.
  * **Reported as findings with the QA result:**
    * a mismatch between the deployed release and `main`;
    * a difference between the deployed bands and the CLI bands for the same birth data.
* **Where an Epic's own surfaces are live.** If its own surfaces are on a production or vendor path, the plan adds at least one open-rails step that exercises those surfaces live. HDE Governance §3.4 already requires this and keeps governing it.
* **What does not satisfy R-1:**
  * closed-rails tests;
  * fixture replay;
  * mocks;
  * static analysis;
  * governed evidence artifacts;
  * review approval;
  * an unrun procedure.
* **The two synthetic stored people.** The deployed Reader scores only people whose charts are stored in the production database. So two synthetic people are kept there as permanent QA fixtures, under fixed UUIDs:
  * SYN-A, `9cff60ae-6eb6-5618-aec5-8acaa4f290d2` (`uuid5(NAMESPACE_URL, "hde-live-qa-synthetic-a")`), born 1990-01-01 at 12:00 in Amsterdam, Netherlands;
  * SYN-B, `57f0c055-ff09-5fdb-aedb-def880437e6f` (`uuid5(NAMESPACE_URL, "hde-live-qa-synthetic-b")`), born 1985-07-15 at 08:30 in London, United Kingdom.
  * They are stored through the engine's own write path, under the Product Owner's write authorization, by the post-closure Ops task HDE-EPIC041-POSTCLOSE-OPS01, Part W.
  * If either is missing when a QA run starts, the deployed check is `TOOLING_BLOCKED` under R-5 until it is stored again.

### R-2 — Only the Product Owner can waive any part of the live test

* **The rule.** Only the Product Owner may decide that R-1, or any part of it, does not apply to an Epic.
* **How a waiver is recorded.** It is written and specific to the change. It quotes the Product Owner's words with their date. It carries the content HDE Governance §3.4 requires of an exemption:
  * the reason;
  * the accepted risk;
  * the substitute proof and why it suffices;
  * the claim withheld;
  * any later live-proof obligation.
* **An agent's finding is a question, not a decision.** An agent may find that an Epic's surfaces are not on a live path, or that the live test cannot be run meaningfully. Either finding is a question for the Product Owner.
  * It is put to him no later than QA-10 readiness, as a named decision.
  * The QA plan is not approval-ready until he answers.
* **Silence.** Silence, reviewer agreement, convenience, closed-rails success or a finding of non-applicability is not a waiver. Without a recorded waiver, R-1 applies in full.

### R-3 — "Live QA" is reserved for QA that ran the live test

* **What may carry the name.** A guide, plan, task set, evidence branch, report or verdict may use "Live QA" only if it covers or records the R-1 live test, or a recorded R-2 waiver.
* **Other QA.** Any other QA is called "closed-rails QA" in its title, branch name and verdict line.
* **The report's first line.** A QA report without the live test says so in its first line: "No live test ran." It names the waiver, or names the missing test.

### R-4 — Every stage checks the live test and blocks without it

* **The live-test line.** Each of these records carries a line "Live test:", with one of `RAN` (and its evidence references), `WAIVED` (and the Product Owner's quoted words and date), or `MISSING`:
  * QA readiness;
  * the QA plan and its review;
  * the QA task set;
  * the QA execution result;
  * the QA evidence review;
  * the final QA report and RCA;
  * the close mutation set result;
  * the closure decision.
* **What `MISSING` does at each stage:**

| Stage | Effect of `MISSING` |
| :- | :- |
| QA readiness | Not `READY_FOR_QA` |
| QA plan | Not approval-ready |
| Plan review | Not approvable |
| Evidence review | Not acceptable |
| Final QA report | No `PASS` verdict |
| Close mutation set | Not close-PR-ready |
| Closure decision | Not `CLOSE` |

* **Who may override.** No agent may override a block. Only the Product Owner may waive under R-2.
* **Change Flow and GCFPE prompts.** Every prompt that produces one of these records applies R-4. Until each prompt is repaired, the agent running it applies R-4 from this addendum.

### R-5 — A live test that cannot run blocks; it does not pass

* **Classification.** A live test that cannot run is classified `TOOLING_BLOCKED` under HDE Governance §3.4. This covers missing credentials, missing target facts, an unavailable vendor and a missing authorization.
* **Effect.** The Epic waits. A blocked live test is never converted into a `PASS`, a waiver or a closure. The Product Owner decides how to proceed.

### R-6 — Execution controls are unchanged

The live test is Ops evidence under HDE Governance §3.4. These controls still apply in full:
* Product Owner authorization, specific to the task, and its delegation to an executor;
* a defined request limit with no load testing;
* step-local rails and synthetic inputs only;
* redaction, secret scanning and quarantine;
* evidence stored secret-free;
* stop checks;
* the classification of failures;
* the nonclaims of a passing test.

### HDE-EPIC041 disposition

* **The closure stands.** HDE-EPIC041 remains `CLOSE` / `CHANGE_CLOSED`, by the Product Owner's decision of 2026-11-01 not to reopen it.
* **What its QA was.** Its QA was closed-rails QA, whatever its records are titled. Its `PASS` verdict establishes no live, vendor, deployed or production behavior, and no later record may cite it as live proof.
* **The separate live compat test.** It is carried by the post-closure Ops task HDE-EPIC041-POSTCLOSE-OPS01, version 1.1: a full compat test under open rails that also stores SYN-A and SYN-B and runs the two-person deployed Reader test. Its result is Ops evidence and does not reopen or re-decide the Epic.

### Known nonconforming items

None is changed by this record. Each needs its owner's action.

* **GCFPE prompts.** None of these requires the R-4 line, or blocks without it:
  * QA-10, QA-20, QA-50, QA-70, QA-90, QA-100, QA-110 and QA-120;
  * CL-05;
  * the Epic and CRD closure-decision prompts.
  * Owner: GCFPE management, on the GCFPE Modification Backlog as MB-060 (S1, proposed; recorded 2026-11-01).
* **The `GATE:CORE-DET` evidence list.** HDE Governance §12.2, D.1 and D.3 name `scripts/make_compat_determinism_artifacts.py`, which cannot run. Owner: the Product Owner, through FND-005: rewrite the script over the supported compat path, or retire it from those lists.
* **SYN-A and SYN-B.**
  * They are not yet stored in production; OPS01 v1.1 Part W stores them.
  * They are registered in the repository's synthetic-identity home (the EPIC011 test-identity record and the engine's synthetic identity map) by the pull request that carries this draft.
* **A guard keyed on the environment label.** The engine refuses production BodyGraph writes by the environment label alone. Every environment shares one database instance (Glow Infrastructure §2.2), so a shell labeled `dev` writes to production. Part W relies on this, under explicit authorization. Owner: the Product Owner.
* **CRDs.** This record does not decide whether a CRD that changes runtime code also runs the R-1 test. Owner: the Product Owner.

### Scope, exclusions and nonclaims

* **Scope:**
  * the minimum live test of every Epic's QA;
  * who may waive it;
  * the meaning of "Live QA";
  * stage enforcement;
  * the disposition of HDE-EPIC041's QA.
* **Excluded:** how the live test is executed (HDE Governance §3.4 governs), and CRDs (see above).
* **Nonclaims.** This record:
  * runs no test;
  * makes no QA verdict, acceptance, Ops, deployment or PF09 movement;
  * reopens no change;
  * drains no canon.

### Dependencies and unresolved obligations

* **Publication.** Publishing this addendum in HDE Build Notes is the Product Owner's action.
* **Drainage into permanent canon** has not been done. Its targets:
  * HDE Governance §3.4, R-1, R-2 and R-5;
  * Change Process Guide §3.5.2.8, R-1 and R-4;
  * Glow QA Guide §3.1.2, §3.4 and §3.5.5, R-1, R-3 and R-4;
  * Plan Templates §1 "Live QA Plan", R-1, R-3 and R-4.
* **Prompt repair.** Repairing the GCFPE prompts listed above belongs to GCFPE management.

### Evidence

* **HDE-EPIC041 records, on main:**
  * the QA-10 readiness record;
  * the QA-20 Live QA Guide;
  * the QA-50 QA Plan, including its target environment and exclusions;
  * the QA-70 review ("Open rails not required");
  * the QA-100 execution results v1.1, with closed-rails `captured_env` in all seven primaries;
  * the QA-120 final QA report ("none was exercised");
  * the CL-E-10 closure decision.
* **The code reading, on main at 5a046cb2:**
  * the production Reader, the compat handler and `hdctl showcompat` call `resolve_compat_chart`;
  * `adapter/chart_orchestration.py::load_chart` has no production caller;
  * `compat_public` was removed by HDE-EPIC040 PR-04 (#467, 2026-09-22), and the generator still looks it up.
  * the production Reader resolves only stored rows in `public.hde_body_graphs_current`, binding a stored chart's label to the UUID requested;
  * the engine's production write refusal for BodyGraph rows is decided from `APP_ENV` (or `ENGINE_ENV`) alone.

---

## Canon relied on

Read on `main` at `5a046cb2`.

* **HDE Build Notes:**
  * front matter and "Precedence, versioning, and scope" §1 to §9;
  * §1 template;
  * §1.1 index;
  * addendum 2.2 (form of a rule addendum);
  * addendum 2.1, D-1 and D-2.
* **HDE Governance:**
  * §3.4 "Open rails (controlled)", in full to "Controlled vendor-backed no-user validation";
  * §12.1, `GATE:CORE-DET`, `GATE:CORE-READER` and `GATE:CORE-MATCH`;
  * §12.2, B.2, D.1 and D.3.
* **Change Process Guide:** §3.5.2.8 "Live QA via harness (required for epic closeout)", in full.
* **Glow QA Guide:** §3.5.5 "PO Live QA sessions (vendor-first rails)", including "Production-affecting Live QA minimum".
* **Glow Infrastructure:** §2.2, §2.5, §2.6 and §2.7.
* **HDE-EPIC041 records, as listed under "Evidence".**
