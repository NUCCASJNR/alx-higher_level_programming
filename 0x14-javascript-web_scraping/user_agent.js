#!/usr/bin/node

const http = require('http');

const server = http.createServer((req, res) => {
  const userAgent = req.headers['user-agent'];
  console.log(userAgent);

  // Rest of your code...
});

server.listen(3000);
