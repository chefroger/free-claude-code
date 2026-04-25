"""Request builder for MiniMax provider."""

from typing import Any

from loguru import logger

from providers.common.message_converter import build_base_request_body

MINIMAX_DEFAULT_MAX_TOKENS = 8192


def build_request_body(request_data: Any, *, thinking_enabled: bool) -> dict:
    """Build OpenAI-format request body from Anthropic request for MiniMax."""
    logger.debug(
        "MINIMAX_REQUEST: conversion start model={} msgs={}",
        getattr(request_data, "model", "?"),
        len(getattr(request_data, "messages", [])),
    )

    body = build_base_request_body(
        request_data,
        include_reasoning_content=True,
        default_max_tokens=MINIMAX_DEFAULT_MAX_TOKENS,
    )

    # MiniMax uses extra_body.thinking for reasoning
    extra_body: dict[str, Any] = {}
    request_extra = getattr(request_data, "extra_body", None)
    if request_extra:
        extra_body.update(request_extra)

    if thinking_enabled:
        extra_body.setdefault("thinking", {"type": "enabled"})

    if extra_body:
        body["extra_body"] = extra_body

    logger.debug(
        "MINIMAX_REQUEST: conversion done model={} msgs={} tools={}",
        body.get("model"),
        len(body.get("messages", [])),
        len(body.get("tools", [])),
    )
    return body
