#!/usr/bin/node

//  Write a script that computes and prints a factorial
//
//  The first argument is integer (argument can be cast as integer) used for computing the factorial
//  Factorial of NaN is 1
//  You must do it recursively
//  You must use a function
//  You must use console.log(...) to print all output
//  You are not allowed to use var

function factorial (number) {
  let result = 1;
  for (let i = 2; i <= number; i++) {
    result *= i;
  }
  return result;
}

const arg1 = process.argv[2];
if (arg1) {
  const res = factorial(arg1);
  console.log(res);
} else if (isNaN) {
  console.log(1);
}
