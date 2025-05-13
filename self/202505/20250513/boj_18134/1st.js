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
    }

    function solve() {
        const pre = Array(2*N+2).fill(-1)
        const indx = Array(2*N+2).fill(-1)
        const checker = Array(2*N+2).fill(0)
        const dist = Array(2*N+2).fill(Infinity)
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

        if (pre[sink] == -1) return dist[sink];

        for (let n = sink; n != src; n = pre[n]) {
            let edge = G[pre[n]][indx[n]];
            --edge.c;
            ++G[n][edge.inv].c;
        }

        return dist[sink]
    }

    const [N, M] = input[z++].split(' ').map(Number)
    const G = Array.from({length: 2*N+2}, () => [])

    for (let u = 1; u < N+1; ++u) set_edge(u<<1, u<<1|1, 1, 0);

    for (let i = 0; i < M; ++i) {
        const [a, b, c] = input[z++].split(' ').map(Number)
        set_edge(b<<1|1, c<<1, 1, a)
        set_edge(c<<1|1, b<<1, 1, a)
    }

    const [a, b] = input[z++].split(' ').map(Number)
    const [src, sink] = [a<<1, b<<1|1]
    set_edge(a<<1, a<<1|1, 1, 0); set_edge(b<<1, b<<1|1, 1, 0);

    for (let i = 0; i < 2; ++i) {
        ans += solve()
    }

    if (ans >= Infinity) console.log(-1);
    else console.log(ans)
})