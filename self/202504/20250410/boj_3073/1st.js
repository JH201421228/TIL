const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0
let ans = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {
    while (true) {
        const [N, M] = input[z++].split(' ').map(Number)

        if (N === 0 && M === 0) break

        ans = 0
        const maps = []
        for (let i = 0; i < N; ++i) maps.push(input[z++].split(''))
        const homes = []
        const children = []

        for (let n = 0; n < N*M; ++n) {
            const [i, j] = [Math.floor(n/M), n%M]

            if (maps[i][j] === 'H') homes.push([i, j])
            else if (maps[i][j] === 'm') children.push([i, j])
        }

        const [n, m] = [homes.length, children.length]
        const [src, sink] = [n+m+1, n+m+2]
        const G = Array.from({length: sink+1}, () => [])
        const F = Array.from({length: sink+1}, () => Array(sink+1).fill(0))
        const C = Array.from({length: sink+1}, () => Array(sink+1).fill(0))
        const D = Array.from({length: sink+1}, () => Array(sink+1).fill(0))

        for (let i = 0; i < n; ++i) {
            const u = i+1
            G[src].push(u)
            G[u].push(src)
            C[src][u] = 1
        }

        for (let i = 0; i < m; ++i) {
            const u = i+1+n
            G[sink].push(u)
            G[u].push(sink)
            C[u][sink] = 1
        }

        for (let i = 0; i < n; ++i) {
            const h = homes[i]
            const u = i+1
            
            for (let j = 0; j < m; ++j) {
                const c = children[j]
                const v = j+1+n

                G[u].push(v)
                G[v].push(u)
                C[u][v] = 1
                D[u][v] = Math.abs(h[0] - c[0]) + Math.abs(h[1] - c[1])
                D[v][u] = -D[u][v]
            }
        }

        while (true) {
            const pre = Array(sink+1).fill(-1)
            const dist = Array(sink+1).fill(Infinity)
            const checker = Array(sink+1).fill(0)
            const q = [src]
            checker[src] = 1
            dist[src] = 0

            while (q.length > 0) {
                const n = q.shift()
                checker[n] = 0

                for (let x of G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x]
                        pre[x] = n

                        if (checker[x] === 0) {
                            checker[x] = 0
                            q.push(x)
                        }
                    }
                }
            }

            if (pre[sink] === -1) break

            for (let n = sink; n !== src; n = pre[n]) {
                ++F[pre[n]][n]
                --F[n][pre[n]]
                ans += D[pre[n]][n]
            }
        }
        console.log(ans)
    }

})