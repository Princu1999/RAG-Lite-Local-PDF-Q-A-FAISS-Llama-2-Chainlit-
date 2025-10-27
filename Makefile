.PHONY: setup ingest run test clean

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

ingest:
	python ingest.py

run:
	chainlit run model.py -w

test:
	pytest -q

clean:
	rm -rf __pycache__ .venv vectorstore/db_faiss/*
