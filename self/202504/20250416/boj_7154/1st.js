const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {
    const satisfaction = [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]]

    while (true) {
        const [N, M] = input[z++].split(' ').map(Number)
        if (N === 0 && M === 0) break

        let ans = 0;
        const [src, sink] = [N+M+1, N+M+2]
        const G = Array.from({length: sink+1}, () => [])
        const F = Array.from({length: sink+1}, () => Array(sink+1).fill(0))
        const D = Array.from({length: sink+1}, () => Array(sink+1).fill(0))
        const C = Array.from({length: sink+1}, () => Array(sink+1).fill(0))

        for (let i = 0; i < N; ++i) {
            const u = i+M+1
            C[u][sink] = Number(input[z++]); G[u].push(sink); G[sink].push(u)
        }

        for (let i = 0; i < M; ++i) {
            const u = i+1
            C[src][u] = 1; G[src].push(u); G[u].push(src)

            const temp = input[z++].split(' ').map(Number)
            const grade = temp[0]
            for (let idx = 1; idx < 5; ++idx) {
                const v = temp[idx]+1+M
                G[u].push(v); G[v].push(u)
                D[u][v] = -satisfaction[grade-1][idx-1]; D[v][u] = -D[u][v]; C[u][v] = 1
            }
        }

        while (true) {
            const pre = Array(sink+1).fill(-1);
            const dist = Array(sink+1).fill(Infinity);
            const checker = Array(sink+1).fill(0);
            const q = [src]; dist[src] = 0; checker[src] = 1

            while (q.length > 0) {
                const n = q.shift(); checker[n] = 0

                for (let x of G[n]) {
                    if (C[n][x] > F[n][x] && dist[x] > dist[n] + D[n][x]) {
                        dist[x] = dist[n] + D[n][x]; pre[x] = n

                        if (checker[x] === 0) {
                            checker[x] = 1; q.push(x)
                        }
                    }
                }
            }

            if (pre[sink] === -1) break

            for (let n = sink; n !== src; n = pre[n]) {
                F[pre[n]][n]++; F[n][pre[n]]--; ans += D[pre[n]][n]
            }
        }

        console.log(-ans)
    }
})