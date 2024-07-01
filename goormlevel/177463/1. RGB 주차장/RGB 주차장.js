const solve = N => {
	let r = 1, g = 1, b = 1;
	
	for (let i = 1; i < N; i++){
		[r, g, b] = [(r*2) % 100000007, (g*2) % 100000007, (b*2) % 100000007];
	}
	
	return (r+g+b) % 100000007;
}


const readline = require('readline');

const rl = readline.createInterface({
	input : process.stdin,
	output : process.stdout
})

input = [];
rl.on('line', (line)=>{
	input.push(line);
	rl.close();
}).on('close', ()=>{
	const N = parseInt(input[0]);
	console.log(solve(N));
})