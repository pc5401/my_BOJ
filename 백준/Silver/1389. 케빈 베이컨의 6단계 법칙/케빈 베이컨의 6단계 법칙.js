function solve(input) {
    const [N, M] = input[0].split(' ').map(Number);
    const Arr = new Map();
    const visit = Array(N+1);
    let res = 0; 
    let minV = Infinity;

    input.slice(1).forEach(element => {
        const [x, y] = element.split(' ').map(Number);
        if (Arr.has(x)) Arr.get(x).push(y);
        else Arr.set(x, [y]);
        if (Arr.has(y)) Arr.get(y).push(x);
        else Arr.set(y, [x]);
    });

    const bfs = (n) => {
        for(let i = 0; i <= N; i++) visit[i] = 0;
        const Q = [n];
        let sum = 0;

        while (Q.length > 0) {
            const v = Q.shift();
            const neighbors = Arr.get(v);
            if (neighbors) {
                for (const node of neighbors) {
                    if (visit[node]) continue;
                    Q.push(node);
                    visit[node] = visit[v] + 1;
                    sum += visit[node];
                }
            }
        }
        return sum;
    }

    for (let i = 1; i <= N; i++) {
        const curV = bfs(i);
        if (minV > curV) {
            minV = curV;
            res = i;
        }
    }
    console.log(res);
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