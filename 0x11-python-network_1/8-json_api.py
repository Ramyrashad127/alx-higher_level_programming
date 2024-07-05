#!/usr/bin/python3
"""import modules"""
import requests
import sys


if __name__ == "__main__":
    if(len(sys.argv) == 1):
        data = {'q': ""}
    else:
        data = {'q': argv[2]}
    url = 'http://0.0.0.0:5000/search_user'
    re = requests.post(url, data=data)
    try:
        response = re.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
