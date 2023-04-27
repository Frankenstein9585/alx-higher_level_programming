#!/bin/bash
# This script prints all the HTTP Request a server will accept
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d " " -f2,3,4,5,6,7
