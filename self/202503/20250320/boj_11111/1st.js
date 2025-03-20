const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const grades = [[10, 8, 7, 5, 1], [8, 6, 4, 3, 1], [7, 4, 3, 2, 1], [5, 3, 2, 2, 1], [1, 1, 1, 1, 0]]
const T = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
const delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
const input = []
let z = 0
let ans = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {
    const [N, M] = input[z++].split(' ').map(Number)

    const B = []
    for (let i = 0; i < N; ++i) B.push(input[z++])
    
    const src = N*M+1
    const sink = N*M+2

    const G = Array.from({length: N*M+3}, () => [])
    const C = Array.from({length: N*M+3}, () => Array(N*M+3).fill(0))
    const D = Array.from({length: N*M+3}, () => Array(N*M+3).fill(0))
    const F = Array.from({length: N*M+3}, () => Array(N*M+3).fill(0))

    for (let i = 0; i < N; ++i) {
        for (let j = (i+1)%2; j < M; j+=2) {
            const v = i*M+j+1

            G[v].push(sink)
            G[sink].push(v)
            C[v][sink] = 1
        }

        for (let j = i%2; j < M; j+=2) {
            const u = i*M+j+1
            G[src].push(u)
            G[u].push(src)
            G[u].push(sink)
            G[sink].push(u)
            C[u][sink] = 1
            C[src][u] = 1

            for (const d of delta) {
                const [xi, xj] = [i+d[0], j+d[1]]
                if (xi >= 0 && xi < N && xj >= 0 && xj < M) {
                    const v = xi*M+xj+1
                    G[u].push(v)
                    G[v].push(u)
                    C[u][v] = 1
                    D[u][v] = -grades[T[B[i][j]]][T[B[xi][xj]]]
                    D[v][u] = -D[u][v]
                }
            }
        }
    }

    while (true) {
        const pre = Array(N*M+3).fill(-1)
        const dist = Array(N*M+3).fill(Infinity)
        const checker = Array(N*M+3).fill(0)
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
                        checker[x] = 1
                        q.push(x)
                    }
                }
            }
        }

        if (pre[sink] === -1) break

        for (let n = sink; n != src; n = pre[n]) {
            F[pre[n]][n] += 1
            F[n][pre[n]] -= 1
            ans += D[pre[n]][n]
        }
    }

    console.log(-ans)
})