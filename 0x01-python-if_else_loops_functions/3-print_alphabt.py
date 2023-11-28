#!/usr/bin/python3
for alph in range(ord('a'), ord('z') + 1):
    if alph != ord('e') and alph != ord('q'):
        print(f"{chr(alph):s}", end="")
