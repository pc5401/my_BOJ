const stepOfcopy = (idx, S, P) =>{
    let rtn = 0;
    let j = 0
    for(let i=0; i < S.length; i++){
        if (S[i] === P[idx]){
            j = 0;
            while (i+j < S.length && idx+j < P.length && S[i+j] === P[idx+j]){
                j++;
            }
            rtn = Math.max(rtn, j)
        }
    }
    return rtn;
}


const solve = (S, P) => {
    let rtn = 0;
    let i = 0
    while (i < P.length){
        i += stepOfcopy(i, S, P);
        rtn += 1
    }
    return rtn;
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', line => {
    input.push(line);
	if (input.length === 2) rl.close();
}).on('close', () => {
    const S = [...input[0]];
    const P = [...input[1]];
    console.log(solve(S, P))
});
