const readline = require('readline');

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
    const V = Array(N+1).fill(0)
    const F = Array(N+1).fill(0)
    const S = []
    let cnt = 0
    let O = 0

    const scc = n => {
        let p = V[n] = ++O
        S.push(n)

        for (let x of G[n]) {
            if (V[x] === 0) {
                p = Math.min(p, scc(x))
            }
            else if (F[x] === 0) {
                p = Math.min(p, V[x])
            }
        }

        if (p === V[n]) {
            ++cnt

            while (S.length > 0) {
                const out = S.pop()
                F[S] = cnt

                if (n == out) {
                    break
                }
            }
        }

        return p
    }

    for (let i = 0; i < M; ++i) {
        const [u, v] = input[i+1].split(" ").map(Number)

        G[u].push(v)
    }

    for (let i = 1; i < N+1; ++i) {
        if (V[i] === 0) {
            scc(i)
        }
    }

    if (cnt === 1) {
        console.log("Yes")
    }
    else {
        console.log("No")
    }
})