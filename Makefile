.PHONY: lint test run train

lint:
	ruff check src/ tests/

test:
	pytest tests/ -v

run:
	uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000

train:
	python -m src.models.train_baseline
	python -m src.models.train_mlp
