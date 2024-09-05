const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on('line', l => {
    input.push(l)
})

rl.on('close', () => {
    const [N, M] = input[0].split(' ').map(Number)

    const fake = Array(4*N+1).fill(0)
    const lazy = Array(4*N+1).fill(0)
    const tree = Array(4*N+1).fill(0)

    const I = (s, e, tree_idx) => {
        if (s === e) {
            fake[tree_idx] = 1
            return 1
        }

        const mid = Math.floor((s + e) / 2)
        
        fake[tree_idx] = I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)
        return fake[tree_idx]
    }

    const lazy_U = (s, e, tree_idx) => {
        if (lazy[tree_idx] === 1) {
            tree[tree_idx] = fake[tree_idx] - tree[tree_idx]
            if (s != e) {
                lazy[tree_idx*2] = 1 - lazy[tree_idx*2]
                lazy[tree_idx*2+1] = 1 - lazy[tree_idx*2+1]
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

        return S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r)
    }

    const U = (s, e, tree_idx, l, r) => {
        lazy_U(s, e, tree_idx)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            tree[tree_idx] = fake[tree_idx] - tree[tree_idx]
            if (s != e) {
                lazy[tree_idx*2] = 1 - lazy[tree_idx*2]
                lazy[tree_idx*2+1] = 1 - lazy[tree_idx*2+1]
            }
            return
        }

        const mid = Math.floor((s + e) / 2)

        U(s, mid, tree_idx*2, l, r)
        U(mid+1, e, tree_idx*2+1, l, r)

        tree[tree_idx] = tree[tree_idx*2] + tree[tree_idx*2+1]
    }

    I(1, N, 1)

    for (let i = 0; i < M; ++i) {
        const [o, s, t] = input[i+1].split(' ').map(Number)

        if (o === 0) {
            U(1, N, 1, s, t)
        }
        else {
            console.log(S(1, N, 1, s, t))
        }
    }
})