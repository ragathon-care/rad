## Getting Started

`scratchpad.http` contains some http requests to make quick surveys of apis.
Use the REST Client extension to use (ext id: humao.rest-client). This requires
the `DIFFBOT_TOKEN` environment variable to be specified.

`.env.development` contains keys for environment variables useful in your
dev setup. Rename the file to .env (this is git ignored so you're safe).

`samples/` contains any kind of sample API responses we get in case we need
a quick reference, and to avoid having to waste credits.

You may also want to check out the [useful commands](#useful-commands) section
in case you are having trouble with vscode.

## Useful commands
```bash
poetry run jupyter notebook
```

```bash
poetry run ipython kernel install --user --name=dev && jupyter notebook
```

vscode doesn't recognize default path of installed venvs via poetry so configure
the venvs to be within the project
```bash
poetry config virtualenvs.in-project true
poetry install
```


## Containers
Multiple dev-container setup in case we need different builds / environments. 

#### test
reserved for any changes to builds

#### dev
reserved for app-level code changes
