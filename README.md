# Python Virtual Environment Manager

A tool to easily manage python virtual environments in new projects.

## TODO
- support different python versions
- support windows

## Notes
Made for macOS.

## Install/Uninstall
```bash
# Development mode, changes in code will reflect
pip install -e .
# Standard Installation
pip install .
# Direct installation
pip install git+https://github.com/lawsus/python-venv-manager.git

# Uninstall the package
pip uninstall python-venv-manager
```

## Usage
```bash
vem --help
```
```
usage: vem [-h] [--create] [--delete] [--reset] [--update] [--activate] [--deactivate]

Manage your Python virtual environment.

options:
  -h, --help    show this help message and exit
  --create      Create the virtual environment and install dependencies if requirements.txt exists.
  --delete      Delete the virtual environment.
  --reset       Reset the virtual environment by deleting and recreating it.
  --update      Update the dependencies in the virtual environment.
  --activate    Get command to activate the virtual environment.
  --deactivate  Get command to deactivate the virtual environment.
```