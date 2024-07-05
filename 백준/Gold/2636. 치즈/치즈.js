const bfs = (N, M, arr) =>{
  let visited = Array.from({length:N},()=>Array(M).fill(false));
  let melted = [];
  let Q = [[0,0]];
  visited[0][0] = true;
  let ni = 0, nj = 0;
  while (Q.length > 0){
    const [x, y] = Q.shift();
    for (const [n, m] of [[0,1],[1,0],[-1,0],[0,-1]]){
      ni = x+n;
      nj = y+m;
      if (0<=ni && ni < N && 0<=nj && nj < M && !visited[ni][nj]){
        if (arr[ni][nj] === 1){
          melted.push([ni, nj]);
          visited[ni][nj] = true;
        } else if (arr[ni][nj] === 0){
          Q.push([ni, nj]);
          visited[ni][nj] = true;
        }
      }
    }
  }
  let rtn = melted.length;
  for (const [i, j] of melted){
    arr[i][j] = 0;
  }
  return rtn;
}


const solve = (N, M, arr) => {
  let cheeze = arr.reduce((x, y)=>{
    return x + y.reduce((a, b)=> a+b, 0);
  }, 0)
  let rtn = 0;
  let cnt = 0;
  while (cheeze > 0){
    rtn = bfs(N, M, arr);
    cheeze -= rtn;
    cnt += 1
  }
  console.log(cnt);
  console.log(rtn);
}

const readline = require('readline');

const rl = readline.createInterface({
  input : process.stdin,
  output : process.stdout
})

let input = [];
rl.on('line', (line)=>{
  input.push(line);

  if (parseInt(input[0].split(' ')[0]) < input.length){
    rl.close();
  }
}).on('close', ()=>{
  const [N, M] = input[0].split(' ').map(Number);
  const arr = input.slice(1).map(e=>e.split(' ').map(Number));
  solve(N, M, arr);
})
