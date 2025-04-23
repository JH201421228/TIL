const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function solve() {
        function set_edge(u, v) {
            G[u].push(v); G[v].push(u); C[u][v] = 1;      
        }

        const [N, M] = input[z++].split(' ').map(Number)
        const [src, sink] = [2*N+1, 2*N+2]; let ans = 0

        const G = Array.from({length: sink+1}, () => [])
        const C = Array.from({length: sink+1}, () => Array(sink+1).fill(0))
        const F = Array.from({length: sink+1}, () => Array(sink+1).fill(0))
        const D = Array.from({length: sink+1}, () => Array(sink+1).fill(0))

        for (let i = 1; i < N+1; ++i) {
            set_edge(i, i+N); set_edge(src, i); set_edge(i+N, sink);
            D[i][i+N] = -1; D[i+N][i] = 1;
        }

        for (let i = 0; i < M; ++i) {
            const [u, v] = input[z++].split(' ').map(Number); set_edge(u+N, v);
        }

        for (let i = 0; i < 2; ++i) {
            const pre = Array(sink+1).fill(-1)
            const dist = Array(sink+1).fill(Infinity)
            const checker = Array(sink+1).fill(0)
            const q = [src]; dist[src] = 0; checker[src] = 1;

            while (q.length > 0) {
                const n = q.shift(); checker[n] = 0;

                for (let x of G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x]; pre[x] = n;

                        if (checker[x] === 0) {
                            checker[x] = 1; q.push(x);
                        }
                    }
                }
            }

            if (pre[sink] === -1) break

            for (let n = sink; n !== src; n = pre[n]) {
                F[pre[n]][n]++; F[n][pre[n]]--; ans += D[pre[n]][n];
            }
        }

        console.log(-ans)
    }

    let T = Number(input[z++])

    while(T-- > 0) {
        solve()
    }
})