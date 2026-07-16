from argparse import Namespace

import pytest

from scripts.ops.hde_epic038_mapped_cache_smoke import SINGLE_REQUEST_RETRY, _preflight, main


def args():
    return Namespace(
        synthetic_user_id="00000000-0000-4000-8000-000000000039",
        synthetic_person_uid="fixture-person",
        birthdate="fixture-date",
        birthtime="fixture-time",
        location="fixture-location",
    )


def configure(monkeypatch, base_url):
    for key, value in {
        "SAFE_MODE":"0", "ALLOW_NETWORK":"1", "APP_ENV":"test",
        "HD_API_BASE_URL":base_url, "HD_API_KEY":"set", "GEO_API_KEY":"set", "DATABASE_URL":"set",
    }.items():
        monkeypatch.setenv(key, value)


def test_preflight_accepts_only_configured_v2_chart_base(monkeypatch):
    configure(monkeypatch, "https://fixture.invalid/v2")
    _preflight(args())


@pytest.mark.parametrize("base_url", ["https://fixture.invalid/v1", "https://fixture.invalid", "https://fixture.invalid/v3"])
def test_preflight_refuses_non_v2_base_before_io(monkeypatch, base_url):
    configure(monkeypatch, base_url)
    with pytest.raises(SystemExit, match="configured-v2 charts route"):
        _preflight(args())


@pytest.mark.parametrize("user_id", ["00000000000040008000000000000039", "{00000000-0000-4000-8000-000000000039}", "AAAAAAAA-AAAA-4AAA-8AAA-AAAAAAAAAAAA"])
def test_preflight_refuses_noncanonical_uuid_before_io(monkeypatch, user_id):
    configure(monkeypatch, "https://fixture.invalid/v2")
    value = args()
    value.synthetic_user_id = user_id
    with pytest.raises(SystemExit, match="canonical UUID form"):
        _preflight(value)


def test_database_is_health_checked_before_vendor_fetch(monkeypatch):
    configure(monkeypatch, "https://fixture.invalid/v2")
    calls = []
    class DB:
        def health(self):
            calls.append("db_health")
            raise RuntimeError("unavailable")
    monkeypatch.setattr("scripts.ops.hde_epic038_mapped_cache_smoke.DBAccess.for_current_env", lambda **kwargs: DB())
    monkeypatch.setattr("scripts.ops.hde_epic038_mapped_cache_smoke.HdApiClient.from_env", lambda **kwargs: calls.append("vendor") or None)
    with pytest.raises(RuntimeError, match="unavailable"):
        main(["--synthetic-user-id", args().synthetic_user_id, "--synthetic-person-uid", "fixture", "--birthdate", "fixture", "--birthtime", "fixture", "--location", "fixture"])
    assert calls == ["db_health"]


def test_vendor_client_is_pinned_to_one_attempt_and_result_is_verified(monkeypatch):
    configure(monkeypatch, "https://fixture.invalid/v2")
    captured = {}

    class DB:
        def health(self):
            return None

    class Client:
        def build_contract_route_request(self, **kwargs):
            return object()

        def fetch(self, request):
            return type("VendorResult", (), {"attempts": 2, "payload": {}})()

    def client_from_env(**kwargs):
        captured.update(kwargs)
        return Client()

    monkeypatch.setattr("scripts.ops.hde_epic038_mapped_cache_smoke.DBAccess.for_current_env", lambda **kwargs: DB())
    monkeypatch.setattr("scripts.ops.hde_epic038_mapped_cache_smoke.HdApiClient.from_env", client_from_env)

    with pytest.raises(SystemExit, match="attempt count must equal one"):
        main(["--synthetic-user-id", args().synthetic_user_id, "--synthetic-person-uid", "fixture", "--birthdate", "fixture", "--birthtime", "fixture", "--location", "fixture"])

    assert captured["retry"] == SINGLE_REQUEST_RETRY
