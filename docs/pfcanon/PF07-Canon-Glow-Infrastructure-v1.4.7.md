# **0\. Front Matter**

**Title:** PF07-Canon-Glow-Infrastructure  
**Version:** v1.4.7

**Status:** Canon  
**Effective date:** 2026-01-13

**Last Update Gate:** BN 9.3.4 Drain A54-57

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

* **Supersession rule (PF10 addenda).** PF10 Build Notes are living canon. Do not reference PF10 by version strings, and do not treat PF10 section numbers as durable anchors. Prefer referencing PF10 by **addendum number \+ addendum title**. When multiple PF10 addenda cover the same topic, the later addendum supersedes the earlier; the superseding addendum should explicitly name what it supersedes (by addendum number/title).

* **PR-first via CodEx.** CodEx opens the PR automatically (one PR per epic or slice). Whenever proofs or artifacts change, update in the same PR: Doc-Delta, the human Evidence Index (`docs/evidence/INDEX.json`) and its path-proof (`docs/evidence/INDEX.json.path_proof.txt`), the Evidence Index hash sentinel (`docs/evidence/INDEX.sha256`) and its path-proof (`docs/evidence/INDEX.sha256.path_proof.txt`), and the machine JSONL mirror (`artifacts/evidence_index.jsonl`).

* **Machine mirror hygiene.** The mirror is records-only, canonical JSONL (UTF-8, sorted keys, compact, exactly one trailing `\n`), unknown-keys rejected. Each record includes `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` to a path-proof stored alongside the artifact. Keep 1:1 parity with the human index.

* **Header snapshot normalization (titles-only).** Transport header snapshots store header names in lower-case; values remain verbatim. Normalization rules and CI checks live in **HDE-Schemas & Artifacts**; PF07 records only which components produce these snapshots and where they are stored.

* **Capture environment pins (titles-only).** Snapshot/canonicalization jobs run with `LC_ALL=C`, `LANG=C`, `TZ=UTC` to guarantee deterministic bytes. Enforcement and gates live in **HDE-Build Checklist** and **HDE-Schemas & Artifacts**; PF07 records only which environments/components are expected to use these pins.

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

## **2.4 Env Deployment Inventory Required−NowRequired-NowRequired−Now**

**Names-only (policy lives in Governance).** This matrix records the default rails posture and the canonical determinism pins per environment. Transport policy, refusal semantics, and acceptance tokens live in **HDE-Governance**; PF07 remains names-only and routes by title.

| env | SAFE\_MODE (default) | ALLOW\_NETWORK (default) | determinism pins (must) | owner | change path |
| ----- | ----- | ----- | ----- | ----- | ----- |
| dev | 0 (open) | 1 (open) | LC\_ALL=C · LANG=C · TZ=UTC | PO | PR \+ Epic-Process-Guide |
| stage | 0 (open) | 1 (open) | LC\_ALL=C · LANG=C · TZ=UTC | PO | PR \+ Epic-Process-Guide |
| prod | 1 (closed) | 0 (closed) | LC\_ALL=C · LANG=C · TZ=UTC | PO | PR \+ Epic-Process-Guide |
| CI | 1 (closed) | 0 (closed) | LC\_ALL=C · LANG=C · TZ=UTC | PO | PR \+ Epic-Process-Guide |

**Notes.**  
 • Rails “open” permits network I/O *subject to policy*; “closed” forbids it (typed refusal).  
 • Determinism pins are required for all evidence/canonicalization jobs.  
 • **No non-canonical pins.** Live QA plans and evidence steps MUST use only the canonical determinism pins listed here. `PYTHONHASHSEED` MUST NOT be added as a required determinism pin for plan approval or execution. If used for one-off diagnostics, it is non-governed and does not extend the canonical pins set.  
 • Details/tokens: see **HDE-Governance**; jobs/proofs: **HDE-Schemas & Artifacts**; process: **Epic-Process-Guide**.

## **2.5 QA windows (names‑only)**

