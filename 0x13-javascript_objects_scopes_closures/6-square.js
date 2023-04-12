#!/usr/bin/node
const OldSquare = require('./5-square');
class Square extends OldSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Square;
