from argparse import Namespace

import pytest

from scripts.ops.hde_epic038_mapped_cache_smoke import _preflight


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
