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
    const [N, Q] = input[0].split(' ').map(Number)

    const nums = [0]
    const tree = Array(4*N).fill(0)

    nums.push(...input[1].split(' ').map(Number))

    const I = (s, e, idx) => {
        if (s === e) {
            tree[idx] = nums[s]
            return tree[idx]
        }

        const mid = Math.floor((s+e) / 2)
        tree[idx] = I(s, mid, idx*2) + I(mid+1, e, idx*2+1)
        return tree[idx]
    }

    const S = (s, e, l, r, idx) => {
        if (s > r || e < l) {
            return 0
        }

        if (s >= l && e <= r) {
            return tree[idx]
        }

        const mid = Math.floor((s+e) / 2)
        let val = S(s, mid, l, r, idx*2) + S(mid+1, e, l, r, idx*2+1)
        return val
    }

    const U = (s, e, nums_idx, tree_idx, v) => {
        if (nums_idx > e || nums_idx < s) {
            return
        }

        tree[tree_idx] += v

        if (s === e) {
            return
        }

        const mid = Math.floor((s+e) / 2)
        U(s, mid, nums_idx, tree_idx*2, v)
        U(mid+1, e, nums_idx, tree_idx*2+1, v)
    }

    I(1, N, 1)

    for (let i = 0; i < Q; ++i) {
        const [x, y, a, b] = input[2+i].split(' ').map(Number)
        console.log(S(1, N, Math.min(x, y), Math.max(x, y), 1))
        U(1, N, a, 1, b-nums[a])
        nums[a] = b
    }
})