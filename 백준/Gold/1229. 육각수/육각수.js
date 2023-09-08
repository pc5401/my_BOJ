function solve(input) {
  // TODO: 알고리즘 로직
    // 입력값 
    const N = Number(input[0]);
    const DP = Array(N+1).fill(Infinity);
    // 육각수 
  // 육각수
    const sixNum = [];
    for(let i=1; i*(2*i-1) <= N; i++){
        sixNum.push(i*(2*i-1));
    }
    
    // DP 테이블 초기화
    DP[0] = 0;
    for(let i=1; i<=N; i++){ // DP 순회 + 육각수 순회
        for(let num of sixNum) {
            if (i - num >= 0 && DP[i - num] + 1 < DP[i]) { // 양의 정수 그리고 현재값과 비교했을 때 작으면 갱싱 
            DP[i] = DP[i - num] + 1;
            }
        }
    }
    console.log(DP[N])
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