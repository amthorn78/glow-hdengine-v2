import pytest
from pathlib import Path
from tools.evidence.retained_evidence_safety import validate_retained_text_safety, RAW_PAYLOAD_MARKERS

def errs(text: str): return validate_retained_text_safety(Path('x'), text.encode())
@pytest.mark.parametrize('marker', sorted(RAW_PAYLOAD_MARKERS))
@pytest.mark.parametrize('style', ['{}', '"{}"', "'{}'"])
@pytest.mark.parametrize('delim', [':','='])
@pytest.mark.parametrize('value', ['false','FALSE','null','NULL','"none"','"REDACTED"'])
def test_safe_marker_forms(marker, style, delim, value):
    assert errs(f'{style.format(marker)} {delim} {value}\n') == ()
@pytest.mark.parametrize('value', ['', '[]', '{}', '|', '${HD_API_KEY:-live-secret}', '${GEO_API_KEY:=live-secret}', '$(cat secret)', '$HD_API_KEY', 'redacted', "'redacted'", '<redacted>', 'some text'])
def test_unsafe_marker_values(value):
    assert 'UNSAFE_RAW_PAYLOAD_MARKER_VALUE' in errs(f'raw_vendor_payload: {value}\n')
def test_substrings_do_not_match():
    assert errs('not_raw_vendor_payload: secret\nraw_vendor_payload_copy: secret\n') == ()
def test_secret_patterns_are_nonsecret_codes():
    assert 'UNREDACTED_CREDENTIAL_VALUE' in errs('HD_API_KEY=${HD_API_KEY:-live-secret}\n')
    assert 'UNREDACTED_CREDENTIAL_VALUE' in errs('GEO_API_KEY=$(cat secret)\n')
    assert validate_retained_text_safety(Path('x'), b'\xff') == ('NON_UTF8_RETAINED_TEXT',)
