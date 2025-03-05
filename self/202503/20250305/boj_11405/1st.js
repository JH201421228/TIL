const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
const maxv = 1<<30
let z = 0

rl.on("line", l => {
    input.push(l)
})

rl.on("close", () => {
    const [N, M] = input[z++].split(' ').map(Number)
    const G = Array.from({length: 203}, () => [])
    const C = Array.from({length: 203}, () => Array(203).fill(0))
    const D = Array.from({length: 203}, () => Array(203).fill(0))
    const F = Array.from({length: 203}, () => Array(203).fill(0))

    const temp1 = input[z++].split(' ').map(Number)
    for (let u = 101; u < 101+N; ++u) {
        G[u].push(202)
        G[202].push(u)
        C[u][202] = temp1[u-101]
    }

    const temp2 = input[z++].split(' ').map(Number)
    for (let v = 1; v < 1+M; ++v) {
        G[v].push(201)
        G[201].push(v)
        C[201][v] = temp2[v-1]
    }

    for (let u = 1; u < 1+M; ++u) {
        const temp3 = input[z++].split(' ').map(Number)
        for (let v = 101; v < 101+N; ++v) {
            D[u][v] = temp3[v-101]
            D[v][u] = -temp3[v-101]
            
            C[u][v] = maxv

            G[u].push(v)
            G[v].push(u)
        }
    }

    let ans = 0

    while (true) {
        const pre = Array(203).fill(-1)
        const dist = Array(203).fill(maxv)
        const checker = Array(203).fill(0)

        const q = [201]

        dist[201] = 0
        checker[201] = 1

        while (q.length > 0) {
            let n = q.shift()
            checker[n] = 0

            for (let x of G[n]) {
                if (C[n][x] - F[n][x] > 0 && dist[x] > dist[n] + D[n][x]) {
                    dist[x] = dist[n] + D[n][x]
                    pre[x] = n

                    if (checker[x] === 0) {
                        q.push(x)
                        checker[x] = 1
                    }
                }
            }
        }

        if (pre[202] === -1) {
            break
        }

        let flow = maxv
        
        for (let n = 202; n !== 201; n = pre[n]) {
            flow = Math.min(flow, C[pre[n]][n] - F[pre[n]][n])
        }

        for (let n = 202; n !== 201; n = pre[n]) {
            ans += (flow * D[pre[n]][n])
            F[pre[n]][n] += flow
            F[n][pre[n]] -= flow
        }
    }

    console.log(ans)
})