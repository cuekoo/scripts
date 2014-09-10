#!/usr/bin/python
#
# This script reads a sequance of chars and ouput the specified interval.

import sys

if len(sys.argv) != 3: 
    sys.exit("Usage: read_char.py filename start_idx end_idx")

start = int(sys.argv[1])
end   = int(sys.argv[2])

if start > end:
    sys.exit("Wrong arguments")

f = open('sequence.fasta', 'r')

cnt = 0

while True:
    char = f.read(1)
    if not char:
        break
    if char.isalpha(): 
        cnt += 1
        if cnt >= start and cnt <=end:
            print char

print 'Total: %d chars\n' % cnt
