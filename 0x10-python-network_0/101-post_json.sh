#!/bin/bash
# sending a JSON POST request to a URL, and displaying the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
