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
    const V = Array(N+1).fill(0);
    const D = Array(N+1).fill(0);
    const A = Array.from({length: N+1}, () => Array(18).fill(0));
    const G = Array.from({length: N+1}, () => []);

    function dfs(cur, depth) {
        D[cur] = depth;

        for (nxt of G[cur]) {
            if (V[nxt] === 0) {
                V[nxt] = 1;
                A[nxt][0] = cur;

                dfs(nxt, depth+1);
            }
        }

        return;
    }

    function LCA(a, b) {
        if (D[a] < D[b]) {
            let tmp = a; a = b; b = tmp;
        }

        if (D[a] !== D[b]) {
            const diff = D[a] - D[b];

            for (let i = 0; i < 18; ++i) {
                if ((diff & (1<<i)) > 0) {
                    a = A[a][i];
                }
            }
        }

        if (a === b) return a;

        for (let i = 17; i >= 0; --i) {
            if (A[a][i] != A[b][i]) {
                a = A[a][i];
                b = A[b][i];
            }
        }

        return A[a][0];
    }
    
    function solve() {
        for (let i = 0; i < N-1; ++i) {
            const [u, v] = input[z++].split(" ").map(Number);
            G[u].push(v); G[v].push(u);

        }

        V[1] = 1;
        dfs(1, 0);

        for (let i = 1; i < 18; ++i) {
            for (let j = 1; j < N+1; ++j) {
                A[j][i] = A[A[j][i-1]][i-1];
            }
        }

        const M = Number(input[z++]);

        for (let i = 0; i < M; ++i) {
            const [u, v] = input[z++].split(" ").map(Number);
            console.log(LCA(u, v));
        }

        return;
    }

    function main() {
        solve();

        return;
    }


    main();

    return;
})