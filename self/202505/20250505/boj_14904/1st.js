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

const delta = [[1, 0], [0, 1]]

rl.on("line", l => input.push(l))

rl.on("close", () => {
    function set_edge(u, v, c, d) {
        G[u].push(new Edge(v, c, -d, G[v].length))
        G[v].push(new Edge(u, 0, d, G[u].length-1))
        return
    }

    function solve() {
        const pre = Array(sink+1).fill(-1)
        const dist = Array(sink+1).fill(Infinity)
        const indx = Array(sink+1).fill(-1)
        const checker = Array(sink+1).fill(0)

        const q = [src]; checker[src] = 1; dist[src] = 0;

        while (q.length !== 0) {
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

        if (dist[sink] === Infinity) {
            return 0;
        }
        
        for (let n = sink; n !== src; n = pre[n]) {
            const edge = G[pre[n]][indx[n]]
            --edge.c
            ++G[n][edge.inv].c
        }

        return dist[sink]
    }

    let [N, K] = input[z++].split(' ').map(Number)
    const [src, sink] = [2, (N*N)<<1|1]
    const maze = []
    const G = Array.from({length: sink+1}, () => [])

    let ans = 0

    for (let i = 0; i < N; ++i) maze.push(input[z++].split(' ').map(Number));

    for (let n = 1; n < N*N+1; ++n) {
        set_edge(n<<1, n<<1|1, 1, maze[Math.floor((n-1)/N)][(n-1)%N])
        set_edge(n<<1, n<<1|1, Infinity, 0)
    }

    for (let i = 0; i < N; ++i) {
        for (let j = 0; j < N; ++j) {
            const u = N*i+j+1
            for (let dd of delta) {
                const [ii, jj] = [i+dd[0], j+dd[1]]
                if (ii >= 0 && ii < N && jj >= 0 && jj < N) {
                    const v = N*ii+jj+1
                    set_edge(u<<1|1, v<<1, Infinity, 0)
                }
            }
        }
    }

    while (K-- > 0) {
        ans += solve()
    }

    console.log(-ans)
})