# Run python linter & checker on github action & pre-commit locally

## uv
> Python package manager
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```
**Init pyproject.toml**
```shell
uv init
```

**Install all dependencies & create virtual environment**
```shell
# Local dev
uv sync --dev
# Product environment
uv sync
```

**Activate venv**
```shell
source ./.venv/bin/activate
```

**Add new package**
```shell
uv add <package-name> # ex: uv add fastapi
uv add --dev <package-name> # ex: uv add ruff
```

## Precommit
### Install
```shell
pre-commit install
```

After installing it, every time you run `git commit`, it will run to check code in the changed files (rules are defined in `.pre-commit-config.yaml`)

GitHub action with the same checks will run just in case we pass the pre-commit (without installing, bypass with config,..)

### Mually run
**Run against all files**
```shell
pre-commit run --all-files
```

**Run against added files**
```shell
pre-commit run
```
### Update version of pre-commit dependencies
To update version of tool inside `.pre-commit-config.yaml`
```shell
pre-commit autoupdate
```

## Python
Vscode Extensions
* meta.pyrefly
* charliermarsh.ruff
* EditorConfig.EditorConfig

## Eslint and prettier
### Vscode extensions
* esbenp.prettier-vscode
* dbaeumer.vscode-eslint

### Install
```shell
npm install --save-dev eslint prettier eslint-config-prettier eslint-plugin-prettier
```

### Command
```shell
npx prettier --check [file]
npx prettier --write [file]
npx eslint
```
## Update
`Biome` is a new tool that can replace both `Eslint + Prettier` but it does not support Vscode yet. So every time doing something, we have to check by command which is not convinient.

## Ruff
Add to `requirements.txt` or run `pip install ruff`

To lint and format
```shell
ruff check --fix
ruff format
```

Precommit hooks are defined in `.pre-commit-config.yaml`. They are equivalent to
```shell
ruff check
ruff format --diff
```
### Vscode
In Vscode's UI, right click then "Format code with ... + Ruff" and "Source Action ..." to trigger Ruff

## Issues

### Pyrefly
Sometimes, it does not recognize the `.venv` folder, choose Python interpreter in right corner then Ctrl Shift P + Reload
