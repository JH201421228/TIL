const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const [N, D] = input[z++].split(' ').map(Number);
    const K = input[z++].split(' ').map(Number);

    const q = [];
    let ans = 0;

    for (let idx = 0; idx < N; ++idx) {
        let cur;
        
        if (q.length === 0) cur = K[idx];
        else cur = q[0][0] + K[idx];

        ans = Math.max(cur, ans);

        while (q.length > 0 && idx - q[0][1] >= D) q.shift();

        while (q.length > 0 && q[q.length - 1][0] <= cur) q.pop();

        q.push([cur, idx]);
    }

    if (ans > 0) console.log(ans);
    else console.log(Math.max(...K));
});