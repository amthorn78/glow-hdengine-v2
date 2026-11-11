# HDE-CRD-0003 WU-OPS-01 attempt 1: Glow Infrastructure doc-delta candidate

Operator observations in Railway (project ample-illumination, service glow-hdengine-v2), recorded 2026-11-10T23:56:49Z. A candidate for the canon owner; it is not canon and changes no PF document.

- Glow Infrastructure §3.1 and §4.1, deploy source and trigger: repo amthorn78/glow-hdengine-v2, branch main; auto-deploy toggle not shown by Railway CLI, inferred on from three consecutive main-commit deployments with reason deploy
- §4.1, builder: RAILPACK
- §4.1, build command (not recorded in canon): NONE (comparison: NO_CUSTOM_COMMAND)
- §4.1 and §10, live start setting against the checked-in declarations: python -m pip install --no-cache-dir -r requirements.txt && python -m gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30 (comparison: MATCHES_SERVICE_CMD)
- Active deployment at the time of observation: commit 3570be826f1fe36323ed67471f327078b62e4667, status SUCCESS (comparison: CANDIDATE)
