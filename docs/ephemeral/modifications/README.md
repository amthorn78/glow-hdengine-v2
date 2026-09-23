# Modifications

One file per run. Everything handed in together is one Modification, with its changes grouped
into parts: a part lands whole or not at all (`D21`, which refines `D20`).

    MODIFICATION-<yyyymmdd>-<slug>.md

Format and rules: `docs/prompt_ecosystem_management/modification-template.md`
Validate:         `docs/prompt_ecosystem_management/modification_validate.py`
Closure and tier: `docs/prompt_ecosystem_management/closure.py`
Intake:           Notion — "Modification Intake and Triage", a child of the redesign tracking page (a persistent prompt, so not kept in the repository)

`status` makes "what is open" a query rather than a reading exercise:

    grep -h '^status:' docs/ephemeral/modifications/MODIFICATION-*.md | sort | uniq -c
