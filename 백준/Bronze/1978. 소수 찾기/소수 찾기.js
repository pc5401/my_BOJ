function solve(input) {
  // TODO: 알고리즘 로직
    const N = input[0].split().map(Number);
    const lst = input[1].split(' ').map(Number);
    const primes = Array(1001).fill(1);
    primes[0] = 0;
    primes[1] = 0;
    primes.forEach((e, i)=>{
        if (e){
            for (let j = i*2; j < primes.length; j += i){
                primes[j] = 0;
            }
        }
    })
    let res = 0;
    for (const v of lst){
        if (primes[v]) {res++}
    }
    console.log(res)
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