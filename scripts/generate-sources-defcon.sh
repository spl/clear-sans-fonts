#!/bin/sh

# - Generate UFO sources from TrueType fonts with the `ufo-extractor` and
#   `defcon` libraries.
# - Run in background with `&` to parallelize.

# Use the Python script with the same base name.
script=`basename -s .sh $0`.py

for ttf in ../fonts/ttf/*.ttf
do
  # Run the script in the `poetry` environment with the font file base name as
  # the argument.
  poetry run python "$script" `basename -s .ttf $ttf` &
done

wait # for all background child jobs to complete.
