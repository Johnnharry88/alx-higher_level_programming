#!/usr/bin/python3
form hidden_4 import *
store = dir()
x = len(store)
for alx in range (0, x):
    if store[alx][:2] != "__":
        print("{}".format(store[alx]))
