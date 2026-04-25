"""Providers package - implement your own provider by extending BaseProvider."""

from .base import BaseProvider, ProviderConfig
from .deepseek import DeepSeekProvider
from .exceptions import (
    APIError,
    AuthenticationError,
    InvalidRequestError,
    OverloadedError,
    ProviderError,
    RateLimitError,
)
from .llamacpp import LlamaCppProvider
from .lmstudio import LMStudioProvider
from .minimax import MiniMaxProvider, MINIMAX_BASE_URL
from .nvidia_nim import NvidiaNimProvider
from .open_router import OpenRouterProvider

__all__ = [
    "APIError",
    "AuthenticationError",
    "BaseProvider",
    "DeepSeekProvider",
    "InvalidRequestError",
    "LMStudioProvider",
    "LlamaCppProvider",
    "MiniMaxProvider",
    "NvidiaNimProvider",
    "OpenRouterProvider",
    "OverloadedError",
    "ProviderConfig",
    "ProviderError",
    "RateLimitError",
]
