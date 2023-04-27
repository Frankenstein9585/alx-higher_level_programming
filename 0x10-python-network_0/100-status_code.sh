#!/bin/bash
# This script sends a GET request and prints the body of a response
curl -s -o /dev/null -w "%{http_code}" "$1"
