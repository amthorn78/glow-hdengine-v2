from __future__ import annotations

import json
from pathlib import Path

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


def test_active_guidance_for_retired_bridge_key_is_rejected(tmp_path):
    _minimal_tree(tmp_path)
    _write(tmp_path, "docs/RUN.md", "Set DB_BRIDGE_URL to the bridge endpoint and run the server.\n")
    assert any("retired_key_active_guidance" in row for row in check.scan(tmp_path))


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
