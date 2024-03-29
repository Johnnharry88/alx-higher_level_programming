#!/usr/bin/python3
"""Displays the X-Request-ID header variable of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    alx = sys.argv[1]

    alx_r = requests.get(alx)
    print(alx_r.headers.get("X-Request-Id"))
