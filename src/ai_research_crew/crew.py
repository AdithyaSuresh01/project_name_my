from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv

from .config.settings import get_llm_model


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = Path(__file__).resolve().parent / "config"


def load_env() -> None:
    """Load environment variables from .env if present."""
    env_path = ROOT_DIR / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def _load_yaml_config() -> Dict[str, Any]:
    """Utility to load agents and tasks YAML.

    CrewAI automatically loads these when running via CLI, but we
    load them manually for `python -m` execution.
    """

    import yaml

    with (CONFIG_DIR / "agents.yaml").open("r", encoding="utf-8") as f:
        agents_cfg = yaml.safe_load(f)
    with (CONFIG_DIR / "tasks.yaml").open("r", encoding="utf-8") as f:
        tasks_cfg = yaml.safe_load(f)

    return {"agents": agents_cfg, "tasks": tasks_cfg}


def build_crew(topic: str) -> Crew:
    """Create and wire up the crew for a single research topic.

    The crew orchestrates:
    1. Research task → 2. Writing task
    """

    load_env()

    cfg = _load_yaml_config()
    agents_cfg = cfg["agents"]
    tasks_cfg = cfg["tasks"]

    llm = get_llm_model()

    # --- Agents ---
    researcher_cfg = agents_cfg["researcher_agent"]
    writer_cfg = agents_cfg["writer_agent"]

    researcher = Agent(
        role=researcher_cfg["role"],
        goal=researcher_cfg["goal"],
        backstory=researcher_cfg["backstory"],
        verbose=researcher_cfg.get("verbose", True),
        allow_delegation=researcher_cfg.get("allow_delegation", False),
        llm=llm,
    )

    writer = Agent(
        role=writer_cfg["role"],
        goal=writer_cfg["goal"],
        backstory=writer_cfg["backstory"],
        verbose=writer_cfg.get("verbose", True),
        allow_delegation=writer_cfg.get("allow_delegation", False),
        llm=llm,
    )

    # --- Tasks ---
    research_cfg = tasks_cfg["research_task"]
    writing_cfg = tasks_cfg["writing_task"]

    research_task = Task(
        description=research_cfg["description"].format(topic=topic),
        agent=researcher,
        expected_output=research_cfg["expected_output"],
    )

    writing_task = Task(
        description=writing_cfg["description"],
        agent=writer,
        expected_output=writing_cfg["expected_output"],
        # Provide previous task output as input
        context=[research_task],
    )

    return Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )


__all__ = ["build_crew"]
