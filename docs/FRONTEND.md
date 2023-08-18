# Frontend

This runbook contains scripts for managing the frontend.

Install yarn dependencies and write lock file:

```sh { name=yarn:install }
source ../bin/env
_build_run_down js yarn install
```

List any installed packages that are outdated

```sh { name=yarn:outdated }
source ../bin/env
_build_run_down js yarn outdated
```