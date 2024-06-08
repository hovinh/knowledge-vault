#### Setup


Install package hosted in jfrog
```bash
# one-time
python -m pip install --index https://jfrogbin... ---trusted-host jfrogbin... <package-name>

# permanent setup
pip config --user set global.index https://jfrogbin.../artifactory/api/pypi/pypi-all
pip config --user set global.index-url https://jfrogbin.../artifactory/api/pypi/pypi-all/simple
pip config --user set global.trusted-host jfrogbin...
pip install <package-name>
```

Setup virtual environment
```bash
# virtual-env
pip install virtualenv
mkdir environments
cd environments
virtualenv <env-name>
source <env-name>/bin/activate

# conda
```

Troubleshooting in script execution
```python
from IPython import embed; embed()
```

Package Note
| Command | Description |
| -------- | -------- |
| `pip-tools`| version 7.0.0 is stable|
| `black`| code formatter|