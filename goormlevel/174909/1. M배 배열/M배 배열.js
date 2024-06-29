// Run by Node.js
const readline = require('readline');
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N, M, numbers;
	
	for await (const line of rl) {
		if (!N) {
			[N, M] = line.split(' ').map(el => parseInt(el));
		}
		else {
			numbers = line.split(' ').map(el => parseInt(el));
			rl.close();
		}
	}
	
	const result = numbers.map(num => (num % M !== 0) ? num * M : num);
	console.log(result.join(' '));
})();