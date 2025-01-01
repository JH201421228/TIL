const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

const input = []
let z = 0

rl.on("line", line => {
    input.push(line)
})

rl.on("close", () => {
    function set_edge(u ,v) {
        G[u].push(v)
        G[v].push(u)
        C[u][v] = 1
    }

    function bfs(src, sink) {
        const q = [src]
        L.fill(-1)
        L[src] = 0

        while (q.length > 0) {
            const u = q.shift()

            for (let v of G[u]) {
                if (L[v] === -1 && C[u][v] > 0) {
                    L[v] = L[u]+1
                    q.push(v)
                }
            }   
        }

        return L[sink] !== -1
    }

    function dfs(u, sink) {
        if (u === sink) {
            return 1
        }

        for (let v of G[u]) {
            if (L[v] === L[u]+1 && C[u][v]) {
                const k = dfs(v, sink)
                if (k === 1) {
                    C[u][v] = 0
                    C[v][u] = 1
                    return 1
                }
            }
        }

        return 0
    }

    function get_ans(src, sink) {
        let ans = 0

        while (bfs(src, sink)) {
            while (true) {
                const flow = dfs(src, sink)
                if (flow === 0) {
                    break
                }
                ans += flow
            }
        }

        return ans
    }

    const [N, P] = input[z++].split(' ').map(Number)
    const G = Array.from({length: N+1}, () => [])
    const C = Array.from({length: N+1}, () => Array(N+1).fill(0))
    const L = Array(N+1).fill(-1)

    for (let i = 0; i < P; ++i) {
        const [u, v] = input[z++].split(' ').map(Number)

        set_edge(u, v)
    }

    console.log(get_ans(1, 2))
})