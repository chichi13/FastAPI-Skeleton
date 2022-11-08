#!/bin/bash
if [ "$1" = "" ]
then
  echo "Must provide the version name"
  exit
fi
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source ${DIR}/../venv/bin/activate || true

# Number of files in alembic/versions/
CURRENT_REV=$(find ${DIR}/../alembic/versions -type f -name "*.py" | wc -l | xargs)

# Generate a new migration file with message in argument and rev-id
alembic revision --autogenerate -m "$@" --rev-id="${CURRENT_REV}"
