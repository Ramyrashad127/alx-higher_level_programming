#!/usr/bin/python3
""" import modules """
import requests


url = 'https://alx-intranet.hbtn.io/status'
req = requests.get(url)
print(req.content)
