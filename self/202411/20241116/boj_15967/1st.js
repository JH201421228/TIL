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
    const I = (s, e, idx) => {
        if (s === e) {
            tree[idx] = arr[s]
            return arr[s]
        }

        const mid = Math.floor((s+e)/2)

        tree[idx] = I(s, mid, idx*2) + I(mid+1, e, idx*2+1)

        return tree[idx]
    }

    const lazy_U = (s, e, idx) => {
        if (lazy[idx] !== 0) {
            tree[idx] += (e-s+1) * lazy[idx]
            if (s !== e) {
                lazy[idx*2] += lazy[idx]
                lazy[idx*2+1] += lazy[idx]
            }
            lazy[idx] = 0
        }
    }

    const S = (s, e, idx, l, r) => {
        lazy_U(s, e, idx)

        if (s > r || e < l) {
            return 0
        }

        if (s >= l && e <= r) {
            return tree[idx]
        }

        const mid = Math.floor((s+e)/2)

        return S(s, mid, idx*2, l, r) + S(mid+1, e, idx*2+1, l, r)
    }

    const U = (s, e, idx, l, r, v) => {
        lazy_U(s, e, idx)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            lazy[idx] += v
            lazy_U(s, e, idx)
            return
        }

        const mid = Math.floor((s+e)/2)

        U(s, mid, idx*2, l, r, v)
        U(mid+1, e, idx*2+1, l, r, v)
        tree[idx] = tree[idx*2] + tree[idx*2+1]
    }

    const [N, Q1, Q2] = input[0].split(" ").map(Number)

    const arr = [0, ...input[1].split(" ").map(Number)]
    const tree = Array(4*N+1).fill(0)
    const lazy = Array(4*N+1).fill(0)

    I(1, N, 1)

    for (let i = 0; i < Q1 + Q2; ++i) {
        const temp = input[i+2].split(" ").map(Number)

        if (temp[0] === 1) {
            console.log(S(1, N, 1, temp[1], temp[2]))
        }
        else {
            U(1, N, 1, temp[1], temp[2], temp[3])
        }
    }
})