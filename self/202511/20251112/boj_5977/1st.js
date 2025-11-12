const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const [N, K] = input[z++].split(' ').map(Number);
    const E = Array(N+1).fill(0);
    const dp = Array(N+1).fill(0);
    const sums = Array(N+1).fill(0);
    const q = [];

    function temp(idx) {
        return dp[idx-1] - sums[idx];
    }

    function solve() {
        for (let idx = 1; idx < N+1; ++idx) sums[idx] = sums[idx-1] + E[idx];

        for (let idx = 1; idx < N+1; ++idx) {
            while (q.length > 0 && q[0] < idx-K) q.shift();

            while (q.length > 0 && temp(q[q.length-1]) <= temp(idx)) q.pop();

            q.push(idx);

            dp[idx] = sums[idx] + temp(q[0]);

            if (idx <= K) dp[idx] = Math.max(dp[idx], sums[idx]);
        }

        console.log(dp[N]);

        return;
    }

    function main() {
        for (let idx = 1; idx < N+1; ++idx) E[idx] = Number(input[z++]);

        solve();

        return;
    }

    main();
})