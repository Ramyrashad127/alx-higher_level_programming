#!/usr/bin/python3
"""module """
import sys
save = __import__('5-save_to_json_file.py').save_to_json_file
load = __import__('6-load_from_json_file.py').load_from_json_file


arg = list(sys.argv[1:])
try:
    st = load('add_item.json')
except Exception:
    st = []

st.extend(arg)
save(st, 'add_item.json')
