#!/usr/bin/node

// Write a script that prints the number of movies where the character “Wedge Antilles” is present.

// The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
// You must use the module request

const req = require('request');
const url = process.argv[2];

req.get(`${url}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const log = JSON.parse(body);
    const a = log.films;

    const cleanedArray = a.map((url) => {
      const segments = url.split('/');
      return segments[segments.length - 2];
    });

    console.log(cleanedArray);
  }
});
