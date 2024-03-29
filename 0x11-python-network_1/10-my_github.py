#!/usr/bin/python3
"""Send the github API ot display a github ID baed on given credentials
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    key = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    alx_r = requests.get("https://api.github.com/user", auth=key)
    print(alx_r.json().get("id"))
