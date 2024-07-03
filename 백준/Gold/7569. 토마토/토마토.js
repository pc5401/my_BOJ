class Queue {
    constructor() {
        this.items = [];
        this.frontIndex = 0;
        this.backIndex = 0;
    }

    enqueue(item) {
        this.items[this.backIndex] = item;
        this.backIndex++;
    }

    dequeue() {
        if (this.isEmpty()) return null;
        const item = this.items[this.frontIndex];
        this.frontIndex++;
        return item;
    }

    isEmpty() {
        return this.frontIndex === this.backIndex;
    }

    size() {
        return this.backIndex - this.frontIndex;
    }
}

const getTomato = (N, M, H, boxes) => {
    let queue = new Queue();
    for (let h = 0; h < H; h++) {
        for (let n = 0; n < N; n++) {
            for (let m = 0; m < M; m++) {
                if (boxes[h][n][m] === 1) {
                    queue.enqueue([h, n, m]);
                }
            }
        }
    }
    return queue;
}

const solve = (N, M, H, boxes) => {
    let queue = getTomato(N, M, H, boxes);
    const directions = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]];

    let days = -1;

    while (!queue.isEmpty()) {
        let size = queue.size();
        while (size > 0) {
            const [h, n, m] = queue.dequeue();
            for (const [dh, dn, dm] of directions) {
                const nh = h + dh, nn = n + dn, nm = m + dm;

                if (0 <= nh && nh < H && 0 <= nn && nn < N && 0 <= nm && nm < M) {
                    if (boxes[nh][nn][nm] === 0) {
                        boxes[nh][nn][nm] = 1;
                        queue.enqueue([nh, nn, nm]);
                    }
                }
            }
            size--;
        }
        days++;
    }

    for (let h = 0; h < H; h++) {
        for (let n = 0; n < N; n++) {
            for (let m = 0; m < M; m++) {
                if (boxes[h][n][m] === 0) {
                    return -1;
                }
            }
        }
    }

    return days;
}

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on('line', line => {
    input.push(line);
    if (Number(input[0].split(' ')[1]) * Number(input[0].split(' ')[2]) < input.length - 1) rl.close();
}).on('close', () => {
    const [M, N, H] = input[0].split(' ').map(Number);
    const boxes = [];
    for (let i = 1; i < input.length; i += N) {
        boxes.push(input.slice(i, i + N).map(e => e.split(' ').map(Number)));
    }
    console.log(solve(N, M, H, boxes));
});
