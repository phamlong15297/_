# Run python linter & checker on github action & pre-commit locally

```shell
pip install pre-commit
pre-commit install
```

After installing it, every time you run `git commit`, it will run to check code in the changed files (rules are defined in `.pre-commit-config.yaml`)

GitHub action with the same checks will run just in case we pass the pre-commit (without installing, bypass with config,..)

## .venv
```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
uv pip install -r ./project1/requirements.txt -r ./project2/requirements.txt
```
