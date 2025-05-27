const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0
let ans = 0

class Edge {
    constructor (x, c, d, inv) {
        this.x = x; this.c = c; this.d = d; this.inv = inv;
    }
}

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function set_edge(u, v, c, d) {
        G[u].push(new Edge(v, c, d, G[v].length))
        G[v].push(new Edge(u, 0, -d, G[u].length-1))

        return
    }

    function solve() {
        while (true) {
            const pre = Array(sink+1).fill(-1)
            const indx = Array(sink+1).fill(-1)
            const checker = Array(sink+1).fill(0)
            const dist = Array(sink+1).fill(Infinity)
            const q = [src]; checker[src] = 1; dist[src] = 0;
    
            while (q.length > 0) {
                const n = q.shift(); checker[n] = 0;

                for (let idx = 0; idx < G[n].length; ++idx) {
                    const edge = G[n][idx]

                    if (edge.c > 0 && dist[edge.x] > dist[n] + edge.d) {
                        dist[edge.x] = dist[n] + edge.d; pre[edge.x] = n; indx[edge.x] = idx;

                        if (checker[edge.x] === 0) {
                            checker[edge.x] = 1; q.push(edge.x);
                        }
                    }
                }
            }

            if (pre[sink] === -1) break;

            for (let n = sink; n != src; n = pre[n]) {
                let edge = G[pre[n]][indx[n]]
                --edge.c
                ++G[n][edge.inv].c
            }

            ans += dist[sink]
        }

        return
    }

    const N = Number(input[z++])
    const [src, sink] = [2*N+2, 2*N+3]
    const G = Array.from({length: sink+1}, () => [])
    const A = input[z++].split(' ').map(Number)
    const H = input[z++].split(' ').map(Number)
    const L = input[z++].split(' ').map(Number)
    const arr = []

    for (let idx = 0; idx < N; ++idx) arr.push([A[idx], H[idx], L[idx]]);

    arr.sort((a, b) => b[0] - a[0])

    set_edge(src, 1<<1, arr[0][2], arr[0][1])
    for (let v = 2; v < N+1; ++v) set_edge(src, v<<1, arr[v-1][2]-1, arr[v-1][1]);
    for (let u = 2; u < N+1; ++u) set_edge(u<<1|1, sink, 1, arr[u-1][1]);
    for (let u = 1; u < N+1; ++u) {
        for (let v = u+1; v < N+1; ++v) set_edge(u<<1, v<<1|1, 1, -(arr[u-1][0]^arr[v-1][0]));
    }

    solve()

    console.log(-ans)
})