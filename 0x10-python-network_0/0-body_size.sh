#!/bin/bash
#sends request with curl and displays the size of body response by sever
curl -s "$1" | wc -c
