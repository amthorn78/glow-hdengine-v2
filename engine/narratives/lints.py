"""Narrative lint enforcement helpers."""

from __future__ import annotations

import re
from typing import Iterable

from .constants import INCLUSIVE_BANNED_TOKENS, JARGON_BANNED_TOKENS

_SENTENCE_PATTERN = re.compile(r"[^.!?]+[.!?]")
_ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'!.?")


def check_length(text: str) -> bool:
    return len(text) <= 300


def check_sentence_count(text: str) -> bool:
    sentences = _SENTENCE_PATTERN.findall(text.strip())
    return 2 <= len(sentences) <= 4


def check_single_paragraph(text: str) -> bool:
    return "\n" not in text and "\r" not in text


def check_no_digits(text: str) -> bool:
    return not any(ch.isdigit() for ch in text)


def check_no_em_dash(text: str) -> bool:
    return "—" not in text


def check_lf_normalization(text: str) -> bool:
    return "\r" not in text


def check_jargon_free(text: str) -> bool:
    lowered = text.lower()
    return not any(token in lowered for token in JARGON_BANNED_TOKENS)


def check_inclusive_tone(text: str) -> bool:
    lowered = text.lower()
    return not any(token in lowered for token in INCLUSIVE_BANNED_TOKENS)


def check_allowed_characters(text: str) -> bool:
    return all(ch in _ALLOWED_CHARS for ch in text)


def run_all(text: str) -> Iterable[str]:
    """Yield lint token names for any failures."""

    checks = [
        ("NARR_LEN_LE_300_OK", check_length),
        ("NARR_2TO4_SENTENCES_OK", check_sentence_count),
        ("NARR_SINGLE_PARAGRAPH_OK", check_single_paragraph),
        ("NARR_NO_NUMERICS_OK", check_no_digits),
        ("NARR_NO_EM_DASH_OK", check_no_em_dash),
        ("NARR_LF_NORMALIZATION_OK", check_lf_normalization),
        ("NARR_JARGON_FREE_OK", check_jargon_free),
        ("NARR_INCLUSIVE_TONE_OK", check_inclusive_tone),
        ("NARR_ALLOWED_CHARS_OK", check_allowed_characters),
    ]
    for token, fn in checks:
        if not fn(text):
            yield token
