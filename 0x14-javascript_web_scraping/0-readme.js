#!/usr/bin/node
const fs = require('fs');

function readAndPrintFileContent (filePath) {
  fs.readFile(filePath, 'utf-8', (error, content) => {
    if (error) {
      console.error('no such file or directory');
      console.error(error);
    } else {
      console.log(content);
    }
  });
}

const filePath = process.argv[2];
readAndPrintFileContent(filePath);
