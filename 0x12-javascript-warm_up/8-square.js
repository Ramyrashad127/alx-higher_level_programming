#!/usr/bin/node
if (!parseInt(process.argv[2])) {
  console.log('Missing size');
} else {
  let res = '';
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    res += 'X';
  }
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(res);
  }
}
