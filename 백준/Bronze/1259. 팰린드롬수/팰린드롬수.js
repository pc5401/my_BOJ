// 알고리즘 로직을 처리하는 함수
function pal(num){
    let i = 0;
    for (let n = num.length - 1; n >= 0; n--){
        if (num[i] !== num[n]){
            return 'no'
        }
        i++
    }
    return 'yes'
}


function solve(input) {
  // TODO: 알고리즘 로직
    for (let i=0; i < input.length-1; i++){
        console.log(pal(input[i]))
    }
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