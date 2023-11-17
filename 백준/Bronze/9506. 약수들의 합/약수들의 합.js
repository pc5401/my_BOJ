function check(n){
    const nums = [];
    for(let i=1; i*2 <= n;i++){
        if (n%i) continue;
        nums.push(i)
    }
    const sumV = nums.reduce((a,b)=>a+b, 0)
    if (sumV === n){
        let word = `${n} = ${nums[0]}`
        nums.slice(1).forEach(e=>{
            word += ` + ${e}`
        })
        return word
    }else{
        return `${n} is NOT perfect.`
    }
}

function solve(input) {
    // TODO: 알고리즘 로직
    input.forEach(element => {
        const N = Number(element);
        if(N > 0){
            console.log(check(N))
        } 
    })
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
