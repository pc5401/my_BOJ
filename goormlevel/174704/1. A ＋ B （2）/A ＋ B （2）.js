const solve = (a, b) =>{
	const A = parseFloat(a);
	const B = parseFloat(b);
	
	console.log((A+B).toFixed(6));
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		solve(...line.split(' '));
		rl.close();
	}
	
	process.exit();
})();
