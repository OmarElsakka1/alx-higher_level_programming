#!/bin/bash
# sending a POST request to the passed URL, and displaying the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
