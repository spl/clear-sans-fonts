#!/bin/sh

# - Generate UFO sources from TrueType fonts.
# - Run in background with `&` to parallelize.

for ttf in ../fonts/ttf/*.ttf
do
  poetry run python extractUfo.py `basename -s .ttf $ttf` &
done

wait # for all background child jobs to complete.
