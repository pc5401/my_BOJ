function solve(N, K, lst){
    let idx = 0;
    let cards = [];
    let card, player;

    lst.forEach((elements, i) => {
        for (let num of elements){
            cards.push([num, i+1]);
        }
    });

    while (cards.length > 0){
        let arr = cards.splice(idx, 1)[0];
        card = arr[0];
        player = arr[1];
        
        if (cards.length > 0) {
            idx = (card + idx - 1) % cards.length;
        }
    }
    
    return [player, card];
}

function main(){
    const readline = require("readline");
    let input = [];
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });
      
    rl.on("line", (line) => {
        input.push(line.split(' ').map(Number));
        if (input.length === parseInt(input[0][0]) + 1){
            rl.close();
        }
    });

    rl.on('close', () => {
        const [N, K] = input[0];
        const result = solve(N, K, input.slice(1));
        console.log(...result);
    });
}

main();
