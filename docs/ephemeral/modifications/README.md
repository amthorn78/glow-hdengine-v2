# Modifications

One file per Modification, the unit of approval in the GCFPE MGMT change process (`D20`).

    MODIFICATION-<yyyymmdd>-<slug>.md

Format and rules: `docs/prompt_ecosystem_management/modification-template.md`
Validate:         `docs/prompt_ecosystem_management/modification_validate.py`
Closure and tier: `docs/prompt_ecosystem_management/closure.py`
Intake:           `docs/prompt_ecosystem_management/modification-intake-triage-prompt.md`

`status` makes "what is open" a query rather than a reading exercise:

    grep -h '^status:' docs/ephemeral/modifications/MODIFICATION-*.md | sort | uniq -c
