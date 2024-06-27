const solve = (N) => {
	let rtn = 1;
	for (let i=1; i <= N; i++){
		rtn = (rtn * i) % 1000000007;
	}
	return rtn;
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