**Policy routing.** This section records only the existence and locations of prod QA windows and their harnesses. Rails semantics, override guards, and acceptance tokens live in HDE‑Governance and Glow QA Guide (titles‑only).

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

**Codespaces as canonical QA console.**  
 GitHub Codespaces for `amthorn78/glow-hdengine-v2` remains the **canonical QA console**:

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
 Live QA plans MUST NOT depend on helper/wrapper scripts unless the script is a canon-named entrypoint by explicit path. Where canon requires an artifact surface but does not name a tool, the plan must validate or produce the governed artifact surface directly using baseline commands (see §10.5 “Live QA evidence is mechanical”).

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
* **Bridged access (names-only): pg-bridge (Railway).** See §9 Resource catalog. The per-environment mapping for `DB_BRIDGE_URL` lives in §8 Config keys; values are maintained there to avoid duplication. Connection precedence is defined in §7.0.  
*  **Bridge in production (guard).** The HTTPS bridge is disabled by default in production; enable only when DB\_ALLOW\_BRIDGE\_IN\_PROD=1 (policy owned in HDE-Governance).  
* **Start command (inventory):** see **§10** (canonical Railway command kept verbatim)  
* **External surfaces (titles-only):**  
  * **Endpoint Catalog (JSON success)** — discovery/proofs live in **HDE-CLI-API-Vendor-Ref** (A7 success routes); Catalog is **internal-only** and **env-gated**; capture headers-only **env-gate** proof (routing only).  
  * **Ops identity** — `/internal/version` (ops-only; posture in **HDE-Governance**).  
  * **Catalog JSON success route (names-only):** `/reader` (env-gated; currently **dev**). The Endpoint Catalog is **internal-only** and **env-gated**; proofs target this **cataloged JSON success** route only. Bytes live in **HDE-CLI-API-Vendor-Ref**; A7 policy & invariants live in **HDE-Governance**.  
  * *(If used) Endpoint Catalog host (internal-only):* **TBD** (non-prod unreachable in prod; names-only)

*Names-only; policy/bytes/tokens are routed by title (HDE-Governance / HDE-CLI-API-Vendor-Ref).*

---

## **4.2 Glow Backend**

* **Hosting:** provider **Railway** · project **ample-illumination** · service **glow-backend-v4** · base URL **TBD**  
* **Source:** repository **amthorn78/glow-backend-v4** (repo root; no file paths pinned)  
* **Build artifact:** **TBD**  
* **Linked database (shared):** instance **ample-illumination/production/postgres** · schema **TBD** (backend schema may differ from `hde`)  
* **Linked cache/datastore:** **Redis (Railway)** — instance **TBD** (connected to the backend)  
* **Bridged access (names-only):** **pg-bridge (Railway)** — see **§9 Resource catalog**; `DB_BRIDGE_URL` mapping per env lives in **§8 Config keys** (values **OPEN/TBD**)  
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
 All directories in the repository and application codebase MUST use **lowercase ASCII** names. Mixed-case or upper-case directory names are non-conforming and must not be introduced. If mixed-case directories exist, treat them as legacy drift and normalize them to lowercase rather than copying them forward.

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

**Note:** Runtime endpoints (base URLs), databases, and schemas are recorded in **§4 Component maps** and **§7 Databases & Schemas** to avoid duplication.

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

### 6.3.2 Staging / QA (GitHub Codespaces)

* **Frontend:** **TBD** *(Codespaces forwarded URL)*  
* **Backend:** **TBD** *(Codespaces forwarded URL)*  
* **HD Engine:** **TBD** *(Codespaces forwarded URL)*

### 6.3.3 Development (CodEx)

