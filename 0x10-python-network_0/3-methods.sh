#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server
curl -sX OPTIONS -I "$1" | grep -i allow
