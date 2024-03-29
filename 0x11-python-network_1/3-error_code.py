#!/usr/bin/python3
"""Sends a request to a given URL and displays the body of response"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    alx = sys.argv[1]
    req = urllib.request.Request(alx)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except urllib.error.HTTPError as x:
        print("Error code: {}".format(x.code))
