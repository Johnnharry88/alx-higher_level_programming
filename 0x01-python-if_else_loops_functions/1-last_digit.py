#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
state = 0
if number < 0:
    number = number * -1
    state = 1
else:
    number = number * 1
    state = 0

units = number % 10
if state == 1:
    number = number * -1
    units = units * -1
print(f"Last digit of {number:d} is {units:d} ", end="")
if units > 5:
    print("and is greater than 5")
elif units == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
