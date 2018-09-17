#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER nqueen;
    CREATE DATABASE nqueen;
    GRANT ALL PRIVILEGES ON DATABASE nqueen TO nqueen;
    ALTER USER nqueen PASSWORD 'nqueen';
EOSQL