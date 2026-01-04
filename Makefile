.PHONY: build up down seed run

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

seed:
	python src/neo4j_agent_ops/data_loader.py

run:
	python src/neo4j_agent_ops/runner.py
