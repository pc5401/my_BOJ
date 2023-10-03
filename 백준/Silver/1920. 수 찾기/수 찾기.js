function search(target, n, Arr){
    let lo, hi, mid;
    lo = 0
    hi = n-1;
    while (lo < hi){
        mid = ~~((lo+hi)/2)
        if (Arr[mid] < target){
            lo = mid + 1
        }else{
            hi = mid
        }
    }

    if (Arr[lo] === target){
        return 1
    } else {
        return 0
    }
}


function solve(input) {
    // TODO: 알고리즘 로직
    const N = Number(input[0]);
    const A = input[1].split(' ').map(Number).sort((a,b) => a - b);
    const M = Number(input[2]);
    const lst = input[3].split(' ').map(Number);

    let result = '';
    lst.forEach(e => {
        result += search(e, N, A) + '\n';
    });
    console.log(result)
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