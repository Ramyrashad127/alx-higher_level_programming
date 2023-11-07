#!/usr/bin/python3
"""module"""
import json


def save_to_json_file(my_obj, filename):
    """ new """
    with open(filename, "w", encoding="UTF-8") as fi:
        st = json.dumps(my_obj)
        fi.write(st)
