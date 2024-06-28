const solve = (N) => {
	return eval(N);
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		const [A, B] = [...line.split(' ')];
		console.log(Math.max(solve(A), solve(B)))
		rl.close();
	}
	
	process.exit();
})();
