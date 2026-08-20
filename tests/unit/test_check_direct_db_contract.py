from __future__ import annotations

import json
from pathlib import Path

import pytest

from ci.checks import check_direct_db_contract as check


def _write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _minimal_tree(root: Path) -> None:
    for relative, markers in check.MANDATORY_MARKERS.items():
        _write(root, relative, "\n".join(markers) + "\n")
    for relative in check.SCHEMAS:
        _write(
            root,
            relative,
            json.dumps(
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "type": "object",
                    "additionalProperties": False,
                }
            ),
        )


def test_direct_contract_scan_accepts_minimal_direct_only_tree(tmp_path):
    _minimal_tree(tmp_path)
    assert check.scan(tmp_path) == ()


def test_direct_contract_scan_requires_bounded_ops_schema_validator(tmp_path):
    _minimal_tree(tmp_path)
    (tmp_path / "tools/evidence/strict_json_schema.py").unlink()

    assert (
        "tools/evidence/strict_json_schema.py:mandatory_file_missing"
        in check.scan(tmp_path)
    )


def test_direct_contract_scan_rejects_retired_file_symbol_and_active_output(tmp_path):
    _minimal_tree(tmp_path)
    _write(tmp_path, "engine/db/providers/bridge_provider.py", "class BridgeProvider: pass\n")
    _write(tmp_path, "scripts/current.py", "OUT='artifacts/db_bridge/new.json'\n")
    violations = check.scan(tmp_path)
    assert any("retired_path_present" in row for row in violations)
    assert any("forbidden_symbol:BridgeProvider" in row for row in violations)
    assert any("active_retired_path:artifacts/db_bridge/" in row for row in violations)


def test_direct_contract_scan_allows_retired_names_only_in_refusal_rosters(tmp_path):
    _minimal_tree(tmp_path)
    adapter = tmp_path / "engine/db/adapter.py"
    adapter.write_text(
        adapter.read_text(encoding="utf-8") + "DB_BRIDGE_URL = 'refusal-name-only'\n",
        encoding="utf-8",
    )
    assert check.scan(tmp_path) == ()
    _write(tmp_path, "scripts/current.py", "import os\nprint(os.getenv('DB_BRIDGE_URL'))\n")
    assert any("active_retired_key_consumption" in row for row in check.scan(tmp_path))


def test_direct_contract_scan_allows_only_explicit_historical_doc_paths(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "docs/EVIDENCE_INDEX.md",
        "Historical retained path: `artifacts/db_bridge/health.json`; not current runtime guidance.\n",
    )
    assert check.scan(tmp_path) == ()

    _write(
        tmp_path,
        "docs/EVIDENCE_INDEX.md",
        "Run the current capture from `artifacts/db_bridge/health.json`.\n",
    )
    assert any("active_retired_path:artifacts/db_bridge/" in row for row in check.scan(tmp_path))


def test_refusal_file_cannot_hide_http_bridge_construction(tmp_path):
    _minimal_tree(tmp_path)
    adapter = tmp_path / "engine/db/adapter.py"
    adapter.write_text(
        adapter.read_text(encoding="utf-8")
        + "\nimport os, urllib.request\n"
        + "def bad():\n    return urllib.request.urlopen(os.getenv('DB_BRIDGE_URL'))\n",
        encoding="utf-8",
    )
    violations = check.scan(tmp_path)
    assert any("active_retired_key_consumption" in row or "retired_key_http_bridge_use" in row for row in violations)


def test_literal_pg_bridge_http_construction_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import urllib.request\n"
        "urllib.request.urlopen('https://pg-bridge.internal/health')\n",
    )
    assert any(
        "scripts/current.py:2:bridge_http_construction" in row
        for row in check.scan(tmp_path)
    )


def test_alternate_bridge_endpoint_alias_to_http_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os, requests\n"
        "url = os.getenv('PG_BRIDGE_ENDPOINT')\n"
        "requests.get(url)\n",
    )
    assert any(
        "scripts/current.py:3:bridge_http_construction" in row
        for row in check.scan(tmp_path)
    )


