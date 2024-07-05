#!/usr/bin/python3
""" import modules """
import requests
import sys


url = sys.argv[1]
response = requests.get(url)
print(response.headers['X-Request-Id'])
