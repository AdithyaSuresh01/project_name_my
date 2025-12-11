from __future__ import annotations

from pathlib import Path

import yaml


def test_agents_and_tasks_yaml_exist() -> None:
    root = Path(__file__).resolve().parents[1]
    agents_path = root / "src" / "ai_research_crew" / "config" / "agents.yaml"
    tasks_path = root / "src" / "ai_research_crew" / "config" / "tasks.yaml"

    assert agents_path.exists(), "agents.yaml should exist"
    assert tasks_path.exists(), "tasks.yaml should exist"

    with agents_path.open("r", encoding="utf-8") as f:
        agents_cfg = yaml.safe_load(f)
    with tasks_path.open("r", encoding="utf-8") as f:
        tasks_cfg = yaml.safe_load(f)

    assert "researcher_agent" in agents_cfg
    assert "writer_agent" in agents_cfg
    assert "research_task" in tasks_cfg
    assert "writing_task" in tasks_cfg
