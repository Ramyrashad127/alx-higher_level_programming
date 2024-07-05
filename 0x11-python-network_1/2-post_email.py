#!/usr/bin/python3
""" import modules """
import sys
import urllib.parse
import urllib.request


url = sys.argv[1]
email = sys.argv[2]
value = {'email' : email}
data = urllib.parse.urlencode(value).encode('ascii')
request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as re:
    print(re.read().decode("utf-8"))
