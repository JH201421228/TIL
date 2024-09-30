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
    const lazy_U = (s, e, tree_idx) => {
        if (lazy[tree_idx] != 0) {
            tree[tree_idx] += (e-s+1) * lazy[tree_idx]
            if (s != e) {
                lazy[tree_idx*2] += lazy[tree_idx]
                lazy[tree_idx*2+1] += lazy[tree_idx]
            }
            lazy[tree_idx] = 0
        }
    }

    const S = (s, e, tree_idx, idx) => {
        lazy_U(s, e, tree_idx)

        if (s > idx || e < idx) {
            return 0
        }

        if (s === e) {
            return tree[tree_idx]
        }

        const mid = Math.floor((s + e) / 2)

        return S(s, mid, tree_idx*2, idx) + S(mid+1, e, tree_idx*2+1, idx)
    }

    const U = (s, e, tree_idx, l, r, v) => {
        lazy_U(s, e, tree_idx)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            lazy[tree_idx] += v
            lazy_U(s, e, tree_idx)
            return
        }

        const mid = Math.floor((s + e) / 2)

        U(s, mid, tree_idx*2, l, r, v)
        U(mid+1, e, tree_idx*2+1, l, r, v)

        tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1]
    }

    const MAX = 100000
    const tree = Array(4*MAX+1).fill(0)
    const lazy = Array(4*MAX+1).fill(0)

    const N = Number(input[0])

    for (let i = 0; i < N; ++i) {
        const temp = input[i+1].split(' ').map(Number)
        
        console.log(S(1, MAX, 1, temp[0]) + S(1, MAX, 1, temp[1]))

        U(1, MAX, 1, temp[0], temp[1], 1)
        U(1, MAX, 1, temp[0], temp[0], -S(1, MAX, 1, temp[0]))
        U(1, MAX, 1, temp[1], temp[1], -S(1, MAX, 1, temp[1]))
    }
})