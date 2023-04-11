const [, , arg] = process.argv;

const times = parseInt(arg);

if (Number.isNaN(times)) {
  console.log('Missing number of occurrences');
  process.exit(1);
}

for (let i = 0; i < times; i++) {
  console.log('C is fun');
}
