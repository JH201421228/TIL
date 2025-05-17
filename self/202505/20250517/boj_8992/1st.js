const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const input = []
let z = 0
let [ans, cnt] = [0, 0]

class Edge {
    constructor (x, c, d, inv) {
        this.x = x; this.c = c; this.d = d; this.inv = inv;
    }
}

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function set_edge(u, v, c, d, G) {
        G[u].push(new Edge(v, c, -d, G[v].length))
        G[v].push(new Edge(u, 0, d, G[u].length-1))
    }

    function solve() {
        const [N, M] = input[z++].split(' ').map(Number)
        const horizontal = []
        const vertical = []

        for (let i = 0; i < N; ++i) horizontal.push(input[z++].split(' ').map(Number));
        for (let i = 0; i < M; ++i) vertical.push(input[z++].split(' ').map(Number));

        const [src, sink] = [N+M+1, N+M+2]
        const G = Array.from({length: N+M+3}, () => [])

        for (let u = 1; u < N+1; ++u) {
            set_edge(src, u, 1, 0, G)
            const [ux1, uy1, ux2, uy2, uw] = horizontal[u-1]

            for (let v = N+1; v < N+M+1; ++v) {
                const [vx1, vy1, vx2, vy2, vw] = vertical[v-N-1]

                if (vx1 > Math.min(ux1, ux2) && vx1 < Math.max(ux1, ux2) && uy1 > Math.min(vy1, vy2) && uy1 < Math.max(vy1, vy2)) set_edge(u, v, 1, uw*vw, G);
            }
        }

        for (let v = N+1; v < N+M+1; ++v) set_edge(v, sink, 1, 0, G);

        cnt = 0
        ans = 0

        while (true) {
            const checker = Array(sink+1).fill(0)
            const dist = Array(sink+1).fill(Infinity)
            const indx = Array(sink+1).fill(-1)
            const pre = Array(sink+1).fill(-1)

            const q = [src]
            checker[src] = 1
            dist[src] = 0

            while (q.length > 0) {
                const n = q.shift()
                checker[n] = 0

                for (let idx = 0; idx < G[n].length; ++idx) {
                    const edge = G[n][idx]

                    if (edge.c > 0 && dist[edge.x] > dist[n] + edge.d) {
                        dist[edge.x] = dist[n] + edge.d
                        pre[edge.x] = n
                        indx[edge.x] = idx

                        if (checker[edge.x] === 0) {
                            checker[edge.x] = 1
                            q.push(edge.x)
                        }
                    }
                }
            }

            if (pre[sink] === -1) break;

            ++cnt

            for (let n = sink; n != src; n = pre[n]) {
                let edge = G[pre[n]][indx[n]]
                --edge.c
                ++G[n][edge.inv].c
            }

            ans += dist[sink]
        }

        console.log(cnt, -ans)
    }

    let T = Number(input[z++])

    while (T-- > 0) solve();
})