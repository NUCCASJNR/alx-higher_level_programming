#!/usr/bin/node

const request = require('request');
const user = process.argv[2];
const options = {
  url: `https://api.github.com/users/${user}`,
  headers: {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,     like Gecko) Chrome/113.0.0.0 Safari/537.36'
  }
};

request.get(options, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(body);
  }
});
