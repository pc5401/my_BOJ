const solve = (N, M, cards) => {
	
	let cnt = 0;
	let check_list = Array.from({length : N},()=>1);
	let rtn = -1;

	cards.some((card, idx)=>{
		if (check_list[card - 1]){
			cnt += 1;
			check_list[card - 1] = 0;
		}
		if (cnt === N){
			rtn = idx+1;
			return true;
		}
	})
	return rtn;
}


// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		
		if (parseInt(input[0].split(' ')[1]) < input.length){
			const [N, M] = input[0].split(' ').map(Number);
			const cards = input.splice(1).map(Number);
			console.log(solve(N, M, cards));
			rl.close();
		}
	}
	
	process.exit();
})();
