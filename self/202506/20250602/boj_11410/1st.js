const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

class Edge {
    constructor (x, c, d, inv) {
        this.x = x; this.c = c; this.d = d; this.inv = inv;
    }
}

const input = []
let z = 0
let ans = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function set_edge(u, v, c, d) {
        G[u].push(new Edge(v, c, -d, G[v].length))
        G[v].push(new Edge(u, 0, d, G[u].length-1))

        return
    }

    function solve() {
        while (true) {
            const pre = Array(sink+1).fill(-1), indx = Array(sink+1).fill(-1), checker = Array(sink+1).fill(0), dist = Array(sink+1).fill(Infinity);
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

            let flow = Infinity
            for (let n = sink; n != src; n = pre[n]) {
                const edge = G[pre[n]][indx[n]]
                flow = Math.min(flow, edge.c)
            }

            for (let n = sink; n != src; n = pre[n]) {
                let edge = G[pre[n]][indx[n]]
                edge.c -= flow
                G[n][edge.inv].c += flow
            }

            ans += flow*dist[sink]
        }

        return
    }

    const [N, P] = input[z++].split(' ').map(Number)
    const [src, sink] = [N+1, N+2]

    const G = Array.from({length: sink+1}, () => [])

    set_edge(src, 1, P, 0); set_edge(N, sink, P, 0);
    for (let u = 1; u < N; ++u) set_edge(u, u+1, Infinity, 0);

    const clients = [], fees = [];
    for (let i = 0; i < N-1; ++i) clients.push(input[z++].split(' ').map(Number));
    for (let i = 0; i < N-1; ++i) fees.push(input[z++].split(' ').map(Number));

    for (let u = 1; u < N; ++u) {
        for (let v = u+1; v < N+1; ++v) set_edge(u, v, clients[u-1][v-u-1], fees[u-1][v-u-1]);
    }

    solve()

    console.log(-ans)
})