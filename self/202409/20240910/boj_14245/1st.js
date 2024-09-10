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
    const N = Number(input[0])

    const arr = [0, ...input[1].split(" ").map(Number)]
    const lazy = Array(4*N+1).fill(0)

    const lazy_U = (s, e, tree_idx) => {
        if (lazy[tree_idx] != 0) {
            if (s === e) {
                arr[s] ^= lazy[tree_idx]
            }
            else {
                lazy[tree_idx*2] ^= lazy[tree_idx]
                lazy[tree_idx*2+1] ^= lazy[tree_idx]
            }
            lazy[tree_idx] = 0
        }
    }

    const S = (s, e, tree_idx, idx) => {
        lazy_U(s, e, tree_idx)

        if (idx > e || idx < s) {
            return 0
        }

        if (s === e) {
            if (s === idx) {
                return arr[s]
            }
            else {
                return 0
            }
        }

        const mid = Math.floor((s + e) / 2)

        return S(s, mid, tree_idx*2, idx) ^ S(mid+1, e, tree_idx*2+1, idx)
    }

    const U = (s, e, tree_idx, l, r, val) => {
        lazy_U(s, e, tree_idx)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            if (s === e) {
                arr[s] ^= val
            }
            else {
                lazy[tree_idx*2] ^= val
                lazy[tree_idx*2+1] ^= val
            }
            return
        }

        const mid = Math.floor((s + e) / 2)

        U(s, mid, tree_idx*2, l, r, val)
        U(mid+1, e, tree_idx*2+1, l, r, val)
    }

    const M = Number(input[2])

    for (let i = 0; i < M; ++i) {
        const temp = input[3+i].split(" ").map(Number)

        if (temp[0] === 1) {
            U(1, N, 1, temp[1]+1, temp[2]+1, temp[3])
        }
        else {
            console.log(S(1, N, 1, temp[1]+1))
        }
    }
})