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
    const find = (x) => {
        if (P[x] === x) {
            return x
        }

        P[x] = find(P[x])

        return P[x]
    }

    const union = (a, b) => {
        a = find(a)
        b = find(b)

        if (a > b) {
            P[a] = b
        }
        else {
            P[b] = a
        }
    }

    const N = Number(input[0])
    const X = []
    const Y = []
    const Z = []
    const M = []
    const P = []    
    
    for (let i = 0; i < N; ++i) {
        P.push(i)
    }

    for (let i = 0; i < N; ++i) {
        const temp = input[i+1].split(" ")
        X.push([BigInt(temp[0]), i])
        Y.push([BigInt(temp[1]), i])
        Z.push([BigInt(temp[2]), i])
    }

    X.sort((a, b) => a[0] > b[0] ? 1 : -1)
    Y.sort((a, b) => a[0] > b[0] ? 1 : -1)
    Z.sort((a, b) => a[0] > b[0] ? 1 : -1)
    
    for (let i = 0; i < N-1; ++i) {
        M.push([X[i+1][0] - X[i][0], X[i][1], X[i+1][1]])
        M.push([Y[i+1][0] - Y[i][0], Y[i][1], Y[i+1][1]])
        M.push([Z[i+1][0] - Z[i][0], Z[i][1], Z[i+1][1]])
    }

    M.sort((a, b) => a[0] > b[0] ? 1 : -1)

    ans = 0n
    cnt = 0
    idx = 0

    while (cnt < N-1) {
        const [c, a, b] = M[idx]
        ++idx

        if (find(a) !== find(b)) {
            ans += c
            ++cnt

            union(a, b)
        }
    }

    console.log(ans.toString())
})