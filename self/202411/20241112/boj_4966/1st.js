const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {
    let z = 0
    const res = []
    const b = Array(501).fill(0)
    const r = Array(501).fill(0)
    const G = Array.from({length: 501}, () => [])
    const C = Array(501).fill(0)
    const V = Array(501).fill(0)

    const is_disjoint = (a, b) => {
        if (b === 1) {
            return false
        }

        if (a % b !== 0) {
            return is_disjoint(b, a % b)
        }
        else {
            return true
        }
    }

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

    while (true) {
        const [M, N] = input[z].split(" ").map(Number)
        ++z

        if (M === 0 && N === 0) {
            break
        }
        
        let idx = 0

        while (idx < M) {
            const temp = input[z].split(" ").map(Number)
            ++z

            for (let m of temp) {
                b[++idx] = m
            }
        }

        idx = 0

        while (idx < N) {
            const temp = input[z].split(" ").map(Number)
            ++z

            for (let n of temp) {
                r[++idx] = n
            }
        }

        for (let i = 1; i < M+1; ++i) {
            let x = b[i]
            G[i] = []
            for (let j = 1; j < N+1; ++j) {
                let y = r[j]

                if (is_disjoint(Math.max(x, y), Math.min(x, y))) {
                    G[i].push(j)
                }
            }
        }

        let ans = 0

        C.fill(0)
        for (let i = 1; i < M+1; ++i) {
            V.fill(0)

            if (B(i)) {
                ++ans
            }
        }

        res.push(ans)
    }
    
    for (let v of res) {
        console.log(v)
    }
})