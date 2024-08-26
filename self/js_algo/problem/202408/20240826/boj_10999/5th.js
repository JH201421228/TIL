const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const input = []

rl.on('line', (line) => {
    input.push(line)
});

rl.on('close', () => {

    const I = (s, e, tree_idx) => {
        if (s === e) {
            tree[tree_idx] = arr[s]
            return arr[s]
        }

        const mid = Math.floor((s + e) / 2)

        tree[tree_idx] = I(s, mid, tree_idx * 2) + I(mid + 1, e, tree_idx * 2 + 1)
        return tree[tree_idx]
    };

    const U_lazy = (s, e, tree_idx) => {
        if (lazy[tree_idx] !== 0n) {
            tree[tree_idx] += BigInt(e - s + 1) * lazy[tree_idx]
            if (s !== e) {
                lazy[tree_idx * 2] += lazy[tree_idx]
                lazy[tree_idx * 2 + 1] += lazy[tree_idx]
            }
            lazy[tree_idx] = 0n
        }
    };

    const S = (s, e, tree_idx, l, r) => {
        U_lazy(s, e, tree_idx)

        if (s > r || e < l) {
            return 0n
        }

        if (s >= l && e <= r) {
            return tree[tree_idx]
        }

        const mid = Math.floor((s + e) / 2)

        return S(s, mid, tree_idx * 2, l, r) + S(mid + 1, e, tree_idx * 2 + 1, l, r)
    };

    const U = (s, e, tree_idx, l, r, c) => {
        U_lazy(s, e, tree_idx)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            tree[tree_idx] += BigInt(e - s + 1) * c
            if (s !== e) {
                lazy[tree_idx * 2] += c
                lazy[tree_idx * 2 + 1] += c
            }
            return;
        }

        const mid = Math.floor((s + e) / 2)

        U(s, mid, tree_idx * 2, l, r, c)
        U(mid + 1, e, tree_idx * 2 + 1, l, r, c)

        tree[tree_idx] = tree[tree_idx * 2] + tree[tree_idx * 2 + 1]
    };

    const [N, M, K] = input[0].split(' ').map(Number)

    const arr = Array(N + 1).fill(0n)
    const tree = Array(4 * N + 1).fill(0n)
    const lazy = Array(4 * N + 1).fill(0n)

    for (let i = 0; i < N; ++i) {
        arr[i + 1] = BigInt(input[i + 1])
    }

    I(1, N, 1)

    for (let i = 0; i < M + K; ++i) {
        const temp = input[N + 1 + i].split(' ')

        if (Number(temp[0]) === 1) {
            U(1, N, 1, Number(temp[1]), Number(temp[2]), BigInt(temp[3]))
        } else {
            console.log(S(1, N, 1, Number(temp[1]), Number(temp[2])).toString())
        }
    }
})
