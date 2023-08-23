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
assert "Learn to Build a SAAS App with Flask" in response.text
print("Post Deployment Check successful ✅")
```

Generate changelog:

```js
const cp = require('node:child_process')
const commitTypes = {
    'feat': '🚀 New Feature',
    'test': '🧪 Testing',
    'chore': '🧹 Cleanups',
    'backend': '🧱 Backend',
    'other': '🧩 Miscellaneous'
}
const logGroups = cp.execSync('git log --pretty=oneline').toString('utf-8')
    // iterate over every line
    .split('\n')
    // get last 10 log lines
    .slice(0, 10)
    // seperate sha from message
    .map((log) => log.split(' '))
    // filter last line
    .filter(([sha]) => Boolean(sha))
    // group commit messages
    .reduce((prev, [sha, ...message]) => {
        const msg = message.join(' ')
        const type = msg.match(/\(\w+\):/g)
        const commitType = type ? type[0].slice(1, -2) : 'other'
        if (!prev[commitType]) {
            prev[commitType] = []
        }
        prev[commitType].push(type ? msg.slice(type[0].length + 1) : msg)
        return prev
    }, {})
const changelog = Object.entries(logGroups).map(
    ([commitType, changes]) => `## ${commitTypes[commitType]}\n- ${changes.join(`\n- `)}`
).join('\n\n')
console.log(changelog)
```

Create git tag:

```sh
export GIT_TAG="enter git tag"
git tag -a $GIT_TAG -m "Release $GIT_TAG\n\nChangelog:\n$__"
git show $GIT_TAG
```