#!/usr/bin/python3
"""import modules """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email' : email}
    re = requests.post(url,data=data)
    print('Your email is: {}'.format(re.text))
