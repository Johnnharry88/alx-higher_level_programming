#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else if (parseInt(process.argv[2]) > 0) {
  for (let x = 1; x <= parseInt(process.argv[2]); x++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
