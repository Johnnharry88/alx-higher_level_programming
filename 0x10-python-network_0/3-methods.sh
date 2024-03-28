#!/bin/bash
# display all HTTP method ther server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
