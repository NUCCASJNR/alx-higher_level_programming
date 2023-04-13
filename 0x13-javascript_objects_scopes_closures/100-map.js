#!/usr/bin/node
const list = require('./100-data.js').list;

const square = list.map((num, idx) => num * idx);
console.log(list);
console.log(square);
