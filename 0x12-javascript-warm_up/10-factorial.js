#!/usr/bin/node
function fact (x) {
  if (x === 1) {
    return (1);
  }
  return (x * fact(x-1));
}
if (process.argv.length === 2) {
  console.log(1);
} else {
  console.log(fact(parseInt(process.argv[2])));
}
