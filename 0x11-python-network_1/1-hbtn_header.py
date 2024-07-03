#!/usr/bin/python3
""" import modules """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        header = dict(response.headers)
        print(header['X-Request-Id'])
