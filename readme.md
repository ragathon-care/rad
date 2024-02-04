# RAD! - a rag assistant for disability resources

Finding resources can be really tough for people with disabilities or their caretakers. They're often left bouncing between different counselors and departments. Can we make resources finding easier?


## Navigating

| Path | Description |
| ---- | ----------- |
| `frontend/` | a simple chat UI extending llama-index's SEC Insights app |
| `backend/` | a backend api and job hosting the chat agent |
| `rad/` | the project package defining the llama agent used in the chat backend |
| `scratchpad.http` | contains some http requests to make quick surveys of apis. Use the REST Client extension to use (ext id: humao.rest-client). This requires the `DIFFBOT_TOKEN` environment variable to be specified.|
| `.env.development` | contains keys for environment variables useful in your dev setup. Rename the file to .env (this is git ignored so you're safe).|
| `samples/` | contains any kind of sample API responses we get in case we need a quick reference, and to avoid having to waste credits.|


## Useful commands
In case you'd like to use a jupyter notebook within the poetry environment, you can:
```bash
poetry run jupyter notebook
```
or...
```bash
poetry run ipython kernel install --user --name=dev && jupyter notebook
```

vscode doesn't recognize default path of installed venvs via poetry so configure
the venvs to be within the project
```bash
poetry config virtualenvs.in-project true
poetry install
```
