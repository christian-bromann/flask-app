# Testing

The following section describe various of testing methodologies used by this project. To run these commands, ensure you have the container running as described in the [Getting Started Guide](./DEVELOPMENT.md).

Perform all project checks together via

```sh { name=test }
runme run test.format test.lint test.unit
```

### Formatting

Format Python code via:

```sh { name=test.format }
runme run test.format.black test.format.imports
```

Run [Black](https://black.readthedocs.io/en/stable/) formatter via:

```sh { name=test.format.black }
. ../bin/env
cmd black . --check
```

Sort Python imports via:

```sh { name=test.format.imports }
. ../bin/env
cmd isort . --check
echo "Import formatting succeeded ✅"
```

### Linting

Lint project code via:

```sh { name=test.lint }
runme run test.lint.flake8 test.lint.dockerfile
```

Run Flake8 checks via:

```sh { name=test.lint.flake8 }
. ../bin/env
cmd flake8 "${@}"
echo "Lint passed ✅"
```

Lint Dockerfile via:

```sh { name=test.lint.dockerfile }
docker container run --rm -i hadolint/hadolint hadolint --ignore DL3008 -t style "${@}" - < ../Dockerfile
```

## Unit Testing

Run test suite via:

```sh { name=test.unit }
. ../bin/env
cmd pytest test/ "${@}"
```

To run unit tests with test coverage support run:

```sh { name=test.unit.coverage }
. ../bin/env
cmd pytest --cov test/ --cov-report term-missing "${@}"
```