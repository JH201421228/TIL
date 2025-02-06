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
    function U(idx) {
        while (idx < N+1) {
            ++T[idx]
            idx += (idx & -idx)
        }
    }

    function S(idx) {
        let res = 0
        while (idx > 0) {
            res += T[idx]
            idx -= (idx & -idx)
        }

        return res
    }

    const N = Number(input[z++])
    const arr = []
    const T = Array(N+1).fill(0)

    for (let i = 0; i < N; ++i) {
        arr.push([Number(input[z++]), i])
    }

    arr.sort((a, b) => a[0] - b[0])

    for (let i = 0; i < N; ++i) {
        arr[i][0] = i+1
    }

    arr.sort((a, b) => a[1] - b[1])

    for (let i = 0; i < N; ++i) {
        console.log(i+1-S(arr[i][0]))
        U(arr[i][0])
    }
})