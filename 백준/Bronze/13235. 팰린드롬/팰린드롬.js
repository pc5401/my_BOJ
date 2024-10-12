const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (input) => {
  const len = input.length;
  let isPalindrome = true;
  
  for (let i = 0; i < Math.floor(len / 2); i++) {
    if (input[i] !== input[len - 1 - i]) {
      isPalindrome = false;
      break;
    }
  }
  
  console.log(isPalindrome ? "true" : "false");
  rl.close();
});