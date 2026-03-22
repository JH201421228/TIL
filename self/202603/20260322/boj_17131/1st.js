const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const MOD = 1_000_000_007;
    const N = Number(input[z++]);

    function S(s, e, l, r, tree_idx, tree) {
        if (s >= l && e <= r) return tree[tree_idx];

        if (l > e || r < s) return 0;

        const mid = (s+e)>>1;

        return (S(s, mid, l, r, tree_idx<<1, tree) + S(mid+1, e, l, r, tree_idx<<1|1, tree)) % MOD;
    }


    function U(s, e, idx, tree_idx, tree) {
        if (s === e && s === idx) {
            ++tree[tree_idx];
            return;
        }

        if (s > idx || e < idx) return;

        const mid = (s+e)>>1;

        U(s, mid, idx, tree_idx<<1, tree);
        U(mid+1, e, idx, tree_idx<<1|1, tree);

        tree[tree_idx] = tree[tree_idx<<1] + tree[tree_idx<<1|1]

        return;
    }


    function solve() {
        const coordinate = [];
        const xs = [];
        const x_dict = new Map();

        for (let i = 0; i < N; ++i) {
            const [x, y] = input[z++].split(" ").map(Number);
            coordinate.push([x, y]);
            xs.push(x);
        }

        xs.sort((a, b) => a-b);
        coordinate.sort((a, b) => a[1]-b[1]);

        let cur = 1;
        for (let x of xs) {
            if (!x_dict.has(x)) x_dict.set(x, cur++);
        }

        const M = x_dict.size;

        const tree = Array(4*M+1).fill(0);

        let ans = 0;

        while (coordinate.length > 0) {
            const [cur_x, cur_y] = coordinate.pop();

            const candidates = [cur_x];

            while (coordinate.length > 0 && coordinate[coordinate.length-1][1] === cur_y) {
                const [cur_x, cur_y] = coordinate.pop();
                candidates.push(cur_x);
            }
            
            for (let x of candidates) {
                ans += (S(1, M, 1, x_dict.get(x)-1, 1, tree) * S(1, M, x_dict.get(x)+1, M, 1, tree)) % MOD;
                ans %= MOD;
            }

            for (let x of candidates) U(1, M, x_dict.get(x), 1, tree);
        }

        console.log(ans);

        return;
    }


    function main() {
        solve();

        return;
    }


    main();

    return;
})