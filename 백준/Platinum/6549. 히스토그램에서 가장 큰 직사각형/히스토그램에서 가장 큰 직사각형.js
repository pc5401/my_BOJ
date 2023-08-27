function histogram(n, lst){
    let rtn = 0;
    const stack = [];

    lst.forEach((h, i) => {
        while (stack.length !== 0 && stack[stack.length-1][1] > h ){
            let [idx, height] = stack.pop();
            let width = stack.length !== 0 ? i - stack[stack.length-1][0] - 1 : i;
            rtn = Math.max(rtn, width * height);
        }
        stack.push([i, h]);
    });

    while (stack.length !== 0){
        let [idx, height] = stack.pop();
        let width = stack.length !== 0 ? n - stack[stack.length-1][0] - 1 : n;
        rtn = Math.max(rtn, width * height);
    }
    return rtn;
}

function solve(input) {
  // TODO: 알고리즘 로직
    for(let i=0; i < input.length -1; i++){
        const Arr = input[i].split(' ').map(Number);
        console.log(histogram(Arr[0], Arr.slice(1)));
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