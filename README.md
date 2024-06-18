# no-exif
no-exif is a python utility that removes exif data from images in a folder, to allow for sharing online. it supports multi-threading for faster performance when processing lots of images.

## dependencies
- pillow - image manipulation
- tqdm - progress bar

## instructions
1. clone the repo
2. download the dependencies listed above
3. run `no-exif.py`
4. enter the path where your target images are
5. enter the max amount of threads to be spawned. i recommend around 20-25; adding more threads will result in high RAM/CPU usage with diminishing speed results
6. the cleaned images will be stored in the `no-exif` folder, inside the folder you selected earlier
