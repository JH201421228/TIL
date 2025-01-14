const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", l => {
    input.push(l)
})

rl.on("close", () => {
    const G = Array.from({length: 5001}, () => [])
    const V = Array(5001).fill(0)
    const F = Array(5001).fill(0)
    let S = []

    let O = 0, cnt = 0

    const Vt = Array(5001).fill(0)
    const Vc = Array(5001).fill(0)

    let ans_list = []

    function scc(n) {
        V[n] = ++O
        let p = O
        S.push(n)

        for (let x of G[n]) {
            if (V[x] === 0) {
                p = Math.min(scc(x), p)
            }
            else if (F[x] === 0) {
                p = Math.min(V[x], p)
            }
        }

        if (p === V[n]) {
            ++cnt
            while (S.length > 0) {
                const o = S.pop()
                F[o] = cnt
                if (o === n) {
                    break
                }
            }
        }

        return p
    }

    function dfs(n, flag) {
        Vt[n] = 1

        for (let x of G[n]) {
            if (Vt[x] === 0) {
                if (F[x] !== flag) return false

                if (!dfs(x, flag)) return false
            }
        }

        return true
    }

    while (true) {
        const NM = input[z++].split(' ').map(Number)

        if (NM[0] === 0) break; const [N, M] = NM

        V.fill(0)
        F.fill(0)
        S = []
        O = 0
        cnt = 0

        for (let i = 0; i < N+1; ++i) G[i] = []

        const temp = input[z++].split(' ').map(Number)

        for (let i = 0; i < M; ++i) {
            G[temp[i*2]].push(temp[i*2+1])
        }

        for (let i = 1; i < N+1; ++i) {
            if (V[i] === 0) {
                scc(i)
            }
        }

        Vc.fill(0)
        ans_list = []

        for (let i = 1; i < N+1; ++i) {
            if (Vc[F[i]] === 0) {
                Vc[F[i]] = 1
                Vt.fill(0)
                if (dfs(i, F[i])) ans_list.push(F[i])
            }
        }

        const ans = []
        for (let i = 1; i < N+1; ++i) {
            if (ans_list.includes(F[i])) {
                ans.push(i)
            }
        }
        
        console.log(...ans)
    }
})