* **Frontend:** **TBD**  
* **Backend:** **TBD**  
* **HD Engine:** **TBD**

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
   • **Prod (guarded):** select **DATABASE\_URL**; the HTTPS bridge is **disabled by default**. Enable **only** when `DB_ALLOW_BRIDGE_IN_PROD=1`; otherwise return a typed error.  
   • **Stage/Test & Dev:** select by availability with fallback: `DATABASE_URL → DB_BRIDGE_URL(https) → typed error`. If `DATABASE_URL` is present but unusable in dev, automatically fall back to `DB_BRIDGE_URL` and proceed.  
   • **No proactive probe:** do not run test queries pre-selection; on total failure return a deterministic, numeric-free error.  
   • **Evidence (dev fallback only):** capture `artifacts/runtime/env_connectivity.snapshot.json` recording attempts and selection; index with the human Evidence Index and machine mirror in the same PR.

* **Runtime search\_path**  
   • `hde, public` (unquoted; in this order). Verify at startup (emit a `SHOW search_path` echo in ops logs). Pin at the ROLE level.

* **Least-privilege (names-only)**  
   • `HDE_APP_ROLE` (runtime): USAGE on app schema; SELECT on `hde.meta`; SELECT/INSERT/DELETE on `hde.public_results`; no DDL.  
   • `HDE_MIGRATOR_ROLE` (DDL): DDL on app schema; no runtime data access.

* **Evidence (titles-only)**  
   Capture: connection echo; search\_path echo; roles/grants snapshot; canonical DDL dump \+ SHA-256 fingerprint; env-selection proof.  
   Indexing & parity: index records-only in the machine mirror (HDE-Schemas & Artifacts). Update the human Evidence Index and its hash sentinel in the same PR. CI enforcement: 1:1 parity; canonical JSONL (single LF); reject unknown keys; each record includes a `proof_anchor` path-proof.  
   Dev-only capture: include `artifacts/runtime/env_connectivity.snapshot.json` proving fallback (attempted, result, selected) when `DB_BRIDGE_URL` is chosen.

* **Acceptance (routing only)**  
   Governed in **HDE-Governance §2.0**. PF07 does not enumerate tokens.

## **7.1 Instances**

Production runs on one Postgres instance; staging/dev connect to the same physical instance via direct `DATABASE_URL` or `DB_BRIDGE_URL` (per §7.0 precedence). Future separation of staging/dev DB instances is **OPEN/TBD**; do not assume.

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

* Dev (CodEx): `postgresql://postgres:<redacted>@metro.proxy.rlwy.net:52353/railway?sslmode=require`

* QA (Codespaces): `postgresql://postgres:<redacted>@metro.proxy.rlwy.net:52353/railway?sslmode=require`

* Prod (Railway): `<internal>` (platform-provided)

**APP\_ENV**

* Dev (CodEx): dev

* QA (Codespaces): dev

* Prod (Railway): prod

	**Note:**  Infra-owned start helpers for the HD Engine (including dev/QA Reader start commands) MUST:

* **Propagate `APP_ENV` from the caller** (shell, harness, or platform) into the child process environment, and

* **MUST NOT silently force a default** (for example, `dev`) when `APP_ENV` is empty or unset.

PF07 records this as an infra responsibility only. The meaning of each `APP_ENV` variant (such as `dev`, `prod`, empty, or unset) and the expected HTTP/rails behavior per value are defined by title in **HDE-Mechanics Guide**, **HDE-Phased Epics**, **HDE-Governance**, and **Glow QA Guide**. PF07 stays names-only and does not restate those semantics; it pins the key name and the requirement that infra helpers faithfully forward `APP_ENV` so that QA harnesses can exercise the configured gating behavior.

**SAFE\_MODE** (rails posture; default, names-only)

* Dev (CodEx): 0 (open)

* QA (Codespaces): 0 (open)

* Prod (Railway): 1 (closed)

**ALLOW\_NETWORK** (rails posture; default, names-only)

* Dev (CodEx): 1 (open)

* QA (Codespaces): 1 (open)

* Prod (Railway): 0 (closed)

**Note (rails windows).**  
 During a PO-approved rails-open prod QA window (see §2.5), production may temporarily run with `SAFE_MODE=0` and `ALLOW_NETWORK=1`. PF07 treats §2.4 as the default posture and §2.5 as the named exception window; do not treat window overrides as the baseline.

