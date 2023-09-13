function solve(input) {
    // TODO: 알고리즘 로직
    const [N, M] = input[0].split(' ').map(Number);
    const targets = input[1].split(' ').map(Number);
    let que = new Array(N);
    for (let i=1; i<=N; i++) que[i-1] = i;
    cnt = 0;
    while (targets.length > 0){
        let target = targets[0]
        if(que[0] === target){
            targets.shift();
            que.shift();
        }else{
            let idx = que.indexOf(target); // 위치
            // 2번연산
            if (idx <= que.length / 2){ // 앞에 있다.
                for (let i = 0; i < idx; i++){
                    let v = que.shift();
                    que.push(v);
                    cnt++
                }
            }else{ // 뒤어 있다. 3번 연산
                for (let i = 0; i < que.length - idx; i++){
                    let v  = que.pop();
                    que.unshift(v);
                    cnt++
                }   
            }
        }
    }
    console.log(cnt);
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