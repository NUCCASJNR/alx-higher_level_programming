#!/usr/bin/node

exports.converter = function (base) {
  return function (test) {
    return (test.toString(base));
  };
};
