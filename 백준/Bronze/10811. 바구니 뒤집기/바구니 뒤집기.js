function solve(input) {
    // TODO: 알고리즘 로직
    const [N, M] = input[0].split(' ').map(Number);
    const Arr = Array.from({length:N}, (e,i)=>i+1)
    const orderList = input.slice(1).map(element=>{
        return element.split(' ').map(Number);
    });
    orderList.forEach(element => {
        const [A, B] = element;
        const temp = Arr.slice(A-1, B).reverse();
        Arr.splice(A-1, B-A+1, ...temp)
    });
    console.log(...Arr)
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