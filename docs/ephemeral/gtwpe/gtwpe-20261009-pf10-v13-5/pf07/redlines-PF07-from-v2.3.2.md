# T-PF07 — exact redlines from PF07 v2.3.2

Run: `gtwpe-20261009-pf10-v13-5/T-PF07`. Preparation revision: `P1`.
Originating preparer: Codex /root in Nathan-started T-PF07 document session; workspace /workspace/scratch/97597970a19d; no conversation URL or provider session ID is exposed.
Target: `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md` at `e7265a090ad0cc8de5f36de2f19481216aa3d073`; Git blob `023ecf8eb7bdd9e7b1debb275b853b157fb61efb`; raw UTF-8 SHA-256 `c4c2505ef3bda71bd4268b098faa03607aaa84c12f0c1f190f1f4ab82e880c4a`.
Ledger: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md`, pinned commit `f057d124176143b3e02ba7ad599880fd7e9991b1`, task `T-PF07`.
Sources: PF10 v13.5 A01 (227–279), A29 (2844–2955), A30 (2956–3010), A32 (3043–3180), A33 (3181–3238), A34 (3239–3306), A37 (3607–3847), A38 (3848–3926); complete C1 (1–190). All at `e7265a090ad0cc8de5f36de2f19481216aa3d073`.
Prompt: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.
Preparation outcome: `READY` after whole-batch producer validation; save completeness is recorded in the separate proof log.

These are eleven independent original-bound REPLACE operations. Header control fields are reserved for TW-APPLY-10. Payloads are literal: the single LF immediately before a closing fence is presentation only, not part of the payload. All other payload newlines and trailing spaces are exact. Fences are four backticks, longer than any payload fence. Each exact old block occurs once in its authored heading scope and once in the whole original.

## RL-001

Redline number: RL-001
Findings or source items: A29; A30
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **0\. Front Matter**`
Original-bound location: # **0\. Front Matter** > **Change control (titles-only cross-refs)**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Replace the superseded locator-citation rule while preserving scoped override precedence and current repository authority. Source-ledger references: A29; A30.

OLD

````text
* **Supersession rule (PF10 addenda).** Consult the complete latest active PF10 base version, whether it is one unlettered document or a complete verified lettered set, and treat every document in a lettered set as an equally authoritative container of independently scoped addenda. Apply every applicable, active, non-superseded addendum to its own scope. A later document letter supersedes nothing by itself; a higher-numbered addendum controls only overlapping or explicitly superseded scope, and lower-numbered guidance remains authoritative for distinct scope. PF10 governs PF07 only where such an addendum explicitly addresses a PF07-owned topic; when the complete active PF10 version is silent on that topic, PF07 governs. PF07 integrates applicable PF10 guidance and routes **by title only** to single homes (no version numbers). Build Notes reference posture: cite PF10 by **addendum number \+ addendum title**; do not use PF10 version strings, document letters, or PF10 section numbers as durable anchors.  
````

NEW

````text
* **HDE Build Notes authority (titles-only).** Resolve current PF documents from `docs/pfcanon/` on `main`, retaining each document's declared standing. **PF10-HDE-Build-Notes** is the canonical override and amendment mechanism. Consult its complete current logical version, whether one unlettered document or a complete verified lettered set. Each active, non-superseded addendum governs its own stated scope; a higher-numbered addendum controls only overlapping or explicitly superseded scope, and a later document letter alone supersedes nothing. When HDE Build Notes is silent on a PF07-owned topic, PF07 governs. PF07 routes to single homes by title only. Current PF prose names **PF10-HDE-Build-Notes** by title alone, without addendum numbers, headings, section numbers, versions or document letters.  
````

## RL-002

Redline number: RL-002
Findings or source items: A38
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **0\. Front Matter**`
Original-bound location: # **0\. Front Matter** > **Change control (titles-only cross-refs)**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Read the PR actor by function; retain the existing PR and evidence obligations. Source-ledger references: A38.

OLD

````text
* **PR-first via CodEx.** CodEx opens the PR automatically (one PR per epic or slice). Whenever proofs or artifacts change, update in the same PR: Doc-Delta, the human Evidence Index (`docs/evidence/INDEX.json`) and its path-proof (`docs/evidence/INDEX.json.path_proof.txt`), the Evidence Index hash sentinel (`docs/evidence/INDEX.sha256`) and its path-proof (`docs/evidence/INDEX.sha256.path_proof.txt`), and the machine JSONL mirror (`artifacts/evidence_index.jsonl`).  
````

NEW

````text
* **PR-first via the executing agent.** The executing agent opens the PR automatically (one PR per epic or slice). Whenever proofs or artifacts change, update in the same PR: Doc-Delta, the human Evidence Index (`docs/evidence/INDEX.json`) and its path-proof (`docs/evidence/INDEX.json.path_proof.txt`), the Evidence Index hash sentinel (`docs/evidence/INDEX.sha256`) and its path-proof (`docs/evidence/INDEX.sha256.path_proof.txt`), and the machine JSONL mirror (`artifacts/evidence_index.jsonl`).  
````

## RL-003

Redline number: RL-003
Findings or source items: A34; A38
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **0\. Front Matter**`
Original-bound location: # **0\. Front Matter** > **Change control (titles-only cross-refs)**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Remove the blanket physical-executor reading for directed vendor work without authorizing other OPS or any discovery in this document task. Source-ledger references: A34; A38.

