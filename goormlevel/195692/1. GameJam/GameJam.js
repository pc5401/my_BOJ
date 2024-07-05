const solve = (N, player, orders) => {
	let x = player[0] - 1, y = player[1] -1;
	let visited = Array.from({length : N}, ()=>Array(N).fill(0));
	visited[x][y] = 1;
	const dir = {'L': [0, -1], 'R': [0, 1],'D': [1, 0],'U': [-1, 0]}
	let ni = x, nj = y;
	while (true){
		const cnt = orders[x][y].slice(0, -1);
		const cmd = orders[x][y].slice(-1)

		for (let i=0; i < parseInt(cnt); i++){
			ni = x + dir[cmd][0];
			nj = y + dir[cmd][1];
			if (ni < 0){ // 왼쪽 초과
				ni = N - 1;
			}else if(N <= ni){
				ni = 0;
			}else if(nj < 0){
				nj = N - 1;
			}else if (N <= nj){
				nj = 0;
			}
			if (visited[ni][nj] === 1){
				return visited.reduce((a, b)=>a + b.reduce((aa, bb)=>aa + bb, 0) ,0);
			}else{
				visited[ni][nj] = 1;
				x = ni;
				y = nj;
			}
		}
	}
}

const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input = [];
rl.on('line', (line) => {
	input.push(line);
	if (parseInt(input[0]) <= input.length - 3) rl.close();
});

rl.on('close', () => {
	const N = input[0];
	const goorm = input[1].split(' ').map(Number);
	const player = input[2].split(' ').map(Number);
	const orders = input.slice(3).map(e=>e.split(' '));
	const p = solve(N, player, orders);
	const g = solve(N, goorm, orders);
	if (p > g){
		console.log(`player ${p}`)
	} else{
		console.log(`goorm ${g}`)
	}
	
})