#!/bin/bash
# This script sends a GET request and prints the body of a response
curl -s -X POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
