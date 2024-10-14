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
    const find_scc = n => {
        let p = V[n] = O = O+1
        S.push(n)

        for (let x of G[n]) {
            if (V[x] === 0) {
                p = Math.min(p, find_scc(x))
            }
            else if (F[x] === 0) {
                p = Math.min(p, V[x])
            }
        }

        if (p === V[n]) {
            const temp = []

            while (S.length > 0) {
                let out = S.pop()
                F[out] = 1
                temp.push(out)

                if (out === n) {
                    GR.push(temp)
                    break
                }
            }
        }

        return p
    }

    const N = Number(input[0])

    const G = []
    const S = []
    const V = Array(N).fill(0)
    const F = Array(N).fill(0)
    const GR = []
    const MAX = 1000000
    let O = 0


    for (let i = 0; i < N; ++i) {
        G.push([])
    }

    const C = input[1].split(" ").map(Number)

    for (let i = 0; i < N; ++i) {
        const temp = input[i+2].split("")
        for (let j = 0; j < N; ++j) {
            if (temp[j] == "1") {
                G[i].push(j)
            }
        }
    }

    for (let i = 0; i < N; ++i) {
        if (V[i] === 0) {
            find_scc(i)
        }
    }

    let ans = 0
    for (let u of GR) {
        let v = MAX
        for (let i of u) {
            v = Math.min(v, C[i])
        }
        ans += v
    }

    console.log(ans)
})