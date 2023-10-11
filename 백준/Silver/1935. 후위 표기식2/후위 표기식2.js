function solve(input) {
    // TODO: 알고리즘 로직
    const N = Number(input[0]);
    const sic = input[1].split('');
    const ascii = Object.fromEntries(
        [...Array(N)].map((_, i) => [String.fromCharCode(65 + i), Number(input[i + 2])])
    );
    const stack = [];
    sic.forEach(element => {
        if (element in ascii){
            stack.push(ascii[element]);
        }else{
            let b = stack.pop();
            let a = stack.pop();
            if(element === '+'){
                stack.push(a+b);
            }else if(element === '-'){
                stack.push(a-b);
            }else if(element === '*'){
                stack.push(a*b);
            }else if(element === '/'){
                stack.push(a/b);
            }
        }
    });
    const result = stack.pop();
    console.log(result.toFixed(2));
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