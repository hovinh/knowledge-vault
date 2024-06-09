#### Setup

**Use Jupyter lab as editor**
- Create a new Workbench session. In Terminal: `pip3 install jupyterlab`
- Test out in Terminal: `/home/cdsw/.local/bin/jupyter-lab --no-browser --ip=127.0.0.1 --port=${CDSW_APP_PORT} --NotebookApp.token= --NotebookApp.allow_remote_access=True --log-level=ERROR`
- If works, enable in project page, `Settings` -> `Editors` -> `New Editor`

**Setup a CRON job** (this shares the same environment with Workbench): CDSW repo -> Tab `Jobs` -> `Create job`.

**Set session timeout to be longer**: go to `Project Settings` -> `Advanced` -> `Environment Variables`
- JUPYTER_KERNEL_TIMEOUT_SECONDS: 9999999999999
- JUPYTER_SERVER_TIMEOUT_SECONDS: 9999999999999

**Clean up storage space**
- Remove unused data
- Remove their deleted files in ~/.local/share/Trash/Files
- `rm -r files/`



