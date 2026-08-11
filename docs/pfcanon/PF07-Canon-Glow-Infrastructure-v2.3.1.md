# **0\. Front Matter**

**Title:** PF07-Canon-Glow-Infrastructure  
**Version:** v2.3.1  
**Status:** Canon  
**Effective date:** 2026-08-11  
**Last Update Gate:** 0808 refresh 3  
**Invocation tag:** `INV-f2ac55d77ce9aacc`

---

**Intent & scope**

Infra reference and routing.  
A single, canonical infrastructure map for Glow that records **where things live and how to reach them** across providers and environments. PF07 owns:

* Provider, project, service, and repository names.  
    
* Base URLs and ports for hosted services where those are stable infra facts.  
    
* Canonical environment and config key names (for example, `DATABASE_URL`, `HDE_BASE_URL`, `DEV_SAMPLER_URL`).  
    
* Canonical root paths for governed evidence and QA trees (for example, `audit/qa/<epic-id>/...`).

PF07 does **not** define operations policy, runbooks, transport rules, byte contracts, token semantics, or detailed schema fields. Those live in other PF docs. PF07 may pin concrete reference values (hostnames, base URLs, ports, directory roots, key names) where there is no other single home for that information.

**Endpoint Catalog posture (routing note).**  
Reader/Aux success proofs are catalog-driven via the Endpoint Catalog (JSON success). The Catalog is internal-only and env-gated; non-prod entries are unreachable in prod (capture a headers-only env-gate proof). PF07 records **where** the Catalog is hosted (service, base URL, env) and which component owns it. Contract details (routes, shapes, A7 semantics) live in the owning docs below.

**Routing (titles-only)**

PF07 is an infrastructure inventory. Behavioral semantics, contracts, tokens, and procedures are owned by the relevant product’s canonical documents and are referenced by title only. At a minimum, PF07 routes:

* **Rails/transport policy, acceptance tokens, and ops posture** → the relevant product’s **Governance** document (titles-only).  
    
* **Public envelope, request/response shapes, and any success-route catalog** → the relevant product’s **API/contract** document (titles-only).  
    
* **Canonical JSON, pack/manifest, and evidence catalog/indexing rules** → the relevant product’s **Schemas & Artifacts** document (titles-only).  
    
* **Jobs/guards and evidence procedures** → the relevant product’s **Mechanics/operations** guide (titles-only).  
    
* **Process & PR workflow** (PR-first; human index \+ machine mirror updated in the same PR) → **Epic-Process-Guide** (titles-only).

Where a single shared canonical home exists for a given capability across multiple products, PF07 may name that document by title. Where products differ, PF07 records only the infra names/locations and routes semantics to each product’s owning canonical docs.

**Narratives persistence (names \+ locations).**  
PF07 records only DB/schema locations, service names, and any canonical infra keys used for narratives persistence. Field/length constraints and JSON shapes live in **HDE-Schemas & Artifacts**; logging/privacy (keys-only; never log text) lives in **HDE-Governance**; Aux/CLI endpoint bytes live in **HDE-CLI-API-Vendor-Ref**.

**Change control (titles-only cross-refs)**

* **Supersession rule (PF10 addenda).** Consult the complete latest active PF10 base version, whether it is one unlettered document or a complete verified lettered set, and treat every document in a lettered set as an equally authoritative container of independently scoped addenda. Apply every applicable, active, non-superseded addendum to its own scope. A later document letter supersedes nothing by itself; a higher-numbered addendum controls only overlapping or explicitly superseded scope, and lower-numbered guidance remains authoritative for distinct scope. PF10 governs PF07 only where such an addendum explicitly addresses a PF07-owned topic; when the complete active PF10 version is silent on that topic, PF07 governs. PF07 integrates applicable PF10 guidance and routes **by title only** to single homes (no version numbers). Build Notes reference posture: cite PF10 by **addendum number \+ addendum title**; do not use PF10 version strings, document letters, or PF10 section numbers as durable anchors.  
    
* **PR-first via CodEx.** CodEx opens the PR automatically (one PR per epic or slice). Whenever proofs or artifacts change, update in the same PR: Doc-Delta, the human Evidence Index (`docs/evidence/INDEX.json`) and its path-proof (`docs/evidence/INDEX.json.path_proof.txt`), the Evidence Index hash sentinel (`docs/evidence/INDEX.sha256`) and its path-proof (`docs/evidence/INDEX.sha256.path_proof.txt`), and the machine JSONL mirror (`artifacts/evidence_index.jsonl`).  
    
* **Machine mirror hygiene.** The mirror is records-only, canonical JSONL (UTF-8, sorted keys, compact, exactly one trailing `\n`), unknown-keys rejected. Each record includes `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` to a path-proof stored alongside the artifact. Keep 1:1 parity with the human index.  
    
* **Header snapshot normalization (titles-only).** Transport header snapshots store header names in lower-case; values remain verbatim. Normalization rules and CI checks live in **HDE-Schemas & Artifacts**; PF07 records only which components produce these snapshots and where they are stored.  
    
* **Capture environment pins (titles-only).** Snapshot/canonicalization jobs run with `LC_ALL=C`, `LANG=C`, `TZ=UTC` to guarantee deterministic bytes. Enforcement and gates live in **HDE-Build Checklist** and **HDE-Schemas & Artifacts**; PF07 records only which environments/components are expected to use these pins.  
    
* **Production rails and CI-lane boundary (names-only).** The production-like `APP_ENV` aliases are `prod`, `production`, and `live`; for the Production — Railway binding in §2.4, the rail pair is `SAFE_MODE=0` and `ALLOW_NETWORK=1`. The PR-01 committed-closure checks supplied the rail alignment required by environment snapshot v3 but did not satisfy or close the broader PR-03 reusable CI-rails scope. The reusable repo locus is the `rails-policy-gates` workflow job. Guard semantics, gate requirements, acceptance, and PF09 status remain routed to their owning documents by title.  
    
* **PF07 as the required infrastructure source for plans and ops-task descriptions.** For planning and documentation posture, PF07 assumes no separate external infra or ops team outside the workspace. Any plan, implementation guide, QA plan, review artifact, remediation guide, or epic document that includes an infra task, ops task, infra-owned value, ops-owned value, environment binding, service binding, URL, port, provider name, project name, service name, repository name, config key, QA root, or start-command dependency MUST treat PF07 as the required source for that concrete infrastructure fact.  
    
* **PF07-derived and PF07-gap postures.** A document that needs a PF07-owned fact MUST either cite the exact PF07 fact directly or identify the exact missing PF07 fact set, mark the affected step or claim as blocked by missing PF07 infrastructure inventory, and record the needed PF07 update as a drain target or doc-delta candidate. Placeholder ownership and guessed values are non-conforming, including “infra to provide,” “ops to confirm,” “infra-owned” without the actual PF07 fact, “ask infra,” “await ops details,” guessed hostnames, guessed ports, guessed URLs, guessed start commands, guessed environment bindings, or treating **TBD** as an executable input.  
    
* **Specificity and review posture.** When PF07 is cited for an infra or ops task, the document MUST name the applicable provider, project, service, repository, base URL or port, database instance or schema, config key, governed evidence root or QA root, and the exact expected value or exact PF07 value source, as relevant. A plan or document that refers to infra or ops work without the concrete PF07-backed value, or without an explicit PF07-gap blocker, is non-conforming and must stop at the gap.  
    
* **PS discovery for discoverable infrastructure facts.** When a PF07-owned fact needed by a plan, implementation guide, QA plan, OPS task, or remediation guide is missing but can be safely discovered by the PO through bounded OPS discovery or a bounded PO-authorized open-rails check, the artifact MUST route the unknown to that discovery work rather than treating the missing fact as automatic deferral. This does not authorize guessing, secret exposure, uncontrolled external action, or agent-performed OPS. If discovery is unsafe, not authorized, requires a decision that cannot be safely staged, or would require inventing facts, record the PF07 gap and stop at the gap.  
    
* **Codex Audit repo-reality posture.** A supplied Codex Audit may be used as observed repo-reality evidence for existing repo-bound infrastructure loci, such as current config helpers, environment files, evidence helpers, or repo paths. Codex Audit observations do not prove live infrastructure truth, OPS completion, QA PASS, acceptance-token satisfaction, PF09 status, or canon authority. Live facts still require PF07, PO confirmation, OPS discovery, PO-authorized open-rails evidence, or repo validation as applicable.  
    
* **Infrastructure examples and executable exactness in review posture.** Infrastructure examples in plans are not required to be paste-ready unless the artifact is explicitly an execution runbook. PF07-owned commands, paths, endpoints, config keys, environment variables, evidence roots, service names, provider names, base URLs, ports, QA roots, evidence paths, manifests, hash files, path-proof files, artifact identities, and environment or rails examples must be judged by source-level identity and infrastructure boundary preservation. Plan approval MUST NOT block on shell syntax, environment-variable command syntax, escaped command examples, helper-code formatting, heredoc form, or pasted command exactness. Escaped display in assistant output, rendered markdown, copied chat text, preview panes, review prose, or other display-layer text is not evidence that the underlying PF07-owned string is invalid. Infrastructure blockers require real rails, secrets, external-action, config, environment-authority, missing-PF07-fact, or source-level infrastructure defects. Command normalization during execution is allowed when the same infrastructure boundaries, authority, rails posture, config identity, and evidence identity are preserved.

**Primary homes referenced in this document (titles-only).**

PF07 routes semantics to each product’s owning canonical documents. The current Glow stack references these primary homes by title (HD Engine plus shared process and evidence homes):

* **PF04 — HDE-Governance**  
    
* **PF05 — HDE-CLI-API-Vendor-Ref**  
    
* **PF02 — HDE Architecture**  
    
* **PF01 — HDE-Math-Spec**  
    
* **PF06 — Epic-Process-Guide**  
    
* **PF12 — HDE-Schemas & Artifacts**

Other Glow products may add additional governance, contract, QA, or schemas documents. PF07 will reference those by title when they exist.

---

# **1\) Purpose & boundaries**

**What this is.**  
The **canonical infrastructure inventory and reference** for Glow. PF07 owns:

* Providers and accounts (Railway, GitHub, Vercel, etc.).  
    
* Projects, services, and deployments for HD Engine, Glow Backend, and Glow Frontend.  
    
* Base URLs and ports for those services in each environment (dev, QA, prod).  
    
* Database instances and schemas (for example, `ample-illumination/production/postgres`, schema `hde`).  
    
* Canonical key names and high-level locations for infra configuration (for example, `DEV_SAMPLER_URL`, `DATABASE_URL`, canonical QA roots such as `audit/qa/<epic-id>/...`).

Where an infra fact must be pinned (like a production base URL or shared DB instance), PF07 is the single home for that reference.

**What this is not.**  
PF07 does **not** define:

* Step-by-step procedures or runbooks.  
    
* Transport headers, response bodies, or HTTP/JSON contracts.  
    
* Acceptance token semantics or QA tokens.  
    
* Detailed schema fields or math.

Those live by title only in the **relevant product’s** canonical documents (governance, contracts, schemas, mechanics, QA, and process), referenced by title only.

For the **HD Engine** surfaces recorded in this document, the currently referenced primary homes include:

* **PF04 — HDE-Governance** (transport/A7, ops policy, acceptance)  
    
* **PF05 — HDE-CLI-API-Vendor-Ref** (public bytes and API contracts)  
    
* **PF12 — HDE-Schemas & Artifacts** (canonical JSON, pack/manifest, machine mirror)  
    
* **PF02 — HDE Architecture** (system design and topology)  
    
* **PF06 — Epic-Process-Guide** (process and change control)

