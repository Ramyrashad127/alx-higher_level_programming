#!/usr/bin/python3
""" import modules """
import requests


url = 'https://alx-intranet.hbtn.io/status'
req = requests.get(url)
print('Body response:')
print('\t- type: {}'.format(type(req.text)))
print('\t- content: {}'.format(req.text))
