#!/usr/bin/node
let myVar = parseInt(process.argv[2]);
if (!myVar) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
