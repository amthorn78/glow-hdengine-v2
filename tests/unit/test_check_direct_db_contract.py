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
