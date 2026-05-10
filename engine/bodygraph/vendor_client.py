from __future__ import annotations

import json
import os
import socket
import time
from dataclasses import dataclass
from datetime import timezone
from email.utils import parsedate_to_datetime
from hashlib import sha256
from pathlib import Path
from typing import Any, Callable, Mapping, MutableMapping
from urllib import error as urlerror
from urllib import request as urlrequest
from urllib.parse import urlparse

__all__ = [
    "PINNED_BACKOFF_PROFILES",
    "PINNED_MAX_ATTEMPTS",
    "PINNED_TIMEOUT_PROFILES",
    "VendorError",
    "VendorRetryConfig",
    "VendorTimeouts",
    "VendorRequest",
    "VendorResult",
    "HdApiClient",
]


_MONTH = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}

PINNED_MAX_ATTEMPTS = frozenset({0, 1, 2, 3})
PINNED_TIMEOUT_PROFILES = frozenset(
    {
        (500, 1000, 2000),
        (1000, 2000, 5000),
        (2000, 5000, 10000),
    }
)
PINNED_BACKOFF_PROFILES = frozenset(
    {
        ("none", 0, 0),
        ("fixed", 250, 250),
        ("fixed", 500, 500),
        ("exponential", 250, 500),
        ("exponential", 500, 2000),
    }
)
_RETRY_AFTER_MAX_MS = 2_147_483_647


def _validate_retry_config(retry: "VendorRetryConfig") -> None:
    if retry.max_attempts not in PINNED_MAX_ATTEMPTS:
        raise VendorError(
            "PROVIDER_CONFIG_INVALID",
            "max_attempts must be pinned to 0, 1, 2, or 3",
            details={"max_attempts": retry.max_attempts},
        )
    profile = (retry.profile, retry.exp_base_ms, retry.exp_ceiling_ms)
    if profile not in PINNED_BACKOFF_PROFILES:
        raise VendorError(
            "PROVIDER_CONFIG_INVALID",
            "retry backoff profile is not pinned",
            details={"profile": retry.profile},
        )


def _validate_timeouts(timeouts: "VendorTimeouts") -> None:
    profile = (timeouts.connect_timeout_ms, timeouts.read_timeout_ms, timeouts.total_timeout_ms)
    if profile not in PINNED_TIMEOUT_PROFILES:
        raise VendorError(
            "PROVIDER_CONFIG_INVALID",
            "timeout profile is not pinned",
            details={"timeout_profile_ms": list(profile)},
        )


def _now_ms() -> float:
    return time.monotonic() * 1000.0


def _utc_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + "Z"


