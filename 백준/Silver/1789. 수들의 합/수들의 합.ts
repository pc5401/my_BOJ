import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let S: number;

rl.on('line', (line: string) => {
  S = Number(line);
  rl.close();
});

rl.on('close', () => {
  console.log(solve(S))
  process.exit(0);
});

const solve = (s:number): number => {
  let sum = 0;
  let cnt = 0
  let i = 1;
  
  while (sum <= s){
    sum += i
    cnt++
    i++
  }

  return cnt-1
}