const solve = (N, S) =>{
	let rtn = "";
	for(let i=0; i<N; i++){
		let word = S[i];
		if (word === word.toUpperCase()){
			rtn += word.toLowerCase();
		} else {
			rtn += word.toUpperCase();
		}
	}
	return rtn;
}


const main = (input) =>{
	const N = Number(input[0]);
	const S = input[1].trim()
	
	console.log(solve(N, S))
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line)
		if (input.length >= 2){
			main(input);
			rl.close();
		}
	}
	
	process.exit();
})();
