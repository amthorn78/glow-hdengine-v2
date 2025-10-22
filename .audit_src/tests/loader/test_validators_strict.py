from __future__ import annotations
import pytest
from engine.util.input_validators import (
    parse_date_yyyy_mm_dd, parse_time_hh_mm, parse_place_city_cc,
    parse_tz_iana, ensure_cid
)

def test_parse_date_good_and_bad():
    assert str(parse_date_yyyy_mm_dd("1990-01-31")) == "1990-01-31"
    with pytest.raises(ValueError):
        parse_date_yyyy_mm_dd("1990-02-30")
    with pytest.raises(ValueError):
        parse_date_yyyy_mm_dd("90-01-01")

def test_parse_time_good_and_bad():
    assert parse_time_hh_mm("00:00") == (0,0)
    assert parse_time_hh_mm("23:59") == (23,59)
    with pytest.raises(ValueError):
        parse_time_hh_mm("24:00")
    with pytest.raises(ValueError):
        parse_time_hh_mm("7:00")

def test_parse_place_city_cc_unicode_and_iso():
    city, cc = parse_place_city_cc("São Paulo, br")
    assert city == "São Paulo" and cc == "BR"
    with pytest.raises(ValueError):
        parse_place_city_cc("Nowhere")
    with pytest.raises(ValueError):
        parse_place_city_cc("City, XXX")

def test_parse_tz_iana_good_and_bad():
    assert parse_tz_iana("Europe/Amsterdam") == "Europe/Amsterdam"
    with pytest.raises(ValueError):
        parse_tz_iana("Europe/NotARealCity")
    with pytest.raises(ValueError):
        parse_tz_iana("")

def test_ensure_cid_regex():
    a = ensure_cid(None)
    b = ensure_cid("CID-deadbeefdeadbeef")
    assert a.startswith("CID-") and len(a) == 20
    assert b == "CID-deadbeefdeadbeef"
