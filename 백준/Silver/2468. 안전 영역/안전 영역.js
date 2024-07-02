const bfs = (a, b, w, N, arr, visited) => {
  let Q = [[a, b]];

  while (Q.length > 0){
    const [i, j] = Q.shift();
    for (const [x, y] of [[0,1],[1,0],[0,-1],[-1,0]]){
      const [ni, nj] = [i+x, j+y];
      if ((0<=ni && ni<N) && (0<=nj && nj<N) && arr[ni][nj] >= w && !visited[ni][nj]){
        visited[ni][nj] = true;
        Q.push([ni, nj]);
      }
    }
  }
}


const island = (w, N, arr) => {
  let cnt = 0;
  let visited = Array.from({length:N}, ()=> Array(N).fill(false));
  for (let i=0; i < N; i++){
    for (let j=0; j < N; j++){
      if (!visited[i][j] && arr[i][j] >= w){
        visited[i][j] = true;
        bfs(i, j, w, N, arr, visited)
        cnt += 1
      }else if (!visited[i][j] && arr[i][j] < w){
        visited[i][j] = true;
      }
    }
  }
  return cnt;
}


const solve = (N, arr) => {
  const maxH = Math.max(...arr.map(e=>Math.max(...e)));
  let rtn = 1;
  for (let i = 1; i < maxH+1; i++){
    rtn = Math.max(rtn, island(i, N, arr));
  }

  return rtn
}

const readline = require('readline');

const rl = readline.createInterface({
  input : process.stdin,
  output : process.stdout
})

let input = [];
rl.on('line', (line)=>{
  input.push(line);

  if (parseInt(input[0]) < input.length){
    rl.close();
  }
}).on('close', ()=>{
  const N = parseInt(input[0]);
  const arr = input.slice(1).map(e=>e.split(' ').map(Number));
  console.log(solve(N, arr));
})
