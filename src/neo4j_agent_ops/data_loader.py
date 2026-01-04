"""Data loader for neo4j_agent_ops.

This module provides functionality to load a seed dataset into a Neo4j database from a Cypher file.
"""

from pathlib import Path
from neo4j import GraphDatabase

from .config import Config


class DataLoader:
    """Loads seed data into Neo4j."""

    def __init__(self, config: Config) -> None:
        self.config = config
        self.driver = GraphDatabase.driver(
            config.uri, auth=(config.user, config.password)
        )

    def load_seed(self, seed_path: str = "data/seed.cypher") -> None:
        """Load seed data into Neo4j from a Cypher file.

        Args:
            seed_path: Path to the Cypher file containing seed data.
        """
        path = Path(seed_path)
        if not path.is_file():
            print(f"Seed file {seed_path} not found.")
            return

        cypher = path.read_text()
        # Split statements by semicolon to allow multiple statements
        statements = [s.strip() for s in cypher.split(";") if s.strip()]

        with self.driver.session() as session:
            for statement in statements:
                session.run(statement)

    def close(self) -> None:
        """Close the underlying Neo4j driver."""
        self.driver.close()
