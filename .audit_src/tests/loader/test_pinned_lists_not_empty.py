from __future__ import annotations
import json
from pathlib import Path

def test_iso_and_iana_lists_present_and_include_exemplars():
    iso = json.loads(Path("artifacts/constants/iso_3166_1_alpha2.json").read_text(encoding="utf-8"))
    iana = json.loads(Path("artifacts/constants/iana_tz_list.json").read_text(encoding="utf-8"))
    assert isinstance(iso, list) and "US" in iso and "NL" in iso
    assert isinstance(iana, list) and "UTC" in iana and "Europe/Amsterdam" in iana
