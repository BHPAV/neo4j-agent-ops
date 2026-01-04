"""
Configuration module for neo4j_agent_ops.
This module reads Neo4j connection details from environment variables.
"""

from dataclasses import dataclass
import os

@dataclass
class Config:
    """Configuration for connecting to Neo4j"""
    neo4j_uri: str = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
    neo4j_user: str = os.getenv("NEO4J_USER", "neo4j")
    neo4j_password: str = os.getenv("NEO4J_PASSWORD", "password")
