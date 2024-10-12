const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (input) => {
  const isPalindrome = input === input.split('').reverse().join('');
  console.log(isPalindrome ? "true" : "false");
  rl.close();
});