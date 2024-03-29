#!/usr/bin/python3
"""Displays the X-request id Header ariable of a request to a given URL.
"""
import sys
import urllib.request


if __name__ == "__main__":
    alx = sys.argv[1]

    req = urllib.request.Request(alx)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
