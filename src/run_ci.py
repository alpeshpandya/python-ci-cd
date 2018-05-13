from pylint import lint
from pylint.reporters.json import JSONReporter
import sys
import json
import importlib, os, sys
import unittest

ARGS = ["-r","n"]

class WritableObject(object):
    "dummy output stream for pylint"
    def __init__(self):
        self.content = []
    def write(self, st):
        "dummy write"
        print st
        self.content.append(st)
    def read(self):
        "dummy read"
        return self.content

def run_pylint(filename):
    print "RUNNING PyLint FOR::::"+filename
    pylint_output = WritableObject()
    lint.Run([filename]+ARGS, reporter=JSONReporter(pylint_output), exit=False)
    for l in pylint_output.read():
        if "trailing-newlines" not in l:
            print l
    return pylint_output.content

def runtests(filename):

    file = os.path.basename(filename)
    dir = os.path.dirname(filename)
    print "RUNNING TEST IN:::"+dir
    test_suite = unittest.TestLoader().discover(dir, pattern=file)
    test_runner = unittest.TextTestRunner().run(test_suite)
    return test_runner

if __name__ == "__main__":
    filename=sys.argv[1]
    run_pylint(filename)
    test_results = runtests(filename)
    
