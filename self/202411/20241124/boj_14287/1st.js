const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on("line", line => {
    input.push(line)
})

rl.on("close", () => {
    const [N, M] = input[0].split(' ').map(Number)
    const G = Array.from({length: N+1}, () => [])
    const A = Array(N+1).fill(0)
    const E = Array(N+1).fill(0)
    let cnt = 0
    const T = Array(N+1).fill(0)

    const U = (idx, v) => {
        while (idx < N+1) {
            T[idx] += v
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

    const dfs = n => {
        A[n] = ++cnt
        for (let x of G[n]) {
            dfs(x)
        }
        E[n] = cnt
    }

    const temp = input[1].split(' ').map(Number)
    for (let i = 1; i < N; ++i) {
        G[temp[i]].push(i+1)
    }

    dfs(1)

    for (let i = 0; i < M; ++i) {
        const tmp = input[i+2].split(' ').map(Number)

        if (tmp[0] == 1) {
            U(A[tmp[1]], tmp[2])
        }
        else {
            console.log(S(E[tmp[1]]) - S(A[tmp[1]]-1))
        }
    }
})