#!/usr/bin/python3
"""Sends a POST to a given URL with a given email"""
import sys
import requests


if __name__ == "__main__":
    alx = sys.argv[1]
    val = {"email": sys.argv[2]}

    alx_r = requests.post(alx, data=val)
    print(alx_r.text)
