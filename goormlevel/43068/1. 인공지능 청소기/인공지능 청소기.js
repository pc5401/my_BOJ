const solve = (X, Y, N) => {
	let cnt = N - Math.abs(X) - Math.abs(Y);
	if (cnt < 0) return 'NO';
	if (cnt % 2 === 0) return 'YES' ;
	return 'NO'
}

// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

let input = [];
rl.on("line", function(line) {
	input.push(line);
	if (parseInt(input[0]) < input.length){
		const T = parseInt(input[0]);
		const result = input.slice(1).map(e=>{
			const [X, Y, N] = e.split(' ').map(Number);
			return solve(X, Y, N);
		})
		// 출력
		for (const res of result) console.log(res);
		rl.close();
	}
}).on("close", function() {
	process.exit();
});