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
    const N = Number(input[z++])

    const [src, sink] = [2*N+1, 2*N+2]

    const G = Array.from({length: 2*N+3}, () => [])
    const C = Array.from({length: 2*N+3}, () => Array(2*N+3).fill(0))
    const F = Array.from({length: 2*N+3}, () => Array(2*N+3).fill(0))
    const D = Array.from({length: 2*N+3}, () => Array(2*N+3).fill(0))

    for (let u = 1; u < N+1; ++u) {
        G[src].push(u)
        G[u].push(src)
        C[src][u] = 1

        G[sink].push(u+N)
        G[u+N].push(sink)
        C[u+N][sink] = 1
    }

    for (let u = 1; u < N+1; ++u) {
        const temp = input[z++].split(' ').map(Number)
        for (let v = N+1; v < 2*N+1; ++v) {
            G[u].push(v)
            G[v].push(u)
            C[u][v] = 1
            D[u][v] = temp[v-N-1]
            D[v][u] = -temp[v-N-1]
        }
    }

    while (true) {
        const pre = Array(2*N+3).fill(-1)
        const dist = Array(2*N+3).fill(Infinity)
        const checker = Array(2*N+3).fill(0)
        const q = [src]
        checker[src] = 1
        dist[src] = 0

        while (q.length > 0) {
            let n = q.shift()
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

    console.log(ans)
})