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
    const arr = Array(N).fill(0);
    const S = [];
    let ans = 0;

    function solve() {
        for (let i = 0; i < N; ++i) arr[i] = Number(input[z++]);

        for (let idx = 0; idx < N; ++idx) {
            if (S.length > 0) {
                ++ans;
                let cur = arr[idx];
                let cur_cnt = 1;

                while (S.length > 0 && S[S.length-1][0] <= cur) {
                    let temp = S.pop();

                    if (S.length > 0) {
                        ans += temp[1];
                    }
                    else {
                        ans += temp[1]-1;
                    }

                    if (temp[0] == cur) {
                        cur_cnt += temp[1];
                        break
                    }
                }

                S.push([cur, cur_cnt]);
            }
            else {
                S.push([arr[idx], 1]);
            }
        }

        console.log(ans);

        return;
    }

    function main() {
        solve();

        return;
    }

    main();
})