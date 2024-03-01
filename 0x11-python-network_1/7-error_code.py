#!/usr/bin/python3
"""Sending a request to a given URL for displaying the response body.

Usage: ./7-error_code.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
