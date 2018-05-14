# Basic CI CD tool for iPython and Jupyter notebooks

## Features
* Setup script that creates virtual environment for the tool to run
* Run script that converts notebook to python script and executes CI CD on it
* Performs static analysis of python code and displays errors/warnings
* Executes test cases defined in the script (if any)

## How to
* Setup
  * Clone https://github.com/alpeshpandya/python-ci-cd.git
  * `cd python-ci-cd`
  * `chmod 0755 src/*`
  * `src/setup.sh`
* Run
  * `src/run.sh data/classification_clean.ipynb`
