#!/usr/bin/node
const request = require('request');
const fs = require('fs');

function savePageToFile (url, filePath) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error occurred while making GET request:');
      console.error(error);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (error) => {
        if (error) {
          console.error('Error occurred while writing to the file:');
          console.error(error);
        }
      });
    }
  });
}

const url = process.argv[2];
const filePath = process.argv[3];
savePageToFile(url, filePath);
