// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		const [N, M] = line.split(' ').map(Number);
		const result = ((0.07 * N) / (N + M)*100).toString()
		const [x,y] = result.split('.');
		console.log(`${x}.${y.slice(0,2)}`);
		rl.close();
	}
	
	process.exit();
})();
