# Developer Documentation

These docs contain development documentation how to operate on this code base.

## Getting Started

First, clone the project by clicking on [![](https://badgen.net/badge/Clone%20this%20/Project/5B3ADF?icon=https://runme.dev/img/logo.svg)](https://runme.dev/api/runme?repository=https%3A%2F%2Fgithub.com%2Fchristian-bromann%2Fflask-app.git&fileToOpen=README.md)

First, copy an example `.env` file because the real one is git ignored:

```bash { name=init cwd=../ }
cp .env.example .env
```

Then build everything via

```sh { name=build background=true }
docker compose up --build
```

If you run this setup for the first time, make sure to initiate the database via:

```sh { name=db.init }
. ../bin/env
cmd flask db reset --with-testdb
echo "DB Reset Successful ✅"
```

You should see the application running on:

```sh { name=open }
open http://localhost:8000
```

Happy coding 🎉