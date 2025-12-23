const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const [N, M, Q] = input[z++].split(" ").map(Number);
    const arr = [0, ...input[z++].split(" ").map(Number)];
    const V = Array(N+1).fill(0);
    const tree = Array(4*N+1).fill(0);
    const L = input[z++].split(" ").map(Number);
    const R = input[z++].split(" ").map(Number);


    function I(s, e, tree_idx) {
        if (s === e) {
            if (V[s] === 1) tree[tree_idx] = arr[s];
            else tree[tree_idx] = -Infinity;

            return tree[tree_idx];
        }

        const mid = (s+e) >> 1;

        return tree[tree_idx] = Math.max(I(s, mid, tree_idx*2), I(mid+1, e, tree_idx*2+1));
    }
    

    function U(s, e, idx, tree_idx, val) {
        if (s > idx || e < idx) return tree[tree_idx];

        if (s === e) {
            tree[tree_idx] = val;
            return val;
        }

        const mid = (s+e) >> 1;

        return tree[tree_idx] = Math.max(U(s, mid, idx, tree_idx*2, val), U(mid+1, e, idx, tree_idx*2+1, val));
    }


    function solve() {
        L.sort((a, b) => a-b);
        R.sort((a, b) => a-b);

        let cur_idx = 0;
        for (let idx = 0; idx < M; ++idx) {
            if (L[idx] > R[idx]) {
                for (let i = 0; i < Q; ++i) console.log(1_000_000_000);

                return;
            }

            const l = Math.max(cur_idx, L[idx])
            const r = Math.max(cur_idx, R[idx])

            for (let i = l; i < r+1; ++i) V[i] = 1;

            cur_idx = r;
        }

        I(1, N, 1);

        for (let i = 0; i < Q; ++i) {
            const [x, y] = input[z++].split(" ").map(Number);

            if (V[x] === 1) U(1, N, x, 1, arr[y]);
            else U(1, N, x, 1, -Infinity);

            if (V[y] === 1) U(1, N, y, 1, arr[x]);
            else U(1, N, y, 1, -Infinity);

            [arr[x], arr[y]] = [arr[y], arr[x]];

            console.log(tree[1]);
        }

        return;
    }

    function main() {
        solve();

        return;
    }

    main();
})