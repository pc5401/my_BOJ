const solve = (R, C) => {
  let result = [];
  for (let i = 0; i < R; i++){
    let line = '';
    for (let j = 0; j < C; j++){
      line += '*';
    }
    result.push(line);
  }

  for (const res of result) console.log(res);
}

const readline = require('readline');

const rl = readline.createInterface({
  input : process.stdin,
  output : process.stdout
})

let input = [];
rl.on('line', (line)=>{
  input.push(line);

  if (input.length === 2){
    rl.close();
  }
}).on('close', ()=>{
  const R = Number(input[0]);
  const C = Number(input[1]);
  solve(R, C);
})
