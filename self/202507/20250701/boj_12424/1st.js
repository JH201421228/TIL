const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

class Edge {
    constructor(x, c, d, inv) {
        this.x = x; this.c = c; this.d = d; this.inv = inv;
    }
}

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function init() {
        const T = Number(input[z++])

        for (let t = 1; t < T+1; ++t) {
            console.log(`Case #${t}: ${String(solve())}`)
        }

        return
    }

    function solve() {
        const [N, A, B, C, D, E, F] = input[z++].split(' ').map(Number)
        const [src, sink] = [7, 8]
        const G = Array.from({length: 9}, () => [])
        const arr = []

        for (let i = 0; i < 3; ++i) arr.push(input[z++].split(' ').map(Number));

        set_edge(src, 1, A, 0, G); set_edge(src, 2, B, 0, G); set_edge(src, 3, C, 0, G);
        set_edge(4, sink, D, 0, G); set_edge(5, sink, E, 0, G); set_edge(6, sink, F, 0, G);

        for (let u = 0; u < 3; ++u) {
            for (let v = 0; v < 3; ++v) {
                set_edge(u+1, v+4, N, -arr[u][v], G)
            }
        }

        return spfa(src, sink, G)
    }

    function spfa(src, sink, G) {
        let res = 0n

        while (true) {
            const pre = Array(9).fill(-1), indx = Array(9).fill(-1), checker = Array(9).fill(0), dist = Array(9).fill(Infinity);
            const q = [src]; dist[src] = 0; checker[src] = 1

            while (q.length > 0) {
                const n = q.shift(); checker[n] = 0;

                for (let idx = 0; idx < G[n].length; ++idx) {
                    const edge = G[n][idx];

                    if (edge.c > 0 && dist[edge.x] > dist[n] + edge.d) {
                        dist[edge.x] = dist[n] + edge.d; pre[edge.x] = n; indx[edge.x] = idx;

                        if (checker[edge.x] === 0) {
                            checker[edge.x] = 1; q.push(edge.x)
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
                const edge = G[pre[n]][indx[n]]
                edge.c -= flow
                G[n][edge.inv].c += flow
            }

            res -= BigInt(flow) * BigInt(dist[sink])
        }

        return res
    }

    function set_edge(u, v, c, d, G) {
        G[u].push(new Edge(v, c, d, G[v].length))
        G[v].push(new Edge(u, 0, -d, G[u].length-1))

        return
    }

    init()
})