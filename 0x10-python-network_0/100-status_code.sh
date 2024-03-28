#!/bin/bash
# sends a request to url and displays only the status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
