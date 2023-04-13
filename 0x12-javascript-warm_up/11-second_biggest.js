#!/usr/bin/node

//  Write a script that searches the second biggest integer in the list of arguments.
//
//  You can assume all arguments can be converted to integer
//  If no argument passed, print 0
//  If the number of arguments is 1, print 0
//  You must use console.log(...) to print all output
//  You are not allowed to use var


const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
console.log(0);
} else {
const sort = args.map((ele)=>Number(ele)).sort((a, b)=>(b-a));
console.log(sort[1]);
}
