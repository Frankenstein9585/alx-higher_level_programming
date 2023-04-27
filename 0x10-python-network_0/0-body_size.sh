#!/bin/bash
# This script prints the size of the body of a response
curl -s -w "%{size_download}\n" "$1" | tail -n 1
