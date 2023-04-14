#!/usr/bin/node

const myDict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};

const arr = Object.entries(myDict);
console.log(arr);

const mapped = arr.map(([key, value]) => ({key, value: value * 2,}));
// Multiply values * 2
console.log(mapped)

const filter = arr.filter(([key, value]) => value === 1);
console.log(filter);
