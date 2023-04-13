#!/usr/bin/node
const args = process.argv.slice(2);
let max = args[0];
let secondMax = args[1];
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (args[i] > max) {
      secondMax = max;
      max = args[i];
    } else if (args[i] > secondMax && args[i] < max) {
      secondMax = args[i];
    }
  }
  console.log(secondMax);
}
