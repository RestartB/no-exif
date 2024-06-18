# no-exif v1 - Restart 2024

# Imports
import os
from PIL import Image, ImageOps
from tqdm import tqdm
import threading
import sys

# Remove EXIF Function
def removeEXIF(path, file):
    try:
        # if not(os.path.isdir(file)):
        # Open input file
        original = Image.open(os.path.join(path, file))

        # Get key image data
        originalData = ImageOps.exif_transpose(original)

        # Create image with removed metadata
        stripped = Image.new(originalData.mode, originalData.size)
        stripped.putdata(list(originalData.getdata()))
        stripped.save(os.path.join(path, "no-exif", file))
        
        progress.update(1)
    except Exception as error:
        print(f"\nFailed to remove data from the following file: {os.path.basename(file)}\n{error}\n")

# Get path and files
try:
    path = input("Enter path: ")
    path = os.path.normpath(path)
    files = os.listdir(path)
except FileNotFoundError:
    print("Error: couldn't find that folder! Check the spelling and try again.")
    sys.exit(1)

# Get max amount of threads
threadAmount = int(input("Enter max amount of threads to spawn (12 recommended): "))

input(f"\nAbout to remove EXIF data from images in the following directory:\n{path}\n\nTo start, press enter.\n")

# Create no-exif folder
if not(os.path.isdir(os.path.join(path, "no-exif"))):
    os.mkdir(os.path.join(path, "no-exif"))

# Set up progress bar
global progress
progress = tqdm(total=len(files))

progress.set_description("Processing images")

# Process files
try:
    for file in files:
        try:
            while True:
                # Create thread when there is an available slot
                if len(threading.enumerate()) < threadAmount:
                    threading.Thread(target=removeEXIF, args=[path, file], daemon=True).start()
                    break
                else:
                    continue
        except Exception as error:
            print(f"\nThreading error while removing data from the following file: {os.path.basename(file)}\n{error}\n\nStopping program.")
            sys.exit(1)

    # Wait for threads to stop
    while not(len(threading.enumerate()) == 1):
        continue
except KeyboardInterrupt:
    print("\n\nAborting.")
    sys.exit(0)

# Complete!
print(f"\nComplete! Converted path:\n{os.path.join(path, "no-exif")}")
sys.exit(0)