# Database

This runbook contains scripts for managing the database. To run these commands, ensure you have the container running as described in the [Getting Started Guide](./DEVELOPMENT.md).

Connect to PostgreSQL:

```sh { name=db.psql }
source ../bin/env
. ../.env
_dc postgres psql -U "${POSTGRES_USER}" "${@}"
```

Connect to Redis:

```sh { name=redis-cli }
source ../bin/env
_dc redis redis-cli "${@}"
```