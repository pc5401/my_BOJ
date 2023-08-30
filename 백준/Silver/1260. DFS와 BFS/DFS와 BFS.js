function dfs(n, visit, v, arr){
    for (let i=0; i < n; i++){
        if (arr[v-1][i] == 1 && !visit.includes(i+1)){
            visit.push(i+1)
            dfs(n, visit, i+1, arr)
        }
    }
    return visit
}

function bfs(n, m, start, arr){
    const visit = [start];
    const que = [start];

    while (que.length > 0){
        let v = que.shift()

        for (let i=0; i < n; i++){
            if (arr[v-1][i] == 1 && !visit.includes(i+1)){
                que.push(i+1)
                visit.push(i+1)
            }
        }
    }
    return visit
}

function solve(input) {
  // TODO: 알고리즘 로직
    const [N, M, V] = input[0].split(' ').map(Number);
    const Arr = []
    for(let i=0; i < N; i++){
        Arr.push(Array(N).fill(0));
    }
    input.slice(1).map(element => {
        const [x, y] = element.split(' ').map(Number);
        Arr[x-1][y-1] = 1;
        Arr[y-1][x-1] = 1;
    });
    console.log(...dfs(N, [V], V, Arr))
    console.log(...bfs(N, M, V, Arr))
}


// 제출하기전에 false 로
const isLocal = true;  // 여기서 true로 설정하면 로컬 환경으로 간주

if (isLocal) {
    // 로컬 환경 (VSCode)에서의 입력 처리
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    let lines = [];
    rl.on('line', (line) => {
        lines.push(line);
    }).on('close', () => {
        solve(lines);
    });
} else {
    // 백준 환경에서의 입력 처리
    const fs = require('fs');
    const lines = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    solve(lines);
}