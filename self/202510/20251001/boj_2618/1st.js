const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {
    let N, W;
    const dp = Array.from({length: 1_003}, () => Array(1_003).fill(-1));
    const dp_trace = Array.from({length: 1_003}, () => Array(1_003).fill(-1));
    const tasks = Array.from({length: 1_003}, () => Array(2).fill(0));


    function dist(i, j) {
        return Math.abs(tasks[i][0] - tasks[j][0]) + Math.abs(tasks[i][1] - tasks[j][1]);
    }


    function cal(n, m) {
        let x = Math.max(n, m) + 1;

        if (x === W+2) return 0;
        if (dp[n][m] !== -1) return dp[n][m];

        let first = cal(n, x) + dist(m, x);
        let second = cal(x, m) + dist(n, x);

        if (first > second) {
            dp[n][m] = second;
            dp_trace[n][m] = 1;
        }
        else {
            dp[n][m] = first;
            dp_trace[n][m] = 2;
        }

        return dp[n][m];
    }


    function solve(N, W) {
        tasks[0][0] = 1;
        tasks[0][1] = 1;
        tasks[1][0] = N;
        tasks[1][1] = N;

        for (let i = 0; i < W; ++i) {
            const [a, b] = input[z++].split(' ').map(Number);
            tasks[i+2][0] = a;
            tasks[i+2][1] = b;
        }

        console.log(cal(0, 1));

        let n = 0; m = 1;
        for (let i = 2; i < W+2; ++i) {
            console.log(dp_trace[n][m]);

            if (dp_trace[n][m] === 1) {
                n = i;
            }
            else {
                m = i;
            }
        }

        return;
    }


    function main() {
        N = Number(input[z++]);
        W = Number(input[z++]);

        solve(N, W);

        return;
    }


    main();
})
