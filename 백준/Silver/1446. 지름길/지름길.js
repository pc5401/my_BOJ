function solve(input) {
  // TODO: 알고리즘 로직
    const [N, D] = input[0].split(' ').map(Number);
    const shortcuts = input.slice(1).map(line => line.split(' ').map(Number));
    shortcuts.sort((a, b) => a[0] - b[0]);
    const road = new Array(D+1);
    for(let i = 0; i <= D; i++) {
    road[i] = i;
    }
    for(let i=0; i < N; i++){
        const [start, end, price] = shortcuts[i];
        if(end > D || (road[end] <= road[start] + price)) continue;
        road[end] = road[start] + price
        for(let j = end+1; j <= D; j++){
            if (road[j] <= road[j-1]+1) break;
            road[j] = road[j-1]+1
        }
    }
    console.log(road.at(-1))
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