
## Naming
temporary project name `arial` - changing project requires changing repo name (optional, but less confusing)
and changing:
- [ ] pyproject.toml["name"]
- [ ] ./arial
- [ ] change repo name
- [ ] change any local git configurations of remotes

## Useful commands
```poetry run jupyter notebook```
```poetry run ipython kernel install --user --name=dev && jupyter notebook```

## Containers
Multiple dev-container setup in case we need different builds / environments. 

#### test
reserved for any changes to builds

#### dev
reserved for app-level code changes
