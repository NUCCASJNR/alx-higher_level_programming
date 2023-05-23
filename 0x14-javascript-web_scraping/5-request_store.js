#!/usr/bin/node

// Write a script that gets the contents of a webpage and stores it in a file.

// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module request

const req = require('request');
const url = process.argv[2];
const save = process.argv[3];
const file = require('fs');

req.get(`${url}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    file.writeFile(`${save}`, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
