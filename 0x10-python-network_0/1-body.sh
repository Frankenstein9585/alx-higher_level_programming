#!/bin/bash
# This script prints the  body of a response
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); if [ $response -eq 200 ]; then curl -s "$1"; fi
