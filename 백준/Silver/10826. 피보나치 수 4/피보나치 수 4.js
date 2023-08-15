const fs = require('fs');
const n = parseInt(fs.readFileSync("/dev/stdin").toString().trim(), 10);

const fibo = [];
fibo[0] = BigInt(0);
fibo[1] = BigInt(1);

for (let i = 2; i <= n; i++) {
    fibo[i] = fibo[i - 1] + fibo[i - 2];
}

console.log(fibo[n].toString());
