const readline = require('readline');

const rl = readline.createInterface({
  input : process.stdin,
  output : process.output
})

let input = [];

rl.on('line', (line)=>{
  input.push(Number(line));
  if (input[0] < input.length) rl.close();
})

rl.on('close', ()=>{
  const N = input[0];
  const arr = input.slice(1);
  const result = solve(N, arr);
  console.log(result);
})


const solve = (n, arr) => {
  let rtn = 0;
  for (let i = 1; i<n; i++) arr[i] += arr[i-1]; // 누적합
  arr.unshift(0)
  let lo = 0;
  let hi = 1;
  let clockwise, counterclockwise;
  while (lo < hi){
    clockwise = arr[hi] - arr[lo];
    counterclockwise = (arr[n] - arr[hi]) + arr[lo];
    rtn = Math.max(rtn, Math.min(clockwise, counterclockwise));

    if (counterclockwise > clockwise) hi++;
    else lo++;

    if (hi >= n) break;
  }

  return rtn;
}
