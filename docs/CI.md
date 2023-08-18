# CI

This runbook contains scripts are meant to be used in [CI](../.github/workflows/ci.yml).

Install Continuous Integration (CI) dependencies

```sh { name=ci.install-deps }
sudo apt-get install -y curl shellcheck
sudo curl \
    -L https://raw.githubusercontent.com/nickjj/wait-until/v0.2.0/wait-until \
    -o /usr/local/bin/wait-until && sudo chmod +x /usr/local/bin/wait-until
sudo curl -sSL https://download.stateful.com/runme/1.7.2/runme_linux_x86_64.tar.gz  | \
    tar -xz -C /usr/local/bin runme
```

Execute Continuous Integration (CI) pipeline.

It's expected that your CI environment has these tools available:

- https://github.com/stateful/runme
- https://github.com/koalaman/shellcheck
- https://github.com/nickjj/wait-until

```sh { name=ci.build cwd=../ }
echo "Run ci.build task"
# shellcheck run bin/*

cp --no-clobber .env.example .env

docker compose build
docker compose up -d

# shellcheck disable=SC1091
ls -la
cat ./.env
source ./.env
wait-until "docker compose exec -T \
-e PGPASSWORD=${POSTGRES_PASSWORD} postgres \
psql -U ${POSTGRES_USER} ${POSTGRES_USER} -c 'SELECT 1'"

docker compose logs
```