Names and pinned infra reference values in PF07 are authoritative for infrastructure. Semantics, tokens, and procedures are routed by title to their single homes above.

---

# 2\) Environments overview

## 2.1 Environment list

* **Production** (Railway / Vercel)  
* **Staging/QA** (GitHub Codespaces)  
* **Development** (OpenAI Codex)

*Names-only. Replace **TBD** as facts are confirmed. No procedures or policy here.*

---

## 2.2 Environment facts

**Shared database (single instance).** All environments point to the **same database instance** (names-only). **Schemas may differ by application**: the **HD Engine** uses schema **`hde`**; the **Backend** schema may **differ (TBD)**.

### **Documented client access vs service identity (names-only)**

* **Default documented local-style access.** For dev and QA documentation, the default documented client access address is `127.0.0.1`, plus the correct port and endpoint path, for non-prod local or local-style surfaces.  
* **Configuration remains environment-variable driven.** This documentation convention does not replace canonical config keys, infra wiring, or per-environment configuration. Runtime behavior remains environment-agnostic and configuration-driven.  
* **Client access, service identity, and server bind are separate facts.** The documented client access address does not redefine provider, project, service name, canonical infra key name, real deployment identity, or the underlying server bind address. Services may still bind to `0.0.0.0`, `$PORT`, or another infra-owned bind target when that is the correct runtime posture.  
* **Prod and prod-facing surfaces stay explicit.** Production services, and any QA or operator flow that targets a real production service, MUST continue to use the real hosted service URL or other real infrastructure address recorded in PF07. They MUST NOT be rewritten to `127.0.0.1` for stylistic uniformity.  
* **Exceptions must be confirmed, not guessed.** If a specific dev or QA surface cannot be reached at `127.0.0.1` from the intended operator context, PF07 records the explicit non-loopback access route as a named exception only when that route is confirmed. Guessed hostnames, guessed forwarded URLs, and placeholder aliases are non-conforming.  
* **Canonical example host.** For new or revised dev and QA documentation, `127.0.0.1` is the preferred canonical example host. `localhost` is not the preferred default.

### Production

