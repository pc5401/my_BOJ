function makeBlocck(n){
    const table = Array.from({length:n}, ()=>0);
    table[1] = 1;
    table[2] = 3;

    for (let i=3; i<n; i++){
        table[i] = (table[i-1] + table[i-2]*2) % 10007
    }

    return table;
}


function solve(input) {
    // TODO: 알고리즘 로직
    const N = Number(input[0]);
    const dp = makeBlocck(1001);
    // console.log(dp)
    console.log(dp[N])
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