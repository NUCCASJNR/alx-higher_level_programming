#!/bin/bash
#HTTP status code
curl -s -w "%{http_code}" "$1"