| Component | Provider | Project (name) | Service (name) | Region | Base URL | DB Instance | DB Schema |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Glow Backend | Railway | ample-illumination | glow-backend-v4 | TBD | TBD | ample-illumination/production/postgres | **TBD (backend schema may differ)** |
| HD Engine | Railway | ample-illumination | glow-hdengine-v2 | TBD | [https://glow-hdengine-v2-production.up.railway.app](https://glow-hdengine-v2-production.up.railway.app) | ample-illumination/production/postgres | **hde** |
| Frontend | Vercel | TBD | TBD | — | glowme.io (prod), previews TBD | — | — |

### Staging/QA (GitHub Codespaces)

| Component | Codespace | Base URL / Forwarded Port | Linked Target / DB |
| :---- | :---- | :---- | :---- |
| Frontend | TBD | TBD | Backend target TBD |
| Backend | TBD | TBD | **Shared production DB instance** *(backend schema **TBD**)* |
| HD Engine | TBD | TBD | **Shared production DB instance** *(schema **`hde`**)* |

### Development (OpenAI Codex)

| Component | Workspace | Upstream / DB |
| :---- | :---- | :---- |
| Frontend | TBD | TBD |
| Backend | TBD | **Shared production DB instance** *(backend schema **TBD**)* |
| HD Engine | TBD | **Shared production DB instance** *(schema **`hde`**)* |

*Inventory only. These are **observed names/locations**, not policy; replace **TBD** with facts as they are confirmed.*

## **2.3 Routing (titles-only)**

### **2.3.1 Policy & acceptance**

Rails/transport policy and acceptance are governed in **HDE-Governance** (single-home token roster). PF07 is **names-only** and does **not** enumerate tokens.

### **2.3.2 Success-route discovery & proofs**

Reader (and Aux) success-route proofs are catalog-driven via the Endpoint Catalog (JSON success) defined in HDE-CLI-API-Vendor-Ref. Proofs MUST target a cataloged JSON success route; `/internal/*` routes are excluded.

**Catalog posture.**  
The Catalog is internal-only and env-gated; non-prod entries MUST be unreachable in production. Capture a headers-only env-gate proof showing this behavior. Architecture stays contract-free and routes bytes by title only.

**A7 invariants (routing only).**

A7 invariants for proofs on a cataloged JSON success route are defined by title in **HDE-Governance** and **HDE-CLI-API-Vendor-Ref**. PF07 does not restate header/body bytes, validator rules, or acceptance semantics here; it records only that proofs target a cataloged JSON success route and that evidence is captured/indexed under governed roots.

**Scope note (names-only).** Under **EPIC-010**, **Aux** evidence consists of **two header snapshots only** (Text 200 and Suppressed 200). **Aux HEAD/304** are **out of scope**; **A7 (GET/HEAD/304, Vary, encoding-invariance)** proofs run **only** on a **Catalog JSON success** route (see §4.1 entry for the route name). Bytes live in **HDE-CLI-API-Vendor-Ref**; policy lives in **HDE-Governance**; capture/indexing discipline lives in **HDE-Schemas & Artifacts**.

**Evidence pointers (titles-only).** Keep success-route artifacts indexed in the human Evidence Index and mirrored 1:1 in the machine JSONL mirror (records-only; canonical; single LF; unknown-key rejection; each record carries a proof\_anchor). See HDE-Schemas & Artifacts for mirror ownership and CI hygiene.

### **2.3.3 Ops-only identity**

`/internal/version` is **operator-only** and **not A7-eligible**. Its transport posture (cache behavior, validator/HEAD handling, and conditional semantics) is defined by title in the owning governance/contract documents. PF07 records only the infra fact that this surface is ops-only and where its governed evidence bundle lives (see §10.5).

**Auth posture (non-invention; routing-only).**  
PF canon does not yet canonize `/internal/version` auth posture (public vs operator-network gated vs auth-header required) or the expected failure mode for missing/invalid access. Until canonized, remediation guides and operational tooling MUST NOT state auth requirements as canon, and MUST NOT treat an auth header as required input for plan execution.

If a run uses an auth header (for example, `Authorization: Bearer …`), it is **optional until canonized** and MUST be treated as **Observed Evidence** only. Runbooks/plans that include an auth header MUST state the header’s source as a concrete input (presence-only; never the value) or they risk creating a false “ops gap” blocker.

Any statement about auth posture MUST be explicitly labeled as **Observed Evidence** (non-PF) and MUST be supported by secret-free status-line \+ headers captures for both conditions:

* **No auth header present**, and  
    
* **Auth header present** *(presence-only noted; value redacted)*.

Store the captured evidence in-repo under a lowercase audit path (see the Ops/QA audit roots in §10.5).

---

### **2.3.4 Canonical bytes & evidence**

**HDE-Schemas & Artifacts** owns canonical JSON policy, pack/manifest, and the evidence indices:

* **Same-PR parity.** Human index and machine mirror update **in the same PR** whenever proofs/artifacts change.  
* **Mirror hygiene.** Machine mirror is **records-only**, **canonical JSONL** (UTF-8, sorted keys, compact, **one trailing LF**), **rejects unknown keys**, and each record includes a **`proof_anchor`** to a path-proof stored alongside the artifact.  
  PF07 does **not** pin evidence file paths beyond these index homes.

### **2.3.5 Names-only reminder**

This chapter records **where things live and their names**. It is **inventory, not policy**: no contract bytes, header matrices, or acceptance tables.

### **2.3.6 Narratives persistence (titles-only)**

PF07 is **names-only**. Admin-only narratives persistence **DB/schema locations** are listed here. Field/length constraints live in **HDE-Schemas & Artifacts**; logging/privacy posture (keys-only; never log text) lives in **HDE-Governance**. Endpoint bytes for Aux/CLI live in **HDE-CLI-API-Vendor-Ref**.

### **2.3.7 BodyGraph ingest (names-only; routing only)**

**Posture (titles-only).**  
The HD Engine BodyGraph resolver exposes database and vendor source names. Source-selection, request-path, rails, and persistence behavior are owned by **HDE-CLI-API-Vendor-Ref**, **HDE-Mechanics Guide**, and **HDE-Governance**; PF07 does not specify environment-driven source selection or automatic upsert behavior.

**Keys (names-only).**  
See §8 for inventory of:

* `ENGINE_DATA_MODE`, `ENGINE_REFRESH_POLICY`  
* `BODYGRAPH_TTL_S`, `BODYGRAPH_SWR_S`  
* `VENDOR_RATE_LIMIT`, `CB_FAIL`, `CB_WINDOW_S`, `CB_COOLDOWN_S`  
* vendor `*_API_KEY` names

*Values remain OPEN/TBD here.*

**Proof surface (titles-only).**  
Source-selection snapshots and refresh-policy snapshots are stored under governed `artifacts/**` with path-proofs and are indexed in the **machine JSONL mirror** (records-only; canonical; single LF; unknown-key reject).

## **2.4 Env Deployment Inventory \[Required-Now\]**

**Inventory-only.** This matrix records currently protected HD Engine environment-variable bindings and rails/determinism pins. Transport policy, refusal semantics, requiredness, and acceptance tokens live in **HDE-Governance**, **HDE-Schemas & Artifacts**, **Glow QA Guide**, and related HDE homes by title. PF07 records provider/context, key names, redacted values or value patterns, and known drift only.

**Secret handling.** Raw secrets are not stored here. Secret-bearing values are redacted or recorded as presence only. Non-secret base URLs, hostnames, ports, provider/context names, and redacted database URL forms may be recorded when supplied by PO or repo-proven evidence.

### **Production — Railway**

* `ALLOW_NETWORK=1`  
    
* `APP_ENV=prod`  
    
* `DATABASE_URL=postgresql://postgres:{redacted}@postgres.railway.internal:5432/railway`  
    
* `GEO_API_KEY={redacted}`  
    
* `HD_API_BASE_URL=https://api.humandesignapi.nl/v2`  
    
* `HD_API_KEY={redacted}`  
    
* `LANG=C`  
    
* `LC_ALL=C`  
    
* `SAFE_MODE=0`  
    
* `TZ=UTC`

  ### **Development — OpenAI Codex**

* `ALLOW_NETWORK=0`  
    
* `APP_ENV=dev`  
    
* `DATABASE_URL=postgresql://postgres:{redacted}@postgres.railway.internal:5432/railway`  
    
* `GEO_API_KEY={redacted}`  
    
* `HD_API_BASE_URL=https://api.humandesignapi.nl/v2`  
    
* `HD_API_KEY={redacted}`  
    
* `LANG=C`  
    
* `LC_ALL=C`  
    
* `SAFE_MODE=1`  
    
* `TZ=UTC`  
    
* `PORT=8000`  
    
* `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`

  ### **QA — GitHub Codespaces**

* `ALLOW_NETWORK=0`  
    
* `APP_ENV=dev`  
    
* `DATABASE_URL=postgresql://postgres:REDACTED@metro.proxy.rlwy.net:52353/railway`  
    
* `DB_BRIDGE_URL=https://illustrious-freedom-production.up.railway.app`  
    
* `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`  
    
* `GEO_API_KEY=REDACTED`  
    
* `HD_API_BASE_URL=https://api.humandesignapi.nl/v2`  
    
* `HDAPI_BASE_URL` — deprecated compatibility alias only; not canonical. Do not use as an executable input unless an owning plan records a bounded compatibility posture.  
    
* `HD_API_KEY=REDACTED`  
    
* `LANG=C`  
    
* `LC_ALL=C`  
    
* `TZ=UTC`  
    
* `SAFE_MODE` is listed in OPS-01 documented environment bindings, but the source matrix does not provide a general QA default value. Do not infer a default value in PF07 from an OPS-02 open-rails task.

  ### **Key-spelling and downgrade rules**

* `HD_API_BASE_URL` is the canonical HumanDesignAPI base URL environment variable.  
    
* The configured `HD_API_BASE_URL` may include the vendor API version path, for example `https://api.humandesignapi.nl/v2`.  
    
* Runtime route construction appends version-neutral resource paths to the configured base URL. Runtime route construction behavior is owned by **HDE-CLI-API-Vendor-Ref** and **HDE-Mechanics Guide** by title.  
    
* `HDAPI_BASE_URL` is deprecated legacy drift. It may be recorded only as observed drift or temporary compatibility alias.  
    
* If both `HD_API_BASE_URL` and `HDAPI_BASE_URL` exist and values differ, treat that as configuration ambiguity and fail closed through the owning implementation and policy homes.  
    
* PO-provided deployed environment facts MUST NOT be downgraded to `OPEN/TBD`.  
    
* PF07 does not define secret validation, runtime request behavior, OPS procedures, or QA PASS semantics.

## **2.5 QA windows (names‑only)**

**Policy routing.** This section records only the existence and locations of prod QA windows and their harnesses. Rails semantics, override guards, and acceptance tokens live in HDE‑Governance and Glow QA Guide (titles‑only).

**Production-affecting Live QA infrastructure posture (names-only).**

For production-affecting HD Engine work, PF07 records only the infrastructure facts needed by the owning plan and QA homes: target environment, provider, service, base URL, database target, config-key names, secret-binding names, rails keys, and governed evidence roots.

When an epic affects deployed service behavior, vendor ingest, HumanDesignAPI calls, request shaping, response mapping, database persistence or retrieval, database transport behavior, public or app-facing behavior, CLI/API behavior used in production, or environment-variable or secret-binding behavior, the owning Live QA Plan must include at least one bounded open-rails live QA step or an explicit authorized exemption. PF07 does not define the step, PASS/FAIL predicate, token semantics, or QA procedure.

Live QA may verify deployed environment bindings, secret presence, base URL posture, external service reachability, and header-shape posture in redacted form. Live QA must not record raw secrets, raw database passwords, raw private payloads, or uncontrolled production data. Production, dev, QA, and Codespaces environment distinctions must remain explicit, and Live QA must use the correct environment and rails posture for the behavior being proven.

### **2.5.1 EPIC‑011 prod QA rails‑open window (Codespaces → prod)**

* **Scope (names‑only).** For EPIC‑011, there is a PO‑approved, time‑boxed prod QA window that exercises production endpoints from the staging/QA environment (GitHub Codespaces). This is an admin‑only QA run; it is not general user traffic.  
    
* **Rails posture during the window.**  
    
  * For the HD Engine service in prod, the QA window opens rails to:  
      
    * `SAFE_MODE=0`  
        
    * `ALLOW_NETWORK=1`

    

  * Outside the window, prod rails posture reverts to the defaults in §2.4 and HDE‑Governance.  
      
  * Rails‑open applies only to the QA harness invocation; normal production traffic remains governed by the default prod rails posture.


* **Harness entrypoint (names‑only).**  
    
  * Supported operator harness for the prod QA choreography:  
      
    * `scripts/ops/admin_vendor_qa.py`

    

  * The canonical runbook and command sequencing for this harness live in:  
      
    * `docs/run/RUN_PROD_QA.md` (names‑only here)  
        
    * Glow QA Guide (step‑by‑step QA procedure; titles‑only)


* **Routing (titles‑only).**  
    
  * Rails/override semantics and acceptance tokens → HDE‑Governance.  
      
  * QA choreography, sample runs, and evidence expectations → Glow QA Guide.  
      
  * Endpoint bytes and A7 behavior for the probed routes → HDE‑CLI‑API‑Vendor‑Ref.  
      
  * Evidence artifacts and indices produced by the harness → HDE‑Schemas & Artifacts.

**Acceptance and artifact impact**

* **Acceptance tokens:** None new in PF07; all tokens remain defined in HDE‑Governance.  
    
* **Artifact paths:** Names‑only references to docs/run/RUN\_PROD\_QA.md and scripts/ops/admin\_vendor\_qa.py; governed evidence artifacts remain owned and shaped in PF12 and PF19.

## **2.6 Prod on Railway, QA via Codespaces (names-only)**

**Production definition (HD Engine, names-only).**  
For the HD Engine, “prod” is defined by the **Railway** service and database names already recorded in §2.2 and §4.1:

* Railway project: `ample-illumination`.  
    
* HD Engine service: `glow-hdengine-v2`.  
    
* Base URL: `https://glow-hdengine-v2-production.up.railway.app`.  
    
* Production database instance: `ample-illumination/production/postgres`.  
    
* HD Engine schema: `hde`.

These are the authoritative names for the HD Engine production service and its primary database. Transport policy, A7 behavior, and acceptance tokens remain owned by **HDE-Governance** and **HDE-CLI-API-Vendor-Ref** (titles-only); PF07 is inventory-only.

**Codespaces role (QA console & artifact sink, names-only).**  
GitHub Codespaces for the repository `amthorn78/glow-hdengine-v2` is a **QA console**, not a production environment:

* It clones the HD Engine repo into a hosted devcontainer.  
    
* It can run CLI (`hdctl`) and HTTP (`curl`) tools configured to talk to the Railway HD Engine service and the shared Postgres instance when environment configuration and rails allow it.  
    
* It writes QA artifacts (logs, notes, snapshots) back into the repo under governed paths (for example, `audit/qa/**`, `artifacts/**`, `docs/**`), and serves as the **artifact sink and analysis workspace** for Live QA runs.

Codespaces does **not** host the production HD Engine itself; it is a remote shell talking to the Railway `glow-hdengine-v2` service and `ample-illumination/production/postgres` database. Names and paths for QA harnesses and windows (for example, EPIC-specific QA rails windows) are recorded in §2.5 and **Glow QA Guide** by title.

**Behavior vs artifacts (routing-only).**  
Within this document:

* “Prod” refers to the Railway HD Engine service and shared DB named above, reached via HTTP/admin surfaces defined in other PF documents.  
    
* “Codespaces” is treated as a **console and artifact sink**: a place to store and inspect QA evidence under `audit/qa/<epic-id>/...` and to run offline checks against those artifacts.

PF07 does **not** decide where behavior tests that satisfy D-goals are executed; those decisions (for example, which admin terminal or GUI exercises compat, narratives, vendor, or admin bundle behavior) are specified in **Epic-Process-Guide** and **Glow QA Guide** by title. PF07 names only the providers, projects, services, repositories, and canonical QA evidence roots that those documents rely on.

## **2.7 Terminal CLI access as admin surface (names-only, pre-Glow)**

**Scope (inventory-only).**  
This section records, at the names-only level, that in the **pre-Glow** period the HD Engine exposes two admin-facing product access surfaces:

* an **Admin GUI** (as recorded in PF10 addenda by title), and  
    
* a **terminal CLI** for the HD Engine (for example, `hdctl` as defined in **HDE-CLI-API-Vendor-Ref**).

PF07 does not define CLI flags, bytes, or payloads; it names the surfaces and routes all CLI contracts and behavior to **HDE-CLI-API-Vendor-Ref** and other PF documents by title only.

**Production target (Railway names).**  
Terminal CLI access for the HD Engine is always **aimed at the same production resources** already listed in §2.2:

* Railway project: `ample-illumination`.  
    
* HD Engine service: `glow-hdengine-v2`.  
    
* Base URL: `https://glow-hdengine-v2-production.up.railway.app`.  
    
* Production DB instance: `ample-illumination/production/postgres`.  
    
* HD Engine schema: `hde`.

Any shell that can reach this base URL and/or connect to this DB instance with the correct configuration can act as a console for the canonical HD Engine CLI in pre-Glow. Governance, SAFE rails, and acceptance tokens remain owned by **HDE-Governance**; CLI bytes and subcommands remain owned by **HDE-CLI-API-Vendor-Ref**.

**CLI-local vendor smoke target distinction (names-only).**

* A controlled HD Engine vendor smoke may target the local HD Engine CLI in a PO-controlled execution context rather than a hosted HD Engine HTTP service.  
* For this CLI-local vendor smoke target, the infrastructure target facts are: command target `hdctl showcompat`, data source `--source vendor`, vendor binding key `HD_API_BASE_URL`, deprecated compatibility alias `HDAPI_BASE_URL` only when explicitly allowed by the owning task, vendor credential key `HD_API_KEY`, optional geocoding credential key `GEO_API_KEY` when required by the command path, deterministic capture pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`, open-rails keys `SAFE_MODE=0` and `ALLOW_NETWORK=1` for the vendor step only, and application environment key `APP_ENV=dev`.  
* Presence-only environment captures for this target family may record the following PF07-owned key names without secret values: `ALLOW_NETWORK`, `APP_ENV`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HDE_BASE_URL`, `HD_API_KEY`, `LANG`, `LC_ALL`, `SAFE_MODE`, and `TZ`.  
* `HDE_BASE_URL` is not required for this CLI-local vendor smoke target unless the target changes to an HD Engine HTTP service call.  
* If a task changes from CLI-local vendor execution to an HD Engine HTTP service call, the task must name a PF07-backed hosted-service target fact set before execution.  
* PF07 records only the target names, key names, and target distinction. Command flags, run preflights, outcome classification, and QA or OPS policy are routed by title.

**HDAPI v2 conformance target posture (names-only).**

* HumanDesignAPI v2 request-shaping posture uses canonical `HD_API_BASE_URL` as the version-owning base URL key and version-neutral runtime resource paths such as `charts`, `charts/simple`, and `charts/coordinates`.  
* `HDAPI_BASE_URL` remains deprecated compatibility drift only.  
* HDE-EPIC034 produced bounded open-rails OPS evidence for the v2 `charts/coordinates` family under `audit/ops/hde-epic034/ops-02/`; this is a concrete OPS evidence root, not a remaining PF07 path gap.  
* HDE-EPIC035 retained evidence records two distinct target facts: `bg:resolve --source vendor` was a BodyGraph ingest-path observation that returned `PROVIDER_NOT_FOUND` / 404 under a configured v2 base, while v2 chart/geokey validation used the v2 `charts/simple` route family and recorded success with `Authorization` and `HD-Geocode-Key` present and legacy `HD-Api-Key` absent.  
* HDE-EPIC036 is historical for the route-policy transition: configured v2 bases selected `unsupported_runtime_nonclaim`, non-v2 bases preserved explicit legacy BodyGraph fallback, and dual-route behavior was not implemented.  
* HDE-EPIC037 later records a bounded BodyGraph-detail evidence chain for HDE-FERM008: field sufficiency, pure v2 ChartResult adapter mapping, resolver route policy, compatibility proof, PO-produced runtime smoke evidence, and parent binding.  
* HDE-EPIC037 OPS-01 evidence records v2 `charts` request posture, `ADAPTER_MAPPED`, `ChartResult`, mapped-no-raw-vendor-payload cache posture, accepted compatibility path summary, exit code 0, and explicit safety/nonclaim boundaries.  
* Current PF07 posture remains names-only: PF07 records the target names, key names, roots, and evidence locations. Command behavior, route bytes, adapter semantics, provider behavior, QA predicates, OPS execution rules, token semantics, and PF09 status remain owned by the HDE CLI/API, Mechanics, Governance, QA, Schemas and Artifacts, Epic Process, and Build Checklist homes by title.  
* Plans, implementation guides, QA plans, reviews, and closeout artifacts MUST NOT claim mapped-cache write persistence, production deployment, broad HumanDesignAPI v2 platform conformance, public Reader expansion, public route or payload expansion, app-side HumanDesignAPI ownership, raw secret or raw vendor payload persistence, PF09 status movement, QA PASS, PO closeout, board update, merge action, epic closeout, or AI scope from PF07 inventory text.

**Codespaces as canonical QA console.**

GitHub Codespaces for `amthorn78/glow-hdengine-v2` remains the canonical and preferred shared QA console and artifact workspace, but canonical and preferred do not mean exclusive or mandatory for every epic:

* It clones the HD Engine repo into a hosted devcontainer.  
    
* It runs the canonical CLI and HTTP tools against the Railway HD Engine service and shared DB when environment pins and rails allow it.  
    
* It stores QA artifacts (logs, notes, snapshots) back into the repo under governed paths (`audit/qa/**`, `artifacts/**`, `docs/**`).

In this model, **Codespaces is a client to prod, not prod itself**. The phrase “prod via Codespaces” should be read as “run commands from a Codespace that talk to the Railway HD Engine prod service and DB, and store artifacts in the repo,” consistent with the Production and Staging/QA tables in §2.2.

**Any-shell terminal access (names-only).**  
Pre-Glow, terminal CLI access is **not limited to Codespaces**:

* Any shell (local terminal, CI shell, or other remote environment) that can reach the production Railway base URL and/or connect to `ample-illumination/production/postgres` with the appropriate environment configuration is a valid console for the canonical HD Engine CLI.  
    
* PF07 records this as an **infrastructure fact only**. It does not define when or how such shells may be used; usage, rails posture (for example, SAFE\_MODE and ALLOW\_NETWORK), and QA expectations are governed by **HDE-Governance**, **Glow QA Guide**, **HDE-Mechanics Guide**, and **HDE-Build Checklist** (titles-only).

In other words, **terminal CLI access** is a named, supported admin-facing product surface in the pre-Glow period. PF07 keeps it names-only, tying it to the production Railway HD Engine and shared DB instances; product semantics, payload completeness (BodyGraphs, bands/scores, narratives), and acceptance tokens remain defined in the owning PF documents (by title) rather than here.

## **2.8 GitHub Codespaces / local dev environments (names-only)**

**Scope.**  
This subsection is infrastructure inventory only. PF07 records:

* Codespaces role and boundaries (QA console \+ artifact sink; not prod).  
    
* The canonical QA evidence root pattern used by Live QA: `audit/qa/<epic-id>/...` (paths and per-epic subtrees remain names-only here).  
    
* Canonical infra key names referenced by Codespaces runs (see §8), and canonical repo/devcontainer locations where infra binds those key names (names-only; no secrets).

**Canonical home for Codespaces configuration (routing-only).**  
The **Glow QA Guide** is the single canonical home for Codespaces QA configuration and requirements (titles-only). PF07 does not enumerate the full prerequisites checklist, required secret mappings, or step-by-step runbook content. Any change to Codespaces/devcontainer requirements, required env-var names, or Live QA prerequisites MUST be reflected in the Glow QA Guide in the same change-set that introduces the new requirement.

**Codespaces snapshot posture (routing-only).** The **Glow QA Guide** controls whether a Codespaces snapshot is required for a Live QA plan. **HDE-Schemas & Artifacts** controls any governed snapshot family, filename, schema, and capture rule. PF07 records only the Codespaces environment and the canonical epic QA root pattern.

**Live QA is gitless (routing-only).**  
Live QA runbooks MUST NOT include git operations and MUST NOT gate PASS/FAIL on working-tree cleanliness. Evidence gating is artifact-based under `audit/qa/<epic-id>/...`. The execution rail is governed by title in **Epic-Process-Guide** and **Glow QA Guide**.

**No non-canonical wrappers (routing-only).**  
Live QA Plans, QA reviews, and any QA runbooks MUST NOT invent or mint new repo loci (scripts, modules, checks, test files, endpoints, or commands). Any executable locus MUST be audit-proven to exist as a repo locus or explicitly canon-defined as a fixed entrypoint by explicit path, and QA plans MUST NOT create new scripts at run time; missing tooling is a repo gap to be resolved by PR work rather than QA-time script creation. Where canon requires an artifact surface but does not name a tool, the plan must validate or produce the governed artifact surface directly using baseline commands (see §10.5 “Live QA evidence is mechanical”).

**Where PF07 fits (names-only reminder).**  
PF07 remains the single home for provider/project/service names, stable base URLs, canonical QA root patterns, and infra key names. It routes Codespaces configuration, Live QA runbooks, and acceptance semantics by title to their owning documents.

---

# 3\) Provider inventory (names-only)

## **3.1 Railway**

* **Account / org:** **TBD**  
    
* **Project(s):**  
    
  * **ample-illumination** — *(id: **TBD**)*


* **Services by component:**  
    
  * **HD Engine:** `glow-hdengine-v2`  
      
  * **Glow Backend:** `glow-backend-v4`


* **Regions:** **TBD**  
    
* **Base URLs (names-only):**  
    
  * **HD Engine:** `https://glow-hdengine-v2-production.up.railway.app`  
      
  * **Glow Backend:** **TBD**

*Names-only; no policy, runbooks, or tokens here. Transport/A7 policy is routed by title to the relevant product’s governance and contract documents.*

**Connectivity from Codespaces (names-only).**

* GitHub Codespaces and other external shells that exercise production HD Engine or Backend behavior use these same Railway **project** and **service** names and **base URLs** as their connectivity targets; there are no separate “Codespaces-only” hostnames recorded here.  
    
* Live QA connectivity checks described in **Glow QA Guide** (for example, curl or CLI commands that prove reachability to production HD Engine or Backend services, or to the shared Postgres instance listed in §2.2/§7.1) are expected to rely on the names in this section; authentication, rails posture (SAFE\_MODE/ALLOW\_NETWORK, APP\_ENV, credentials), and acceptance semantics are governed by **HDE-Governance**, **Glow QA Guide**, **HDE-Build Checklist**, and **HDE-Mechanics Guide** (titles-only).

* ## PF07 does **not** define how connectivity tests are run or which D-goals or QA tokens they satisfy; it records only the provider, project, service, base-URL, and instance names that those tests and tokens depend on.

  ## **3.2 Vercel**

* **Team / org:** **TBD**  
    
* **Projects & aliases:**  
    
  * **Glow Frontend:** project **TBD** · production alias `glowme.io` · preview alias pattern **TBD**


* **Domains:** primary `glowme.io`; additional **TBD**  
    
* **Preview policy (names-only):** **TBD**

*Names-only; policy/headers/acceptance routed by title.*

---

## **3.3 GitHub**

* **Organization / user:** `amthorn78` *(for HD Engine repo)*  
    
* **Repositories by component:**  
    
  * **HD Engine:** `amthorn78/glow-hdengine-v2` · default branch `main`  
      
  * **Glow Backend:** `amthorn78/glow-backend-v4` · default branch **TBD**  
      
  * **Glow Frontend:** `amthorn78/glow-frontend-v2` · default branch **TBD**

*Names-only; no paths/tokens. Evidence indexing lives in component specific canonical evidence docs.*

---

# **4\) Component maps**

## **4.1 HD Engine**

* **Hosting:** provider **Railway** · project **ample-illumination** · service **glow-hdengine-v2** · base URL [**https://glow-hdengine-v2-production.up.railway.app**](https://glow-hdengine-v2-production.up.railway.app)  
* **Source:** repository **amthorn78/glow-hdengine-v2** (repo root; no file paths pinned)  
* **Build artifact:** container image (Railway) — **TBD**  
* **Linked database (shared):** instance **ample-illumination/production/postgres** · schema **hde**  
* **Vendor credential boundary (names-only):** `HD_API_BASE_URL`, `HD_API_KEY`, and `GEO_API_KEY` belong to the HD Engine infrastructure boundary. Glow app integration should consume HD Engine outputs through a controlled integration surface and should not require direct HumanDesignAPI credentials. Any future cross-service invocation must preserve secret isolation unless a future ADR or canon update explicitly changes this boundary.  
* **Database binding (names-only):** `DATABASE_URL` → direct PostgreSQL through the Glow-owned psycopg provider (sole active HDE database transport). See §7.0 and §8 Config keys.  
* **Start command (inventory):** see **§10** (canonical Railway command kept verbatim)  
* **External surfaces (titles-only):**  
  * **Endpoint Catalog (JSON success)** — discovery/proofs live in **HDE-CLI-API-Vendor-Ref** (A7 success routes); Catalog is **internal-only** and **env-gated**; capture headers-only **env-gate** proof (routing only).  
  * **Ops identity** — `/internal/version` (ops-only; posture in **HDE-Governance**).  
  * **Catalog JSON success route (names-only):** `GET /reader` (env-gated; currently **dev**; Reader v1 is selected via query parameter `v=1`, with no route-path change). When the Reader blueprint is mounted under an `/api` prefix in a given runtime configuration, `/api/reader` is an alias of the same Reader surface (not a distinct contract and not a separate proof surface). There is no `/api/reader-proof/v1` route and it MUST NOT be referenced. The Endpoint Catalog is **internal-only** and **env-gated**; proofs target the cataloged JSON success route for the configured mount (`/reader`, or `/api/reader` only when that is the configured mount). Bytes live in **HDE-CLI-API-Vendor-Ref**; A7 policy & invariants live in **HDE-Governance**.  
  * Aux narrative surface (names-only): /aux/narrative (served from the same adapter HTTP surface family as Reader).  
  * **Compat HTTP surface (internal/admin; names-only):** `/api/compat/v1` (cataloged as internal/admin and env-gated; contract details live by title in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**).  
  * Dev-only conjunction endpoints (names-only; dev/test/local only):  
    * `/dev/sampler/conjunction (dev-harness surface)`  
    * `/dev/reader/conjunction (dev-harness surface)`  
    * `/dev/writer/conjunction (dev-harness surface; gated via dev admin gate)`  
  * *(If used) Endpoint Catalog host (internal-only):* **TBD** (non-prod unreachable in prod; names-only)

*Names-only; policy/bytes/tokens are routed by title (HDE-Governance / HDE-CLI-API-Vendor-Ref).*

---

## **4.2 Glow Backend**

* **Hosting:** provider **Railway** · project **ample-illumination** · service **glow-backend-v4** · base URL **TBD**  
* **Source:** repository **amthorn78/glow-backend-v4** (repo root; no file paths pinned)  
* **Build artifact:** **TBD**  
* **Linked database (shared):** instance **ample-illumination/production/postgres** · schema **TBD** (backend schema may differ from `hde`)  
* **Linked cache/datastore:** **Redis (Railway)** — instance **TBD** (connected to the backend)  
* **Start command (inventory):** **TBD**. §10 applies only to the HD Engine service.  
* **External surfaces (titles-only):** Backend API surfaces — contract/fields/status/headers live in the owning **Glow Backend API/contract** document (titles-only; doc title TBD). PF07 records names and locations only.

*Names-only; schema/policy/bytes routed by title; no token lists or pinned evidence paths.*

---

## **4.3 Glow Frontend**

* **Hosting:** provider **Vercel** · team **TBD** · project **TBD** · site **glowme.io** · domains: `glowme.io` (production), **previews TBD** (Vercel preview alias pattern)  
* **Source:** repository **amthorn78/glow-frontend-v2** (repo root; no file paths pinned)  
* **Runtime config:** public config key **names TBD** (values **OPEN/TBD**)  
* **Upstream targets:** Backend base URL **TBD** · HD Engine base URL **TBD** (names-only; see **§6 Domains & DNS** and **§4.1**)

*Names-only; routing by title to the owning Frontend governance, contract, and schemas documents (public envelope and request/response shapes; transport policy; canonical JSON and evidence catalog/indexing).*

# **5\) Repositories**

## **5.1 HD Engine repo**

**Repository.**  
`amthorn78/glow-hdengine-v2`

**Primary paths of interest (runtime core).**

* `adapter/`  
    
* `engine/`  
    
* `presenter/`

**CLI entrypoint loci (names-only).**

* `pyproject.toml` — package script entry `hdctl = "engine.cli.main:cli"`  
    
* `scripts/hdctl.py` — launcher path for `hdctl`

**Other infra-relevant repo roots (names-only).**

These top-level roots are part of the HD Engine repo inventory and are infra- and evidence-relevant. PF07 records only their names; behavior, schemas, and acceptance for files under these roots remain owned by their single-home PF documents.

* `docs/` — governed documentation, including evidence material and runbooks referenced elsewhere in this document (for example, `docs/evidence/**`, `docs/run/**`).  
    
* `artifacts/` — governed machine mirror and other generated artifacts (for example, evidence index files and DB snapshots).  
    
* `catalog/` — JSON catalogs (for example, channels, gates, manifests, narratives) consumed by Engine runtime and proofs.  
    
* `scripts/` — operational, QA, and release helpers (referenced by title in epic- and QA-specific sections).  
    
* `tests/` — test suites used by QA and CI (test behavior and acceptance live in other PF docs by title).  
    
* `schemas/` — schema reference material for local tooling (canonical schema ownership remains in **HDE-Schemas & Artifacts**).  
    
* `migrations/` — database migration files for the HD Engine schema (canonical DDL and evidence rules live in **HDE-Schemas & Artifacts**).  
    
* `audit/` — QA and audit logs, including trees rooted at `audit/qa/<epic-id>/...` referenced by title in QA guides.

PF07 records this repo structure as an infra inventory only. Transport behavior, governance, QA policy, schemas, and evidence acceptance are routed by title to their owning PF documents (for example, **HDE-Governance**, **HDE-CLI API Vendor Ref**, **HDE-Schemas & Artifacts**, **Glow QA Guide**, **HDE-Mechanics Guide**).

**Directory naming (repo-wide; names-only).**

All directories in the repository and application codebase MUST use **lowercase ASCII** names. Mixed-case or upper-case directory names are non-conforming and must not be introduced. If mixed-case directories exist, treat them as legacy drift and normalize them to lowercase rather than copying them forward. Uppercase characters in filename segments are allowed and MUST NOT be treated as a lowercase-rule violation. Identifier classes explicitly defined as lowercase-only elsewhere (for example check IDs and test IDs) remain lowercase-only.

This applies to all governed roots listed above (for example, `docs/`, `artifacts/`, `audit/`, `catalog/`, `schemas/`, and per-epic QA trees under `audit/qa/<epic-id>/...`).

---

### **5.1.1 Additional governed paths (EPIC-011; names-only)**

These paths are infra-relevant assets in the HD Engine repo for EPIC-011. Only names are recorded here; behavior, schemas, and acceptance are routed by title.

* `docs/run/PROD_ENDPOINTS.json`  
  Canonical source-of-truth for production endpoint base URLs (names-only; no secrets).  
    
* `docs/run/RUN_PROD_QA.md`  
  Prod QA rails-window runbook for admin QA (Codespaces → prod). Step-by-step choreography and acceptance live in **Glow QA Guide**.  
    
* `scripts/runtime/validate_prod_endpoints.py`  
  Helper that validates `PROD_ENDPOINTS.json` against the deployed production endpoints. Evidence paths and schema are governed in **HDE-Schemas & Artifacts** and **Glow QA Guide**.  
    
* `scripts/ops/admin_vendor_qa.py`  
  Admin vendor QA harness used to execute the prod QA runbook from the staging/QA environment. Behavior, rails policy, and acceptance tokens live in **HDE-Governance** and **Glow QA Guide**.

---

### **5.1.2 Notes (routing only)**

PF07 records these paths as part of the HD Engine repo **inventory**. It does not own their behavior or policy.

On-wire behavior, endpoint contracts, evidence shapes, and acceptance tokens for these assets are owned by:

* **HDE-CLI-API-Vendor-Ref** — endpoint bytes and A7 behavior.  
    
* **HDE-Schemas & Artifacts** — artifact schemas and indexing rules.  
    
* **Glow QA Guide** — QA procedures and sample runs.  
    
* **HDE-Governance** — policy and acceptance tokens.

---

### **5.1.3 Acceptance and artifact impact**

* **Acceptance tokens.**  
  None new in PF07; acceptance remains defined in **HDE-Governance** and is referenced here by title only.  
    
* **Artifact paths.**  
  PF07 names `docs/run/PROD_ENDPOINTS.json`, `docs/run/RUN_PROD_QA.md`, `scripts/runtime/validate_prod_endpoints.py`, and `scripts/ops/admin_vendor_qa.py` as HD Engine repo assets of infrastructure interest; detailed schemas and indexing live in **HDE-Schemas & Artifacts**.

---

### **5.1.4 Service mapping (names-only)**

* **Railway project:** `ample-illumination`  
    
* **Railway service:** `glow-hdengine-v2`

  ### **5.1.5 EPIC-019 D6 vendor Live QA harness (names-only)**

These paths are infra-relevant assets in the HD Engine repo for **EPIC-019 D6**. Only names are recorded here; behavior, schemas, acceptance tokens, and QA procedures are routed by title.

* `scripts/qa/d6_live_vendor_qa.py`  
  Live Vendor QA harness for EPIC-019 D6. This script exercises the HDAPI BodyGraph endpoint over HTTPS and writes governed JSONL logs under the EPIC-scoped QA directory. Rails posture, token semantics (for example, Live Vendor transport and open-rails environment tokens), and failure classification logic are defined by title in **Glow QA Guide**, **HDE-Governance**, and **HDE-Phased Epics**.  
    
* `audit/qa/hde-epic019/d6-vendor-live-qa/`  
  QA evidence root for EPIC-019 D6 Live Vendor QA. Contains JSONL run logs (happy-path and classified failure runs) and a `rails_snapshot.json` capturing the rails pins and PF-Canon references for the D6 harness. Artifact schemas, indexing rules, and Machine Mirror records live in **HDE-Schemas & Artifacts**; QA usage and sample runs live in **Glow QA Guide**.  
    
* `notes/d6_vendor_live_qa_discovery.md`  
  Discovery note for EPIC-019 D6 Live Vendor QA, describing the vendor surfaces, environment keys, and rails choices that led to the D6 harness. This note is part of the governed QA documentation set for EPIC-019; acceptance and discovery token semantics are owned by **Glow QA Guide** and **HDE-Governance**.

PF07 records these paths as part of the HD Engine repo **inventory**. It does not define their on-wire behavior, evidence schemas, or acceptance tokens. Those remain in their single-home PF documents:

* **HDE-CLI-API-Vendor-Ref** — vendor HTTP bytes and request/response shapes.  
    
* **HDE-Schemas & Artifacts** — Evidence Index and Machine Mirror entries for D6 artifacts.  
    
* **Glow QA Guide** — QA procedures, Live Vendor QA choreography, and classification semantics.  
    
* **HDE-Governance** and **HDE-Phased Epics** — token semantics and EPIC-level acceptance.

  ### **5.1.6 EPIC-019 D3 sampler QA harnesses & remedial docs (names-only)**

These paths are infra-relevant assets in the HD Engine repo for **EPIC-019** remedial work on the sampler (Cards C1–C3). Only names are recorded here; behavior, schemas, acceptance tokens, and QA procedures are routed by title.

* `scripts/qa/dev_sampler_healthcheck.py`  
  Dev-only sampler healthcheck harness used to prove that the internal/dev sampler HTTP surface is reachable and behaving as expected under closed rails. Routes, status expectations, and acceptance tokens are governed by title in **Glow QA Guide**, **HDE-Governance**, **HDE-Mechanics Guide**, and **HDE-Phased Epics**.  
    
* `scripts/qa/dev_sampler_live_qa.py`  
  Dev-only sampler Live QA harness for EPIC-019 D3. Exercises `DEV_SAMPLER_URL` and related APP\_ENV permutations under closed rails, writing governed logs under the EPIC019 sampler QA evidence root. Classification semantics and token bindings (for example, ENV rails tokens) are owned by **Glow QA Guide**, **HDE-Governance**, and **HDE-Phased Epics**.  
    
* `audit/qa/hde-epic019/dev_sampler_http/`  
  QA evidence root for EPIC-019 sampler QA (healthcheck and Live QA). Contains governed logs produced by the sampler QA harnesses for D3 under closed rails. Artifact schemas, indexing rules, and Machine Mirror records live in **HDE-Schemas & Artifacts**; QA usage and sample runs live in **Glow QA Guide**.  
    
* `docs/evidence/EPIC019_evidence.md`  
  Evidence overview for EPIC-019, summarizing evidence layers (Index, Mirror, path-proofs, orientation demo) and the D3/D6 QA families, including sampler HTTP QA under `audit/qa/hde-epic019/dev_sampler_http/` and vendor Live QA under `audit/qa/hde-epic019/d6-vendor-live-qa/`. This is a governed evidence doc; semantics and acceptance remain owned by **Glow QA Guide** and **HDE-Governance**.  
    
* `docs/hde_epic019_remediation.md`  
  Remedial rails summary for EPIC-019 Cards C1–C3 (dev Reader helper \+ DEV\_SAMPLER\_URL, D3 dev sampler QA, D6 vendor Live QA). It ties the infra-owned harnesses and QA roots listed here and in §5.1.5 back to the EPIC019 remedial plan; acceptance semantics and rails posture live by title in **HDE-Phased Epics**, **Glow QA Guide**, and **HDE-Governance**.

PF07 records these paths as part of the HD Engine repo **inventory** only. It does not define their on-wire behavior, evidence schemas, or token semantics. Those remain in their single-home PF documents:

* **HDE-CLI-API-Vendor-Ref** — public and admin HTTP/CLI bytes and request/response shapes.  
    
* **HDE-Schemas & Artifacts** — Evidence Index, Machine Mirror entries, and artifact schemas.  
    
* **Glow QA Guide** — QA procedures, rails windows, and behavior vs tooling classification.  
    
* **HDE-Governance** and **HDE-Phased Epics** — acceptance tokens, EPIC-level goals, and remedial rails semantics.  
    
  ---

## **5.2 Glow Backend repo**

* **Repository:** `amthorn78/glow-backend-v4`  
* **Primary service code paths:** **TBD**  
* **Service mapping (names-only):**  
  * **Railway project:** `ample-illumination`

  * ## **Railway service:** `glow-backend-v4`

## **5.3 Glow Frontend repo**

* **Repository:** `amthorn78/glow-frontend-v2`  
* **Primary app code paths:** **TBD**  
* **Service mapping (names-only):**  
  * **Vercel team:** **TBD**  
  * **Vercel project:** **TBD**  
  * **Production domain:** `glowme.io`  
  * **Preview domains:** **TBD**

>   
> **Note:** Runtime endpoints (base URLs), databases, and schemas are recorded in **§4 Component maps** and **§7 Databases & Schemas** to avoid duplication.

# 6\) Domains & DNS (names-only)

## 6.1 Intent & scope (inventory-only)

This section lists **domain names and DNS roles in use across Glow**. It is **names-only** (no policy, no header/TTL/cert bytes). Behavioral semantics are owned by the relevant product-level canonical documents and referenced by title. Evidence indexing and mirror parity are routed via §10.5 **“Evidence & indexing”** (titles-only).

## 6.2 Root domains used by Glow

* **glowme.io** — production apex (hosted and registered at **Vercel**; names-only)

## 6.3 Subdomains by environment & component (names-only)

### 6.3.1 Production

* **Frontend:** `glowme.io` (apex)  
* **Frontend previews:** **TBD** *(Vercel preview alias pattern)*  
* **Backend:** **TBD** *(Railway app domain **or** a `*.glowme.io` subdomain — confirm)*  
* **HD Engine:** served on a **Railway app domain**; see **§4.1 Component maps** for the base URL (names-only; not duplicated here)  
* **Endpoint Catalog host (A7 routing, internal-only):** **TBD** *(cataloged JSON success route lives behind env-gating; not public)*

### **6.3.2 Staging / QA (GitHub Codespaces)**

* **Frontend:** **TBD** *(record a Codespaces forwarded or public URL here only when a confirmed non-loopback exception exists; default documented local-style access uses `127.0.0.1` plus the correct port and endpoint path)*  
* **Backend:** **TBD** *(record a Codespaces forwarded or public URL here only when a confirmed non-loopback exception exists; default documented local-style access uses `127.0.0.1` plus the correct port and endpoint path)*  
* **HD Engine:** **TBD** *(record a Codespaces forwarded or public URL here only when a confirmed non-loopback exception exists; the canonical local-style harness binding for `DEV_SAMPLER_URL` remains `http://127.0.0.1:8000/internal/dev/sampler` in §8.2.1)*

### **6.3.3 Development (CodEx)**

* **Frontend:** **TBD** *(default documented local-style access uses `127.0.0.1` plus the correct port and endpoint path; record a non-loopback exception only when confirmed)*  
* **Backend:** **TBD** *(default documented local-style access uses `127.0.0.1` plus the correct port and endpoint path; record a non-loopback exception only when confirmed)*  
* **HD Engine:** **TBD** *(default documented local-style access uses `127.0.0.1` plus the correct port and endpoint path; the actual local-dev harness binding remains **OPEN/TBD** until confirmed in §8.2.1)*

## **6.4 DNS provider & record types (names-only)**

**Provider:** Vercel DNS (zone: `glowme.io`)

**Record types in use (names-only):**

* A / AAAA  
    
* CNAME *(confirm exact hostnames as we populate)*  
    
* TXT *(verification, if required — OPEN/TBD)*

  ## **6.5 Routing (titles-only)**

* **Transport & A7 policy / acceptance:** owned by the relevant product’s governance and transport policy documents (titles-only).  
    
* **Public envelope & request/response shapes:** owned by the relevant product’s API/contract documents (titles-only).  
    
* **Evidence registry & mirror discipline:** §10.5 “Evidence & indexing” (titles-only; ownership in the canonical Schemas & Artifacts documents).

**Notes (inventory-only).**

* Use **OPEN/TBD** when not confirmed (no guessing).  
    
* PF07 records names only; values, TTLs, cert details, and policy live by title in their single homes.

---

# **7\) Databases & Schemas \[Required-Now\]**

## **7.0 Runtime posture (normative)**

* **Connection precedence (env-aware)**  
    
  * **All environments:** `DATABASE_URL` is the sole HDE database endpoint key; direct PostgreSQL through the Glow-owned psycopg provider is the sole selectable HDE database transport.  
  * **Production-like APP\_ENV aliases:** `prod`, `production`, and `live` remain production-like `APP_ENV` values. They use the same direct-only `DATABASE_URL` posture under the applicable rails and authorization controls.  
  * **Stage/Test & Dev:** use `DATABASE_URL` with direct psycopg only. Missing, invalid, unavailable, or unauthorized direct access returns a typed error without bridge or alternate-provider fallback.  
  * **Retired-key drift:** presence of `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, or `DB_ALLOW_BRIDGE_IN_PROD` is configuration drift. Report key names only; do not print or retain their values.  
  * **Stage APP\_ENV example:** `APP_ENV=stage` is a stage/test value for non-dev typed failure evidence. It is not a production-like alias and must not use production guard posture. Production-like aliases remain `prod`, `production`, and `live`.


* **Selection mechanics (routing-only):** Pre-selection probing and typed-failure behavior are owned by **HDE-Mechanics Guide** and **HDE-Governance**; PF07 records only the `DATABASE_URL` key and the direct psycopg transport name.  
    
* **Runtime search\_path**  
    
  * `hde, public` (unquoted; in this order). Verify at startup (emit a `SHOW search_path` echo in ops logs). Pin at the ROLE level.


* **Least-privilege (names-only)**  
    
  * `HDE_APP_ROLE` (runtime): USAGE on app schema; SELECT on `hde.meta`; SELECT/INSERT/DELETE on `hde.public_results`; no DDL.  
  * `HDE_MIGRATOR_ROLE` (DDL): DDL on app schema; no runtime data access.


* **Evidence (titles-only)**  
  Capture: connection echo; search\_path echo; roles/grants snapshot; canonical DDL dump \+ SHA-256 fingerprint; env-selection proof.  
  Indexing & parity: index records-only in the machine mirror (HDE-Schemas & Artifacts). Update the human Evidence Index and its hash sentinel in the same PR. CI enforcement: 1:1 parity; canonical JSONL (single LF); reject unknown keys; each record includes a `proof_anchor` path-proof.  
    
* **Acceptance (routing only)**  
  Governed in **HDE-Governance §2.0**. PF07 does not enumerate tokens.

## **7.1 Instances**

Production runs on one Postgres instance; staging/dev connect to the same physical instance via direct `DATABASE_URL` only (per §7.0). Future separation of staging/dev DB instances is **OPEN/TBD**; do not assume.

**Environment instances**

* Production (Railway)  
    
  * Database (shared): Postgres — instance `ample-illumination/production/postgres` *(via DB proxy; confirm)* — used by the HD Engine (schema `hde`) and Glow Backend (schema TBD)  
      
  * Engine: Postgres  
      
  * Version floor: ≥ 14


* Staging/QA (GitHub Codespaces)  
    
  * Database (shared): same physical instance as Production — `ample-illumination/production/postgres` *(via DB proxy; confirm)*  
      
  * Engine: Postgres  
      
  * Version floor: ≥ 14


* Development (OpenAI Codex)  
    
  * Database (shared): same physical instance as Production — `ample-illumination/production/postgres` *(via DB proxy; confirm)*  
      
  * Engine: Postgres  
      
  * Version floor: ≥ 14

  ## **7.2 Application schema map (per application)**

Inventory-only. List schema names and key objects per application. No DDL, types, or data/PII. Schema ownership and validation live in HDE-Schemas & Artifacts; governance/retention policy lives in HDE-Governance (titles-only).

### **7.2.1 HD Engine schema — `hde` \[Implemented\]**

* **Tables (names & one-line purpose).**  
    
  * `meta` — singleton engine/provenance row *(read-only at runtime)*  
  * `public_results` — append-only store for public compatibility envelopes \+ minimal metadata  
  * **body\_graphs**: durable BodyGraph rows (vendor, version, input\_fingerprint, payload, created\_at, refreshed\_at, ttl\_at)  
  * **body\_graphs\_current**: view of latest valid per user/vendor


* **Primary/unique keys (names-only).** `meta_pkey`, `public_results_pkey`  
    
* **Partitioning policy (name-only, if used).** **TBD**  
    
* **Roles & grants (names-only).**  
    
  * **HDE\_APP\_ROLE** — `USAGE` on `hde`; `SELECT` on `hde.meta`; `SELECT/INSERT/DELETE` on `hde.public_results`  
  * **HDE\_MIGRATOR\_ROLE** — DDL on `hde` *(no runtime data access)*

  ### **7.2.2 Backend schema — TBD \[Speculative\]**

* **Schema name.** **TBD** *(may differ from `hde`; record once confirmed)*  
    
* **Tables (names & purpose).** **TBD**  
    
* **Primary/unique keys (names-only).** **TBD**  
    
* **Partitioning policy (name-only, if used).** **TBD**  
    
* **Roles & grants (names-only).** **TBD**

**Routing (titles-only).** Schema definitions, canonical DDL, and mirror schema → **HDE-Schemas & Artifacts**. Governance/policy (retention, access, PII handling) → **HDE-Governance**. Evidence capture and indexing → see **§7.3** (single home for artifact titles/paths; same-PR human↔machine mirror parity with path-proofs).

### **7.2.3 Narratives authoring schema (TBD; names-only)**

**Schema name**  
TBD (record once confirmed; authoring plane is DB-backed).

**Tables (names & one-line purpose)**  
• **packs**: narrative pack headers/status  
• **fragments**: narrative rows (by category, band, perspective, slot, slug)  
• **suppression\_rules**: content-level guards  
• **\[palettes\]**: optional later  
• **audit**: editorial audit trail

**Routing (titles-only)**  
Field/length constraints, IDs, and lints live in **HDE-Schemas & Artifacts** and **HDE-Mechanics Guide**. Policy surfaces (Aux/preview) live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**. **PF17** provides narrative posture at names level.

## **7.3 Evidence & indexing (titles-only)**

* **Records-only mirror (HDE-Schemas & Artifacts).** Canonical DDL dump \+ fingerprint; roles/grants snapshot; connection echo, `search_path` echo; optional RW-smoke log when DB is in scope; **env-selection proof** and **env-matrix snapshot/failure envelopes** are indexed there by title.  
* **Same-PR rule.** Update the human Evidence Index, its hash sentinel, and the machine mirror in the same PR; CI enforces 1:1 parity and requires sibling `*.path_proof.txt` artifacts for governed index/mirror files. For the exact canonical filenames, see §10.5 “Indexing discipline (same-PR rule)”.  
* **Routing.** Canonical bytes & mirror schema: **HDE-Schemas & Artifacts**; governance/evidence policy: **HDE-Governance**.

### **7.3.1 DB lifecycle evidence (OPS‑managed; names‑only)**

**Execution model (names‑only).** For EPIC‑011, database lifecycle operations for the HD Engine DB — backup, restore rehearsal, and retention — are executed by OPS via the Railway UI or equivalent provider tooling. There is no dedicated CI job that calls the provider APIs for these tasks; lifecycle work is OPS‑run and promoted into governed artifacts by hand as part of an evidence PR.

**Governed lifecycle artifacts (paths only).**

* `artifacts/db/backup/backup_manifest.json` — describes the most recent Railway backup/snapshot/export (id/timestamp/objects; no raw dump).  
    
* `artifacts/db/backup/restore_verify.log` — summarizes a restore rehearsal (target, time window, smoke checks, status).  
    
* `artifacts/db/retention/retention_run.log` — retention activity summary (policy id and label/count metadata only; no payload/PII).

Each of the above artifacts has a corresponding path‑proof sidecar:

* `artifacts/db/backup/backup_manifest.json.path_proof.txt`  
    
* `artifacts/db/backup/restore_verify.log.path_proof.txt`  
    
* `artifacts/db/retention/retention_run.log.path_proof.txt`

**Indexing and routing (titles‑only).**

* Indexing rules, mirror schema, and field‑level constraints for these artifacts live in HDE‑Schemas & Artifacts (Evidence Index and JSONL mirror).  
    
* Backup/restore/retention QA procedures and acceptance criteria live in Glow QA Guide, with policy and tokens routed to HDE‑Governance.  
    
* PF07 records only that lifecycle work is OPS‑run on Railway and where its governed artifacts live; it does not restate lifecycle policy, token names, or artifact schemas.

**Acceptance and artifact impact**

* **Acceptance tokens:** None new in PF07; lifecycle acceptance remains defined in HDE‑Governance and Glow QA Guide, with PF12 owning mirror/index behavior.  
    
* **Artifact paths:** Names‑only registration of the three lifecycle artifacts and their `.path_proof.txt` sidecars as part of the DB evidence set.

---

# **8\) Config keys & references (names \+ current values)**

**Policy (inventory-only).** This section lists key names and the current observed settings. When unknown, the value is marked **OPEN/TBD** (no guessing). **Secrets remain redacted.** Ownership/requiredness lives (titles-only) in **HDE-Schemas & Artifacts**; rails/policy lives in **HDE-Governance**. These entries are observations, not policy.

## **8.1 Shared keys**

**DATABASE\_URL**

* Prod (Railway): `postgresql://postgres:{redacted}@postgres.railway.internal:5432/railway`  
* Dev (OpenAI Codex): `postgresql://postgres:{redacted}@postgres.railway.internal:5432/railway`  
* QA (GitHub Codespaces): `postgresql://postgres:REDACTED@metro.proxy.rlwy.net:52353/railway`

**APP\_ENV**

* Prod (Railway): `prod`  
* Dev (OpenAI Codex): `dev`  
* QA (GitHub Codespaces): `dev`

**Note:** Infra-owned start helpers for the HD Engine, including dev/QA Reader start commands, MUST:

* Propagate `APP_ENV` from the caller (shell, harness, or platform) into the child process environment, and  
* MUST NOT silently force a default when `APP_ENV` is empty or unset.

PF07 records this as an infra responsibility only. The meaning of each `APP_ENV` variant and the expected HTTP/rails behavior per value are defined by title in **HDE-Mechanics Guide**, **HDE-Governance**, and **Glow QA Guide**. PF07 stays names-only and does not restate those semantics; it pins the key name and the requirement that infra helpers faithfully forward `APP_ENV` so QA harnesses can exercise the configured gating behavior.

**Conjunction identity env keys (names-only)**

* `ENGINE_TAG` — OPEN/TBD  
* `RELEASE_ID` — OPEN/TBD  
* `PRODUCT_INVOCATION_TAG` — OPEN/TBD

PF07 records only the key names here and does not define their byte-level behavior.

**SAFE\_MODE** (rails posture; current deployment inventory, names-only)

* Prod (Railway): `0`  
* Dev (OpenAI Codex): `1`  
* QA (GitHub Codespaces): key listed in OPS-01 documented bindings; value not supplied in the source matrix.

**ALLOW\_NETWORK** (rails posture; current deployment inventory, names-only)

* Prod (Railway): `1`  
* Dev (OpenAI Codex): `0`  
* QA (GitHub Codespaces): `0`

**Note (rails windows).**  
Current deployment values are infrastructure inventory, not transport policy. Rails policy, refusal semantics, and any temporary window semantics remain owned by **HDE-Governance** and **Glow QA Guide** by title.

**Environment pins** (names-only)

* `LC_ALL` — C  
* `LANG` — C  
* `TZ` — UTC

**EVIDENCE\_ROOT** (QA evidence root; names-only)

* Pattern: `audit/qa/<epic-id>`  
* Example (EPIC025): `audit/qa/hde-epic025`  
* Usage: Live QA plans may declare required evidence artifacts relative to `${EVIDENCE_ROOT}`.  
  * Common relative paths include `qa_step_logs_manifest.json`, `qa_step_logs_manifest.json.path_proof.txt`, `00_meta/doc_deltas.md`, and `checks/<check_id>/primary.log`.

**Railway metadata** (names-only)  
`RAILWAY_PROJECT_ID`, `RAILWAY_PROJECT_NAME`, `RAILWAY_SERVICE_ID`, `RAILWAY_SERVICE_NAME`, `RAILWAY_ENVIRONMENT`, `RAILWAY_ENVIRONMENT_NAME`, `RAILWAY_PUBLIC_DOMAIN`, `RAILWAY_PRIVATE_DOMAIN` — OPEN/TBD

**Retired HDE database-transport key names (history-only; not valid runtime inputs)**

* `DB_ALLOW_BRIDGE_IN_PROD`  
* `DB_BRIDGE_URL`  
* `DB_FORCE_BRIDGE`

These names are retained only as compatibility history and have no active PF07 environment mapping. Their absence is the required configuration posture; if present, report key names only and never values.

---

**Deprecated / unused (engine mode-free)**  
Recorded here to avoid drift; **not consumed by the Engine**. The Engine exposes no runtime modes; source selection is owned by Adapter/CLI.

* `ENGINE_DATA_MODE` — OPEN/TBD (dev: may be direct; prod: cached)  
    
* `ENGINE_REFRESH_POLICY` — OPEN/TBD (scheduled | explicit | hybrid)  
    
  ---

**BodyGraph and vendor tuning keys**

* `BODYGRAPH_TTL_S` — OPEN/TBD  
    
* `BODYGRAPH_SWR_S` — OPEN/TBD  
    
* `VENDOR_RATE_LIMIT` — OPEN/TBD (per-minute / per-hour)  
    
* `CB_FAIL`, `CB_WINDOW_S`, `CB_COOLDOWN_S` — OPEN/TBD  
    
  ---

**Notes**

* **Connection binding:** see §7.0 — the active HDE binding for every environment is `DATABASE_URL` with direct psycopg only; missing or unavailable direct access fails closed without bridge or alternate-provider fallback.

* ## **Historical evidence:** `artifacts/runtime/env_connectivity.snapshot.json` is retained as a governed bridge-era record only. It is not a current fallback requirement or evidence target.

**Admin writer credentials** (names-only; no values here)

* `HDE_ADMIN_TOKENS`, `HDE_ADMIN_SCOPES` — **OPEN/TBD**  
  Names-only keys for the admin credentials used to gate **admin-only HD Engine surfaces**, including CLI and HTTP admin bundle access to the Railway HD Engine (`glow-hdengine-v2`) and its shared database.

**Notes.**

* Values are **not** stored in the repo; they are realized as provider-managed secrets (for example, Railway environment secrets) and configured per environment by operators.  
    
* QA uses the same channel (provider secrets / environment configuration) for exercising admin-only surfaces under rails and QA windows defined elsewhere.  
    
* Rotation and revocation procedures (for example, changing or removing admin tokens) are documented by title in **HDE-Governance**, **Glow QA Guide**, and any relevant runbooks; PF07 records only the key names and their association with admin surfaces (CLI and HTTP admin bundle).  
    
* Requiredness, defaults, and validation rules for these keys are not defined here: ownership/requiredness → **HDE-Schemas & Artifacts**; rails/policy (including “admin auth required” and logging) → **HDE-Governance** (titles-only).  
    
* **No-guess binding posture for PF07-owned environments.** QA and Live QA documents MUST NOT guess or redefine PF07-owned bindings. When PF07 still records a needed binding as **OPEN/TBD**, including the local-dev sampler binding, the document MUST treat that requirement as a PF07-gap blocker and name the missing fact explicitly. It MUST NOT invent host, port, base URL, or external placeholder ownership for that binding. This applies to `DEV_SAMPLER_URL`, `HDE_BASE_URL`, `DATABASE_URL`, production service base URLs, environment-specific host and port bindings, and canonical QA-root patterns.

  ## **8.2 Component-specific keys**

  ### **8.2.1 HD Engine**

**Port**  
• Dev (CodEx): `scripts/dev_start_reader.sh` defaults to 8000; `run_flask.py` and `run_flask_dev.sh` default to 5000 unless overridden. • QA (Codespaces): 8000  
• Prod (Railway): 8000

**`HDE_WRITE_A7_PROOFS` — A7 proof artifact emission gate (names-only)**

* **Observed behavior (routing-only):** when this key is set for a run, A7 proof artifacts are written; default test runs do not write proof files.  
    
* **Observed usage:** `HDE_WRITE_A7_PROOFS=1` (value and binding are run-scoped; per-environment bindings are **OPEN/TBD**).

**Dev harness URLs (internal/dev HTTP; names-only)**

**`DEV_SAMPLER_URL` — dev sampler HTTP harness base URL**

*Dev/CodEx (local dev):* `http://127.0.0.1:8000/internal/dev/sampler`

*QA (Codespaces):* `http://127.0.0.1:8000/internal/dev/sampler`

*Prod (Railway):* not set / not applicable (internal/dev sampler HTTP harness is dev-only).

**Binding ownership and pattern (names-only).**

* `DEV_SAMPLER_URL` is an **infra-owned config key** for the **dev-only sampler HTTP harness** base URL (for routes such as `POST /internal/dev/sampler`) in dev/Codespaces/local-dev environments.  
* The value MUST be derived from the **actual dev Reader process wiring** (host and port) for that environment, not guessed or reconstructed inside QA harnesses or docs.  
* Across environments, the invariant **pattern** is:  
  `DEV_SAMPLER_URL = <base_url>/internal/dev/sampler`  
  where `<base_url>` is the reachable base URL for the dev Reader HTTP service in that environment.  
* **Single published client-access binding per environment.** For the dev-only sampler harness, PF07 records at most one published client-access `DEV_SAMPLER_URL` binding per environment at a time.  
* QA, OPS, and closeout artifacts MUST consume the one published binding recorded for the named environment and MUST NOT model parallel published bindings for that same environment unless PF07 is explicitly updated.

**Codespaces home for DEV\_SAMPLER\_URL (names-only).**

In the HD Engine GitHub Codespaces environment for `amthorn78/glow-hdengine-v2`:

* The **canonical home** for the DEV\_SAMPLER\_URL binding is the devcontainer configuration. `.devcontainer/devcontainer.json` MUST define:  
  `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`  
  under a container environment block (for example, `containerEnv`), so that every shell in the Codespace sees the same value without manual export.  
* Shell-level `export DEV_SAMPLER_URL=...` MAY be used for one-off debugging, but the devcontainer environment is the **authoritative infra binding** for this environment.

**Harness expectations (routing-only).**

* Dev sampler HTTP QA tools in this repo (for example, healthcheck and D3 Live QA harnesses) are expected to **read DEV\_SAMPLER\_URL from the environment** and treat it as a required input; they MUST NOT hardcode host/port or recompute `<base_url>` internally.  
* Missing or mismatched DEV\_SAMPLER\_URL for a given environment is classified here as an **infra/tooling misconfiguration** for dev sampler HTTP harnesses, not as an HD Engine behavior failure. Detailed classification (for example, FAIL\_TOOLING vs behavior), preconditions, and token semantics live by title in **Glow QA Guide**, **HDE-Governance**, **HDE-Mechanics Guide**, and **HDE-Build Checklist**.

PF07 records the **key name**, the **per-environment binding locations**, and the **URL pattern** as infrastructure facts. It does **not** define HTTP behavior, header/body contracts, or acceptance tokens for the dev sampler HTTP harness; those remain owned by **HDE-CLI-API-Vendor-Ref**, **HDE-Mechanics Guide**, **Glow QA Guide**, **HDE-Governance**, and **HDE-Build Checklist** (titles-only).

**LOG\_LEVEL**  
• OPEN/TBD (all envs)

**Loader selector**  
• `PACK_SHA`: OPEN/TBD (active narratives pack identity; file-backed runtime)

**Vendor-ingest keys (present where noted; secrets redacted)**

* `HD_API_BASE_URL` — canonical HumanDesignAPI base URL environment variable. Current deployed v2 base URL value: `https://api.humandesignapi.nl/v2`. The configured base URL owns the vendor API version boundary.  
* Runtime request construction must append only version-neutral resource paths to the configured base URL. PF07 records the infrastructure key and current base URL value only. Request construction, byte contracts, route contracts, and validation behavior live in **HDE-CLI-API-Vendor-Ref** and **HDE-Mechanics Guide** by title.  
* `HDAPI_BASE_URL` — deprecated legacy alias only. It must not be used as the canonical key in plans, implementation prompts, QA plans, OPS tasks, or PF documentation.  
* If both `HD_API_BASE_URL` and `HDAPI_BASE_URL` exist with different values, classify that as configuration ambiguity and fail closed through the owning implementation and policy homes. PF07 records the key posture only; runtime behavior remains owned by **HDE-CLI-API-Vendor-Ref** and **HDE-Mechanics Guide**.  
* `HD_API_KEY` — canonical vendor API key environment variable. It is secret-bearing and belongs to the HD Engine infrastructure boundary.  
* `GEO_API_KEY` — canonical geocoding/vendor-support key when required. It is secret-bearing and belongs to the HD Engine infrastructure boundary.  
* Outbound vendor header projection is not the same as environment-variable naming:  
  * HumanDesignAPI v1 legacy BodyGraph routes project `HD_API_KEY` as `HD-Api-Key: {redacted}`.  
  * HumanDesignAPI v2 chart routes project `HD_API_KEY` as `Authorization: Bearer {redacted}`.  
  * Routes requiring geocoding project `GEO_API_KEY` as `HD-Geocode-Key: {redacted}`.  
* Glow app should not require direct vendor API credentials. Any future cross-service invocation must preserve secret isolation and avoid a parallel vendor credential path unless a future ADR or canon update explicitly changes this boundary.  
* No raw API keys, bearer tokens, geocode keys, database passwords, full unredacted request headers, or full private vendor payloads may be recorded in PF07, plans, prompts, QA artifacts, OPS evidence, or closeout records.  
* No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider base URL, AI-provider API key, AI-provider secret-binding name, or AI-provider runtime rail is required or permitted by this HDAPI v2 conformance update.

**Notes (inventory-only).**

* PF07 names the HD Engine port mapping and the `DEV_SAMPLER_URL` key as part of the infrastructure inventory. PF07 pins the **Codespaces container-local** `DEV_SAMPLER_URL` binding (`http://127.0.0.1:8000/internal/dev/sampler`) because it is a stable infra fact for the governed dev sampler harnesses; other environments may use a different `<base_url>` and remain **OPEN/TBD** until confirmed. PF07 does not define how the dev harness is started or specify QA procedures; those details (start commands, curl patterns, acceptance tokens) live by title in **HDE-Mechanics Guide**, **HDE-CLI-API-Vendor-Ref**, **Glow QA Guide**, and **HDE-Build Checklist**.  
* Requiredness, defaults, and validation rules for these keys are not defined here: ownership/requiredness → **HDE-Schemas & Artifacts**; rails/policy (including dev-harness validation and rails posture) → **HDE-Governance** and **Glow QA Guide** (titles-only).

**HDE-EPIC029 binding-equivalence note (historical exception; names-only).**

* For HDE-EPIC029 only, a bounded governed evidence family recorded `local_dev` using the same published `DEV_SAMPLER_URL` client-access binding as Codespaces — `http://127.0.0.1:8000/internal/dev/sampler` — for the same dev-only sampler harness route.  
* When that epic-specific posture was used, the closure mode was named explicitly as **binding-equivalence**.  
* The equivalence was limited to the published client-access binding only. It did **not** by itself assert the same server bind address, a globally confirmed local-dev environment identity, a different route, or a different port beyond the published binding.  
* This was an epic-specific closure exception and does **not** establish a general PF07 rule for future work. Future epics must not treat local-dev as closed by binding-equivalence unless PF07 is explicitly updated again with a new bounded rule.  
* Unless independently confirmed, PF07’s general local-dev environment binding remains **OPEN/TBD** and must be evidenced directly rather than inferred from another environment’s published binding.  
* This historical exception does **not** authorize invented hosts, invented ports, invented routes, guessed forwarded URLs, or any change to prod-facing URLs.

### **8.2.2 Glow Backend — TBD (names-only)**

* `PORT`, `LOG_LEVEL`, `SECRET_KEY`, `REDIS_URL`, `MAILGUN_API_KEY`, `MAILGUN_DOMAIN`, `SESSION_SECRET`, `CSRF_SECRET`, `TZ`, \[TBD additional names\] — **OPEN/TBD** (all values)

### **8.2.3 Glow Frontend — TBD (names-only)**

* \[TBD public config names\], \[TBD additional names\] — **OPEN/TBD** (all values)

**Notes (inventory-only).**

* Dev/CodEx and QA/Codespaces may operate with rails open; this is reflected only where observed (explicit where known, **OPEN/TBD** where not visible).  
* Any **OPEN/TBD** indicates “not present in the variable report / not confirmed.” Please supply the value when known.  
* **Names-only disclaimer.** Requiredness, defaults, and validation rules are not defined here: ownership/requiredness → **HDE-Schemas & Artifacts**; rails/policy → **HDE-Governance** (titles-only).

---

# **9\) Resource catalog (IDs & links)**

> **Names-only.** This catalog lists stable **provider/project/service** names and known **hosts/links** where we have them. Unknowns remain **TBD** (no guessing). It mirrors single homes in §§2, 3, 4, 5, and 6 to avoid duplication.

## **9.1 Provider projects**

* **Railway**  
  * **HD Engine project:** `ample-illumination` *(id: **TBD**)*  
  * **Glow Backend project:** `ample-illumination` *(id: **TBD**)*  
* **Vercel**  
  * **Team:** **TBD**  
  * **Glow Frontend project:** **TBD**

## **9.2 Services**

* **HD Engine (Railway)** — service `glow-hdengine-v2` · base URL `https://glow-hdengine-v2-production.up.railway.app`  
* **Glow Backend (Railway)** — service `glow-backend-v4` · base URL **TBD**  
* **Glow Frontend (Vercel)** — site `glowme.io` (production) · previews **TBD**

**Notes (names-only).** No secrets or policy here. Endpoint bytes, request/response contracts, and governance/policy are routed by title to the owning product’s canonical contract and governance documents. For the HD Engine surfaces recorded in this section, the current contract home is **HDE-CLI-API-Vendor-Ref** and the current governance home is **HDE-Governance** (titles-only).

### **9.2.1 Object storage (narratives pack store)**

• **Provider:** TBD  
• **Bucket / prefix:** TBD (immutable path pattern `/narratives/<pack_sha>/...`)  
• **Used by:** HD Engine loader (file-backed runtime)

*Note (narratives):* The loader fetches and verifies pack files from object storage by **PACK\_SHA** (see §8.2.1). Policy, identity, and canonicalization live by title in **HDE-Schemas & Artifacts** and **Narratives Guide**.

---

## **9.3 Repositories (titles-only)**

* Authoritative slugs & paths: **§5.1 HD Engine repo**, **§5.2 Glow Backend repo**, **§5.3 Glow Frontend repo**.

  ## **9.4 Domains**

* **Root:** `glowme.io`  
    
* **Subdomains per environment & component:** see **§6 Domains & DNS**.  
    
  * **Note:** HD Engine uses a **Railway app domain** (see §4.1), not a `glowme.io` subdomain.


  ---

# **10\) Service start declarations**

PF07 records the following checked-in repository declarations at the inspected commit. This section does not assert that any declaration is the current Railway start command or the normative production command. The current Railway setting is not verified.

## **10.1 Checked-in declarations**

- `validation/service_cmd.txt` records a validation command that installs `requirements.txt` and then invokes Gunicorn with `adapter.factory:create_app()`, binding `0.0.0.0:$PORT` with 2 workers, 4 threads, and a 30-second timeout.

```
python -m pip install --no-cache-dir -r requirements.txt && python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30
```

- `Procfile` declares a `web` process that invokes Gunicorn through `/app/.venv/bin/python`, with the same app-factory, bind, worker, thread, and timeout values, and without the validation file's dependency-install prefix.

```
web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30
```

- `scripts/start_web.sh` is an auxiliary launcher that prefers `/app/.venv/bin/python`, otherwise selects `gunicorn` from `PATH`, and substitutes port 8000 when `PORT` is absent.

```shell
#!/usr/bin/env bash
set -euo pipefail

CMD_ARGS="'adapter.factory:create_app()' --bind 0.0.0.0:${PORT:-8000} --workers 2 --threads 4 --timeout 30"

if [ -x /app/.venv/bin/python ]; then
  echo "[start_web] using venv python at /app/.venv/bin/python"
  exec /app/.venv/bin/python -m gunicorn ${CMD_ARGS}
else
  echo "[start_web] /app/.venv/bin/python not found; falling back to shimmed gunicorn on PATH"
  command -v gunicorn >/dev/null 2>&1 || { echo "[start_web] gunicorn not found on PATH"; exit 127; }
  exec gunicorn ${CMD_ARGS}
fi
```

These declarations differ in interpreter selection, dependency installation, and missing-`PORT` behavior. Their common fields do not make them equivalent, deployed, or canonical.

## **10.2 What this does (architecture, names-only)**

- **Process model.** All three declarations invoke Gunicorn with `--workers 2`, `--threads 4`, and `--timeout 30`; none invokes the Flask development server.  
    
- **Binding.** `validation/service_cmd.txt` and `Procfile` bind to `0.0.0.0:$PORT`. `scripts/start_web.sh` binds to `0.0.0.0:${PORT:-8000}`.  
    
- **Entrypoint.** All three declarations name `adapter.factory:create_app()`.  
    
- **Bootstrap.** Only `validation/service_cmd.txt` installs runtime dependencies from `requirements.txt` before invoking Gunicorn.

  ## **10.3 Environment prerequisites (names-only)**

- `PORT`: `validation/service_cmd.txt` and `Procfile` reference `$PORT` without a fallback; `scripts/start_web.sh` substitutes `8000` when `PORT` is absent.  
    
- `APP_ENV`: the `prod` example remains inventoried in §8; none of the three declarations assigns `APP_ENV`.  
    
- **Environment pins (names-only):** `LC_ALL`, `LANG`, and `TZ` remain inventoried in §8 with values OPEN/TBD unless confirmed; none of the three declarations assigns them.

  ## **10.4 Change control (minimal)**

- Treat the three declarations as distinct checked-in surfaces. Their presence does not establish deployment or a normative production command.  
    
- If a declaration changes, update this section and any checked-in description or validation artifact that claims to mirror it in the same change.  
    
- Governed evidence synchronization is owned by `PF12-Canon-HDE-Schemas-and-Artifacts`. PR workflow is owned by `PF06-Canon-Epic-Process-Guide`. PF07 does not restate either contract.

## **10.5 Evidence index locations and ownership**

PF07 records two stable repository locations used to discover governed evidence:

- Human Evidence Index: `docs/evidence/INDEX.json`  
- Machine Evidence Mirror: `artifacts/evidence_index.jsonl`

PF07 owns no additional evidence root, index, schema, record shape, artifact-path catalog, QA layout, run-history policy, or snapshot policy. Governed evidence families, record shapes, artifact paths, companion proofs, checksums, root classification, and index/mirror contracts are owned by `PF12-Canon-HDE-Schemas-and-Artifacts`. Live QA layout, current-state evidence posture, historical-run treatment, and the optional Codespaces snapshot posture are owned by `PF19-Canon-Glow-QA-Guide`.

---

## 10.6 Acceptance (titles-only)

Acceptance requirements for environment and runtime wiring (for example, start-command capture, app-factory binding to $PORT, and required PORT at runtime) are governed by the relevant product’s canonical governance and QA documents (titles-only). Glow Infrastructure routes by title and does not enumerate token names.