# Deployment

This application is deployed on [fly.io](https://fly.io/). You can trigger a new deploy via:

```sh { name=deploy cwd=../ }
fly deploy
```

Run quick post deployment tests:

```py { name=deploy.postdeploymentCheck }
import requests
response = requests.get("https://flask.fly.dev")
assert response.status_code == 200
print("Post Deployment Check successful ✅")
```

Generate changelog:

```js
const cp = require('node:child_process')
const log = cp.execSync('git log --pretty=oneline').toString('utf-8')
    // iterate over every line
    .split('\n')
    // get last 10 log lines
    .slice(0, 10)
    // seperate sha from message
    .map((log) => log.split(' '))
    // filter last line
    .filter(([sha]) => Boolean(sha))
    // format message
    .map(([sha, ...message]) => `(fix) ${message.join(' ')} (${sha.slice(0, 10)})`)
    .join('\n')
console.log(log)
```

Create git tag:

```sh
export GIT_TAG="enter git tag"
git tag -a $GIT_TAG -m "Release $GIT_TAG\n\nChangelog:\n$__"
git show $GIT_TAG
```