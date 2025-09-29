install:
	@command -v uv >/dev/null 2>&1 || { echo "uv is not installed. Installing uv..."; curl -LsSf https://astral.sh/uv/0.6.12/install.sh | sh; source $HOME/.local/bin/env; }
	uv sync && npm --prefix frontend install

dev:
	make dev-backend & make dev-frontend

dev-backend:
	uv run adk api_server app --allow_origins="*"

dev-frontend:
	npm --prefix frontend run dev

playground:
	uv run adk web --port 8501

lint:
	uv sync --dev --extra lint
	uv run codespell
	uv run ruff check . --diff
	uv run ruff format . --check --diff
	uv run mypy .

# --- Commands from Agent Starter Pack ---

backend:
	# Export dependencies to requirements file using uv export.
	uv export --no-hashes --no-header --no-dev --no-emit-project --no-annotate > .requirements.txt 2>/dev/null || \
	uv export --no-hashes --no-header --no-dev --no-emit-project > .requirements.txt && uv run app/agent_engine_app.py

setup-dev-env:
	PROJECT_ID=$$(gcloud config get-value project) && \
	(cd deployment/terraform/dev && terraform init && terraform apply --var-file vars/env.tfvars --var dev_project_id=$$PROJECT_ID --auto-approve)

test:
	uv run pytest tests/unit && uv run pytest tests/integration


# --- Commands from Agent Starter Pack ---

data-ingestion:
	(cd data_ingestion && uv run data_ingestion_pipeline/submit_pipeline.py \
		--project-id="tradieai-fullstack-production" \
		--region="us-central1" \
		--data-store-id="tradieai-fullstack-v2-datastore" \
		--data-store-region="us" \
		--service-account="tradieai-fullstack-v2-rag@tradieai-fullstack-production.iam.gserviceaccount.com" \
		--pipeline-root="gs://tradieai-fullstack-production-tradieai-fullstack-v2-rag" \
		--pipeline-name="data-ingestion-pipeline")

