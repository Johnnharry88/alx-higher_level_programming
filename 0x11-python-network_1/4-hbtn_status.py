#!/usr/bin/python3
"""Fetches https://alx-intranet.bbtn.io/status."""
import requests


if __name__ == "__main__":
    alx = request.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(alx.test)))
    print("\t- content: {}".format(alx.test))
