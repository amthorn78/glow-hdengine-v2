# **0\. Front Matter**

**Title:** PF07-Canon-Glow-Infrastructure  
 **Version:** v1.0.9

**Status:** Canon  
**Effective date:** 2025-11-25  
**Last Update Gate:** BN 7.7.8 Drain A13

**Invocation tag:** `INV-f2ac55d77ce9aacc`

---

## **Intent & scope**

**Inventory only.** A single, static, **names-only** infrastructure map for Glow. This document shows **where things live** across providers and environments. It does **not** include operations policy, runbooks, transport rules, byte contracts, token lists, or pinned file paths. Cross-document references are **titles-only** (no version numbers).

**Endpoint Catalog posture (routing note).** Reader/Aux success proofs are **catalog-driven** via the Endpoint Catalog (JSON success). The Catalog is **internal-only** and **env-gated**; non-prod entries are **unreachable in prod** (capture a headers-only **env-gate proof**). PF07 remains names-only; contracts live in the owning docs below.

### **Routing (titles-only)**

* **Rails/transport policy, acceptance tokens, and ops posture** → **HDE-Governance**.  
* **Public envelope, request/response shapes, and Endpoint Catalog (JSON success)** → **HDE-CLI-API-Vendor-Ref**.  
* **Canonical JSON, pack/manifest, and the machine Evidence Index** → **HDE-Schemas & Artifacts**.  
* **Jobs/guards and evidence procedures** → **HDE-Mechanics Guide**.  
* **Process & PR workflow (PR-first; human index \+ machine mirror updated in the same PR)** → **Epic-Process-Guide**.  
* **Narratives persistence (names-only).** Only **DB/schema locations** are referenced here. Field/length constraints live in **HDE-Schemas & Artifacts**; logging/privacy (keys-only; never log text) lives in **HDE-Governance**; Aux/CLI endpoint bytes live in **HDE-CLI-API-Vendor-Ref**.

---

## **Change control (titles-only cross-refs)**

**Supersession rule (PF10 addenda).** When PF10 contains multiple lettered addenda on the same topic, the later letter supersedes the earlier. Route all references by title only.

**PR-first via CodEx.** CodEx opens the PR automatically (one PR per epic or slice). Whenever proofs or artifacts change, update in the same PR: Doc-Delta, the human Evidence Index (`docs/evidence/INDEX.json`), the Evidence Index **hash sentinel** (`docs/evidence/INDEX.sha256`), and the machine JSONL mirror (`artifacts/evidence_index.jsonl`).

