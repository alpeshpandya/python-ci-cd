#!/bin/sh
virtualenv python-ci-cd-env
chmod 0755 python-ci-cd-env/bin/activate
script_dir=`dirname $0`
/bin/bash -c ". python-ci-cd-env/bin/activate"
which python
pip install -r src/requirements.txt
deactivate
