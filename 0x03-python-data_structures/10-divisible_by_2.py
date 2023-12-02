#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Twos = []
    a = len(my_list)
    for x in range(a):
        if my_list[x] % 2 == 0:
            Twos.append(True)
        else:
            Twos.append(False)
    return Twos
