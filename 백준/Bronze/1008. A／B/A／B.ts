import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (line: string) => {
  const [A, B] = line.split(' ').map(Number);
  console.log(A/B)
  rl.close()
});