OLD

````text
* **PS discovery for discoverable infrastructure facts.** When a PF07-owned fact needed by a plan, implementation guide, QA plan, OPS task, or remediation guide is missing but can be safely discovered by the PO through bounded OPS discovery or a bounded PO-authorized open-rails check, the artifact MUST route the unknown to that discovery work rather than treating the missing fact as automatic deferral. This does not authorize guessing, secret exposure, uncontrolled external action, or agent-performed OPS. If discovery is unsafe, not authorized, requires a decision that cannot be safely staged, or would require inventing facts, record the PF07 gap and stop at the gap.  
````

NEW

````text
* **PS discovery for discoverable infrastructure facts.** When a PF07-owned fact needed by a plan, implementation guide, QA plan, OPS task, or remediation guide is missing but can be safely discovered through bounded Product Owner-authorized OPS discovery or an open-rails check, the artifact MUST route the unknown to that discovery work rather than treating the missing fact as automatic deferral. Execution authority for an identified live vendor task, including execution by the Product Owner's directed agent, is governed by **PF10-HDE-Build-Notes** and the owning governance and QA documents. Other OPS and privileged-action boundaries remain with their owning documents. This does not authorize guessing, secret exposure, or uncontrolled external action. If discovery is unsafe, not authorized, requires a decision that cannot be safely staged, or would require inventing facts, record the PF07 gap and stop at the gap.  
````

## RL-004

Redline number: RL-004
Findings or source items: A38
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **0\. Front Matter**`
Original-bound location: # **0\. Front Matter** > **Change control (titles-only cross-refs)**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Replace the product-named audit role by its read-only repository function, preserving all evidence limits. Source-ledger references: A38.

OLD

````text
* **Codex Audit repo-reality posture.** A supplied Codex Audit may be used as observed repo-reality evidence for existing repo-bound infrastructure loci, such as current config helpers, environment files, evidence helpers, or repo paths. Codex Audit observations do not prove live infrastructure truth, OPS completion, QA PASS, acceptance-token satisfaction, PF09 status, or canon authority. Live facts still require PF07, PO confirmation, OPS discovery, PO-authorized open-rails evidence, or repo validation as applicable.  
````

NEW

````text
* **Read-only repository audit posture.** A supplied read-only repository audit may be used as observed repo-reality evidence for existing repo-bound infrastructure loci, such as current config helpers, environment files, evidence helpers, or repo paths. Audit observations do not prove live infrastructure truth, OPS completion, QA PASS, acceptance-token satisfaction, PF09 status, or canon authority. Live facts still require PF07, PO confirmation, OPS discovery, PO-authorized open-rails evidence, or repo validation as applicable.  
````

## RL-005

Redline number: RL-005
Findings or source items: A33
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# 2\) Environments overview` > `## **2.5 QA windows (names‑only)**`
Original-bound location: # 2\) Environments overview > ## **2.5 QA windows (names‑only)** > **Production-affecting Live QA infrastructure posture (names-only).**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Remove the superseded exemption alternative for production-functional surfaces and route operational proof requirements to their owners. Source-ledger references: A33.

OLD

````text
When an epic affects deployed service behavior, vendor ingest, HumanDesignAPI calls, request shaping, response mapping, database persistence or retrieval, database transport behavior, public or app-facing behavior, CLI/API behavior used in production, or environment-variable or secret-binding behavior, the owning Live QA Plan must include at least one bounded open-rails live QA step or an explicit authorized exemption. PF07 does not define the step, PASS/FAIL predicate, token semantics, or QA procedure.
````

NEW

````text
When an epic affects deployed service behavior, vendor ingest, HumanDesignAPI calls, request shaping, response mapping, database persistence or retrieval, database transport behavior, public or app-facing behavior, CLI/API behavior used in production, or environment-variable or secret-binding behavior, its live-proof requirement is governed by **HDE-Governance** and **Glow QA Guide**. For any surface used to produce a production feature described as functional in PF canon, **PF10-HDE-Build-Notes** governs the mandatory open-rails live vendor test with synthetic data only and its non-substitution rule; an exemption, a closed-rails test, or a non-vendor live step does not replace that scoped requirement. PF07 records the supporting infrastructure facts and does not define the step, PASS/FAIL predicate, token semantics, or QA procedure.
````

