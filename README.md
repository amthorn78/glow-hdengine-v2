# Glow HD Engine — README

**Version:** 1.0  
**Status:** Active (Alpha A3–A5 scope; A6 doc deltas in progress)  
**Owner:** Product Owner (PO) — Nathan  
**Gatekeeper:** Isis (Head Dev — AI session)  
**Lead Dev:** Full Stack Guru (AI session)

---

## Human/AI Disclosure (Fire compliance)

All roles named here — except the **Product Owner** — are **AI-operated ChatGPT sessions**, not human persons.

- **Only human participant:** Product Owner (PO) — Nathan.  
- **All other roles are AI sessions:** “Isis,” “Full Stack Guru,” “Cyrano,” “HD Coder,” “QA,” etc. These are labels for ChatGPT sessions performing scoped tasks under PO direction.  
- **Authority & approvals:** Approvals and signoffs are performed only by the PO. AI “signoff” lines are advisory and must be recorded by the PO to be effective.

---

## What this is

Glow HD Engine produces a **minimal, numeric‑free public envelope** used by the SPA to display **Bands** for “harmony” and (optionally) a short **Aux Narrative**. In Alpha:

- Public JSON is **bands‑only**, free of HD jargon.  
- Determinism is enforced via a **canonical serializer**, **one trailing LF**, an **idempotence preimage** hash, and **AB↔BA parity**.  
- **Reader v1** is a **dev harness** that reproduces the CLI public bytes for acceptance and smoke tests.

> Canonical source for engine/public contract: **HD Engine Math & Tech Spec v4.1.6** (serializer, keys, categories rule, preimage, parity).

---

## Canonical & repo docs

- **Canon**: *HD Engine Math & Tech Spec v4.1.6* (single source of truth for public contract & math).  
- **Repo playbooks** (implementation guides):
  - `docs/CLI_commands.md` — CLI surface, idempotence, sidecar gate, artifacts, quick checks.  
  - `docs/server/reader_v1.md` — Reader v1 dev harness (A5), APP_ENV gating, error tokens, **A5 transport guard**.  
  - `docs/architecture/emitters.md` — **Single emitter canon** (`engine/emit_public.py`) & provenance.  
  - `docs/alpha_acceptance.md` — A3 + A5 acceptance (minimal markers & artifacts).  
  - `CHANGELOG.md` — doc updates summary.

> Deprecated: *Glow HD Engine Architecture & Design v4* (do not reference).

---

## Quick start (local/dev)

> Assumes Python is available. Use a virtualenv if preferred.

```bash
# 1) Create fixtures
mkdir -p fixtures/charts
# Place your two charts as JSON dicts:
#   fixtures/charts/alice.json
#   fixtures/charts/bob.json

# 2) Environment pins (Alpha acceptance posture)
export SAFE_MODE=1
export PRODUCT_INVOCATION_TAG=INV-C9F3AFB03805F430
export ENGINE_TAG=hdengine-alpha

# 3) CLI: produce public bytes (AB/BA)
OUT=artifacts/cards/A3
mkdir -p "$OUT"
./scripts/hdctl.py showcompat --a fixtures/charts/alice.json --a-tz Africa/Cairo \
                              --b fixtures/charts/bob.json   --b-tz Africa/Cairo > "$OUT/cli_stdout_AB.json"
./scripts/hdctl.py showcompat --a fixtures/charts/bob.json   --a-tz Africa/Cairo \
                              --b fixtures/charts/alice.json --b-tz Africa/Cairo > "$OUT/cli_stdout_BA.json"
cmp -s "$OUT/cli_stdout_AB.json" "$OUT/cli_stdout_BA.json" && echo "CLI_AB_BA_IDENTITY: OK"
```

**What to expect**  
- LF‑terminated JSON, **no BOM**, **no ANSI**.  
- Top‑level keys (sorted): `categories`, `eligible`, `idempotence_hash`, `meta`, `release_id`.  
- `categories` contains one item: `{"id":"harmony","band":"Cool|Open|Warm|Glow"}`.

---

## Reader v1 (dev harness)

Reader v1 is a **dev‑only** HTTP harness that returns bytes **identical** to the CLI for the same inputs.

