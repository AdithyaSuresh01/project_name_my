from __future__ import annotations

import sys
from pathlib import Path

from .crew import build_crew


DEFAULT_TOPIC = "latest AI developments in healthcare"


def run(topic: str | None = None) -> str:
    """Run the crew for a given topic and return the final markdown report.

    This function is used by both `python -m` execution and `crewai run`.
    """

    final_topic = topic or DEFAULT_TOPIC
    crew = build_crew(final_topic)

    print(f"[AIResearchCrew] Running crew for topic: {final_topic}\n")
    result = crew.kickoff()

    markdown_report = str(result)

    # Save to reports folder for portfolio/demo purposes
    root = Path(__file__).resolve().parents[2]
    reports_dir = root / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = reports_dir / "latest_report.md"
    out_path.write_text(markdown_report, encoding="utf-8")

    print(f"\n[AIResearchCrew] Report saved to: {out_path}")
    return markdown_report


if __name__ == "__main__":
    user_topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    run(user_topic if user_topic else None)
