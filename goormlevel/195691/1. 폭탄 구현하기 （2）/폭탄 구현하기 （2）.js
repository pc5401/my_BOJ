const solve = (N, K, arr, bombs) => {
	let attacked = Array.from({length : N}, () => Array(N).fill(0));
	let ni = 0, nj = 0;
	for (const [i, j] of bombs){
		for (const [x, y] of [[0,0], [1,0], [0,1], [-1,0], [0,-1]]){
			ni = i+x-1;
			nj = j+y-1;
			
			if (0 <= ni && ni < N && 0 <= nj && nj < N){
				if (arr[ni][nj] === '@'){
					attacked[ni][nj] += 2;
				} else if (arr[ni][nj] === '0'){
					attacked[ni][nj] += 1
				}
			}
		}
	}

	let rtn = 0;
	for (let i=0; i<N; i++){
		for (let j=0; j<N; j++){
			rtn = Math.max(rtn, attacked[i][j])
		}
	}
	return rtn;
}

const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input = [];
rl.on('line', (line) => {
	input.push(line);
	if(input[0].split(' ').map(Number).reduce((a,b)=>a+b, 0) < input.length){
		rl.close();
	}
});

rl.on('close', () => {
	const [N, K] = input[0].split(' ').map(Number);
	const arr = input.slice(1, N+1).map(e=>e.split(' '));
	const bombs = input.slice(N+1).map(e=>e.split(' ').map(Number));
	console.log(solve(N, K, arr, bombs))
})