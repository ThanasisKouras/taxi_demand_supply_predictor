.PHONY: init features training inference frontend monitoring

# Set the default target
.DEFAULT_GOAL := features

# downloads Poetry and installs all dependencies from pyproject.toml
init:
	(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py - --version $env:POETRY_VERSION
	poetry install

# generates new batch of features and stores them in the feature store
features:
	@echo "Running feature pipeline"
	@poetry run python scripts/feature_pipeline.py

# trains a new model and stores it in the model registry
training:
	@echo "Running training pipeline"
	@poetry run python scripts/training_pipeline.py

# generates predictions and stores them in the feature store
inference:
	@echo "Running inference pipeline"
	@poetry run python scripts/inference_pipeline.py

# backfills the feature store with historical data
backfill:
	@echo "Running backfill feature group pipeline"
	@poetry run python scripts/backfill_feature_group.py

# starts the Streamlit app
frontend-app:
	@echo "Starting Streamlit app"
	@poetry run streamlit run src/frontend.py

monitoring-app:
	@echo "Starting monitoring app"
	@poetry run streamlit run src/frontend_monitoring.py
