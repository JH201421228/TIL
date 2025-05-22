const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

class Edge {
    constructor (x, c, d, inv) {
        this.x = x; this.c = c; this.d = d; this.inv = inv;
    }
}

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function set_edge(u, v, c, d, G) {
        G[u].push(new Edge(v, c, d, G[v].length))
        G[v].push(new Edge(u, 0, -d, G[u].length-1))

        return
    }

    function solve(src, sink, G) {
        let ans = 0

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

            for (let n = sink; n != src; n = pre[n]) {
                let edge = G[pre[n]][indx[n]]
                --edge.c
                ++G[n][edge.inv].c
            }

            ans += dist[sink]
        }

        return ans
    }

    let T = Number(input[z++])

    while (T-- > 0) {
        const [N, M] = input[z++].split(' ').map(Number)
        const [src, sink] = [2*N+2, 2*N+3]
        const G = Array.from({length: sink+1}, () => [])

        for (let u = 1; u < N+1; ++u) set_edge(u<<1, u<<1|1, Infinity, 0, G);

        for (let i = 0; i < M; ++i) {
            const [x, y] = input[z++].split(' ').map(Number)
            set_edge(x<<1|1, y<<1, Infinity, 1, G)
            set_edge(y<<1|1, x<<1, Infinity, 1, G)
        }

        const temp = input[z++].split(' ').map(Number)
        for (let u = 1; u < N+1; ++u) {
            if (temp[u-1] === 0) set_edge(u<<1|1, sink, 1, 0, G);
        }

        const tmp = input[z++].split(' ').map(Number)
        for (let v = 1; v < N+1; ++v) {
            if (tmp[v-1] === 0) set_edge(src, v<<1, 1, 0, G);
        }

        console.log(solve(src, sink, G))
    }
})