## RL-006

Redline number: RL-006
Findings or source items: A34
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# 2\) Environments overview` > `## **2.7 Terminal CLI access as admin surface (names-only, pre-Glow)**`
Original-bound location: # 2\) Environments overview > ## **2.7 Terminal CLI access as admin surface (names-only, pre-Glow)** > **CLI-local vendor smoke target distinction (names-only).**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Conform the named target configuration to the two-key vendor set and canonical-base/absent-canonical alias posture; retain target, rails and environment names. Source-ledger references: A34.

OLD

````text
* For this CLI-local vendor smoke target, the infrastructure target facts are: command target `hdctl showcompat`, data source `--source vendor`, vendor binding key `HD_API_BASE_URL`, deprecated compatibility alias `HDAPI_BASE_URL` only when explicitly allowed by the owning task, vendor credential key `HD_API_KEY`, optional geocoding credential key `GEO_API_KEY` when required by the command path, deterministic capture pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`, open-rails keys `SAFE_MODE=0` and `ALLOW_NETWORK=1` for the vendor step only, and application environment key `APP_ENV=dev`.  
````

NEW

````text
* For this CLI-local vendor smoke target, the infrastructure target facts are: command target `hdctl showcompat`, data source `--source vendor`, vendor binding key `HD_API_BASE_URL`, deprecated compatibility input `HDAPI_BASE_URL` when `HD_API_BASE_URL` is absent, vendor credential keys `HD_API_KEY` and `GEO_API_KEY`, deterministic capture pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`, open-rails keys `SAFE_MODE=0` and `ALLOW_NETWORK=1` for the vendor step only, and application environment key `APP_ENV=dev`.  
````

## RL-007

Redline number: RL-007
Findings or source items: A32 C040-09; A37 DD-02 / C040-09; C1 §5.3
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# 2\) Environments overview` > `## **2.8 GitHub Codespaces / local dev environments (names-only)**`
Original-bound location: # 2\) Environments overview > ## **2.8 GitHub Codespaces / local dev environments (names-only)** > **Live QA is gitless (routing-only).** and **No non-canonical wrappers (routing-only).**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Drain the APPROVED_AS_CHANGED C040-09 correction: attribution-only git reads and approved tracked-harness invocations are distinct from VCS mutation, new evaluators and product/runtime minting. Source-ledger references: A32 C040-09; A37 DD-02 / C040-09; C1 §5.3.

OLD

````text
**Live QA is gitless (routing-only).**  
Live QA runbooks MUST NOT include git operations and MUST NOT gate PASS/FAIL on working-tree cleanliness. Evidence gating is artifact-based under `audit/qa/<epic-id>/...`. The execution rail is governed by title in **Epic-Process-Guide** and **Glow QA Guide**.

**No non-canonical wrappers (routing-only).**  
Live QA Plans, QA reviews, and any QA runbooks MUST NOT invent or mint new repo loci (scripts, modules, checks, test files, endpoints, or commands). Any executable locus MUST be audit-proven to exist as a repo locus or explicitly canon-defined as a fixed entrypoint by explicit path, and QA plans MUST NOT create new scripts at run time; missing tooling is a repo gap to be resolved by PR work rather than QA-time script creation. Where canon requires an artifact surface but does not name a tool, the plan must validate or produce the governed artifact surface directly using baseline commands (see §10.5 “Live QA evidence is mechanical”).
````

NEW

````text
**Live QA source attribution (routing-only).**  
**PF19-Canon-Glow-QA-Guide** governs read-only repository observations, including git reads, for tested-source attribution and the working locus. Such observations and ordinary working-tree cleanliness are not QA PASS/FAIL gates. Repository mutation and publication remain in their separately authorized lanes; PF07 supplies no execution or publication authority.

**Harness requirements (routing-only).**  
**PF19-Canon-Glow-QA-Guide** and **PF27-Canon-Plan-Templates** govern executable entrypoints, approved embedded calls to tracked, reviewed, tested harness APIs, and the boundary excluding newly written decisive evaluators and product/runtime code during QA. An approved embedded call need not create a standalone script. Missing implementation tooling remains a repository gap under the owning QA and implementation routes. PF07 records names and locations and does not define a separate QA execution policy.
````

## RL-008

Redline number: RL-008
Findings or source items: A34
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **8\) Config keys & references (names \+ current values)**` > `  ## **8.2 Component-specific keys**` > `  ### **8.2.1 HD Engine**`
Original-bound location: # **8\) Config keys & references (names \+ current values)** > ## **8.2 Component-specific keys** > ### **8.2.1 HD Engine** > **Vendor-ingest keys (present where noted; secrets redacted)**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: State the environment-held compatibility input's exact condition while preserving canonical-key naming. Source-ledger references: A34.

