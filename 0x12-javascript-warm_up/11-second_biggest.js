#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(1);
} else {
  const arr = process.argv.sort();
  console.log(arr[process.argv.length - 2]);
}
