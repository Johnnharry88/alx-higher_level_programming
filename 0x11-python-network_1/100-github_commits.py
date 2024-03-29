#!/usr/bin/python3
"""Lists the 10 most recent commits on a given github repo"""
import sys
import requests


if __name__ == "__main__":
    alx = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    alx_r = requests.get(alx)
    commits = alx_r.json()
    try:
        for x in range(10):
            print("{}: {}".format(
                commits[x].get("sha"),
                commits[x].get("commit").get("author").get("name")))
    except IndexError:
        pass
