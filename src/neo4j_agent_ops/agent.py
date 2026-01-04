"""
Agent core logic for neo4j_agent_ops.
This class encapsulates the operations of the agent.
"""

from neo4j import GraphDatabase
from .config import Config

class Agent:
    """A simple agent that interacts with a Neo4j database."""
    def __init__(self, config: Config) -> None:
        self.config = config
        # initialize Neo4j driver using configuration
        self.driver = GraphDatabase.driver(
            self.config.neo4j_uri,
            auth=(self.config.neo4j_user, self.config.neo4j_password)
        )

    def close(self) -> None:
        """Close the Neo4j driver"""
        self.driver.close()

    def run(self) -> int:
        """Run a simple test query to verify connectivity.

        Returns:
            int: returns 1 if connection is successful
        """
        with self.driver.session() as session:
            result = session.run("RETURN 1 AS ok")
            return result.single()["ok"]
