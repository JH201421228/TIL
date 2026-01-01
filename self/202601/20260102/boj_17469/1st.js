const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


const input = [];
let z = 0;

rl.on(("line"), l => input.push(l));

rl.on(("close"), () => {
    const [N, Q] = input[z++].split(" ").map(Number);
    const parent = Array(N+1);
    const tree = Array(N+1);
    const sets = Array.from({length: N+1}, () => new Set());
    const questions = [];
    const ans = [];


    function find(idx) {
        let root = idx;

        while (root != tree[root]) root = tree[root];

        while (root != idx) {
            let cur = idx;
            idx = tree[idx];
            tree[cur] = root;
        }

        return root;
    }


    function union(idx) {
        let p = find(parent[idx])
        tree[idx] = p;

        if (sets[p].size < sets[idx].size) {
            const tmp = sets[p];
            sets[p] = sets[idx];
            sets[idx] = tmp;
        }

        for (const v of sets[idx]) sets[p].add(v);
        sets[idx].clear();

        return;
    }


    function solve() {
        parent[1] = 1;
        for (let idx = 0; idx < N-1; ++idx) parent[idx+2] = Number(input[z++]);

        for (let idx = 0; idx < N; ++idx) {
            sets[idx+1].add(Number(input[z++]));
        }

        for (let i = 0; i < N+Q-1; ++i) questions.push(input[z++].split(" ").map(Number));

        for (let idx = 0; idx < N+1; ++idx) tree[idx] = idx;

        for (let idx = N+Q-1; idx > 0; --idx) {
            const cur_question = questions[idx-1];

            if (cur_question[0] === 1) union(cur_question[1]);
            else ans.push(sets[find(cur_question[1])].size);
        }

        for (let idx = Q; idx > 0; --idx) console.log(ans[idx-1]);

        return;
    }


    function main() {
        solve();

        return;
    }


    main();

    return;
})
