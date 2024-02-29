#!/bin/bash
# when you run this script with a URL as an argument, it will fetch the content
#  from that URL and display the size of the response body in bytes.
curl -s "$1" | wc -c
