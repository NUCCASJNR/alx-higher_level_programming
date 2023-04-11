#!/usr/bin/node

//  a script that prints My number: <first argument converted in integer>
//  if the first argument can be converted to an integer

const arg1 = process.argv[2];
//const new_arg = parseFloat(arg1)

if (!isNaN(arg1)) {
  console.log(ParseInt(arg1));
} else {
  console.log('Not a number');
}
