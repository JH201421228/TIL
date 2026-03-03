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
    const arr = input[z++].split(" ").map(BigInt);

    const cnt = [0];
    const left = [-1];
    const right = [-1];


    function cal(idx, depth, need) {
        if (depth > 60) return depth - need + cnt[idx];

        if (cnt[idx] <= need) return depth;

        if (left[idx] === -1) return cal(right[idx], depth+1, need+1);
        else if (right[idx] === -1) return cal(left[idx], depth+1, need+1);
        else return Math.max(cal(left[idx], depth+1, Math.max(1, need+1-cnt[right[idx]])), cal(right[idx], depth+1, Math.max(1, need+1-cnt[left[idx]])));
    }


    function solve() {
        for (let i = 0; i < N; ++i) {
            let idx = 0;
            ++cnt[idx];
            const cur_n = arr[i];

            for (let j = 0; j < 61; ++j) {
                if ((cur_n & (1n<<BigInt(j))) !== 0n) {
                    if (right[idx] === -1) {
                       right[idx] = cnt.length;
                       cnt.push(0);
                       left.push(-1);
                       right.push(-1);
                    }
                    idx = right[idx];
                    ++cnt[idx];
                }
                else {
                    if (left[idx] === -1) {
                        left[idx] = cnt.length;
                        cnt.push(0);
                        left.push(-1);
                        right.push(-1);
                    }
                    idx = left[idx];
                    ++cnt[idx];
                }
            }
        }

        console.log(cal(0, 0, 0));

        return;
    }


    function main() {
        solve();

        return;
    }


    main();

    return;
})