#!/usr/bin/python3
alx =122
while alx >= 97:
    switch = 0
    if alx % 2!= 0:
        alx = alx - 32
        switch = 1
    print("{:c}".format(alx), end="")
    if switch == 1:
        alx = alx + 32
    alx = alx - 1
