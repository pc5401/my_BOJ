function solve(input) {
    // TODO: 알고리즘 로직
    // 입력값 처리
    let cntWord = {};
    input.forEach(sentence => {
        const words = sentence.replace(/ /g,"");
        Array.from(words).forEach(word=>{
            cntWord[word] = (cntWord[word] ?? 0) + 1;
        })
    });

    let longWordList = [];
    let maxV = 0;
    for (const alpa of Object.keys(cntWord)){
        if (cntWord[alpa] > maxV){
            maxV = cntWord[alpa];
            longWordList = [alpa];
        }else if (cntWord[alpa] === maxV){
            longWordList.push(alpa)
        }
    }
    console.log(longWordList.sort().join(''))
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