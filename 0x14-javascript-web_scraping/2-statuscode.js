#!/usr/bin/node
const request = require('request');

function getStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error('Error occurred while making GET request:');
      console.error(error);
    } else {
      console.log('code:', response.statusCode);
    }
  });
}

const url = process.argv[2];
getStatusCode(url);
