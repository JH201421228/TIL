const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", line => {
    input.push(line)
})

rl.on("close", () => {
    const merge = (X, Y) => {
        const res = []
        let i = 0, j = 0; const x = X.length, y = Y.length

        while (i < x && j < y) {
            if (X[i] > Y[j]) {
                res.push(Y[j++])
            }
            else {
                res.push(X[i++])
            }
        }

        while (i < x) res.push(X[i++])
        while (j < y) res.push(Y[j++])

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

            if (X[mid] < v) {
                s = mid+1
            }
            else {
                e = mid-1
            }
        }

        return s
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

    const [N, Q] = input[z++].split(' ').map(Number)

    const arr = [0, ...input[z++].split(' ').map(Number)]
    const T = Array.from({length: 4*N+1}, () => [])

    I(1, N, 1)

    for (let i = 0; i < Q; ++i) {
        const [a, b, c] = input[z++].split(' ').map(Number)

        let s = -1_000_000_000, e = 1_000_000_000

        while (s <= e) {
            const mid = (s+e) >> 1

            if (S(1, N, 1, a, b, mid) < c) {
                s = mid+1
            }
            else {
                e = mid-1
            }
        }

        console.log(e)
    }
})