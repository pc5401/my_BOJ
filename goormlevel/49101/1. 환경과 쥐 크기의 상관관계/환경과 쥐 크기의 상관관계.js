const getValue = (N, arr) =>{
	arr.sort((a, b) => a-b);
	
	let rtn = 0;
	let maxV = 0;

	for (let x=0; x<N; x++){
		for (const X of [arr[x]-2, arr[x]-1, arr[x], arr[x]+1, arr[x]+2]){
			let lo = x, hi = x;
			while (lo >= 0 && arr[lo] >= (X - 2)) lo--;
			while (hi < N && arr[hi] <= (X + 2)) hi++;
			
			if (maxV < (hi - lo + 1)){
				maxV = (hi - lo + 1);
				rtn = X;
			}
		}

	}
	return rtn;
}

const solve = (N, A, B) => {
	const a = getValue(N, A);
	const b = getValue(N, B);
	
	console.log(a, b);
	console.log(a>b ? 'good':'bad')
}

const readline = require('readline');

rl = readline.createInterface({
	input : process.stdin
})

input = [];
rl.on('line',(line)=>{
	input.push(line);
	if (input.length === 3) rl.close();
}).on('close',()=>{
	const N = parseInt(input[0]);
	const A = input[1].split(' ').map(Number);
	const B = input[2].split(' ').map(Number);
	solve(N, A, B)
})
