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
    function set_edge(u, v, c, d) {
        G[u].push(new Edge(v, c, -d, G[v].length))
        G[v].push(new Edge(u, 0, d, G[u].length))

        return
    }

    function solve() {
        let ans = 0
        
        while (true) {
            const pre = Array(sink+1).fill(-1);
            const dist = Array(sink+1).fill(Infinity);
            const indx = Array(sink+1).fill(-1);
            const checker = Array(sink+1).fill(0);
            const q = [src]
            checker[src] = 1; dist[src] = 0;

            while (q.length > 0) {
                const n = q.shift(); checker[n] = 0;

                for (let idx = 0; idx < G[n].length; ++idx) {
                    let edge = G[n][idx]

                    if (edge.c > 0 && dist[edge.x] > dist[n] + edge.d) {
                        dist[edge.x] = dist[n] + edge.d; pre[edge.x] = n; indx[edge.x] = idx;

                        if (checker[edge.x] === 0) {
                            checker[edge.x] = 1; q.push(edge.x);
                        }
                    }
                }
            }

            if (pre[sink] === -1) break;

            for (let n = sink; n !== src; n = pre[n]) {
                let edge = G[pre[n]][indx[n]]
                --edge.c
                ++G[n][edge.inv].c
            }

            ans += dist[sink]
        }

        console.log(-ans - 3e6)

        return
    }

    const N = Number(input[z++])
    const [src, sink] = [N+5, N+6]
    const G = Array.from({length: sink+1}, () => [])
    const stories = input[z++].split(' ').map(Number)

    for (let v = 1; v < 4; ++v) {
        set_edge(src, v, 1, 1e6)
        set_edge(src, v, stories[v-1]-1, 0)
    }
    set_edge(src, 4, Infinity, 0)

    for (let u = 5; u < N+5; ++u) {
        const temp = input[z++].split(' ').map(Number)
        
        set_edge(u, sink, 1, 0)

        for (let v = 1; v < 4; ++v) set_edge(v, u, 1, temp[v-1]);

        set_edge(4, u, 1, 0)
    }

    solve()
})