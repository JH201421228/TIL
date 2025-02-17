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
    const T = Number(input[z++])

    function B(n, G, V, C) {
        for (let x of G[n]) {
            if (V[x] === 1) continue
            V[x] = 1

            if (C[x] === 0 || B(C[x], G, V, C)) {
                C[x] = n
                return true
            }
        }

        return false
    }

    for (let zz = 0; zz < T; ++zz) {
        console.log(`Data Set ${zz+1}:`)
        
        const [M, N] = input[z++].split(' ').map(Number)
        const G = Array.from({length: N+1}, () => [])
        
        for (let _ = 0; _ < N; ++_) {
            const temp = input[z++].split(' ').map(Number)
            for (let idx = 1; idx < temp[0]+1; ++idx) {
                G[_+1].push(temp[idx])
            }
        }

        const C = Array(M+1).fill(0)
        let ans = 0
        for (let n = 1; n < N+1; ++n) {
            const V = Array(M+1).fill(0)
            if (B(n, G, V, C)) {
                ++ans
            }
        }

        console.log(ans, '\n')
    }
})