#!/usr/bin/node

const fetch = require('node-fetch');

fetch('https://api.github.com/users/NUCCASJNR')
  .then(response => response.json())
  .then(data => {
    const user = data.login;
    const follow = data.followers;
    const id = data.id;
    const node = data.node_id;
    const name = data.name;
    console.log(`username: ${user}`);
    console.log(`followers: ${follow}`);
    console.log(`id: ${id}`);
    console.log(`node: ${node}`);
    console.log(`name: ${name}`);
  })
  .catch(error => console.error(error));
