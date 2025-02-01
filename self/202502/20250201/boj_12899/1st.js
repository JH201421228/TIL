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
    function U(s, e, idx, v) {
        if (s === e && s === v) {
            ++T[idx]
            return T[idx]
        }

        if (s > v || e < v) {
            return T[idx]
        }

        const mid = (s+e) >> 1

        T[idx] = U(s, mid, idx<<1, v) + U(mid+1, e, idx<<1|1, v)

        return T[idx]
    }

    function D(s, e, idx, v) {
        if (s === e) {
            --T[idx]
            return s
        }

        const mid = (s+e) >> 1
        let res

        if (T[idx<<1] >= v) {
            res = D(s, mid, idx<<1, v)
        }
        else {
            res = D(mid+1, e, idx<<1|1, v-T[idx<<1])
        }

        --T[idx]
        
        return res
    }
    
    const N = Number(input[z++])
    const T = Array(2000001 * 4 + 1).fill(0)

    for (let i = 0; i < N; ++i) {
        const [t, x] = input[z++].split(' ').map(Number)

        if (t === 1) {
            U(1, 2000000, 1, x)
        }
        else {
            console.log(D(1, 2000000, 1, x))
        }
    }
    
    return
})