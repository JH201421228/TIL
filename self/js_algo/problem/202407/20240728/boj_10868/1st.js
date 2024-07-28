const readline = require('readline')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})


let input = []
const MAXV = 1000000000

rl.on('line', line => {
    input.push(line)
})

rl.on('close', () => {
    const [N, M] = input[0].split(' ').map(Number)
    const nums = Array(N + 1).fill(0)
    const st = Array(4 * N).fill(MAXV)

    const I = (s, e, idx) => {
        if (s === e) {
            st[idx] = nums[s]
            return st[idx]
        }

        const mid = Math.floor((s+e)/2)
        st[idx] = Math.min(I(s, mid, idx*2), I(mid+1, e, idx*2+1))
        return st[idx]
    }

    const S = (s, e, l, r, idx) => {
        if (s > r || e < l) {
            return MAXV
        }

        if (s >= l && e <= r) {
            return st[idx]
        }

        const mid = Math.floor((s+e)/2)
        const val = Math.min(S(s, mid, l, r, idx*2), S(mid+1, e, l, r, idx*2+1))
        return val
    }

    for (let i = 1; i <= N; ++i) {
        nums[i] = Number(input[i])
    }

    I(1, N, 1)

    for (let i = N+1; i < N+M+1; ++i) {
        const [a, b] = input[i].split(' ').map(Number)
        console.log(S(1, N, a, b, 1))
    }
})