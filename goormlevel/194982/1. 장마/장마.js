const solve = (lst) => {
    const [N, M] = lst[0];
    let heights = lst[1];
    let rain = Array(N).fill(0);

    // 누적합을 사용하여 비 내린 횟수 기록
    lst.slice(2).forEach(([s, e], day) => {
        for (let i = s - 1; i < e; i++) {
            rain[i] += 1;
        }

        // 매 3일마다 배수 시스템 작동
        if ((day + 1) % 3 === 0) {
            for (let i = 0; i < N; i++) {
                if (rain[i] > 0) {
                    heights[i] += (rain[i] - 1);
                    rain[i] = 0;
                }
            }
        }
    });

    // 남은 비 내린 횟수를 최종 높이에 반영
    for (let i = 0; i < N; i++) {
        heights[i] += rain[i];
    }

    console.log(...heights);
}

// Run by Node.js
const readline = require('readline');

(async () => {
    let rl = readline.createInterface({ input: process.stdin });
    let input = [];
    for await (const line of rl) {
        input.push(line.split(' ').map(Number));
    }
    rl.close();
    solve(input);
    process.exit();
})();

