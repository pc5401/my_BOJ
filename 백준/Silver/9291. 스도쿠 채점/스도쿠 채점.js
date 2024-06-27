function make_arr(x, y, table){
    let arr = [];
    for (let i=0; i < 3; i++){
        for (let j=0; j <3; j++){
            arr.push(table[x+i][y+j]);
        }
    }
    return arr
}


function check_arr(arr){
    let check = Array.from({length : 9}).fill(0);
    for(let a of arr){
        check[a-1] += 1;
    }

    for(let c of check){
        if (c !== 1) return false;
    }
    return true
}


function check_table(table){
    for (let i=0; i < 9; i++){
        if (check_arr(table[i]) === false) return false;
        else if (check_arr(Array.from({length : 9}, (e, j) => table[j][i])) === false) return false;
    }

    for (let i=0; i<9; i+=3){
        for (let j=0; j<9; j+=3){
            if (check_arr(make_arr(i, j, table)) === false) return false;
        }
    }
    return true
}


function solve(input) {
    // TODO: 알고리즘 로직
    let result = [];
    let case_number = 0;
    const T = parseInt(input[0]);
    for (let i=1; i < T*10; i += 10){
        let arr = [];
        case_number += 1;
        for(let j=i; j < i+9; j++){
            arr.push(input[j].split(' ').map(Number));
        }
        result.push(check_table(arr)? `Case ${case_number}: CORRECT` : `Case ${case_number}: INCORRECT`);
    }
    return result.join('\n');
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
        console.log(solve(lines));
    });
} else {
    // 백준 환경에서의 입력 처리
    const fs = require('fs');
    const lines = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    console.log(solve(lines));
}
