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
    const yss = Array(200_001 * 2).fill(0);
    const counts = Array(200_001 * 8).fill(0);
    const tree = Array(200_001 * 8).fill(0);

    const xs = [];
    const ys = new Set();
    const y_to_cnt = new Map();

    function U(s, e, l, r, tree_idx, val) {
        if (s > r || e < l) return;

        if (s >= l && e <= r) counts[tree_idx] += val;
        else {
            const mid = (s+e)>>1;
            U(s, mid, l, r, tree_idx<<1, val);
            U(mid+1, e, l, r, tree_idx<<1|1, val);
        }

        if (counts[tree_idx] > 0) tree[tree_idx] = yss[e+1] - yss[s];
        else {
            if (s === e) tree[tree_idx] = 0;
            else tree[tree_idx] = tree[tree_idx<<1] + tree[tree_idx<<1|1];
        }

        return;
    }

    function solve() {
        for (let i = 0; i < N; ++i) {
            const [x1, x2, y1, y2] = input[z++].split(" ").map(Number);
            
            xs.push([x1, y1, y2, 1])
            xs.push([x2, y1, y2, -1])
            ys.add(y1); ys.add(y2);
        }

        xs.sort((a, b) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            if (a[1] !== b[1]) return a[1] - b[1];
            if (a[2] !== b[2]) return a[2] - b[2];
            return a[3] - b[3];
        })

        let cnt = 0;
  
        let sorted_ys = [...ys].sort((a, b) => a - b);

        for (let y of sorted_ys) {
            ++cnt;
            y_to_cnt.set(y, cnt)
            yss[cnt] = y;
        }

        let ans = 0n;

        let [prev, y1, y2, _] = xs[0];
        U(1, cnt-1, y_to_cnt.get(y1), y_to_cnt.get(y2)-1, 1, 1)

        for (let idx = 1; idx < xs.length; ++idx) {
            const [x, y1, y2, flag] = xs[idx];

            ans += BigInt(x - prev) * BigInt(tree[1]);
            prev = x;
            U(1, cnt-1, y_to_cnt.get(y1), y_to_cnt.get(y2)-1, 1, flag)
        }

        console.log(ans.toString());

        return
    }


    function main() {

        solve();

        return;
    }


    main();

    return;
})