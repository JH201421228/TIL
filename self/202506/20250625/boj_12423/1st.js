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

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function set_dege(u, v, c, d, G) {
        G[u].push(new Edge(v, c, d, G[v].length));
        G[v].push(new Edge(u, 0, -d, G[u].length-1));

        return;
    }

    function spfa(src, sink, G) {
        let res = 0

        while (true) {
            const pre = Array(9).fill(-1), indx = Array(9).fill(-1), checker = Array(9).fill(0), dist = Array(9).fill(Infinity);
            const q = [src]; checker[src] = 1; dist[src] = 0;

            while (q.length > 0) {
                const n = q.shift(); checker[n] = 0;

                for (let idx = 0; idx < G[n].length; ++idx) {
                    const edge = G[n][idx];

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
                flow = Math.min(edge.c, flow)
            }

            for (let n = sink; n != src; n = pre[n]) {
                let edge = G[pre[n]][indx[n]]
                edge.c -= flow
                G[n][edge.inv].c += flow
            }

            res -= flow*dist[sink]
        }

        return res
    }

    function solve(t) {
        const [N, A, B, C, D, E, F] = input[z++].split(' ').map(Number)
        const [src, sink] = [7, 8]

        const G = Array.from({length: 9}, () => [])
        const arr = []
        for (let i = 0; i < 3; ++i) arr.push(input[z++].split(' ').map(Number));

        set_dege(src, 1, A, 0, G); set_dege(src, 2, B, 0, G); set_dege(src, 3, C, 0, G);
        set_dege(4, sink, D, 0, G); set_dege(5, sink, E, 0, G); set_dege(6, sink, F, 0, G);

        for (let u = 0; u < 3; ++u) {
            for (let v = 0; v < 3; ++v) {
                set_dege(u+1, v+4, Infinity, -arr[u][v], G)
            }
        }

        console.log(`Case #${t}: ${spfa(src, sink, G)}`)
    }

    const T = Number(input[z++])

    for (let t = 1; t < T+1; ++t) {
        solve(t)
    }
})