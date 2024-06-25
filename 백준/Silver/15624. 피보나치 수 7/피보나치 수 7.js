function solve(input) {
    // TODO: 알고리즘 로직
    const N = parseInt(input[0]);
    if (N === 0){
        return 0;
    }else if (N < 3){
        return 1;
    }
    
    const dp = Array.from({length : (N+1)}, () => 0)
    dp[1] = 1;
    dp[2] = 1;
    for (let i = 3; i < N+1; i++){
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007;
    }

    return dp[N]
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
        console.log(solve(lines));
    });
} else {
    // 백준 환경에서의 입력 처리
    const fs = require('fs');
    const lines = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    console.log(solve(lines));
}
