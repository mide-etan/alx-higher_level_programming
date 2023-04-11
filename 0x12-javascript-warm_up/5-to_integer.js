#!/usr/bin/node

const [, , arg] = process.argv;

const number = parseInt(arg);

if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
