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
    const MOD = 1000000007

    const I = (s, e, tree_idx) => {
        if (s === e) {
            tree[tree_idx] = arr[s]
            return arr[s]
        }

        const mid = Math.floor((s + e) / 2)

        tree[tree_idx] = (I(s, mid, tree_idx*2) + I(mid+1, e, tree_idx*2+1)) % MOD

        return tree[tree_idx]
    }

    const lazy_U = (s, e, tree_idx) => {
        if (lazy[tree_idx][0] != 1 || lazy[tree_idx][1] != 0) {
            tree[tree_idx] = (tree[tree_idx] * lazy[tree_idx][0] + (e-s+1) * lazy[tree_idx][1]) % MOD
            if (s != e) {
                lazy[tree_idx*2][0] = (lazy[tree_idx*2][0] * lazy[tree_idx][0]) % MOD
                lazy[tree_idx*2][1] = (lazy[tree_idx*2][1] * lazy[tree_idx][0] + lazy[tree_idx][1]) % MOD
                lazy[tree_idx*2+1][0] = (lazy[tree_idx*2+1][0] * lazy[tree_idx][0]) % MOD
                lazy[tree_idx*2+1][1] = (lazy[tree_idx*2+1][1] * lazy[tree_idx][0] + lazy[tree_idx][1]) % MOD
            }
            lazy[tree_idx][0] = 1
            lazy[tree_idx][1] = 0
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

        return (S(s, mid, tree_idx*2, l, r) + S(mid+1, e, tree_idx*2+1, l, r)) % MOD
    }

    const U = (s, e, tree_idx, l, r, v1, v2) => {
        lazy_U(s, e, tree_idx)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            lazy[tree_idx][0] = (lazy[tree_idx][0] * v1) % MOD
            lazy[tree_idx][1] = (lazy[tree_idx][1] * v1 + v2) % MOD

            lazy_U(s, e, tree_idx)

            return
        }

        const mid = Math.floor((s + e) / 2)

        U(s, mid, tree_idx*2, l, r, v1, v2);
        U(mid+1, e, tree_idx*2+1, l, r, v1, v2);

        tree[tree_idx] = (tree[tree_idx*2] + tree[tree_idx*2+1]) % MOD
    }

    const N = Number(input[0])

    const arr = [0, ...input[1].split(' ').map(Number)]
    const tree = Array(4*N+1).fill(0)
    const lazy = Array.from({length: 4*N+1}, () => { return ([1, 0])})

    const M = Number(input[2])

    I(1, N, 1)

    for (let i = 0; i < M; ++i) {
        const temp = input[i+3].split(' ').map(Number)

        if (temp[0] === 1) {
            U(1, N, 1, temp[1], temp[2], 1, temp[3])
        }
        else if (temp[0] === 2) {
            U(1, N, 1, temp[1], temp[2], temp[3], 0)
        }
        else if (temp[0] === 3) {
            U(1, N, 1, temp[1], temp[2], 0, temp[3])
        }
        else {
            console.log(S(1, N, 1, temp[1], temp[2]))
        }
    }
})