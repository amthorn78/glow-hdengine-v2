---
P-0 delegation (verbatim):
I, Nathan (Product Owner), delegate execution of Ops task HDE-EPIC040-OPS01 to this session.
Objective: build and verify the strict release attestation for release 1.3.0.
Target: a clean checkout of main in this workspace, with output to an empty directory outside the repository.
Scope: exactly the preflight, operations, adverse checks and evidence commit in docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.0.md, and nothing else.
Record this message verbatim as P-0 in the execution log.
---
Date UTC:
Sun Sep 27 00:58:15 UTC 2026
---
Preflight P-1/P-2/P-3/P-4/P-5
6f53d828a30101bb7cd6638f3695eb82c2b10979
git_rev_exit:0
pytest 8.4.2
pytest_exit:0
?? audit/ops/hde-epic040/
git_status_exit:0
release_check_exit:0
AdmittedMechanicsBundle
registry_probe_exit:0
---
RELEASE_ATTESTATION_FAILED:source_tree_not_clean
build_exit:1
RELEASE_ATTESTATION_FAILED:attestation_root_inventory_invalid
verify_exit:1
---
Adverse checks
RELEASE_ATTESTATION_FAILED:source_tree_not_clean
A1_exit:1
RELEASE_ATTESTATION_FAILED:output_root_must_be_outside_source
A2_exit:1
RELEASE_ATTESTATION_FAILED:output_root_not_empty
A3_exit:1
RELEASE_ATTESTATION_FAILED:output_root_symlink_refused
A4_exit:1
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
  File "/usr/local/lib/python3.11/pathlib.py", line 1058, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.11/pathlib.py", line 1044, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/hde-epic040-ops01-a5/attestation.json'
RELEASE_ATTESTATION_FAILED:attestation_root_inventory_invalid
A5_exit:1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
StopIteration
RELEASE_ATTESTATION_FAILED:attestation_root_inventory_invalid
A6_exit:1
RELEASE_ATTESTATION_FAILED:source_tree_not_clean
A7_exit:1
---
Evidence bundle dir:
drwx------+ 2 vscode vscode 4096 Sep 27 00:58 /tmp/hde-epic040-attestation.GcI9zL
Bundle files:
total 4
-rw-r--rw- 1 vscode vscode 141 Sep 27 00:58 failure.json
Bundle evidence:
ls: cannot access '/tmp/hde-epic040-attestation.GcI9zL/evidence': No such file or directory

--- final git status ---
?? audit/ops/hde-epic040/