**Environment pins** (names-only)

* `LC_ALL` — C

* `LANG` — C

* `TZ` — UTC

**Railway metadata** (names-only)  
 `RAILWAY_PROJECT_ID`, `RAILWAY_PROJECT_NAME`, `RAILWAY_SERVICE_ID`, `RAILWAY_SERVICE_NAME`, `RAILWAY_ENVIRONMENT`, `RAILWAY_ENVIRONMENT_NAME`, `RAILWAY_PUBLIC_DOMAIN`, `RAILWAY_PRIVATE_DOMAIN` — OPEN/TBD

---

**DB\_BRIDGE\_URL** (shared)

* Dev (CodEx): `https://illustrious-freedom-production.up.railway.app`

* QA: not used

* Prod: not used

**`DB_ALLOW_BRIDGE_IN_PROD`**  
 Names-only guard that enables the HTTPS bridge in production when set (policy owned in **HDE-Governance**).

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

* **Connection precedence:** see §7.0 — non-dev selects by presence (`DATABASE_URL → DB_BRIDGE_URL`); dev falls back to `DB_BRIDGE_URL` if `DATABASE_URL` is unusable.

* **Evidence:** when dev fallback occurs, capture `artifacts/runtime/env_connectivity.snapshot.json` and index it in the human Evidence Index \+ machine mirror in the same PR.

  ---

**Admin writer credentials** (names-only; no values here)

* `HDE_ADMIN_TOKENS`, `HDE_ADMIN_SCOPES` — **OPEN/TBD**  
   Names-only keys for the admin credentials used to gate **admin-only HD Engine surfaces**, including CLI and HTTP admin bundle access to the Railway HD Engine (`glow-hdengine-v2`) and its shared database.

**Notes.**

* Values are **not** stored in the repo; they are realized as provider-managed secrets (for example, Railway environment secrets) and configured per environment by operators.  
* QA uses the same channel (provider secrets / environment configuration) for exercising admin-only surfaces under rails and QA windows defined elsewhere.

* Rotation and revocation procedures (for example, changing or removing admin tokens) are documented by title in **HDE-Governance**, **Glow QA Guide**, and any relevant runbooks; PF07 records only the key names and their association with admin surfaces (CLI and HTTP admin bundle).  
* Requiredness, defaults, and validation rules for these keys are not defined here: ownership/requiredness → **HDE-Schemas & Artifacts**; rails/policy (including “admin auth required” and logging) → **HDE-Governance** (titles-only).

  ## **8.2 Component-specific keys**

  ### **8.2.1 HD Engine**

**Port**  
• Dev (CodEx): 8000  
• QA (Codespaces): 8000  
• Prod (Railway): 8000

**Dev harness URLs (internal/dev HTTP; names-only)**

**`DEV_SAMPLER_URL` — dev sampler HTTP harness base URL**

*Dev/CodEx (local dev):* **OPEN/TBD** (must follow the `<base_url>/internal/dev/sampler` pattern; base URL derived from the local dev Reader wiring once confirmed).  
*QA (Codespaces):* `http://127.0.0.1:8000/internal/dev/sampler`  
*Prod (Railway):* not set / not applicable (internal/dev sampler HTTP harness is dev-only).

**Binding ownership and pattern (names-only).**

* `DEV_SAMPLER_URL` is an **infra-owned config key** for the **dev-only sampler HTTP harness** base URL (for routes such as `POST /internal/dev/sampler`) in dev/Codespaces/local-dev environments.  
* The value MUST be derived from the **actual dev Reader process wiring** (host and port) for that environment, not guessed or reconstructed inside QA harnesses or docs.  
* Across environments, the invariant **pattern** is:  
  `DEV_SAMPLER_URL = <base_url>/internal/dev/sampler`  
  where `<base_url>` is the reachable base URL for the dev Reader HTTP service in that environment.

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
• `HDAPI_BASE_URL`: `https://api.humandesignapi.nl/v1` (where configured)  
• `HD_API_KEY`  
• `GEO_API_KEY`

