# Development Tools Train Track

Instructions for the Development tools (VS Code) train track

## Installation

### Python itself

There are many different ways to install Python depending on your OS and preferences. Real Python give a nice list of them here
https://realpython.com/installing-python/

For the uninitated, there is a substantial difference between Python versions 2 & 3, which means most code written for one won't work for the other by default. Python 2 has been deprecated since 2020, so we will be working with Python 3 exclusively. Therefore, please make sure the Python you have installed is version 3 (e.g `python --version`), or ensure you always use the `python3` and `pip3` aliases.

### Virtual environments

One of the major strengths of Python compared to other programming languages is the vast amount of 3rd party packages available, which come in all shapes and sizes (you can even write one yourself pretty easily!). However, with this vastness comes a fair bit of complexity in managing shared dependencies, particularly ones that require specific versions. To get around this, it is common to create a fresh "environment" for each project/workspace and install only the packages you need for it in order to avoid clashes.

There are two popular ways to create virtual environments in Python either using the built-in `venv` module or the more general software package manager [Anaconda](https://anaconda.org/anaconda/python) (which Chris explained how to use in the "Intro to Python" train-track earlier this week). Either way is fine to use for this tutorial, so if you are set up with "Conda" already it is fine to use that, but it is a bit quicker to get started with `venv` so we will go with that by default.

To create a new virtual env in Python 3 simply type

```python3 -m venv /a/directory/on/your/system```

which will create a new virtual environment (i.e. place to install Python packages) in the `/a/directory/on/your/system` directory. To activate the virtual environment

### Install VS Code + extensions

[Download](https://code.visualstudio.com/download) and [install](https://code.visualstudio.com/docs/setup/setup-overview) Visual Studio Code

https://code.visualstudio.com/docs/python/environments

## Write a simple package

### Clone repository

Create a fork of the https://github.com/brainhack-aus/dev-tools-train-track repository (i.e. this one).

### Dipy tutorial
### Write command line using click

## Run, debug and test package

### Open a terminal within vscode and run script
### Launch a script via launcher/debugger
### Write a unittest with pytest
### Configure Conftest to break in exception
