const BFS = (i, j, N, K, M, visited) => {
		let rtn = 0;
		let Q = [[i, j]];
	
		visited[i][j] = true;

		while (Q.length !== 0){
			const [x, y] = Q.shift();
			rtn += 1;

			for (const [n, m] of [[0,1], [1,0],[-1, 0], [0, -1]]){
				const [ni, nj] = [x+n, y+m];
				if ( (0 <= ni && ni < N) && (0 <= nj && nj < N) && M[ni][nj] === K && !visited[ni][nj]){
					visited[ni][nj] = true;
					Q.push([ni, nj]);
				}
			}
		}

	return rtn;
}


const solve = (N, K, M) => {
	let visited = Array.from({length : N}, ()=> Array(N).fill(false));
	let rtn = 0;
	
	for (let i=0; i<N; i++){
		for (let j=0; j<N; j++){
			if (!visited[i][j] && M[i][j] === K){
				rtn = Math.max(rtn, BFS(i, j, N, K, M, visited))
			} else {
				visited[i][j] = true;
			}
		}
	}
	
	return rtn;
}

// Run by Node.js
const readline = require('readline');

let rl = readline.createInterface({
	input : process.stdin,
	output : process.stdout
})


let input = [];

rl.on('line', (line)=>{
	input.push(line);

	if (parseInt(input[0]) < input.length - 2){
		rl.close();
	}
}).on('close', ()=>{
	const N = parseInt(input[0]);
	const [x, y] = input[1].split(' ').map(Number);
	const M = input.slice(2).map(line=>line.split(' ').map(Number));
	const K = M[x-1][y-1];
	
	console.log(solve(N, K, M))
})