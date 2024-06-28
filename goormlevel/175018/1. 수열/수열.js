const solve = (n) => {
	let a = 0;
	let b = 1;
	
	for (let i=1; i < n; i++){
		[a, b] = [b, (a + b) % 1000000007];
	}
	return a;
}

// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		console.log(solve(Number(line)));
		rl.close();
	}
	
	process.exit();
})();
