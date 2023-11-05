import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let T: number | null = null;
let lines: string[][] = [];
let result: string[] = [];

rl.on('line', (line: string) => {
  if (T === null){
    T = Number(line);
  }else if (T === (lines.length+1)){
    lines.push(line.split(' '))
    rl.close()
  }else{
    lines.push(line.split(' '))
  }
});

rl.on('close', () => {
  lines.forEach(lst=>{
    let n: number = Number(lst[0]);
    lst.splice(1).forEach(e=>{
      switch (e){
        case '@':
          n *= 3;
          break;
        case '%':
          n += 5;
          break;
        case '#':
          n -= 7;
          break
      }
    })
    result.push(n.toFixed(2));
  })
  result.forEach(e=>console.log(e))
  process.exit(0);
});
