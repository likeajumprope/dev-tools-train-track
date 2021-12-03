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

```python3 -m venv /a/directory/to/install/yourenv```

which will create a new virtual environment (i.e. place to install Python packages) in the `/a/directory/to/install/yourenv` directory. To activate the virtual environment, which you need to do **before** installing and using any of the packages, use

```source /a/directory/to/install/yourenv/bin/activate``` on Linux/MacOs

and

```???``` on Windows

You should see the name of the directory (e.g. `(yourenv)`) as part of your command line prompt when the environment is activated.

### Install VS Code + extensions

Installing VS Code itself is pretty straightforward. Just [download](https://code.visualstudio.com/download) and [install](https://code.visualstudio.com/docs/setup/setup-overview) it from the visual studio website.

VS Code is a general purpose code editor that can be configured to be used for virtually any programming language. This supported by a wide array of 3rd party extensions. New extensions can be added to your workspace by clicking on the "Extensions" tab on the bar on the LHS of the screen

<img width="1549" alt="Screen Shot 2021-12-03 at 1 11 25 pm" src="https://user-images.githubusercontent.com/1054870/144533076-717bb891-3f5e-456e-bdcb-b0ddb6afc648.png">


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
