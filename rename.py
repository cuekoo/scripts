#!/usr/bin/python

# RENAME renames all *.jpg to *.JPG 

import os
import subprocess

for filename in os.listdir("."):
    basename, extension = os.path.splitext(filename)
    if extension == ".jpg":
        subprocess.call(["mv", filename, basename + ".JPG"])
