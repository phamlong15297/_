# Run python linter & checker on github action & pre-commit locally

```shell
pip install pre-commit
pre-commit install
```

After installing it, every time you run `git commit`, it will run to check code in the changed files (rules are defined in `.pre-commit-config.yaml`)

GitHub action with the same checks will run just in case we pass the pre-commit (without installing, bypass with config,..)

## .venv
```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r ./project1/requirements.txt -r ./project2/requirements.txt
```

## Eslint and prettier
### Vscode extensions
* esbenp.prettier-vscode
* dbaeumer.vscode-eslint

### Install
```shell
npm install --save-dev eslint prettier eslint-config-prettier eslint-plugin-prettier
```
