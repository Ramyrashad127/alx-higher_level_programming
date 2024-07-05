#!/usr/bin/python3
""" import modules"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    re = requests.get(url)
    if re.status_code >= 400:
        print('Error code: {}'.format(re.status_code))
    else:
        print(re.text)
