const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {
    const [N, M] = input[0].split(" ").map(Number)

    const G = Array.from({length: N+1}, () => [])
    const tree = Array(4*N+1).fill(0)
    const lazy = Array(4*N+1).fill(0)
    const A = Array(N+1).fill(0)
    const E = Array(N+1).fill(0)
    let cnt = 0

    const dfs = n => {
        A[n] = ++cnt
        for (let x of G[n]) {
            dfs(x)
        }
        E[n] = cnt
    }

    const lazy_U = (s, e, idx) => {
        if (lazy[idx] !== 0) {
            if (s === e) {
                tree[idx] += lazy[idx]
            }
            else {
                lazy[idx*2] += lazy[idx]
                lazy[idx*2+1] += lazy[idx]
            }
            lazy[idx] = 0
        }
    }

    const U = (s, e, idx, l, r, v) => {
        lazy_U(s, e, idx)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            lazy[idx] += v
            lazy_U(s, e, idx)
            return
        }

        const mid = (s+e) >> 1

        U(s, mid, idx*2, l, r, v)
        U(mid+1, e, idx*2+1, l, r, v)
    }

    const S = (s, e, idx, i) => {
        lazy_U(s, e, idx)

        if (s > i || e < i) {
            return 0
        }

        if (s === e) {
            return tree[idx]
        }

        const mid = (s+e) >> 1
        
        return S(s, mid, idx*2, i) + S(mid+1, e, idx*2+1, i)
    }

    const temp = input[1].split(" ").map(Number)
    for (let i = 1; i < N; ++i) {
        G[temp[i]].push(i+1)
    }

    dfs(1)

    for (let i = 0; i < M; ++i) {
        const temp = input[i+2].split(" ").map(Number)

        if (temp[0] === 1) {
            U(1, N, 1, A[temp[1]], E[temp[1]], temp[2])
        }
        else {
            console.log(S(1, N, 1, A[temp[1]]))
        }
    }
})