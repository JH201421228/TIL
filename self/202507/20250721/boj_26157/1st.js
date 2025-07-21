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
    const F = Array(N+1).fill(0)
    const V = Array(N+1).fill(0)
    const order = Array(N+1).fill(0)
    const G = Array.from({length: N+1}, () => [])
    const graph = Array.from({length: N+1}, () => [])
    const S = []
    const q = []
    const ans = []
    let O = 0
    let Z = 0
    let cmp = 1

    function scc(n) {
        let p = ++O
        V[n] = O
        S.push(n)

        for (let x of G[n]) {
            if (V[x] === 0) p = Math.min(p, scc(x));
            else if (F[x] === 0) p = Math.min(p, V[x]);
        }

        if (p === V[n]) {
            ++Z

            while (S.length > 0) {
                let o = S.pop()
                F[o] = Z

                if (n === o) break;
            }
        }

        return p
    }

    function generate_graph() {
        for (let n = 1; n < N+1; ++n) {
            const u = F[n]

            for (let x of G[n]) {
                const v = F[x]

                if (u === v) continue;

                graph[u].push(v)
                ++order[v];
            }
        }

        return
    }

    function topology_sort() {
        for (let idx = 1; idx < Z+1; ++idx) {
            if (order[idx] === 0) q.push(idx);
        }

        if (q.length > 1) {
            console.log(0)
            return
        }

        const res = q[0]
        while (q.length > 0) {
            if (q.length > 1) {
                console.log(0)
                return
            }

            const n = q.shift()
            for (let x of graph[n]) {
                --order[x]

                if (order[x] === 0) {
                    q.push(x)
                    ++cmp
                }
            }
        }

        if (cmp === Z) {
            for (let idx = 1; idx < N+1; ++idx) {
                if (F[idx] === res) ans.push(idx);
            }

            console.log(ans.length)
            console.log(ans.join(' '))
            return
        }
        else {
            console.log(0)
            return
        }
    }

    for (let i = 0; i < M; ++i) {
        const [u, v] = input[z++].split(' ').map(Number)
        G[u].push(v)
    }

    for (let n = 1; n < N+1; ++n) {
        if (V[n] === 0) scc(n);
    }

    generate_graph()

    topology_sort()

    return
})