OLD

````text
* `HDAPI_BASE_URL` — deprecated legacy alias only. It must not be used as the canonical key in plans, implementation prompts, QA plans, OPS tasks, or PF documentation.  
````

NEW

````text
* `HDAPI_BASE_URL` — deprecated legacy alias only. It is the compatibility input when `HD_API_BASE_URL` is absent, not a second canonical key. It must not be used as the canonical key in plans, implementation prompts, QA plans, OPS tasks, or PF documentation.  
````

## RL-009

Redline number: RL-009
Findings or source items: A34
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **8\) Config keys & references (names \+ current values)**` > `  ## **8.2 Component-specific keys**` > `  ### **8.2.1 HD Engine**`
Original-bound location: # **8\) Config keys & references (names \+ current values)** > ## **8.2 Component-specific keys** > ### **8.2.1 HD Engine** > **Vendor-ingest keys (present where noted; secrets redacted)**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Correct the optional-key implication and route environment use and blocker semantics without asserting presence in any console. Source-ledger references: A34.

OLD

````text
* `GEO_API_KEY` — canonical geocoding/vendor-support key when required. It is secret-bearing and belongs to the HD Engine infrastructure boundary.  
````

NEW

````text
* `GEO_API_KEY` — canonical geocoding/vendor-support API key environment variable. Together with `HD_API_KEY`, it is part of the vendor's two-key configuration; the base URL is separate configuration. It is secret-bearing and belongs to the HD Engine infrastructure boundary. Directed use of environment-held configuration, presence-only evidence and missing-configuration classification are governed by **PF10-HDE-Build-Notes** and the owning governance and QA documents.  
````

## RL-010

Redline number: RL-010
Findings or source items: A01; A29
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **9\) Resource catalog (IDs & links)**` > `## **9.3 Repositories (titles-only)**`
Original-bound location: # **9\) Resource catalog (IDs & links)** > ## **9.3 Repositories (titles-only)**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Record the board/pointer and repository source locations with A29's later authority/storage correction; preserve unresolved operating-procedure placement and evidence homes. Source-ledger references: A01; A29.

OLD

````text
* Authoritative slugs & paths: **§5.1 HD Engine repo**, **§5.2 Glow Backend repo**, **§5.3 Glow Frontend repo**.
````

NEW

````text
* Authoritative slugs & paths: **§5.1 HD Engine repo**, **§5.2 Glow Backend repo**, **§5.3 Glow Frontend repo**.

**Documentation and navigation locations (names-only).**

* Current PF source: `amthorn78/glow-hdengine-v2`, `docs/pfcanon/` on `main`; each document retains its declared Canon, Build Notes or Reference standing.
* Change-process documents: `docs/ephemeral/`, referenced by repository path. Persistent prompt-ecosystem management records: `docs/prompt_ecosystem_management/`.
* Operational board: [Glow HD Engine Development Board](https://app.notion.com/p/3d54590a05eb819dacccfcfbfee8666b?pvs=204), under the Glow Operations Hub.
* Historical-source navigation: [PF16 Historical Records](https://app.notion.com/p/3d54590a05eb81a7a56be6b0da418f16?pvs=204), [PF20 Historical Records](https://app.notion.com/p/3d54590a05eb811a8df3fe0e5703c4b0?pvs=204), and [PF30 Historical Records](https://app.notion.com/p/3d54590a05eb8199b80edc967990e3e6?pvs=204). The current PF source home for these pointers is `docs/pfcanon/` on `main`, identified by PF identity and versionless title.

The Notion board and pointers are operational metadata and navigation, not PF authority or independent implementation, QA, acceptance or closure proof. Google Drive and ChatGPT Library are neither PF authority nor change-process document destinations; existing files there retain their historical provenance. Governed evidence keeps its established homes and writers. Operating-procedure placement that remains undecided is not assigned a new home here.
````

## RL-011

Redline number: RL-011
Findings or source items: A30
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# 2\) Environments overview` > `## **2.7 Terminal CLI access as admin surface (names-only, pre-Glow)**`
Original-bound location: # 2\) Environments overview > ## **2.7 Terminal CLI access as admin surface (names-only, pre-Glow)** > **Scope (inventory-only).**
Expected non-overlapping occurrence count: `1`.
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Replace the generic addendum-title locator posture with the Build Notes document title alone. Source-ledger references: A30.

OLD

````text
* an **Admin GUI** (as recorded in PF10 addenda by title), and  
````

NEW

````text
* an **Admin GUI** (as recorded in **PF10-HDE-Build-Notes**), and  
````

END OF REDLINES
