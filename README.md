# mcms-content-service

## Alembic related commands
To build containers:
docker-compose up -d --build

To initialize alembid:
docker-compose exec -w app/src web uv run alembic init alembic

To create revision:
docker-compose exec -w /app/src web uv run alembic revision --autogenerate -m "init"

To apply migration:
docker-compose exec -w /app/src web uv run alembic upgrade head
