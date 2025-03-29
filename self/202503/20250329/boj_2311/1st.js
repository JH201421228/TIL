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
    function setVertex(n) {
        G[n].push(n+N)
        G[n+N].push(n)
        C[n][n+N] = Infinity
    }

    function setEdge(u, v, c) {
        G[u+N].push(v)
        G[v].push(u+N)
        C[u+N][v] = 1
        D[u+N][v] = c
        D[v][u+N] = -c

        G[v+N].push(u)
        G[u].push(v+N)
        C[v+N][u] = 1
        D[v+N][u] = c
        D[u][v+N] = -c
    }

    function solve() {
        for (let zz = 0; zz < 2; ++zz) {
            const pre = Array(2*N+1).fill()
            const dist = Array(2*N+1).fill()
            const checker = Array(2*N+1).fill()
    
            const q = [1]
            checker[1] = 1
            dist[1] = 0

            while (q.length > 0) {
                const n = q.shift()

                for (let x of G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x]
                        pre[x] = n
                
                        if (checker[x] === 0) {
                            checker[x] = 1
                            q.push(x)
                        }
                    }
                }
            }

            for (let n = 2*N; n !== 1; n = pre[n]) {
                ++F[pre[n]][n]
                --F[n][pre[n]]
                ans += D[pre[n]][n]
            }
        }
    }

    const [N, M] = input[z++].split(' ').map(Number)
    const G = Array.from({length: 2*N+1}, () => [])
    const D = Array.from({length: 2*N+1}, () => Array(2*N+1).fill(0))
    const C = Array.from({length: 2*N+1}, () => Array(2*N+1).fill(0))
    const F = Array.from({length: 2*N+1}, () => Array(2*N+1).fill(0))
    
    for (let n = 1; n < N+1; ++n) {
        setVertex(n)
    }

    for (let i = 0; i < M; ++i) {
        const [u, v, c] = input[z++].split(' ').map(Number)
        setEdge(u, v, c)
    }

    solve()

    console.log(ans)
})