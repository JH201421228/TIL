const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0
let ans = 0

class Edge {
    constructor(x, c, d, inv) {
        this.x = x; this.c = c; this.d = d; this.inv = inv
    }
}

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function solve() {
        pre.fill(-1)
        checker.fill(0)
        indx.fill(0)
        dist.fill(Infinity)

        const q = [src]
        dist[src] = 0
        checker[src] = 1

        while (q.length > 0) {
            let n = q.shift()
            checker[n] = 0

            for (let idx = 0; idx < G[n].length; ++idx) {
                let edge = G[n][idx]
                if (edge.c > 0 && dist[edge.x] > dist[n] + edge.d) {
                    dist[edge.x] = dist[n] + edge.d
                    indx[edge.x] = idx
                    pre[edge.x] = n

                    if (checker[edge.x] === 0) {
                        checker[edge.x] = 1
                        q.push(edge.x)
                    }
                }
            }
        }

        for (let n = sink; n !== src; n = pre[n]) {
            --G[pre[n]][indx[n]].c
            ++G[n][G[pre[n]][indx[n]].inv].c
        }

        return dist[sink]
    }

    function set_edge(u, v, c, d) {
        G[u].push(new Edge(v, c, d, G[v].length))
        G[v].push(new Edge(u, 0, -d, G[u].length-1))
    }   

    const [N, M] = input[z++].split(' ').map(Number)
    const [src, sink] = [2, N<<1|1]
    const pre = Array(sink+1).fill(-1)
    const checker = Array(sink+1).fill(0)
    const indx = Array(sink+1).fill(-1)
    const dist = Array(sink+1).fill(Infinity)
    const G = Array.from({length: sink+1}, () => [])

    for (let n = 1; n < N+1; ++n) {
        set_edge(n<<1, n<<1|1, Infinity, 0)
    }

    for (let i = 0; i < M; ++i) {
        const [u, v, d] = input[z++].split(' ').map(Number)
        set_edge(u<<1|1, v<<1, 1, d)
        set_edge(v<<1|1, u<<1, 1, d)
    }

    for (let i = 0; i < 2; ++i) {
        ans += solve()
    }

    console.log(ans)
})