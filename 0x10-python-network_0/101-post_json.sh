#!/bin/bash
#json post
curl -sX POST -H "Content-Type: application/json" -d "$1" "$2"
