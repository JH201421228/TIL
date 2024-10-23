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
    const M = Array.from({length: N+1}, () => Array(N).fill(0))
    const cur = [0]
    const S = []
    const V = Array(2*N+1).fill(0)
    const F = Array(2*N+1).fill(0)
    const G = Array.from({length: 2*N+1}, () => [])
    let O = 0
    let cnt = 0
    let s = 0
    let e = N
    let mid = 0

    const connect = t => {
        for (let i = 1; i < N+1; ++i) {
            for (let j = t+1; j < N; ++j) {
                const a = i
                const b = M[i][j]

                if (cur[a] === cur[b]) {
                    G[a].push(2*N+1-b)
                    G[b].push(2*N+1-a)
                    G[2*N+1-b].push(a)
                    G[2*N+1-a].push(b)
                }
                else if ((cur[a] + 1) % 3 === (cur[b] + 2) % 3) {
                    G[a].push(b)
                    G[2*N+1-b].push(2*N+1-a)
                }
                else {
                    G[b].push(a)
                    G[2*N+1-a].push(2*N+1-b)
                }
            }
        }
    }

    const scc = n => {
        let p = V[n] = ++O
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
                out = S.pop()
                F[out] = cnt

                if (out === n) {
                    break
                }
            }
        }

        return p
    }

    for (let i = 0; i < N; ++i) {
        const temp = input[i+1].split(' ').map(Number)

        cur.push(temp[0])

        for (let j = 1; j < N; ++j) {
            M[i+1][j] = temp[j]
        }
    }

    while (s <= e) {
        mid = Math.floor((s+e)/2)
        O = 0
        cnt = 0
        let check = true

        for (let i = 1; i < 2*N+1; ++i) {
            V[i] = 0
            F[i] = 0
            G[i] = []
        }

        connect(mid)

        for (let i = 1; i < 2*N+1; ++i) {
            if (V[i] === 0) {
                scc(i)
            }
        }

        for (let i = 1; i < N+1; ++i) {
            if (F[i] === F[2*N+1-i]) {
                s = mid + 1
                check = false
                break
            }
        }
        if (check) {
            e = mid - 1
        }
    }

    console.log(s)
})