#!/usr/bin/node
const args = process.argv;
if (isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(args[2]); i++) {
    for (let j = 0; j < Number(args[2]); j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
