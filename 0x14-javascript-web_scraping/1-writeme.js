#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, string) {
  fs.writeFile(filePath, string, 'utf-8', (error) => {
    if (error) {
      console.error('An error occurred');
      console.error(error);
    }
  });
}

const filePath = process.argv[2];
const string = process.argv[3];
writeToFile(filePath, string);
