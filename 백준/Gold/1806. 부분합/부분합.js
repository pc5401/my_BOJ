function makeTable(n, arr){
    const rtn = Array.from({length:(n+1)}, ()=>0);
    for (let i=1; i<(n+1); i++){
        rtn[i] = rtn[i-1] + arr[i-1];
    }
    return rtn;
}

function result(s, table){
    const n = table.length;
    let [lo, hi] = [0, 1];
    let rtn = 10000000;
    while (hi < n){
        const val = table[hi] - table[lo];
        if (val < s){
            hi++
        }else{
            if (hi-lo < rtn) rtn = hi-lo;
            lo++
        }
    }
    return rtn === 10000000 ? 0 : rtn;
}

function solve(input) {
    // TODO: 알고리즘 로직
    const [N, S] = input[0].split(' ').map(Number);
    const arr = input[1].split(' ').map(Number);
    const table = makeTable(N, arr);

    console.log(result(S, table));
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
