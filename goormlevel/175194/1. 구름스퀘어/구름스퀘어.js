const solve = (N, times) => {
	times.sort((a, b) => a[1] - b[1]);
	let rtn = 0;
	let now = 0;
	
	for (let time of times){
		if (now < time[0]){
			rtn += 1;
			now = time[1];
		}
	}
	
	return rtn;
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if (input.length === parseInt(input[0])+1){
			const N = parseInt(input[0]);
			const times = Array.from({length : N}, (e, i) => input[i+1].split(' ').map(Number));
			console.log(solve(N, times));
			rl.close();
		}
	}
	
	process.exit();
})();
