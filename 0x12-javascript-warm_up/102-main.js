#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
let nb = 0;
addMeMaybe(4, function (nb) {
	  console.log('New value: ' + nb);
});