**Machine mirror hygiene.** The mirror is records-only, canonical JSONL (UTF-8, sorted keys, compact, exactly one trailing `\n`), unknown-keys rejected. Each record includes `artifact_key`, `role`, `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, and a `proof_anchor` to a path-proof stored alongside the artifact. Keep 1:1 parity with the human index.

**Header snapshot normalization (titles-only).** Transport header snapshots store header names in lower-case; values remain verbatim. Normalization rules and CI checks live in **HDE-Schemas & Artifacts**; PF07 records this as a names-only pointer.

**Capture environment pins (titles-only).** All snapshot/canonicalization jobs run with `LC_ALL=C`, `LANG=C`, `TZ=UTC` to guarantee deterministic bytes. Enforcement and gates live in **HDE-Build Checklist** and **HDE-Schemas & Artifacts**. PF07 stays names-only and routes by title.

**Primary homes (by title):**

* PF04 — HDE-Governance  
* PF05 — HDE-CLI-API-Vendor-Ref  
* PF02 — HDE Architecture  
* PF01 — HDE-Math-Spec  
* PF06 — Epic-Process-Guide  
* PF12 — HDE-Schemas & Artifacts

---

# **1\) Purpose & boundaries**

**What this is.** A **names-only inventory** of the infrastructure that powers Glow: providers, projects, services, repositories, domains, environments, and database schemas for HD Engine, Glow Backend, and Glow Frontend.

**What this is not.** No procedures, no transport headers or acceptance rules, no start/run commands, no policy. Those live by title only in:

* **PF04 — HDE-Governance** (transport/A7, ops policy, acceptance)  
* **PF05 — HDE-CLI-API-Vendor-Ref** (public bytes & API)  
* **PF12 — HDE-Schemas & Artifacts** (canonical JSON, pack/manifest, machine mirror)  
* **PF02 — HDE Architecture** (system design; high-level topology)  
* **PF06 — Epic-Process-Guide** (process/change control)

**Names here are authoritative;** values, semantics, and procedures are routed **by title only** to their single homes above.

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

---

**UPDATED BLOCK (paste-ready)**

## **2.3 Routing (titles-only)**

### **2.3.1 Policy & acceptance**

Rails/transport policy and acceptance are governed in **HDE-Governance** (single-home token roster). PF07 is **names-only** and does **not** enumerate tokens.

### **2.3.2 Success-route discovery & proofs**

Reader (and Aux) success-route proofs are catalog-driven via the Endpoint Catalog (JSON success) defined in HDE-CLI-API-Vendor-Ref. Proofs MUST target a cataloged JSON success route; `/internal/*` routes are excluded.

**Catalog posture.**  
 The Catalog is internal-only and env-gated; non-prod entries MUST be unreachable in production. Capture a headers-only env-gate proof showing this behavior. Architecture stays contract-free and routes bytes by title only.

**A7 invariants (routing only).** On a cataloged JSON success route, proofs MUST satisfy:

* GET/200 with a strong, quoted ETag over the LF-terminated canonical body.  
* HEAD/200 validator parity; Content-Type \== GET; no body; Content-Length \== len(identity 200 body).  
* 304 only after a prior 200; no body; omit both Content-Type and Content-Length; validators mirror the cached 200\.  
* `Vary: Authorization, Accept-Encoding` present.  
* Encoding invariance of identity (ETag) and effective Content-Length across accepted encodings. Token semantics and concrete header bytes live in HDE-Governance and HDE-CLI-API-Vendor-Ref; Architecture cites them by title only.

**Scope note (names-only).** Under **EPIC-010**, **Aux** evidence consists of **two header snapshots only** (Text 200 and Suppressed 200). **Aux HEAD/304** are **out of scope**; **A7 (GET/HEAD/304, Vary, encoding-invariance)** proofs run **only** on a **Catalog JSON success** route (see §4.1 entry for the route name). Bytes live in **HDE-CLI-API-Vendor-Ref**; policy lives in **HDE-Governance**; capture/indexing discipline lives in **HDE-Schemas & Artifacts**.

**Evidence pointers (titles-only).** Keep success-route artifacts indexed in the human Evidence Index and mirrored 1:1 in the machine JSONL mirror (records-only; canonical; single LF; unknown-key rejection; each record carries a proof\_anchor). See HDE-Schemas & Artifacts for mirror ownership and CI hygiene.

---

### **2.3.3 Ops-only identity**

`/internal/version` is **operator-only** and **not A7-eligible**. Its posture is governed in **HDE-Governance**: `Cache-Control: no-store`, **no ETag**, **HEAD 200 parity**, and **conditionals ignored** (always 200). Architecture remains contract-free and routes these rules **by title**.

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

**Names-only (policy lives in Governance).** This matrix records the default rails posture and determinism pins per environment. Transport policy, refusal semantics, and acceptance tokens live in **HDE-Governance**; PF07 remains names-only and routes by title.

| env | SAFE\_MODE (default) | ALLOW\_NETWORK (default) | determinism pins (must) | owner | change path |
| ----- | ----- | ----- | ----- | ----- | ----- |
| dev | 0 (open) | 1 (open) | LC\_ALL=C · LANG=C · TZ=UTC | PO | PR \+ Epic-Process-Guide |
| stage | 0 (open) | 1 (open) | LC\_ALL=C · LANG=C · TZ=UTC | PO | PR \+ Epic-Process-Guide |
| prod | 1 (closed) | 0 (closed) | LC\_ALL=C · LANG=C · TZ=UTC | PO | PR \+ Epic-Process-Guide |
| CI | 1 (closed) | 0 (closed) | LC\_ALL=C · LANG=C · TZ=UTC | PO | PR \+ Epic-Process-Guide |

**Notes.**  
 • Rails “open” permits network I/O *subject to policy*; “closed” forbids it (typed refusal).  
 • Determinism pins are required for all evidence/canonicalization jobs.  
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

**Codespaces role (QA console, names-only).**  
 GitHub Codespaces for the repository `amthorn78/glow-hdengine-v2` is a **QA console**, not a production environment:

* It clones the HD Engine repo into a hosted devcontainer.

* It runs CLI (`hdctl`) and HTTP (`curl`) commands that can target the Railway HD Engine service and the shared Postgres instance when environment configuration and rails allow it.

* It writes QA artifacts (logs, notes, snapshots) back into the repo under governed paths (for example, `Audit/QA/**`, `artifacts/**`, `docs/**`).

Codespaces does **not** host the production HD Engine itself; it is a remote shell talking to the Railway `glow-hdengine-v2` service and `ample-illumination/production/postgres` database. Names and paths for QA harnesses and windows (for example, EPIC-specific QA rails windows) are recorded in §2.5 and **Glow QA Guide** by title.

**“Prod via Codespaces” (gloss, names-only).**  
 When other PF documents or QA guides use the phrase **“prod via Codespaces”**, it SHOULD be read as:

* Commands are run **from** a Codespace attached to `amthorn78/glow-hdengine-v2` (or an equivalent workspace), and

* Those commands **talk to** the HD Engine production service at `https://glow-hdengine-v2-production.up.railway.app` and/or the `ample-illumination/production/postgres` database (schema `hde`), and

* QA artifacts from those runs are stored in the HD Engine repo under governed paths.

It does **not** mean that the Codespace itself is a production environment. Any shell that can reach the Railway base URL and/or connect to the production DB with the correct configuration can exercise production behavior; PF07 names the standard providers, projects, services, and repos, and routes QA procedures and proof steps by title to **Glow QA Guide**, **HDE-Governance**, and **HDE-CLI-API-Vendor-Ref**.

---

# 3\) Provider inventory (names-only)

## 3.1 Railway

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

*Names-only; no policy, runbooks, or tokens here. Transport/A7 policy → HDE-Governance (titles-only).*

---

## 3.2 Vercel

* **Team / org:** **TBD**  
* **Projects & aliases:**  
  * **Glow Frontend:** project **TBD** · production alias `glowme.io` · preview alias pattern **TBD**  
* **Domains:** primary `glowme.io`; additional **TBD**  
* **Preview policy (names-only):** **TBD**

*Names-only; policy/headers/acceptance routed by title.*

---

## 3.3 GitHub

* **Organization / user:** `amthorn78` *(for HD Engine repo)*  
* **Repositories by component:**  
  * **HD Engine:** `amthorn78/glow-hdengine-v2` · default branch `main`  
  * **Glow Backend:** **TBD** · default branch **TBD**  
  * **Glow Frontend:** **TBD** · default branch **TBD**

*Names-only; no paths/tokens. Evidence indexing lives in §36 / HDE-Schemas and Artifacts.*

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
* **External surfaces (titles-only):** Backend API surfaces — contract/fields/status/headers live in **HDE-CLI-API-Vendor-Ref** (PF07 records names only)  
  * **Aux Narrative (public, names-only):** canonical route `GET /api/aux/narrative?v=1` · BC alias: `/aux/narrative` · bytes live in **HDE-CLI-API-Vendor-Ref** · canon/alias parity and transport header posture are governed by title there. (Aux is **not** Catalog/A7; see §2.3.2 scope note.)

*Names-only; schema/policy/bytes routed by title; no token lists or pinned evidence paths.*

---

## **4.3 Glow Frontend**

* **Hosting:** provider **Vercel** · team **TBD** · project **TBD** · site **glowme.io** · domains: `glowme.io` (production), **previews TBD** (Vercel preview alias pattern)  
* **Source:** repository **amthorn78/glow-frontend-v2** (repo root; no file paths pinned)  
* **Runtime config:** public config key **names TBD** (values **OPEN/TBD**)  
* **Upstream targets:** Backend base URL **TBD** · HD Engine base URL **TBD** (names-only; see **§6 Domains & DNS** and **§4.1**)

*Names-only; routing by title to **HDE-CLI-API-Vendor-Ref** (public envelope & request/response), **HDE-Governance** (A7/transport), **HDE-Schemas & Artifacts** (canonical JSON & mirror).*

# **5\) Repositories**

## **5.1 HD Engine repo**

**Repository.**  
 `amthorn78/glow-hdengine-v2`

**Primary paths of interest.**

* `adapter/`

* `engine/`

* `presenter/`

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

This section lists **domain names** and **DNS roles** in use. It is **names-only** (no policy, no header/TTL/cert bytes). Transport/A7 policy and acceptance live in **HDE-Governance**; public envelope and request/response shapes live in **HDE-CLI-API-Vendor-Ref**. Evidence indexing and mirror parity live in **§36 Documentation Artifacts & Registry** and **§1.3 Evidence & CI coupling**.  
 Supersession note. PF07 follows the latest PF10 addenda (later letter wins) and routes by **title only**.

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

## 6.4 DNS provider & record types (names-only)

* **Provider:** **Vercel DNS** (zone: `glowme.io`)  
* **Record types in use:** `A` / `AAAA`, `CNAME` *(confirm exact hostnames as we populate)*; `TXT` *(verification, if required — OPEN/TBD)*

### **6.5 Routing (titles-only)**

* **Transport & A7 policy / acceptance:** **HDE-Governance**  
* **Public envelope & request/response shapes:** **HDE-CLI-API-Vendor-Ref**  
* **Evidence registry & mirror discipline:** **§36 Documentation Artifacts & Registry** and **§1.3 Evidence & CI coupling**

**Notes (inventory-only).**

* Use **OPEN/TBD** when not confirmed (no guessing).  
* PF07 records **names** only; values, TTLs, cert details, and policy live by **title** in their single homes.

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

**Single database instance (current posture, names-only)**  
 Production runs on one Postgres instance; staging/dev connect to the same physical instance via direct DATABASE\_URL or DB\_BRIDGE\_URL (per §7.0 precedence). Future separation of instances for staging/dev is OPEN/TBD and will be recorded here when facts are confirmed.

**Production (Railway)**

* Provider: Railway (names-only)  
* Database (shared): Postgres — instance `ample-illumination/production/postgres` *(observed; confirm)* — used by `glow-hdengine-v2` and `glow-backend-v4`  
* Schemas: HD Engine: `hde` · Backend: **TBD**  
* Engine & version floor: Postgres ≥ 14 *(refine from build evidence)*

**Staging/QA (GitHub Codespaces)**

* Provider: GitHub Codespaces  
* Instance: **OPEN/TBD** *(do not assume shared prod; confirm bridge vs direct)*  
* Schemas: HD Engine: `hde` · Backend: **TBD**  
* Engine & version floor: **TBA**

**Development (CodEx)**

* Provider: CodEx  
* Instance: **OPEN/TBD** *(do not assume shared prod; confirm bridge vs direct)*  
* Schemas: HD Engine: `hde` · Backend: **TBD**  
* Engine & version floor: **TBA**

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
* **Same-PR rule.** Update the human Evidence Index, its **hash sentinel** (`docs/evidence/INDEX.sha256`), and the machine mirror in the **same PR**; CI enforces 1:1 parity, canonical JSONL (one LF), unknown-key rejection, and presence of `proof_anchor` path-proofs.  
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

* Dev (CodEx): OPEN/TBD (a prior report showed “prod”; treat as OPEN/TBD until verified)

* QA (Codespaces): OPEN/TBD

* Prod (Railway): OPEN/TBD

**SAFE\_MODE** (rails posture; observation only)

* Dev (CodEx): OPEN/TBD (default expectation historically was rails-closed in dev; do not infer—confirm)

* QA (Codespaces): OPEN/TBD

* Prod (Railway): OPEN/TBD

**ALLOW\_NETWORK** (rails posture; observation only)

* Dev (CodEx): OPEN/TBD

* QA (Codespaces): OPEN/TBD

* Prod (Railway): OPEN/TBD

**Environment pins** (names-only)

* `LC_ALL` — OPEN/TBD (all envs)

* `LANG` — OPEN/TBD (all envs)

* `TZ` — OPEN/TBD (all envs)

**Railway metadata** (names-only)  
 `RAILWAY_PROJECT_ID`, `RAILWAY_PROJECT_NAME`, `RAILWAY_SERVICE_ID`, `RAILWAY_SERVICE_NAME`, `RAILWAY_ENVIRONMENT`, `RAILWAY_ENVIRONMENT_NAME`, `RAILWAY_PUBLIC_DOMAIN`, `RAILWAY_PRIVATE_DOMAIN` — OPEN/TBD

---

**DB\_BRIDGE\_URL** (shared)

* Dev (CodEx): `https://illustrious-freedom-production.up.railway.app`

* QA: ⟪set URL⟫

* Prod: ⟪set URL⟫

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

* `HDE_ADMIN_TOKENS`, `HDE_ADMIN_SCOPES` — OPEN/TBD

Notes: Values are operator-managed in production; QA uses the same channel. Rotation process is documented by title (no secrets in repo).

* 

  ## **8.2 Component-specific keys**

### **8.2.1 HD Engine**

**Port**  
 • Dev (CodEx): 8000  
 • QA (Codespaces): 8000  
 • Prod (Railway): 8000

**LOG\_LEVEL**  
 • OPEN/TBD (all envs)

**Loader selector**  
 • PACK\_SHA: OPEN/TBD (active narratives pack identity; file-backed runtime)

**Vendor-ingest keys (present where noted; secrets redacted)**  
 • HDAPI\_BASE\_URL: [https://api.humandesignapi.nl/v1](https://api.humandesignapi.nl/v1) (where configured)  
 • HD\_API\_KEY:  
 • GEO\_API\_KEY: 

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

**Notes (names-only).** No secrets or policy here; endpoints/bytes live by title in **HDE-CLI-API-Vendor-Ref**; governance/policy lives by title in **HDE-Governance**.

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

  ## **10.5 Evidence & indexing (titles-only)**

* **Single home (entries & types).** The authoritative listing of artifact **titles/paths** lives in **PF12 §8.6 “Evidence Index entries”**; governed record types live in **PF12 Appendix C**. PF07 is **names-only** and does not pin file paths. If this document contains “§36 Documentation Artifacts & Registry,” treat it as a **pointer only** to PF12 (not a second source of truth).

* **Indexing discipline (same-PR rule).** Whenever evidence changes, update in the **same PR**:

  * Human Evidence Index: `docs/evidence/INDEX.json`  
  * **Evidence Index hash sentinel:** `docs/evidence/INDEX.sha256`  
  * Machine mirror (records-only): `artifacts/evidence_index.jsonl`  
     CI enforces **1:1 parity** (human ↔ machine).  
* **Mirror hygiene (records-only JSONL).** Canonical JSONL (UTF-8, sorted keys, compact, **one trailing `\n`**), unknown-keys rejected. Each record includes:

  * `artifact_key`, **`role`** (`proof|golden|snapshot|script|log`), `sha256`, `size_bytes`, `produced_at_utc`, `discovered_physical_path`, `proof_anchor` (points to a path-proof stored alongside the artifact).  
* **Write discipline (merge-blocking).**

  * **Field order (ASCII, exact):** `artifact_key`, `discovered_physical_path`, `produced_at_utc`, `proof_anchor`, `role`, `sha256`, `size_bytes`.  
  * **Sort-before-write:** by (`artifact_key`, `discovered_physical_path`).  
  * **Single mirror file:** exactly one `artifacts/evidence_index.jsonl`.  
  * **Uniqueness:** (`artifact_key`, `discovered_physical_path`) must be unique.  
  * **Path-proofs:** a `path_proof.txt` (or equivalent) must exist beside each artifact; the record’s `proof_anchor` must match it exactly.

  ---

  ## **10.6 Acceptance (titles-only; tokens live in HDE-Governance §2.0)**

Acceptance for **start-command capture**, **app-factory binding to `$PORT`**, and **required `PORT` at runtime** is governed in **HDE-Governance**. This document **routes by title** and **does not enumerate token names**.

# **11\) Change log & ownership**

## **How updates are requested and approved**

* **When:** this document is reviewed and updated **after each EPIC**, or earlier if discovery is needed to unblock an EPIC.  
* **Flow:** Lead Dev or CodeX proposes **names-only infra** changes (providers, projects, services, repos, domains, database names). The **PO (human)** reviews/approves, then updates the canonical copy.  
* **Scope discipline:** this guide records **where things live**; **operations/policy** (headers, acceptance, runbooks) continue to live **by title only** in **PF04 — Canon-HDE-Governance**.

  ## **Content owner for this document**

* **Single owner:** the **PO (human)** is the only person with authority to update this document.

  ## **Routing note**

* Any ops changes (headers, acceptance, runbooks) remain in **PF04 — Canon-HDE-Governance** by title only. This document is an **infrastructure map**.  
  ---

  {  
    "production": {  
      "hd\_engine": {  
        "provider": "Railway",  
        "project": "ample-illumination",  
        "service": "glow-hdengine-v2",  
        "repo": "amthorn78/glow-hdengine-v2",  
        "base\_url": "https://glow-hdengine-v2-production.up.railway.app",  
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
        "db\_schema": "hde"  
      },  
      "pg\_bridge": {  
        "provider": "Railway",  
        "project": "ample-illumination",  
        "service": "pg-bridge",  
        "repo": "TBD",  
        "base\_url": "https://illustrious-freedom-production.up.railway.app",  
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
        "db\_instance": "TBD",  
        "db\_schema": "hde"  
      },  
      "backend": {  
        "provider": "GitHub Codespaces",  
        "project": "TBD",  
        "service": "TBD",  
        "repo": "TBD",  
        "base\_url": "TBD",  
        "db\_instance": "TBD",  
        "db\_schema": "TBD"  
      },  
      "frontend": {  
        "provider": "GitHub Codespaces",  
        "project": "TBD",  
        "service": "TBD",  
        "repo": "TBD",  
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
        "db\_instance": "TBD",  
        "db\_schema": "hde"  
      },  
      "backend": {  
        "provider": "OpenAI Codex",  
        "project": "TBD",  
        "service": "TBD",  
        "repo": "TBD",  
        "base\_url": "TBD",  
        "db\_instance": "TBD",  
        "db\_schema": "TBD"  
      },  
      "frontend": {  
        "provider": "OpenAI Codex",  
        "project": "TBD",  
        "service": "TBD",  
        "repo": "TBD",  
        "base\_url": "TBD",  
        "db\_instance": null,  
        "db\_schema": null  
      }  
    }  
  }  
  


