#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    store = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    xty = 0
    alx = len(roman_string)
    for x in range(alx):
        if x > 0 and store[roman_string[x]] > store[roman_string[x - 1]]:
            xty = xty + store[roman_string[x]] - 2 * \
                    store[roman_string[x - 1]]
        else:
            xty = xty + store[roman_string[x]]
    return xty
