from __future__ import annotations

import pytest

from engine.charts.pure import BirthInputs, ChartInputError, normalize_chart, validate_birth_inputs

ISO = frozenset({"NL", "US"})
IANA = frozenset({"Europe/Amsterdam"})
FIXTURE_CHART = {
    "gates": [1, 2, 3], "channels_short": [], "centers": [], "type": "", "authority": "",
    "profile": "", "meta": {"provider": "fixtures", "source": "default"},
}


def _validate(birthdate="1990-01-01", birthtime="12:34", place="Amsterdam, NL", tz="Europe/Amsterdam"):
    return validate_birth_inputs(birthdate, birthtime, place, tz, iso_codes=ISO, iana_zones=IANA)


def _error(**kwargs):
    with pytest.raises(ChartInputError) as ei:
        _validate(**kwargs)
    return ei.value.code, ei.value.details, ei.value.message


def test_valid_inputs_return_the_parsed_values():
    assert _validate() == BirthInputs((1990, 1, 1), (12, 34), "Amsterdam", "NL", "Europe/Amsterdam")
    # The compat-determinism generator's two inputs.
    assert _validate("1990-05-04", "14:22", "Austin, US") == BirthInputs((1990, 5, 4), (14, 22), "Austin", "US", "Europe/Amsterdam")
    assert _validate("1992-07-19", "08:05", "New York, US") == BirthInputs((1992, 7, 19), (8, 5), "New York", "US", "Europe/Amsterdam")


@pytest.mark.parametrize(
    "kwargs,field,message",
    [
        ({"birthdate": "1990-02-30"}, "date", "invalid date"),
        ({"birthtime": "24:00"}, "time", "invalid time"),
        ({"place": "Nowhere"}, "place", "invalid place"),
        ({"tz": None}, "tz", "tz required on internal path"),
        ({"tz": "Europe/NotARealCity"}, "tz", "invalid tz"),
    ],
)
def test_each_invalid_field_raises_the_typed_error(kwargs, field, message):
    assert _error(**kwargs) == ("READER_INVALID_INPUT", {"field": field}, message)


def test_checks_run_in_the_loaders_order():
    assert _error(birthdate="1990-02-30", birthtime="24:00", place="Nowhere", tz=None)[1] == {"field": "date"}
    assert _error(birthtime="24:00", place="Nowhere", tz=None)[1] == {"field": "time"}
    assert _error(place="Nowhere", tz=None)[1] == {"field": "place"}


def test_normalize_chart_returns_the_fixture_chart_unchanged_and_copies_it():
    src = dict(FIXTURE_CHART)
    out = normalize_chart(src)
    assert out == FIXTURE_CHART and out is not src
    assert list(out) == list(FIXTURE_CHART)
