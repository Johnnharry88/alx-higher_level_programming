#!/usr/bin/python3
"""Sends a POST request to a given URL using a given email"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    alx = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(alx, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
