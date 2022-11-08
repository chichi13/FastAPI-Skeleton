# Install with Docker

## Env file

Create `.env` file in root directory :

```text
FASTAPI_ENV=development

PROJECT_NAME=FastAPI Skeleton
APP_VERSION=1.0.0

DATABASE_USER=app
DATABASE_PASSWORD=password
DATABASE_URL=127.0.0.1
DATABASE_NAME=skeleton
DATABASE_PORT=5432
```

## PostgreSQL

Run a postgresql database in docker :

```docker
docker network create fast-api
docker run -d --network fast-api --name postgres-app -e POSTGRES_USER=app -e POSTGRES_DB=app -e POSTGRES_PASSWORD=password -e PGDATA=/var/lib/postgresql/data/pgdata -v pgdata:/var/lib/postgresql/data -p 5432:5432 postgres
```

## Start FastAPI app

```
docker build . -f docker/dockerfile.dev -t app-fast-api:dev
docker run --rm --name fastapi --network fast-api --env-file app/config/.env -it -v $PWD:/app/fast-api/ -p 5555:5555 app-fast-api:dev
```

**DO NOT USE `dockerfile.dev` FOR PRODUCTION. Use `dockerfile.prod` instead.**

## Database migration

If there is no migration file, or you need to generate a new one, execute these commands, use `docker exec` :

```bash
docker exec -it fastapi alembic revision --autogenerate -m "init"
```

## Generate tables with Alembic

To apply your migration file to the database : 
```bash
alembic upgrade head
```

In case of error : `FAILED: Can't locate revision identified by '747e6da84866'` you might delete entry in alembic_version table :

```bash
$ docker exec -it postgres-app psql -U app
DELETE FROM alembic_version;
```
