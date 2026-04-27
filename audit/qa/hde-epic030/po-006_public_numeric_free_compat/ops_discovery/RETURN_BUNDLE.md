# RETURN_BUNDLE

## EPIC_ID
hde-epic030

## STEP_NAME
Public user-facing compatibility output must remain band-only and free of numeric compatibility details

## STEP_SLUG
po-006_public_numeric_free_compat

## OUTPUT_DIR
[audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery)

## Commands run (verbatim)
```text
EPIC_ID=hde-epic030
STEP_SLUG=po-006_public_numeric_free_compat
OUTPUT_DIR=audit/qa/${EPIC_ID}/${STEP_SLUG}/ops_discovery
mkdir -p "$OUTPUT_DIR"
python --version
python -m pytest --version
command -v grep
file/existence inventory for po-006 required loci and Step-0A
parse po-006 primary.log header
capture rc values and key excerpts from po-006 artifacts
capture category_framework_binding.log numeric-free marker lines
write evidence file sha256 ledger
```

## Key outputs (short excerpts, with filenames)
1. Tool preflight from [audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/tool_preflight.txt](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/tool_preflight.txt)
- Python 3.13.5
- pytest 8.4.2
- grep at /usr/bin/grep
- python_version_rc=0, pytest_version_rc=0, grep_lookup_rc=0

2. Parsed po-006 header from [audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/primary_header_extract.json](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/primary_header_extract.json)
- parse_ok: true
- status: FAIL_BEHAVIOR
- fail_status: FAIL_BEHAVIOR
- exit_code: 1
- command_provenance: Copy/paste from approved plan with open-rails rerun requested by PO
- captured_env: SAFE_MODE=0, ALLOW_NETWORK=1, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC
- raw first line preserved in the same file

3. Step-0A discovery check from [audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/step0a_extract.json](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/step0a_extract.json)
- audit/qa/hde-epic030/checks/po-015/discovery.json exists: false
- audit/qa/hde-epic030/checks/po-015/primary.log exists: false

4. Dependency/loci inventory from [audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/artifact_inventory.tsv](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/artifact_inventory.tsv)
- Present:
  [audit/qa/hde-epic030/checks/po-006/primary.log](audit/qa/hde-epic030/checks/po-006/primary.log),
  [audit/qa/hde-epic030/checks/po-006/exit_code.txt](audit/qa/hde-epic030/checks/po-006/exit_code.txt),
  [audit/qa/hde-epic030/checks/po-006/pytest_rc.txt](audit/qa/hde-epic030/checks/po-006/pytest_rc.txt),
  [audit/qa/hde-epic030/checks/po-006/grep_rc.txt](audit/qa/hde-epic030/checks/po-006/grep_rc.txt),
  [audit/qa/hde-epic030/checks/po-006/pytest_stdout.log](audit/qa/hde-epic030/checks/po-006/pytest_stdout.log),
  [audit/qa/hde-epic030/checks/po-006/pytest_stderr.log](audit/qa/hde-epic030/checks/po-006/pytest_stderr.log),
  [audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt](audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt),
  [audit/qa/hde-epic030/checks/po-006/grep_stderr.log](audit/qa/hde-epic030/checks/po-006/grep_stderr.log),
  [audit/qa/hde-epic030/pr-05/category_framework_binding.log](audit/qa/hde-epic030/pr-05/category_framework_binding.log),
  [tests/compat/test_compat_public_ab_ba_identity.py](tests/compat/test_compat_public_ab_ba_identity.py),
  [tests/compat/test_compat_public_lf_bom.py](tests/compat/test_compat_public_lf_bom.py)
- Missing:
  audit/qa/hde-epic030/checks/po-015/discovery.json,
  audit/qa/hde-epic030/checks/po-015/primary.log

5. RC values from [audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/rc_values.json](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/rc_values.json)
- exit_code=1
- pytest_rc=1
- grep_rc=0

6. Failure signature and marker excerpts from [audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/key_excerpts.txt](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/key_excerpts.txt)
- TypeError excerpt:
  compat_public() missing 5 required positional arguments: viewer_top, viewer_weights, engine_tag, release_id, and invocation_tag
- Numeric-free marker in po-006 grep output:
  8:public_reader_bands_only_numeric_free: True
- Numeric-free marker in PR-05 binding log:
  public_reader_bands_only_numeric_free: True

## Evidence files produced (full paths + sha256 for each)
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/artifact_inventory.tsv
  sha256 d1e22189e1f40b5851db1609588082960bcf751db314c4cec25cbf236f4a6eee
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/commands_run.txt
  sha256 7e85df1aab19ba18dfdd027938d8beb947f44237a84d34e3c7bf56988a07bc4c
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/key_excerpts.txt
  sha256 2a85caf022b63f0b9afc34f03c35cbd51af1e924049c3199a24396848663f821
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/primary_header_extract.json
  sha256 4fe5357972168f3dc247643d743d849c7dea44f37670b47c8a3f6651dfd47b96
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/primary_header_extract.stderr
  sha256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/rc_values.json
  sha256 5357d87948df547177dcf03b25eab4efa50163ff7d561c362ccf8b56ef766b0a
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/step0a_extract.json
  sha256 dd2dce7a29bc51f40d3b3d2c9315257205358dd70d406dc077b209af52c526d3
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/step0a_extract.stderr
  sha256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/tool_preflight.stderr
  sha256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/tool_preflight.txt
  sha256 8e34f1bf2cdc6cff122c5c041b4a1f1b5be231e478ab430c064a4cb8a3843287
- /workspaces/glow-hdengine-v2/audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/evidence_files_sha256.txt
  sha256 captured in [audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/evidence_files_sha256.txt](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/evidence_files_sha256.txt)

## Notes (only deviations from Doc B, if any)
- Python invocations were executed with /usr/bin/python3 (workspace-configured interpreter) instead of python. The commands documented in [audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/commands_run.txt](audit/qa/hde-epic030/po-006_public_numeric_free_compat/ops_discovery/commands_run.txt) remain exactly as requested.
- No po-006 pytest behavior tests were rerun in this discovery step.
