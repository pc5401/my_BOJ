const solve = (N) => {
	let won = N;
	let rtn = 0;
	let cnt;
	for (let coin of [40, 20, 10, 5, 1]){
		cnt =  Math.floor(won / coin);
		rtn += cnt;
		won -= (cnt * coin);
	}
	return rtn;
}

// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		console.log(solve(parseInt(line)));
		rl.close();
	}
	
	process.exit();
})();