def test_curl_pg_bridge_command_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import subprocess\n"
        "subprocess.run(['curl', 'https://pg-bridge.internal/health'])\n",
    )
    assert any(
        "scripts/current.py:2:bridge_executable_command" in row
        for row in check.scan(tmp_path)
    )


def test_ordinary_http_and_subprocess_commands_remain_allowed(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import requests, subprocess\n"
        "requests.get('https://example.invalid/health')\n"
        "subprocess.run(['curl', 'https://example.invalid/health'])\n",
    )
    assert check.scan(tmp_path) == ()


def test_raw_psycopg_import_and_connect_are_rejected_outside_owned_paths(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "adapter/current.py",
        "import psycopg as pg\npg.connect('postgresql://forbidden')\n",
    )

    violations = check.scan(tmp_path)
    assert "adapter/current.py:1:unauthorized_psycopg_import" in violations
    assert "adapter/current.py:2:unauthorized_psycopg_connect" in violations


def test_raw_psycopg_connect_alias_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "from psycopg import connect as open_db\nopen_db('postgresql://forbidden')\n",
    )

    violations = check.scan(tmp_path)
    assert "scripts/current.py:1:unauthorized_psycopg_import" in violations
    assert "scripts/current.py:2:unauthorized_psycopg_connect" in violations


def test_owned_psycopg_provider_and_exact_ops_runner_seam_remain_authorized(tmp_path):
    _minimal_tree(tmp_path)
    provider = tmp_path / "engine/db/providers/psycopg_provider.py"
    provider.write_text(
        "# SET TRANSACTION READ ONLY\n"
        "# validate_readonly_statements\n"
        "# conn.rollback()\n"
        "import psycopg\n"
        "psycopg.connect('fixture')\n",
        encoding="utf-8",
    )
    runner = tmp_path / check.OPS03_RAW_PSYCOPG_OWNER
    runner.write_text(
        "# ORDERED_QUERY_IDS expected_argv authorization_bytes_changed tools.evidence.strict_json_schema\n"
        "def live_provider_factory(counters):\n"
        "    def factory(dsn):\n"
        "        def connect(value):\n"
        "            import psycopg\n"
        "            return psycopg.connect(value, connect_timeout=5)\n"
        "        return connect\n"
        "    return factory\n",
        encoding="utf-8",
    )

    assert check.scan(tmp_path) == ()


def test_ops_runner_rejects_any_second_raw_psycopg_seam(tmp_path):
    _minimal_tree(tmp_path)
    runner = tmp_path / check.OPS03_RAW_PSYCOPG_OWNER
    runner.write_text(
        "# ORDERED_QUERY_IDS expected_argv authorization_bytes_changed tools.evidence.strict_json_schema\n"
        "def live_provider_factory(counters):\n"
        "    def factory(dsn):\n"
        "        def connect(value):\n"
        "            import psycopg\n"
        "            return psycopg.connect(value, connect_timeout=5)\n"
        "        return connect\n"
        "    return factory\n"
        "import psycopg\n"
        "psycopg.connect('second')\n",
        encoding="utf-8",
    )

    violations = check.scan(tmp_path)
    assert any("unauthorized_psycopg_import" in row for row in violations)
    assert any("unauthorized_psycopg_connect" in row for row in violations)


@pytest.mark.parametrize(
    "source",
    [
        "__import__('psycopg').connect('forbidden')\n",
        "import importlib\nimportlib.import_module('psycopg').connect('forbidden')\n",
        "from importlib import import_module as load\npg = load('psycopg')\npg.connect('forbidden')\n",
    ],
)
def test_dynamic_psycopg_import_and_connect_are_rejected(tmp_path, source):
    _minimal_tree(tmp_path)
    _write(tmp_path, "scripts/current.py", source)

    violations = check.scan(tmp_path)
    assert any("unauthorized_psycopg_import" in row for row in violations)
    assert any("unauthorized_psycopg_connect" in row for row in violations)


def test_active_guidance_for_retired_bridge_key_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(tmp_path, "docs/RUN.md", "Set DB_BRIDGE_URL to the bridge endpoint and run the server.\n")
    assert any("retired_key_active_guidance" in row for row in check.scan(tmp_path))


