import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N: number | null = null;
let words: string = '';

rl.on('line', (line: string) => {
  if (N === null) {
    N = Number(line)
  }else{
    words = line;
    rl.close();
  }
});

rl.on('close', () => {
  console.log(solve(N, words))
  process.exit(0);
});

const solve = (target: any, words: string): number => {
  const n = words.length;
  const data: { [key: string]: number } = {};
  let ans: number = 0;
  let [lo, hi] = [0, 0];

  while (hi < n){
    if (Object.keys(data).length < target || data.hasOwnProperty(words[hi])){
      data[words[hi]] = hi;
      hi++;
      ans = Math.max(ans, hi - lo); 
    } else {
      if (data[words[lo]] === lo){
        delete data[words[lo]];
      }
      lo++;
    }
  }

  return ans;
}