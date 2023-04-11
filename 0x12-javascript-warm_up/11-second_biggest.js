#!/usr/bin/node
const args = process.argv;
let max = 0;
const second_max = 0;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    if (args[i] > max) {
      max = args[i];
    }
  }
}
