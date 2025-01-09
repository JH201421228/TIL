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
    function I(s, e, idx) {
        if (s === e) {
            T[idx] = arr[s]
            return arr[s]
        }

        const mid = (s+e) >> 1

        T[idx] = Math.min(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1))

        return T[idx]
    }

    function lazy_U(s, e, idx) {
        if (L[idx] !== 0) {
            T[idx] += L[idx]
            if (s !== e) {
                L[idx<<1] += L[idx]
                L[idx<<1|1] += L[idx]
            }
            L[idx] = 0
        }
    }

    function U(s, e, idx, l, r, v) {
        lazy_U(s, e, idx)

        if (s > r || e < l) {
            return T[idx]
        }

        if (s >= l && e <= r) {
            L[idx] += v
            lazy_U(s, e, idx)
            return T[idx]
        }

        const mid = (s+e) >> 1

        T[idx] = Math.min(U(s, mid, idx<<1, l, r, v), U(mid+1, e, idx<<1|1, l, r, v))

        return T[idx]
    }

    let ans = 0

    const S = input[z++].split('')
    const N = S.length
    const M = Number(input[z++])

    const arr = [0]

    const T = Array(4*N+1).fill(0)
    const L = Array(4*N+1).fill(0)

    for (let i = 0; i < N; ++i) {
        if (S[i] === '(') {
            arr[i+1] = arr[i] + 1
        }
        else {
            arr[i+1] = arr[i] - 1
        }
    }

    let V = arr[N]

    I(1, N, 1)

    for (let i = 0; i < M; ++i) {
        const q = Number(input[z++])
        let k = 0;

        if (S[q-1] === '(') {
            S[q-1] = ')'
            V -= 2
            k = U(1, N, 1, q, N, -2)
        }
        else {
            S[q-1] = '('
            V += 2
            k = U(1, N, 1, q, N, 2)
        }

        if (V === 0 && k >= 0) {
            ++ans
        }
    }

    console.log(ans)
})