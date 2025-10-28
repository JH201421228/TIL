const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l))

rl.on("close", () => {
    const [N, L] = input[z++].split(' ').map(Number);
    const arr = input[z++].split(' ').map(Number);
    const D = Array(N).fill(0);

    const q = [];

    function solve() {
        for (let idx = 0; idx < N; ++idx) {
            if (q.length === 0) {
                q.push([arr[idx], idx]);
            }
            else {
                if (idx - q[0][1] >= L) {
                    q.shift();
                }

                const cur = arr[idx];

                while (q.length !== 0 && q[q.length-1][0] > cur) {
                    q.pop();
                }

                q.push([cur, idx]);
            }

            D[idx] = q[0][0];
        }

        console.log(...D);

        return;
    }

    function main() {
        solve();

        return;
    }

    main();
})