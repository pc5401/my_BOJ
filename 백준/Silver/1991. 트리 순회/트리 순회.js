const preOrder = (node, tree) =>{
    if (node === null) return;
    const [left, right] = tree[node];
    process.stdout.write(node);
    preOrder(left, tree);
    preOrder(right, tree);
}

const inOrder = (node, tree) => {
    if (node === null) return; 
    const [left, right] = tree[node]
    inOrder(left, tree);
    process.stdout.write(node)
    inOrder(right, tree)
}

const postOrder = (node, tree) => {
    if (node === null) return;
    const [left, right] = tree[node]
    postOrder(left, tree);
    postOrder(right, tree);
    process.stdout.write(node)
}


function solve(tree, root='A') {
    // TODO: 알고리즘 로직
    preOrder(root, tree);
    console.log();
    inOrder(root, tree);
    console.log();
    postOrder(root, tree);
    console.log();
    return 
}

// 제출하기전에 false 로
const isLocal = true;  // 여기서 true로 설정하면 로컬 환경으로 간주

if (isLocal) {
    // 로컬 환경 (VSCode)에서의 입력 처리
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    let lines = [];
    rl.on('line', (line) => {
        lines.push(line);
    }).on('close', () => {
        const N = Number(lines[0]);
        const tree = {};
        for (let i=1; i <= N; i++){
            const [a, b, c] = lines[i].split(' ');
            tree[a] = [b !== '.'? b : null, c !== '.'? c : null]
        }
        solve(tree);
    });
} else {
    // 백준 환경에서의 입력 처리
    const fs = require('fs');
    const lines = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    solve(tree);
}
