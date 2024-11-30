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
conda create --name env_name python=3.9
conda install <package-name>

# Have pip-tools installed
pip install pip-tools==7.0.0
# Use requirements.in to keep track core packages
# Build requirements.txt based on requirements.in
pip-compile -v --rebuild -o requirements.txt
pip-sync requirements.txt

# jupyter notebook kernel
python -m ipykernel install --user --name=<env-name> 
jupyter kernelspec list # verify that kernel is installed
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
| `mlflow`| model version control|
| `pathlib`| get suffix, extension of file|

#### Demo

For quick prototyping, use Jupyter Notebook widget (ipywidgets), gradio, streamlit, dash plotly.


#### Class

- decorator @dataclass to create a struct contain fields without specifying in __init__.
- decorator @classmethod to convert a function into class method.