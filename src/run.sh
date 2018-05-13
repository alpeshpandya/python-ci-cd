#!/bin/sh
NOTEBOOK_PATH=$1
PYTHON_NAME="$(basename $NOTEBOOK_PATH .ipynb)"
echo $PYTHON_NAME

ipython nbconvert --to=python $NOTEBOOK_PATH --output $PYTHON_NAME

DIRNAME=$(dirname $NOTEBOOK_PATH)
PYTHON_INPUT="$DIRNAME/$PYTHON_NAME"
echo $PYTHON_INPUT
python src/run_ci.py "$PYTHON_INPUT.py"
