#!/usr/bin/python

# simple command line argument manipulation

import sys

if len(sys.argv) != 2:
    sys.exit("Usage: cmdline_arg.py ARGUMENT")

if sys.argv[1] == "print":
    print "hello world!"
else:
    print "unknown argument"



