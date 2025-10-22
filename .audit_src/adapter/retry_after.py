import datetime as dt
from email.utils import parsedate_to_datetime

def parse_retry_after_ms(value: str | None, now: dt.datetime | None = None) -> int | None:
    """
    RFC7231 Retry-After header:
      - If integer seconds -> seconds * 1000
      - If HTTP-date       -> max(0, date - now) in milliseconds
    Returns int ms (>=0) or None if unparseable/absent.
    """
    if not value:
        return None
    v = value.strip()
    if v.isdigit():
        try:
            ms = int(v) * 1000
        except Exception:
            return None
        return ms if ms >= 0 else 0
    try:
        when = parsedate_to_datetime(v)
        if when.tzinfo is None:
            when = when.replace(tzinfo=dt.timezone.utc)
        now_dt = now or dt.datetime.now(dt.timezone.utc)
        delta_s = (when - now_dt).total_seconds()
        ms = int(max(0.0, delta_s) * 1000.0)
        return ms
    except Exception:
        return None
