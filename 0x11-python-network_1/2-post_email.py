#!/usr/bin/python3
""" import modules """
import sys
import urllib.parse
import urllib.request


url = sys.argv[1]
value = {"email": sys.argv[2]}
data = urllib.parse.urlencode(value).encode("utf-8")
request = urllib.request.Request(url, data=data)
with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
