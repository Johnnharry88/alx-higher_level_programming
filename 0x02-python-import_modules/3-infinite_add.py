#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ans = 0
    sch = len(sys.argv)
    for alx in range(1, sch):
        ans = ans + int(sys.argv[alx])
    print("{}".format(ans))
