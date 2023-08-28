function solve(input) {
  // TODO: 알고리즘 로직
    const N = Number(input[0]);
    const lst = input.slice(1).map(e=>e.split(' ').map(Number));
    let res = 1;
    let maxV = 0
    for(let std=1; std <= N; std++){
        const frd = Array(N).fill(0);
        for(let i=0; i < N; i++){ // 학생 번호
            for(let j=0; j<5; j++){ // 학년
                if (i === std-1) continue;
                if (lst[i][j] === lst[std-1][j]){
                    frd[i] = 1;
                }
            }
        }
        const sumV = frd.reduce(function add(sum,  val){
            return sum + val;
        }, 0);
        if (sumV > maxV){
            res = std;
            maxV = sumV;
        }
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