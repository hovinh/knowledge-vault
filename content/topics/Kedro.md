#### Setup

```bash
# Have pip-tools installed
pip install pip-tools==7.0.0
# Use requirements.in to keep track core packages
# Build requirements.txt based on requirements.in
pip-compile -v --rebuild -o requirements.txt
pip-sync requirements.txt
```

#### Code Snippets

| Command | Place | Description |
| -------- | -------- | -------- |
| `hostname -i`| Terminal | Get hostname to view pipeline dashboard|
| `kedro viz run --host <host-name> --port <port-id>`| Terminal | Execute pipeline visualization|
| `kedro run --pipeline <pipeline-name>`| Terminal | Execute a specific pipeline|
| `kedro pipeline`| Terminal | Create a new pipeline |
| `kedro registry list`| Terminal | List all datasets in the registry |
| `%load_ext kedro.ipython`| Jupyter notebook | Load context, session, catalog, pipelines |
| `%reload_kedro`| ipython | Load context, session, catalog, pipelines |
| `catalog.load('params:a')`| Python | Load parameters from catalog |
