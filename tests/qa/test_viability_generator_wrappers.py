import importlib
import json
from pathlib import Path

import pytest

from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, ViabilityResult, record_check


MODULES = (
    "tools.qa.generate_epic027_close_pack",
    "tools.qa.generate_epic028_acceptance_ledger",
    "tools.qa.generate_epic029_close_pack",
)


@pytest.mark.parametrize("module_name", MODULES)
def test_generator_wrapper_binds_verified_returned_ledger(
    module_name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    number = module.EPIC_ID.removeprefix("HDE-EPIC")
    ledger = tmp_path / f"audit/qa/hde-epic{number}/acceptance_map_viability.log"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(
        json.dumps({"epic_id": module.EPIC_ID, "status": "PASS", "status_reason": "", "token_status": {}}) + "\n",
        encoding="utf-8",
    )
    config = HarnessConfig(module.EPIC_ID, repo_root=tmp_path)
    primary, manifest = record_check(
        config,
        CheckResult("acceptance-map-viability", Status.PASS, exit_code=0),
    )
    result = ViabilityResult(Status.PASS, "", primary, manifest, ledger, {})
    calls = []
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", ledger)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: calls.append((config, kwargs)) or result,
    )
    module._write_viability_log()
    assert calls[0][1] == {"publish_governed_ledger": True}


@pytest.mark.parametrize("module_name", MODULES)
@pytest.mark.parametrize("status", [Status.FAIL_BEHAVIOR, Status.FAIL_TOOLING, Status.TOOLING_BLOCKED, Status.PARKED])
def test_generator_wrapper_stops_on_every_non_pass(
    module_name: str, status: Status, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    number = module.EPIC_ID.removeprefix("HDE-EPIC")
    ledger = tmp_path / f"audit/qa/hde-epic{number}/acceptance_map_viability.log"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", ledger)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: ViabilityResult(status, "blocked", None, None, None, {}),
    )
    with pytest.raises(SystemExit, match=f"ACCEPTANCE_MAP_VIABILITY_{status.value}"):
        module._write_viability_log()


@pytest.mark.parametrize("module_name", MODULES)
def test_generator_wrapper_rejects_stale_or_mismatched_ledger(
    module_name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    number = module.EPIC_ID.removeprefix("HDE-EPIC")
    ledger = tmp_path / f"audit/qa/hde-epic{number}/acceptance_map_viability.log"
    ledger.parent.mkdir(parents=True)
    ledger.write_text(json.dumps({"epic_id": "HDE-EPIC999", "status": "PASS"}) + "\n", encoding="utf-8")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", ledger)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: ViabilityResult(Status.PASS, "", tmp_path / "primary", tmp_path / "manifest", ledger, {}),
    )
    with pytest.raises(SystemExit, match="STALE_OR_MISMATCHED"):
        module._write_viability_log()


@pytest.mark.parametrize("module_name", MODULES)
def test_generator_wrapper_rejects_missing_pass_outputs(
    module_name: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(module_name)
    number = module.EPIC_ID.removeprefix("HDE-EPIC")
    ledger = tmp_path / f"audit/qa/hde-epic{number}/acceptance_map_viability.log"
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", ledger)
    monkeypatch.setattr(
        module.qa_harness,
        "generate_acceptance_map_viability",
        lambda config, **kwargs: ViabilityResult(Status.PASS, "", None, None, None, {}),
    )
    with pytest.raises(SystemExit, match="LEDGER_MISMATCH"):
        module._write_viability_log()
