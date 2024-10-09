const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {
    const T = Number(input[z]); ++z;

    for (let i = 0; i < T; ++i) {
        const [N, M] = input[z].split(" ").map(Number); ++z;

        const G = []

        for (let j = 0; j < N; ++j) {
            G.push([])
        }

        for (let j = 0; j < M; ++j) {
            const [u, v] = input[z].split(" ").map(Number); ++z;

            G[u].push(v)
        }
        ++z

        const V = Array(N).fill(-1)
        const F = Array(N).fill(0)
        const S = []
        let O = 0
        let GN = 0

        const find_scc = n => {
            ++O
            let p = V[n] = O
            S.push(n)
    
            for (let x of G[n]) {
                if (V[x] === -1) {
                    p = Math.min(p, find_scc(x))
                }
                else if (F[x] === 0) {
                    p = Math.min(p, V[x])
                }
            }
    
            if (p === V[n]) {
                ++GN
    
                while (S.length > 0) {
                    const out = S.pop()
                    F[out] = GN
    
                    if (out === n) {
                        break
                    }
                }
            }
    
            return p
        }

        for (let j = 0; j < N; ++j) {
            if (V[j] === -1) {
                find_scc(j)
            }
        }

        const C = Array(GN+1).fill(0)

        for (let j = 0; j < N; ++j) {
            for (let k of G[j]) {
                if (F[j] !== F[k]) {
                    C[F[k]] = F[j]
                }
            }
        }

        const temp = []

        for (let j = 1; j < GN+1; ++j) {
            if (C[j] === 0) {
                temp.push(j)
            }
        }

        if (temp.length > 1) {
            console.log("Confused")
        }
        else {
            for (let j = 0; j < N; ++j) {
                if (F[j] === temp[0]) {
                    console.log(j)
                }
            }
        }
        console.log()
    }
})