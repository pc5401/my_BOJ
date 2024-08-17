const readline = require('readline');

const rl = readline.createInterface({
  input : process.stdin,
  output : process.output
})

let input = [];

rl.on('line', (line)=>{
  input.push(line.split(' ').map(Number));
  if (input.length === 3) rl.close();
})

rl.on('close', ()=>{
  const N = input[0];
  const [T, P] = input[2];
  let t = 0;
  input[1].forEach(size=>{
    t += Math.ceil(size/T)
  })

  const sumV = input[1].reduce((cur, acc)=>cur+acc, 0);
  console.log(t);
  console.log(Math.floor(sumV/P), sumV%P)
})
