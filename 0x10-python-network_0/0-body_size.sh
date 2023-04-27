#!/bin/bash
# This script prints the size of the body of a response
curl curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
