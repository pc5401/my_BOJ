const solve = (N, K, orders) => {
	let queue = [];
	let rtn = [];
	
	for (const order of orders){
		if (order[1] === 'u'){
			if (queue.length < K){
				queue.push(order.split(' ')[1])
			} else{
				rtn.push('Overflow');
			}
		} else{ // pop
			if (queue.length === 0){
				rtn.push('Underflow');
			}else{
				rtn.push(queue.shift());
			}
		}
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
		if (input.length > parseInt(input[0].split(' ')[0])){
			const [N, K] = input[0].split(' ').map(Number);
			const orders = input.splice(1);
			const result = solve(N, K, orders);
			for (const res of result) console.log(res);
			rl.close();			
		}

	}
	
	process.exit();
})();
