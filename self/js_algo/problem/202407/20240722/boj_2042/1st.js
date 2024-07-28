const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


let input = []

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {

    const I = (s, e, idx) => {
        if (s === e) {
            tree[idx] = nums[s-1]
            return tree[idx]
        }

        const mid = Math.floor((s+e) / 2)
        tree[idx] = I(s, mid, idx*2) + I(mid+1, e, idx*2+1)
        return tree[idx]
    }

    const S = (s, e, l, r, idx) => {
        if (s > r || e < l) {
            return 0;
        }

        if (s >= l && e <= r) {
            return tree[idx]
        }

        const mid = Math.floor((s+e) / 2)
        const val = S(s, mid, l, r, idx*2) + S(mid+1, e, l, r, idx*2+1)
        return val
    }

    const U = (s, e, idx, cidx, val) => {
        if (cidx < s || cidx > e) {
            return
        }

        tree[idx] += val

        if (s === e) {
            return
        }

        const mid = Math.floor((s+e) / 2)
        U(s, mid, idx*2, cidx, val)
        U(mid+1, e, idx*2+1, cidx, val)

    }

    let idx = 0
    const [N, M, K] = input[idx++].split(' ').map(Number)
    const nums = []
    const tree = Array(4*N).fill(0)

    for (let i = 0; i < N; ++i) {
        nums.push(Number(input[idx++]))
    }

    I(1, N, 1)

    for (let i = 0; i < M+K; ++i) {
        const [a, b, c] = input[idx++].split(' ').map(Number)
        if (a === 1) {
            const v = c - nums[b-1]
            nums[b-1] = c
            U(1, N, 1, b, v)
        }
        else {
            console.log(S(1, N, b, c, 1))
        }
    }
})