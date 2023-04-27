#!/bin/bash
# This script makes a request to a URL and gets a response
curl -s -X PUT -d "user_id=98" -H "Referer: 0.0.0.0:5000/catch_me" -H "Origin: HolbertonSchool" -i 0.0.0.0:5000/catch_me
