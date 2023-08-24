# User Model

This Flask application has a user model implemented. To run the cells in this runbook make sure you have setup your [Development Environment](./DEVELOPMENT.md). You can fetch all existing users stored in the DB via:

```py
import requests
import json

r = requests.get(url = "http://localhost:8000/api/user") 
print(json.dumps(r.json(), indent=2))
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

```js
const http = require('http');

http.get('http://localhost:8000/api/user/1', (res) => {
    let data = [];
    res.on('data', (chunk) => data.push(chunk));
    res.on('end', () => console.log(JSON.parse(Buffer.concat(data).toString())));
});
```