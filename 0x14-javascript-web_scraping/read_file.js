#!/usr/bin/node

const fs = require('fs');
fs.readFile('test.txt', 'utf8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
