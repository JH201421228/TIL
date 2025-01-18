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
    function scc(n) {
        let p = ++O
        V[n] = O
        S.push(n)

        for (let x of G[n]) {
            if (V[x] === 0) {
                p = Math.min(p, scc(x))
            }
            else if (F[x] === 0) {
                p = Math.min(p, V[x])
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

    const [N, M] = input[z++].split(" ").map(Number)
    const interset = [[]]
    const prefer = [[]]
    const leafs = Array.from({length: 500001}, () => [])
    const G = Array.from({length: 2*N+1}, () => [])
    const V = Array(2*N+1).fill(0)
    const F = Array(2*N+1).fill(0)
    const S = []

    let O = 0
    let cnt = 0

    for (let i = 0; i < N; ++i) {
        interset.push([0, ...input[z++].split(" ").map(Number)])
    }

    for (let i = 1; i < N+1; ++i) {
        const [a, b] = input[z++].split(" ").map(Number)

        prefer.push([a, b])
        leafs[a].push([i, 0])
        leafs[b].push([i, 1])
    }

    for (let leaf of leafs) {
        const n = leaf.length

        for (let i = 0; i < n; ++i) {
            for (let j = i+1; j < n; ++j) {
                const an = leaf[i][0] + N*leaf[i][1]
                const bn = leaf[j][0] + N*leaf[j][1]

                if (an <= N && bn <= N) {
                    G[an].push(bn+N)
                    G[bn].push(an+N)
                }
                else if (an > N && bn <= N) {
                    G[an].push(bn+N)
                    G[bn].push(an-N)
                }
                else if (an <= N && bn > N) {
                    G[an].push(bn-N)
                    G[bn].push(an+N)
                }
                else {
                    G[an].push(bn-N)
                    G[bn].push(an-N)    
                }
            }
        }
    }
    
    for (let i = 0; i < M; ++i) {
        const [a, b, c] = input[z++].split(" ").map(Number)
        
        for (let aleaf of leafs[a]) {
            for (let bleaf of leafs[b]) {
                if (interset[aleaf[0]][c] !== interset[bleaf[0]][c]) {
                    const an = aleaf[0] + N*aleaf[1]
                    const bn = bleaf[0] + N*bleaf[1]
                    
                    if (an <= N && bn <= N) {
                        G[an].push(bn+N)
                        G[bn].push(an+N)
                    }
                    else if (an > N && bn <= N) {
                        G[an].push(bn+N)
                        G[bn].push(an-N)
                    }
                    else if (an <= N && bn > N) {
                        G[an].push(bn-N)
                        G[bn].push(an+N)
                    }
                    else {
                        G[an].push(bn-N)
                        G[bn].push(an-N)    
                    }
                }
            }
        }
    }

    for (let n = 1; n < 2*N+1; ++n) {
        if (V[n] === 0) {
            scc(n)
        }
    }

    const ans_list = []
    for (let n = 1; n < N+1; ++n) {
        if (F[n] === F[n+N]) {
            console.log("NO")
            process.exit(0)
        }
        else if (F[n] > F[n+N]) {
            ans_list.push([prefer[n][1], n])
        }
        else {
            ans_list.push([prefer[n][0], n])
        }
    }
    
    ans_list.sort((a, b) => a[0] - b[0])

    console.log("YES")
    console.log(...ans_list.map((ans) => ans[1]))
})