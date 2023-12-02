#!/usr/bin/python3
def no_c(my_string):
    output = my_string
    output = output.translate({ord(x): None for x in 'Cc'})
    return output
