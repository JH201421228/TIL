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
    const D = Array(N+1).fill(0);
    const V = Array(N+1).fill(0);
    const A = Array.from({length: N+1}, () => Array.from({length: 18}, () => Array(3).fill(0)));
    const G = Array.from({length: N+1}, () => []);


    function LCA(a, b) {
        if (D[a] < D[b]) {
            const tmp = a;
            a = b; b = tmp;
        }

        let min_res = Number.MAX_VALUE;
        let max_res = Number.MIN_VALUE;

        if (D[a] !== D[b]) {
            const diff = D[a] - D[b];
            for (let i = 0; i < 18; ++i) {
                if ((diff & (1<<i)) > 0) {
                    max_res = Math.max(max_res, A[a][i][1]);
                    min_res = Math.min(min_res, A[a][i][2]);
                    a = A[a][i][0];
                }
            }
        }

        if (a === b) {
            if (min_res === Number.MAX_VALUE) min_res = 0;
            if (max_res === Number.MIN_VALUE) max_res = 0;

            return [min_res, max_res];
        }

        for (let i = 17; i >= 0; --i) {
            if (A[a][i][0] !== A[b][i][0]) {
                max_res = Math.max(max_res, Math.max(A[a][i][1], A[b][i][1]));
                min_res = Math.min(min_res, Math.min(A[a][i][2], A[b][i][2]));

                a = A[a][i][0];
                b = A[b][i][0];
            }
        }

        max_res = Math.max(max_res, Math.max(A[a][0][1], A[b][0][1]));
        min_res = Math.min(min_res, Math.min(A[a][0][2], A[b][0][2]));

        if (min_res === Number.MAX_VALUE) min_res = 0;
        if (max_res === Number.MIN_VALUE) max_res = 0;

        return [min_res, max_res];
    }


    function dfs(cur, depth) {
        D[cur] = depth;

        for (let x of G[cur]) {
            const nxt = x[0];
            const cost = x[1];

            if (V[nxt] !== 1) {
                V[nxt] = 1;
                A[nxt][0][0] = cur;
                A[nxt][0][1] = cost;
                A[nxt][0][2] = cost;

                dfs(nxt, depth+1);
            }
        }

        return;
    }


    function solve() {
        for (let idx = 0; idx < N+1; ++idx) {
            for (let jdx = 0; jdx < 18; ++jdx) {
                A[idx][jdx][1] = Number.MIN_VALUE;
                A[idx][jdx][2] = Number.MAX_VALUE;
            }
        }

        for (let i = 0; i < N-1; ++i) {
            const [u, v, c] = input[z++].split(" ").map(Number);
            G[u].push([v, c]);
            G[v].push([u, c]);
        }

        V[1] = 1;
        dfs(1, 0);

        for (let i = 1; i < 18; ++i) {
            for (let j = 1; j < N+1; ++j) {
                A[j][i][0] = A[A[j][i-1][0]][i-1][0];
                A[j][i][1] = Math.max(A[A[j][i-1][0]][i-1][1], A[j][i-1][1]);
                A[j][i][2] = Math.min(A[A[j][i-1][0]][i-1][2], A[j][i-1][2]);
            }
        }

        const K = Number(input[z++]);

        for (let i = 0; i < K; ++i) {
            const [u, v] = input[z++].split(" ").map(Number);

            const res = LCA(u, v);

            console.log(res[0], res[1]);
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