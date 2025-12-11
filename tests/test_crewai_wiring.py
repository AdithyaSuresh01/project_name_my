from __future__ import annotations

from ai_research_crew.crew import build_crew


def test_build_crew_sequential_process() -> None:
    crew = build_crew("test topic")
    # basic sanity checks
    assert len(crew.agents) == 2
    assert len(crew.tasks) == 2

    # Check that the second task depends on the first via context
    research_task, writing_task = crew.tasks
    assert research_task in writing_task.context
