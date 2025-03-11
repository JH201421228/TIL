const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const maxv = Infinity
const input = []
let cnt = 0
let ans = 0
let z = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {

    
    const [N, M] = input[z++].split(' ').map(Number)
    const src = N+M+1
    const sink = N+M+2
    
    G = Array.from({length: N+M+3}, () => [])
    F = Array.from({length: N+M+3}, () => Array(N+M+3).fill(0))
    C = Array.from({length: N+M+3}, () => Array(N+M+3).fill(0))
    D = Array.from({length: N+M+3}, () => Array(N+M+3).fill(0))
    
    for (let u = 1; u < N+1; ++u) {
        G[src].push(u)
        G[u].push(src)
        C[src][u] = 1
    }
    
    for (let u = N+1; u < N+M+1; ++u) {
        G[sink].push(u)
        G[u].push(sink)
        C[u][sink] = 1
    }
    
    for (let u = 1; u < N+1; ++u) {
        const temp = input[z++].split(' ').map(Number)
        for (let idx = 1; idx < temp[0]*2; idx += 2) {
            const v = temp[idx] + N
            const c = temp[idx+1]
            
            G[v].push(u)
            G[u].push(v)

            C[u][v] = 1
            D[u][v] = c
            D[v][u] = -c
        }
    }

    while (true) {
        const pre = Array(N+M+3).fill(-1)
        const dist = Array(N+M+3).fill(maxv)
        const checker = Array(N+M+3).fill(0)

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

        for (let n = sink; n !== src; n = pre[n]) {
            F[pre[n]][n] += 1
            F[n][pre[n]] -= 1
            ans += D[pre[n]][n]
        }
        cnt += 1
    }

    console.log(cnt)
    console.log(ans)
})