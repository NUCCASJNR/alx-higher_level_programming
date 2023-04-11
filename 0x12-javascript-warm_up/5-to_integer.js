#!/usr/bin/node

//  a script that prints My number: <first argument converted in integer>
//  if the first argument can be converted to an integer

const arg1 = parseInt(process.argv[2]);
if (arg1) {
  console.log(`My number: ${arg1}`);
} else {
  console.log('Not a number');
}
