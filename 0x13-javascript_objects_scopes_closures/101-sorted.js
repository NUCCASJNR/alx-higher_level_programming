#!/usr/bin/node

const dict = require('./101-data.js').dict;
const arr = Object.entries(dict)
const key = 1;
const new_dict = arr.filter(obj => obj.key === key);
const count = new_dict.length;
console.log(count);
