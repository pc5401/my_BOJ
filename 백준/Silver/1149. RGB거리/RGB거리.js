function solve(input) {
    // TODO: 알고리즘 로직
    const N = Number(input[0]);
    const priceList = input.slice(1).map(line => line.split(' ').map(Number));
    let dp = Array.from({ length: N }, () => Array(3).fill(0));

    // 초기값 설정
    dp[0][0] = priceList[0][0];
    dp[0][1] = priceList[0][1];
    dp[0][2] = priceList[0][2];

    // DP 로직
    for (let i = 1; i < N; i++) {
        dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + priceList[i][0];
        dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + priceList[i][1];
        dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + priceList[i][2];
    }

    console.log(Math.min(dp[N-1][0], dp[N-1][1], dp[N-1][2]));
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