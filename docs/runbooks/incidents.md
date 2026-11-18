# Incidents

Operator runbook for HD Engine incidents (HDE Build Checklist — Coagulation, HDE-COAG003.1). Canon states no numeric threshold for any class below: the thresholds are the operator's alerting and are not canon. Every first check uses a surface that exists; escalation goes to the Product Owner with the smoke capture; a rollback follows `docs/runbooks/build_verify_release_rollback.md`, "Rollback".

## First check for every class

Run the post-deploy smoke against the service, under closed rails, into a new evidence directory, with the read-only `DATABASE_URL` from the Ops Task Record when the database is in question:

```bash
LC_ALL=C LANG=C TZ=UTC python scripts/ops/post_deploy_smoke.py --base-url <base URL> --evidence-dir <new evidence directory> --ops-task-ref <Ops Task Record ID> --target-app-env prod
```

Read the capture: the `headers_get` and `provenance_note` captures show the release identity `/internal/version` serves; the `success_writers_errors` and `reader_refusal_get` captures show the error posture; the `db_posture_spot_check` capture shows the live DB posture. Exit codes are in the release runbook.

## Elevated 5xx on Reader or Compat

* **Symptom.** Reader (`POST /api/reader`) or Compat answers 5xx at a rate the operator's alerting flags.
* **First checks.** The smoke run above. A failing H-02 to H-07 check, or a release identity that differs from the one deployed, points at the deployment.
* **Compat in production.** The Compat namespace answers 404 under production posture by design; a Compat 5xx in production is a configuration incident.
* **Escalate** to the Product Owner with the capture. **Roll back** by the release runbook when the deployment is the cause.

## Slow Reader or Compat responses

* **Symptom.** Response latency above the operator's alerting threshold.
* **First checks.** The smoke run above (each probe has a fixed timeout; a timeout is recorded as a failed check with no response). The DB posture capture, when the database is in question.
* **Escalate** to the Product Owner with the capture and the alert. **Roll back** by the release runbook when a release introduced the regression.

## Stuck queue or processing backlog

* **Symptom.** Work that should complete is not completing, as the operator's monitoring shows.
* **First checks.** The smoke run above, to confirm the service is up and serving its release identity; the DB posture capture.
* **Escalate** to the Product Owner. The queue's own inspection and recovery steps are not stated in canon and belong to the Ops Task Record.

## DB lag or degraded DB posture

* **Symptom.** Database latency, connection failures, or a posture that differs from the governed one.
* **First checks.** The smoke's DB spot-check (H-08) with the read-only `DATABASE_URL`: it compares the live search path, objects, unique constraint and not-null columns with the governed `artifacts/db` posture files, and records what it cannot compare. Offline, the governed posture files themselves:

  ```bash
  python tools/evidence/generate_db_runtime_posture.py --check
  ```

* **Escalate** to the Product Owner with the capture. **Roll back** by the release runbook only when a release changed the posture; a rollback rewrites no stored data.
