const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

function fee(t, s, k) {
    if (t > s) {
        if ((t-s)*(t-s) > k) return k
        else return (t-s)*(t-s)
    }
    else return 0
}

function solve() {
    const N = Number(input[z++])
    const time_in = input[z++].split(' ').map(Number)
    const time_out = input[z++].split(' ').map(Number)
    const T = Number(input[z++])
    const K = Number(input[z++])

    const [src, sink] = [2*N+1, 2*N+2]

    const G = Array.from({length: 2*N+3}, () => [])
    const D = Array.from({length: 2*N+3}, () => Array(2*N+3).fill(0))
    const F = Array.from({length: 2*N+3}, () => Array(2*N+3).fill(0))
    const C = Array.from({length: 2*N+3}, () => Array(2*N+3).fill(0))

    const ans_list = []

    for (let i = 0; i < N; ++i) {
        const u = i+1
        G[src].push(u); G[u].push(src); C[src][u] = 1;
        G[u+N].push(sink); G[sink].push(u+N); C[u+N][sink] = 1;

        for (let j = 0; j < N; ++j) {
            const v = N+j+1
            if (time_out[j]-time_in[i] > 0) {
                const f = fee(T, time_out[j]-time_in[i], K)
                G[u].push(v); G[v].push(u); C[u][v] = 1; D[u][v] = f; D[v][u] = -f;
            }
        }
    }

    let ans = 0; let isPossible = true;

    for (let i = 0; i < N; ++i) {
        const pre = Array(2*N+3).fill(-1)
        const dist = Array(2*N+3).fill(Infinity)
        const checker = Array(2*N+3).fill(0)
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

        if (pre[sink] === -1) {
            isPossible = !isPossible
            break
        }

        for (let n = sink; n !== src; n = pre[n]) {
            ++F[pre[n]][n]; --F[n][pre[n]]; ans += D[pre[n]][n];
        }
    }

    if (isPossible) ans_list.push(ans);
    else {
        console.log(-1)
        process.exit(0)
    }

    for (let i = 0; i < 2*N+3; ++i) {
        for (let j = 0; j < 2*N+3; ++j) {
            F[i][j] = 0
        }
    }

    ans = 0

    for (let i = 0; i < N; ++i) {
        const pre = Array(2*N+3).fill(-1)
        const dist = Array(2*N+3).fill(Infinity)
        const checker = Array(2*N+3).fill(0)
        const q = [src]
        checker[src] = 1
        dist[src] = 0

        while (q.length > 0) {
            const n = q.shift()
            checker[n] = 0

            for (let x of G[n]) {
                if (C[n][x] > F[n][x] && dist[x] > dist[n] - D[n][x]) {
                    dist[x] = dist[n] - D[n][x]
                    pre[x] = n

                    if (checker[x] === 0) {
                        checker[x] = 1
                        q.push(x)
                    }
                }
            }
        }

        for (let n = sink; n !== src; n = pre[n]) {
            ++F[pre[n]][n]; --F[n][pre[n]]; ans -= D[pre[n]][n];
        }
    }
    ans_list.push(-ans);

    console.log(...ans_list)
}

rl.on("line", l => input.push(l))

rl.on("close", () => {
    solve()
})