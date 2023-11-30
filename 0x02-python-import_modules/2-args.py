#!/usr/bin/python3
import sys
l_arg = len(sys.argv)
if l_arg == 1:
    print("{} arguments.".format(l_arg - 1))
elif l_arg == 2:
    print("{} argument:".format(l_arg - 1))
else:
    print("{} arguments:".format(l_arg - 1))

for alx in range(1, l_arg):
    print("{}: {}".format(alx, sys.argv[alx]))
