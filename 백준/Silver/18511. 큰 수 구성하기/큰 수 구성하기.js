const solve = (N, K, list) => {
    list.sort((a, b)=>a-b);
    let Q = [...list];
    let rtn = 0;

    while (true){
        const v = Q.shift();
        if (v <= N){
            rtn = v;
            for (const k of list){
                Q.push(v*10 + k)
            }
        } else{
            break;
        }
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
	if (input.length > 1) rl.close();
}).on('close', () => {
    const [N, K] = input[0].split(' ').map(Number);
    const list = input[1].split(' ').map(Number);
    console.log(solve(N, K, list));
});

