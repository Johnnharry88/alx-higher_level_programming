#!/bin/bash
# sends a JSON Post reques to a URL and displays response from server
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
