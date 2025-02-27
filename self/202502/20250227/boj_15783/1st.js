const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
const S = []
let z = 0
let O = 0

rl.on("line", l => {
    input.push(l)
})

rl.on("close", () => {
    function scc(n) {
        let p = ++O
        V[n] = O
        S.push(n)

        for (let x of G[n]) {
            if (V[x] === 0) p = Math.min(p, scc(x))
            else if (F[x] === 0) p = Math.min(p, V[x])
        }

        if (V[n] === p) {
            while (S.length > 0) {
                const o = S.pop()
                F[o] = p
                if (o === n) break
            }
        }

        return p
    }

    const [N, M] = input[z++].split(' ').map(Number)

    const G = Array.from({length: N+1}, () => [])
    const V = Array(N+1).fill(0)
    const F = Array(N+1).fill(0)

    for (let i = 0; i < M; ++i) {
        const [u, v] = input[z++].split(' ').map(Number)
        G[u+1].push(v+1)
    }

    for (let n = 1; n < N+1; ++n) {
        if (V[n] === 0) scc(n)
    }

    checker = {}
    for (let n = 1; n < N+1; ++n) {
        checker[F[n]] = new Set()
    }

    for (let s = 1; s < N+1; ++s) {
        for (let e of G[s]) {
            if (F[s] !== F[e]) checker[F[e]].add(F[s])
        }
    }

    let ans = 0
    for (const[k, v] of Object.entries(checker)) {
        if (v.size === 0) ++ans
    }

    console.log(ans)
})