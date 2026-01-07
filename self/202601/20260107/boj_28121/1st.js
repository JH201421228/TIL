const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const [N, Q] = input[z++].split(" ").map(Number);
    const parent = Array(N+1).fill(0);
    const odd = Array(N+1).fill(0);
    const is_ans = Array(N+1).fill(0);
    const sets = Array.from({length: N+1}, () => new Set());
    let ans = 0;
    let out = "";

    function find(idx) {
        let root = idx;

        while (root !== parent[root]) root = parent[root];

        while (root !== idx) {
            let p = parent[idx];
            parent[idx] = root;
            idx = p;
        }

        return root;
    }


    function union(a, b) {
        let pa = find(a);
        let pb = find(b);

        if (is_ans[pa] == 1 || is_ans[pb] == 1) {
            if (is_ans[pa] === 0) {
                ans += sets[pa].size;
                is_ans[pa] = 1;
            }
            if (is_ans[pb] === 0) {
                ans += sets[pb].size;
                is_ans[pb] = 1;
            }
        }

        if (sets[pa].size < sets[pb].size) {
            const temp = sets[pa];
            sets[pa] = sets[pb];
            sets[pb] = temp;
        }

        parent[pb] = pa;

        if (odd[a] === odd[b]) {
            for (let v of sets[pb]) {
                sets[pa].add(v);
                odd[v] = 1 - odd[v];
            }
            sets[pb].clear();
        }
        else {
            for (let v of sets[pb]) sets[pa].add(v);
            sets[pb].clear();
        }

        return ans;
    }


    function solve() {
        for (let idx = 0; idx < N+1; ++idx) {
            parent[idx] = idx;
            sets[idx].add(idx);
        }

        for (let i = 0; i < Q; ++i) {
            const [a, b] = input[z++].split(" ").map(Number);

            let pa = find(a);
            let pb = find(b);

            if (pa === pb && odd[a] === odd[b] && is_ans[pa] === 0) {
                is_ans[pa] = 1;
                ans += sets[pa].size;
            }

            if (pa !== pb) ans = union(a, b);

            out += ans.toString() + '\n';
        }

        console.log(out);

        return;
    }


    function main() {
        solve();

        return;
    }


    main();
});