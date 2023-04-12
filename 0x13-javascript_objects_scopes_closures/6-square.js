#!/usr/bin/node

// Write a class Square that defines a square and inherits from Square of 5-square.js:
// You must use the class notation for defining your class and extends
// Create an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X

const PreSquare = require('./5-square');

class Square extends PreSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const row1 = 'X'.repeat(this.width);
    if (c === undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(row1);
      }
    } else {
      const row2 = c.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(row2);
      }
    }
  }
}

module.exports = Square;
