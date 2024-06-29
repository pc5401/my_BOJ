const solve = (N) => {
	if (N < 3) return 1;
	let a = 1, b = 1, c = 1;
	let rtn = 0;
	
	for (let i = 3; i <= N; i++){
		rtn = (a + c) % 1000000007;
		[a, b, c] = [b, c, rtn]
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
