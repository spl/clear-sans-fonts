#!/bin/sh

# - Generate UFO sources from TrueType fonts with the `fontforge` library.
# - Run in background with `&` to parallelize.

# Use the Python script with the same base name.
script=`basename -s .sh $0`.py

# Add Homebrew `fontforge` Python package directories to PYTHONPATH. This is
# necessary to use the `fontforge` library along with the dependencies installed
# with `poetry`.
for pythonLibDirPath in `brew --prefix fontforge`/lib/python*
do
  PYTHONPATH="$pythonLibDirPath/site-packages":"$PYTHONPATH"
done
export PYTHONPATH

for ttf in ../fonts/ttf/*.ttf
do
  poetry run python "$script" `basename -s .ttf $ttf` &
done

wait # for all background child jobs to complete.
