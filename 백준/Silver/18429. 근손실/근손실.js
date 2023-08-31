function solve(input) {
  // TODO: 알고리즘 로직
    const [N, K] = input[0].split(' ').map(Number);
    const Arr = input[1].split(' ').map(Number);
    let res = 0;
    
    function dfs(visit, value, cnt){
        if (value < 0){
            return;
        }
    
        if (N===cnt){
            res++;
            return;
        }
    
        for (let i=0; i < N; i++){
            if (visit[i] === 0){
                visit[i] = cnt + 1;
                dfs(visit, value + Arr[i] - K, cnt+1);
                visit[i] = 0;
            }
        }
    }
    dfs(Array(N).fill(0), 0, 0);
    console.log(res);
}


// 제출하기전에 false 로
const isLocal = false;  // 여기서 true로 설정하면 로컬 환경으로 간주

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