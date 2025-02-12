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
    function S(idx, T) {
        let res = 0
        
        while (idx > 0) {
            res += T[idx]
            idx -= idx & -idx
        }

        return res
    }


    function U(idx, T, N) {
        while (idx < N+1) {
            ++T[idx]
            idx += idx & -idx
        }
    }


    const C = Number(input[z++])

    for (let zz = 0; zz < C; ++zz) {
        const N = Number(input[z++])
        const islands = []
        const xs = []
        const ys = []
        const xd = {}
        const yd = {}
        const T = Array(N+1).fill(0)

        for (let i = 0; i < N; ++i) {
            const [x, y] = input[z++].split(' ').map(Number)

            islands.push([x, -y])
            xs.push(x)
            ys.push(-y)
        }
        xs.sort((a, b) => a - b)
        ys.sort((a, b) => a - b)

        let prex = 1, prey = 1
        for (let i = 0; i < N; ++i) {
            if (!(xs[i] in xd)) xd[xs[i]] = prex++
            if (!(ys[i] in yd)) yd[ys[i]] = prey++
        }

        for (let i = 0; i < N; ++i) {
            const [x, y] = islands[i]
            islands[i] = [xd[x], yd[y]]
        }
        islands.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1])

        let ans = 0n;
        for (let i = 0; i < N; ++i) {
            ans += BigInt(S(islands[i][1], T))
            U(islands[i][1], T, N)
        }

        console.log(ans.toString())
    }
})