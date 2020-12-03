#!/bin/sh

# - Format all Python scripts with `yapf`.

poetry run yapf --in-place *.py