**Notes (inventory-only).**

* PF07 names the HD Engine port mapping and the `DEV_SAMPLER_URL` key as part of the infrastructure inventory. PF07 pins the **Codespaces container-local** `DEV_SAMPLER_URL` binding (`http://127.0.0.1:8000/internal/dev/sampler`) because it is a stable infra fact for the governed dev sampler harnesses; other environments may use a different `<base_url>` and remain **OPEN/TBD** until confirmed. PF07 does not define how the dev harness is started or specify QA procedures; those details (start commands, curl patterns, acceptance tokens) live by title in **HDE-Mechanics Guide**, **HDE-CLI-API-Vendor-Ref**, **Glow QA Guide**, and **HDE-Build Checklist**.  
* Requiredness, defaults, and validation rules for these keys are not defined here: ownership/requiredness → **HDE-Schemas & Artifacts**; rails/policy (including dev-harness validation and rails posture) → **HDE-Governance** and **Glow QA Guide** (titles-only).

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

**Names-only.** This catalog lists stable **provider/project/service** names and known **hosts/links** where we have them. Unknowns remain **TBD** (no guessing). It mirrors single homes in §§2, 3, 4, 5, and 6 to avoid duplication.

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
* **PG bridge (Railway)** — service `pg-bridge` · host `https://illustrious-freedom-production.up.railway.app` *(names-only; `DB_BRIDGE_URL` values map per environment in §8; PF07 lists names only)*  
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

### Indexing discipline (same-change-set rule)

Whenever governed evidence bytes change, update in the same change-set:

* Human Evidence Index: `docs/evidence/INDEX.json`  
* Human Evidence Index path-proof: `docs/evidence/INDEX.json.path_proof.txt`  
* Evidence Index hash sentinel: `docs/evidence/INDEX.sha256`  
* Evidence Index hash sentinel path-proof: `docs/evidence/INDEX.sha256.path_proof.txt`  
* Machine mirror (records-only): `artifacts/evidence_index.jsonl`  
* Machine mirror path-proof: `artifacts/evidence_index.jsonl.path_proof.txt`

**Proof freshness (governed artifacts).** If any file above changes bytes, its co-located `*.path_proof.txt` transcript MUST be refreshed in the same change-set. Stale index or mirror path-proofs are a hard evidence integrity failure.

**Parity rule.** CI enforces 1:1 parity (human index ↔ machine mirror) for governed evidence records.

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

The only valid governed evidence surface for canonical JSON gate artifacts is:

* `audit/gates/json_gate/canonical/`

Legacy / non-authoritative (MUST NOT be treated as the canonical evidence surface for acceptance binding or indexing):

* `audit/gates/canonical_json/`

* `audit/gates/canonical/`

Implementation Plan legacy record (non-authoritative; MUST NOT be required for future Implementation Plans or Live QA Plans unless canon explicitly reinstates it via Schemas & Artifacts):

* `audit/gates/canonical_json/canonical_json.gate.json`

* `audit/gates/canonical_json/canonical_json.gate.json.path_proof.txt`

No dual-home binding: acceptance maps, token/evidence matrices, close-pack manifests, and Evidence Index/Mirror entries MUST reference only `audit/gates/json_gate/canonical/` for canonical JSON gate evidence.

Canonical artifacts under this root (names-only; minimum family):

* `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`

* `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`

* `audit/gates/json_gate/canonical/json_gate_structured_record.json`

* (plus corresponding path proofs as defined by the owning canon)

### `/internal/version` evidence bundle (canonical root; names-only)

The governed evidence bundle for `/internal/version` is rooted at: `artifacts/ops/internal_version/`

Endpoint Catalog inventory file (names-only; symlink surface):

* `docs/ENDPOINTS_CATALOG.json`

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

These two files are the deterministic path-of-record for epic close-pack. Do not relocate them under other trees (for example `audit/qa/**` or `artifacts/**`). Additional copies elsewhere are convenience-only and MUST NOT be used for acceptance binding.

