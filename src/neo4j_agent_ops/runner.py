"""Runner for neo4j_agent_ops.
This module orchestrates loading seed data into Neo4j and starting the agent.
"""

from .config import Config
from .agent import Agent
from .data_loader import DataLoader


def main() -> None:
    """Main entry point for the neo4j_agent_ops runner."""
    config = Config.from_env()
    # Load seed data
    loader = DataLoader(config)
    try:
        loader.load_seed()
    except Exception as exc:
        # Log or print error (print for simplicity)
        print(f"Error seeding data: {exc}")
    finally:
        loader.close()

    # Initialize agent and run
    agent = Agent(config)
    try:
        agent.run()
    finally:
        agent.close()


if __name__ == "__main__":
    main()
