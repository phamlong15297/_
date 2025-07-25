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

## Note
Currently, in `style-checking.yml` file, we setup Ruff, pyrefly, eslint as local but what if we use precommit like this
```yml
  precommit:
    needs: get-changed-files
    if: ${{ needs.get-changed-files.outputs.py_files != '' || needs.get-changed-files.outputs.js_files != '' }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          cache: 'pip'

      - name: Install pre-commit
        run: |
          pip install pre-commit
          pre-commit install

      - name: Run pre-commit
        run: |
          FILES="${{ needs.get-changed-files.outputs.py_files }} ${{ needs.get-changed-files.outputs.js_files }}"
          echo "Running pre-commit on files: $FILES"
          pre-commit run --files $FILES
```
Pre-commit will run ruff, prefly, eslint as local, so if modify, we need modify pre-commit file only.

## Update
`Biome` is a new tool that can replace both `Eslint + Prettier` but it does not support Vscode yet. So every time doing something, we have to check by command which is not convinient.

## Ruff
Add to `requirements.txt` or run `pip install ruff`

To check manually
```shell
ruff check --fix
```

To run on git commit
```shell
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4
    hooks:
      - id: ruff
        args: [--fix] # auto fix code on git commit - add this
```