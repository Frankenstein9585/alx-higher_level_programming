#!/bin/bash
# This script sends a GET request and prints the body of a response
curl -s -X POST -H "Content-Type: application/json" --data @"$2" "$1"
