import hashlib
import json

from engine.serializer.canon import sercanon
from tools.generate_registry_report import build_registry_report


def _render_current_report() -> bytes:
    return sercanon(build_registry_report(), sort_keys=True)


def test_registry_report_two_run_identity() -> None:
    first = _render_current_report()
    second = _render_current_report()
    assert first == second
    data = json.loads(first.decode("utf-8"))
    assert data["schema"] == "registry_report.v1"
    assert first.endswith(b"\n")
    assert hashlib.sha256(first).hexdigest() == hashlib.sha256(second).hexdigest()