**Epic QA root directory (canonical pattern).** Epic QA roots MUST be lower-case and MUST use:

* `audit/qa/hde-epic<NNN>/` (example: `audit/qa/hde-epic022/`)

Plans and implementations MUST NOT introduce alternate spellings for the same epic in paths. If legacy artifacts exist under non-canonical names, treat them as deprecated and do not create new artifacts under deprecated patterns.

**Run-id discipline (updated posture).** Run-id discipline is not a correctness mechanism. Per-run directory nesting MAY exist for convenience/history, but it is optional and non-canon. The canonical evidence posture is epic-level current-state indexing by `check_id` under the epic QA root.

### Epic OPS evidence root directory (canonical pattern)

Ops execution evidence (PO-only, IA-guided; names-only) MUST be stored under a lowercase audit root such as:

* `audit/ops/<epic-id>/...`

When ops execution evidence is captured as part of Live QA execution, it MAY instead live under the epic QA root:

* `audit/qa/<epic-id>/...`

### Epic QA meta and layout (names-only; updated)

Under the epic QA root, EPIC-level meta artifacts and run artifacts follow canonical layout patterns (names-only):

**Epic meta directory (stable):** `audit/qa/hde-epic<NNN>/00_meta/`

* `audit/qa/hde-epic<NNN>/00_meta/codespaces_snapshot.json (optional; non-mandatory)`

* `audit/qa/hde-epic<NNN>/00_meta/codespaces_snapshot.json.path_proof.txt (optional; non-mandatory)`

* `audit/qa/hde-epic<NNN>/00_meta/doc_deltas.md`

* `audit/qa/hde-epic<NNN>/00_meta/doc_deltas.md.path_proof.txt`

* `audit/qa/hde-epic<NNN>/00_meta/pf23_consult.md`

**Doc-delta two-surface pair (names-only).** Doc-deltas are recorded in two distinct surfaces:

* **Draft/staging path-proof (names-only):** `audit/docdeltas/hde-epic<NNN>_doc_deltas.md.path_proof.txt`

* **Epic-scoped capture (QA record surface):** `audit/qa/hde-epic<NNN>/00_meta/doc_deltas.md`

Placeholders like `audit/docdeltas/<doc-delta>.md` are nonconforming. The draft/staging surface MUST be a concrete filename.

**Per-epic step-log manifest (stable; current-state):**

* `audit/qa/hde-epic<NNN>/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic<NNN>/qa_step_logs_manifest.json.path_proof.txt`

**Per-check primary logs (stable; one per check):**

* `audit/qa/hde-epic<NNN>/checks/<check_id>/primary.log`

**Optional per-run subtree (non-canon; history only):**

* `audit/qa/hde-epic<NNN>/runs/<run_id>/...`  
  Common subdirectories (names-only; exact schemas owned elsewhere):  
* `snapshots/` (run-local copies of governed artifacts and headers)  
* `step_logs/` (per-step logs)  
* `results/` (step outputs and verdict artifacts)  
* `closeout/` (run-local close summaries)

**Remediation subtree (names-only):** `audit/qa/hde-epic<NNN>/remediation/`

**Indexing note (routing-only).** `remediation_only/` content inside remediation bundles is excluded from the governed Evidence Index and machine mirror; governed artifacts remain under their canonical `artifacts/**` roots.

### Live QA evidence is mechanical (routing-only)

Artifacts treated as Live QA evidence under `audit/qa/<epic-id>/...` MUST be produced by commands (shell/scripts/tools), not by hand-editing prose files in an editor. Placeholder fields such as “(fill PASS/FAIL)” are non-conforming.

Live QA plans MUST NOT depend on helper/wrapper scripts unless the script is a canon-named entrypoint by explicit path. Where canon requires an artifact surface but is silent on an entrypoint, the plan must validate or produce the governed artifact surface directly using baseline commands (explicit shell/Python one-liners, direct invocation of canon tools, explicit file writes), with no opaque runners.

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

"pg\_bridge": {

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

