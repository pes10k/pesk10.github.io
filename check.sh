#!/bin/bash

# Simple helper script to do some static checking of the code.

mypy --strict build.py
pycodestyle peteresnyder/*
