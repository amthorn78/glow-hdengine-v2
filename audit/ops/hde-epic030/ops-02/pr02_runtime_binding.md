# OPS-02 PR-02 Runtime Binding Proof

Scope:

Prove the runtime used for OPS-02 contains PR-02 birth-only remediation behavior and does not require caller user_id or caller person_uid for vendor-source birth-only showcompat command execution.

Runtime provenance (available proof):

- git branch at evidence assembly: main
- git commit at evidence assembly: 7a4804ff6607b5ac728c63aa7c2e397bfc88f9d6
- working tree at evidence assembly: dirty (non-OPS files changed outside this binding proof)

Birth-only boundary helper excerpt (source-level runtime proof):

File: engine/cli/main.py

def _vendor_inputs_from_args(args: argparse.Namespace, prefix: str) -> VendorInputs:
    birthdate = getattr(args, f"birthdate_{prefix}", None)
    birthtime = getattr(args, f"birthtime_{prefix}", None)
    location = getattr(args, f"location_{prefix}", None)
    missing = [name for name, value in (("birthdate", birthdate), ("birthtime", birthtime), ("location", location)) if not (value and value.strip())]
    if missing:
        raise CliError("MISSING_VENDOR_INPUT")
    base = {"birthdate": birthdate.strip(), "birthtime": birthtime.strip(), "location": location.strip()}
    user_id = _derive_uid(base)
    return VendorInputs(
        user_id=user_id,
        birthdate=base["birthdate"],
        birthtime=base["birthtime"],
        location=base["location"],
    )

Interpretation:

- vendor path requires birthdate, birthtime, and location fields
- caller user_id is not required as input for vendor-source showcompat path
- caller person_uid is not required as input for vendor-source showcompat path
- internal uid derivation is implementation-internal and not caller identity input

Accepted PR-02 birth-only proof name (canonical record):

- test_no_user_boundary_accepts_birth_only_input_without_person_uid_or_user_id_and_is_ab_ba_stable
- Canon references: docs/pfcanon/PF10-HDE-Build-Notes-v10.6.9.md lines 5336 and 5637

Executable runtime proof test command and pass result:

- command: /usr/bin/python3 -m pytest -q tests/cli/test_showcompat_sources.py::test_showcompat_vendor_dry_run
- result: 1 passed in 0.06s
- command verifies showcompat vendor path accepts birth-only args with source vendor and succeeds without caller user_id/person_uid input fields

Required truth lines:

- PR-02 remediation present in runtime: true
- birth-only boundary implemented: true
- no caller user_id required: true
- no caller person_uid required: true
- target runtime used for OPS-02 includes PR-02 remediation: true