# Python data analysis template

A ready-to-use Python environment for data analysis in GitHub Codespaces. It includes
**pandas**, **polars**, **numpy** and **matplotlib**, plus Jupyter notebooks in VS Code.
There's nothing to install on your own computer.

## Start a new project

1. On this repository's GitHub page, click **Use this template → Create a new repository**.
2. Give it a name and create it. Choose **Private** if your data or code is sensitive.
3. In your new repository, click **Code → Codespaces → Create codespace on main**.
4. Wait a few minutes the first time while it builds. The terminal shows `uv sync` installing packages.
5. Open `notebooks/01_getting_started.ipynb` and run each cell with **Shift + Enter**.
   If you're asked to select a kernel, choose **Python Environments → .venv**.

## What's where

| Folder | Put this here | Saved to git? |
|---|---|---|
| `notebooks/` | Jupyter notebooks (`.ipynb`) | Yes |
| `scripts/` | Python scripts (`.py`) | Yes |
| `data/example/` | Small, non-sensitive example data | Yes |
| `data/raw/` | Original data, never edited | **No** |
| `data/processed/` | Cleaned data you've produced | **No** |
| `outputs/` | Charts, tables, exports | **No** |

`data/raw/`, `data/processed/` and `outputs/` are ignored by git on purpose, so data
files don't end up on GitHub by accident. Files stored there still stay in your
codespace between sessions.

**Never commit personal or confidential data**, even to a private repository.

## Everyday tasks

Run these in the VS Code terminal (**Ctrl + `**).

| I want to... | Command |
|---|---|
| Add a package (e.g. seaborn) | `uv add seaborn` |
| Remove a package | `uv remove seaborn` |
| Run a script | `uv run python scripts/example_analysis.py` |
| Tidy my code's formatting | `uv run ruff format .` |
| Check my code for mistakes | `uv run ruff check .` |
| Reinstall everything if something breaks | `uv sync` |

After `uv add`, restart the notebook kernel (the **Restart** button at the top of the
notebook) so it picks up the new package.

`uv add` updates `pyproject.toml` (the list of packages) and `uv.lock` (their exact
versions). Commit both files so anyone who opens the project gets the same setup.

## Uploading data

Drag files from your computer into a folder in the VS Code **Explorer** panel, or
right-click a folder and choose **Upload...**. Then load it with, for example:

```python
import pandas as pd
df = pd.read_csv("data/raw/my_file.csv")
```

Paths are relative to the top of the repository, in notebooks and scripts alike.

## Saving your work to GitHub

Use the **Source Control** panel (the branch icon on the left):

1. Type a short message describing what you changed.
2. Click **Commit**, then **Sync Changes**.

## Don't burn through your free hours

Codespaces bill for the time they're running. A codespace stops itself after 30
minutes of inactivity, but it's good practice to stop it yourself when you finish:
**Code → Codespaces → ... → Stop codespace** on GitHub, or run
**Codespaces: Stop Current Codespace** from the Command Palette (**Ctrl + Shift + P**).
Delete codespaces you no longer need at <https://github.com/codespaces>.

## Using this on your own computer

Install [VS Code](https://code.visualstudio.com/) and [uv](https://docs.astral.sh/uv/),
clone the repository, then run `uv sync` in its folder. Select the `.venv`
interpreter when VS Code asks.
