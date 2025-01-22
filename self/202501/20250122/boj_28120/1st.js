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

rl.on("close", function () {
    function B(n) {
        for (let x of G[n]) {
            if (V[x] !== 0) {continue}
            V[x] = 1

            if (C[x] === 0 || B(C[x])) {
                C[x] = n
                return true
            }
        }

        return false
    }

    const [N, K, X] = input[z++].split(' ').map(Number)
    const G = Array.from({length: N+1}, () => [])
    const V = Array(16).fill(0)
    const C = Array(16).fill(0)

    const W = Array.from({length: N}, () => [0])
    for (let i = 0; i < N; ++i) {
        W[i].push(i+1)
        W[i].push(...input[z++].split(' ').map(Number))
    }

    const temp = input[z++].split(' ').map(Number)
    for (let i = 0; i < N; ++i) {
        W[i][0] = -temp[i]
    }

    W.sort((a, b) => a[0] - b[0])

    for (let i = 1; i < N+1; ++i) {
        const n = W[i-1].length
        for (let j = 3; j < n; ++j) {
            for (let k = 0; k < X; ++k) {
                G[i].push((W[i-1][j]-1)*X+1+k)
            }
        }
    }

    for (let i = 1; i < N+1; ++i) {
        V.fill(0)
        B(i)
    }

    const ans_list = Array.from({length: K}, () => [])
    for (let i = 1; i < 16; ++i) {
        if (C[i] !== 0) {
            ans_list[Math.floor((i-1)/X)].push(W[C[i]-1][1])
        }
    }

    for (let ans of ans_list) {
        console.log(ans.length, ...ans)
    }
})