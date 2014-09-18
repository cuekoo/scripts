#!/usr/bin/python

import os
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: ./check_file_existence.py FILENAME")

filename = sys.argv[1]
if os.path.isfile(filename):
    print filename + " exists"
else:
    print filename + " can't be found"

