#!/usr/bin/python3
"""Sends a request to a given URL and displays the nody response
"""
import sys
import requests


if __name__ == "__main__":
    alx = sys.argv[1]
    alx_r = requests.get(alx)
    if alx_r.status_code >= 400:
        print("Error code: {}".format(alx_r.status_code))
    else:
        print(alx_r.text)
