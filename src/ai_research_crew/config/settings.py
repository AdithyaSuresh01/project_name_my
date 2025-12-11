from __future__ import annotations

import os
from typing import Any

from crewai import LLM


def get_llm_model() -> LLM:
    """Create and return a configured LLM instance for Agents.

    Configuration is read from environment variables so it can be
    adjusted without changing code.
    """

    model_name = os.getenv("LLM_MODEL_NAME", "gpt-4o")
    temperature_str = os.getenv("LLM_TEMPERATURE", "0.1")
    try:
        temperature = float(temperature_str)
    except ValueError:
        temperature = 0.1

    # CrewAI's LLM wrapper automatically picks provider based on environment
    # (e.g., OPENAI_API_KEY, ANTHROPIC_API_KEY).
    return LLM(
        model=model_name,
        temperature=temperature,
    )


__all__ = ["get_llm_model"]
