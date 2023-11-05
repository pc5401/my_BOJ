import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let N: number | null = null;
let A: number[] = [];;


rl.on('line', (line: string) => {
  if (N===null){
    N = parseInt(line, 10);
  }else{
    A = line.split(' ').map(Number);
    rl.close();
  }
});

rl.on('close', () => {
  const B = Array.from(A).sort((a,b)=> a - b)
  const P = Array.from(A,e=>{
    const idx = B.indexOf(e);
    B[idx] = -1;
    return idx
  })
  console.log(P.join(' '))
  process.exit(0);
});
