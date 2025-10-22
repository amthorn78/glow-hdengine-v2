class ProviderError(RuntimeError):
    """Base class for provider-layer errors."""

class ProviderRefusedInSafeMode(ProviderError):
    """Raised when a non-fixtures provider is used while SAFE_MODE is enabled."""

class ProviderUnavailable(ProviderError):
    """
    Raised when provider calls are gated by runtime rails (e.g., SAFE_MODE on,
    ALLOW_NETWORK off, or network disabled in tests).
    """

class ProviderConfigMissing(ProviderError):
    """Raised when a provider is selected but required config is missing/blank."""
