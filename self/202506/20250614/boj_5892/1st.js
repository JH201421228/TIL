const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

class Edge {
    constructor(x, c, d, inv) {
        this.x = x; this.c = c; this.d = d; this.inv = inv
    }
}

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function set_edge(u, v, c, d) {
        G[u].push(new Edge(v, c, d, G[v].length))
        G[v].push(new Edge(u, 0, -d, G[u].length-1))
    }

    function solve() {
        while (true) {
            const pre = Array(sink+1).fill(-1), indx = Array(sink+1).fill(-1), checker = Array(sink+1).fill(0), dist = Array(sink+1).fill(Infinity)
            const q = [src]; dist[src] = 0; checker[src] = 1;

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

            ans += dist[sink]*flow
        }

        return ans
    }

    let cur = 0, tar = 0, ans = 0;
    let [N, X, Y, Z] = input[z++].split(' ').map(Number)
    let [src, sink] = [(N+1)<<1, (N+1)<<1|1]
    const G = Array.from({length: sink+1}, () => [])

    for (let i = 1; i < N+1; ++i) {
        const [a, b] = input[z++].split(' ').map(Number)
        cur += a; tar += b;
        set_edge(src, i<<1, a, 0)
        set_edge(i<<1|1, sink, b, 0)
    }

    if (tar > cur) ans += (tar-cur)*X;
    else ans += (cur - tar)*Y;

    const fee = X+Y
    for (let u = 1; u < N+1; ++u) {
        for (let v = 1; v < N+1; ++v) {
            const base = Math.abs(u-v)*Z
            const charge = Math.min(fee, base)
            set_edge(u<<1, v<<1|1, Infinity, charge)
        }
    }

    console.log(solve())
})