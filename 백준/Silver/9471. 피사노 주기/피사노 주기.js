const period = (m) => {
    let [a, b] = [1, 1]
    for (let i=1; i < m**2; i++){
        [a, b] = [b, (a+b) % m];
        if (a === 1 && b === 1){
            return i;
        }
    }
}


function solve(input) {
    // TODO: 알고리즘 로직
    const result = [];
    input.slice(1).forEach(e=>{
        const [n, m] = e.split(' ').map(Number);
        result.push(period(m))
    })
    result.forEach((e,i)=>console.log(i+1,e))
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