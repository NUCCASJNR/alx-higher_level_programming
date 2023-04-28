#!/usr/bin/python3

import urllib.request
import urllib.parse

url = 'http://codewithalareef.tech'
values = { 'name' : 'Adegbite Al-Areef',
           'Age' : 16,
           'Lang' : 'python'
           }
data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
       the_page = response.read()
       print(the_page)
