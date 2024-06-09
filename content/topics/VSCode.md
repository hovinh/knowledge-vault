#### Settings

| Attribute | Description |
| -------- | -------- |
| `Formatter` | Enable "Format on Save". Install your python environment with `autopep8`, `black`, or `prettier`|
| `Auto Save`| `onWindowChange`|
| `Open with VSCode` on any file/folder| [StackOverFlow-Wosy](https://stackoverflow.com/questions/37306672/visual-studio-code-open-with-code-does-not-appear-after-right-clicking-a-folde)|
|Enable `Anaconda Prompt` in terminal list| [StackOverFlow-Simba](https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10)|

<br>

Create **Anaconda Prompt Terminal Profile**: 
- `Ctrl+Shift+P` in selected conda environment -> `Preferences: Open User Settings (JSON)` -> `Edit in settings.json`

```yaml
"terminal.integrated.defaultProfile.windows": "Command Prompt",
    "terminal.integrated.profiles.windows": {
        "Anaconda Prompt": {
            "path": "${env:windir}\\System32\\cmd.exe",
            "args": [
                "/K",
                "C:\\Users\\user_name\\AppData\\Local\\Continuum\\anaconda3\\condabin\\activate.bat C:\\Users\\user_name\\AppData\\Local\\Continuum\\anaconda3"
            ],
            "icon": "squirrel"
        },
        "PowerShell": {
            "source": "PowerShell",
            "icon": "terminal-powershell"
        },
        "Command Prompt": {
            "path": [
                "${env:windir}\\Sysnative\\cmd.exe",
                "${env:windir}\\System32\\cmd.exe"
            ],
            "args": [],
            "icon": "terminal-cmd"
        },
        "Git Bash": {
            "source": "Git Bash"
        }
    }
```

#### Extension list

| Extension | Description |
| -------- | -------- |
| Python | interpreter to execute and navigate the code base, interact with jupyter notebook's kernel|
| indent-rainbow| highlight indentation|
| Codeium| AI coding autocomplete and chat|
| GitLens| Visualize Git-related attributes: code authorship...|

<br>

**indent-rainbow settings.json**
```yaml
"indentRainbow.colors": [
    "rgba(239, 68, 68, 0.3)",
    "rgba(251, 146, 60, 0.3)",
    "rgba(253, 224, 71, 0.3)",
    "rgba(163, 230, 53, 0.3)",
    "rgba(59, 130, 246, 0.3)",
    "rgba(168, 85, 247, 0.3)",
    "rgba(217, 70, 239, 0.3)",
]
```