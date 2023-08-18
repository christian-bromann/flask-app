# A Flask + Docker app operated by [Runme](https://runme.dev)

This project is a Flask application using Docker as container and Runme as operational engine. You could use this example app as a base for your new project or as a guide to Dockerize your existing Flask app.

The example app is minimal but it wires up a number of things you might use in a real world Flask app, but at the same time it's not loaded up with a million personal opinions.

For the Docker bits, everything included is an accumulation of [Docker best practices](https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose) based on building and deploying dozens of assorted Dockerized web apps since late 2014.

**This app is using Flask 2.3.2 and Python 3.11.4**.

[![Screenshot](.github/docs/screenshot.jpg)](https://github.com/christian-bromann/flask-app/blob/main/.github/docs/screenshot.jpg?raw=true)

## Requirements

Make sure you have the following requirements installed on your machine:

- Docker Desktop (v24 or above)
- Docker Compose (v2.20 or above)

## Getting Started

This project uses [Runme](https://runme.dev) as operation engine and has several runbooks defined within the `/docs` directory. To get started make sure you have Runme installed:

- As [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=stateful.runme)
- as CLI command using `brew install runme` or `npm install -g runme` (more installation options can be found in the [docs](https://docs.runme.dev/install#runme-cli))

Once installed you get an overview on all available commands via:

```sh
runme ls
```

Open [`DEVELOPMENT.md`](./docs/DEVELOPMENT.md) for further instructions.