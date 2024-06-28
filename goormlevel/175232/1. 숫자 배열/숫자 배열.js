const solve = (N) => {
	let arr = [];
	for(let i=1; i <= N; i++){
		let start = i * N - N + 1;
		arr.push(Array.from({length:N}, (e, j) => start+j));
	}
	let rtn = ""
	for (let a of arr){
		rtn += a.join(' ');
		rtn += "\n";
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
