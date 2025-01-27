const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", l => {
    input.push(l)
})

rl.on("close", () => {
    function B(n) {
        for (let x of G[n]) {
            if (V[x] === 1) {
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

    const [N, K] = input[z++].split(' ').map(Number)
    
    const M = []
    for (let i = 0; i < N; ++i) M.push(input[z++].split(' ').map(Number))

    const G = Array.from({length: K+1}, () => [])
    for (let i = 0; i < K; i++) {
        for (let j = 0; j < N; ++j) {
            if (M[j][K-1-i] === 1) {
                G[i+1].push(j+1)
            }
        }
    }

    const C = Array(N+1).fill(0)
    const V = Array(N+1).fill(0)

    let ans = 0
    let camera = 0

    for (let i = 1; i < K+1; ++i) {
        V.fill(0)
        if (B(i)) {
            if (ans-camera+2 > K+1-i) {
                console.log(ans)
                process.exit(0)
            }
            ans++
        }
        else {
            if (camera < ans) camera++
        }
    }
    console.log(ans)
})