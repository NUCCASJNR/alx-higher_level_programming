#!/usr/bin/node

//  Write a script that searches the second biggest integer in the list of arguments.
//
//  You can assume all arguments can be converted to integer
//  If no argument passed, print 0
//  If the number of arguments is 1, print 0
//  You must use console.log(...) to print all output
//  You are not allowed to use var

function second (arg) {
  const max = Math.max(...arg);
  let min = Math.min(...arg);
  for (const i of arg) {
    if (i > min && i < max) {
      min = i;
    }
  }
  return min;
}
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  console.log(second(args));
}
