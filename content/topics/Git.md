#### Setup

Clone a repo ([instruction](https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-linux/)):
- install SSH agent and lauch it.
- generate private and public key in user directory.
- Copy public key to Bitbucket account.

#### Code Snippets

| Command | Description |
| -------- | -------- |
| `git clone <ssh_command>`| Clone a git repo; ensure no weird symbol to avoid unexpected error|
| `git branch -a`| Show all branches|
| `git branch -d <branch_name>`| Delete a local branch|
| `git checkout -b <branch_name>`| Create a local branch|
| `git checkout <branch_name>` | Checkout to a remote branch and track locally|
| `git push -u origin <new_branch>` | Push a local branch (not tracked in server) to server|
| `git fetch`| Get metadata of latest changes from remote|
| `git pull`| Download latest changes from remote|
| `git diff`| Show uncommited changes|
| `git add <file_1> <file_2>`| Stage files before committing|
| `git reset --staged <file_1>`| Unstage change|
| `git rm <file_1> --cached`| Stop tracking files|
| `git reset --hard`| Remove all uncommited changes; normally this should suffice|
| `git clean  -ndx`| Dry run to see what to be removed|
| `git clean -fdx`| Cannot be undone; use as your own risk|
| `git ls-tree --full-tree --name-only -r HEAD`| List all files being tracked|

<br>

Sample `.gitignore`:
- Linux: `touch .gitignore`, button `i` to insert, copy data over, `Esc` then `.wq` to save & exit.

```bash
/data
*.csv
*.html
*.zip
*.pkl
*.npz
*.pyc
__pycache__
*.ipynb_checkpoints*
.vscode
logs
data
.nfs*
*.pub
*.swp

```