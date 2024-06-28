const check = (idx, N, M, S, E) => {
	if (idx + N > M) return false;
	
	for (let i=0; i < N; i++){
		if (S[i] !== E[idx+i]) return false;
	}
	return true;
}

const filtering = (N, M, S, E) => {
	let rtn = [];
	for (let i=0; i < M; i++){
		if (E[i] === S[0] && check(i, N, M, S, E)){
			i += (N-1);
			continue;
		}
		rtn.push(E[i])
	}

	return rtn.join('');
}

const solve = (N, M, S, E) => {
	let rtn = filtering(N, M, S, E)
	
	while (rtn.includes(S)){
		rtn = filtering(N, rtn.length, S, rtn)
	}
	
	return rtn !== '' ? rtn : 'EMPTY'
	
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let lst = [];
	
	for await (const line of rl) {
		lst.push(line);
		if (lst.length === 3){
			const [N, M] = [...lst[0].split(' ').map(Number)];
			let S = lst[1].trim();
			let E = lst[2].trim();
			console.log(solve(N, M, S, E));
			rl.close();
		}
	}
	
	process.exit();
})();