def test_active_accepted_adr_is_scanned_for_retired_bridge_guidance(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "docs/adr/current_transport.md",
        "## Status\nAccepted\n\nConfigure DB_BRIDGE_URL and use BridgeProvider fallback.\n",
    )
    violations = check.scan(tmp_path)
    assert any("retired_key_active_guidance" in row for row in violations)
    assert any("forbidden_symbol:BridgeProvider" in row for row in violations)


def test_active_design_and_root_agent_guidance_are_scanned(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "docs/design/current_transport.md",
        "Run scripts/db_bridge/capture_introspection.py for the current fallback.\n",
    )
    _write(
        tmp_path,
        "AGENTS.md",
        "Export DB_FORCE_BRIDGE=1 to use the current fallback.\n",
    )
    violations = check.scan(tmp_path)
    assert any("active_retired_path:scripts/db_bridge/" in row for row in violations)
    assert any("AGENTS.md:1:retired_key_active_guidance" in row for row in violations)


def test_bridge_guidance_without_a_specific_key_or_path_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "docs/design/current_transport.md",
        "Use the bridge fallback when direct access fails.\n",
    )
    assert any(
        "docs/design/current_transport.md:1:bridge_active_guidance" in row
        for row in check.scan(tmp_path)
    )


def test_explicit_historical_adr_and_design_references_are_allowed(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "docs/adr/retired_transport.md",
        "Historical retained record, not current guidance: DB_BRIDGE_URL once selected BridgeProvider fallback.\n",
    )
    _write(
        tmp_path,
        "docs/design/retired_transport.md",
        "Historical retained record, not current guidance: scripts/db_bridge/capture_introspection.py wrote artifacts/db_bridge/ captures; do not run curl https://pg-bridge.invalid.\n",
    )
    assert check.scan(tmp_path) == ()


def test_historical_file_header_does_not_hide_active_guidance_line(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "docs/design/mixed_transport.md",
        "Status: historical retained record, not current guidance.\n"
        "Run scripts/db_bridge/capture_introspection.py for current fallback.\n",
    )
    assert any(
        "docs/design/mixed_transport.md:2:active_retired_path:scripts/db_bridge/"
        in row
        for row in check.scan(tmp_path)
    )


def test_executable_source_cannot_use_historical_wording_as_an_exemption(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "BridgeProvider = object  # historical retained record, not current\n",
    )
    assert any(
        "scripts/current.py:1:forbidden_symbol:BridgeProvider" in row
        for row in check.scan(tmp_path)
    )


def test_ignored_build_residue_is_not_scanned(tmp_path):
    _minimal_tree(tmp_path)
    _write(tmp_path, "build/generated.py", "BridgeProvider DB_BRIDGE_URL\n")
    assert check.scan(tmp_path) == ()

def test_refusal_roster_file_cannot_hide_retired_key_membership_consumption(tmp_path):
    _minimal_tree(tmp_path)
    adapter = tmp_path / "engine/db/adapter.py"
    adapter.write_text(
        "import os\n"
        "from os import environ\n"
        "RETIRED_DB_TRANSPORT_KEYS = ()\n"
        "def retired_db_transport_keys_present():\n    return ()\n"
        "def readonly_tx():\n    return None\n"
        "if 'DB_BRIDGE_URL' in os.environ:\n    raise RuntimeError('active')\n"
        "if 'DB_FORCE_BRIDGE' not in environ:\n    raise RuntimeError('active')\n",
        encoding="utf-8",
    )
    violations = check.scan(tmp_path)
    membership_violations = [
        row for row in violations if "active_retired_key_consumption" in row
    ]
    assert len(membership_violations) == 2


