#!/bin/bash
# sending a request to a URL, and displaying only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
