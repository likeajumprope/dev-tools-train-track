# Development Tools Train Track

Instructions for the Development tools (VS Code) train track

## Installation

### Python

There are many different ways to install Python depending on your OS and preferences. Real Python give a nice list of them here
https://realpython.com/installing-python/

For the uninitated, there is a substantial difference between Python versions 2 & 3, which means most code written for one won't work for the other by default. Python 2 has been deprecated since 2020, so we will be working with Python 3 exclusively. Therefore, please make sure the Python you have installed is version 3 (e.g `python --version`), or ensure you always use the `python3` and `pip3` aliases.


### Install VS Code + extensions

Installing VS Code itself is pretty straightforward. Just [download](https://code.visualstudio.com/download) and [install](https://code.visualstudio.com/docs/setup/setup-overview) it from the visual studio website.

VS Code is a general purpose code editor that can be configured to be used for virtually any programming language. This supported by a wide array of 3rd party extensions. New extensions can be added to your workspace by clicking on the "Extensions" tab on the bar on the LHS of the screen

<img width="1704" alt="extensions-tab" src="https://user-images.githubusercontent.com/1054870/144533458-92fdc895-b464-4c18-9d65-cd77021a7f4b.png">

The extensions we will use/reference today are

* Python
* Github
* Gitlens
* Docker

### Virtual environments

One of the major strengths of Python compared to other programming languages is the vast amount of 3rd party packages available, which come in all shapes and sizes (you can even write one yourself pretty easily!). However, with this vastness comes a fair bit of complexity in managing shared dependencies, particularly ones that require specific versions. To get around this, it is common to create a fresh "environment" for each project/workspace and install only the packages you need for it in order to avoid clashes.

There are two popular ways to create virtual environments in Python either using the built-in `venv` module or the more general software package manager [Anaconda](https://anaconda.org/anaconda/python) (which Chris explained how to use in the "Intro to Python" train-track earlier this week). Since we will be relying on some packages that have C dependencies we will use Anaconda to manage them for this tutorial.

To do this you first create a new conda environment

```conda create --name bhg-devtools```

and then activate it, which you need to do **before** installing or using your packages every time you open a new terminal

```conda activate bhg-devtools```

The packages you will need to install inside your Conda environment for today's session are

* dipy
* click
* pytest

by using 

```conda install -c conda-forge dipy click pytest```

After setting up your virtual environment you will need to configure VS Code to use it by selecting the Python interpreter for your workspace (see https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)


### Clone repository

Create a fork of the https://github.com/brainhack-aus/dev-tools-train-track repository (i.e. this one) by using the source control tab

![source-control-tab](https://user-images.githubusercontent.com/1054870/144535957-e6905dce-0218-4274-ac01-9e67c317389f.png)

and open it as a new project.

Should see virtually empty project with just a README file and gitignore.

You will then pull some changes I have made upstream using the source control tab.


## Create Dipy program

### Simple intensify method

Use the examples shown in the [Dipy Quick Start Guide](https://dipy.org/documentation/1.4.1./examples_built/quick_start/#example-quick-start) to create three (trivial) methods in a new module, i.e. a Python file called `intensify.py`, to load a nifti file, multiply its intensity, and save it back to disk.

### Write command line using click

Use [click](https://click.palletsprojects.com/en/8.0.x/quickstart/#basic-concepts-creating-a-command) to create a script in a separate file that imports and runs your method in a command line tool that takes the following arguments/options

* input file path (argument)
* output file path (argument)
* intensity (option with default value)

### More advanced example

If you are feeling confident you might want to work with this cool example to estimate the SNR of diffusion-weighted images
https://dipy.org/documentation/1.4.1./examples_built/snr_in_cc/#example-snr-in-cc.


## Run, debug and test package

### Open a terminal within vscode and run script

Open new terminal by pressing Ctrl-Shift-P (Cmd-Shift-P on Mac), typing "terminal" and selecting "new terminal". This is just a normal terminal so you can run your command line tool by

```python3 your-script.py```

### Launch a script via launcher/debugger

Create a launch.json file from the "Run and Debug" tab in the LHS menu

### Write a unittest with pytest

Create a directory called `tests` and a file called `test_intensify.py` within it.

Write a simple test that tests a small part of your code e.g.

```python
def test_intensify():
    orig_image = dipy.load_nifti()
    intensified_image = intensify(orig_image, 10)
    assert np.max(my_image) == np.max(orig_image) * 10
```
### Configure Conftest to break in exception

Add a `conftest.py` file to allow unittests to break on exceptions in debug mode 

```python
import os
import shutil
from pathlib import Path
from tempfile import mkdtemp
import pytest


@pytest.fixture
def work_dir():
    tmp_dir = tempfile.mkdtemp()
    yield tmp_dir
    shutil.rmtree(tmp_dir)

# For debugging in IDE's don't catch raised exceptions and let the IDE
# break at it
if os.getenv('_PYTEST_RAISE', "0") != "0":

    @pytest.hookimpl(tryfirst=True)
    def pytest_exception_interact(call):
        raise call.excinfo.value

    @pytest.hookimpl(tryfirst=True)
    def pytest_internalerror(excinfo):
        raise excinfo.value

```

