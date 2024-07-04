const changeCheeze = (N, M, cheezes, visited) => {
    let rtn = 0;
    for (let i=0; i<N; i++){
        for (let j=0; j<M; j++){
            if (cheezes[i][j] === 1 && visited[i][j] > 1){
                cheezes[i][j] = 0;
                rtn += 1;
            }
        }
    }
    return rtn;
}

const solve = (N, M, cheezes) => {
    let rtn = 0;
    let cntOfCheeze = cheezes.reduce((x, y)=>{
        return x + y.reduce((ya,yb) => ya+yb, 0);
    }, 0);

    while(cntOfCheeze > 0){
        let visited = Array.from({length : N}, ()=>Array(M).fill(0));
        Q = [[0,0]];
        visited[0][0] = 1;

        while (Q.length > 0){
            const [i, j] = Q.shift();
            let ni = i, nj = j;
            for (const [x, y] of [[0,1],[1,0],[-1,0],[0,-1]]){
                ni = i + x;
                nj = j + y;
                if (0<=ni && ni<N && 0<=nj && nj<M){
                    if (cheezes[ni][nj] === 0 && visited[ni][nj] === 0){
                        Q.push([ni,nj]);
                        visited[ni][nj] = 1;
                    } else if (cheezes[ni][nj] === 1){
                        visited[ni][nj] += 1;
                    }
                }
            }
        }

        cntOfCheeze -= changeCheeze(N, M, cheezes, visited);
        rtn += 1
    }
    return rtn;
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', line => {
    input.push(line);
	if (input.length > parseInt(input[0].split(' ')[0])) rl.close();
}).on('close', () => {
    const [N, M] = input[0].split(' ').map(Number);
    const cheezes = input.slice(1).map(e=>e.split(' ').map(Number));
    console.log(solve(N, M, cheezes));
});

