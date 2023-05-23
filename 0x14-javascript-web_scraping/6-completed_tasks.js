#!/usr/bin/node

// Write a script that computes the number of tasks completed by user id.

// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
// You must use the module request

const req = require('request');
const url = process.argv[2];
req.get(`${url}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const arg = JSON.parse(body);
    const result = {};
    for (let i = 0; i < arg.length; i++) {
      const search = arg[i];
      if (search.completed === true) {
        result[search.userId] = search.id;
      }
    }
    console.log(result);
  }
});
