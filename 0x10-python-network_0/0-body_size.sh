#!/bin/bash
# sending a request to that URL, and displaying the size of the body of the response
curl -s "$1" | wc -c
