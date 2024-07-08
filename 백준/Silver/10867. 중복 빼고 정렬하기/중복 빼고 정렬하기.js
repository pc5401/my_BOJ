const solve = (N, arr) => {
  let lst = new Set();

  arr.forEach(element => {
    lst.add(element);
  });
  
  let rtn = [];
  lst.forEach(e=>rtn.push(e));

  return rtn.sort((a,b)=>a-b);
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
  const N = parseInt(input[0]);
  const arr = input[1].split(' ').map(Number);
  console.log(...solve(N, arr));
})
