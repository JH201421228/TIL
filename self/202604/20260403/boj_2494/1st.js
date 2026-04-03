const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const N = Number(input[z++]);
    const cur = Array(N).fill(0);
    const tar = Array(N).fill(0);
    const dp = Array.from({length: N+1}, () => Array(10).fill(Number.MAX_VALUE))
    const trace = Array.from({length: N+1}, () => Array(10).fill(0))

    const ans = [];


    function solve() {
        for (let i = 0; i < 10; ++i) dp[0][i] = i;

        const tmp1 = input[z++];
        const tmp2 = input[z++];

        for (let i = 0; i < N; ++i) {
            cur[i] = Number(tmp1[i]);
            tar[i] = Number(tmp2[i]);
        }

        for (let i = 1; i < N+1; ++i) {
            for (let j = 0; j < 10; ++j) {
                for (let k = 0; k < 10; ++k) {
                    const l = (j-k+10) % 10;
                    const cur_n = (cur[i-1] + j) % 10;
                    const diff = (cur_n - tar[i-1] + 10) % 10;

                    if (dp[i-1][k] + diff + l < dp[i][j]) {
                        dp[i][j] = dp[i-1][k] + diff + l;
                        trace[i][j] = k;
                    }
                }
            }
        }

        let min_val = dp[N][0];
        let cur_idx = 0;

        for (let i = 1; i < 10; ++i) {
            if (dp[N][i] < min_val) {
                min_val = dp[N][i];
                cur_idx = i;
            }
        }

        console.log(min_val);

        ans.push(cur_idx);
        for (let idx = N; idx > 1; --idx) {
            cur_idx = trace[idx][cur_idx];
            ans.push(cur_idx);
        }

        let acc = 0;
        let idx = 0;
        while (ans.length > 0) {
            const a = ans.pop();
            const left = (a - acc + 10) % 10;
            const right = ((cur[idx] + a) % 10 - tar[idx] + 10) % 10;

            if (left > 0) console.log(`${idx+1} ${left}`);
            else console.log(`${idx+1} -${right}`);

            acc = a;
            ++idx;
        }

        return;
    }


    function main() {
        solve();

        return;
    }


    main();

    return;
})