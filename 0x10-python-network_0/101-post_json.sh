#!/bin/bash
#json post
curl -s -H "Content-Type: application/json" -d "$2" "$1"
