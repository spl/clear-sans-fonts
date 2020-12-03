import defcon
import extractor
import os
import pathlib
import sys
import ufonormalizer

# The only argument is the base name of the font. No directory or extension.
fileName = sys.argv[1]

# Create a new empty defcon font object
font = defcon.Font()

# File paths
ttf = os.path.join(os.path.join("..", "fonts", "ttf"), fileName + ".ttf")
ufo = os.path.join(os.path.join("..", "sources"), fileName + ".ufo")

# Load the TrueType font data into the font object
extractor.extractUFO(ttf, font)

# Save the font object as a UFO (Unified Font Object)
font.save(ufo)

# Close the font object since we are going to normalize it next
font.close()

# Normalize the UFO without writing modification times
ufonormalizer.normalizeUFO(ufo, writeModTimes=False)
