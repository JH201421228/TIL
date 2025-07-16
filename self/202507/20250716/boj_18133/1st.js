const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", l => input.push(l))

rl.on("close", () => {
    const [N, M] = input[z++].split(' ').map(Number)
    const V = Array(N+1).fill(0)
    const F = Array(N+1).fill(0)
    const G = Array.from({length: N+1}, () => [])
    const connect = {}
    const uniques = new Set()
    const S = []
    let O = 0
    let cnt = 0

    function scc(n) {
        let p = ++O
        V[n] = O
        S.push(n)

        for (let x of G[n]) {
            if (V[x] === 0) p = Math.min(p, scc(x));
            else if (F[x] === 0) p = Math.min(p, V[x]);
        }

        if (V[n] == p) {
            ++cnt
            
            while (S.length > 0) {
                let o = S.pop()
                F[o] = cnt

                if (o == n) break;
            }
        }

        return p
    }

    for (let i = 0; i < M; ++i) {
        const [u, v] = input[z++].split(' ').map(Number)
        G[u].push(v)
    }

    for (let n = 1; n < N+1; ++n) {
        if (V[n] === 0) scc(n);
    }

    for (let idx = 1; idx < N+1; ++idx) {
        uniques.add(F[idx])
    }

    for (let n of uniques) connect[n] = [];

    for (let n = 1; n < N+1; ++n) {
        for (let x of G[n]) {
            if (F[x] != F[n]) connect[F[x]].push(F[n]);
        }
    }

    let ans = 0

    for (let [k, v] of Object.entries(connect)) {
        if (v.length === 0) ++ans;
    }

    console.log(ans)
})