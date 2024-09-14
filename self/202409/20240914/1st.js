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
    const I = (s, e, tree_idx) => {
        if (s === e) {
            tree[tree_idx] = arr[s]
            return arr[s]
        }

        const mid = Math.floor((s + e) / 2)
        
        tree[tree_idx] = I(s, mid, tree_idx*2) ^ I(mid+1, e, tree_idx*2+1)
        
        return tree[tree_idx]
    }

    const lazy_U = (s, e, tree_idx) => {
        if (lazy[tree_idx] != 0) {
            if ((e-s+1) % 2 === 1) {
                tree[tree_idx] ^= lazy[tree_idx]
            }
            if (s != e) {
                lazy[tree_idx*2] ^= lazy[tree_idx]
                lazy[tree_idx*2+1] ^= lazy[tree_idx]
            }
            lazy[tree_idx] = 0
        }
    }

    const S = (s, e, tree_idx, l, r) => {
        lazy_U(s, e, tree_idx)

        if (s > r || e < l) {
            return 0
        }

        if (s >= l && e <= r) {
            return tree[tree_idx]
        }

        const mid = Math.floor((s + e) / 2)

        return S(s, mid, tree_idx*2, l, r) ^ S(mid+1, e, tree_idx*2+1, l, r)
    }

    const U = (s, e, tree_idx, l, r, val) => {
        lazy_U(s, e, tree_idx)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            if ((e-s+1) % 2 === 1) {
                tree[tree_idx] ^= val
            }
            if (s != e) {
                lazy[tree_idx*2] ^= val
                lazy[tree_idx*2+1] ^= val
            }
            return
        }

        const mid = Math.floor((s + e) / 2)

        U(s, mid, tree_idx*2, l, r, val)
        U(mid+1, e, tree_idx*2+1, l, r, val)

        tree[tree_idx] = tree[tree_idx*2] ^ tree[tree_idx*2+1]
    }

    const N = Number(input[0])

    const tree = Array(4*N+1).fill(0)
    const lazy = Array(4*N+1).fill(0)

    const arr = [0, ...input[1].split(" ").map(Number)]

    I(1, N, 1)

    const M = Number(input[2])

    for (let i = 0; i < M; ++i) {
        const temp = input[i+3].split(" ").map(Number)

        if (temp[0] === 1) {
            U(1, N, 1, temp[1]+1, temp[2]+1, temp[3])
        }
        else {
            console.log(S(1, N, 1, temp[1]+1, temp[2]+1))
        }
    }
})