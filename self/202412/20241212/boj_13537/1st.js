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
        let i = 0, j = 0
        const x = X.length, y = Y.length

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

    const count = (X, k) => {
        let s = 0, e = X.length-1

        while (s <= e) {
            const mid = (s+e) >> 1

            if (X[mid] > k) {
                e = mid-1
            }
            else {
                s = mid+1
            }
        }

        return X.length-s
    }

    const S = (s, e, idx, l, r, k) => {
        if (s > r || e < l) {
            return 0
        }

        if (s >= l && e <= r) {
            return count(T[idx], k)
        }

        const mid = (s+e) >> 1

        return S(s, mid, idx<<1, l, r, k) + S(mid+1, e, idx<<1|1, l, r, k)
    }

    const N = Number(input[z++])

    const arr = [0, ...input[z++].split(" ").map(Number)]
    const T = Array.from({length: 4*N+1}, () => [])

    I(1, N, 1)

    const M = Number(input[z++])

    for (let i = 0; i < M; ++i) {
        const [a, b, c] = input[z++].split(" ").map(Number)

        console.log(S(1, N, 1, a, b, c))
    }
})