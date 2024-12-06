const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", line => {
    input.push(line)
})

rl.on("close", () => {
    const dfs = n => {
        A[n] = ++cnt
        W[n] = ++order
        for (let x of G[n]) {
            if (A[x] === 0) {
                dfs(x)
                --order
            }
        }
        E[n] = cnt
    }

    const U = idx => {
        while (idx < N+1) {
            T[idx] += 1
            idx += (idx & -idx)
        }
    }

    const S = idx => {
        let res = 0
        while (idx > 0) {
            res += T[idx]
            idx -= (idx & -idx)
        }
        return res
    }

    const [N, C] = input[z].split(" ").map(Number); ++z

    const A = Array(N+1).fill(0)
    const E = Array(N+1).fill(0)
    const T = Array(N+1).fill(0)
    const W = Array(N+1).fill(0)
    let order = 0
    let cnt = 0

    const G = Array.from({length: N+1}, () => [])
    for (let i = 0; i < N-1; ++i) {
        const [u, v] = input[z].split(" ").map(Number); ++z
        G[u].push(v); G[v].push(u)
    }

    dfs(C)

    const M = Number(input[z]); ++z

    for (let i = 0; i < M; ++i) {
        const [a, b] = input[z].split(" ").map(Number); ++z

        if (a === 1) {
            U(A[b])
        }
        else {
            console.log(W[b] * (S(E[b]) - S(A[b]-1)))
        }
    }
})