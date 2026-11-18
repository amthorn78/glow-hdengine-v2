# Build, verify, release and rollback

Operator runbook for the HD Engine release flow (HDE Build Checklist — Coagulation, HDE-COAG003.1). It names only commands that exist in this repository. Where canon is silent, the step is marked **unknown here** and belongs to the Ops Task Record of the authorized deployment.

## Before you start

Run every command from the repository root, under closed rails, after installing what CI installs:

```bash
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0
python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .
python -m pytest --version
```

Never hard-code a `release_id`, version or build commit into a command or a note: read them from the tools below. Never put a secret, token or connection string on a command line or into a file. The database is reached only through the single configured database URL, `DATABASE_URL`.

## Build: release identity

`release_id` is the SHA-256 of the canonical bytes of `catalog/manifest.json`. Validate the manifest and its declared inputs:

```bash
python scripts/release_id_recompute.py --check-manifest-only
python ci/checks/check_release_identity.sh
```

`ci/checks/check_release_identity.sh` is a Python file: run it with `python`, not `bash`.

A new manifest is cut only in a pull request, after the admission constants in `engine/config/registry_loader.py` name the new release, and only with the cutter; check the cut with `--check`:

```bash
python scripts/cut_release_manifest.py --version <version> --built-at-utc <UTC timestamp>
python scripts/cut_release_manifest.py --version <version> --built-at-utc <UTC timestamp> --check
```

## Verify: evidence

Each check is read-only and is owned by one generator. All of them exit 0 on a coherent tree.

```bash
python tools/evidence/generate_a7_transport_proofs.py --check
python tools/evidence/generate_determinism_gate_proofs.py --check
python tools/evidence/generate_db_runtime_posture.py --check
python tools/evidence/generate_bodygraph_policy_proofs.py --check
```

* A7 transport (local, at the release candidate): `tools/evidence/generate_a7_transport_proofs.py`.
* Determinism and parity (Reader-to-CLI parity, AB-to-BA, two-run identity): `tools/evidence/generate_determinism_gate_proofs.py`.
* DB posture (offline, from the tracked DDL): `tools/evidence/generate_db_runtime_posture.py`.
* BodyGraph invariance (source invariance): `tools/evidence/generate_bodygraph_policy_proofs.py`.

A failing check is repaired in a pull request by its owning generator in write mode, under that evidence work's own authorization. Never edit a generated artifact by hand.

## Release

1. **Attestation**, with the bundle outside the repository (the identity closure):

   ```bash
   python tools/evidence/build_release_attestation.py --output <empty directory outside the repository> --require-clean
   python tools/evidence/build_release_attestation.py --verify <same directory> --require-clean
   ```

2. **Human Evidence Index, hash sentinel and Machine Mirror**, updated in the same pull request as the evidence they index, by the updater only:

   ```bash
   python tools/evidence/update_evidence_index.py
   python tools/evidence/update_evidence_index.py --check
   python tools/evidence/orientation_demo.py --check
   ci/checks/check_mirror_schema.sh
   ```

   Never edit `docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`, their sentinels or any path proof by hand.

3. **Cutover guard**, before the deploy of a release that changes the active Magic10 configuration. Run it from the root of a checkout, over a clean checkout of the release candidate and the prior release's commit, which is the head of `main` before promotion:

   ```bash
   LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1 python scripts/m10_cutover_guard.py --candidate <candidate checkout root> --prior <prior release commit>
   ```

   | Exit | Meaning |
   | :- | :- |
   | 0 | all four proofs passed: one active configuration; no reachable v1 configuration or legacy fallback; a new release identity that binds every new member; a compatible complete prior release |
   | 1 | a proof failed; the JSON report on stdout names each failing proof and its refusal codes |
   | 2 | usage error |
   | 3 | a precondition refused (`M10_CUTOVER_GUARD_REFUSED:<token>` on stderr): closed rails are not set, the candidate is not the root of a clean git checkout, or the prior commit does not resolve in it |
   | 4 | the candidate checkout changed during the run |
   | 5 | the guard stopped on an internal error |

   Any exit other than 0 stops the deployment. At the cutover the guard runs over the frozen candidate as the Ops Task Record's preflight, and the record captures its stdout report.

4. **Deploy.** Commits landing on `main` of the HD Engine repository (amthorn78/glow-hdengine-v2) are the deploy source. The Railway redeploy procedure, its delegation and its authorization are **unknown here**: the Ops Task Record states them.

5. **Post-deploy smoke**, immediately after the deploy. Set `SAFE_MODE` and `ALLOW_NETWORK` (each `0` or `1`), and set `DATABASE_URL` to the read-only database URL the Ops Task Record supplies; never echo it.

   ```bash
   LC_ALL=C LANG=C TZ=UTC python scripts/ops/post_deploy_smoke.py --base-url <base URL> --evidence-dir <evidence directory the Ops Task Record assigns> --ops-task-ref <Ops Task Record ID> --target-app-env prod
   ```

   | Exit | Meaning |
   | :- | :- |
   | 0 | every check passed; the capture set and its retained-path manifest are written |
   | 3 | a precondition refused (`OPS_REFUSED:<token>` on stderr); nothing was written |
   | 4 | the smoke failed: a check failed or the DB spot-check was refused; the capture shows which |
   | 5 | the secret scan refused the capture; nothing was written |
   | 6 | a write failed; the files of the run were removed |

   Exit 4 is a failed deployment smoke: the deployment decision rests on it, and the rollback section applies. The capture is indexed by running the updater (step 2) in the Ops evidence pull request.

   The smoke records the three A7 success-route proofs as not captured under the Product Owner's waiver (C-16) and captures the production refusal of `GET /reader` in their place. It claims no production A7 success-route behaviour.

## Rollback

* **Target.** One complete prior release whose code, catalog, configuration, schema and manifest bytes are mutually compatible. If that target is unavailable, or its identity cannot be reproduced, the affected surface fails closed. Never mix prior code with current configuration or current schemas (HDE Schemas and Artifacts, "Release rollback coupling").
* **Pattern.** Use the "pointer-flip" rollback pattern, by title.
* **Data safety.** A rollback rewrites no stored record and no user identity into a result.
* **After the rollback, check:**
  * the release identity served: run the post-deploy smoke again and read its `provenance_note` capture;
  * no stale cache entry: cache keys carry the configuration in their prefix (`magic10:v1:` and `magic10:v2:` are disjoint) and the `pair_key` under each `config_id` (HDE Schemas and Artifacts §2.9), so a rolled-back configuration reads only its own entries. The production method for inspecting the cache is **unknown here** and belongs to the Ops Task Record;
  * no A7 breakage: the local A7 transport proofs at the release candidate, and the smoke's refusal capture in production. Production serves no A7-eligible route, so the production method for "no A7 breakage" on a rollback is an open obligation of the Ops Task Record; this runbook claims none.

## Where canon is silent

The Railway redeploy and rollback steps, their delegation and authorization, and the behaviour of Railway's edge are **unknown here** and routed to the Ops Task Record. The only target facts this runbook states are those of HDE Glow Infrastructure:

* provider: Railway;
* project: ample-illumination;
* HD Engine service: glow-hdengine-v2;
* base URL: https://glow-hdengine-v2-production.up.railway.app;
* deploy source: commits landing on `main` of amthorn78/glow-hdengine-v2.

Incidents: see `docs/runbooks/incidents.md`.
