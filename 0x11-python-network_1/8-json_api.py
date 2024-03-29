#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter
"""
import sys
import requests


if __name__ == "__main__":
    search = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": search}

    alx_r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = alx_r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name"0)))
    except ValueError:
        print("Not a vlaid JSON")
