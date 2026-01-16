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

    const parent = Array(N + 1).fill(0);

    // 🔴 BigInt 적용
    const state = Array(N + 1).fill(0n);
    const debt  = Array(N + 1).fill(0n);

    const sets = Array.from({ length: N + 1 }, () => new Set());

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
            pa = pb;
            pb = tmp;
        }

        parent[pb] = pa;

        const sizeA = BigInt(sets[pa].size);
        const sizeB = BigInt(sets[pb].size);

        const avgA = debt[pa] / sizeA;
        const avgB = debt[pb] / sizeB;
        const cost = avgA - avgB;

        debt[pa] = avgA * (sizeA + sizeB);

        for (let v of sets[pb]) {
            sets[pa].add(v);
            state[v] += cost;
        }

        sets[pb].clear();
    }

    function solve() {
        for (let i = 0; i < M; ++i) {
            const [a, b, c] = input[z++].split(" ");
            const C = BigInt(c);

            if (Number(a) === 1) {
                union(Number(b), Number(c));
            } else {
                const rb = find(Number(b));
                debt[rb] += C;
                state[Number(b)] += C;
            }
        }

        const p = find(1);

        if (debt[p] !== 0n) {
            const cost = debt[p] / BigInt(N);
            for (let i = 1; i <= N; ++i) {
                state[i] -= cost;
            }
        }

        let ans = "";
        let cnt = 0;

        for (let i = 1; i <= N; ++i) {
            if (i === p || state[i] === 0n) continue;

            cnt++;
            if (state[i] > 0n) {
                ans += `${p} ${i} ${state[i].toString()}\n`;
            } else {
                ans += `${i} ${p} ${(-state[i]).toString()}\n`;
            }
        }

        console.log(cnt);
        console.log(ans);
    }

    function main() {
        for (let i = 0; i <= N; ++i) {
            parent[i] = i;
            sets[i].add(i);
        }
        solve();
    }

    main();
});
