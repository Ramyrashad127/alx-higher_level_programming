#!/usr/bin/python3
""" module """
import json


def load_from_json_file(filename):
    """new"""
    with open(filename, "r", encoding="UTF-8") as fi:
        st = fi.read()
        return json.loads(st)
