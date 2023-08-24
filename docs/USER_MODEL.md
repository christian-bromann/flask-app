# User Model

This Flask application has a user model implemented. To run the cells in this runbook make sure you have setup your [Development Environment](./DEVELOPMENT.md). You can fetch all existing users stored in the DB via:

```sh
curl -X GET http://localhost:8000/api/user
```

Create a user by running:

```sh
export USER_NAME=<username>
export EMAIL=<email>
curl -X POST http://localhost:8000/api/user \
    -H "Content-Type: application/json" \
    -d '{"username": "'"$USER_NAME"'", "email": "'"$EMAIL"'"}'
```

You can inspect a single user via:

```sh
export ID=<id>
curl -X GET http://localhost:8000/api/user/$ID
```