import defcon
import extractor
import os
import pathlib
import ufonormalizer

# Base file names of all of the Clear Sans fonts
baseFileNames = [
    "ClearSans-Bold",
    "ClearSans-BoldItalic",
    "ClearSans-Italic",
    "ClearSans-Light",
    "ClearSans-Medium",
    "ClearSans-MediumItalic",
    "ClearSans-Regular",
    "ClearSans-Thin",
]

# Directory paths
ttfFontsPath = os.path.join("..", "fonts", "ttf")
ufoSourcesPath = os.path.join("..", "sources")

# Create the UFO sources directory if it does not exist
pathlib.Path(ufoSourcesPath).mkdir(parents=True, exist_ok=True)

for baseFileName in baseFileNames:
    # Create a new Font object
    font = defcon.Font()

    # File paths
    ttfFilePath = os.path.join(ttfFontsPath, baseFileName + ".ttf")
    ufoFilePath = os.path.join(ufoSourcesPath, baseFileName + ".ufo")

    # Load the TrueType font data into the Font object
    extractor.extractUFO(ttfFilePath, font)

    # Save the Font object as a UFO (Unified Font Object)
    font.save(ufoFilePath)

    # Close the font since we are going to normalize it next
    font.close()

    # Normalize the UFO without writing modification times
    ufonormalizer.normalizeUFO(ufoFilePath, writeModTimes=False)
