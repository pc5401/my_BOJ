function bisectLeft(array, x) {
    let lo = 0, hi = array.length;
    
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        
        if (array[mid] < x) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    
    return lo;
}

function bisectRight(array, x) {
    let lo = 0, hi = array.length;
    
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        
        if (array[mid] <= x) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    
    return lo;
}


function solve(input) {
    // TODO: 알고리즘 로직
    const N = Number(input[0]);
    const myCards = input[1].split(' ').map(Number).sort((a,b)=>a-b);
    const M = Number(input[2]);
    const cards = input[3].split(' ').map(Number);
    const countCards = Array(M).fill(0);
    for (let i=0; i < M; i++){
        const left = bisectLeft(myCards, cards[i])
        const right = bisectRight(myCards, cards[i])
        countCards[i] = (right - left)
    }
    console.log(...countCards)
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