run:
	echo "Running in local mode."
	docker compose create db
	docker compose start db
	poetry run start

run_docker:
	echo "Running in local mode with docker."
	docker compose up

migrate:
	echo "Running migrations."
	docker compose create db
	docker compose start db
	poetry run python -m alembic upgrade head
	# workaround for having PGVector create its tables
	poetry run python -m scripts.build_vector_tables

refresh_db:
	# First ask for confirmation.
	@echo -n "Are you sure you want to refresh the local database? This will delete all data in your local db. [Y/n] "; \
	read ans; \
	if [ $${ans:-'N'} = 'Y' ]; then make confirmed_refresh_db; else echo "Aborting."; fi

confirmed_refresh_db:
	echo "Refreshing database."
	docker compose down db
	docker volume rm backend_postgres_data
	make migrate

test:
	poetry run python -m pytest tests/

chat:
	poetry run python -m scripts.chat_llama

seed_db_based_on_env:
	# Call either seed_db or seed_db_preview, seed_db_local based on the environment
	# This is used by the CI/CD pipeline
	ENVIRONMENT=$$(poetry run python -c "from app.core.config import settings;print(settings.ENVIRONMENT.value)"); \
	echo "Environment: $$ENVIRONMENT"; \
	if [ "$$ENVIRONMENT" = "preview" ]; then \
		make seed_db_preview; \
	elif [ "$$ENVIRONMENT" = "production" ]; then \
		make seed_db; \
	else \
		make seed_db_local; \
	fi

seed_db:
	echo "Seeding database."
	poetry run python scripts/seed_db.py

seed_db_preview:
	echo "Seeding database for Preview."
	# only need to populate with two companies for Preview
	poetry run python scripts/seed_db.py  --ciks '["0001018724", "1326801"]'

seed_db_local:
	echo "Seeding database for local."
	docker compose create db
	docker compose start db
	python scripts/seed_db.py --ciks '["0001018724", "1326801"]'  --filing_types '["10-K"]'
