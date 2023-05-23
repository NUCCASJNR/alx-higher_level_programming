#!/usr/bin/node

// Write a script that reads and prints the content of a file.

// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object

const file = require('fs');
const arg1 = process.argv[2];

file.readFile(`${arg1}`, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
