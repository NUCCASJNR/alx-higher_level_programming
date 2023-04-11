#!/usr/bin/node

// Write a function that increments and calls a function.
//
// The function must be visible from outside
// Prototype: function (number, theFunction)
// You are not allowed to use varWrite a function that increments and calls a function.
//
// The function must be visible from outside
// Prototype: function (number, theFunction)
// You are not allowed to use var

exports.addMeMaybe = function (number, theFunction) {
  let result = 0;
  return function() {
    result++;
    if (result <= number) {
      theFunction();
    }
  }
}

