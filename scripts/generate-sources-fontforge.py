import fontforge
import os
import sys
import ufonormalizer

# The only argument is the base name of the font. No directory or extension.
fileName = sys.argv[1]

# File paths
ttf = os.path.join(os.path.join("..", "fonts", "ttf"), fileName + ".ttf")
ufo = os.path.join(os.path.join("..", "sources"), fileName + ".ufo")

# Create a new FontForge font object from the TrueType font file
font = fontforge.open(ttf)

#font.correctReferences()

#for glyph in font.glyphs():
#    glyph.removeOverlap()
#    glyph.correctDirection()
#    glyph.addExtrema()
#    glyph.simplify()
#    glyph.round()

# Save the font object as a UFO (Unified Font Object)
font.generate(ufo)

# Close the font object since we are going to normalize it next
font.close()

# Normalize the UFO without writing modification times
ufonormalizer.normalizeUFO(ufo, writeModTimes=False)
