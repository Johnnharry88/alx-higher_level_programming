#!/usr/bin/python3
"""Fetches https://alx-intranet'hbtn.iostatus"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as res:
        show = res.read()
        print("Body response.")
        print("\t- type: {}".format(type(show)))
        print("\t- content: {}".format(show))
        print("\t- utf8 content: {}".format(show.decode("utf-8")))
