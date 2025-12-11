# AI Research & Report Crew

Mini-project built with **CrewAI** that takes a single topic (e.g., "latest AI developments in healthcare") and returns a concise **markdown report**.

## Features
- **v1**: Single-agent research flow
- **v2**: Two-agent pipeline (Researcher → Writer)
- CLI entry via `python -m ai_research_crew.main` or `crewai run`
- Sample generated report in `reports/`

## Project Structure
```text
AIResearchCrew/
├── .env.example
├── README.md
├── pyproject.toml
├── crewai.yaml
├── reports/
│   └── sample_healthcare_ai_report.md
└── src/
    └── ai_research_crew/
        ├── __init__.py
        ├── crew.py
        ├── main.py
        ├── config/
        │   ├── agents.yaml
        │   ├── tasks.yaml
        │   └── settings.py
        └── tools/
            ├── __init__.py
            └── llm_healthcheck.py
```

## Setup
1. Install **Python 3.10–3.13**.
2. Install CrewAI and tools:
   ```bash
   pip install "crewai[tools]"
   ```
3. Create project via CLI (for reference):
   ```bash
   crewai create crew ai_research_report
   ```
4. From the project root:
   ```bash
   crewai install
   ```

5. Configure environment:
   ```bash
   cp .env.example .env
   # edit .env and set your OPENAI_API_KEY or provider key
   ```

## Running the crew
### Using Python
```bash
python -m ai_research_crew.main
```

### Using CrewAI CLI
```bash
crewai run
```

The default topic is set in `main.py` but can be overridden with a CLI argument:
```bash
python -m ai_research_crew.main "latest AI developments in healthcare"
```

## Iteration workflow
1. Run once with a topic.
2. Inspect the markdown report for:
   - structure (headings, bullets)
   - factual clarity
   - missing sections
3. Refine prompts in `config/tasks.yaml` (task descriptions and expected_output) and rerun.

## Data Science angle
Although this is primarily an **agentic LLM orchestration** project, it is structured to be extended with:
- retrieval over local datasets
- evaluation scripts for factuality and coverage
- logging and experiment tracking around prompt changes.
