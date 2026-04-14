# Approved Remediation Plan EPIC029

## Work Item W-004

- Work type: OPS
- Intent: Execute the minimum OPS remediation needed to close HDE-CONJ001.4 by validating the canonical dev sampler binding and recording governed per-environment disposition evidence.
- Closure rule: codespaces must be independently validated. local_dev may be satisfied either by independent local-dev validation or, when the canonical binding is the same loopback DEV_SAMPLER_URL already validated in Codespaces and no distinct local-dev binding is defined for this epic, by explicit binding-equivalence closure recorded in the governed evidence.
- Why needed: The environment story must be closed truthfully without forcing a fictitious second runtime when the epic canonical binding is the same.
- Dependencies: W-002 sequencing correction approved; canonical DEV_SAMPLER_URL available; no separate local-dev binding required for this epic unless explicitly defined elsewhere.
- Risks: Evidence must say "binding-equivalence closure" explicitly and must not imply an independently exercised second runtime.

## Scope Guard

This is a bounded documentation-and-evidence remediation.
It does not require a new OPS rerun, a new environment-validation pass, runtime code changes, route/port changes, or test changes.
