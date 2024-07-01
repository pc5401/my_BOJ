const solve = (N, K, orders) => {
	let rtn = [];
	let stack = [];
	
	for(let i=0; i < N; i++){
		const order = orders[i];
		if (order[1] === 'u'){ // push
			const n = parseInt(order.split(' ')[1]);
			if (stack.length < K){
				stack.push(n);
			} else {
				rtn.push('Overflow');
			}
		} else { // pop
			if (stack.length === 0){
				rtn.push('Underflow');
			} else {
				rtn.push(stack.pop().toString());
			}
		}
	}
	
	return rtn;
}

// Run by Node.js
const readline = require('readline');

const rl = readline.createInterface({
	input : process.stdin, 
	output : process.stdout
})

let input = [];
rl.on('line', (line)=>{
	input.push(line);
	if (parseInt(input[0].split(' ')[0]) < input.length){
		rl.close();
	}
}).on('close', ()=>{
	const [N, K] = input[0].split(' ').map(Number);
	const orders = input.slice(1);
	const result = solve(N,K,orders);
	for (const res of result) console.log(res);
})