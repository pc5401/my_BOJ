const readline = require('readline');

const rl = readline.createInterface({
  input : process.stdin,
  output : process.output
})

let n;

rl.on('line', (line)=>{
  const n = BigInt(line.trim());
  solve(n);
  rl.close();
})


const solve = (n) => {
  result = [];
  for (let i = 2; i <= 10; i++){
    const a = n.toString(i)
    const b = [...a].reverse().join('');
    if (a === b) result.push(`${i} ${a}`)
  }

  if (result.length !==0){
    result.forEach(e=>console.log(e))
  }else{
    console.log('NIE')
  }
}
