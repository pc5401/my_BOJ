const solve = (N, K, A) => {
	let cnt = 0;
	for (let a of A){
		if (!a.match(K)){
			cnt += 1
		}
	}
	return cnt;
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	let input = [];
	for await (const line of rl) {
		input.push(line);
	
		if (input.length >= 2){
			const [N, K] = [...input[0].split(' ')];
			const A = input[1].split(' ');
			console.log(solve(N, K, A));
			rl.close();
		}
	}
	
	process.exit();
})();
