const solve = (n) => {
	return n.length;
}



// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N;
	
	for await (const line of rl) {
		N = line;
		console.log(line.length)
		rl.close();
	}
	
	rl.on('close', ()=>{
		console.log(solve(N));
	})
	
	process.exit();
})();
