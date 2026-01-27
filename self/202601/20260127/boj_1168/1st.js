const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const [N, K] = input[z++].split(" ").map(Number);
    const tree = Array(400_005);

    function I(s, e, tree_idx) {
        if (s === e) {
            tree[tree_idx] = 1;
            return 1;
        }

        const mid = (s+e)>>1;

        tree[tree_idx] = I(s, mid, tree_idx<<1) + I(mid+1, e, tree_idx<<1|1);

        return tree[tree_idx];
    }

    function U(s, e, tree_idx, target) {
        tree[tree_idx] -= 1;

        if (s === e) return s;

        const mid = (s+e)>>1;

        if (target <= tree[tree_idx<<1]) return U(s, mid, tree_idx<<1, target);
        else return U(mid+1, e, tree_idx<<1|1, target-tree[tree_idx<<1]);
    }

    function solve() {
        I(1, N, 1);

        let cur = K;
        const res = [];
        for (let t = 0; t < N; ++t) {
            res.push(U(1, N, 1, cur));

            if (t === N-1) break;
            cur = (cur+K-2) % (N-t-1) + 1;
        }

        console.log(`<${res.join(", ")}>`)

        return;
    }

    function main() {
        solve();

        return;
    }

    main();

    return;
})