#!/usr/bin/python3
sub = 0
for alx in range(ord('z'), ord('a') - 1, -2):
    print("{}".format(chr(alx + sub)), end="")
    if sub == 0:
        sub = sub + 32
    else:
        sub = 0
