#!/usr/bin/python3

"""
This scripts updates a github username
"""

import requests
import json
import sys

username = sys.argv[1]
token = sys.argv[2]

url = f"https://api.github.com/users/{username}"
Auth = {"Authorization": f"token {token}"}

data = {'bio': 'codewithalareef'}
re = requests.patch(url, headers=Auth)
if re.status_code == 200:
    print(f"User updated successfully!")
else:
    print(f"Error updating user: {re.text}")
