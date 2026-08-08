# **0\. Front Matter**

**Title:** PF07-Canon-Glow-Infrastructure  
**Version:** v2.2.8

**Status:** Canon  
**Effective date:** 2026-08-08

**Last Update Gate:** BN 12.6.2 A28-44

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
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Glow Backend | Railway | ample-illumination | glow-backend-v4 | TBD | TBD | ample-illumination/production/postgres | **TBD (backend schema may differ)** |
| HD Engine | Railway | ample-illumination | glow-hdengine-v2 | TBD | [https://glow-hdengine-v2-production.up.railway.app](https://glow-hdengine-v2-production.up.railway.app) | ample-illumination/production/postgres | **hde** |
| Frontend | Vercel | TBD | TBD | — | glowme.io (prod), previews TBD | — | — |

### Staging/QA (GitHub Codespaces)

| Component | Codespace | Base URL / Forwarded Port | Linked Target / DB |
| ----- | ----- | ----- | ----- |
| Frontend | TBD | TBD | Backend target TBD |
| Backend | TBD | TBD | **Shared production DB instance** *(backend schema **TBD**)* |
| HD Engine | TBD | TBD | **Shared production DB instance** *(schema **`hde`**)* |

### Development (OpenAI Codex)

| Component | Workspace | Upstream / DB |
| ----- | ----- | ----- |
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
 The adapter selects its source by environment: **prod → database** (no inline vendor calls in the request path); **dev → vendor allowed**, and on success **upsert to DB** for repeatability. **SAFE rails and detailed policy** live in **HDE-CLI-API-Vendor-Ref** and **HDE-Governance**; PF07 records **names-only**. Evidence of source selection (keys-only snapshot) is indexed per **HDE-Schemas & Artifacts** (human index \+ machine mirror in the same PR).

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

**Codespaces snapshot step (routing-only).**  
 Every Live QA plan executed in Codespaces MUST include a mechanical “Codespaces snapshot” step at the beginning of the run that captures the run-relevant environment context into the epic QA root under `audit/qa/<epic-id>/...` (including tool versions, rails variables, and presence/absence of required secrets, but never secret values). Canonical artifact locations and filenames for the snapshot are recorded in §10.5 (names-only); schema and capture commands are owned by title in **Glow QA Guide** (and in **HDE-Schemas & Artifacts** if the snapshot is a governed evidence family).

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

* PF07 does **not** define how connectivity tests are run or which D-goals or QA tokens they satisfy; it records only the provider, project, service, base-URL, and instance names that those tests and tokens depend on.  
  ---

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
* **Start command (inventory):** see **§10** (canonical Railway command kept verbatim)  
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
  * **Railway service:** `glow-backend-v4`  
    ---

## **5.3 Glow Frontend repo**

* **Repository:** `amthorn78/glow-frontend-v2`  
* **Primary app code paths:** **TBD**  
* **Service mapping (names-only):**  
  * **Vercel team:** **TBD**  
  * **Vercel project:** **TBD**  
  * **Production domain:** `glowme.io`  
  * **Preview domains:** **TBD**

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
  * **No proactive probe:** do not run test queries pre-selection; on total failure return a deterministic, numeric-free error.

* **Runtime search\_path**  
  *  `hde, public` (unquoted; in this order). Verify at startup (emit a `SHOW search_path` echo in ops logs). Pin at the ROLE level.

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
* **Historical evidence:** `artifacts/runtime/env_connectivity.snapshot.json` is retained as a governed bridge-era record only. It is not a current fallback requirement or evidence target.  
  ---

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
• Dev (CodEx): 8000  
• QA (Codespaces): 8000  
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
* Machine snapshot keys: use the JSON keys maintained in the **resource object of §9 (machine block)** for `production.*.repo`, `staging.*.repo`, `development.*.repo`.

  ## **9.4 Domains**

* **Root:** `glowme.io`  
* **Subdomains per environment & component:** see **§6 Domains & DNS**.  
  * **Note:** HD Engine uses a **Railway app domain** (see §4.1), not a `glowme.io` subdomain.

  ---

  # **10\) Service start command (production) \[Implemented\]**

  ## **10.1 Canonical command (Railway)**

Keep verbatim — this is the source of truth as configured in Railway.  
 python \-m pip install \--no-cache-dir \-r requirements.txt && python \-m gunicorn 'adapter.factory:create\_app()' \--bind 0.0.0.0:$PORT \--workers 2 \--threads 4 \--timeout 30

## **10.2 What this does (architecture, names-only)**

* **Process model.** Gunicorn master with a worker pool (`--workers 2`) and per-worker threads (`--threads 4`); **no Flask dev server**.  
* **Binding.** Listens on `0.0.0.0:$PORT` (platform injects `PORT`).  
* **Entrypoint.** Application factory `adapter.factory:create_app()` returns the WSGI app.  
* **Bootstrap.** Installs runtime dependencies from `requirements.txt` before starting the server.

  ## **10.3 Environment prerequisites (names-only)**

* `PORT` (platform-provided)  
* `APP_ENV` (e.g., prod; value observed in §8)  
* **Environment pins (names-only):** `LC_ALL`, `LANG`, `TZ` — inventory lives in §8 (values OPEN/TBD unless confirmed)

  ## **10.4 Change control (minimal)**

* Treat the command string above as **canonical for production**.  
* If the command or any parameter changes (flags, worker/thread counts, entrypoint), **update this section and the canonical evidence** in the **same change** (see 10.5).  
* PR-first via CodEx: the **Doc-Delta**, **human Evidence Index**, and **machine JSONL mirror** must update **in the same PR** when the command or env-pins change.

## 10.5 Evidence & indexing (titles-only; updated QA posture)

### Single home (entries & types)

The authoritative listing of evidence artifacts (titles/paths) and governed record types is owned by the canonical **Schemas & Artifacts** document (titles-only). **Glow Infrastructure** is names-only: it inventories stable evidence index and mirror file locations used by the repo, but does not define evidence schemas, acceptance rules, or token semantics.

**Multi-root evidence posture (clarification; names-only).** The EPIC025, EPIC030, EPIC031, EPIC032, and EPIC033 audits observe governed or evidence-like outputs stored across multiple roots and root-adjacent homes, including `docs/evidence/`, `artifacts/`, `audit/gates/`, `audit/qa/`, `artifacts/audit/`, `artifacts/proofs/`, `artifacts/ops/internal_version/`, `audit/`, `docs/`, `tools/`, `scripts/`, `catalog/`, `ci/`, `.github/`, `config/`, `schemas/`, `goldens/`, `fixtures/`, `proofs/`, `parity/`, `reports/`, `scan_reports/`, `validation/`, `narratives/`, `internal/`, `sql/`, `migrations/`, `math/`, `freeze/`, `release/`, and `tests/transport/headers/`. In PF07, “single home” in evidence terms means the single authoritative Evidence Index plus machine mirror parity and the fixed-path governed evidence surfaces enumerated below, not that all evidence bytes or evidence-like snapshots must live under one directory root.

**Classification note (routing-only).** PF07 records root names and stable paths only. Evidence-family classification and any decision to treat a root as governed evidence vs tooling output is owned by the canonical Schemas & Artifacts document (titles-only).

**Retired bridge evidence classification (routing-only).** Every retained evidence title or path in §10.5 that names `pg-bridge`, `DB_BRIDGE_URL`, `DB_FORCE_BRIDGE`, `DB_ALLOW_BRIDGE_IN_PROD`, bridge selection, fallback, capability, parity, consistency, or a bridge-only token is historical only. It remains listed to preserve governed paths and bindings; it does not prove a current service, runtime input, fallback, evidence target, token claim, or OPS PASS. No new bridge evidence is produced through a retired transport.

**Governed-root coordination (routing-only).** Coordination across `docs/`, `artifacts/`, and `audit/` is authoritative only through the Evidence Index, the machine mirror, and the fixed canonical governed surfaces recorded in this section. Multi-root synchronization does not create additional truth homes by itself.

**Authority boundary (routing-only).** Roots that appear to hold evidence, proofs, reports, parity material, or other truth-like outputs are non-authoritative by default unless the canonical Schemas & Artifacts document or another owning canonical home explicitly catalogs them or routes authority there. Their presence in repo reality does not, by itself, make them governed evidence homes or acceptance-binding locations.

**Example-list posture (routing-only).** Root lists in this section are illustrative and non-exhaustive. They identify roots readers might mistake for truth homes, but enumeration alone does not grant authority to any listed root.

### Indexing discipline (same-change-set rule)

Whenever governed evidence bytes change, update in the same change-set:

* Human Evidence Index: `docs/evidence/INDEX.json`  
* Human Evidence Index path-proof: `docs/evidence/INDEX.json.path_proof.txt`  
* Evidence Index hash sentinel: `docs/evidence/INDEX.sha256`  
* Evidence Index hash sentinel path-proof: `docs/evidence/INDEX.sha256.path_proof.txt`  
* Human Evidence Index page (docs-side): `docs/evidence/INDEX.md`  
* Human path-proof anchors root (docs-side): `docs/evidence/path_proof/`  
* `Machine mirror (records-only): artifacts/evidence_index.jsonl`  
* `Machine mirror path-proof: artifacts/evidence_index.jsonl.path_proof.txt`  
* `Machine mirror hash sentinel: artifacts/evidence_index.jsonl.sha256`  
* `Machine mirror hash sentinel path-proof: artifacts/evidence_index.jsonl.sha256.path_proof.txt`  
* Docs evidence index snapshot (JSON): `docs/evidence_index_snapshot/index.json`  
* Docs evidence index snapshot (JSON): `docs/evidence_index_snapshot/index.json`  
* Docs evidence index snapshot path-proof: `docs/evidence_index_snapshot/index.json.path_proof.txt`

* Docs evidence index snapshot hash sentinel: `docs/evidence_index_snapshot/index.sha256`  
* Docs evidence index snapshot hash path-proof: `docs/evidence_index_snapshot/index.sha256.path_proof.txt`  
* Mirror schema (JSON): `ci/checks/mirror_schema.json`  
* Mirror schema path-proof: `ci/checks/mirror_schema.json.path_proof.txt`  
* Mirror schema hash sentinel: `ci/checks/mirror_schema.json.sha`  
  Mirror schema hash path-proof: `ci/checks/mirror_schema.json.sha.path_proof.txt`

**Proof freshness (governed artifacts).** If any file above changes bytes, its co-located `*.path_proof.txt` transcript MUST be refreshed in the same change-set. Stale index or mirror path-proofs are a hard evidence integrity failure.

**`HDE-EPIC033 PR-01 HDAPI v2 contract-inventory evidence roots (names-only).`** `The HDE-EPIC033 PR-01 HumanDesignAPI v2 and legacy v1 contract-inventory evidence family is governed path inventory for HDE-FERM006. It records contract-inventory evidence only. It does not claim HumanDesignAPI v2 runtime conformance, runtime request shaping, runtime source selection, open-rails vendor smoke, public Reader byte change, public route change, new HTTP home, or AI runtime or evidence scope.`

`Primary governed contract-inventory artifacts:`

* `artifacts/vendor/hdapi_v2/source_inventory.json`  
* `artifacts/vendor/hdapi_v2/source_inventory.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/source_inventory.md`  
* `artifacts/vendor/hdapi_v2/source_inventory.md.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/openapi_validation.log`  
* `artifacts/vendor/hdapi_v2/openapi_validation.log.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/known_anomalies.md`  
* `artifacts/vendor/hdapi_v2/known_anomalies.md.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/endpoint_reference.csv`  
* `artifacts/vendor/hdapi_v2/endpoint_reference.csv.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/contract_map.json`  
* `artifacts/vendor/hdapi_v2/contract_map.json.path_proof.txt`

`Closed-rails source-cache inputs for the PR-01 contract inventory:`

* `artifacts/vendor/hdapi_v2/source_cache/api-reference.openapi.json`  
* `artifacts/vendor/hdapi_v2/source_cache/authentication.body`  
* `artifacts/vendor/hdapi_v2/source_cache/coordinates_guide.body`  
* `artifacts/vendor/hdapi_v2/source_cache/llms-full.endpoint-tiers.txt`  
* `artifacts/vendor/hdapi_v2/source_cache/llms_txt.body`  
* `artifacts/vendor/hdapi_v2/source_cache/migration_v1_to_v2.body`  
* `artifacts/vendor/hdapi_v2/source_cache/rate_limiting.body`  
* `artifacts/vendor/hdapi_v2/source_cache/response_format.body`  
* `artifacts/vendor/hdapi_v2/source_cache/robots_preflight.body`  
* `artifacts/vendor/hdapi_v2/source_cache/source_metadata.json`  
* `artifacts/vendor/hdapi_v2/source_cache/v1-routes.yaml`  
* `artifacts/vendor/hdapi_v2/source_cache/v1_overview.body`  
* `artifacts/vendor/hdapi_v2/source_cache/v2-routes.yaml`  
* `artifacts/vendor/hdapi_v2/source_cache/v2_coordinates_chart_page.body`  
* `artifacts/vendor/hdapi_v2/source_cache/v2_full_chart_page.body`  
* `artifacts/vendor/hdapi_v2/source_cache/v2_overview.body`  
* `artifacts/vendor/hdapi_v2/source_cache/v2_simple_chart_page.body`

`HDE-EPIC033 PR-01 QA, acceptance, and doc-delta support surfaces:`

* `docs/acceptance_map_epic033.json`  
* `docs/acceptance_map_epic033.json.path_proof.txt`  
* `audit/qa/hde-epic033/token_evidence_matrix.md`  
* `audit/qa/hde-epic033/token_evidence_matrix.md.path_proof.txt`  
* `audit/qa/hde-epic033/acceptance_map_viability.log`  
* `audit/qa/hde-epic033/acceptance_map_viability.log.path_proof.txt`  
* `audit/docdeltas/hde-epic033_doc_deltas.md`  
* `audit/docdeltas/hde-epic033_doc_deltas.md.path_proof.txt`  
* `audit/qa/hde-epic033/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic033/00_meta/doc_deltas.md.path_proof.txt`

**HDE-EPIC033 Live QA Step-0B, po-001 through po-014, and qa-16 check-local evidence surfaces (names-only).** The governed check-local and supporting evidence surfaces for these HDE-EPIC033 QA checks are carried at:

Step-0B \- Doc Delta Capture receipt:

* `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log`  
* `audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`

PO-001 \- source inventory grounding receipt:

* `audit/qa/hde-epic033/checks/po-001/primary.log`  
* `audit/qa/hde-epic033/checks/po-001/primary.log.path_proof.txt`

PO-002 \- AI and LLM boundary receipt:

* `audit/qa/hde-epic033/checks/po-002/primary.log`  
* `audit/qa/hde-epic033/checks/po-002/primary.log.path_proof.txt`

PO-003 \- route validation receipt:

* `audit/qa/hde-epic033/checks/po-003/primary.log`  
* `audit/qa/hde-epic033/checks/po-003/primary.log.path_proof.txt`

PO-004 \- OpenAPI validation and anomaly quarantine receipt:

* `audit/qa/hde-epic033/checks/po-004/primary.log`  
* `audit/qa/hde-epic033/checks/po-004/primary.log.path_proof.txt`

PO-005 \- endpoint reference and contract-map receipt:

* `audit/qa/hde-epic033/checks/po-005/primary.log`  
* `audit/qa/hde-epic033/checks/po-005/primary.log.path_proof.txt`

PO-006 \- contract-map and no-runtime-request-shaping receipt:

* `audit/qa/hde-epic033/checks/po-006/primary.log`  
* `audit/qa/hde-epic033/checks/po-006/primary.log.path_proof.txt`

PO-006 accepted remediation receipt:

* `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log`  
* `audit/qa/hde-epic033/checks/po-006-remediation-r3/primary.log.path_proof.txt`

PO-007 \- Evidence Index and Machine Mirror receipt:

* `audit/qa/hde-epic033/checks/po-007/primary.log`  
* `audit/qa/hde-epic033/checks/po-007/primary.log.path_proof.txt`

PO-008 \- acceptance-token posture receipt:

* `audit/qa/hde-epic033/checks/po-008/primary.log`  
* `audit/qa/hde-epic033/checks/po-008/primary.log.path_proof.txt`

PO-009 \- HDE-FERM006 supportability receipt:

* `audit/qa/hde-epic033/checks/po-009/primary.log`  
* `audit/qa/hde-epic033/checks/po-009/primary.log.path_proof.txt`

PO-010 \- runtime-request-shaping non-claim receipt:

* `audit/qa/hde-epic033/checks/po-010/primary.log`  
* `audit/qa/hde-epic033/checks/po-010/primary.log.path_proof.txt`

PO-010 accepted remediation receipt:

* `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log`  
* `audit/qa/hde-epic033/checks/po-010-remediation-r1/primary.log.path_proof.txt`

PO-011 \- inventory-only runtime-conformance non-claim receipt:

* `audit/qa/hde-epic033/checks/po-011/primary.log`  
* `audit/qa/hde-epic033/checks/po-011/primary.log.path_proof.txt`

PO-012 \- no-expansion boundary receipt:

* `audit/qa/hde-epic033/checks/po-012/primary.log`  
* `audit/qa/hde-epic033/checks/po-012/primary.log.path_proof.txt`

PO-012 accepted remediation receipt:

* `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log`  
* `audit/qa/hde-epic033/checks/po-012-remediation-r1/primary.log.path_proof.txt`

PO-013 \- evidence refresh, orientation, and index coherence receipt:

* `audit/qa/hde-epic033/checks/po-013/primary.log`  
* `audit/qa/hde-epic033/checks/po-013/primary.log.path_proof.txt`

PO-013 QA\_PLAN\_UPDATE routing receipt:

* `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/primary.log`  
* `audit/qa/hde-epic033/checks/po-013-qa-plan-update-r1/primary.log.path_proof.txt`

PO-013 accepted remediation receipt:

* `audit/qa/hde-epic033/checks/po-013-remediation-r3/primary.log`  
* `audit/qa/hde-epic033/checks/po-013-remediation-r3/primary.log.path_proof.txt`

PO-014 \- final separation and non-claim receipt:

* `audit/qa/hde-epic033/checks/po-014/primary.log`  
* `audit/qa/hde-epic033/checks/po-014/primary.log.path_proof.txt`

qa-16 \- closeout deliverables receipt:

* `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log`  
* `audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.path_proof.txt`

qa-16 closeout support surfaces:

* `audit/qa/hde-epic033/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic033/qa_step_logs_manifest.json.path_proof.txt`  
* `audit/qa/hde-epic033/00_meta/discovery_artifact.md`  
* `audit/qa/hde-epic033/00_meta/discovery_artifact.md.path_proof.txt`  
* `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md`  
* `audit/qa/hde-epic033/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`

These check-local receipts do not replace, satisfy, or relocate canonical close-pack artifacts, and they do not create HumanDesignAPI v2 runtime conformance, public Reader byte changes, public route changes, open-rails vendor-smoke proof, or AI runtime or evidence scope.

HDAPI v2 conformance evidence surfaces shared across HDE-EPIC034 and HDE-EPIC035 (names-only; no runtime-conformance overclaim):

* `artifacts/vendor/hdapi_v2/source_selection.snapshot.json`  
* `artifacts/vendor/hdapi_v2/source_selection.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/v1_legacy_guard.log`  
* `artifacts/vendor/hdapi_v2/v1_legacy_guard.log.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`  
* `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`  
* `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`  
* `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/closed_rails_refusal.txt`  
* `artifacts/vendor/hdapi_v2/closed_rails_refusal.txt.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json`  
* `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`  
* `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`  
* `artifacts/vendor/hdapi_v2/release_binding.snapshot.json.path_proof.txt`

HDE-EPIC035 classification for the shared HDAPI v2 evidence surfaces:

* HDE-EPIC035 PR-01 provider-outcome evidence for HDE-FERM008.3 uses `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` and `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json`, with their sibling path-proof transcripts.  
* HDE-EPIC035 PR-02 response-normalization evidence for HDE-FERM008.4 uses `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` and `artifacts/vendor/hdapi_v2/release_binding.snapshot.json`, with their sibling path-proof transcripts.  
* HDE-EPIC035 PR-02 records an exact adapter/schema gap. It does not prove that v2 ChartResult or ChartSimpleResult data feeds the existing BodyGraph cache, person input, or compat path.  
* HDE-EPIC035 PR-03 binds PR-01, PR-02, and retained OPS-01 evidence into the evidence-loop closure surface. The canonical PR-03 acceptance map lives at `docs/acceptance_map_epic035.json`, with sibling path proof.  
* HDE-EPIC035 PR-03 QA and acceptance-boundary support surfaces include `audit/qa/hde-epic035/token_evidence_matrix.md`, `audit/qa/hde-epic035/acceptance_map_viability.log`, `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log`, `audit/docdeltas/hde-epic035_doc_deltas.md`, and `audit/qa/hde-epic035/00_meta/doc_deltas.md`, with sibling path proofs where promoted into governed evidence.  
* These HDE-EPIC035 evidence surfaces do not create full HumanDesignAPI v2 runtime conformance, PF09 status movement, QA PASS, OPS completion, epic closeout, public Reader change, public route change, public flag change, public payload or transport change, new HTTP home, app-side HumanDesignAPI credential ownership, raw payload persistence, or AI runtime or evidence scope.

**HDE-EPIC036 PR-01 and PR-02 `bg:resolve` route-policy evidence surfaces (names-only).**

The HDE-EPIC036 `bg:resolve --source vendor` route-policy evidence family is carried under:

* `artifacts/vendor/hdapi_v2/`  
* `audit/qa/hde-epic036/`  
* `audit/docdeltas/`  
* `docs/`

Concrete PR-01 route-policy evidence surfaces include:

* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`  
* `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`  
* `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`  
* `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`  
* `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json.path_proof.txt`  
* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`  
* `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json.path_proof.txt`  
* `audit/qa/hde-epic036/route_policy_decision.log`  
* `audit/qa/hde-epic036/route_policy_decision.log.path_proof.txt`

Concrete PR-02 evidence-loop surfaces include:

* `docs/acceptance_map_epic036.json`  
* `docs/acceptance_map_epic036.json.path_proof.txt`  
* `audit/qa/hde-epic036/token_evidence_matrix.md`  
* `audit/qa/hde-epic036/token_evidence_matrix.md.path_proof.txt`  
* `audit/qa/hde-epic036/acceptance_map_viability.log`  
* `audit/qa/hde-epic036/acceptance_map_viability.log.path_proof.txt`  
* `audit/docdeltas/hde-epic036_doc_deltas.md`  
* `audit/docdeltas/hde-epic036_doc_deltas.md.path_proof.txt`  
* `audit/qa/hde-epic036/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic036/00_meta/doc_deltas.md.path_proof.txt`

This evidence family records route-policy classification and evidence-loop binding for HDE-EPIC036 only. It does not create QA PASS by implementation alone, OPS completion, PF09 status movement, HDE-FERM008 parent Done, epic closeout, full HumanDesignAPI v2 runtime conformance, public Reader change, public route change, public flag change, public payload or transport change, new HTTP home, app-side HumanDesignAPI credential ownership, raw payload persistence, or AI scope.

HDE-EPIC037 PR-01 through PR-05 HDAPI v2 BodyGraph-detail evidence surfaces (names-only).

The HDE-EPIC037 HDAPI v2 BodyGraph-detail evidence family is carried under:

* `artifacts/vendor/hdapi_v2/`  
* `audit/qa/hde-epic037/`  
* `audit/docdeltas/`  
* `docs/`

Concrete PR-01 field-sufficiency evidence surfaces include:

* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract.snapshot.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract_nonclaims.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json`  
* `audit/docdeltas/hde-epic037_doc_deltas.md`  
* `audit/qa/hde-epic037/00_meta/doc_deltas.md`

Concrete PR-02 adapter-mapping evidence surfaces include:

* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_adapter_negative_fixtures.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_no_raw_payload_persistence.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_public_reader_no_change.json`

Concrete PR-03 resolver and route-policy evidence surfaces include:

* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json`

Concrete PR-04 v2-to-compat evidence surfaces include:

* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_proof.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_two_run.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_pair_order.json`  
* `artifacts/vendor/hdapi_v2/hde_epic037_admin_public_boundary.json`

Concrete PR-05 parent-binding evidence surfaces include:

* `docs/acceptance_map_epic037.json`  
* `audit/qa/hde-epic037/token_evidence_matrix.md`  
* `audit/qa/hde-epic037/acceptance_map_viability.log`  
* `audit/qa/hde-epic037/parent_evidence_binding.log`  
* `audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md`  
* `audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md`

Sibling path-proof transcripts, Human Evidence Index entries, Machine Mirror records, hash sentinels, and canonical JSON expectations remain governed by the evidence homes by title. These HDE-EPIC037 surfaces record evidence location and binding posture only. They do not perform QA PASS, OPS completion by PR work, PF09 status movement, PF09 drainage, PO closeout, board update, merge action, PF-canon edit, epic closeout, production deployment, broad HumanDesignAPI v2 platform conformance beyond the bounded HDE-FERM008.7 through HDE-FERM008.11 evidence chain, public Reader change, public route change, public flag change, public payload or transport change, new HTTP home, app-side HumanDesignAPI ownership, raw secret persistence, raw request body persistence, raw response body persistence, uncontrolled raw vendor payload persistence, or AI scope.

**HDE-EPIC035 Live QA Pass 1 and closeout evidence surfaces (names-only).**

The HDE-EPIC035 Live QA Pass 1 and closeout evidence family is carried under:

* `audit/qa/hde-epic035/`

Concrete QA and closeout evidence surfaces include:

* `audit/qa/hde-epic035/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log`  
* `audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`  
* `audit/qa/hde-epic035/checks/po-001/primary.log`  
* `audit/qa/hde-epic035/checks/po-001/primary.log.path_proof.txt`  
* `audit/qa/hde-epic035/checks/po-014/primary.log`  
* `audit/qa/hde-epic035/checks/po-014/primary.log.path_proof.txt`  
* `audit/qa/hde-epic035/checks/qa-16-close-out-deliverables/primary.log`  
* `audit/qa/hde-epic035/checks/qa-16-close-out-deliverables/primary.log.path_proof.txt`  
* `audit/qa/hde-epic035/00_meta/discovery_artifact.md`  
* `audit/qa/hde-epic035/00_meta/qa_rca_doc_delta_summary.md`

This evidence family records QA and closeout-review surfaces only. It does not perform PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full runtime conformance, public expansion, raw payload persistence, or AI scope.

**HDE-EPIC037 Live QA, remediation, QA RCA, and closeout-review evidence surfaces (names-only).**

The HDE-EPIC037 Live QA and closeout-review evidence family is carried under:

* `audit/qa/hde-epic037/`

Concrete QA Pass 1, remediation, QA Pass 2, and closeout-review evidence surfaces include:

* `audit/qa/hde-epic037/checks/qa-00-runbook-preflight-and-discovery/primary.log`  
* `audit/qa/hde-epic037/checks/qa-00b-doc-delta-capture/primary.log`  
* `audit/qa/hde-epic037/checks/po-001/primary.log`  
* `audit/qa/hde-epic037/checks/po-002/primary.log`  
* `audit/qa/hde-epic037/checks/po-002-remediation-r1/primary.log`  
* `audit/qa/hde-epic037/checks/po-003/primary.log`  
* `audit/qa/hde-epic037/checks/po-004/primary.log`  
* `audit/qa/hde-epic037/checks/po-005/primary.log`  
* `audit/qa/hde-epic037/checks/po-006/primary.log`  
* `audit/qa/hde-epic037/checks/post-remediation-suite-rerun-r1/primary.log`  
* `audit/qa/hde-epic037/checks/po-007/primary.log`  
* `audit/qa/hde-epic037/checks/po-007/preflight_stdout.log`  
* `audit/qa/hde-epic037/checks/po-007/preflight_stderr.log`  
* `audit/qa/hde-epic037/checks/po-007/preflight_exit_code.txt`  
* `audit/qa/hde-epic037/checks/po-007/stdout.json`  
* `audit/qa/hde-epic037/checks/po-007/stderr.log`  
* `audit/qa/hde-epic037/checks/po-007/exit_code.txt`  
* `audit/qa/hde-epic037/checks/po-007/live_smoke_summary.json`  
* `audit/qa/hde-epic037/checks/po-007/summary_exit_code.txt`  
* `audit/qa/hde-epic037/checks/po-008/primary.log`  
* `audit/qa/hde-epic037/checks/po-009/primary.log`  
* `audit/qa/hde-epic037/checks/po-010/primary.log`  
* `audit/qa/hde-epic037/checks/po-011/primary.log`  
* `audit/qa/hde-epic037/checks/po-012/primary.log`  
* `audit/qa/hde-epic037/checks/qa-13-qa-rca-doc-delta-summary/primary.log`  
* `audit/qa/hde-epic037/checks/qa-13-qa-rca-doc-delta-summary/stdout.log`  
* `audit/qa/hde-epic037/checks/qa-13-qa-rca-doc-delta-summary/stderr.log`  
* `audit/qa/hde-epic037/checks/qa-13-qa-rca-doc-delta-summary/exit_code.txt`  
* `audit/qa/hde-epic037/checks/qa-13-qa-rca-doc-delta-summary/summary_exit_code.txt`  
* `audit/qa/hde-epic037/00_meta/qa_rca_doc_delta_summary.md`

Related doc-delta surfaces used by the HDE-EPIC037 QA closeout trace include:

* `audit/docdeltas/hde-epic037_doc_deltas.md`  
* `audit/qa/hde-epic037/00_meta/doc_deltas.md`

The preserved `po-002` failure receipt and the `po-002-remediation-r1` remediation receipt are both part of the HDE-EPIC037 QA evidence trail. The preserved failure receipt does not create an unresolved PF07 infrastructure defect when the remediation and rerun evidence remain repo-present under governed roots.

This evidence family records QA evidence, remediation evidence, QA RCA, and closeout-review surfaces only. It does not perform PO closeout, board update, PF edit, merge action, PF09 status movement, OPS completion, full runtime conformance, mapped-cache write persistence, production deployment, public expansion, app-side vendor credential ownership, raw payload persistence, raw secret persistence, or AI scope.

**HDE-EPIC036 Live QA and closeout-review evidence surfaces (names-only).**

The HDE-EPIC036 Live QA and closeout-review evidence family is carried under:

* `audit/qa/hde-epic036/`

Concrete Live QA and closeout-review evidence surfaces include:

* `audit/qa/hde-epic036/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic036/qa_step_logs_manifest.json.path_proof.txt`  
* `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log`  
* `audit/qa/hde-epic036/checks/step-0b-doc-delta-capture/primary.log.path_proof.txt`  
* `audit/qa/hde-epic036/checks/po-001/primary.log`  
* `audit/qa/hde-epic036/checks/po-001/primary.log.path_proof.txt`  
* `audit/qa/hde-epic036/checks/po-010/primary.log`  
* `audit/qa/hde-epic036/checks/po-010/primary.log.path_proof.txt`  
* `audit/qa/hde-epic036/checks/po-010/live_route_policy.log`  
* `audit/qa/hde-epic036/checks/po-010/live_route_policy.log.path_proof.txt`  
* `audit/qa/hde-epic036/checks/po-011/primary.log`  
* `audit/qa/hde-epic036/checks/po-011/primary.log.path_proof.txt`  
* `audit/qa/hde-epic036/checks/po-012/primary.log`  
* `audit/qa/hde-epic036/checks/po-012/primary.log.path_proof.txt`  
* `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log`  
* `audit/qa/hde-epic036/checks/qa-13-governed-evidence-gates/primary.log.path_proof.txt`  
* `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log`  
* `audit/qa/hde-epic036/checks/qa-14-close-out-deliverables/primary.log.path_proof.txt`  
* `audit/qa/hde-epic036/00_meta/discovery_artifact.md`  
* `audit/qa/hde-epic036/00_meta/discovery_artifact.md.path_proof.txt`  
* `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md`  
* `audit/qa/hde-epic036/00_meta/qa_rca_doc_delta_summary.md.path_proof.txt`  
* `audit/qa/hde-epic036/00_meta/hde_epic036_po010_moon_loop_remediation_action_report.md`  
* `audit/qa/hde-epic036/00_meta/hde_epic036_po011_po012_qa13_qa14_remediation_evidence_addendum.md`

The PO-010 live route-policy log is an open-rails QA evidence surface, not an OPS evidence root. Non-QA-root governed evidence refreshes referenced by HDE-EPIC036 QA were routed through PR work and remain governed by the evidence homes by title.

This evidence family records QA and closeout-review surfaces only. It does not perform PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full runtime conformance, public expansion, raw payload persistence, or AI scope.

**HDE-EPIC034 OPS-02 HDAPI v2 open-rails OPS evidence root (names-only).**

The bounded PO-authorized HDE-EPIC034 OPS-02 open-rails HumanDesignAPI v2 smoke evidence family is carried under:

* `audit/ops/hde-epic034/ops-02/`

Concrete OPS-02 evidence surfaces include:

* `audit/ops/hde-epic034/ops-02/commands.txt`  
* `audit/ops/hde-epic034/ops-02/stdout.log`  
* `audit/ops/hde-epic034/ops-02/stderr.log`  
* `audit/ops/hde-epic034/ops-02/exit_codes.txt`  
* `audit/ops/hde-epic034/ops-02/env_presence_redacted.json`  
* `audit/ops/hde-epic034/ops-02/request_summary.json`  
* `audit/ops/hde-epic034/ops-02/result_summary.json`  
* `audit/ops/hde-epic034/ops-02/files_sha256.txt`

This root records a bounded open-rails v2 smoke for HDE-EPIC034 OPS-02. It does not prove full HumanDesignAPI v2 runtime conformance, full vendor conformance, HDE-FERM008 parent completion, public Reader expansion, new public routes, new public flags, new HTTP homes, or AI runtime/evidence scope.

This root family is HDAPI-only and must not create OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, or AI-provider evidence paths.

**HDE-EPIC035 OPS-01 HDAPI v2 open-rails retained OPS evidence root (names-only).**

The bounded PO-authorized HDE-EPIC035 OPS-01 retained open-rails HumanDesignAPI evidence family is carried under:

* `audit/ops/hde-epic035/ops-01/`

The retained run-label evidence root is:

* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/`

Concrete retained OPS-01 evidence surfaces include:

* `audit/ops/hde-epic035/ops-01/ops_evidence_manifest.txt`  
* `audit/ops/hde-epic035/ops-01/files_sha256.txt`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/commands.txt`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stdout.log`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/stderr.log`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/exit_codes.txt`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/redacted_env_presence.json`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/request_summary.txt`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/result_summary.md`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/session_summary_and_evidence.md`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.json`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run.stderr`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.json`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/vendor_bodygraph_dry_run_no_version.stderr`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_commands.txt`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stdout.log`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_stderr.log`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/v2_charts_simple_result_summary.txt`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_classification.txt`  
* `audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final_repo_status.txt`

The manifest maps approved-plan deliverable names to retained evidence paths. This root records retained OPS evidence only. It does not prove QA PASS, PF09 status movement, epic closeout, full HumanDesignAPI v2 runtime conformance, public Reader change, new public route, app-side vendor credential ownership, raw payload persistence, or AI scope.

HDE-EPIC037 OPS-01 PO-produced open-rails runtime-smoke evidence root (names-only).

The HDE-EPIC037 OPS-01 PO-produced runtime-smoke evidence family is carried under:

* `audit/ops/hde-epic037/ops-hde-epic037-001/`

Concrete OPS-01 evidence surfaces include:

* `audit/ops/hde-epic037/ops-hde-epic037-001/commands.txt`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/stdout.log`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/stderr.log`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/exit_codes.txt`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/env_presence_redacted.json`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/request_summary.json`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/result_summary.json`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/adapter_mapping_result_summary.json`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/compat_path_result_summary.json`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/failure_classification.json`  
* `audit/ops/hde-epic037/ops-hde-epic037-001/files_sha256.txt`

The QA pointer for this OPS evidence is carried under:

* `audit/qa/hde-epic037/ops-hde-epic037-001/`

Concrete QA pointer surface:

* `audit/qa/hde-epic037/ops-hde-epic037-001/ops_evidence_pointer.md`

Sibling path-proof transcripts, index records, mirror records, and hash sentinels remain governed by the evidence homes by title. This OPS evidence root records PO-produced OPS evidence only. It does not prove QA PASS, PF09 status movement, parent Done, closeout, production deployment, public Reader expansion, app-side vendor ownership, raw vendor payload persistence, or AI scope.

**EPIC030 PR-01 normalization evidence family (names-only).** The governed PR-01 normalization evidence family is carried at:

* audit/qa/hde-epic030/pr-01/invalid\_viewer\_prefs.log  
* audit/qa/hde-epic030/pr-01/invalid\_viewer\_prefs.log.path\_proof.txt  
* audit/qa/hde-epic030/pr-01/normalization\_canonical\_compare.log  
* audit/qa/hde-epic030/pr-01/normalization\_canonical\_compare.log.path\_proof.txt  
* audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json  
* audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json.path\_proof.txt

**EPIC030 PR-02 dev-sampler evidence family (names-only).** The governed PR-02 dev-sampler evidence family is carried at:

* audit/qa/hde-epic030/pr-02/dev\_sampler\_http\_headers.txt  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_http\_headers.txt.path\_proof.txt  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_http\_body.json  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_http\_body.json.path\_proof.txt  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json.path\_proof.txt  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_seed\_only.json  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_seed\_only.json.path\_proof.txt

**EPIC030 PR-03 compat binding evidence family (names-only).** The governed PR-03 compat binding evidence family is carried at:

* audit/qa/hde-epic030/pr-03/category\_order\_binding.log  
* audit/qa/hde-epic030/pr-03/category\_order\_binding.log.path\_proof.txt  
* audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log  
* audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log.path\_proof.txt  
* audit/qa/hde-epic030/pr-03/compat\_parity\_binding.log  
* audit/qa/hde-epic030/pr-03/compat\_parity\_binding.log.path\_proof.txt

**EPIC030 PR-04 band-threshold evidence family (names-only).** The governed PR-04 band-threshold evidence family is carried at:

* audit/qa/hde-epic030/pr-04/band\_edges\_binding.log  
* audit/qa/hde-epic030/pr-04/band\_edges\_binding.log.path\_proof.txt  
* audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json  
* audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json.path\_proof.txt  
* audit/qa/hde-epic030/pr-04/band\_thresholds\_identity\_hash.txt  
* audit/qa/hde-epic030/pr-04/band\_thresholds\_identity\_hash.txt.path\_proof.txt

**EPIC030 PR-05 category-framework evidence family (names-only).** The governed PR-05 category-framework evidence family is carried at:

* audit/qa/hde-epic030/pr-05/category\_canonical\_compare.log  
* audit/qa/hde-epic030/pr-05/category\_canonical\_compare.log.path\_proof.txt  
* audit/qa/hde-epic030/pr-05/category\_framework\_binding.log  
* audit/qa/hde-epic030/pr-05/category\_framework\_binding.log.path\_proof.txt  
* audit/qa/hde-epic030/pr-05/per\_channel\_mechanics.json  
* audit/qa/hde-epic030/pr-05/per\_channel\_mechanics.json.path\_proof.txt

**EPIC030 PR-slice evidence versus close-pack posture (names-only).** The EPIC030 PR-01 through PR-05 evidence families above are implementation-slice evidence families under the epic QA tree. They do not replace, satisfy, or relocate the canonical epic close-pack artifacts. Close-pack artifacts remain governed by the canonical close-pack filename section below.

**EPIC031 PR-slice evidence surfaces (names-only).** The HDE-EPIC031 PR-01 through PR-03 evidence families are implementation-slice evidence families under governed audit and artifact roots. They do not replace, satisfy, or relocate canonical close-pack artifacts.

PR-01 — SAFE rails open posture and provider-gate policy proof:

* `artifacts/vendor/policies_pinned.md`  
* `artifacts/vendor/policies_pinned.md.path_proof.txt`  
* `artifacts/vendor/retry_after_parse.log`  
* `audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json`  
* `audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json.path_proof.txt`  
* `audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json`  
* `audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json.path_proof.txt`  
* `audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json`

PR-02 — SAFE rails observability and keys-only log posture:

* `audit/qa/hde-epic031/pr-02/bounded_label_observability.json`  
* `audit/qa/hde-epic031/pr-02/bounded_label_observability.json.path_proof.txt`  
* `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json`  
* `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json.path_proof.txt`  
* `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log`  
* `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log.path_proof.txt`  
* `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl`  
* `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl.path_proof.txt`  
* `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`  
* `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt.path_proof.txt`

PR-03 — SAFE rails governed evidence and indexing coherence:

* `audit/qa/hde-epic031/pr-03/evidence_family_map.json`  
* `audit/qa/hde-epic031/pr-03/evidence_family_map.json.path_proof.txt`  
* `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json`  
* `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json.path_proof.txt`  
* `audit/qa/hde-epic031/pr-03/evidence_refresh.log`  
* `audit/qa/hde-epic031/pr-03/evidence_refresh.log.path_proof.txt`

Shared restored DB-bridge evidence surfaces that must not be overwritten by PR-specific vendor evidence:

* `artifacts/logs/keys_only.sample.jsonl`  
* `artifacts/logs/keys_only.sample.jsonl.path_proof.txt`  
* `artifacts/ops/rails_open_scope.txt`  
* `artifacts/ops/rails_open_scope.txt.path_proof.txt`

**EPIC032 PR-slice evidence surfaces (names-only).** The HDE-EPIC032 PR-01 through PR-03 evidence families are implementation-slice evidence families under governed audit and artifact roots. They do not replace, satisfy, or relocate canonical close-pack artifacts.

PR-01 \- narrative router parity and evidence-indexing proof:

* `audit/gates/narratives/keys_10x4.table.json`  
* `audit/gates/narratives/keys_10x4.table.json.path_proof.txt`  
* `artifacts/narratives/router/parity_abba.log`  
* `artifacts/narratives/router/parity_abba.log.path_proof.txt`  
* `artifacts/narratives/router/cli_http_parity.log`  
* `artifacts/narratives/router/cli_http_parity.log.path_proof.txt`

PR-02 \- narrative registry diff, pack identity, and Doc-Delta evidence proof:

* `audit/gates/narratives/registry.diff.json`  
* `audit/gates/narratives/registry.diff.json.path_proof.txt`  
* `audit/gates/narratives/pack_identity.txt`  
* `audit/gates/narratives/pack_identity.txt.path_proof.txt`  
* `audit/docdeltas/hde-epic032_doc_deltas.md`  
* `audit/docdeltas/hde-epic032_doc_deltas.md.path_proof.txt`

PR-03 \- DB bridge fallback, bridge capability, and provider parity proof:

* `artifacts/db_bridge/adapter_selection.snapshot.json`  
* `artifacts/db_bridge/adapter_selection.snapshot.json.path_proof.txt`  
* `artifacts/db_bridge/provider_parity.proof.json`  
* `artifacts/db_bridge/provider_parity.proof.json.path_proof.txt`  
* `artifacts/runtime/env_connectivity.snapshot.json`  
* `artifacts/runtime/env_connectivity.snapshot.json.path_proof.txt`

**EPIC032 PR-04 and OPS-01 DB evidence surfaces (names-only).** The HDE-EPIC032 PR-04 and OPS-01 evidence families are governed evidence surfaces under artifact and audit roots. They do not replace, satisfy, or relocate canonical close-pack artifacts.

PR-04 \- non-dev typed DB failure and DB evidence-coherence proof:

* `artifacts/runtime/env_connectivity.nondev_failure.json`  
* `artifacts/runtime/env_connectivity.nondev_failure.json.path_proof.txt`  
* `artifacts/db_bridge/caps.snapshot.json.path_proof.txt`

PR-04 DB posture path-proof refresh surfaces:

* `artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt`  
* `artifacts/db/check_schema.txt.path_proof.txt`  
* `artifacts/db/ddl_fingerprint.json.path_proof.txt`  
* `artifacts/db/grants.txt.path_proof.txt`  
* `artifacts/db/partition_plan.txt.path_proof.txt`  
* `artifacts/db/partition_verify.log.path_proof.txt`  
* `artifacts/db/provider_parity/bridge.json.path_proof.txt`  
* `artifacts/db/provider_parity/direct.json.path_proof.txt`  
* `artifacts/db/provider_parity/summary.json.path_proof.txt`

OPS-01 \- DB provider parity closure packet and support artifacts:

* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json.path_proof.txt`  
* `audit/ops/hde-epic032/db-provider-parity/provider_parity.proof.json`  
* `audit/ops/hde-epic032/db-provider-parity/bridge_consistency_result.txt`  
* `audit/ops/hde-epic032/db-provider-parity/parity_scope_rationale.txt`  
* `audit/ops/hde-epic032/db-provider-parity/non_claims.txt`  
* `audit/ops/hde-epic032/db-provider-parity/ops01_final_report.txt`  
* `audit/ops/hde-epic032/db-provider-parity/created_files_sha256.txt`  
* `audit/ops/hde-epic032/db-provider-parity/commands.txt`  
* `audit/ops/hde-epic032/db-provider-parity/stdout.log`  
* `audit/ops/hde-epic032/db-provider-parity/stderr.log`  
* `audit/ops/hde-epic032/db-provider-parity/exit_codes.txt`  
* `audit/ops/hde-epic032/db-provider-parity/redacted_env_presence.txt`  
* `audit/ops/hde-epic032/db-provider-parity/adapter_selection.snapshot.json`  
* `audit/ops/hde-epic032/db-provider-parity/env_connectivity.snapshot.json`

**EPIC032 Live QA Step-0A, Step-0B, and po-001 through po-024 check-local evidence surfaces (names-only).** The governed check-local and supporting evidence surfaces for these HDE-EPIC032 QA checks are carried at:

Step-0A \- discovery posture and Live QA harness setup:

* `audit/qa/hde-epic032/00_meta/live_qa_harness.py`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/result.json`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/remediation_provenance.md`

Step-0B \- Doc Delta capture:

* `audit/docdeltas/hde-epic032_doc_deltas.md`  
* `audit/qa/hde-epic032/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log`  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/result.json`

HDE-EPIC032 QA step-log manifest surfaces:

* `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`

Step-0A bounded Moon Loop remediation provenance surfaces:

* `audit/qa/hde-epic032/00_meta/delta/`  
* `audit/qa/hde-epic032/00_meta/delta/changed_files.txt`  
* `audit/qa/hde-epic032/00_meta/delta/changed_files.sha256`  
* `audit/qa/hde-epic032/00_meta/delta/remediation_note.txt`  
* `audit/qa/hde-epic032/00_meta/delta/failure_signature.txt`

PO-001 \- Fermentation Pass 3 scope-boundary proof:

* `audit/qa/hde-epic032/checks/po-001/primary.log`  
* `audit/qa/hde-epic032/checks/po-001/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-001/result.json`

PO-002 \- narrative-router deterministic key-selection proof:

* `audit/qa/hde-epic032/checks/po-002/primary.log`  
* `audit/qa/hde-epic032/checks/po-002/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-002/result.json`

PO-003 \- keys-only router proof and public Reader non-expansion proof:

* `audit/qa/hde-epic032/checks/po-003/primary.log`  
* `audit/qa/hde-epic032/checks/po-003/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-003/result.json`

PO-004 \- narrative-router identity proof:

* `audit/qa/hde-epic032/checks/po-004/primary.log`  
* `audit/qa/hde-epic032/checks/po-004/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-004/result.json`

PO-005 \- registry diff and pack identity proof:

* `audit/qa/hde-epic032/checks/po-005/primary.log`  
* `audit/qa/hde-epic032/checks/po-005/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-005/result.json`

PO-006 \- registry non-overclaim proof:

* `audit/qa/hde-epic032/checks/po-006/primary.log`  
* `audit/qa/hde-epic032/checks/po-006/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-006/result.json`

PO-007 \- registry and doc-delta identity proof:

* `audit/qa/hde-epic032/checks/po-007/primary.log`  
* `audit/qa/hde-epic032/checks/po-007/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-007/result.json`

PO-008 \- DB bridge and provider parity proof-chain proof:

* `audit/qa/hde-epic032/checks/po-008/primary.log`  
* `audit/qa/hde-epic032/checks/po-008/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-008/result.json`

PO-009 \- OPS evidence non-claim proof:

* `audit/qa/hde-epic032/checks/po-009/primary.log`  
* `audit/qa/hde-epic032/checks/po-009/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-009/result.json`

PO-010 \- DB bridge structural selection-order proof:

* `audit/qa/hde-epic032/checks/po-010/primary.log`  
* `audit/qa/hde-epic032/checks/po-010/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-010/result.json`

PO-010 Moon Loop remediation evidence surfaces:

* `audit/qa/hde-epic032/remediation/moon_loop/patch.diff`  
* `audit/qa/hde-epic032/remediation/moon_loop/boundary_classification.md`

PO-011 \- generated-proof failure mode proof:

* `audit/qa/hde-epic032/checks/po-011/primary.log`  
* `audit/qa/hde-epic032/checks/po-011/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-011/result.json`

PO-012 \- supportability and non-overclaim proof:

* `audit/qa/hde-epic032/checks/po-012/primary.log`  
* `audit/qa/hde-epic032/checks/po-012/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-012/result.json`

PO-013 \- evidence-index coherence proof:

* `audit/qa/hde-epic032/checks/po-013/primary.log`  
* `audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-013/result.json`

PO-014 \- human and machine evidence loci proof:

* `audit/qa/hde-epic032/checks/po-014/primary.log`  
* `audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-014/result.json`

PO-015 \- generated-proof command-coherence proof:

* `audit/qa/hde-epic032/checks/po-015/primary.log`  
* `audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-015/result.json`

PO-016 \- DB proof-label token-boundary proof:

* `audit/qa/hde-epic032/checks/po-016/primary.log`  
* `audit/qa/hde-epic032/checks/po-016/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-016/result.json`

PO-017 \- bridge fallback-scope proof:

* `audit/qa/hde-epic032/checks/po-017/primary.log`  
* `audit/qa/hde-epic032/checks/po-017/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-017/result.json`

PO-018 \- active evidence-family and PF09 drainage non-claim proof:

* `audit/qa/hde-epic032/checks/po-018/primary.log`  
* `audit/qa/hde-epic032/checks/po-018/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-018/result.json`

PO-019 \- reused-foundation posture proof:

* `audit/qa/hde-epic032/checks/po-019/primary.log`  
* `audit/qa/hde-epic032/checks/po-019/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-019/result.json`

PO-020 \- truth-class separation proof:

* `audit/qa/hde-epic032/checks/po-020/primary.log`  
* `audit/qa/hde-epic032/checks/po-020/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-020/result.json`

PO-021 \- vendor-version runtime non-claim proof:

* `audit/qa/hde-epic032/checks/po-021/primary.log`  
* `audit/qa/hde-epic032/checks/po-021/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-021/result.json`

PO-022 \- live-provider non-claim proof:

* `audit/qa/hde-epic032/checks/po-022/primary.log`  
* `audit/qa/hde-epic032/checks/po-022/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-022/result.json`

PO-023 \- public Reader non-expansion proof:

* `audit/qa/hde-epic032/checks/po-023/primary.log`  
* `audit/qa/hde-epic032/checks/po-023/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-023/result.json`

PO-024 \- proof-only Live QA role proof:

* `audit/qa/hde-epic032/checks/po-024/primary.log`  
* `audit/qa/hde-epic032/checks/po-024/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/po-024/result.json`

**EPIC031 Live QA Step-0A, Step-0B, and po-001 through po-018 check-local evidence surfaces (names-only).** The governed check-local and supporting evidence surfaces for these HDE-EPIC031 QA checks are carried at:

Step-0A \- discovery posture and harness setup:

* `audit/qa/hde-epic031/00_meta/live_qa_harness.py`  
* `audit/qa/hde-epic031/checks/step-0a-discovery/primary.log`  
* `audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json`

Step-0A accepted discovery-path posture:

* `audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json` is the accepted current-state discovery path for HDE-EPIC031 Step-0A.  
* `audit/qa/hde-epic031/00_meta/discovery.json` is recorded as framing-only drift for this epic and is not the accepted Step-0A current-state discovery path.

Step-0B \- doc-delta capture:

* `audit/docdeltas/hde-epic031_doc_deltas.md`  
* `audit/qa/hde-epic031/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic031/checks/step-0b-doc-delta/primary.log`

PO-001 \- Fermentation first-slice scope boundary:

* `audit/qa/hde-epic031/checks/po-001/primary.log`  
* `audit/qa/hde-epic031/checks/po-001/result.json`

PO-002 \- closed-by-default provider access with explicit bounded opening:

* `audit/qa/hde-epic031/checks/po-002/primary.log`  
* `audit/qa/hde-epic031/checks/po-002/result.json`

PO-003 \- deterministic typed provider refusal when external access is not allowed:

* `audit/qa/hde-epic031/checks/po-003/primary.log`  
* `audit/qa/hde-epic031/checks/po-003/result.json`

PO-004 \- retry and backoff proof check:

* `audit/qa/hde-epic031/checks/po-004/primary.log`  
* `audit/qa/hde-epic031/checks/po-004/result.json`

PO-005 \- 429 and Retry-After proof check:

* `audit/qa/hde-epic031/checks/po-005/primary.log`  
* `audit/qa/hde-epic031/checks/po-005/result.json`

PO-006 \- keys-only redaction proof check:

* `audit/qa/hde-epic031/checks/po-006/primary.log`  
* `audit/qa/hde-epic031/checks/po-006/result.json`

HDE-EPIC031 Moon Loop remediation evidence surfaces:

* `audit/qa/hde-epic031/remediation/moon_loop/patch.diff`  
* `audit/qa/hde-epic031/remediation/moon_loop/changed_files.txt`  
* `audit/qa/hde-epic031/00_meta/doc_deltas.md`

PO-007 \- sensitive-provider-data absence and live-vendor-call prohibition proof:

* `audit/qa/hde-epic031/checks/po-007/primary.log`  
* `audit/qa/hde-epic031/checks/po-007/result.json`

PO-008 \- PR-03 evidence coherence and Moon Loop remediation proof:

* `audit/qa/hde-epic031/checks/po-008/primary.log`  
* `audit/qa/hde-epic031/checks/po-008/result.json`

PO-009 \- machine mirror and evidence family map alignment proof:

* `audit/qa/hde-epic031/checks/po-009/primary.log`  
* `audit/qa/hde-epic031/checks/po-009/result.json`

PO-010 \- generated-proof fail-closed proof:

* `audit/qa/hde-epic031/checks/po-010/primary.log`  
* `audit/qa/hde-epic031/checks/po-010/result.json`

PO-011 \- acceptance-claim boundary proof:

* `audit/qa/hde-epic031/checks/po-011/primary.log`  
* `audit/qa/hde-epic031/checks/po-011/result.json`

PO-012 \- active Fermentation subtask support proof:

* `audit/qa/hde-epic031/checks/po-012/primary.log`  
* `audit/qa/hde-epic031/checks/po-012/result.json`

PO-013 \- reused-foundation history-only proof:

* `audit/qa/hde-epic031/checks/po-013/primary.log`  
* `audit/qa/hde-epic031/checks/po-013/result.json`

PO-014 \- prior-log and readiness-separation proof:

* `audit/qa/hde-epic031/checks/po-014/primary.log`  
* `audit/qa/hde-epic031/checks/po-014/result.json`

PO-015 \- truth-class and documentation-drainage separation proof:

* `audit/qa/hde-epic031/checks/po-015/primary.log`  
* `audit/qa/hde-epic031/checks/po-015/result.json`

PO-016 \- vendor-version runtime non-claim proof:

* `audit/qa/hde-epic031/checks/po-016/primary.log`  
* `audit/qa/hde-epic031/checks/po-016/result.json`

PO-017 \- live-vendor behavior non-claim proof:

* `audit/qa/hde-epic031/checks/po-017/primary.log`  
* `audit/qa/hde-epic031/checks/po-017/result.json`

PO-018 \- Live QA proof-only boundary proof:

* `audit/qa/hde-epic031/checks/po-018/primary.log`  
* `audit/qa/hde-epic031/checks/po-018/result.json`

**EPIC031 QA manifest and close-pack caveat surfaces (names-only).** HDE-EPIC031 carries the following additional surfaces:

* `audit/qa/hde-epic031/qa_step_logs_manifest.json`  
* `audit/EPIC-031_close_report.md`  
* `audit/EPIC-031_MANIFEST.json`

The QA step-log manifest is a proven QA evidence-family surface for this epic. The close-report and manifest paths are recorded as framing-only caveat surfaces in this retrospective and do not establish completed close-pack proof by themselves.

**EPIC030 Live QA po-001 through po-017 check-local evidence surfaces (names-only).** The governed check-local evidence surfaces for these HDE-EPIC030 QA checks are carried at:

PO-001 — surface inventory and no public widening check:

* `audit/qa/hde-epic030/checks/po-001/primary.log`  
* `audit/qa/hde-epic030/checks/po-001/surface_inventory.txt`  
* `audit/qa/hde-epic030/checks/po-001/exit_code.txt`

PO-002 — zero-weight user intent and sampler handoff check:

* `audit/qa/hde-epic030/checks/po-002/primary.log`  
* `audit/qa/hde-epic030/checks/po-002/pytest_stdout.log`  
* `audit/qa/hde-epic030/checks/po-002/generator_stdout.log`  
* `audit/qa/hde-epic030/checks/po-002/pytest_rc.txt`  
* `audit/qa/hde-epic030/checks/po-002/generator_rc.txt`  
* `audit/qa/hde-epic030/checks/po-002/exit_code.txt`

PO-003 — viewer-preference normalization proof check:

* `audit/qa/hde-epic030/checks/po-003/primary.log`

PO-004 — dev sampler harness proof check:

* `audit/qa/hde-epic030/checks/po-004/primary.log`

PO-005 — compatibility identity and parity proof check:

* `audit/qa/hde-epic030/checks/po-005/primary.log`

PO-006 — public compatibility output and OPS-02 proof validation:

* `audit/qa/hde-epic030/checks/po-006/primary.log`  
* `audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt`  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.json`  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.stderr`  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation_rc.txt`  
* `audit/qa/hde-epic030/checks/po-006/pytest_rc.txt`  
* `audit/qa/hde-epic030/checks/po-006/exit_code.txt`

PO-007 — threshold ownership proof:

* `audit/qa/hde-epic030/checks/po-007/primary.log`  
* `audit/qa/hde-epic030/checks/po-007/threshold_ownership.txt`  
* `audit/qa/hde-epic030/checks/po-007/generator_stdout.log`  
* `audit/qa/hde-epic030/checks/po-007/generator_stderr.log`  
* `audit/qa/hde-epic030/checks/po-007/generator_rc.txt`  
* `audit/qa/hde-epic030/checks/po-007/preflight.log`  
* `audit/qa/hde-epic030/checks/po-007/exit_code.txt`

PO-008 — band tuning comparison and identity proof:

* `audit/qa/hde-epic030/checks/po-008/primary.log`  
* `audit/qa/hde-epic030/checks/po-008/status_gate.log`  
* `audit/qa/hde-epic030/checks/po-008/preflight.log`  
* `audit/qa/hde-epic030/checks/po-008/pytest_stdout.log`

PO-009 — category framework binding proof:

* `audit/qa/hde-epic030/checks/po-009/primary.log`  
* `audit/qa/hde-epic030/checks/po-009/exit_code.txt`  
* `audit/qa/hde-epic030/checks/po-009/generator_rc.txt`  
* `audit/qa/hde-epic030/checks/po-009/pytest_rc.txt`  
* `audit/qa/hde-epic030/checks/po-009/pytest_stdout.log`

PO-010 — fail-closed proof visibility:

* `audit/qa/hde-epic030/checks/po-010/primary.log`  
* `audit/qa/hde-epic030/checks/po-010/exit_code.txt`  
* `audit/qa/hde-epic030/checks/po-010/fail_closed_visibility.txt`  
* `audit/qa/hde-epic030/checks/po-010/pytest_rc.txt`  
* `audit/qa/hde-epic030/checks/po-010/pytest_stdout.log`

PO-011 — PR-slice traceability proof:

* `audit/qa/hde-epic030/checks/po-011/primary.log`  
* `audit/qa/hde-epic030/checks/po-011/traceability_summary.json`  
* `audit/qa/hde-epic030/checks/po-011/exit_code.txt`

PO-012 — reused-history classification proof:

* `audit/qa/hde-epic030/checks/po-012/primary.log`  
* `audit/qa/hde-epic030/checks/po-012/reused_history_classification.txt`

PO-013 — source-of-truth and drainage separation proof:

* `audit/qa/hde-epic030/checks/po-013/primary.log`  
* `audit/qa/hde-epic030/checks/po-013/source_of_truth_posture.txt`

PO-014 — all-slice coherence proof:

* `audit/qa/hde-epic030/checks/po-014/primary.log`  
* `audit/qa/hde-epic030/checks/po-014/all_slice_coherence.json`  
* `audit/qa/hde-epic030/checks/po-014/exit_code.txt`

PO-015 — baseline execution context and discovery proof:

* `audit/qa/hde-epic030/checks/po-015/primary.log`  
* `audit/qa/hde-epic030/checks/po-015/discovery.json`  
* `audit/qa/hde-epic030/checks/po-015/discovery_validation.txt`

PO-016 — final QA interpretation and RCA proof:

* `audit/qa/hde-epic030/checks/po-016/primary.log`  
* `audit/EPIC-030_QA_RCA.md`

PO-017 — documentation-drainage non-blocker proof:

* `audit/qa/hde-epic030/checks/po-017/primary.log`  
* `audit/qa/hde-epic030/checks/po-017/documentation_drainage_posture.txt`

EPIC030 Step-0B doc-delta precondition evidence surfaces:

* `audit/qa/hde-epic030/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic030/00_meta/step_0b_primary.log`  
* `audit/docdeltas/hde-epic030_doc_deltas.md`

**EPIC030 po-006 remediation OPS adoption evidence surfaces (names-only).** The governed OPS adoption evidence surfaces for the po-006 remediation path are carried at:

OPS-01 discovery and command-proof surfaces:

* `audit/ops/hde-epic030/ops-01/commands.txt`  
* `audit/ops/hde-epic030/ops-01/python_version.txt`  
* `audit/ops/hde-epic030/ops-01/python_version.stderr`  
* `audit/ops/hde-epic030/ops-01/pytest_version.txt`  
* `audit/ops/hde-epic030/ops-01/pytest_version.stderr`  
* `audit/ops/hde-epic030/ops-01/grep_path.txt`  
* `audit/ops/hde-epic030/ops-01/grep_path.stderr`  
* `audit/ops/hde-epic030/ops-01/hdctl_path.txt`  
* `audit/ops/hde-epic030/ops-01/hdctl_path.stderr`  
* `audit/ops/hde-epic030/ops-01/hdctl_help.txt`  
* `audit/ops/hde-epic030/ops-01/hdctl_help.stderr`  
* `audit/ops/hde-epic030/ops-01/showcompat_help.txt`  
* `audit/ops/hde-epic030/ops-01/showcompat_help.stderr`  
* `audit/ops/hde-epic030/ops-01/env_presence.json`  
* `audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt`  
* `audit/ops/hde-epic030/ops-01/discovery_summary.md`  
* `audit/ops/hde-epic030/ops-01/files_sha256.txt`

OPS-02 controlled vendor-smoke surfaces:

* `audit/ops/hde-epic030/ops-02/vendor_command.txt`  
* `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json`  
* `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`  
* `audit/ops/hde-epic030/ops-02/target_disposition.md`  
* `audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md`  
* `audit/ops/hde-epic030/ops-02/request_summary.txt`  
* `audit/ops/hde-epic030/ops-02/stdout.json`  
* `audit/ops/hde-epic030/ops-02/stderr.log`  
* `audit/ops/hde-epic030/ops-02/exit_code.txt`  
* `audit/ops/hde-epic030/ops-02/stdout_parse_validation.md`  
* `audit/ops/hde-epic030/ops-02/stdout.json.sha256`  
* `audit/ops/hde-epic030/ops-02/execution_classification.md`  
* `audit/ops/hde-epic030/ops-02/result_summary.md`  
* `audit/ops/hde-epic030/ops-02/pfcanon_ops02_completion_matrix.md`  
* `audit/ops/hde-epic030/ops-02/files_sha256.txt`  
* `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`

**EPIC030 OPS-03 close-pack surfacing evidence surfaces (names-only).** The governed OPS-03 evidence-packaging and close-pack surfacing surfaces are carried at:

OPS-03 command, output, validation, inventory, and checksum surfaces:

* `audit/ops/hde-epic030/ops-03/commands.txt`  
* `audit/ops/hde-epic030/ops-03/commands_prev_invalid.txt`  
* `audit/ops/hde-epic030/ops-03/stdout.log`  
* `audit/ops/hde-epic030/ops-03/stderr.log`  
* `audit/ops/hde-epic030/ops-03/exit_codes.txt`  
* `audit/ops/hde-epic030/ops-03/final_evidence_inventory.md`  
* `audit/ops/hde-epic030/ops-03/final_evidence_inventory.md.path_proof.txt`  
* `audit/ops/hde-epic030/ops-03/final_validation.log`  
* `audit/ops/hde-epic030/ops-03/created_files_sha256.txt`

OPS-03 bound close-pack and support-family surfaces:

* `audit/EPIC-030_close_report.md`  
* `audit/EPIC-030_close_report.md.path_proof.txt`  
* `audit/EPIC-030_MANIFEST.json`  
* `audit/EPIC-030_MANIFEST.json.path_proof.txt`  
* `audit/EPIC-030_QA_RCA.md`  
* `docs/acceptance_map_epic030.json`  
* `audit/qa/hde-epic030/token_evidence_matrix.md`  
* `audit/qa/hde-epic030/qa_step_logs_manifest.json`  
*   
* `audit/docdeltas/hde-epic030_doc_deltas.md`  
* `audit/docdeltas/hde-epic030_drain_targets.md`

**Parity rule.** CI enforces 1:1 parity (human index ↔ machine mirror) for governed evidence records.

.

### Fixed-path evidence surfaces (names-only; binding correctness)

Some acceptance claims are path-sensitive and have a single canonical governed evidence surface. Where a fixed canonical path exists, any plan/matrix/index/mirror binding to a different path is a mechanical blocker and must be corrected (not interpreted).

### **Evidence index snapshot (canonical surface)**

The only valid governed evidence surface for evidence index snapshot artifacts is:

* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`

* `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`

Bindings for evidence index snapshot evidence MUST reference this governed surface only. The EPIC-local variant under `audit/qa/hde-epic<NNN>/.../evidence_index_snapshot.json` is not a closure-required canonical surface; snapshot copies may exist as run-local convenience, but the canonical evidence surface and index binding remain the governed `audit/gates/evidence_index_snapshot/...` path above.

### **Determinism predicate surfaces lock (routing-only)**

Determinism remediation predicates for D16–D18 MUST validate the canonical emitted evidence surfaces recorded in this section (D16: topology orientation demo; D17: determinism env pins log; D18: sanity log) and MUST NOT require wrapper bundles or extra non-canon marker lines.

**D17 env pins log predicate shape (routing-only).** The first JSON record MUST be a compact object with keys: `env` (object), `status` (string), `suites` (array). Validators MUST NOT require schema, rails, or other wrapper fields.

**D18 sanity log predicate markers (routing-only).** Validators MUST accept the canonical structure (header `sanity_pipeline`, then `env:`, then one-or-more `check ...`, ending with `summary:PASS`) and MUST NOT require `run:sanity-pipeline` or `env_pins:` marker lines.

**Path-proof naming is locked.** For these canonical surfaces, the path-proof MUST be the full filename plus `.path_proof.txt` (including the original extension), for example `env_pins.log.path_proof.txt` (not `env_pins.path_proof.txt`).

**Citation posture (routing-only).** PF20 — HDE-Phased-Epics MUST NOT be cited to define evidence surface paths, evidence shapes, or remediation predicate targets. Plans/remediations MUST cite PF10 — HDE-Build Notes, PF09 — HDE-Build Checklist, PF06 — Epic-Process-Guide, PF12 — HDE-Schemas & Artifacts, PF19 — Glow QA Guide, and PF04 — HDE-Governance (as applicable) for those requirements.

### Determinism env pins (canonical surface)

The only valid governed evidence surface for determinism env pins is:

* `audit/gates/determinism/env_pins.log`  
* `audit/gates/determinism/env_pins.log.path_proof.txt`

Bindings for determinism env pins MUST reference this governed surface only. Snapshot copies under epic QA trees are allowed as run-local convenience, but the canonical evidence surface and index binding remain the governed `audit/gates/determinism/...` path above.

**Note (pins).** Canonical determinism pins are the locale/timezone pins listed in the governing sections referenced by the QA posture. PYTHONHASHSEED is not part of the canonical pins set and must not be required for plan approval or execution.

### **Sanity log (canonical surface)**

The only valid governed evidence surface for sanity log artifacts is:

* `artifacts/sanity/sanity.log`

* `artifacts/sanity/sanity.log.path_proof.txt`

Bindings for sanity log evidence MUST reference this governed surface only. Snapshot copies under epic QA trees are allowed as run-local convenience, but the canonical evidence surface and index binding remain the governed `artifacts/sanity/...` path above.

### **Canonical JSON gates (canonical surface)**

The authoritative governed evidence surface for canonical JSON gate acceptance binding is:

* `audit/gates/json_gate/canonical/`

Legacy / transition-only variants (non-binding; retained for backward compatibility):

* `audit/gates/canonical_json/` (legacy family; evidence index / governed outputs may still include this family during transition)

* `audit/gates/canonical/` (legacy folder; retained for backward compatibility)

Legacy canonical\_json gate records and logs (names-only; non-binding):

* `audit/gates/canonical_json/canonical_json.gate.json`

* `audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt`

* `audit/gates/canonical_json/json_canon_compare.log`

* `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`

* `audit/gates/canonical_json/json_canonical_check.log`

* `audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`

Flat canonical JSON gate snapshot (names-only; transition/non-binding):

* `audit/gates/canonical_json_gate.json`

No dual-home acceptance binding: acceptance maps, token/evidence matrices, and close-pack manifests MUST bind only to `audit/gates/json_gate/canonical/` for canonical JSON gate evidence. Evidence Index/Mirror entries may also track legacy `audit/gates/canonical_json/` artifacts during transition, but they are non-binding and MUST NOT be treated as a second source of truth.

Canonical artifacts under this root (names-only; minimum family):

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`

* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`

* `audit/gates/json_gate/canonical/json_gate_structured_record.json`

* (plus corresponding path proofs as defined by the owning canon)

### `/internal/version` evidence bundle (canonical root; names-only)

The governed evidence bundle for `/internal/version` is rooted at: `artifacts/ops/internal_version/`

Endpoint Catalog inventory file (names-only; symlink surface):

* `docs/ENDPOINTS_CATALOG.json`

* `artifacts/audit/ENDPOINTS_CATALOG.json`

* `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`

* `docs/ENDPOINTS_CATALOG.json.sha256`

* `docs/ENDPOINTS_CATALOG.json.sha256.path_proof.txt`

* `docs/ENDPOINTS_CATALOG.json.path_proof.txt`

Additional Endpoint Catalog surfaces (names-only):

* `docs/endpoint_catalog.json`

* `docs/endpoint_catalog.json.sha256`

* `docs/endpoint_catalog.json.path_proof.txt`

* `docs/endpoint_catalog.json.sha256.path_proof.txt`

* `artifacts/endpoint_catalog.json`

* `artifacts/endpoint_catalog.json.sha256`

* `artifacts/endpoint_catalog.json.path_proof.txt`

* `artifacts/endpoint_catalog.json.sha256.path_proof.txt`

Additional EPIC026 Endpoint Catalog source surfaces (names-only):

* `docs/ENDPOINTS_CATALOG.md`

* `audit/ENDPOINTS_CATALOG.json`

* `audit/ENDPOINTS_CATALOG.sha256`

Canonical artifact family under this root (names-only):

* `artifacts/ops/internal_version/body_get.json`  
* `artifacts/ops/internal_version/body_get.sha256`  
* `artifacts/ops/internal_version/headers_get.txt`  
* `artifacts/ops/internal_version/headers_head.txt`  
* `artifacts/ops/internal_version/headers_cond_if_none_match.txt`  
* `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`  
* `artifacts/ops/internal_version/request_chain_manifest.json`  
* `artifacts/ops/internal_version/two_run_identity.log`

**Sidecar discipline (names-only).** Canonical artifacts above MUST have co-located sibling path-proofs: `<file>.path_proof.txt`. Where checksum sidecars exist (example: `body_get.sha256`), they also require sibling path-proofs. `request_chain_manifest.json` MUST have `request_chain_manifest.json.path_proof.txt` as a sibling.

**Deprecated / legacy internal\_version variants (compat-only; MUST NOT be treated as canonical evidence surfaces):**

* `artifacts/ops/internal_version/conditional_headers.json`  
* `artifacts/ops/internal_version/conditional_headers.sha256`  
* `artifacts/ops/internal_version/cond_if_none_match_headers.txt`  
* `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`

**Indexing note (titles-only).** Evidence indexing is single-homed elsewhere; index entries must reference only the canonical artifact family listed above. Deprecated variants are transition-only and are not second sources of truth.

### **Endpoint Catalog checksum sidecar note (names-only)**

The checksum sidecar `docs/ENDPOINTS_CATALOG.json.sha256` records the checksum line against the `docs/ENDPOINTS_CATALOG.json` relative path (not a repo-root path).

### **`/reader` A7 proof artifacts (EPIC025; names-only)**

Canonical proof artifacts under `artifacts/proofs/` (plus sibling path-proofs `<file>.path_proof.txt`):

* `artifacts/proofs/endpoints_env_gate_proof.log`

* `artifacts/proofs/success_get.txt`

* `artifacts/proofs/success_head.txt`

* `artifacts/proofs/success_304.txt`

* `artifacts/proofs/success_writers_errors.txt`

* `artifacts/proofs/reader_route_proof.json`  
* `artifacts/proofs/success_encoding_invariance.txt`

### **CLI showcompat artifacts (EPIC025; names-only)**

* `artifacts/cli/showcompat/args.json`

* `artifacts/cli/showcompat/args.json.path_proof.txt`

* `artifacts/cli/showcompat/stdout.json`

### **CLI conjunction artifacts (EPIC026; names-only)**

* `artifacts/audit/cli/pair.json`

* `artifacts/audit/cli/pair.json.path_proof.txt`

* `artifacts/audit/cli/pair_ba.json`

* `artifacts/audit/cli/pair_ba.json.path_proof.txt`

* `artifacts/audit/cli/showcompat_ab.json`

* `artifacts/audit/cli/showcompat_ab.json.path_proof.txt`

* `artifacts/audit/cli/showcompat_ba.json`

* `artifacts/audit/cli/showcompat_ba.json.path_proof.txt`

* `artifacts/cli/abba_sidecar.json`

* `artifacts/cli/abba_sidecar.json.path_proof.txt`

* `artifacts/cli/out.json`

* `artifacts/cli/out.json.path_proof.txt`

* `artifacts/cli/out_ba.json`

* `artifacts/cli/out_ba.json.path_proof.txt`

### CLI installability, help, and parity artifacts (EPIC027; names-only)

* `artifacts/cli/install/entrypoints.txt`  
* `artifacts/cli/install/installability_summary.json`  
* `artifacts/cli/help/hdctl_help.txt`  
* `artifacts/cli/help/showcompat_help.txt`  
* `artifacts/cli/help/reject_nonjson.txt`  
* `artifacts/cli/ab.json`  
* `artifacts/cli/ba.json`  
* `artifacts/cli/summary.json`

### CLI serializer-coupling proof artifacts (EPIC028; names-only)

* `artifacts/cli/guards/emitter_symbol_proof.txt`  
* `artifacts/cli/guards/emitter_symbol_proof.txt.path_proof.txt`  
* `artifacts/cli/guards/serializer_grep_guard.log`  
* `artifacts/cli/reader_cli_parity.bytes`

### Compat identity-hash and narrative-linkage artifacts (EPIC027 / EPIC030 PR-03; names-only)

* `artifacts/compat/AB.json`  
* `artifacts/compat/AB.json.path_proof.txt`  
* `artifacts/compat/BA.json`  
* `artifacts/compat/BA.json.path_proof.txt`  
* `artifacts/compat/identity_hash.txt`  
* `artifacts/narratives/key_table_10x2.snapshot.json`  
* `artifacts/narratives/key_table_10x2.snapshot.json.path_proof.txt`

### Bridge adapter-selection snapshot artifact (EPIC027; names-only)

* `artifacts/db_bridge/adapter_selection.snapshot.json`

### Writer evidence artifacts (EPIC027; names-only)

* `artifacts/writer/conjunction_write_readback.log`

* `artifacts/writer/conjunction_write_readback.log.path_proof.txt`

* `artifacts/writer/conjunction_writer_summary.json`

* `artifacts/writer/conjunction_writer_summary.json.path_proof.txt`

### Release identity (EPIC022; canonical surfaces)

Release identity evidence surfaces (names-only; canonical paths):

* `artifacts/math/release_id.txt`  
* `artifacts/math/release_id_recompute.log`  
* `artifacts/math/freeze_pack_manifest.json`

**Notes (routing-only).** The Freeze-Pack Manifest single source of truth remains `catalog/manifest.json`; `artifacts/math/freeze_pack_manifest.json` is an evidence copy and MUST NOT act as an alternate manifest contract. Evidence-only summaries (for example `manifest_snapshot.json`) MUST NOT be used as identity inputs.

### Epic close-pack filenames and QA root normalization (names-only; updated)

To prevent naming ambiguity and parallel spellings, governed epic close-pack artifacts and QA roots use canonical path patterns.

**Epic close-pack artifacts (canonical filenames).** Epic close-pack artifacts MUST use:

* `audit/EPIC-<NNN>_close_report.md`  
* `audit/EPIC-<NNN>_MANIFEST.json`

**Close-pack path proofs (names-only).** Each close-pack artifact above has a sibling path-proof file:

* `audit/EPIC-<NNN>_close_report.md.path_proof.txt`

* `audit/EPIC-<NNN>_MANIFEST.json.path_proof.txt`

where `<NNN>` is a zero-padded 3-digit epic number (example: 022).

**Conditional close-pack QA RCA artifact (names-only).** If the QA RCA and Doc Delta summary is maintained as a separate governed artifact rather than embedded inside the close report, use:

* `audit/EPIC-<NNN>_QA_RCA.md`

When externalized, the epic close report references this artifact by path.

**Close-pack proof completeness (clarification).** When a plan, deliverables report, or closure review asserts the close-pack pair exists, it MUST also explicitly assert the existence of the two `.path_proof.txt` siblings listed above. A close-pack pair without these two path proofs is not a complete close-pack proof.

These two files are the deterministic path-of-record for epic close-pack. Do not relocate them under other trees (for example `audit/qa/**` or `artifacts/**`). Additional copies elsewhere are convenience-only and MUST NOT be used for acceptance binding.

Examples of convenience-only close-pack support artifacts (names-only; MUST NOT be used for acceptance binding):

* `docs/epic025_close_pack/endpoint_catalog_sha256.txt`

* `docs/epic025_close_pack/endpoint_catalog_sha256.txt.path_proof.txt`

* `docs/epic025_close_pack/generate_close_pack.stdout.txt`

* `docs/epic025_close_pack/generate_close_pack.stdout.txt.path_proof.txt`

Additional convenience-only close-pack surfaces (names-only; MUST NOT be used for acceptance binding):

* `audit/EPIC-<NNN>_close_pack.md`

* `audit/qa/hde-epic<NNN>/close_pack/`

**Epic QA root directory (canonical pattern).** Epic QA roots MUST be lower-case and MUST use:

* `audit/qa/hde-epic<NNN>/` (example: `audit/qa/hde-epic022/`)

Plans and implementations MUST NOT introduce alternate spellings for the same epic in paths. If legacy artifacts exist under non-canonical names, treat them as deprecated and do not create new artifacts under deprecated patterns.

**Run-id discipline (updated posture).** Run-id discipline is not a correctness mechanism. Per-run directory nesting MAY exist for convenience/history, but it is optional and non-canon. The canonical evidence posture is epic-level current-state indexing by `check_id` under the epic QA root.

### **QA root summary artifacts (optional; names-only)**

Some workflows may also emit top-level QA summary artifacts under `audit/qa/` (outside the epic-scoped QA root). These artifacts are convenience-only and MUST NOT replace canonical close-pack artifacts under `audit/EPIC-<NNN>_*` or canonical gate outputs under `audit/gates/`.

* `audit/qa/run.json`

* `audit/qa/epic025_close_pack.md`

* `audit/qa/evidence_index/index.jsonl`

* `audit/qa/evidence_index/index.sha256`

* `audit/qa/gates/canonical_json_summary.json`

* `audit/qa/gates/canonical_json_summary.sha256`

### Epic OPS evidence root directory (canonical pattern)

Ops execution evidence (PO-only, IA-guided; names-only) MUST be stored under a lowercase audit root such as:

* `audit/ops/<epic-id>/`

When ops execution evidence is captured as part of Live QA execution, it MAY instead live under the epic QA root:

* `audit/qa/<epic-id>/`

Common numbered OPS closeout bundles (names-only). When an epic records discrete OPS closeout runs under the OPS root, paths may include:

* `audit/ops/<epic-id>/ops-01/commands.txt`  
* `audit/ops/<epic-id>/ops-01/stdout.log`  
* `audit/ops/<epic-id>/ops-01/stderr.log`  
* `audit/ops/<epic-id>/ops-01/exit_codes.txt`  
* `audit/ops/<epic-id>/ops-01/codespaces_dev_sampler_url.md`  
* `audit/ops/<epic-id>/ops-01/local_dev_sampler_url.md`  
* `audit/ops/<epic-id>/ops-01/binding_disposition.md`  
* `audit/ops/<epic-id>/ops-01/created_files_sha256.txt`  
* `audit/ops/<epic-id>/ops-02/commands.txt`  
* `audit/ops/<epic-id>/ops-02/repo_root.txt`  
* `audit/ops/<epic-id>/ops-02/repo_head.txt`  
* `audit/ops/<epic-id>/ops-02/python_version.txt`  
* `audit/ops/<epic-id>/ops-02/stdout.log`  
* `audit/ops/<epic-id>/ops-02/stderr.log`  
* `audit/ops/<epic-id>/ops-02/exit_codes.txt`  
* `audit/ops/<epic-id>/ops-02/codespaces_harness_binding.md`  
* `audit/ops/<epic-id>/ops-02/codespaces_harness_binding.md.path_proof.txt`

**Task-scoped OPS validation and classification artifacts (names-only).** Some bounded OPS validation or blocker-classification runs under `ops-02/` may also write:

* `audit/ops/<epic-id>/ops-02/W-001_action_log_and_evidence_output_run2.md`  
* `audit/ops/<epic-id>/ops-02/W-001_classification_run2.md`  
* `audit/ops/<epic-id>/ops-02/commands_w001_run2.txt`  
* `audit/ops/<epic-id>/ops-02/exit_codes_w001_run2.txt`  
* `audit/ops/<epic-id>/ops-02/stdout_w001_run2.log`  
* `audit/ops/<epic-id>/ops-02/stderr_w001_run2.log`

### Epic QA meta and layout (names-only; updated)

Under the epic QA root, EPIC-level meta artifacts and run artifacts follow canonical layout patterns (names-only):

**Epic meta directory (stable):** `audit/qa/hde-epic<NNN>/00_meta/`

* `audit/qa/hde-epic<NNN>/00_meta/codespaces_snapshot.json (optional; non-mandatory)`  
* `audit/qa/hde-epic<NNN>/00_meta/codespaces_snapshot.json.path_proof.txt (optional; non-mandatory)`

**`Bounded surface-inventory and harness-binding coverage artifacts (names-only).`** `Some epics may also capture:`

* `audit/qa/hde-epic<NNN>/00_meta/conjunction_json_surface_inventory.md`  
* `audit/qa/hde-epic<NNN>/00_meta/conjunction_json_surface_inventory.md.path_proof.txt`  
* `audit/qa/hde-epic<NNN>/00_meta/dev_harness_binding_coverage.md`  
* `audit/qa/hde-epic<NNN>/00_meta/dev_harness_binding_coverage.md.path_proof.txt`  
* `audit/qa/hde-epic<NNN>/00_meta/repo_baseline.txt`  
* `audit/qa/hde-epic<NNN>/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic<NNN>/00_meta/doc_deltas.md.path_proof.txt`  
* `audit/qa/hde-epic<NNN>/00_meta/pf23_consult.md`  
* `audit/qa/hde-epic<NNN>/00_meta/deferred_scope_posture.md`

**Meta sha sidecar capture (EPIC025; names-only).** If a meta file requires a governed sha256 sidecar, the sha256 file MAY be stored under the producing check directory using the meta file basename, for example:

* audit/qa/hde-epic\<NNN\>/checks/\<check\_id\>/deferred\_scope\_posture.md.sha256

	

**Doc-delta two-surface pair (names-only).** Doc-deltas are recorded in two distinct surfaces:

* **Draft/staging path-proof (names-only):** `audit/docdeltas/hde-epic<NNN>_doc_deltas.md`  
* **Draft/staging path-proof (names-only):** `audit/docdeltas/hde-epic<NNN>_doc_deltas.md.path_proof.txt`

* **Epic-scoped capture (QA record surface):** `audit/qa/hde-epic<NNN>/00_meta/doc_deltas.md`

Placeholders like `audit/docdeltas/<doc-delta>.md` are nonconforming. The draft/staging surface MUST be a concrete filename.

**Close-pack drain-target ledger (names-only).** When an epic close-pack includes an explicit drain-target planning artifact, use:

* `audit/docdeltas/hde-epic<NNN>_drain_targets.md`

**Per-epic manifest pair (stable; current-state):**

* `audit/qa/hde-epic<NNN>/qa_step_logs_manifest.json`

* `audit/qa/hde-epic<NNN>/qa_step_logs_manifest.json.path_proof.txt`

When the step-log manifest is indexed as governed evidence, the sibling path-proof records the exact manifest path and current SHA-256.

**Epic closure record (EPIC025; names-only).** Some epics may include an epic-scoped closure record at the epic QA root:

* `audit/qa/hde-epic<NNN>/epic_closure_record.md`

* `audit/qa/hde-epic<NNN>/epic_closure_record.md.sha256`

**Epic topology demo artifact (EPIC026; names-only).** Some epics may include epic-scoped topology demo evidence under:

* `audit/qa/hde-epic<NNN>/topology/topology_conjunction_demo.json`

**Step-0 check support artifacts (EPIC026; names-only).** Some epics may create additional Step-0 support outputs under the stable check directory:

* `audit/qa/hde-epic<NNN>/checks/po-000/doc_deltas.md`

* `audit/qa/hde-epic<NNN>/checks/po-000/qa_helpers.sh`

**Bounded Moon Loop delta capture (EPIC028; names-only).** Some epics may capture bounded remediation under the stable delta directory:

* `audit/qa/hde-epic<NNN>/00_meta/delta/patch.diff`  
* `audit/qa/hde-epic<NNN>/00_meta/delta/changed_files.txt`

**Preserved context-note artifacts (EPIC028; names-only; step-specific).** When contextual note content is preserved before trigger-file removal, checks may write:

* `audit/qa/hde-epic<NNN>/checks/po-005/context_note_pre_po010_moonloop.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-006/context_note_pre_po010_moonloop.txt`

EPIC028 discovery and governed-path snapshot artifacts (names-only; step-specific).

D0 — Discovery and evidence bootstrap:

* `audit/qa/hde-epic<NNN>/checks/d0/runtime_context.txt`  
* `audit/qa/hde-epic<NNN>/checks/d0/cli_health.txt`  
* `audit/qa/hde-epic<NNN>/checks/d0/services_surfaces.txt`

PO-001 — Internal compatibility canonical, order-neutral, shared governed emission path:

* `audit/qa/hde-epic<NNN>/checks/po-001/ordering_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-001/compat_compute_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-001/emitter_snapshot.txt`

PO-002 — One governed emission path across CLI, Reader, and internal compatibility:

* `audit/qa/hde-epic<NNN>/checks/po-002/reader_v1_emitter_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-002/runtime_public_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-002/emitter_symbol_proof_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-002/serializer_grep_guard_snapshot.txt`

**Per-check primary logs (stable; one per check):**

* `audit/qa/hde-epic<NNN>/checks/<check_id>/primary.log`

**Per-check gate QA log families (EPIC027; names-only; step-specific).** Some close-workflow gate checks use `<check_id>` values such as `gate_update_evidence_index_write`, `gate_update_evidence_index_check`, `gate_mirror_schema`, `gate_evidence_paths_validation`, `gate_lf_endings`, `gate_orientation_demo_check`, and `gate_orientation_demo_write`. The stable per-check `primary.log` surface above applies to these checks, and they may additionally write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/stdout.log`

**Per-check deliverables reports (EPIC026; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/deliverables_report.md`

**Per-check repo-supported completion summary artifact (EPIC028; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/po-010/final_summary.txt`

**Per-check CLI entrypoint and resolve proof artifacts (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/entrypoint_proof.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/cli_install_help.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/bg_resolve_test.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/bg_resolve_help.txt`

**Per-check route-proof artifacts (EPIC026; names-only; step-specific). Some checks may write:**

* `audit/qa/hde-epic<NNN>/checks/<check_id>/route_proof.txt`

**Per-check dev-route and endpoint-catalog proof artifacts (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/route_inventory.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/dev_conjunction_http.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/endpoint_catalog.txt`

**Per-check reader A7, catalog-route, and mirror-row proof artifacts (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/reader_a7_transport.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/catalog_routes.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/writer_index_rows.txt`

**Per-check Reader proof-surface designation artifacts (EPIC028; names-only; step-specific).**

PO-005 — Governed Reader proof-surface designation:

* `audit/qa/hde-epic<NNN>/checks/po-005/catalog_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-005/http_reader_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-005/blocked_note.txt`

**Per-check Reader transport resolution artifacts (EPIC028; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/po-006/po_005_lookup.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-006/blocked_note.txt`

**Per-check runtime proof inventory artifacts (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/runtime_log_presence.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/runtime_surface_inventory.txt`

**Per-check acceptance-binding snapshot artifacts (EPIC028; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/po-007/acceptance_map_snapshot.json`  
* `audit/qa/hde-epic<NNN>/checks/po-007/token_matrix_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-007/acceptance_map_viability_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-007/mirror_binding_snapshot.jsonl`

**Per-check step artifacts (EPIC025; names-only; step-specific).** In addition to `primary.log`, checks MAY write step-specific artifacts under `audit/qa/hde-epic<NNN>/checks/<check_id>/`. Examples observed in EPIC025 include:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/success_head.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/success_head.txt.sha256`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/success_get.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/success_get.txt.sha256`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/canonical_json_gate_stdout.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/canonical_json_gate_stdout.txt.sha256`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/env_pins.log`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/env_pins.log.sha256`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/env_pins_check_stdout.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/env_pins_check_stdout.txt.sha256`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/sanity_pipeline_stdout.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/sanity_pipeline_stdout.txt.sha256`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/endpoints_catalog.json`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/endpoints_catalog.json.sha256`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/index.sha256`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/index.sha256.sha256`

**Per-check pytest and catalog artifacts (EPIC026; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/pytest_stdout.log`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/pytest_stderr.log`  
  `audit/qa/hde-epic<NNN>/checks/<check_id>/pytest_rc.txt`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/catalog_extract_dev_endpoints.json`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/<check_id>_manifest.json`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/catalog_api_compat_entry.json`

**Per-check compat-surface and identity-discovery artifacts (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/compat_surface.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/compat_identity_discovery.txt`

**Per-check catalog-surface and token-inventory artifacts (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/catalog_surface_inventory.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/token_inventory.txt`

**Per-check canonical JSON gate and evidence-index update artifacts (EPIC026 and EPIC028; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/canonical_json_gate_stdout.log`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/canonical_json_gate_stderr.log`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/canonical_json_gate_rc.txt`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/run_canonical_json_gate.stdout.log`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/run_canonical_json_gate.stderr.log`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/run_canonical_json_gate.rc.txt`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/update_evidence_index.stdout.log`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/update_evidence_index.stderr.log`  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/update_evidence_index.rc.txt`

**Per-check evidence-discipline deliverables (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/update_evidence_index_write.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/update_evidence_index_check.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/orientation_demo_write.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/orientation_demo_check.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/validate_evidence_paths.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/check_lf_endings.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/check_mirror_schema.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/qa_step_manifest_lookup.txt`

**Per-check canonical-JSON family coherence artifacts (EPIC028; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/po-008/json_gate_family_before.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-008/canonical_json_family_before.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-008/json_gate_family_after.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-008/canonical_json_family_after.txt`

**Per-check manifest refresh coherence artifacts (EPIC028; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/po-009/index_snapshot.json`  
* `audit/qa/hde-epic<NNN>/checks/po-009/index_sha_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-009/mirror_path_proof_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-009/manifest_updater_lookup.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-009/manifest_human_index_lookup.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-009/manifest_mirror_lookup.txt`

**Per-check close-pack execution and binding artifacts (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/generate_close_pack.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/close_pack_bindings.txt`

**Per-check CLI help, rejection, and conditional conjunction-output artifacts (EPIC026; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/cli_help.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/showcompat_help.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/reject_nonjson_stdout.log`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/reject_nonjson_stderr.log`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/reject_nonjson_rc.txt`

When `USER_A_ID` and `USER_B_ID` are provided, some checks may also write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/concat_output.json`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/concat_output_order_check.txt`

**Per-check CLI emitter and parity artifacts (EPIC027; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/cli_emitter_proof.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/showcompat_parity.txt`

Per-check EPIC028 CLI and Reader-envelope snapshot artifacts (names-only; step-specific).

PO-003 — CLI compatibility surface presence and deterministic proof-surface verification:

* `audit/qa/hde-epic<NNN>/checks/po-003/hdctl_help.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-003/hdctl_help.stderr.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-003/hdctl_help.rc.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-003/showcompat_presence.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-003/emitter_symbol_proof_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-003/serializer_grep_guard_snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-003/reader_cli_parity_probe.txt`

PO-004 — Public six-part Reader success envelope remains numeric-free:

* `audit/qa/hde-epic<NNN>/checks/po-004/success_encoding_invariance_snapshot.txt`

Per-check EPIC029 bounded-conjunction and sampler-binding artifacts (names-only; step-specific).

PO-001 — Bounded Conjunction closeout slice / no new public surface:

* `audit/qa/hde-epic<NNN>/checks/po-001/conjunction_json_surface_inventory.snapshot.md`  
* `audit/qa/hde-epic<NNN>/checks/po-001/endpoints_catalog.snapshot.json`  
* `audit/qa/hde-epic<NNN>/checks/po-001/route_snapshot.txt`

PO-002 — Canonical JSON discipline across the bounded Conjunction slice:

* `audit/qa/hde-epic<NNN>/checks/po-002/run_canonical_json_gate.output.log`  
* `audit/qa/hde-epic<NNN>/checks/po-002/json_gate_structured_record.snapshot.json`  
* `audit/qa/hde-epic<NNN>/checks/po-002/json_canonical_check.snapshot.log`

PO-003 — Existing dev writer posture remains typed, numeric-free, and outside formal transport proofs:

* `audit/qa/hde-epic<NNN>/checks/po-003/generate_conjunction_writer_evidence.output.log`  
* `audit/qa/hde-epic<NNN>/checks/po-003/generate_conjunction_writer_evidence.rc.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-003/test_dev_conjunction_http.output.log`  
* `audit/qa/hde-epic<NNN>/checks/po-003/test_dev_conjunction_http.rc.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-003/conjunction_write_readback.snapshot.log`  
* `audit/qa/hde-epic<NNN>/checks/po-003/conjunction_writer_summary.snapshot.json`  
* `audit/qa/hde-epic<NNN>/checks/po-003/moon_loop_po_approval_entry.md`

PO-004 — Internal sampler harness remains dev/admin-only and refuses prod or misconfigured use:

* `audit/qa/hde-epic<NNN>/checks/po-004/test_dev_sampler_http.output.log`  
* `audit/qa/hde-epic<NNN>/checks/po-004/test_dev_sampler_http.rc.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-004/dev_start_reader.snapshot.sh`  
* `audit/qa/hde-epic<NNN>/checks/po-004/dev_sampler_healthcheck.snapshot.py`

PO-005 — OPS-01 sampler binding normalization and closure posture:

* `audit/qa/hde-epic<NNN>/checks/po-005/commands.snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-005/exit_codes.snapshot.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-005/codespaces_dev_sampler_url.snapshot.md`  
* `audit/qa/hde-epic<NNN>/checks/po-005/local_dev_sampler_url.snapshot.md`  
* `audit/qa/hde-epic<NNN>/checks/po-005/binding_disposition.snapshot.md`

PO-006 — Formal transport proof surface remains only the cataloged Reader success surface:

* `audit/qa/hde-epic<NNN>/checks/po-006/test_endpoint_catalog.output.log`  
* `audit/qa/hde-epic<NNN>/checks/po-006/test_endpoint_catalog.rc.txt`  
* `audit/qa/hde-epic<NNN>/checks/po-006/endpoints_catalog.snapshot.json`

PO-007 — At least one real functional harness proof exists and passes:

* `audit/qa/hde-epic<NNN>/checks/po-007/functional_bundle.output.log`  
* `audit/qa/hde-epic<NNN>/checks/po-007/functional_bundle.rc.txt`

PO-008 — Final closeout records stay on one bounded acceptance surface and are backed by real passing QA evidence:

* `audit/qa/hde-epic<NNN>/checks/po-008/acceptance_map.snapshot.json`  
* `audit/qa/hde-epic<NNN>/checks/po-008/token_evidence_matrix.snapshot.md`  
* `audit/qa/hde-epic<NNN>/checks/po-008/acceptance_map_viability.snapshot.log`  
* `audit/qa/hde-epic<NNN>/checks/po-008/qa_step_logs_manifest.snapshot.json`  
* `audit/qa/hde-epic<NNN>/checks/po-008/close_report.snapshot.md`  
* `audit/qa/hde-epic<NNN>/checks/po-008/close_manifest.snapshot.json`  
* `audit/qa/hde-epic<NNN>/checks/po-008/po_epic_close_live_qa.snapshot.log`  
* `audit/qa/hde-epic<NNN>/checks/po-008/po_precommit.snapshot.log`  
* `audit/qa/hde-epic<NNN>/checks/po-008/po_postcommit.snapshot.log`

**Per-check CLI rails proof artifacts (EPIC026; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/closed_rails_classification.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/open_rails_ab_rc.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/open_rails_ba_rc.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/open_rails_ab_canonical_json_check.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/open_rails_ba_canonical_json_check.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/abba_identity_check.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/open_rails_note.txt` (conditional; when the open-rails lane cannot run)

**Per-check close-pack generator and copied close-pack artifacts (EPIC026; names-only; step-specific).** Some checks may write:

* `audit/qa/hde-epic<NNN>/checks/<check_id>/generator_stdout.log`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/generator_stderr.log`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/generator_rc.txt`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/close_pack_copy/epic-<NNN>_manifest.json`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/close_pack_copy/epic-<NNN>_evidence_index.json`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/close_pack_copy/endpoints_catalog.json`

* `audit/qa/hde-epic<NNN>/checks/<check_id>/close_pack_copy/endpoints_catalog.json.sha256`

**Per-run nesting is disallowed (checks-only):**

Live QA evidence MUST NOT use `audit/qa/hde-epic<NNN>/runs/`, timestamped run directories, or operator-selected fresh run roots. Canonical Live QA evidence lives under stable `audit/qa/hde-epic<NNN>/checks/<check_id>/` directories.

`run_id` (or `RUN_ID`) is prohibited: Live QA Plans MUST NOT introduce or require it as an operator input, step-log header field, manifest field, or correctness key. Operator-set per-run root selection is also prohibited. Plan-created outputs MUST be written under the stable check directory.

**Remediation subtree (names-only):** `audit/qa/hde-epic<NNN>/remediation/`

**Indexing note (routing-only).** `remediation_only/` content inside remediation bundles is excluded from the governed Evidence Index and machine mirror; governed artifacts remain under their canonical `artifacts/**` roots.

### Live QA evidence is mechanical (routing-only)

Artifacts treated as Live QA evidence under `audit/qa/<epic-id>/...` MUST be produced by commands (shell/scripts/tools), not by hand-editing prose files in an editor. Placeholder fields such as “(fill PASS/FAIL)” are non-conforming.

Live QA plans MUST NOT depend on helper/wrapper scripts unless the script is a canon-named entrypoint by explicit path. Where canon requires an artifact surface but is silent on an entrypoint, the plan must validate or produce the governed artifact surface directly using baseline commands (explicit shell/Python one-liners, direct invocation of canon tools, explicit file writes), with no opaque runners.

### **Canonical evidence tooling entrypoints (EPIC025; names-only)**

When canon requires an explicit repo-local entrypoint script for evidence discipline, use the following canon-named paths:

* LF endings check wrapper: `tools/evidence/check_lf_endings.py` (wraps `ci/checks/check_final_lf.sh`)  
* Evidence-path validation gate: `tools/evidence/validate_evidence_paths.py` (validates `artifacts/evidence_index.jsonl` paths)  
* EPIC025 close-pack generator: `tools/qa/generate_epic025_close_pack.py`  
* EPIC026 close-pack generator: `tools/qa/generate_epic026_close_pack.py`  
* `EPIC027 close-pack generator: tools/qa/generate_epic027_close_pack.py`  
* Deliverables report generator: `tools/qa/generate_deliverables_report.py`  
* CLI conformance generator: `tools/cli/generate_cli_conformance_artifacts.py`  
* Writer evidence generator: `tools/evidence/generate_conjunction_writer_evidence.py`  
* Canonical JSON gate runner: `tools/evidence/run_canonical_json_gate.py`  
* Evidence index updater/checker: `tools/evidence/update_evidence_index.py`  
* HDAPI v2 contract-inventory evidence generator: `tools/evidence/generate_hdapi_v2_contract_inventory.py`  
* EPIC031 PR-03 evidence coherence generator: `tools/evidence/generate_epic031_pr03_evidence_coherence.py`  
* EPIC032 PR-01 router evidence generator: `tools/evidence/generate_epic032_pr01_router_evidence.py`  
* EPIC032 PR-02 narrative registry diff and pack-identity generator: `tools/evidence/generate_narrative_registry_diff.py`  
* HDE-EPIC038 direct database-selection producer: `tools/evidence/generate_hde_epic038_direct_db_selection.py`  
* Direct PostgreSQL contract checker: `ci/checks/check_direct_db_contract.py`  
* Evidence sanity pipeline runner: `tools/evidence/run_sanity_pipeline.py`  
* Evidence index hash checker: `ci/checks/check_evidence_index_hash.sh`  
* Evidence index refresh helper: `tools/evidence/refresh_evidence_index.py`  
* Audit/QA path validator: `tools/evidence/validate_audit_qa_paths.py`  
* Evidence bindings checker: `tools/evidence/check_evidence_bindings.py` (source-excerpt-captured outputs, when written, use `audit/qa/hde-epic<NNN>/checks/<check_id>/check_evidence_bindings_stdout.log`, `audit/qa/hde-epic<NNN>/checks/<check_id>/check_evidence_bindings_stderr.log`, and `audit/qa/hde-epic<NNN>/checks/<check_id>/check_evidence_bindings_rc.txt`; these outputs are non-required unless explicitly listed as deliverables)  
* Topology orientation demo check: `tools/evidence/orientation_demo.py`  
* Mirror schema check: `ci/checks/check_mirror_schema.sh`

### Epic acceptance-ledger artifacts (canonical paths; names-only)

In addition to the close-pack artifacts, epics may carry governed acceptance-ledger artifacts at canonical paths:

* Token↔Evidence matrix (per epic): `audit/qa/hde-epic<NNN>/token_evidence_matrix.md`  
* Acceptance map (per epic): `docs/acceptance_map_epic<NNN>.json`  
* Acceptance map path-proof (per epic): `docs/acceptance_map_epic<NNN>.json.path_proof.txt`  
* Acceptance map viability log (per epic): `audit/qa/hde-epic<NNN>/acceptance_map_viability.log`  
* Token↔Evidence matrix path-proof (per epic): `audit/qa/hde-epic<NNN>/token_evidence_matrix.md.path_proof.txt`  
* Acceptance map viability log path-proof (per epic): `audit/qa/hde-epic<NNN>/acceptance_map_viability.log.path_proof.txt`

These are “where it lives” infra facts only. Semantics, required fields, and token rules live by title in the owning governance, QA, and schemas documents.

### Evidence skeleton artifact (canonical path; names-only)

When governed evidence changes (Index, mirror, or governed artifacts), the evidence skeleton includes the canonical topology orientation demo artifact:

* `audit/gates/topology/orientation_demo.txt`  
* `audit/gates/topology/orientation_demo.txt.path_proof.txt`

**EPIC023 orientation demo derived artifacts (names-only).** The D16 orientation demo check references an EPIC023 artifact directory under `artifacts/hde-epic023_orientation_demo/` derived from the canonical topology orientation demo surface listed above:

* `artifacts/hde-epic023_orientation_demo/orientation_demo_report.json`

* `artifacts/hde-epic023_orientation_demo/sample_result.json`

Generator helper (names-only): `tools/evidence/generate_epic023_orientation_artifacts.py`

### Canonical path binding validation (routing-only)

When acceptance tokens are bound to evidence artifacts (for example, in an Epic Plan, a token/evidence matrix, or an acceptance map), those bindings MUST be validated against the canonical evidence catalog before approval or merge. If the catalog defines a fixed canonical path for a token’s evidence surface, the plan/matrix MUST bind to that exact path. Any binding to a non-canonical path is a mechanical blocker and must be corrected (or routed via explicit ADR and drained into the appropriate canonical home).

### Path-proof transcripts are not primary evidence titles

Path-proofs (`*.path_proof.txt`) are required mechanical companions, but token/evidence binding surfaces MUST NOT list `*.path_proof.txt` as primary evidence entries. Proofs are referenced via `proof_anchor` in the machine mirror and validated through the index/mirror integrity checks (titles-only routing).

Mirror hygiene (records-only JSONL; single-home)

Canonical JSONL (UTF-8, sorted keys, compact, one trailing `\n`), unknown keys rejected. Each record includes:

* artifact\_key  
* role (proof|golden|snapshot|script|log)  
* sha256  
* size\_bytes  
* produced\_at\_utc  
* discovered\_physical\_path  
* proof\_anchor (points to a path-proof stored alongside the artifact)

Record shape invariant (names-only). Each evidence-index JSONL line MUST be a single JSON object record (not an array or primitive value).

Path safety invariant (names-only). discovered\_physical\_path MUST be repo-root-relative and MUST resolve within the repository root; absolute paths and traversal segments (for example ..) are invalid.

**Single mirror file (anti-drift).** Exactly one canonical machine mirror exists:

* `artifacts/evidence_index.jsonl`

No alternate mirror files are permitted unless explicitly introduced via a doc delta in the owning Schemas & Artifacts home. Do not bind acceptance artifacts or indexing to alternate mirror file paths.

---

## 10.6 Acceptance (titles-only)

Acceptance requirements for environment and runtime wiring (for example, start-command capture, app-factory binding to $PORT, and required PORT at runtime) are governed by the relevant product’s canonical governance and QA documents (titles-only). Glow Infrastructure routes by title and does not enumerate token names.

# **11\) Change log & ownership**

## **How updates are requested and approved**

* **When:** this document is reviewed and updated **after each EPIC**, or earlier if discovery is needed to unblock an EPIC.  
* **Flow:** Lead Dev or CodeX proposes **names-only infra** changes (providers, projects, services, repos, domains, database names). The **PO (human)** reviews/approves, then updates the canonical copy.  
* **Scope discipline:** this guide records **where things live** (providers, projects, services, repos, domains, database names, stable base URLs/ports, and governed root paths). **Operations/policy** (headers, acceptance, runbooks, and procedural gates) live by title only in the relevant product’s canonical governance, QA, and process documents. PF07 remains an infrastructure map and does not restate policy or token semantics.

  ## **Content owner for this document**

* **Single owner:** the **PO (human)** is the only person with authority to update this document.

  ## **Routing note**

* Any ops changes (headers, acceptance, runbooks) remain in the relevant product’s canonical governance and QA documents by title only. For HD Engine ops policy, the current governance home is **PF04 — HDE-Governance**. PF07 remains an infrastructure map.  
  ---

{

"production": {

"hd\_engine": {

"provider": "Railway",

"project": "ample-illumination",

"service": "glow-hdengine-v2",

"repo": "amthorn78/glow-hdengine-v2",

"base\_url": "[https://glow-hdengine-v2-production.up.railway.app](https://glow-hdengine-v2-production.up.railway.app)",

"db\_instance": "ample-illumination/production/postgres",

"db\_schema": "hde"

},

"backend": {

"provider": "Railway",

"project": "ample-illumination",

"service": "glow-backend-v4",

"repo": "amthorn78/glow-backend-v4",

"base\_url": "TBD",

"db\_instance": "ample-illumination/production/postgres",

"db\_schema": "TBD"

},

      "frontend": {

      "provider": "Vercel",

"provider": "Railway",

"project": "ample-illumination",

"service": "pg-bridge",

"repo": "TBD",

"base\_url": "[https://illustrious-freedom-production.up.railway.app](https://illustrious-freedom-production.up.railway.app)",

"db\_instance": null,

"db\_schema": null

},

"frontend": {

"provider": "Vercel",

"project": "TBD",

"service": "TBD",

"repo": "amthorn78/glow-frontend-v2",

"base\_url": "glowme.io",

"db\_instance": null,

"db\_schema": null

}

},

"staging": {

"hd\_engine": {

"provider": "GitHub Codespaces",

"project": "TBD",

"service": "TBD",

"repo": "amthorn78/glow-hdengine-v2",

"base\_url": "TBD",

"db\_instance": "ample-illumination/production/postgres",

"db\_schema": "hde"

},

"backend": {

"provider": "GitHub Codespaces",

"project": "TBD",

"service": "TBD",

"repo": "amthorn78/glow-backend-v4",

"base\_url": "TBD",

"db\_instance": "ample-illumination/production/postgres",

"db\_schema": "TBD"

},

"frontend": {

"provider": "GitHub Codespaces",

"project": "TBD",

"service": "TBD",

"repo": "amthorn78/glow-frontend-v2",

"base\_url": "TBD",

"db\_instance": null,

"db\_schema": null

}

},

"development": {

"hd\_engine": {

"provider": "OpenAI Codex",

"project": "TBD",

"service": "TBD",

"repo": "amthorn78/glow-hdengine-v2",

"base\_url": "TBD",

"db\_instance": "ample-illumination/production/postgres",

"db\_schema": "hde"

},

"backend": {

"provider": "OpenAI Codex",

"project": "TBD",

"service": "TBD",

"repo": "amthorn78/glow-backend-v4",

"base\_url": "TBD",

"db\_instance": "ample-illumination/production/postgres",

"db\_schema": "TBD"

},

"frontend": {

"provider": "OpenAI Codex",

"project": "TBD",

"service": "TBD",

"repo": "amthorn78/glow-frontend-v2",

"base\_url": "TBD",

"db\_instance": null,

"db\_schema": null

}

}

}

