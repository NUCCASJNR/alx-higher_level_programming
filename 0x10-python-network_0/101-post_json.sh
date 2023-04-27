#!/bin/bash
#json post
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
