const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []

rl.on("line", line => {
    input.push(line)
})

rl.on("close", () => {
    const dfs = n => {
        A[n] = ++cnt
        for (let x of G[n]) {
            dfs(x)
        }
        E[n] = cnt
    }

    const lazy_U = (s, e, idx, tree, lazy) => {
        if (lazy[idx] !== 0) {
            tree[idx] += (e-s+1) * lazy[idx]
            if (s !== e) {
                lazy[idx*2] += lazy[idx]
                lazy[idx*2+1] += lazy[idx]
            }
            lazy[idx] = 0
        }
    }

    const U = (s, e, idx, l, r, v, tree, lazy) => {
        lazy_U(s, e, idx, tree, lazy)

        if (s > r || e < l) {
            return
        }

        if (s >= l && e <= r) {
            lazy[idx] += v
            lazy_U(s, e, idx, tree, lazy)
            return
        }

        const mid = (s+e) >> 1
        U(s, mid, idx*2, l, r, v, tree, lazy)
        U(mid+1, e, idx*2+1, l, r, v, tree, lazy)
        tree[idx] = tree[idx*2] + tree[idx*2+1]
    }

    const S = (s, e, idx, l, r, tree, lazy) => {
        lazy_U(s, e, idx, tree, lazy)

        if (s > r || e < l) {
            return 0
        }

        if (s >= l && e <= r) {
            return tree[idx]
        }

        const mid = (s+e) >> 1
        return S(s, mid, idx*2, l, r, tree, lazy) + S(mid+1, e, idx*2+1, l, r, tree, lazy)
    }

    const [N, M] = input[0].split(' ').map(Number)
    const A = Array(N+1).fill(0)
    const E = Array(N+1).fill(0)
    const tree1 = Array(4*N+1).fill(0)
    const tree2 = Array(4*N+1).fill(0)
    const lazy1 = Array(4*N+1).fill(0)
    const lazy2 = Array(4*N+1).fill(0)
    let cnt = 0;
    let is_down_direction = true;

    const temp = input[1].split(' ').map(Number)
    const G = Array.from({length: N+1}, () => [])

    for (let i = 1; i < N; ++i) {
        G[temp[i]].push(i+1)
    }

    dfs(1)

    for (let i = 0; i < M; ++i) {
        const tmp = input[2+i].split(' ').map(Number)

        if (tmp[0] === 1) {
            if (is_down_direction) {
                U(1, N, 1, A[tmp[1]], E[tmp[1]], tmp[2], tree1, lazy1)
            }
            else {
                U(1, N, 1, A[tmp[1]], A[tmp[1]], tmp[2], tree2, lazy2)
            }
        }
        else if (tmp[0] === 2) {
            console.log(S(1, N, 1, A[tmp[1]], A[tmp[1]], tree1, lazy1) + S(1, N, 1, A[tmp[1]], E[tmp[1]], tree2, lazy2))
        }
        else {
            is_down_direction = !is_down_direction
        }
    }
})