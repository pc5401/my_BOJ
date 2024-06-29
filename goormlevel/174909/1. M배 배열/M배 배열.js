const readline = require('readline');

const solve = (N, M, A) => {
    return A.map(e => e % M === 0 ? e : e * M).join(' ');
}

// Run by Node.js
(async () => {
    const rl = readline.createInterface({ input: process.stdin });
    const input = [];

    for await (const line of rl) {
        input.push(line);
        if (input.length === 2) {
            const [N, M] = input[0].split(' ').map(Number);
            const A = input[1].split(' ').map(Number);
            const result = solve(N, M, A);
            console.log(result);
            input.length = 0; // Clear the input array for the next case
        }
    }
    rl.close();
})();