class VendorError(Exception):
    """Typed vendor error surfaced to CLI + ingest harness."""

    def __init__(self, code: str, message: str, *, details: Mapping[str, Any] | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = dict(details or {})

    def as_payload(self) -> Mapping[str, Any]:
        payload: MutableMapping[str, Any] = {"code": self.code, "message": self.message}
        if self.details:
            payload["details"] = dict(self.details)
        return payload


@dataclass(frozen=True)
class VendorRetryConfig:
    max_attempts: int
    profile: str
    exp_base_ms: int
    exp_ceiling_ms: int


@dataclass(frozen=True)
class VendorTimeouts:
    connect_timeout_ms: int
    read_timeout_ms: int
    total_timeout_ms: int


@dataclass(frozen=True)
class VendorRequest:
    url: str
    headers: Mapping[str, str]
    body_bytes: bytes
    input_fingerprint: str


@dataclass(frozen=True)
class VendorResult:
    payload: Mapping[str, Any]
    duration_ms: float
    attempts: int


def _append_retry_log(path: Path | None, record: Mapping[str, Any]) -> None:
    if not path:
        return
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        text = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
        with path.open("a", encoding="utf-8") as handle:
            handle.write(text)
    except Exception:
        return


class HdApiClient:
    """HTTP client with pinned retry/backoff and typed error mapping."""

    def __init__(
        self,
        *,
        base_url: str,
        api_key: str,
        geo_key: str,
        release_id: str,
        retry: VendorRetryConfig,
        timeouts: VendorTimeouts,
        log_path: Path | None = None,
        request: Callable[[urlrequest.Request, float], tuple[int, bytes, Mapping[str, str]]] | None = None,
        sleep: Callable[[float], None] | None = None,
        monotonic_ms: Callable[[], float] | None = None,
        wall_time: Callable[[], float] | None = None,
    ) -> None:
        parsed = urlparse(base_url)
        if parsed.scheme != "https":
            raise VendorError("PROVIDER_CONFIG_MISSING", "HDAPI_BASE_URL must be https", details={"base_url": base_url})
        _validate_retry_config(retry)
        _validate_timeouts(timeouts)
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._geo_key = geo_key
        self._release_id = release_id
        self._retry = retry
        self._timeouts = timeouts
        self._log_path = log_path
        self._request = request or self._default_request
        self._sleep = sleep or time.sleep
        self._monotonic = monotonic_ms or _now_ms
        self._wall_time = wall_time or time.time

    @classmethod
    def from_env(
        cls,
        *,
        log_path: Path | None = None,
        retry: VendorRetryConfig | None = None,
        timeouts: VendorTimeouts | None = None,
        release_id: str | None = None,
        request: Callable[[urlrequest.Request, float], tuple[int, bytes, Mapping[str, str]]] | None = None,
    ) -> "HdApiClient":
        env = os.environ
        raw_base_url = (env.get("HDAPI_BASE_URL") or "").strip().rstrip("/")
        api_key = (env.get("HD_API_KEY") or "").strip()
        geo_key = (env.get("GEO_API_KEY") or "").strip()
        pairs = (("HDAPI_BASE_URL", raw_base_url), ("HD_API_KEY", api_key), ("GEO_API_KEY", geo_key))
        missing = [key for key, value in pairs if not value]
        if missing:
            raise VendorError(
                "PROVIDER_CONFIG_MISSING",
                "missing vendor configuration",
                details={"missing": sorted(missing)},
            )
        base_url = raw_base_url
        rid = (release_id or env.get("RELEASE_ID") or "").strip().lower()
        if not rid:
            rid = "0" * 64
        if len(rid) != 64 or any(ch not in "0123456789abcdef" for ch in rid):
            rid = sha256(rid.encode("utf-8")).hexdigest()
        retry_cfg = retry or VendorRetryConfig(max_attempts=3, profile="exponential", exp_base_ms=500, exp_ceiling_ms=2000)
        timeouts_cfg = timeouts or VendorTimeouts(connect_timeout_ms=2000, read_timeout_ms=5000, total_timeout_ms=10000)
        return cls(
            base_url=base_url,
            api_key=api_key,
            geo_key=geo_key,
            release_id=rid,
            retry=retry_cfg,
            timeouts=timeouts_cfg,
            log_path=log_path,
            request=request,
        )

    def build_request(self, *, birthdate: str, birthtime: str, location: str) -> VendorRequest:
        fields = ("birthdate", "birthtime", "location")
        missing = [name for name, value in zip(fields, (birthdate, birthtime, location)) if not (isinstance(value, str) and value.strip())]
        if missing:
            raise VendorError("PROVIDER_INPUT_INVALID", "birth data incomplete", details={"missing": missing})
        try:
            yyyy, mm, dd = birthdate.split("-")
        except ValueError as exc:
            raise VendorError("PROVIDER_INPUT_INVALID", "invalid birthdate", details={"birthdate": birthdate}) from exc
        if mm not in _MONTH:
            raise VendorError("PROVIDER_INPUT_INVALID", "invalid birthdate", details={"birthdate": birthdate})
        canon_date = f"{dd}-{_MONTH[mm]}-{yyyy}"
        body = {
            "birthdate": canon_date,
            "birthtime": birthtime,
            "location": location,
        }
        body_bytes = json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
        fingerprint = sha256(body_bytes).hexdigest()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json; charset=utf-8",
            "HD-Api-Key": self._api_key,
            "HD-Geocode-Key": self._geo_key,
            "User-Agent": f"GlowHDEngine/{self._release_id}",
        }
        return VendorRequest(
            url=f"{self._base_url}/bodygraphs",
            headers=headers,
            body_bytes=body_bytes,
            input_fingerprint=fingerprint,
        )

    def fetch(self, request: VendorRequest) -> VendorResult:
        attempt = 0
        deadline = self._monotonic() + self._timeouts.total_timeout_ms
        last_error: VendorError | None = None
        while attempt < self._retry.max_attempts:
            attempt += 1
            start = self._monotonic()
            status: Any = "error"
            duration_ms = 0.0
            error_code = None
            error_class = "none"
            retry_after_ms: int | None = None
            planned_backoff_ms = 0.0
            retryable = False
            try:
                req = urlrequest.Request(request.url, data=request.body_bytes, headers=request.headers, method="POST")
                timeout = self._timeouts.read_timeout_ms / 1000.0
                status_code, body_bytes, headers = self._request(req, timeout)
                duration_ms = self._monotonic() - start
                status = status_code
                if status_code != 200:
                    error_code = self._map_status_to_code(status_code)
                    error_class = self._error_class(status_code)
                    retryable = self._is_retryable_error_class(error_class)
                    if status_code == 429:
                        retry_after_ms = self._retry_after_ms(headers)
                    raise VendorError(error_code, "vendor_error", details={"status": status_code})
                try:
                    payload = json.loads(body_bytes.decode("utf-8"))
                except Exception as exc:
                    raise VendorError("PROVIDER_BAD_RESPONSE", "malformed JSON", details={"status": status_code}) from exc
                self._log_attempt(attempt, status_code, duration_ms, error_class)
                return VendorResult(payload=payload, duration_ms=duration_ms, attempts=attempt)
            except VendorError as exc:
                last_error = exc
                duration_ms = duration_ms or (self._monotonic() - start)
                error_code = exc.code
                error_class = error_class or exc.code.lower()
                if retryable and attempt < self._retry.max_attempts:
                    planned_backoff_ms = self._bounded_backoff_delay(attempt, deadline)
                self._log_attempt(
                    attempt,
                    status,
                    duration_ms,
                    error_class,
                    error_code=error_code,
                    retry_after_ms=retry_after_ms,
                    backoff_ms=planned_backoff_ms,
                )
                if not retryable:
                    break
            except (urlerror.URLError, TimeoutError, socket.timeout, OSError) as exc:
                last_error = VendorError("PROVIDER_NETWORK_ERROR", "network failure", details={"error": str(exc)})
                duration_ms = self._monotonic() - start
                error_class = "network_error"
                retryable = True
                if attempt < self._retry.max_attempts:
                    planned_backoff_ms = self._bounded_backoff_delay(attempt, deadline)
                self._log_attempt(
                    attempt,
                    status,
                    duration_ms,
                    error_class,
                    error_code="PROVIDER_NETWORK_ERROR",
                    backoff_ms=planned_backoff_ms,
                )
            if attempt >= self._retry.max_attempts or not retryable or planned_backoff_ms <= 0:
                break
            self._sleep(planned_backoff_ms / 1000.0)
        raise last_error or VendorError("PROVIDER_UNAVAILABLE", "vendor unavailable")

    def _log_attempt(
        self,
        attempt: int,
        status: Any,
        duration_ms: float,
        error_class: str,
        *,
        error_code: str | None = None,
        retry_after_ms: int | None = None,
        backoff_ms: float | None = None,
    ) -> None:
        record = {
            "at": _utc_iso(),
            "attempt": attempt,
            "status": status,
            "duration_ms": round(float(duration_ms), 3),
            "profile": self._retry.profile,
            "error_class": error_class,
            "route": "vendor.hdapi.post:/bodygraphs",
        }
        if error_code:
            record["error_code"] = error_code
        if retry_after_ms is not None:
            record["retry_after_ms"] = retry_after_ms
        if backoff_ms is not None:
            record["backoff_ms"] = int(backoff_ms)
        _append_retry_log(self._log_path, record)

    def _bounded_backoff_delay(self, attempt: int, deadline: float) -> float:
        delay = self._backoff_delay(attempt)
        if delay <= 0:
            return 0.0
        now = self._monotonic()
        if now >= deadline or now + delay > deadline:
            return 0.0
        return delay

    def _backoff_delay(self, attempt: int) -> float:
        if attempt <= 0 or self._retry.profile == "none":
            return 0.0
        if self._retry.profile == "fixed":
            return float(self._retry.exp_base_ms)
        if self._retry.profile == "exponential":
            exp = attempt - 1
            delay = min(self._retry.exp_base_ms * (2 ** exp), self._retry.exp_ceiling_ms)
            return float(delay)
        return 0.0

    @staticmethod
    def _is_retryable_error_class(error_class: str) -> bool:
        return error_class in {"network_error", "5xx"}

    def _map_status_to_code(self, status: int) -> str:
        if status == 401:
            return "PROVIDER_UNAUTHORIZED"
        if status == 403:
            return "PROVIDER_FORBIDDEN"
        if status == 404:
            return "PROVIDER_NOT_FOUND"
        if status == 429:
            return "PROVIDER_RATE_LIMITED"
        if 500 <= status <= 599:
            return "PROVIDER_UNAVAILABLE"
        return "PROVIDER_ERROR"

    def _error_class(self, status: int) -> str:
        if status == 429:
            return "429"
        if 500 <= status <= 599:
            return "5xx"
        if 400 <= status <= 499:
            return "4xx"
        return "network_error"

    def _retry_after_ms(self, headers: Mapping[str, str]) -> int | None:
        retry_after = None
        if headers:
            retry_after = headers.get("retry-after") or headers.get("Retry-After")
        if not retry_after:
            return None
        retry_after = retry_after.strip()
        if not retry_after:
            return None
        delay_ms: int | None
        if retry_after.isdigit():
            delay_ms = self._retry_after_delta_ms(retry_after)
        else:
            delay_ms = self._retry_after_http_date_ms(retry_after)
        if delay_ms is None or delay_ms > _RETRY_AFTER_MAX_MS:
            return None
        return delay_ms

    @staticmethod
    def _retry_after_delta_ms(raw: str) -> int | None:
        try:
            seconds = int(raw, 10)
        except ValueError:
            return None
        delay_ms = seconds * 1000
        if delay_ms > _RETRY_AFTER_MAX_MS:
            return None
        return delay_ms

    def _retry_after_http_date_ms(self, raw: str) -> int | None:
        try:
            parsed = parsedate_to_datetime(raw)
        except (TypeError, ValueError, IndexError, OverflowError):
            return None
        if parsed is None:
            return None
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        target = parsed.astimezone(timezone.utc).timestamp()
        delta_seconds = max(0.0, target - self._wall_time())
        delay_ms = int(delta_seconds * 1000)
        if delay_ms > _RETRY_AFTER_MAX_MS:
            return None
        return delay_ms

    @staticmethod
    def _default_request(req: urlrequest.Request, timeout: float) -> tuple[int, bytes, Mapping[str, str]]:
        with urlrequest.urlopen(req, timeout=timeout) as resp:  # type: ignore[arg-type]
            status = getattr(resp, "status", resp.getcode())
            body = resp.read()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return status, body, headers
