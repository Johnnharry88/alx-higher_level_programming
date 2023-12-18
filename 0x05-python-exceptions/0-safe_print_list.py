#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    t_sum = 0
    for a in range(x):
        try:
            print(f"{my_list[a]}", end="")
            t_sum = t_sum + 1
        except IndexError:
            break
    print()
    return (t_sum)
