function goDown(n, h, table) {
    for (let start = 0; start < n; start++) {
        let i = 0;
        let j = start;
        while (i < h) {
            if (table[i][j] === 1) {
                j += 1;
            } else if (j > 0 && table[i][j - 1] === 1) {
                j -= 1;
            }
            i += 1;
        }
        if (j !== start) {
            return false;
        }
    }
    return true;
}

function dfs(n, h, table, count, x, y) {
    if (count > 3) {
        return -1;
    }

    if (goDown(n, h, table)) {
        return count;
    }

    let ans = -1;
    for (let i = x; i < h; i++, y = 0) {
        for (let j = y; j < n - 1; j++) {
            if (table[i][j] === 0 && (j === 0 || table[i][j - 1] !== 1) && table[i][j + 1] !== 1) {
                table[i][j] = 1;
                let temp = dfs(n, h, table, count + 1, i, j + 2);
                if (temp !== -1) {
                    if (ans === -1 || ans > temp) {
                        ans = temp;
                    }
                }
                table[i][j] = 0;
            }
        }
    }
    return ans;
}

function solve(input) {
    // TODO: 알고리즘 로직
    // 입력값 처리
    const [N, M, H] = input[0].split(' ').map(Number);
    const ladder = Array.from(Array(H), () => Array(N).fill(0));

    input.slice(1).forEach(element => {
        const [a, b] = element.split(' ').map(Number);
        ladder[a - 1][b - 1] = 1;
    });

    const result = dfs(N, H, ladder, 0, 0, 0);
    console.log(result);
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