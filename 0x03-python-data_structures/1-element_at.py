#!/usr/bin/python3
def element_at(my_list, idx):
    y = len(my_list)
    if idx < 0 or idx > (y - 1):
        return None
    x = my_list[idx]
    return x
