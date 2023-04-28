#!/usr/bin/python3

"""
python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

url = "https://alx-intranet.hbtn.io/status"
r = requests.get(url)
print(f"Body response:")
print(f"\t- type: {type(r.content)}")
print(f"\t- content: {r.content.decode()}")
