#!/usr/bin/env python3
# echob.py - echo command line args backwards
import sys

args = sys.argv[1:]          # list of args
for (i, _) in enumerate(args):
    print(args[len(args)-i-1], end=" ")
print()

##########################################

#    $ python3 echob.py one two three
#    three two one
#
