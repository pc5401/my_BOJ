function vs(our, other){
    if (our === 'S'){
        switch (other){
            case 'S': return 1;
            case 'P': return 2;
            case 'R': return 0;
        }
    } else if (our === 'P'){
        switch (other){
            case 'S': return 0;
            case 'P': return 1;
            case 'R': return 2;
        }
    } else{
        switch (other){
            case 'S': return 2;
            case 'P': return 0;
            case 'R': return 1;
        }
    }
}

function realVs(R, realDone, N, frendDone){
    let rtnValue = 0;
    for (let i=0; i<R; i++){
        for (let j=0; j<N; j++){
            rtnValue += vs(realDone[i], frendDone[j][i]);
        }
    }
    return rtnValue;
}

function VirtualVs(R, N, frendDone){
    let rtnValue = 0;
    for (let i=0; i<R; i++){
        let s = 0, p= 0, r =0;
        for (let j=0; j<N; j++){
            s += vs('S', frendDone[j][i]);
            p += vs('P', frendDone[j][i]);
            r += vs('R', frendDone[j][i]);
        }
        rtnValue += Math.max(s,p,r);
    }
    return rtnValue;
}


function solve(input) {
    // TODO: 알고리즘 로직
    // input 처리
    const R = Number(input[0]);
    const realDone = input[1].split('');
    const N = Number(input[2]);
    const frendDone = input.slice(3).map(e=>e.split(''))
    console.log(realVs(R, realDone, N, frendDone))
    console.log(VirtualVs(R, N, frendDone))
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