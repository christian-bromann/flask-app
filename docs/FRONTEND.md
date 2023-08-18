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

## Container Commands

These commands are meant to be run from within the assets container.

Build JS assets:

```sh { name=yarn:build:js cwd=../assets }
mkdir -p ../public/js
node esbuild.config.mjs
```

Build CSS assets, this is meant to be run from within the assets container

```sh { name=yarn:build:css cwd=../assets }
local args=()

if [ "${NODE_ENV:-}" == "production" ]; then
    args=(--minify)
else
    args=(--watch)
fi

mkdir -p ../public/css
tailwindcss --postcss -i css/app.css -o ../public/css/app.css "${args[@]}"
```

Remove cache and other machine generates files

```sh { name=clean cwd=../ }
rm -rf public/*.* public/js public/css public/images public/fonts .pytest_cache/ .coverage celerybeat-schedule
touch public/.keep
```