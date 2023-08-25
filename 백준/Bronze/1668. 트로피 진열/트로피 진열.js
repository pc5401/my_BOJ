function solve(input) {
  // TODO: 알고리즘 로직
    const N = Number(input[0]);
    const trophies = input.slice(1).map(Number);

    let leftCnt = 0, leftMax = 0;
    for (const height of trophies) {
        if (leftMax < height) {
            leftMax = height;
            leftCnt++;
        }
    }

    let rightCnt = 0, rightMax = 0;
    for (let i = N - 1; i >= 0; i--) {
        if (rightMax < trophies[i]) {
            rightMax = trophies[i];
            rightCnt++;
        }
    }

    console.log(leftCnt);
    console.log(rightCnt);
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