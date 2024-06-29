const solve = (N, S) => {
	let rtn = Math.max(...S);
	
	let stack = S[0];
	for (let i=1; i < N; i++){
		if (S[i] === S[i-1] + 1){
			stack += S[i];
		} else {
			rtn = Math.max(rtn, stack);
			stack = S[i];
		}
	}
	rtn = Math.max(rtn, stack);
	
	return rtn;
}


// Run by Node.js
const readline = require('readline');

let rl = readline.createInterface(
	{ 
		input: process.stdin,
		output: process.stdout
	}
);

let input = [];

rl.on('line', (line) =>{
	input.push(line);

}).on('close', ()=>{

	const N = parseInt(input[0]);
	const S = input[1].split(' ').map(Number);
	
	const result = solve(N, S);
	console.log(result)
});

