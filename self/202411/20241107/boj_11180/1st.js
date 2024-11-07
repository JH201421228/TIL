const { exit } = require('process')
const readline = require('readline')

const rl  = readline.createInterface({
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
    const C = Array(N+1).fill(0)
    const V = Array(N+1).fill(0)

    const B = n => {
        for (let x of G[n]) {
            if (V[x] !== 0) {
                continue
            }
            V[x] = 1

            if (C[x] === 0 || B(C[x])) {
                C[x] = n
                return true
            }
        }

        return false
    }

    for (let i = 0; i < M; ++i) {
        const [a, b] = input[i+1].split(" ").map(Number)

        G[a].push(b)
        G[b].push(a)
    }

    for (let i = 1; i < N+1; ++i) {
        V.fill(0)
        if (!B(i)) {
            console.log('Impossible')
            exit(0)
        }
    }

    for (let i = 1; i < N+1; ++i) {
        console.log(C[i])
    }
})