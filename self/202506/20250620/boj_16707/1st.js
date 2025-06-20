const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

class Edge {
    constructor(x, c, d, inv) {
        this.x = x; this.c = c; this.d = d; this.inv = inv;
    }
}

const input = []
let z = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function set_edge(u, v, c, d) {
        G[u].push(new Edge(v, c, d, G[v].length))
        G[v].push(new Edge(u, 0, -d, G[u].length-1))

        return
    }

    function spfa(src, sink) {
        const pre = Array((N+1)<<1).fill(-1), indx = Array((N+1)<<1).fill(-1), checker = Array((N+1)<<1).fill(0), dist = Array((N+1)<<1).fill(Infinity)
        const q = [src]; checker[src] = 1; dist[src] = 0;

        while (q.length > 0) {
            let n = q.shift(); checker[n] = 0;

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

        for (let n = sink; n != src; n = pre[n]) {
            const edge = G[pre[n]][indx[n]]
            --edge.c
            ++G[n][edge.inv].c
        }

        return dist[sink]
    }

    const [N, M] = input[z++].split(' ').map(Number)
    G = Array.from({length: (N+1)<<1}, () => [])

    for (let n = 1; n < N+1; ++n) set_edge(n<<1, n<<1|1, Infinity, 0);

    for (let i = 0; i < M; ++i) {
        const [u, v, d] = input[z++].split(' ').map(Number)
        set_edge(u<<1|1, v<<1, 1, d)
        set_edge(v<<1|1, u<<1, 1, d)
    }

    console.log(spfa(2<<1, 1<<1|1) + spfa(2<<1, N<<1|1))
})