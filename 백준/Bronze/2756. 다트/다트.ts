import * as readline from 'readline';

const score = (line: Array<number>) => {
  let p: number = 0;
  for(let i=0; i<6; i+=2){
    const [x, y] = [line[i], line[i+1]];
    const l = Math.sqrt(x**2 + y**2);

    if (l <= 3) p += 100;
    else if (l <= 6) p += 80;
    else if (l <= 9) p += 60;
    else if (l <= 12) p += 40;
    else if (l <= 15) p += 20;
    else p += 0;
  }
  
  return p;
}

const solve = (line: Array<number>)=>{
  // player 1
  let p1: number = score(line.slice(0,6));
  let p2: number = score(line.slice(6,12));

  if (p1 > p2){
    return `SCORE: ${p1} to ${p2}, PLAYER 1 WINS.`
  }else if (p1 < p2){
    return `SCORE: ${p1} to ${p2}, PLAYER 2 WINS.`
  }else {
    return `SCORE: ${p1} to ${p2}, TIE.`
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let lines: number[][] = [];
let numberOfInputs: number | null = null;

rl.on('line', (line: string) => {
  if (numberOfInputs === null) {
    // 첫 번째 입력값으로 입력의 개수를 설정합니다.
    numberOfInputs = parseInt(line, 10);
  } else {
    lines.push(line.split(' ').map(Number));
    
    // 입력의 개수만큼 입력을 받았다면, readline 인터페이스를 종료합니다.
    if (lines.length === numberOfInputs) {
      rl.close();
    }
  }
});

rl.on('close', () => {
  // 입력이 종료되었을 때의 로직을 여기에 작성합니다.
  const result: Array<String> = []
  for (const line of lines){
    result.push(solve(line));
  }
  for (const res of result){
    console.log(res);
  }
});
