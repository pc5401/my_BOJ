const searchXy = (N, M) => {
	for (let i=0; i<N; i++){
		for (let j=0; j<N; j++){
			if (M[i][j] === 0) return [i, j]
		}
	}	
}

const solve = (N, M) => {
	const [x, y] = [...searchXy(N, M)]
	let rtn = 0;
	for (let i=0; i<N; i++){
		rtn += M[i][y];
		rtn += M[x][i];
	}
	return rtn;
}



// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	for await (const line of rl) {
		input.push(line);
		if (parseInt(input[0]) < input.length){
			const N = parseInt(input[0]);
			const M = Array.from({length : N}, (e, i) => input[i+1].split(' ').map(Number));
			console.log(solve(N, M))
			rl.close()
		}
	}
	
	process.exit();
})();
