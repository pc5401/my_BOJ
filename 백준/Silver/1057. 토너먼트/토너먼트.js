function solve(input) {
    // TODO: 알고리즘 로직
    let [N, kim, im] = input[0].split(' ').map(Number);
    let round = 0;


    while (kim !== im) {
        kim = Math.ceil(kim / 2);
        im = Math.ceil(im / 2);
        round++;
    }
    console.log(round);
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
