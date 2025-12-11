"""Custom tools for AIResearchCrew.

For this mini-project, we include a simple healthcheck that performs a
minimal LLM call to validate that credentials and configuration work.
"""

from .llm_healthcheck import llm_healthcheck

__all__ = ["llm_healthcheck"]
