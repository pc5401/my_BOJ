// 알고리즘 로직을 처리하는 함수
function make_pal(words){
    let keys = Object.keys(words).sort();
    let [left, mid, right] = ['', '', ''];
    for (let key of keys){
        if (words[key] % 2 === 0){
            for (let i = 0; i < words[key] / 2; i++){
                left = left + key
                right = key + right
            }
        }else{
            if (mid === ''){
                mid += key

                for (let i = 0; i < Math.floor(words[key] / 2); i++){
                    left = left + key
                    right = key + right
                }
            }else{
                return "I'm Sorry Hansoo"
            }
        }
    }
    return left + mid + right
}


function solve(input) {
  // TODO: 알고리즘 로직
    let words = input[0];
    let cnt = {};
    for (let word of words){
        if (cnt[word]){
            cnt[word] += 1;
        }
        else{
            cnt[word] = 1;
        }
    }
    console.log(make_pal(cnt));
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