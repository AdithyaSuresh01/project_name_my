from __future__ import annotations

from crewai import LLM


def llm_healthcheck(llm: LLM) -> str:
    """Run a tiny call against the configured LLM to verify connectivity.

    This can be invoked in a notebook or small script while setting up
    environment variables.
    """

    prompt = "You are a healthcheck. Reply with: LLM OK."
    response = llm.invoke(prompt)
    return str(response)
