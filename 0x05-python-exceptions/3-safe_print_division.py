#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        ans = a / b
    except (TypeError, ZeroDivisionError):
        ans = None
    finally:
        print("Invlid result: {}".format(ans))
    return (ans)
