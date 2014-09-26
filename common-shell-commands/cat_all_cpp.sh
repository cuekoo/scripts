#!/bin/bash

FILES=`ls *.cpp`

for args in $FILES; do
    cat $args
done
