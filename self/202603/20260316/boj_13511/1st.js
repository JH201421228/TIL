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
    const A = Array.from({length: N+1}, () => Array.from({length: 18}, () => Array(2).fill(0)));
    const G = Array.from({length: N+1}, () => []);


    function dfs(cur, depth) {
        D[cur] = depth;

        for (let nxt of G[cur]) {
            const [x, c] = nxt;
            
            if (V[x] === 0) {
                V[x] = 1;
                A[x][0][0] = cur;
                A[x][0][1] = c;

                dfs(x, depth+1);
            }
        }

        return;
    }


    function LCA(a, b) {
        if (D[a] < D[b]) {
            const tmp = a;
            a = b;
            b = tmp;
        }

        let cost = 0;

        if (D[a] !== D[b]) {
            const diff = D[a] - D[b];

            for (let i = 0; i < 18; ++i) {
                if ((diff & (1<<i)) > 0) {
                    cost += A[a][i][1];
                    a = A[a][i][0];
                }
            }
        }

        if (a === b) return [cost, a];

        for (let i = 17; i > -1; --i) {
            if (A[a][i][0] !== A[b][i][0]) {
                cost += A[a][i][1];
                cost += A[b][i][1];

                a = A[a][i][0];
                b = A[b][i][0];
            }
        }

        cost += A[a][0][1]; 
        cost += A[b][0][1]; 

        return [cost, A[a][0][0]];
    }


    function solve() {
        for (let i = 0; i < N-1; ++i) {
            const [u, v, w] = input[z++].split(" ").map(Number);
            G[u].push([v, w]);
            G[v].push([u, w]);
        }
    
        V[1] = 1;
        dfs(1, 0);

        for (let i = 1; i < 18; ++i) {
            for (let j = 0; j < N+1; ++j) {
                A[j][i][0] = A[A[j][i-1][0]][i-1][0];
                A[j][i][1] = A[j][i-1][1] + A[A[j][i-1][0]][i-1][1];
            }
        }

        const M = Number(input[z++]);

        for (let i = 0; i < M; ++i) {
            const temp = input[z++].split(" ").map(Number);
            let u = temp[1];
            let v = temp[2];

            const res = LCA(u, v);

            if (temp[0] === 1) console.log(res[0]);
            else {
                let k = temp[3]; --k;
                let node = res[1];

                if (D[u] - D[node] < k) {
                    k = D[u] + D[v] - 2*D[node] - k;
                    u = v;
                }

                for (let j = 17; j > -1; --j) {
                    if ((k & (1<<j)) > 0) u = A[u][j][0];
                }

                console.log(u);
            }
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