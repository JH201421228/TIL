const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {
    let O, V, F, U, G, result, S

    function init() {
        while (true) {
            const N = Number(input[z++])
            if (N === 0) {
                break
            }

            solve(N)
        }

        return
    }

    function scc(n) {
        let p = ++O
        V[n] = O
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
            const temp = []

            while (S.length > 0) {
                let o = S.pop()
                F[o] = 1
                temp.push(String.fromCharCode(o + 64))

                if (o === n) {
                    temp.sort()
                    result.push(temp)
                    break
                }
            }
        }

        return p
    }

    function solve(N) {
        O = 0
        V = Array(27).fill(0)
        F = Array(27).fill(0)
        U = Array(27).fill(0)
        G = Array.from({length: 27}, () => [])
        result = []
        S = []

        for (let i = 0; i < N; ++i) {
            const choices = input[z++].split(' ').map(c => c.charCodeAt(0) - 'A'.charCodeAt(0) + 1)
            for (let idx = 0; idx < 5; ++idx) {
                G[choices[idx]].push(choices[5])
                U[choices[idx]] = 1
            }
        }

        for (let n = 1; n < 27; ++n) {
            if (V[n] === 0 && U[n] === 1) {
                scc(n)
            }
        }

        result.sort((a, b) => a[0].localeCompare(b[0]))

        for (let temp of result) {
            console.log(...temp)
        }
        console.log()

        return
    }

    init()
})