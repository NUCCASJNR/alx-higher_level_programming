#!/usr/bin/node

// Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

// The first argument is the movie ID
// You must use the Star wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id
// You must use the module request

const req = require('request');
const movieId = process.argv[2];

req.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
