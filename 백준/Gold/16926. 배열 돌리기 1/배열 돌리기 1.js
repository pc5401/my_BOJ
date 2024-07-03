const turnArr = (N, M, arr) => {
    let rtn = Array.from({length: N}, () => Array(M).fill(0));
    const delta = [[1, 0], [0, 1], [-1, 0], [0, -1]];

    for (let k = 0; k < Math.min(N, M) / 2; k++) {
        let dir = 0;
        let i = k, j = k;
        let ni = i, nj = j;

        while (dir < 4) {
            ni = i + delta[dir][0];
            nj = j + delta[dir][1];

            if (k <= ni && ni < N - k && k <= nj && nj < M - k && rtn[ni][nj] === 0) {
                rtn[ni][nj] = arr[i][j];
                i = ni;
                j = nj;
            } else {
                dir += 1;
            }
        }
    }

    return rtn;
};

const solve = (N, M, R, arr) => {
    let rtn = arr;
    for (let i = 0; i < R; i++) {
        rtn = turnArr(N, M, rtn);
    }
    return rtn;
};

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', line => {
    input.push(line);
    if (input.length - 1 === Number(input[0].split(' ')[0])) rl.close();
}).on('close', () => {
    const [N, M, R] = input[0].split(' ').map(Number);
    const arr = input.slice(1).map(e => e.split(' ').map(Number));
    const result = solve(N, M, R, arr);
    result.forEach(row => console.log(...row));
});
