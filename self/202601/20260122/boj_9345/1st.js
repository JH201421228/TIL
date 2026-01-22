const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    let T, N, K, Q, A, B;
    const arr = Array(100_001);
    const min_tree = Array(400_005);
    const max_tree = Array(400_005);


    function I(s, e, tree_idx, flag, tree) {
        if (s === e) {
            tree[tree_idx] = arr[s];
            return arr[s];
        }

        const mid = (s+e)>>1;

        if (flag === 1) tree[tree_idx] = Math.max(I(s, mid, tree_idx<<1, flag, tree), I(mid+1, e, tree_idx<<1|1, flag, tree));
        else tree[tree_idx] = Math.min(I(s, mid, tree_idx<<1, flag, tree), I(mid+1, e, tree_idx<<1|1, flag, tree));

        return tree[tree_idx];
    }


    function U(s, e, idx, tree_idx, flag, tree) {
        if (idx > e || idx < s) return;

        if (s === e) {
            tree[tree_idx] = arr[idx];
            return;
        }

        const mid = (s+e)>>1;

        U(s, mid, idx, tree_idx<<1, flag, tree);
        U(mid+1, e, idx, tree_idx<<1|1, flag, tree);

        if (flag === 1) tree[tree_idx] = Math.max(tree[tree_idx<<1], tree[tree_idx<<1|1]);
        else tree[tree_idx] = Math.min(tree[tree_idx<<1], tree[tree_idx<<1|1]);

        return;
    }


    function S(s, e, l, r, tree_idx, flag, tree) {
        if (s >= l && e <= r) return tree[tree_idx];

        if (s > r || e < l) {
            if (flag === 1) return 0;
            else return Number.MAX_VALUE;
        }

        const mid = (s+e)>>1;

        if (flag === 1) return Math.max(S(s, mid, l, r, tree_idx<<1, flag, tree), S(mid+1, e, l, r, tree_idx<<1|1, flag, tree));
        else return Math.min(S(s, mid, l, r, tree_idx<<1, flag, tree), S(mid+1, e, l, r, tree_idx<<1|1, flag, tree));
    }


    function solve() {
        [N, K] = input[z++].split(' ').map(Number);

        for (let idx = 0; idx < N; ++idx) arr[idx] = idx;
        for (let idx = 0; idx < 4*N+1; ++idx) {
            max_tree[idx] = 0;
            min_tree[idx] = Number.MAX_VALUE;
        }

        I(0, N-1, 1, 1, max_tree);
        I(0, N-1, 1, 0, min_tree);

        for (let i = 0; i < K; ++i) {
            [Q, A, B] = input[z++].split(' ').map(Number);

            if (Q === 1) {
                if (A === S(0, N-1, A, B, 1, 0, min_tree) && B === S(0, N-1, A, B, 1, 1, max_tree)) console.log("YES");
                else console.log("NO");
            }
            else {
                const tmp = arr[A];
                arr[A] = arr[B];
                arr[B] = tmp;

                U(0, N-1, A, 1, 0, min_tree);
                U(0, N-1, B, 1, 0, min_tree);
                U(0, N-1, A, 1, 1, max_tree);
                U(0, N-1, B, 1, 1, max_tree);
            }
        }

        return;
    }


    function main() {
        T = Number(input[z++]);

        for (let i = 0; i < T; ++i) solve();

        return;
    }


    main();

    return;
})