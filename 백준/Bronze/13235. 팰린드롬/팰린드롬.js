const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

rl.on('line', a => {
    const b = [...a].reduce((a,b)=>b+a, '');
    console.log(a===b)
    rl.close()
});
