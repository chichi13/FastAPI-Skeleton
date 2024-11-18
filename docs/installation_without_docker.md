# Installation without Docker

## Env file

Create `.env` file in root directory :

```text
ENV=development

PROJECT_NAME=FastAPI Skeleton
APP_VERSION=1.0.0

DATABASE_USER=app
DATABASE_PASSWORD=password
DATABASE_URL=127.0.0.1
DATABASE_NAME=skeleton
DATABASE_PORT=5432
```

## Installation without docker

Use at least **python 3.10**.

## Create a virtualenv and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install requirements

```bash
pip3 install -r requirements/dev.txt # or prod.txt
```

## Install/Configure PostgreSQL

Install PostgreSQL [here](https://doc.ubuntu-fr.org/postgresql).

And then create a database/user :

```SQL
CREATE DATABASE app
CREATE USER app WITH PASSWORD 'password';
```

## Database migration

If there is no versions in `migrations/versions` folder, execute this command :

```bash
# Generate version file
alembic revision --autogenerate -m "init"
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

# Start FastAPI app

```bash
python3 main.py
```