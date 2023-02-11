# Installing in Windows

## Python

* Download and install (don't use windows store -- it installs to a weird path)
* Add to path (I had to place it at the front of the path)
* Restart powershell
* This should now find it: `get-command python`

## PyEnv

* `python -m pip install pyenv-win`
* run the above again to see where it was installed.  Create an environment variable `PYENV_HOME` pointing to this.  Add `%PYENV_HOME%\bin` to the path.
* modify powershell execution policy to allow running scripts

## Poetry

* Create an environment variable `POETRY_HOME`.  Initialize it to where you want this installed.  Also, add `%POETRY_HOME%\bin` to the path.
* Install poetry: `(iwr https://install.python-poetry.org/ -UseBasicParsing).Content | python`
* No need to restart terminal: `poetry --version`
* cd into the directory with your project
* Create a `pyproject.toml`: `poetry init`
* `poetry config virtualenvs.path "$(pwd)/.venv"`
* Create the environment: `poetry env use $(get-command python)`

## Git

* Download git for windows

## Spark

* `git clone https://github.com/steveloughran/winutils.git`
* Download spark pre-built for apache hadoop 2.7
* Verify: `certUtil --hashfile ~\Downloads\spark... SHA512`


## PySpark
