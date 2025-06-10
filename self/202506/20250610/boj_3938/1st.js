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
    function set_edge(u, v, c, d, G) {
        G[u].push(new Edge(v, c, -d, G[v].length))
        G[v].push(new Edge(u, 0, d, G[u].length-1))

        return
    }

    const [src, sink] = [366<<1, 366<<1|1]
    
    while (true) {
        const N = Number(input[z++])
        if (N === 0) break;

        const G = Array.from({length: sink+1}, () => [])
        set_edge(src, 1<<1, 2, 0, G)
        set_edge(365<<1|1, sink, 2, 0, G)
        for (let i = 1; i < 366; ++i) set_edge(i<<1, i<<1|1, Infinity, 0, G);
        for (let u = 1; u < 365; ++u) set_edge(u<<1|1, (u+1)<<1, Infinity, 0, G);
        for (let i = 0; i < N; ++i) {
            const [a, b, c] = input[z++].split(' ').map(Number)
            set_edge(a<<1, b<<1|1, 1, c, G)
        }

        let ans = 0

        while (true) {
            const pre = Array(sink+1).fill(-1), indx = Array(sink+1).fill(-1), checker = Array(sink+1).fill(0), dist = Array(sink+1).fill(Infinity);
            const q = [src]; dist[src] = 0; checker[src] = 1;

            while (q.length > 0) {
                const n = q.shift(); checker[n] = 0;

                for (let idx = 0; idx < G[n].length; ++idx) {
                    const edge = G[n][idx]

                    if (edge.c > 0 && dist[edge.x] > dist[n] + edge.d) {
                        dist[edge.x] = dist[n] + edge.d; pre[edge.x] = n; indx[edge.x] = idx;

                        if (checker[edge.x] === 0) {
                            checker[edge.x] = 1; q.push(edge.x)
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

        console.log(-ans)
    }
})