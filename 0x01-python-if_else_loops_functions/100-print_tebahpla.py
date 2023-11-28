#!/usr/bin/python3
for alx in range(ord('z'), ord('a') - 1, - 1):
    print("{:c}{:c}".format(alx, (alx - 32)), end="")
