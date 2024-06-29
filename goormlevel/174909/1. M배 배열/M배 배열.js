const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', (line) => {
    input.push(line);
    if (input.length === 2) {
        rl.close();
    }
});

rl.on('close', () => {
    const [N, M] = input[0].split(' ').map(Number);
    const A = input[1].split(' ').map(Number);

    console.log(solve(N, M, A));
});

const solve = (N, M, A) => {
    return A.map(e => e % M === 0 ? e : e * M).join(' ');
}