- **Route:** `GET /api/reader?v=1&a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA>`  
- **APP_ENV gating:**  
  - `APP_ENV=dev`: may read **only** `fixtures/charts/*`; rejects traversal & symlinks; errors are one‑line JSON + LF.  
  - non‑dev: returns `403` (no filesystem access).  
- **Transport (A5):** `Content-Type: application/json; charset=utf-8` only — **no `ETag` / `Cache-Control`**; conditional GET arrives in **A7**.

```bash
# Smoke (Reader equals CLI), assumes server on http://127.0.0.1:8000
RART=artifacts/cards/A5; CART=artifacts/cards/A3; mkdir -p "$RART"
curl -sS -D "$RART/headers_AB.txt" \
  "http://127.0.0.1:8000/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" \
  -o "$RART/reader_AB.json"
cmp -s "$RART/reader_AB.json" "$CART/cli_stdout_AB.json" && echo READER_EQ_CLI_AB_OK
```

---

## Determinism & emitter canon

- **Serializer (MUST):** `json.dumps(..., sort_keys=True, separators=(',',':'), ensure_ascii=False) + "\n"`  
- **Preimage (MUST):** `idempotence_hash = sha256( sercanon(preimage_without_idempotence_hash) )` (lowercase 64‑hex).  
- **Parity (MUST):** public bytes identical for AB and BA (swap inputs).  
- **Single emitter (MUST):** both CLI and Reader call `engine/emit_public.py`; closeouts record `EMITTER_SHA256=<64hex>`.

---

## Evidence & release identity

- **Release ID:** `scripts/release_id.sh` prints **one 64‑hex + LF** (`sha256` of `release/manifest.sorted.json`).  
- **A3 Artifacts (minimal):**
  ```
  artifacts/cards/A3/cli_stdout_AB.json
  artifacts/cards/A3/cli_stdout_BA.json
  artifacts/cards/A3/release_id.txt
  artifacts/cards/A3/IDENTITY_OK.txt
  artifacts/cards/A3/validation.log
  ```
- **A5 Artifacts (minimal):**
  ```
  artifacts/cards/A5/reader_AB.json
  artifacts/cards/A5/reader_BA.json
  artifacts/cards/A5/headers_AB.txt
  artifacts/cards/A5/headers_BA.txt
  artifacts/cards/A5/validation.log
  ```

See `docs/alpha_acceptance.md` for the Run‑This‑Now acceptance steps and minimal grep markers.

---

## Environment variables

- `SAFE_MODE` — **1** for acceptance (no network). **0** only for explicit vendor calls (requires `ALLOW_NETWORK=1`).  
- `ALLOW_NETWORK` — set to **1** only when intentionally enabling vendor/network (never in acceptance).  
- `PRODUCT_INVOCATION_TAG` — current invocation tag (e.g., `INV-C9F3AFB03805F430`).  
- `ENGINE_TAG` — human‑readable engine tag for meta.  
- `APP_ENV` — `dev` to enable Reader harness filesystem access; otherwise returns 403.

---

## Project layout (key paths)

```
docs/
  CLI_commands.md
  server/reader_v1.md
  architecture/emitters.md
  alpha_acceptance.md
CHANGELOG.md
fixtures/
  charts/           # input charts for dev/acceptance
release/
  manifest.sorted.json
scripts/
  hdctl.py          # CLI entrypoint
  release_id.sh     # prints 64-hex + LF
artifacts/
  cards/
    A3/             # CLI evidence
    A5/             # Reader harness evidence
```

---

## Governance (acceptance delivery)

- Work on `main`. **No PRs** for final acceptance.  
- Each card ends with **one revert‑friendly commit** and an evidence bundle under `artifacts/cards/<CARD>/`.  
- **PO** performs closeout and signoff; see template in `docs/alpha_acceptance.md`.

---

## FAQ

**Q: Why no `ETag` in A5?**  
A: Transport caching and conditional GET are introduced in **A7** to keep Alpha focused on body invariants and harness gating.

**Q: Where is the engine/public contract defined?**  
A: In *HD Engine Math & Tech Spec v4.1.6* — single source of truth.

**Q: Is the old Architecture & Design doc required?**  
A: No. It’s deprecated and removed from active references.

---

## Changelog (README)

- **v1.0 (2025‑10‑02):** Initial comprehensive README for Alpha A3–A5; links to canonical Spec and repo playbooks; A5 transport guard documented.
