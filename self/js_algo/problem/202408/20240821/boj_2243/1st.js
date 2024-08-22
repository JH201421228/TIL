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

    const tree = Array(4000004).fill(0)

    const S = (s, e, tree_idx, v) => {
        if (s === e) {
            return s
        }

        const mid = Math.floor((s+e) / 2)
        if (tree[tree_idx*2] >= v) {
            return S(s, mid, tree_idx*2, v)
        }
        else {
            return S(mid+1, e, tree_idx*2+1, v-tree[tree_idx*2])
        }
    }

    const U = (s, e, idx, tree_idx, c) => {
        if (idx > e || idx < s) {
            return
        }

        tree[tree_idx] += c

        if (s === e) {
            return
        }

        const mid = Math.floor((s+e) / 2)
        U(s, mid, idx, tree_idx*2, c)
        U(mid+1, e, idx, tree_idx*2+1, c)
    }

    for (let i = 1; i <= N; ++i) {
        const temp = input[i].split(' ').map(Number)
        const a = temp[0]
        if (a === 1) {
            const b = temp[1]
            const ans = S(1, 1000001, 1, b)
            console.log(ans)
            U(1, 1000001, ans, 1, -1)
        }
        else {
            const b = temp[1]
            const c = temp[2]
            U(1, 1000001, b, 1, c)
        }
    }
})