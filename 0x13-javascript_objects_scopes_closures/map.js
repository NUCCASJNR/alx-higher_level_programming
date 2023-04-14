#!/usr/bin/node

const numbers = [3, 4, 5, 6, 7, 8, 9, 10];
console.log(numbers)
const sn = numbers.map((num) => num * num);
console.log(sn);

const re = numbers.map((num, index) => num * index);
console.log(re)
