const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});


const input = [];
let z = 0;


rl.on("line", l => input.push(l));

rl.on("close", () => {
    const [N, M] = input[z++].split(" ").map(Number);
    const parent = Array(N+1).fill(0);
    const state = Array(N+1).fill(0);
    const debt = Array(N+1).fill(0);
    const sets = Array.from({length: N+1}, () => new Set());


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

        if (sets[pa].size < sets[pb].size) {
            const tmp = pa;
            pa = pb; pb = tmp;
        }

        parent[pb] = pa;

        const cost = (debt[pa] / sets[pa].size) - (debt[pb] / sets[pb].size);

        debt[pa] = (debt[pa] / sets[pa].size) * (sets[pa].size + sets[pb].size);

        for (let v of sets[pb]) {
            sets[pa].add(v);
            state[v] += cost;
        }

        sets[pb].clear();

        return;
    }


    function solve() {
        for (let i = 0; i < M; ++i) {
            const [a, b, c] = input[z++].split(" ").map(Number);

            if (a === 1) union(b, c);
            else {
                debt[find(b)] += c;
                state[b] += c;
            }
        }

        const p = find(1);

        if (debt[p] !== 0) {
            const cost = debt[p] / N;
            for (let idx = 1; idx < N+1; ++idx) state[idx] -= cost;
        }

        let ans = "";
        let cnt = 0;

        for (let idx = 1; idx < N+1; ++idx) {
            if (idx === p || state[idx] === 0) continue;

            ++cnt;

            if (state[idx] > 0) ans += p + " " + idx + " " + state[idx] + "\n";
            else ans += p + " " + idx + " " + -state[idx] + "\n";
        }

        console.log(cnt);
        console.log(ans);
        
        return;
    }

    
    function main() {
        for (let idx = 0; idx < N+1; ++idx) {
            parent[idx] = idx;
            sets[idx].add(idx);
        }

        solve();

        return;
    }


    main();

    return;
})