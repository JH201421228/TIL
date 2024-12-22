const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0
let last_ans = 0

rl.on("line", line => {
    input.push(line)
})

rl.on("close", () => {
    const merge = (X, Y) => {
        let i = 0, j = 0, x = X.length, y = Y.length
        const res = []

        while (i < x && j < y) {
            if (X[i] > Y[j]) {
                res.push(Y[j++])
            }
            else {
                res.push(X[i++])
            }
        }

        while (i < x) res.push(X[i++]); 
        while (j < y) res.push(Y[j++]); 

        return res
    }

    const I = (s, e, idx) => {
        if (s == e) {
            T[idx].push(arr[s])

            return T[idx]
        }

        const mid = (s+e) >> 1

        T[idx] = merge(I(s, mid, idx<<1), I(mid+1, e, idx<<1|1))
        return T[idx]
    }

    const count = (X, v) => {
        let s = 0, e = X.length-1

        while (s <= e) {
            const mid = (s+e) >> 1

            if (X[mid] > v) {
                e = mid-1
            }
            else {
                s = mid+1
            }
        }

        return X.length-e-1
    }

    const S = (s, e, idx, l, r, v) => {
        if (s > r || e < l) {
            return 0
        }

        if (s >= l && e <= r) {
            return count(T[idx], v)
        }

        const mid = (s+e) >> 1

        return S(s, mid, idx<<1, l, r, v) + S(mid+1, e, idx<<1|1, l, r, v)
    }

    const N = Number(input[z++])

    const arr = [0, ...input[z++].split(' ').map(Number)]
    const T = Array.from({length: 4*N+1}, () => [])

    I(1, N, 1)

    const M = Number(input[z++])

    for (let i = 0; i < M; ++i) {
        let [a, b, c] = input[z++].split(' ').map(Number)
        a ^= last_ans
        b ^= last_ans
        c ^= last_ans

        last_ans = S(1, N, 1, a, b, c)
        console.log(last_ans)
    }
})