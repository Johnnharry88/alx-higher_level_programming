#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp = my_list[:]
    x = len(my_list)
    for itr in range(x):
        if tmp[itr] == search:
            tmp[itr] = replace
    return (tmp)
