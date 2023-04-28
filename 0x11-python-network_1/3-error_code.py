#!/usr/bin/python3

"""
 a Python script that takes in a URL, sends a request to the
 URL and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import sys
#from urllib.error import HTTPError
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
