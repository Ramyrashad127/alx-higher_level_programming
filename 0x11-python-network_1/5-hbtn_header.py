#!/usr/bin/python3
""" import modules """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
