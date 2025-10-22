import pytest
from adapter.etag_core import reader_response, writer_headers, VARY_VAL, READER_CACHE, NO_STORE

BYTES = b'{"reader_version":"v1"}\n'
HASH  = "a"*64  # lowercase hex

def _H(d):  # Title-case for assertions without framework specifics
    return {k.title(): v for k, v in d.items()}

def test_get_200_has_strong_quoted_etag_and_headers():
    status, headers, body = reader_response(BYTES, HASH, if_none_match=None, method="GET")
    hh = _H(headers)
    assert status == 200
    assert hh["Etag"] == f"\"{HASH}\""
    assert "Authorization" in hh["Vary"] and "Accept-Encoding" in hh["Vary"]
    assert hh["Cache-Control"] == READER_CACHE
    assert body == BYTES
    assert "Content-Length" not in hh  # body present

def test_get_304_on_exact_match_with_empty_body_and_parity_headers():
    inm = f"\"{HASH}\""
    status, headers, body = reader_response(BYTES, HASH, if_none_match=inm, method="GET")
    hh = _H(headers)
    assert status == 304
    assert body == b""
    assert hh["Etag"] == f"\"{HASH}\""
    assert hh["Cache-Control"] == READER_CACHE
    assert "Authorization" in hh["Vary"] and "Accept-Encoding" in hh["Vary"]
    assert hh.get("Content-Length") == "0"

def test_head_miss_200_empty_body_same_headers():
    status, headers, body = reader_response(BYTES, HASH, if_none_match=None, method="HEAD")
    hh = _H(headers)
    assert status == 200
    assert body == b""
    assert hh["Etag"] == f"\"{HASH}\""
    assert hh.get("Content-Length") == "0"

def test_head_match_304_empty_body():
    inm = f"\"{HASH}\""
    status, headers, body = reader_response(BYTES, HASH, if_none_match=inm, method="HEAD")
    hh = _H(headers)
    assert status == 304
    assert body == b""
    assert hh.get("Content-Length") == "0"

def test_wildcard_treated_as_miss():
    status, headers, body = reader_response(BYTES, HASH, if_none_match="*", method="GET")
    assert status == 200 and body == BYTES

def test_no_etag_on_writers_and_no_store():
    hh = _H(writer_headers())
    assert "Etag" not in hh
    assert hh["Cache-Control"] == NO_STORE
