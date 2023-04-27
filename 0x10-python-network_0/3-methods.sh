#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server
curl -X OPTIONS "$1"
