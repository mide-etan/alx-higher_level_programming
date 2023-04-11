const [, , arg1, arg2] = process.argv;

const firstArg = arg1 || 'undefined';
const secondArg = arg2 || 'undefined';

console.log(`${firstArg} is ${secondArg}`);
