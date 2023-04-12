#!/usr/bin/node
const args = process.argv.slice(2);
const max = Math.max(...args);
const min = Math.min(...args);
let second_max = 0;
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (args[i] > min && args[i] < max) {
      second_max = args[i];
    }
  }
  console.log(second_max);
}
