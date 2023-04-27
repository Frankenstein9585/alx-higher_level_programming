#!/bin/bash
url=$1
curl -s -w "%{size_download}\n" $url | tail -n 1
