# neo4j-agent-ops

## Overview
A self-improving agent scaffold built with a modular Python runner, a Neo4j graph database and Docker tooling. The project includes a small seed dataset for Neo4j and a containerised development environment.

## Architecture

- **Modular Runner**: The `src/neo4j_agent_ops/runner.py` module is the entry point. It loads tools and orchestrates the agent’s reasoning and actions. Additional tools can be added in the `tools/` directory.
- **Agent Core**: The `agent.py` defines an `Agent` class responsible for planning, acting and learning.
- **Configuration**: Configuration (e.g. Neo4j connection) is read from environment variables via `config.py`.
- **Data Loader**: A simple loader seeds Neo4j using Cypher scripts from the `data/` folder.
- **Docker**: A `docker-compose.yml` brings up Neo4j and the agent. The Python service builds from the provided `Dockerfile`.

## Milestones

1. **MVP Scaffold** – repository structure with Docker, seed dataset and modular runner.
2. **Tooling Layer** – implement additional tools (e.g. web search, file I/O) and plug-ins.
3. **Self‑Improvement Loop** – enable the agent to evaluate its outputs and adjust its behaviour (e.g. using reflection or evaluations).
4. **User Interface** – add CLI or web UI for interacting with the agent.
5. **Deployment** – prepare CI/CD and container registry.

## Getting Started

```bash
# clone and change into the repo
git clone https://github.com/BHPAV/neo4j-agent-ops.git
cd neo4j-agent-ops

# bring up services (Neo4j and agent)
docker compose up --build
```

The agent expects the following environment variables for connecting to Neo4j:

- `NEO4J_URI` (e.g. `bolt://neo4j:7687`)
- `NEO4J_USER`
- `NEO4J_PASSWORD`
- `NEO4J_DATABASE` (default `neo4j`)

## Makefile

The included `Makefile` provides shortcuts:

- `make build` – build Docker images.
- `make up` – start services via docker-compose.
- `make down` – stop services.
- `make seed` – seed the Neo4j database using scripts in `data/`.
- `make run` – run the Python runner locally.
