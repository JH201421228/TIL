const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = [];
let z = 0;

rl.on("line", l => input.push(l))

rl.on("close", () => {
    let N, M, G, V, F, S, O, C;

    function scc(n) {
        let p = ++O;
        V[n] = O;
        S.push(n);

        for (let x of G[n]) {
            if (V[x] == 0) p = Math.min(p, scc(x));
            else if (F[x] == 0) p = Math.min(p, V[x]);
        }

        if (p == V[n]) {
            ++C;

            while (S.length > 0) {
                const o = S.shift();
                F[o] = C;

                if (o == n) break;
            }
        }

        return p;
    }

    function solve() {
        [N, M] = input[z++].split(' ').map(Number);
        G = Array.from({length: N+1}, () => []);
        V = Array(N+1).fill(0);
        F = Array(N+1).fill(0);
        S = [];
        
        for (let i = 0; i < M; ++i) {
            const [u, v] = input[z++].split(' ').map(Number);
            G[u].push(v)
        }

        O = 0;
        C = 0;

        for (let n = 1; n < N+1; ++n) {
            if (V[n] == 0) scc(n);
        }

        const parent = {};
        const target_cycles = {}
        
        for (let idx = 1; idx < C+1; ++idx) parent[idx] = [];

        for (let n = 1; n < N+1; ++n) {
            for (let x of G[n]) {
                if (F[n] !== F[x]) parent[F[x]].push(F[n]);
            }
        }

        for (const [k, v] of Object.entries(parent)) {
            if (v.length === 0) target_cycles[k] = false;            
        }

        const Z = Number(input[z++]);
        for (let i = 0; i < Z; ++i) {
            let n = Number(input[z++]);
            if (F[n] in target_cycles) target_cycles[F[n]] = true;
        }

        for (const [k, v] of Object.entries(target_cycles)) {
            if (!v) {
                console.log(-1);

                return;
            }
        }

        console.log(Object.keys(target_cycles).length)

        return;
    }

    solve();
})