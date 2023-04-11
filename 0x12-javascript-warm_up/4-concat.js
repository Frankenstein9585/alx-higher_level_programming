#!/usr/bin/node
const args = process.argv;
let sentence = '';
if (args[2] && args[3]) {
  sentence += args[2] + ' is ' + args[3];
} else if (args[2] && !args[3]) {
  sentence += args[2] + ' is undefined';
} else {
  sentence += 'undefined is undefined';
}
console.log(sentence);
