#!/usr/bin/python3
'''Module'''
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


argv.pop(0)

try:
    oldItms = load_from_json_file('add_item.json')
except FileNotFoundError:
    oldItms = []

for itm in argv:
    oldItms.append(itm)
save_to_json_file(oldItms, 'add_item.json')
