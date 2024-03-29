#!/usr/bin/python3
"""Fetches https://alx-intranet.bbtn.io/status."""
import requests


if __name__ == "__main__":
    alx = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(alx.text)))
    print("\t- content: {}".format(alx.text))
