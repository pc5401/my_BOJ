const solve = (N, M, A) => {
	return A.map(e=>e % M === 0 ? e : e * M).join(' ');
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if (input.length === 2){
			const [N, M] = input[0].split(' ').map(Number);
			const A = input[1].split(' ').map(Number);
			console.log(solve(N, M, A));
			input.length = 0;
		}
	}
	rl.close();
})();
