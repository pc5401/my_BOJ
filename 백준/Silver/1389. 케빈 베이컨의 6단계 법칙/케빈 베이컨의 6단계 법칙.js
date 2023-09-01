function solve(input) {
  // TODO: 알고리즘 로직
    const [N, M] = input[0].split(' ').map(Number);
    // 테이블 생성
    const Arr = new Map();
    input.slice(1).forEach(element => {
        const [x, y] = element.split(' ').map(Number);
        
        if (Arr.has(x)) {
            Arr.get(x).push(y);
        } else {
            Arr.set(x, [y]);
        }

        if (Arr.has(y)) {
            Arr.get(y).push(x);
        } else {
            Arr.set(y, [x]);
        }
    });

    let res = 0; // 결과
    let minV = Infinity; // 최소값

    const bfs = (n) => {
        const Q = [n];
        const visit = Array(N+1).fill(0);

        while (Q.length > 0) {
            const v = Q.shift();
            for (const node of Arr.get(v) || []) {
                if (visit[node]) continue;
                Q.push(node);
                visit[node] = visit[v] + 1;
            }
        }

        return visit.reduce((a, b) => a + b, 0);
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