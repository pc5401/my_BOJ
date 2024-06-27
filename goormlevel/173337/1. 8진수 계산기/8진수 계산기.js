const solve = (N, lst) => {
	let number = lst.reduce((a, b)=> a+b, 0);
	let rtn = [];
	while (number !== 0){
		rtn.unshift(number % 8);
		number = Math.floor(number / 8);
	}
	return rtn.join('');
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	for await (const line of rl) {
		input.push(line);
		if(input.length === 2){
			const N = parseInt(input[0]);
			const list = input[1].split(' ').map(Number);
			console.log(solve(N, list))
			rl.close();
		}
	}
	
	process.exit();
})();