def test_aliased_os_imports_cannot_hide_retired_key_consumption(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os as operating_system\n"
        "from os import environ as env\n"
        "from os import getenv as read_env\n"
        "operating_system.getenv('DB_BRIDGE_URL')\n"
        "operating_system.environ.get('DB_FORCE_BRIDGE')\n"
        "env['DB_ALLOW_BRIDGE_IN_PROD']\n"
        "if 'DB_BRIDGE_URL' in env:\n"
        "    read_env('DB_FORCE_BRIDGE')\n",
    )
    violations = check.scan(tmp_path)
    consumption_lines = {
        int(row.split(":")[1])
        for row in violations
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4, 5, 6, 7, 8}


def test_assigned_os_symbols_cannot_hide_retired_key_consumption(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "operating_system = os\n"
        "env = operating_system.environ\n"
        "copied_env = env.copy()\n"
        "read_env = operating_system.getenv\n"
        "typed_env: object = copied_env\n"
        "if 'DB_BRIDGE_URL' in env:\n"
        "    pass\n"
        "copied_env.get('DB_FORCE_BRIDGE')\n"
        "typed_env['DB_ALLOW_BRIDGE_IN_PROD']\n"
        "read_env('DB_BRIDGE_URL')\n",
    )
    violations = check.scan(tmp_path)
    consumption_lines = {
        int(row.split(":")[1])
        for row in violations
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {7, 9, 10, 11}


def test_unimported_env_mapping_name_is_not_treated_as_os_environ(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "env = {'DB_BRIDGE_URL': 'historical-name-only'}\n"
        "assert env.get('DB_BRIDGE_URL') == 'historical-name-only'\n",
    )
    assert check.scan(tmp_path) == ()


def test_historical_reader_cannot_hide_active_retired_key_consumption(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "tools/evidence/run_sanity_pipeline.py",
        "import os\n"
        "if 'DB_ALLOW_BRIDGE_IN_PROD' in os.environ:\n"
        "    raise RuntimeError('active')\n",
    )
    assert any(
        "tools/evidence/run_sanity_pipeline.py:2:active_retired_key_consumption"
        in row
        for row in check.scan(tmp_path)
    )


def test_release_pipeline_has_no_historical_bridge_reader_exception(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "tools/evidence/run_sanity_pipeline.py",
        "HISTORICAL_BRIDGE_PRIMARY_SHA256 = {\n"
        "    'artifacts/db_bridge/health.json': 'a' * 64,\n"
        "}\n",
    )
    violations = check.scan(tmp_path)
    assert any(
        "tools/evidence/run_sanity_pipeline.py:2:active_retired_path:artifacts/db_bridge/"
        in row
        for row in violations
    )


def test_release_pipeline_cannot_hide_active_retired_evidence_path(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "tools/evidence/run_sanity_pipeline.py",
        "CURRENT = 'artifacts/db_bridge/current.json'\n",
    )
    assert any(
        "active_retired_path:artifacts/db_bridge/" in row
        for row in check.scan(tmp_path)
    )

def test_historical_reader_mapping_get_is_not_environment_consumption(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "tools/evidence/run_sanity_pipeline.py",
        "rails = {'direct': {'DB_FORCE_BRIDGE': 'UNSET'}}\n"
        "assert rails['direct'].get('DB_FORCE_BRIDGE') == 'UNSET'\n",
    )
    assert check.scan(tmp_path) == ()


def test_http_session_use_of_retired_environ_subscript_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "from os import environ\n"
        "session.get(environ['DB_BRIDGE_URL'])\n",
    )
    violations = check.scan(tmp_path)
    assert any("active_retired_key_consumption" in row for row in violations)
    assert any("retired_key_http_bridge_use" in row for row in violations)


def test_computed_retired_key_environment_to_http_flow_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os, requests\n"
        "key = 'DB_BRIDGE_URL'\n"
        "url = os.environ.get(key)\n"
        "requests.get(url)\n",
    )
    violations = check.scan(tmp_path)
    assert any("scripts/current.py:3:active_retired_key_consumption" in row for row in violations)
    assert any("scripts/current.py:4:active_retired_key_consumption" in row for row in violations)


def test_alias_tracing_uses_assignment_value_at_read_site(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "key = 'DB_BRIDGE_URL'\n"
        "os.getenv(key)\n"
        "key = 'SAFE_MODE'\n",
    )
    assert any(
        "scripts/current.py:3:active_retired_key_consumption" in row
        for row in check.scan(tmp_path)
    )


