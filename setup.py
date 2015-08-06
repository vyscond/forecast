
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup
import json
setupjson = json.load(open('setup.json'))
# additionals entries not covered by the project can be add here! :)
setup(**setupjson)

