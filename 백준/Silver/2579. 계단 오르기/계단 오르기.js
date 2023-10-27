function res(N, table){
    if (N < 2) return table.reduce((acc, cur)=>acc+cur,0);
    const dp = Array.from({length:N}, ()=>[0,0]);
    [dp[0][0], dp[0][1], dp[1][0], dp[1][1]] = [table[0], table[0], table[0]+table[1], table[1]];

    for (let i=2; i<N; i++){
        v = table[i];
        dp[i][0] = v + dp[i-1][1];
        dp[i][1] = v + Math.max(dp[i-2][0], dp[i-2][1]);
    }
    // console.log(dp)
    return Math.max(...dp[N-1]);
}

function solve(input) {
    // TODO: 알고리즘 로직
    const N = Number(input[0]);
    const table = Array.from({length:N}, (e,i)=> Number(input[i+1]));
    console.log(res(N, table));
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