def test_alias_tracing_scans_function_and_control_flow_bodies(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "def f():\n"
        "    key = 'DB_BRIDGE_URL'\n"
        "    os.getenv(key)\n"
        "if True:\n"
        "    key = 'DB_FORCE_BRIDGE'\n"
        "    os.environ.get(key)\n",
    )
    violations = check.scan(tmp_path)
    assert any(
        "scripts/current.py:4:active_retired_key_consumption" in row
        for row in violations
    )
    assert any(
        "scripts/current.py:7:active_retired_key_consumption" in row
        for row in violations
    )


def test_compound_body_scans_apply_inner_aliases_before_reads(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "key = 'DB_BRIDGE_URL'\n"
        "def f():\n"
        "    key = 'SAFE_MODE'\n"
        "    os.getenv(key)\n"
        "if True:\n"
        "    key = 'SAFE_MODE'\n"
        "    os.environ.get(key)\n"
        "for key in ('SAFE_MODE',):\n"
        "    os.getenv(key)\n",
    )
    assert check.scan(tmp_path) == ()


def test_compound_statement_headers_remain_scanned(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "if os.getenv('DB_BRIDGE_URL'):\n"
        "    pass\n"
        "for value in (os.environ['DB_FORCE_BRIDGE'],):\n"
        "    pass\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {2, 4}


def test_function_parameters_clear_same_named_outer_aliases(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "key = 'DB_BRIDGE_URL'\n"
        "def read(key):\n"
        "    return os.getenv(key)\n",
    )
    assert check.scan(tmp_path) == ()


def test_function_defaults_preserve_captured_retired_aliases(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "key = 'DB_BRIDGE_URL'\n"
        "def captured(key=key):\n"
        "    return os.getenv(key)\n"
        "def direct(other='DB_FORCE_BRIDGE'):\n"
        "    return os.environ.get(other)\n"
        "def keyword_only(*, third=key):\n"
        "    return os.environ[third]\n"
        "def safe(key='SAFE_MODE'):\n"
        "    return os.getenv(key)\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4, 6, 8}


def test_compound_block_aliases_propagate_to_following_reads(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "from contextlib import nullcontext\n"
        "if True:\n"
        "    key = 'DB_BRIDGE_URL'\n"
        "os.getenv(key)\n"
        "while False:\n"
        "    other = 'DB_FORCE_BRIDGE'\n"
        "os.environ.get(other)\n"
        "with nullcontext():\n"
        "    third = 'DB_ALLOW_BRIDGE_IN_PROD'\n"
        "os.environ[third]\n"
        "try:\n"
        "    fourth = 'DB_BRIDGE_URL'\n"
        "except Exception:\n"
        "    pass\n"
        "os.getenv(fourth)\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {5, 8, 11, 16}


def test_all_if_branches_can_replace_retired_alias_with_safe_value(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "key = 'DB_BRIDGE_URL'\n"
        "if condition:\n"
        "    key = 'SAFE_MODE'\n"
        "else:\n"
        "    key = 'APP_ENV'\n"
        "os.getenv(key)\n",
    )
    assert check.scan(tmp_path) == ()


def test_alias_tracing_binds_loop_targets_before_body_scan(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "keys = ('DB_BRIDGE_URL', 'DB_FORCE_BRIDGE')\n"
        "for key in keys:\n"
        "    os.getenv(key)\n"
        "def nested():\n"
        "    nested_keys = ('DB_ALLOW_BRIDGE_IN_PROD',)\n"
        "    for nested_key in nested_keys:\n"
        "        os.environ.get(nested_key)\n"
        "safe_keys = ('SAFE_MODE',)\n"
        "for safe_key in safe_keys:\n"
        "    os.getenv(safe_key)\n",
    )
    violations = check.scan(tmp_path)
    consumption_lines = {
        int(row.split(":")[1])
        for row in violations
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4, 8}


def test_alias_tracing_binds_destructured_literal_loop_targets(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "for key, ignored in (('DB_BRIDGE_URL', None),):\n"
        "    os.getenv(key)\n"
        "for ignored, other in ((None, 'DB_FORCE_BRIDGE'),):\n"
        "    os.environ.get(other)\n"
        "for safe, ignored in (('SAFE_MODE', None),):\n"
        "    os.getenv(safe)\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {3, 5}


def test_alias_tracing_binds_comprehension_targets_before_reads(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "keys = ('DB_BRIDGE_URL',)\n"
        "[os.getenv(key) for key in keys]\n"
        "[os.environ.get(key) for key, _ in (('DB_FORCE_BRIDGE', None),)]\n"
        "tuple(os.getenv(key) for key in ('DB_ALLOW_BRIDGE_IN_PROD',))\n"
        "key = 'DB_BRIDGE_URL'\n"
        "[os.getenv(key) for key in ('SAFE_MODE',)]\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {3, 4, 5}


def test_module_constants_are_visible_to_earlier_function_bodies(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "def read():\n"
        "    key = BRIDGE_KEY\n"
        "    return os.getenv(key)\n"
        "BRIDGE_KEY = 'DB_BRIDGE_URL'\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4}


def test_function_local_constants_do_not_leak_across_scopes(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "def define_local():\n"
        "    local_key = 'DB_BRIDGE_URL'\n"
        "def read_other_scope():\n"
        "    return os.getenv(local_key)\n",
    )
    assert not any(
        "scripts/current.py" in row and "active_retired_key_consumption" in row
        for row in check.scan(tmp_path)
    )


def test_lambda_parameters_shadow_outer_aliases_and_bind_defaults(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "key = 'DB_BRIDGE_URL'\n"
        "safe = lambda key: os.getenv(key)\n"
        "captured = lambda key=key: os.getenv(key)\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4}


def test_with_and_exception_targets_shadow_outer_aliases(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "key = 'DB_BRIDGE_URL'\n"
        "with manager() as key:\n"
        "    os.getenv(key)\n"
        "try:\n"
        "    pass\n"
        "except Exception as key:\n"
        "    os.getenv(key)\n",
    )
    assert not any(
        "scripts/current.py" in row and "active_retired_key_consumption" in row
        for row in check.scan(tmp_path)
    )


def test_canonical_retired_roster_imports_bind_loop_aliases(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS\n"
        "for key in RETIRED_DB_TRANSPORT_KEYS:\n"
        "    os.getenv(key)\n"
        "def nested():\n"
        "    from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS as roster\n"
        "    return [os.environ.get(key) for key in roster]\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4, 7}


def test_unrelated_same_named_import_is_not_the_canonical_roster(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "from unrelated import RETIRED_DB_TRANSPORT_KEYS\n"
        "for key in RETIRED_DB_TRANSPORT_KEYS:\n"
        "    os.getenv(key)\n",
    )
    assert not any(
        "scripts/current.py" in row and "active_retired_key_consumption" in row
        for row in check.scan(tmp_path)
    )


def test_module_qualified_canonical_rosters_bind_loop_aliases(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "import engine.db.adapter as adapter\n"
        "for key in adapter.RETIRED_DB_TRANSPORT_KEYS:\n"
        "    os.getenv(key)\n"
        "from engine.db import adapter as db_adapter\n"
        "[os.environ.get(key) for key in db_adapter.RETIRED_DB_TRANSPORT_KEYS]\n"
        "import engine.db.adapter\n"
        "for key in engine.db.adapter.RETIRED_DB_TRANSPORT_KEYS:\n"
        "    os.getenv(key)\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4, 6, 9}


def test_unrelated_module_qualified_roster_is_not_canonical(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "import unrelated as adapter\n"
        "for key in adapter.RETIRED_DB_TRANSPORT_KEYS:\n"
        "    os.getenv(key)\n",
    )
    assert not any(
        "scripts/current.py" in row and "active_retired_key_consumption" in row
        for row in check.scan(tmp_path)
    )


def test_roster_wrapper_calls_bind_loop_and_enumerate_targets(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS as roster\n"
        "for key in list(roster):\n"
        "    os.getenv(key)\n"
        "for key in tuple(roster):\n"
        "    os.environ.get(key)\n"
        "for _, key in enumerate(sorted(roster)):\n"
        "    os.getenv(key)\n"
        "for key, _ in list((('DB_BRIDGE_URL', None),)):\n"
        "    os.getenv(key)\n"
        "for key in list(('SAFE_MODE',)):\n"
        "    os.getenv(key)\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4, 6, 8, 10}


def test_constant_computed_retired_key_strings_are_resolved(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "prefix = 'DB_'\n"
        "bridge = prefix + 'BRIDGE_URL'\n"
        "os.getenv(bridge)\n"
        "force = f'{prefix}FORCE_BRIDGE'\n"
        "os.environ.get(force)\n"
        "allow = f\"DB_ALLOW_{'BRIDGE_IN_PROD'}\"\n"
        "os.environ[allow]\n"
        "safe = 'SAFE_' + 'MODE'\n"
        "os.getenv(safe)\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {4, 6, 8}


def test_signed_sliced_and_dynamic_roster_subscripts_are_resolved(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS as roster\n"
        "os.getenv(roster[-1])\n"
        "for key in roster[:2]:\n"
        "    os.getenv(key)\n"
        "for key in roster[::-1]:\n"
        "    os.environ.get(key)\n"
        "index = 1\n"
        "os.getenv(roster[index])\n"
        "for key in roster[:0]:\n"
        "    os.getenv(key)\n"
        "safe = ('SAFE_MODE',)\n"
        "os.getenv(safe[-1])\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {3, 5, 7, 9}


def test_zipped_rosters_bind_corresponding_loop_targets(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS as roster\n"
        "labels = ('allow', 'url', 'force')\n"
        "for key, _ in zip(roster, labels):\n"
        "    os.getenv(key)\n"
        "for _, key in zip(labels, list(roster)):\n"
        "    os.environ.get(key)\n"
        "for key, _ in zip(('SAFE_MODE',), labels):\n"
        "    os.getenv(key)\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {5, 7}


def test_walrus_aliases_are_bound_before_retired_key_reads(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "if (key := 'DB_BRIDGE_URL'):\n"
        "    os.getenv(key)\n"
        "os.getenv(other := 'DB_FORCE_BRIDGE')\n"
        "os.environ[third := 'DB_ALLOW_BRIDGE_IN_PROD']\n"
        "(later := 'DB_BRIDGE_URL')\n"
        "os.getenv(later)\n"
        "os.getenv(safe := 'SAFE_MODE')\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {3, 4, 5, 7}


def test_unresolved_computed_environment_value_read_fails_closed(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "def read(bridge_key):\n"
        "    return os.environ.get(bridge_key)\n",
    )
    assert any(
        "scripts/current.py:3:active_retired_key_consumption" in row
        for row in check.scan(tmp_path)
    )


def test_unresolved_environment_subscript_fails_closed(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "scripts/current.py",
        "import os\n"
        "def read(bridge_key):\n"
        "    return os.environ[bridge_key]\n"
        "def safe(safe_key):\n"
        "    return os.environ[safe_key]\n",
    )
    consumption_lines = {
        int(row.split(":")[1])
        for row in check.scan(tmp_path)
        if "scripts/current.py" in row and "active_retired_key_consumption" in row
    }
    assert consumption_lines == {3}


def test_active_guidance_cannot_hide_behind_retired_context(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "docs/RUN.md",
        "Set retired DB_BRIDGE_URL to the bridge endpoint.\n",
    )
    assert any(
        "retired_key_active_guidance" in row for row in check.scan(tmp_path)
    )


def test_negated_and_historical_retained_key_lines_remain_refusal_only(tmp_path):
    _minimal_tree(tmp_path)
    _write(
        tmp_path,
        "docs/SECRETS.md",
        "Do not set retired DB_BRIDGE_URL to an endpoint; it must remain absent.\n"
        "Historical retained evidence records DB_FORCE_BRIDGE was set to REDACTED; "
        "this is not current guidance.\n",
    )
    assert check.scan(tmp_path) == ()
