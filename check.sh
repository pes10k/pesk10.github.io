#!/bin/bash

# Simple helper script to do some static checking of the code.

mypy --strict build.py
pylint --disable=missing-class-docstring,missing-function-docstring,missing-module-docstring,too-many-arguments peteresnyder build.py
